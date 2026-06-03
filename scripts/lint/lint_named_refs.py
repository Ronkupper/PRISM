#!/usr/bin/env python3
"""
PRISM named-references linter.

Emits NDJSON findings (one violation per line) under the public lint
catalog rule IDs:

  PRISM-LINT-01  named-refs-resolve         (error)
  PRISM-LINT-02  named-refs-orphan-anchor   (info)

PRISM-LINT-01 consolidates three error-class structural failure modes
under a single rule per the catalog at `lint_rules.md`:

  - broken-ref       — `§{ns.slug}` does not resolve to a defined anchor
  - slug-collision   — duplicate anchor slugs in the same namespace
  - mixed-ref-style  — bare numeric ref `§X.Y` outside the `DD.` namespace

The internal sub-mode is preserved in the `detail` field of each finding
for diagnosability; the outward rule ID is the catalog ID.

Usage:
    python lint_named_refs.py <PRISM.md> [--severities error,warning,info]
                                          [--text]

Default output is NDJSON. `--text` switches to a human-readable line
format. Exit code 0 if no error-severity findings, 1 otherwise.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass, field
from typing import Optional


# ---------------------------------------------------------------------------
# Heading / anchor / ref regexes
# ---------------------------------------------------------------------------

RE_SECTION_HEADING = re.compile(r"^(#{2,4})\s+(\d+(?:\.\d+){0,2})\.?\s+(.+?)\s*$")
RE_APPENDIX_TOP = re.compile(r"^(##)\s+Appendix\s+([A-Z])\s+[—–-]\s+(.+?)\s*$")
RE_APPENDIX_SUB = re.compile(r"^(#{3,4})\s+([A-Z])\.(\d+(?:\.\d+)*)\s+(.+?)\s*$")
RE_APPENDIX_F_SP = re.compile(r"^(#{3,4})\s+(SP-\d+)\b\s*(.*)$")
RE_ANCHOR = re.compile(r'^<a id="([a-z]+)-([a-z0-9][a-z0-9.-]*)"></a>\s*$')

RE_NAMED_REF = re.compile(r"§\{(?P<ns>[a-z]+)\.(?P<slug>[A-Za-z0-9.-]+)\}")
RE_NUMERIC_REF_OUTSIDE_DD = re.compile(r"(?<!DD\.)§(\d+(?:\.\d+)*)")

RE_STABILITY_TAG = re.compile(r"\s*`\[[^`]+\]`\s*$")
RE_EMPHASIS = re.compile(r"\*+([^*]+)\*+")

VALID_NAMESPACES = {
    "section", "appendix", "lens", "principle", "monitor", "probe", "gate",
}


# ---------------------------------------------------------------------------
# Slug derivation (inlined from migrate_named_refs.py to keep this script
# self-contained — the public lint scripts directory does not depend on the
# workshop's migration scripts).
# ---------------------------------------------------------------------------

def _slugify(s: str) -> str:
    s = RE_EMPHASIS.sub(r"\1", s)
    s = s.replace("'", "").replace("\u2019", "")
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


def derive_slug(raw: str) -> str:
    no_tag = RE_STABILITY_TAG.sub("", raw)
    slug = _slugify(no_tag)
    if slug:
        return slug
    return _slugify(raw)


# ---------------------------------------------------------------------------
# Finding / Index data structures
# ---------------------------------------------------------------------------

@dataclass
class Finding:
    rule: str          # "PRISM-LINT-01" | "PRISM-LINT-02"
    alias: str         # "named-refs-resolve" | "named-refs-orphan-anchor"
    severity: str      # "error" | "warning" | "info"
    file: str
    line: int
    message: str
    context: str = ""


@dataclass
class Index:
    anchors: dict[str, set[str]] = field(default_factory=dict)
    section_keys: dict[str, str] = field(default_factory=dict)
    appendix_keys: dict[str, str] = field(default_factory=dict)
    id_inventory: dict[str, set[str]] = field(default_factory=dict)
    definitions: dict[tuple[str, str], int] = field(default_factory=dict)
    references: dict[tuple[str, str], list[int]] = field(default_factory=dict)
    collisions: list[Finding] = field(default_factory=list)


# ---------------------------------------------------------------------------
# Index builder
# ---------------------------------------------------------------------------

def build_index(lines: list[str], path: str) -> Index:
    idx = Index()
    idx.id_inventory = {
        "principle": set(),
        "monitor": set(),
        "probe": set(),
        "gate": set(),
        "lens": set(),
    }

    in_fence = False
    in_appendix_f = False

    for i, line in enumerate(lines):
        line_no = i + 1
        if re.match(r"^```", line):
            in_fence = not in_fence
            continue
        if in_fence:
            ym = re.match(r"^\s*-?\s*id:\s*(LL-[UD]-\d{3})\s*$", line)
            if ym:
                idx.id_inventory["lens"].add(ym.group(1))
            continue

        # Standing-Principle IDs are catalogued one row per SP in the §10.2
        # disposition table; harvest them there so principle.SP-N refs resolve
        # against the canonical SP catalog. This is the v2.9.0 source of truth
        # for principle IDs (the §10/Appendix-F de-dup removed Appendix F, whose
        # `### SP-N` headings the in_appendix_f path below used to harvest; that
        # path is now inert pending the cross-file linter rework).
        tm = re.match(r"^\|\s*(SP-\d+)\s*\|", line)
        if tm:
            idx.id_inventory["principle"].add(tm.group(1))
            continue

        am = RE_APPENDIX_TOP.match(line)
        if am:
            letter = am.group(2)
            title = am.group(3).strip()
            slug = derive_slug(title)
            if letter in idx.appendix_keys:
                idx.collisions.append(Finding(
                    rule="PRISM-LINT-01", alias="named-refs-resolve",
                    severity="error", file=path, line=line_no,
                    message=f"duplicate appendix letter {letter}",
                    context="slug-collision",
                ))
            idx.appendix_keys[letter] = slug
            idx.definitions.setdefault(("appendix", slug), line_no)
            in_appendix_f = (letter == "F")
            continue

        asub = RE_APPENDIX_SUB.match(line)
        if asub:
            letter = asub.group(2)
            num = asub.group(3)
            title = asub.group(4).strip()
            slug = derive_slug(title)
            key = f"{letter}.{num}"
            idx.appendix_keys[key] = slug
            idx.definitions.setdefault(("appendix", slug), line_no)
            continue

        if in_appendix_f:
            fm = RE_APPENDIX_F_SP.match(line)
            if fm:
                sp_id = fm.group(2)
                idx.id_inventory["principle"].add(sp_id)
                idx.definitions.setdefault(("principle", sp_id), line_no)
                continue

        sm = RE_SECTION_HEADING.match(line)
        if sm:
            num = sm.group(2)
            title = sm.group(3).strip()
            slug = derive_slug(title)
            idx.section_keys[num] = slug
            idx.definitions.setdefault(("section", slug), line_no)
            in_appendix_f = False
            for m in re.finditer(r"\b(M\d+|GATE-\d+|P\d+(?:\.\d+)?|SP-\d+)\b", title):
                tok = m.group(1)
                if tok.startswith("SP-"):
                    idx.id_inventory["principle"].add(tok)
                elif tok.startswith("GATE-"):
                    idx.id_inventory["gate"].add(tok)
                elif tok.startswith("M"):
                    idx.id_inventory["monitor"].add(tok)
                elif tok.startswith("P"):
                    idx.id_inventory["probe"].add(tok)
            for m in re.finditer(r"\bProbe\s+(\d+)\b", title):
                idx.id_inventory["probe"].add(f"P{m.group(1)}")
            continue

        an = RE_ANCHOR.match(line)
        if an:
            ns, slug = an.group(1), an.group(2)
            idx.anchors.setdefault(ns, set()).add(slug)
            continue

    return idx


# ---------------------------------------------------------------------------
# Checks
# ---------------------------------------------------------------------------

def check_named_refs(lines: list[str], idx: Index, path: str) -> list[Finding]:
    findings: list[Finding] = []
    in_fence = False
    for i, line in enumerate(lines):
        if re.match(r"^```", line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if re.match(r"^#{1,6}\s", line):
            continue
        for m in RE_NAMED_REF.finditer(line):
            ns = m.group("ns")
            slug = m.group("slug")
            if ns not in VALID_NAMESPACES:
                findings.append(Finding(
                    rule="PRISM-LINT-01", alias="named-refs-resolve",
                    severity="error", file=path, line=i + 1,
                    message=f"unknown namespace '{ns}' in §{{{ns}.{slug}}}",
                    context="broken-ref",
                ))
                continue
            if ns in ("section", "appendix"):
                anchors = idx.anchors.get(ns, set())
                if slug not in anchors:
                    findings.append(Finding(
                        rule="PRISM-LINT-01", alias="named-refs-resolve",
                        severity="error", file=path, line=i + 1,
                        message=f"unresolved §{{{ns}.{slug}}}",
                        context="broken-ref",
                    ))
                else:
                    idx.references.setdefault((ns, slug), []).append(i + 1)
            else:
                inv = idx.id_inventory.get(ns, set())
                resolved = slug in inv
                if not resolved and ns == "probe" and "." in slug:
                    parent = slug.split(".", 1)[0]
                    if parent in inv:
                        resolved = True
                if not resolved:
                    findings.append(Finding(
                        rule="PRISM-LINT-01", alias="named-refs-resolve",
                        severity="error", file=path, line=i + 1,
                        message=f"unresolved §{{{ns}.{slug}}}",
                        context="broken-ref",
                    ))
                else:
                    idx.references.setdefault((ns, slug), []).append(i + 1)
    return findings


def check_mixed_style(lines: list[str], path: str) -> list[Finding]:
    findings: list[Finding] = []
    in_fence = False
    for i, line in enumerate(lines):
        if re.match(r"^```", line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if re.match(r"^#{1,6}\s", line):
            continue
        for m in RE_NUMERIC_REF_OUTSIDE_DD.finditer(line):
            findings.append(Finding(
                rule="PRISM-LINT-01", alias="named-refs-resolve",
                severity="error", file=path, line=i + 1,
                message=f"bare numeric ref §{m.group(1)} (use named form)",
                context="mixed-ref-style",
            ))
    return findings


def check_collisions(idx: Index, path: str) -> list[Finding]:
    findings: list[Finding] = list(idx.collisions)
    by_ns: dict[str, dict[str, list[int]]] = {}
    for (ns, slug), line in idx.definitions.items():
        by_ns.setdefault(ns, {}).setdefault(slug, []).append(line)
    for ns, slugs in by_ns.items():
        for slug, lns in slugs.items():
            if len(lns) > 1:
                findings.append(Finding(
                    rule="PRISM-LINT-01", alias="named-refs-resolve",
                    severity="error", file=path, line=lns[0],
                    message=f"slug collision ns={ns} slug={slug} lines={lns}",
                    context="slug-collision",
                ))
    return findings


def check_orphans(idx: Index, path: str) -> list[Finding]:
    findings: list[Finding] = []
    for (ns, slug), line in idx.definitions.items():
        if ns not in ("section", "appendix"):
            continue
        if (ns, slug) in idx.references:
            continue
        findings.append(Finding(
            rule="PRISM-LINT-02", alias="named-refs-orphan-anchor",
            severity="info", file=path, line=line,
            message=f"orphan {ns} '{slug}' (never referenced)",
            context="orphan-anchor",
        ))
    return findings


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="Lint PRISM.md named cross-references.")
    ap.add_argument("path", help="Path to PRISM.md")
    ap.add_argument(
        "--severities",
        default="error,warning,info",
        help="Comma-separated severities to emit (default: all).",
    )
    ap.add_argument(
        "--text",
        action="store_true",
        help="Emit human-readable text rather than NDJSON.",
    )
    args = ap.parse_args(argv)

    with open(args.path, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    idx = build_index(lines, args.path)
    findings: list[Finding] = []
    findings.extend(check_named_refs(lines, idx, args.path))
    findings.extend(check_mixed_style(lines, args.path))
    findings.extend(check_collisions(idx, args.path))
    findings.extend(check_orphans(idx, args.path))

    findings.sort(key=lambda f_: (f_.rule, f_.line))

    sev_filter = {s.strip() for s in args.severities.split(",") if s.strip()}
    emitted = [f_ for f_ in findings if f_.severity in sev_filter]

    if args.text:
        for f_ in emitted:
            print(f"{f_.rule} {f_.severity} {f_.file}:{f_.line} {f_.message}"
                  + (f" [{f_.context}]" if f_.context else ""))
    else:
        for f_ in emitted:
            print(json.dumps(asdict(f_), ensure_ascii=False))

    err = sum(1 for f_ in findings if f_.severity == "error")
    info = sum(1 for f_ in findings if f_.severity == "info")
    print(f"Summary: {err} error, {info} info", file=sys.stderr)

    return 1 if err else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
