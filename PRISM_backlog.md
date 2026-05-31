# PRISM Backlog

**Version:** 16
**Maintained by:** Ron Kuper + Claude
**Purpose:** Capture ideas, proposals, and deferred items for future PRISM versions. Separate from PRISM.md because backlog items are proposals, not in-force rules — keeping them out of PRISM.md preserves the "everything in PRISM.md is canonical" property.

---

## How to use this file

Attach this file to planning/workshop sessions where PRISM evolution is being discussed. Do not attach it to regular PRISM project sessions — it's not canonical and would add noise.

When an item promotes to a version, move it from **Accepted for next version** into PRISM.md's Version History, and delete it from this file (or move to **Shipped** with the version number, if a record of the backlog lineage is useful).

When an item is declined, move it to **Declined** with rationale — prevents re-litigating the same idea across cycles.

---

## Structure

- **Active proposals** — being workshopped, no decision yet
- **Accepted for next version** — committed to a specific version, not yet built
- **Deferred** — considered, held for later with rationale
- **Declined** — considered, rejected with rationale
- **Shipped** — optional historical record of which backlog items made it into which version

---

## Active proposals

### Contribution channel for cross-vendor adaptations

**Triggered by:** v1.10.1's compatibility notice. The user-facing invitation ("ask your LLM of choice to adapt the Claude-specific machinery... we'd love to get your upgrade. Share what you built, tell us what broke, send patches back.") promises a destination that doesn't yet exist.

**The gap:** A non-Claude user who takes the invitation seriously and produces a working GPT or Gemini port has nowhere obvious to send it. "PRISM grows through the projects that feed it" is vibes-accurate but infrastructure-absent. Before the first real contribution lands and asks "where do I send this?", PRISM should have a channel ready.

**Options to consider (not decided):**
- **GitHub repo (public)** with CONTRIBUTING.md and issue/PR templates — the expected pattern for open-source, but adds maintenance overhead (watching issues, triaging PRs, responding to questions)
- **Dedicated email address** — lowest overhead, but contributions are private by default; hard to surface them to future users who'd benefit
- **Gist registry** — a single index Gist pointing to community-published adaptations, each hosted wherever the contributor prefers. Lightweight on the maintainer side, handles the read-side well
- **Discord / community space** — social and responsive, but conversations fragment over time; no durable record without extra curation

**Urgency:** Not blocking. v1.10.1 shipped with the invitation and is usable as-is. Becomes time-sensitive when the first actual contribution arrives with nowhere to go — answering "thanks, can you send it to... uh..." would be a worse experience than having said nothing at all in the invitation.

**Likely resolution:** a future version (v1.10.2 patch or v1.11 minor, depending on whether the channel itself requires any framework-side changes) adds a **Contributing** subsection to PRISM.md pointing to the chosen channel. The invitation text in the v1.10.1 compatibility notice stays as-is; it just gains a concrete pointer. Also worth: a section in the Starter's README template for projects to optionally credit community adaptations they used.

**User commitment:** "I would like to do that at some point near future" — v1.10.1 build session, Apr 2026.

**Note:** Appendix H — Vendor parsing observations (shipped in v2.1.0) provides one of the maintenance surfaces this channel will feed into. Cross-vendor adaptation contributions either add new H3 sections (new content types) or new rows in existing tables (new vendor observations for an existing content type). Once the channel itself lands, the appendix is one of the documented destinations.

---

### Cowork execution mode (`cowork` orchestration surface)

*(Active proposal — promotion gate cleared in v2.4.0; this is the `cowork` orchestration-surface value plus its capability set (PRISM.md §3.5.2, the Cowork capability surface). Build pending; the prose-adaptation layer is gated on the orthodox baseline run. The reserved `agentic_orchestration` token was retired in v2.4.0 and re-homed to the `auto_drive` execution driver.)*

---

### Claude Plugins integration (native)

*(Active proposal — unchanged.)*

---

### Multi-vendor skills/plugins ecosystems

*(Active proposal — unchanged.)*

---

## Accepted for next version

*(none currently — v1.9 foundation items shipped; see Shipped.)*

---

## Deferred

*(none currently)*

---

## Declined

### Timer on ask_user_input with auto-advance to default

**Proposed:** In workshop, user initially suggested a timer with high-confidence defaults auto-advancing on timeout.

**Declined because:** Inverts PRISM's core ethos. SP-5 ("no heuristic guessing on ambiguous input"), the full-decline flag rule, and the general stance of "flag, don't assume" all require explicit user input on decisions. A timer makes silence a decision — the user not tapping becomes the user consenting to the default. PRISM's "Keep all defaults" shortcut solves the same convenience problem (one tap for the common path) without conceding the principle.

Codified as SP-9 in v1.9.

---

### Named-vendor recommendations in PRISM.md

**Proposed:** Embed specific vendor recommendations in the framework file ("use Gemini Pro for Deep Research, Perplexity for Fact Check").

**Declined because:** Vendor strengths drift on a 6-12 month timescale; the framework file is meant to outlive specific vendor capabilities. Named-vendor recommendations would force frequent patch bumps just to stay current, and would be wrong more often than right.

**Resolution:** Role-based recommendations in PRISM.md ("use a vendor with strong multi-document synthesis for DR"), with vendor-to-role mapping kept as a separate, shorter-lived reference. Adopted in v1.9.

---

### Per-prompt thinking-depth matrix

**Proposed:** A matrix in PRISM.md specifying which prompts benefit from extended thinking ("Red Team → extended thinking; Layer 2 → extended thinking + Deep Research").

**Declined because:** Claude.ai now exposes Adaptive Thinking as a platform-level flag that decides per-turn whether to think deeply. A framework-level matrix would be redundant at best, wrong at worst — the model itself is making the same decision with more information than the framework has.

**Resolution:** Adaptive Thinking recommended on at Setup as a single flag. No per-prompt thinking-depth column in the execution envelope. Adopted in v1.9.

---

## Shipped

### Repo-backed PRISM mode (v2.5.0)

**Shipped on:** `main` of `Ronkupper/PRISM`, 2026-05-31. Tag `v2.5.0` (mechanics build), with same-day clarifying PATCHes v2.5.1 (execution-return persistence) and v2.5.2 (operator-input persistence).

**What landed.** The build for the persistence axis's `repo_backed` value (value + contract were fixed in v2.4.0's three-axis modes model). New §3.5.3 mechanics: 6-step Setup flow, Claude-as-committer model (operator-as-committer fallback), operator-side PAT hygiene, 8-section engagement-SI skeleton; §3.4 extended with the repo-resident *What's next* variant. MINOR — default `ephemeral` cell and the triple contract untouched.

**Lineage.** Promotion gate cleared by the modes-architecture decision (v2.4.0), which reframed this from a standalone "mode" into the `repo_backed` value on the persistence axis. Provenance: `PRISM-workshop/design/backlog_sequencing_dd_rev1.md` (2026-05-31 amendments). Was an Active proposal in this file; moved here on ship.

---

### Tooling-conventions Pattern B Phase B2 — legacy element marking sweep (v2.2.0)

**Shipped on:** `main` of `Ronkupper/PRISM`, 2026-05-30. Tag `v2.2.0`.

**What landed.** The retroactive Pattern B sweep: ratified strength × polarity normativity markers applied to all 32 in-scope legacy elements (13 Standing Principles excluding retired SP-11, 12 Monitors, 7 Probes; no Gate elements survive the v2 dissolution). Markup-only — zero body-text change. Released as MINOR (purely additive metadata on existing headings).

- **Distribution:** 28 elements carry a polarity glyph at default strength (three-token form); SP-6 carries the four-token form with non-default strength `recommended`; 3 elements are detection-only / no-glyph (SP-3, M5, M9) and retain the two-token form.
- **Operator calls.** SP-3 ratified Option 1 — retains its numbering slot with the two-token `[operator-scaffolding | stable]` form (renumber-and-remove declined on citation-stability grounds; a v3.0.0 candidate). M5 ratified detection-only — an override of the proposals-doc `⚠️` lean, on the B2 worked-example principle that M5's four-band behavior (silent / advisory / active / directive) would be distorted by any single polarity glyph.
- **App F retrospective headings** received the marker alongside the §10 numbered headings, per the proposals doc's "every listed location" instruction.

**Pre-flight.** Lint 0 errors / 0 warnings / 56 info-level orphans — identical to the v2.1.1 baseline (§1.1/§1.2 anchor rename swapped one orphan for another, net unchanged). Idempotent transformation (second pass produces no diff). SP-15 (added in v2.1.1, after the proposals doc) deliberately left untouched at both its §10.1.6 and Appendix F locations. Customer-name leak-class sweep clean on every public-surface artifact.

**Provenance.** `PRISM-workshop/handoffs/tooling_conventions_pattern_b_phase_b2_build.md` (ratified marker set, rev1, 2026-05-23); proposals at `PRISM-workshop/notes/pattern_b_legacy_marker_proposals.md`; vocabulary at `PRISM-workshop/design/tooling_conventions_micro_dds_rev1.md` B1–B6. Transformation scripts `PRISM-workshop/scripts/apply_phase_b2_markers.py` + `bump_v220_version_strings.py`.

**Downstream.** `PRISM-LINT-06 / element-marking-completeness` remains at `info` — promotion to `warning` is a separate decision after operators live with the marked file.

---

### Release-hygiene patch — SP-15 + §1.1 framing + Prompt-digest semantics (v2.1.1)

**Shipped on:** `main` of `Ronkupper/PRISM`, 2026-05-23. Tag `v2.1.1`.

**What landed.** Three release-hygiene surfaces, bundled as a PATCH over v2.1.0:

- **SP-15 — Triangulation integrity** added at §10.1.6 (with carryforward-catalog row in §10.2, full text in Appendix F, and an inline cross-ref at the top of §4.3 Vendor Triangulation). Codifies the Vendor Triangulation premise as adversarial-not-parallel and names two corollaries: single-vendor multi-agent fan-out is not falsifier-grade triangulation (equivalence dispatch requires distinct vendors); self-triangulation carries no asymmetric weighting (convergence remains mechanical when the orchestration vendor is also a triangulated execution vendor).
- **§1.1 framing line tightened.** `(orchestration on Claude; execution on any vendor)` → `(orchestration on Claude; execution on selected vendor per Vendor Selection)`. Removes the read-prone summary phrase that compressed-attention readers had been misreading as Claude-exclusion (§4.5's default-stance correction sits 900 lines downstream).
- **Prompt-digest semantics rewrite.** §3.2.3 field-semantics bullet now leads with purpose ("detects wrong-prompt / wrong-attachment delivery at dispatch boundaries") before mechanism, and adds the explicit anti-pattern callout *Generating the digest at return time provides zero integrity check — there is nothing to compare against.* §3.2.1 Envelope-template token inverted to `[orchestration-generated at dispatch; copy verbatim; never recomputed]`, so the counter-signal sits inside the template itself rather than in detail-section prose downstream.

**Housekeeping.** §1.1 and §1.2 anchors and headings rebumped to v2.1.1 per release-pin convention; one cross-ref in Appendix C updated. All version-touching surfaces (frontmatter, EOF marker, §18.x, snapshot filename, CITATION.cff, README, SKILL.md, VERSION) updated.

**Pre-flight.** Lint 0 errors / 56 info-level orphans (baseline 55 + 1 for the new `principle-SP-15` anchor stub). Snapshot `PRISM_v2_1_1.md` byte-identical to `PRISM.md` at the tag. Customer-name leak-class sweep clean on every public-surface artifact. Commit `b0847ca` signed and GitHub-verified.

**Provenance.** Workshop diagnostic entries in `PRISM-workshop/notes/pending.md`: 2026-05-01 (Cowork irregular PRISM run — digest-at-return; default-vendor-stance inversion; codification drift toward asymmetric mitigation) and 2026-05-08 (single-vendor multi-agent ≠ cross-vendor triangulation). Patch spec at `PRISM-workshop/design/PRISM_v2_1_1_patch_spec.md`. Entries graduated `status: absorbed` with the v2.1.1 ship.

**Deferred to downstream carriers.** Three related pending observations not bundled into this patch: framing-block sweep meta-pattern (rides tooling-conventions optimization-phase or self-elevates on third instance); verbatim-memory operator pattern from Cowork codification drift (Cowork-mode design once that promotes); three-strike agent-substrate addendum (cross-vendor adaptation channel design or Cowork mode design, whichever lands first).

---

### Tooling conventions Patterns A + D + B Phase B1 (v2.1.0)

**Shipped on:** `main` of `Ronkupper/PRISM`, 2026-05-22. Tag `v2.1.0`.

**What landed.** Three independently-designed patterns bundled into one MINOR release per `PRISM-workshop/design/tooling_conventions_micro_dds_rev1.md` X1:

- **Pattern A — machine-readable frontmatter.** `PRISM.md` frontmatter expanded into two comment-grouped sections (skill metadata + framework metadata). New fields: `version`, `released`, `supersedes`, `lens_library_embedded`, `substrate_target`, `normativity`, `lint_catalog_version`. Authoritative schema at `PRISM-workshop/schemas/prism_frontmatter.schema.json` (Python `check-jsonschema` validator).
- **Pattern B Phase B1 — strength × polarity vocabulary.** Frontmatter `normativity` block declares strength vocabulary (`required` / `recommended` / `optional`, default `required`) and polarity glyphs (✅ / ⚠️ / 🚫). Title-block tag-convention paragraph extended (two sentences) to announce the axes; vocabulary source is the frontmatter. New elements use the extended `[durability | review-trigger | strength? | polarity?]` form going forward; legacy element sweep deferred to Phase B2.
- **Pattern D — Appendix H, Vendor parsing observations.** New appendix indexing empirical observations of vendor parsing behaviour on dispatched content. Six-status closed vocabulary (`passthrough` / `stripped` / `mangled` / `error` / `not-tested` / `observed-once`), per-content-type H3 sections with narrow per-vendor tables, observation-driven appends with release-sweep at 12-month staleness. Seed entry: ChatGPT mobile paste = stripped (the empirical observation that drove §4.12 atomic-prompt self-containment in v2.0.2).

**Pre-shipping ratifications** (per `design/tooling_conventions_micro_dds_rev1.md` rev1 amendment, 2026-05-22): X1 bundle locked; C5 workshop retirement of `lint_named_refs.py` locked; C1 expanded with `PRISM-LINT-07` (description-version-match); X4 review-trigger locked to `review-if: release-sweep`; Step 2b convention-prose location locked to extending the title-block tag-convention paragraph (no new subsection); Step 3a Appendix H seed locked to single ChatGPT-mobile entry.

**Provenance.** `PRISM-workshop/design/tooling_conventions_survey_dd_rev1.md` (survey); `PRISM-workshop/design/tooling_conventions_micro_dds_rev1.md` (combined micro-DD A+B+C+D); `PRISM-workshop/handoffs/tooling_conventions_micro_dds_build.md` (build handoff). Sequenced via `design/backlog_sequencing_dd_rev1.md`.

**Coupling watch-out called out.** Bundling A + D + B Phase B1 into one release silently couples three thinking sessions' delivery dates (per `backlog_sequencing_dd_rev1.md` Watch-out #2). Bundle is justified by review-surface efficiency: all three are independent content additions with no semantic conflict. If any of the three had hit a real blocker, the bundle would have broken rather than waited.

---

### Tooling conventions Pattern C — lint catalog (`lint-v1`)

**Shipped on:** `main` of `Ronkupper/PRISM`, 2026-05-22. Tag `lint-v1`.

**What landed.** Off-cycle reference artifacts for the public lint catalog. No `PRISM.md` content change.

- `lint_rules.md` at repo root — contributor-facing catalog with seven entries: two active (`PRISM-LINT-01 / named-refs-resolve` error; `PRISM-LINT-02 / named-refs-orphan-anchor` info), five reserved (`-03` `-04` `-05` `-07` gated on Pattern A; `-06` gated on Pattern B Phase B1, now active as of v2.1.0).
- `scripts/lint/lint_named_refs.py` — Python lint script. NDJSON output by default; `--text` flag for human-readable; `--severities` flag for selective emission. Consolidates broken-ref / slug-collision / mixed-ref-style under `PRISM-LINT-01`; emits `PRISM-LINT-02` for orphan anchors. Self-contained (slug-derivation function inlined; no workshop-script dependency).
- `.github/workflows/lint.yml` — PR-only CI workflow with two jobs: `lint-required` (runs error + warning; translates NDJSON to GitHub `::error` / `::warning` annotations; best-effort frontmatter-schema validation against the workshop-hosted schema) and `lint-info` (runs info; posts NDJSON-rendered summary as a sticky PR comment).
- `CONTRIBUTING.md` — new section "Reviewing PRs — rendered-diff convention" per `design/tooling_conventions_micro_dds_rev1.md` C7.

**Workshop retirement.** `PRISM-workshop/scripts/lint_named_refs.py` (the working/staging copy under the old `PRISM-REF-NN` rule IDs) is retired immediately on Pattern C ship per C5: single canonical home, no staging duplication.

**Provenance.** Same DD and handoff as the v2.1.0 bundle. Decisions C1–C8.

---

### Named cross-references migration (v2.0.2)

**Shipped on:** PRISM v2.0.2, 2026-05-22.

**What landed.** PRISM.md migrated from numbered `§X.Y` cross-references to named `§{namespace.slug}` form. 171 explicit `<a id="{ns}-{slug}"></a>` anchors injected. Single deterministic Python transformation (`PRISM-workshop/scripts/migrate_named_refs.py`). Initial linter (workshop's `lint_named_refs.py`) implemented `PRISM-REF-01/02/03/04` per the design DD. Lint run on the migrated file: 0 errors, 55 info-level orphan findings.

**Provenance.** `PRISM-workshop/design/named_refs_taxonomy_dd_rev1.md` (settled D1–D7); `handoffs/named_refs_build_v1.md` (build session). Sequenced via `design/backlog_sequencing_dd_rev1.md` Phase A.3.

**Catalog rename.** In `lint-v1` (Pattern C, 2026-05-22), the four `PRISM-REF-NN` rule IDs are consolidated under the public catalog: `REF-01` / `REF-02` / `REF-03` (all error) → `PRISM-LINT-01 / named-refs-resolve`; `REF-04` (info) → `PRISM-LINT-02 / named-refs-orphan-anchor`. Internal sub-mode (`broken-ref` / `slug-collision` / `mixed-ref-style` / `orphan-anchor`) preserved in NDJSON `context` field for diagnosability.

**Deferred to follow-up.** Bidirectional alias normalizer for contributor inputs (issue/PR/chat). Split-mode resolver (when partial decomposition of PRISM.md happens). External `prism-md` CLI.

---

### v1.9 foundation items — ask_user_input UX, LLM-access Scope Flag + execution envelope, SP-9 (v1.9)

**Shipped on:** PRISM v1.9 (the three items previously held under "Accepted for v1.9" in this file; cleared here as backlog housekeeping).

**What landed.** `ask_user_input` UX integration for discrete decision points (Scope Flags, Enrichment Scoping, M10 classification, Adaptation confirmation) with prose fallback; the LLM-access Scope Flag (`claude-only` / `multi-vendor`) plus the execution envelope on the attach map (role-based vendor recommendations, not named-vendor hardcoding); and **SP-9 (Silence is never consent)**, generalizing the no-timer / flag-don't-assume stance framework-wide. Full mechanism and decisions live in PRISM.md's §18 Version History; the timer-with-auto-advance variant was Declined (see Declined).

---

*End of backlog.*
