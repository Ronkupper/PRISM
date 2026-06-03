#!/usr/bin/env python3
"""
PRISM cross-file named-reference linter (v2.9.0 Skill archive).

The single-file linter (lint_named_refs.py) gates the assembled PRISM.md. After
the decomposition, named refs cross files: the lean core (PRISM_core.md) points
into on-demand bundles (reference/*.md) and the standalone lens
(lens/PRISM_lens_library.md). This linter resolves refs across the whole archive
by building ONE union index over all manifest files, then running the same
PRISM-LINT-01/02 checks against it.

Design (DD D4): build_index per file → union the anchors / id-inventory /
definitions (with file provenance) → resolve every file's refs against the union
→ orphan-detect against the union (so a core anchor referenced only from a bundle
is not a false orphan) → flag any slug defined in two files (cross-file collision).
A ref whose target lives in a bundle absent from the manifest surfaces naturally
as a broken-ref error (its anchor is simply not in the union).

Reuses lint_named_refs.py wholesale — same rule IDs, severities, and NDJSON shape.
Exit 0 iff no error-severity findings.

Usage:
    python lint_cross_file_refs.py <file1.md> <file2.md> ...   [--text]
    python lint_cross_file_refs.py --manifest <file-of-paths>  [--text]
"""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lint_named_refs import (  # noqa: E402
    Finding, Index, build_index,
    check_named_refs, check_mixed_style, check_collisions, check_orphans,
)


def union_index(per_file: list[tuple[str, Index]]) -> Index:
    u = Index()
    u.id_inventory = {}
    prov: dict[tuple[str, str], list[tuple[str, int]]] = {}
    for fname, idx in per_file:
        for ns, s in idx.anchors.items():
            u.anchors.setdefault(ns, set()).update(s)
        for ns, s in idx.id_inventory.items():
            u.id_inventory.setdefault(ns, set()).update(s)
        for (ns, slug), line in idx.definitions.items():
            prov.setdefault((ns, slug), []).append((fname, line))
            u.definitions.setdefault((ns, slug), line)
        u.collisions.extend(idx.collisions)
    # cross-file collision: same (ns, slug) defined in more than one file
    for (ns, slug), locs in prov.items():
        files = sorted({f for f, _ in locs})
        if len(files) > 1:
            u.collisions.append(Finding(
                rule="PRISM-LINT-01", alias="named-refs-resolve", severity="error",
                file=files[0], line=locs[0][1],
                message=f"cross-file slug collision ns={ns} slug={slug} in {files}",
                context="slug-collision",
            ))
    return u


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="Lint PRISM Skill-archive cross-file named refs.")
    ap.add_argument("paths", nargs="*", help="Manifest files (core + bundles + lens).")
    ap.add_argument("--manifest", help="File listing one path per line.")
    ap.add_argument("--severities", default="error,warning,info")
    ap.add_argument("--text", action="store_true")
    args = ap.parse_args(argv)

    files = list(args.paths)
    if args.manifest:
        files += [ln.strip() for ln in Path(args.manifest).read_text().splitlines()
                  if ln.strip() and not ln.strip().startswith("#")]
    if not files:
        ap.error("no manifest files given")

    loaded = [(f, Path(f).read_text(encoding="utf-8").splitlines()) for f in files]
    per_file = [(f, build_index(lines, f)) for f, lines in loaded]
    union = union_index(per_file)

    findings: list[Finding] = []
    for (f, lines), (_, idx) in zip(loaded, per_file):
        findings.extend(check_named_refs(lines, union, f))   # resolve against the union
        findings.extend(check_mixed_style(lines, f))         # per-file (bare numeric)
        findings.extend(check_collisions(idx, f))            # within-file collisions
    findings.extend(c for c in union.collisions)             # cross-file collisions
    findings.extend(check_orphans(union, "archive"))         # orphans over the union

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
