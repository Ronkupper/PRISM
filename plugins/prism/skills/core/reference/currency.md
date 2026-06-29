<!-- PRISM v2.21.0 Skill bundle (on-demand reference). Currency reference (sections 7.5-7.6 + 18.3) — point-refresh, the Update session, and the session-open currency check. Fetch for an Update session or when the currency-check-at-open fires.
     Generated from the assembled PRISM.md — edit PRISM.md, not this. -->

### 7.5 Currency maintenance — point refresh `[methodological | stable]`
<a id="section-currency-maintenance-point-refresh"></a>

Two-tier mechanism: point refresh (per-project, in Setup) + Update session
(standalone, rare, operator-gated, §{section.currency-maintenance-update-session}).

**Point refresh.**

- **Trigger.** Probe 1 evaluation extends to citation currency. For each
  lens with `rubric_anchor:` set:
  - If `verification_basis:` is `schema-introduction-only`: the
    `last_verified:` date does not establish currency; disposition is
    `unverified-anchor` regardless of date age. Orchestration runs a
    web-search currency check and refreshes the citation in the Prompt
    Strategy (the canonical Library file is *not* modified). This gates
    every other clause below.
  - Else if `last_verified:` is within 6 months: disposition includes
    `fresh`. No flag.
  - Else if `last_verified:` is 6–12 months old: disposition includes
    `stale-refresh`. Orchestration runs a web-search currency check and
    refreshes the citation in the Prompt Strategy (the canonical Library
    file is *not* modified).
  - Else if `last_verified:` is > 12 months old: disposition includes
    `stale-accumulating`. Same inline refresh, but advisory signal
    accumulates toward an Update session (per §{section.currency-maintenance-update-session}).
- **Output.** Probe 1 output includes per-anchored-entry currency
  disposition.
- **Inline refresh format.** The refreshed citation appears in the Prompt
  Strategy with provenance:
  ```
  P3.4 — accessibility pass
  Specialist framing: WCAG-qualified accessibility auditor (§{lens.LL-D-002} "Can anyone use?")
  Anchor: WCAG 2.2 (October 2023) — verified current as of [date]
          via web search; PRISM Lens Library v0.16 last_verified
          2026-04-24 still current.
  ```
  If the web-search currency check finds a newer version (e.g., WCAG 3.0
  published):
  ```
  Anchor: WCAG 2.2 (October 2023). Note: WCAG 3.0 published [date];
          considered for use; chose WCAG 2.2 because [rationale —
          subject's commitment, regulatory pin, etc.] OR
          updating to 3.0 because [rationale].
  ```
- **No silent modification of Library.** Library file is read-only at
  point-refresh time.

### 7.6 Currency maintenance — Update session `[methodological | stable]`
<a id="section-currency-maintenance-update-session"></a>

Standalone session, rarely run, operator-gated. PRISM-file-in /
PRISM-file-out contract.

**When.**

- Triggered by point-refresh advisory signal accumulation (count of
  `stale-accumulating` over time + count of `informed_by:` framework
  changes seen across sessions).
- Operator decision; framework recommends in *What's next* when signal
  exceeds threshold (rev. 1 draft threshold: 3 stale-pattern accumulations
  across 6+ months).
- Operator can also run on demand at any time.

**Mechanic.**

1. Operator opens fresh orchestration session.
2. Attaches: PRISM v2 framework, current Lens Library, possibly other
   reference frameworks pertinent to anchor checks.
3. Operator declares: `Run Update session against Lens Library [version].`
4. Orchestration's Update routine:
   - Walks each entry with `rubric_anchor:`. Web-searches current state of
     the external spec. Records currency.
   - Walks each entry's `informed_by:` list. Web-searches major framework
     updates since `last_verified:`. Records changes.
   - Produces a delta document: per-entry currency status, recommended
     `last_verified:` date updates, recommended citation text updates.
   - Does *not* modify entry IDs, schema, tier composition, or
     `informed_by:` provenance lineage. Architectural changes are flagged,
     not made inline.
5. Operator reviews delta document.
6. Orchestration applies approved deltas to a new Library file (e.g.,
   `PRISM_lens_library_v0_9_1.md`).
7. Operator reviews, ratifies, and ships the new Library.

**Resilient to partial source-access failure.** When a web-search currency
check fails (gated source, paywall, expired URL), Update routine records
`currency-check-failed` for that anchor and proceeds. Operator decides
whether to escalate.

**Library versioning rides PRISM's own.** Library version increments are
minor patches (v0.9 → v0.9.1) unless schema changes (in which case
major-bump and architectural review).

**Library changelog lives inside Library file.** Update session appends to
it.

**Not architectural drift.** Schema/tier/composition changes are
out-of-scope for Update sessions and produce flag-don't-fix outputs.
Architectural changes go through a fresh Library design cycle, not an
Update session.

---

### 18.3 Currency check at session open `[methodological | stable]`
<a id="section-currency-check-at-session-open"></a>

At orchestration session open, when the substrate supports web access,
orchestration **may** check the framework and Lens version stamps against
the attached versions and surface any newer-version finding as a soft
flag in *What's next* under the *Operator next* surface. The check is
opportunistic, not mandatory: substrates without web access skip it; a
failed check is not an error.

**Mechanics.**

1. Read the framework core's version (its header) and the bundled
   Lens Library version (`lens/PRISM_lens_library.md` header).
2. If web access is available, GET the two `VERSION` endpoints from the
   repository's `main` branch. The endpoints return one line each.
3. Compare. If the published version is greater than the attached
   version on either track, surface a soft flag:
   `Framework v2.21.0 attached; v{published} available at {releases URL}.`
   `Lens v0.16 attached; v{published} available at {releases URL}.`
4. The flag is informational. The operator decides whether to upgrade
   between sessions. PRISM does not silently swap attached files at
   runtime.

**Why this is in the framework.** The repository is the framework's
source of truth for currency. Putting the URLs and the check protocol
in the framework body means the file carries its own discoverability
instead of relying on the operator to remember the project URL. It also
addresses the `informed_by` chain: a Lens anchor (e.g., WCAG 2.2) can
move; the Lens Library evolves; the framework evolves; and operators
working from a saved attachment have an explicit, in-file path back to
the latest.
