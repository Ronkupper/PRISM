#!/usr/bin/env python3
"""
PRISM package-integrity linter.

The named-refs linters (`lint_named_refs.py`, `lint_cross_file_refs.py`) gate the
framework *prose* — the assembled `PRISM.md` and the split Skill archive. This
linter gates the installable *package* — the surface a user actually installs —
under new public catalog IDs:

  PRISM-LINT-10  package-frontmatter-parses   (error)
                 Every shipped SKILL.md and command .md has well-formed YAML
                 frontmatter (the leading `---` … `---` block parses). Runs
                 unconditionally — no external schema needed — so it cannot be
                 silently skipped the way the schema-fetch step can.
  PRISM-LINT-11  command-metadata-types       (error)
                 Command frontmatter field types match the Claude Code schema:
                 `description` is a non-empty string; `argument-hint` (if present)
                 is a string, NOT a YAML list; `disable-model-invocation` (if
                 present) is a boolean.
  PRISM-LINT-12  manifest-json-valid          (error)
                 plugin.json and marketplace.json parse as JSON.
  PRISM-LINT-13  version-consistency          (error)
                 VERSION == plugin.json `version` == marketplace plugin `version`.

Usage:
    python lint_package.py [--root DIR] [--severities error,warning,info] [--text]

Default output is NDJSON (one finding per line), same shape as the other PRISM
linters. Exit code 0 iff no error-severity findings, 1 otherwise.
"""
from __future__ import annotations

import argparse
import glob
import json
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    print(json.dumps({
        "rule": "PRISM-LINT-10", "alias": "package-frontmatter-parses",
        "severity": "error", "file": "(environment)", "line": 0,
        "message": "PyYAML not installed; cannot validate frontmatter",
        "context": "missing-dep",
    }))
    raise SystemExit(1)


@dataclass
class Finding:
    rule: str
    alias: str
    severity: str
    file: str
    line: int
    message: str
    context: str = ""


def _rel(root: Path, p: Path) -> str:
    try:
        return str(p.relative_to(root))
    except ValueError:
        return str(p)


def _split_frontmatter(text: str):
    """Return frontmatter text (between the first two `---` lines) or None."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return "\n".join(lines[1:i])
    return None


def check_frontmatter(files, root) -> list:
    findings = []
    for p in files:
        text = Path(p).read_text(encoding="utf-8")
        rel = _rel(root, Path(p))
        fm = _split_frontmatter(text)
        if fm is None:
            findings.append(Finding(
                "PRISM-LINT-10", "package-frontmatter-parses", "error", rel, 1,
                "no YAML frontmatter block (expected leading '---' … '---')",
                "no-frontmatter"))
            continue
        try:
            data = yaml.safe_load(fm)
        except yaml.YAMLError as e:
            line = 1
            mark = getattr(e, "problem_mark", None)
            if mark is not None:
                line = mark.line + 2  # +1 for opening '---', +1 to 1-index
            findings.append(Finding(
                "PRISM-LINT-10", "package-frontmatter-parses", "error", rel, line,
                f"YAML frontmatter does not parse: {str(e).splitlines()[0]}",
                "parse-error"))
            continue
        if not isinstance(data, dict):
            findings.append(Finding(
                "PRISM-LINT-10", "package-frontmatter-parses", "error", rel, 2,
                "frontmatter is not a mapping", "not-a-mapping"))
    return findings


def check_command_types(cmd_files, root) -> list:
    findings = []
    for p in cmd_files:
        fm = _split_frontmatter(Path(p).read_text(encoding="utf-8"))
        if fm is None:
            continue  # LINT-10 owns missing frontmatter
        try:
            data = yaml.safe_load(fm)
        except yaml.YAMLError:
            continue  # LINT-10 owns parse errors
        if not isinstance(data, dict):
            continue
        rel = _rel(root, Path(p))
        desc = data.get("description")
        if not isinstance(desc, str) or not desc.strip():
            findings.append(Finding(
                "PRISM-LINT-11", "command-metadata-types", "error", rel, 2,
                "`description` must be a non-empty string", "description-type"))
        if "argument-hint" in data and not isinstance(data["argument-hint"], str):
            got = type(data["argument-hint"]).__name__
            findings.append(Finding(
                "PRISM-LINT-11", "command-metadata-types", "error", rel, 2,
                f"`argument-hint` must be a quoted string, parsed as YAML {got} "
                "(quote it: argument-hint: \"[...]\")", "argument-hint-type"))
        if "disable-model-invocation" in data and not isinstance(
                data["disable-model-invocation"], bool):
            findings.append(Finding(
                "PRISM-LINT-11", "command-metadata-types", "error", rel, 2,
                "`disable-model-invocation` must be a boolean", "dmi-type"))
    return findings


def check_manifests(root):
    """Return (findings, {'plugin': dict|None, 'marketplace': dict|None})."""
    findings = []
    parsed = {"plugin": None, "marketplace": None}
    targets = {
        "plugin": root / "plugins/prism/.claude-plugin/plugin.json",
        "marketplace": root / ".claude-plugin/marketplace.json",
    }
    for key, p in targets.items():
        if not p.exists():
            findings.append(Finding(
                "PRISM-LINT-12", "manifest-json-valid", "error",
                _rel(root, p), 1, "manifest file missing", "missing"))
            continue
        try:
            parsed[key] = json.loads(p.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            findings.append(Finding(
                "PRISM-LINT-12", "manifest-json-valid", "error",
                _rel(root, p), getattr(e, "lineno", 1),
                f"invalid JSON: {e.msg}", "json-parse"))
    return findings, parsed


def check_version_consistency(root, parsed) -> list:
    findings = []
    vp = root / "VERSION"
    if not vp.exists():
        return [Finding("PRISM-LINT-13", "version-consistency", "error",
                        "VERSION", 1, "VERSION file missing", "missing")]
    version = vp.read_text(encoding="utf-8").strip()
    plugin, market = parsed.get("plugin"), parsed.get("marketplace")
    if plugin is None or market is None:
        return findings  # LINT-12 already flagged the unparseable manifest
    pj = _rel(root, root / "plugins/prism/.claude-plugin/plugin.json")
    mk = _rel(root, root / ".claude-plugin/marketplace.json")
    if plugin.get("version") != version:
        findings.append(Finding(
            "PRISM-LINT-13", "version-consistency", "error", pj, 1,
            f"plugin.json version {plugin.get('version')!r} != VERSION {version!r}",
            "plugin-vs-version"))
    entry = next((e for e in market.get("plugins", [])
                  if e.get("name") == plugin.get("name")), None)
    if entry is None:
        findings.append(Finding(
            "PRISM-LINT-13", "version-consistency", "error", mk, 1,
            f"marketplace has no plugin entry named {plugin.get('name')!r}",
            "no-entry"))
    elif entry.get("version") != version:
        findings.append(Finding(
            "PRISM-LINT-13", "version-consistency", "error", mk, 1,
            f"marketplace plugin version {entry.get('version')!r} != VERSION "
            f"{version!r}", "marketplace-vs-version"))
    return findings


def main(argv) -> int:
    ap = argparse.ArgumentParser(description="Lint the installable PRISM package.")
    ap.add_argument("--root", default=".", help="Repo root (default: cwd).")
    ap.add_argument("--severities", default="error,warning,info")
    ap.add_argument("--text", action="store_true")
    args = ap.parse_args(argv)
    root = Path(args.root).resolve()

    skill_files = []
    if (root / "SKILL.md").exists():
        skill_files.append(str(root / "SKILL.md"))
    skill_files += sorted(glob.glob(
        str(root / "plugins/prism/skills/**/SKILL.md"), recursive=True))
    cmd_files = sorted(glob.glob(str(root / "plugins/prism/commands/*.md")))

    findings = []
    findings += check_frontmatter(skill_files + cmd_files, root)
    findings += check_command_types(cmd_files, root)
    mf, parsed = check_manifests(root)
    findings += mf
    findings += check_version_consistency(root, parsed)

    findings.sort(key=lambda x: (x.rule, x.file, x.line))
    sev = {s.strip() for s in args.severities.split(",") if s.strip()}
    emitted = [x for x in findings if x.severity in sev]

    if args.text:
        for x in emitted:
            print(f"{x.rule} {x.severity} {x.file}:{x.line} {x.message}"
                  + (f" [{x.context}]" if x.context else ""))
    else:
        for x in emitted:
            print(json.dumps(asdict(x), ensure_ascii=False))

    return 1 if any(x.severity == "error" for x in findings) else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
