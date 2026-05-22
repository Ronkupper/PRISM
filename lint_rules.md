# PRISM lint catalog

**Catalog version:** 1

This file is the contributor-facing reference catalog of lint rules
enforced against `PRISM.md` by the workflow at `.github/workflows/lint.yml`.
Each rule has a stable ID (`PRISM-LINT-NN`), a stable alias, a severity,
and a one-paragraph description.

## Preamble — when a constraint lives here vs. in `PRISM.md`

The PRISM lint catalog enforces what tooling can verify mechanically.
Where a constraint requires operator judgment, it lives in `PRISM.md`
prose; where it can be checked deterministically, the catalog is the
canonical statement.

Lint rules and prose injunctions are mutually exclusive expressions of
the same intent: the catalog grows when prose injunctions become
mechanically checkable, and prose loses redundant restatements when
their lint rule lands. This placement principle sits one level below
PRISM's earn-your-seat filter — it is a *placement* rule, not a *content*
rule. The catalog is intentionally small and slow-growing.

## Severity tiers

- **error** — blocks merge in CI. Structural integrity is broken if this
  fires (refs don't resolve; schema invalid; versions mismatch).
- **warning** — surfaces in CI annotations; does not block merge. Drift
  signal that needs attention but is not necessarily wrong.
- **info** — surfaces only when explicitly requested (e.g., a separate
  workflow job); does not annotate PRs by default. Hygiene observations.

## Catalog

### `PRISM-LINT-01` / `named-refs-resolve` — error

Every `§{namespace.slug}` cross-reference in `PRISM.md` resolves to a
defined anchor. Implementation also surfaces three error-class structural
issues under this rule because they are all forms of named-reference
resolution failure: unresolved refs (broken-ref), duplicate anchor slugs
in the same namespace (slug-collision), and bare numeric refs outside the
`DD.` namespace (mixed-ref-style, post-migration residue).

Implemented by `scripts/lint/lint_named_refs.py`.

### `PRISM-LINT-02` / `named-refs-orphan-anchor` — info

A `<a id="ns-slug"></a>` anchor is defined in `PRISM.md` but no
`§{ns.slug}` reference resolves to it. Many appendix subsection anchors
are deliberately defined as index entries without inbound prose refs;
that pattern is acceptable and produces info-level findings rather than
warnings.

Implemented by `scripts/lint/lint_named_refs.py`.

### `PRISM-LINT-03` / `frontmatter-schema-valid` — error  *(reserved — gated on Pattern A)*

`PRISM.md`'s YAML frontmatter validates against
`PRISM-workshop/schemas/prism_frontmatter.schema.json` via the Python
`check-jsonschema` validator. Pattern A's frontmatter shape (machine-
readable framework metadata: `version`, `released`, `supersedes`,
`lens_library_embedded`, `substrate_target`, `normativity`,
`lint_catalog_version`) is the validation target.

**Status at catalog v1:** reserved slot. Activates when Pattern A ships.

### `PRISM-LINT-04` / `version-title-match` — error  *(reserved — gated on Pattern A)*

The version string in the title block (`# PRISM v{X.Y.Z} — Framework
operating document`) matches the frontmatter `version` field. Mismatch is
a CI-blocking error because the title-block is the human-readable mirror
of the canonical machine-readable `version`.

**Status at catalog v1:** reserved slot. Activates when Pattern A ships.

### `PRISM-LINT-05` / `lens-library-version-match` — warning  *(reserved — gated on Pattern A)*

Frontmatter `lens_library_embedded` matches the embedded Lens Library's
own `Version:` line inside Appendix G. Warning rather than error because
in-between Lens-Library bumps and PRISM-MINOR bumps create transient
drift that the framework handles via M2 (Version Drift) at runtime
rather than at lint time.

**Status at catalog v1:** reserved slot. Activates when Pattern A ships.

### `PRISM-LINT-06` / `element-marking-completeness` — info  *(reserved — gated on Pattern B Phase B1)*

Every Standing Principle, Monitor, Gate, and Probe heading in `PRISM.md`
carries a parseable decision-tag block (`[durability | review-trigger]`
plus optional strength and polarity tokens). Info-severity initially
because Pattern B's Phase B1 ships frontmatter and new-element shape
only; legacy elements remain unmarked until Phase B2 completes the
sweep. Severity may promote to warning after Phase B2 ships.

**Status at catalog v1:** reserved slot. Activates when Pattern B Phase
B1 ships.

### `PRISM-LINT-07` / `description-version-match` — error  *(reserved — gated on Pattern A)*

The substring `Currently v{X.Y.Z}` inside frontmatter `description`
matches frontmatter `version`. Closes the third location in `PRISM.md`
where a version string lives (the others: frontmatter `version` and the
title-block heading — both checked by `PRISM-LINT-04`). Skill-loader
description copy is operator-facing and version-bound.

**Status at catalog v1:** reserved slot. Activates when Pattern A ships.

## Output format

All lint scripts emit NDJSON (newline-delimited JSON), one violation per
line:

```json
{"rule": "PRISM-LINT-01", "alias": "named-refs-resolve", "severity": "error", "file": "PRISM.md", "line": 1234, "message": "Reference §{section.foo} does not resolve", "context": ""}
```

The workflow at `.github/workflows/lint.yml` translates NDJSON into
GitHub's `::error file=...,line=...::message` and `::warning ...::`
annotations.

## Catalog versioning

`lint_catalog_version` in `PRISM.md` frontmatter is a monotonic integer
(1, 2, 3, …); not semver. The catalog isn't a public API with consumers
beyond CI. The integer bumps when the catalog's surface changes
meaningfully (rule added; severity changed; rule removed).

| Catalog version | Active rules | Reserved rules |
|---|---|---|
| 1 | `LINT-01`, `LINT-02` | `LINT-03`, `LINT-04`, `LINT-05`, `LINT-06`, `LINT-07` |
