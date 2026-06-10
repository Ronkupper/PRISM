---
# Framework metadata (consumed by PRISM maintenance tooling)
version: 2.13.0
released: 2026-06-10
supersedes: 2.12.2
lens_library_bundled: "0.14"
substrate_target:
  vendor: claude
  tier: opus-class       # flagship/frontier tier — a capability floor, not a lightweight model
  version: latest        # version-agnostic; the latest Opus-class Claude by default
normativity:
  strength_vocabulary: [required, recommended, optional]
  strength_default: required
  polarity_vocabulary: ["✅", "⚠️", "🚫"]
  polarity_default: null
lint_catalog_version: 4
---

<!-- PRISM v2.13.0 Skill core (lean, always-loaded). Generated from the assembled
     PRISM.md by scripts/decompose/project_skill_archive.py — edit PRISM.md, not this.
     Reference-grade material is in reference/*.md and lens/, fetched on demand. -->

# PRISM v2.13.0 — Framework operating document

**Status:** v2.13.0 release. Canonical framework for Claude orchestration sessions.
**Date:** June 2026
**Supersedes:** PRISM v2.12.3 (MINOR: adds §{section.sp-16-the-elephant-rule} SP-16 "The Elephant Rule" — negation as a targeting decision, not a style choice. Prose may negate only a live alternative the reader demonstrably brings (a common prior, a named risk, or an inference the document's own numbers invite); uncalled-for denials plant the very frame they deny and are rewritten positively before release. Wired as step 5 of the Execution Self-check (§{section.prism-execution-self-check}) — an output-side audit that enumerates and tags every negation before the Output is emitted — and into the Lens Library as document-review lens LL-D-019 "Who said otherwise?" (Pack 1). Embedded Lens Library bumps v0.13 → v0.14 (additive: one new domain lens, 23 → 24 entries, no schema change); lint catalog stays v4.). PRISM v1.10.4 is terminal on the v1.x line (pinned per DD §{section.standing-principles-introduced-or-extended-in-v2}).
**Required attachments at every orchestration session:** the PRISM Skill
(its core loads automatically) and the project's Master. The Skill bundles
Lens Library v0.14 at `lens/PRISM_lens_library.md`, fetched on demand. Pin a
newer standalone Library version only when the project explicitly requires
one (see §{section.library-reference-at-setup}).
**Substrate:** Claude, Opus-class (flagship tier) — a capability floor,
version-agnostic, latest by default. Lighter-tier or non-Claude orchestration
is report-worthy per §{section.two-session-types}.

**Citation convention.** This file is self-contained operating instructions.
References to source artifacts: `Spec.§X.Y` points to PRISM_v2_spec_rev2.md;
`DD.§X.Y` points to PRISM_v2_rev8_design_document.md; `LL.LL-{U|D}-NNN`
points to a Lens Library entry.

**Reference resolution.** Internal cross-references are written in braces
after the section glyph (`§`) and resolve by namespace. A `section.` or
`appendix.` reference resolves directly to the matching `section-…` /
`appendix-…` anchor — its slug is the anchor id with the namespace prefix
removed. A `monitor.`, `principle.`, `probe.`, or `lens.` reference resolves
by typed token instead: the token (`M4`, `SP-9`, `P1`, `LL-D-002`) names the
construct, and the reference resolves to that construct's home-section anchor
— `§{monitor.M4}` → `section-m4-…`, `§{principle.SP-9}` → `section-sp-9-…`.
Both forms are validated by the named-reference linter under `scripts/lint/`.

**Tag convention.** Every decision in this document carries a two-axis tag —
durability axis (`structural` / `methodological` / `vendor-dependent` /
`empirical` / `operator-scaffolding`) × review-trigger axis
(`stable` / `review-if: <trigger>` / `review-annually`). Decisions may also
carry a strength token (`required` / `recommended` / `optional`, default
`required`) and a polarity glyph (✅ always do / ⚠️ ask first / 🚫 never),
appended after the review-trigger token when present; both vocabularies are
declared in this file's frontmatter `normativity` block. Per-element marking
is optional for legacy elements and applied to new ones going forward.
The full tag index is in `reference/provenance.md` (decision tag index).

**Voice.** This is operating instruction for Claude in an orchestration session.
Imperative where Claude must act; declarative where defining shape; descriptive
where pointing. Section headers carry the operative scope.

---

## Quick reference — first-time reader

Reading order for first encounter:

1. **§{section.scope} Scope** (this section group) — what v2.13.0 is and what it isn't.
2. **§{section.system-overview} System overview** — every construct, every lifecycle slot, the visual
   map. Use this to locate any specific mechanic later.
3. **§{section.architecture-mechanics} Architecture** — sessions, the triple contract, Master, *What's next*,
   Vendor Selection. The everyday machinery.
4. **§{section.setup-mechanics} Setup** — what happens before any prompt is dispatched. Library-graded
   iterative refinement; the seven probes.
5. **§{section.monitor-specifications} Monitors** + **§{section.standing-principles} Standing Principles** — the always-on background
   posture.

After that, §{section.prompt-package-engine} (prompt-package engine), §{section.context-pressure-framework} (context-pressure framework), §{section.library-integration}
(Library integration), §{section.filename-conventions-and-bump-atomicity} (filename conventions), §{section.atomic-prompt-template-v2-form} (atomic prompt template
v2 form), and §{section.operator-hint-catalog} (operator hint catalog) carry the rest of the operating
mechanics. §{section.worked-example-flow} walks a complete worked example.

Reading order for an operator returning to v2.13.0 after running a session:
*What's next* → relevant §{section.architecture-mechanics}–§{section.library-integration} mechanics → §{section.monitor-specifications} Monitors if a fire surfaced.

---

## 1. Scope
<a id="section-scope"></a>

### 1.1 What v2.13.0 covers `[structural | stable]`
<a id="section-what-v2-8-0-covers"></a>

PRISM v2.13.0 is a structured multi-session, multi-vendor LLM-orchestrated audit
and research framework. v2.13.0 covers:

- **Two session types** (orchestration on Claude; execution on selected vendor per Vendor Selection)
  with explicit role separation (§{section.two-session-types}).
- **The triple contract** (Envelope inbound, Self-check, Output outbound) as
  the load-bearing interface between sessions (§{section.the-triple-contract}).
- **Master + *What's next* as continuous-state artifacts** written at every
  orchestration turn-close, regardless of band state (§{section.the-master}, §{section.whats-next}, §{section.failsafe-recovery-continuous-state-mechanics}).
- **Vendor Selection at dispatch** with live web-search currency check
  (§{section.vendor-selection-at-dispatch}).
- **Setup as iterative refinement** against the Lens Library v0.14, with
  three-layer readiness clearing the P0→P1 boundary (§{section.setup-mechanics}).
- **Seven Setup probes** (§{probe.P1} Coverage grading, P2 Adversarial Scope, P3
  Decision Framing, P4 Pre-mortem, P5 Falsifier, P6 Domain Reconnaissance,
  P7 User Voice) — Setup-time grading constructs only (§{section.the-seven-probes}).
- **Library integration** — the Lens Library v0.14 as canonical reference
  catalog (bundled at `lens/PRISM_lens_library.md`, fetched on demand);
  point-refresh in Setup; Update sessions for
  currency maintenance (§{section.library-integration}).
- **Twelve Monitor slots** (M1–M12, with v1.x M12 Conversation Pressure
  retired into M5 and the M12 slot reused for Result Completeness Check)
  firing orchestration-side at defined lifecycle slots (§{section.monitor-specifications}).
- **Telemetric context-pressure framework** (§{monitor.M5}) — seven signals,
  qualitative compounding, four bands (🟢🟡🟠🔴), continuous-curation
  posture from 🟡 onward (§{section.context-pressure-framework}).
- **Migration handoff** as a defined artifact at 🔴 (mandatory) and 🟠
  (operator-elective) (§{section.migration-handoff}).
- **Standing Principles** governing posture across sessions (§{section.standing-principles}).
- **Filename discipline** — structured patterns for Outputs, Masters,
  handoffs, and Library files (§{section.filename-conventions-and-bump-atomicity}, SP-14).
- **Forward-compatibility commitments** — Tools slot in Envelope, and the
  three-axis execution-configuration schema at Setup
  (§{section.orchestration-driver-and-persistence-axes}).
- **Atomic prompt template v2 form** — wraps the triple contract around the
  prompt body (§{section.atomic-prompt-template-v2-form}).

### 1.2 What v2.13.0 does not cover
<a id="section-what-v2-8-0-does-not-cover"></a>

- **Re-debating direction.** v2.13.0 implements the spec; the spec implements
  the design document. Direction is settled. New direction goes through a
  fresh design cycle.
- **Standalone Library evolution.** The Lens Library catalog is bundled at
  `lens/PRISM_lens_library.md` (tag `prism-lens-v0.14`, v0.14 at this release),
  fetched on demand. The bundled file remains authoritative for the Library's
  own evolution and for projects that explicitly pin to a newer Library version.
- **Empirical calibration.** Several thresholds in v2.13.0 are rev. 1 draft
  estimates: M5 band thresholds (§{section.telemetric-framework-signal-weighting-and-compounding}), Update session trigger (§{section.currency-maintenance-update-session}),
  probe iteration ceilings (§{section.from-waterfall-to-library-graded-iterative-refinement}). Calibration against real use is a
  post-release item (§{section.empirical-calibration-items}).
- **Multi-vendor Self-check empirical footing.** Verified on Claude
  Opus-class and Sonnet-class models. Behavior on Gemini, ChatGPT, Perplexity
  is report-worthy (§{section.empirical-calibration-items}).
- **Non-Claude orchestration.** v2.13.0's machinery uses Claude-specific
  affordances (`present_files`, `create_file`, `str_replace`,
  `ask_user_input`, `conversation_search`, Skill packaging). Non-Claude
  orchestration is graceful-degradation, not a design target (DD.§3.1).

### 1.3 Three-leg constraint `[structural | stable]`
<a id="section-three-leg-constraint"></a>

v2.13.0 honours the constraint inherited from the design document (DD.§8.3):

- **Operator constraint.** Mobile-first; plain-chat substrate; manual
  artifact handling between sessions.
- **Substrate constraint.** Claude Opus-class (flagship tier) in orchestration; multi-
  vendor on the execution side.
- **Methodology constraint.** Structured audit-and-research with explicit
  scope-completeness and convergence discipline.

Mechanics that violate any leg do not earn their place in v2.13.0. Roadmap
adjacencies (DD.§9: automated cross-vendor orchestration, plugin-equipped
execution, multi-vendor skill ecosystems) live in reserved structural
surfaces — the `Tools:` slot and the reserved values on the
execution-configuration axes (§{section.orchestration-driver-and-persistence-axes}) —
but no machinery beyond the reservation.

---
## 2. System overview
<a id="section-system-overview"></a>

**Read this section first if you are encountering v2.13.0 mechanics for the
first time, and re-read it any time you need to locate a specific construct.**
This section is a map. Definitions live in the per-construct sections (§{section.architecture-mechanics}–§{section.missing-handoff-recovery}).

### 2.1 Construct list
<a id="section-construct-list"></a>

PRISM v2.13.0 has the following constructs, grouped by category.

**Sessions** (§{section.two-session-types})
- Orchestration session — Claude session with the framework attached
- Execution session — vendor session running a single dispatched prompt
- Update session — out-of-band, operator-gated, maintains Library currency
  (§{section.currency-maintenance-update-session})

**Phases**
- P0.x — Setup (iterates against draft Prompt Strategy)
- P1+ — Execution (dispatched prompts run; convergence absorbs results)
- P0→P1 boundary — three-layer readiness clears (§{section.three-layer-readiness})

**Probes** (§{section.the-seven-probes}) — Setup-time grading constructs only
- P1 Coverage grading · P2 Adversarial Scope · P3 Decision Framing · P4
  Pre-mortem · P5 Falsifier · P6 Domain Reconnaissance · P7 User Voice

**Monitors** (§{section.monitor-specifications}) — orchestration-side checks
- M1 Missing Inputs · M2 Version Drift · M3 Sequence Violation · M4
  Ambiguous Ask · M5 Context Pressure · M6 Premise Shift · M7 Claim
  Conflict · M8 Stale Source · M9 Convergence Type Drift · M10 Rerun /
  Fix Required · M11 Layer 2 Readiness · M12 Result Completeness Check

**Top-level artifacts**
- Master (§{section.the-master}) · *What's next* (§{section.whats-next}) · Lens Library (§{section.library-integration}) · Migration
  handoff (§{section.migration-handoff}) · Convergence delta (§{section.convergence-delta-document})

**Master sections** (state lives here)
- Decision brief · Stakeholder register · Claim inventory · Jurisdiction
  map · Prompt Strategy · Dispatch register · Findings · Rerun Register ·
  Learnings Register · Changelog · Open dispatches list · Active probes
  list · Open monitors list

**Execution contract** (the triple, §{section.the-triple-contract})
- Envelope (inbound) · Self-check (substrate verification) · Output
  (outbound)

**Standing Principles** (§{section.standing-principles})
- v2-new/extended: SP-1 ext, SP-12, SP-13, SP-14, SP-15, SP-16
- Carryforward: SP-2, SP-4, SP-5, SP-6, SP-7, SP-8 (narrowed), SP-9, SP-10
- Dissolved: SP-3

**Mechanisms**
- Vendor Selection (§{section.vendor-selection-at-dispatch}) · Vendor Triangulation (§{section.vendor-triangulation}) · Bump atomicity
  (§{section.standalone-monitors-m1-m2-m4-m5-m9} spec / §{section.filename-conventions-and-bump-atomicity}) · Telemetric framework (§{section.telemetric-framework-signal-weighting-and-compounding}) · Point refresh (§{section.currency-maintenance-point-refresh}) ·
  Update session (§{section.currency-maintenance-update-session}) · Continuous-curation (§{section.continuous-curation-posture}) · Strategy stability
  (§{section.strategy-stability}) · Three-layer readiness (§{section.three-layer-readiness}) · Two-layer convergence · Triple
  contract

**Bands** — 🟢 Comfortable · 🟡 Getting warm · 🟠 Curate now · 🔴 Migrate

### 2.2 Visual map
<a id="section-visual-map"></a>

```
+----------------------------------------------------------------------+
| ORCHESTRATION SESSION (Claude; framework attached)                   |
|                                                                      |
|  +------------------+    +------------------+    +---------------+   |
|  | Setup (P0.x)     |    | Per-turn         |    | Layer-2       |   |
|  | ---------------- |    | ---------------- |    | ------------- |   |
|  | P1 Coverage      |    | M1 Missing Inp.  |    | Cold synth    |   |
|  | P2 Adv. Scope    |    | M2 Ver. Drift    |    | M9 type drift |   |
|  | P3 Decision Fr.  |    | M3 Seq. Viol.    |    | Falsifier     |   |
|  | P4 Pre-mortem    |    | M4 Ambig. Ask    |    | check         |   |
|  | P5 Falsifier     |    | M5 Ctx. Press.   |    +---------------+   |
|  | P6 Domain Recon  |    | M11 L2 Ready.    |                        |
|  | P7 User Voice    |    +------------------+                        |
|  +------------------+                                                |
|         |                                                            |
|         v                                                            |
|  Three-layer readiness (Structural, Lib coverage, Op ratification)   |
|         |                                                            |
|         v                                                            |
|  Master version bump (P0->P1) ---- continuous Master + What's next   |
|                                    written every turn-close          |
|         |                                                            |
|         v                                                            |
|  +----------------------------------------------------------+        |
|  | Vendor Selection (live web check at dispatch)            |        |
|  |  -> produces Envelope                                    |        |
|  +----------------------------------------------------------+        |
|         |                                                            |
+---------+------------------------------------------------------------+
          | (operator dispatches)
          v
+----------------------------------------------------------------------+
| EXECUTION SESSION (any vendor; framework NOT attached)               |
|                                                                      |
|  Envelope (inbound) --> Self-check (substrate verify) --> Task body  |
|                                                                |     |
|                                                                v     |
|                                                         Output (.md) |
+----------------------------------------------------------------+-----+
                                                                 |
                                                                 v
+----------------------------------------------------------------------+
| ORCHESTRATION SESSION (continued; operator attaches Output)          |
|                                                                      |
|  Layer-1 convergence:                                                |
|    M6 Premise Shift                                                  |
|    M7 Claim Conflict      --+                                        |
|    M8 Stale Source         +-> may chain to M10 (Rerun)              |
|    M12 Result Completeness -+                                        |
|                                                                      |
|    Vendor Triangulation (if equivalence dispatch, N>=2)              |
|       +-> Convergence delta written to Master                        |
|                                                                      |
|  Reconciliation (Output Vendor/config vs Envelope) --> Dispatch reg  |
|                                                                      |
|  Master + What's next rewritten --> band header (M5)                 |
|         |                                                            |
|         v                                                            |
|  At red: Migration handoff produced; operator opens fresh session.   |
+----------------------------------------------------------------------+

OUT-OF-BAND
+----------------------------------------------------------------------+
| Update session (rare; operator-gated)                                |
|   Library file in -> currency check -> delta document -> Library out |
+----------------------------------------------------------------------+
```

### 2.3 Construct cards
<a id="section-construct-cards"></a>

Per-construct lifecycle, reads, writes, triggers. Cross-refs to detail
sections.

**Sessions and phases**

| Construct | Lifecycle | Reads | Writes | Trigger | Detail |
|---|---|---|---|---|---|
| Orchestration session | Per session | All Master sections, Library, briefs | Master, *What's next* | Operator opens | §{section.two-session-types} |
| Execution session | Per dispatch | Envelope.Attachments only | Output `.md` | Envelope dispatched | §{section.two-session-types} |
| Update session | Out-of-band | Library file, web | New Library file | Operator declares | §{section.currency-maintenance-update-session} |
| P0 Setup | Iterates per turn | Subject brief, Library | Setup artifacts, Prompt Strategy | First session | §{section.setup-mechanics} |
| P1+ Execution | Per orchestration turn | Master, returned Outputs | Master findings | Operator dispatches | §{section.strategy-stability} |

**Probes** (Setup-only)

| Probe | Trigger | Reads | Writes | Detail |
|---|---|---|---|---|
| P1 Coverage grading | P0.x turn-close (iterates) | Library, draft strategy | Coverage map in Master | §{section.probe-1-coverage-grading-iterates} |
| P2 Adversarial Scope | P0.x turn-close (iterates) | Library, draft strategy, domain context | Omission candidate list | §{section.probe-2-adversarial-scope-iterates} |
| P3 Decision Framing | First P0 turn (once) | Subject brief | Decision brief, Stakeholder register | §{section.probe-3-decision-framing-once} |
| P4 Pre-mortem | P0.x turn-close (iterates) | Draft strategy, Decision brief | Failure-mode list | §{section.probe-4-pre-mortem-iterates} |
| P5 Falsifier | Late P0 (once) | Decision brief | Falsifiers section | §{section.probe-5-falsifier-once} |
| P6 Domain Reconnaissance | Early P0.x (iterates) | Subject, web (live) | Jurisdiction map, authoritative-source citations | §{section.probe-6-domain-reconnaissance-iterates-early} |
| P7 User Voice | Early P0.x (iterates) | User-facing surfaces, web | User-signal list | §{section.probe-7-user-voice-iterates-early} |

**Monitors** — orchestration-side; M12 (v2) is Result Completeness Check;
v1.x M12 Conversation Pressure retired into M5

| Monitor | Lifecycle | Reads | Writes | Trigger | Detail |
|---|---|---|---|---|---|
| M1 Missing Inputs | Per session-open + per turn | Session attachments, Output Attachment-warnings | M1 fire | Required attachment absent | §{section.m1-missing-inputs} |
| M2 Version Drift | Per session-open | Master metadata, expected version | M2 fire | Master version ≠ expected | §{section.m2-version-drift} |
| M3 Sequence Violation | Per turn (op declaration) | Prompt Strategy, op input | M3 fire | Step before prereq | §{section.m3-sequence-violation} |
| M4 Ambiguous Ask | Per turn (op input) | Op turn content | M4 fire | Cannot confidently parse | §{section.m4-ambiguous-ask} |
| M5 Context Pressure | Per turn-close | 7 telemetric signals | Band header | Every turn-close | §{section.m5-context-pressure-monitor} |
| M6 Premise Shift | Per Layer-1 ingestion | New finding, Setup artifacts | M6 fire | Premise invalidated | §{section.m6-premise-shift} |
| M7 Claim Conflict | Per Layer-1 ingestion | New finding, prior findings | M7 fire | Two findings incompatible | §{section.m7-claim-conflict} |
| M8 Stale Source | Per Layer-1 ingestion | New finding's cited sources, web | M8 fire | Source invalidated | §{section.m8-stale-source} |
| M9 Convergence Type Drift | Per Layer-1 + Layer-2 | Convergence step type | M9 fire | Wrong-posture convergence | §{section.m9-convergence-type-drift} |
| M10 Rerun/Fix Required | Multi-source (chain or op) | Trigger source | Rerun Register | Rerun condition | §{section.m10-rerun-fix-required} |
| M11 Layer 2 Readiness | Per turn-close | Dispatch register, Rerun reg, Open monitors | What's next candidate | Layer 2 conditions met | §{section.m11-layer-2-readiness} |
| M12 Result Completeness | Per Layer-1 ingestion | New finding's domain coverage | M12 fire | Domain coverage gap inside finding | §{section.m12-result-completeness-check} |

**Artifacts** (state lives here; only orchestration writes Master)

| Artifact | Lifecycle | Reads | Writes | Detail |
|---|---|---|---|---|
| Master | Persistent + per-turn write | Orchestration + execution (selective) | Orchestration only | §{section.the-master} |
| *What's next* | Per-turn rewrite | Orchestration + operator | Orchestration only | §{section.whats-next} |
| Lens Library | Persistent (read) | Orchestration | Update session only | §{section.library-integration} |
| Migration handoff | Per-🔴 (or 🟠 elective) | Orchestration | Orchestration | §{section.migration-handoff} |
| Convergence delta | Per Layer-1 batch | Orchestration | Orchestration | §{section.convergence-delta-document} |
| Dispatch register | Per dispatch + per return | Orchestration, *What's next*, M3, M10 | Orchestration | §{section.master-tracking-dispatch-register} |

**Mechanisms** (active behavioral routines)

| Mechanism | Lifecycle | Detail |
|---|---|---|
| Vendor Selection | Per dispatch | §{section.vendor-selection-at-dispatch} |
| Vendor Triangulation | Per Layer-1 batch (equivalence mode, N≥2) | §{section.vendor-triangulation} |
| Bump atomicity | Per Master version increment | §{section.filename-conventions-and-bump-atomicity} |
| Telemetric framework | Per turn-close | §{section.telemetric-framework-signal-weighting-and-compounding} |
| Point refresh | Per Setup probe iteration | §{section.currency-maintenance-point-refresh} |
| Continuous-curation | Per turn-close (band ≥🟡) | §{section.continuous-curation-posture} |
| Strategy stability | Per Layer-1 trigger | §{section.strategy-stability} |
| Three-layer readiness | Per P0→P1 boundary | §{section.three-layer-readiness} |
| Triple contract | Per dispatch | §{section.the-triple-contract} |

**Standing Principles** — persistent posture; not discrete fires (§{section.standing-principles})

| SP | v2 status | Detail |
|---|---|---|
| SP-1 ext Canonicity | Extended in v2 | §{section.sp-1-extended-canonicity-preservation} |
| SP-2 Defer non-critical | Carryforward | §{section.carryforward-sps-application-surfaces} |
| SP-3 (dissolved) | — | §{section.v1-x-standing-principles-carryforward-catalog} |
| SP-4 Monitors visible | Carryforward | §{section.carryforward-sps-application-surfaces} |
| SP-5 No heuristic guessing | Carryforward | §{section.carryforward-sps-application-surfaces} |
| SP-6 Rebuild at threshold | Carryforward | §{section.carryforward-sps-application-surfaces} |
| SP-7 File delivery mandatory | Carryforward | §{section.carryforward-sps-application-surfaces} |
| SP-8 Canonical authority (narrowed) | Carryforward (narrowed) | §{section.sp-8-narrowed-canonical-authority} |
| SP-9 Silence not consent | Carryforward | §{section.carryforward-sps-application-surfaces} |
| SP-10 Verify state before recommending | Carryforward as named principle | §{section.sp-10-verify-state-before-recommending} |
| SP-12 Bounded-search disclosure | New in v2 | §{section.sp-12-bounded-search-disclosure} |
| SP-13 Substrate declaration | New in v2 | §{section.sp-13-substrate-declaration} |
| SP-14 Filename discipline | New in v2 | §{section.sp-14-filename-discipline} |
| SP-15 Triangulation integrity | New in v2.1.1 | §{section.sp-15-triangulation-integrity} |
| SP-16 The Elephant Rule (negation discipline) | New in v2.13.0 | §{section.sp-16-the-elephant-rule} |

### 2.4 Lifecycle slots
<a id="section-lifecycle-slots"></a>

Every construct fires in exactly one lifecycle slot.

| Slot | What fires here |
|---|---|
| Setup-only | All probes (P1–P7) |
| Per session-open | M1 (also fires per-turn), M2, SP-13 substrate verification |
| Per orchestration turn | M3, M4, M5, M11, *What's next* write, Master append |
| Per dispatch | Envelope production, Self-check execution, Output return, Vendor Selection |
| Per Layer-1 ingestion | M6, M7, M8, M12, Vendor Triangulation (if applicable), reconciliation |
| Per Layer-2 synthesis | M9 (also Layer-1) |
| Out-of-band | Update session, point refresh (in-Setup) |
| 🔴 band | Migration handoff |
| Persistent posture | All Standing Principles |

### 2.5 Band legend
<a id="section-band-legend"></a>

Bands are M5's output; they drive curation and migration posture. Per-band
table in §{section.defensive-migration-at-natural-seams}.

- 🟢 **Comfortable.** Silent. No intervention.
- 🟡 **Getting warm.** Curation observation in *What's next*. Migration
  available at next natural seam.
- 🟠 **Curate now.** Active curation. Migration strongly recommended at
  immediate next seam.
- 🔴 **Migrate.** Migration handoff produced; fresh session.

### 2.6 Cross-section quick-find
<a id="section-cross-section-quick-find"></a>

If you need to find:

- **A specific construct's full mechanics** → §{section.construct-cards} construct card →
  cross-ref to detail.
- **How constructs flow in a real audit** → §{section.worked-example-flow} worked example.
- **What changed from v1.10.4** → `reference/provenance.md` (v1.x → v2 surface drift).
- **Decision rationale on something** → `reference/provenance.md` (decision tag index) → Spec.§
  reference for chosen alternative + rationale.
- **A template to paste** → `reference/templates.md` (template compendium).
- **The full text of a Standing Principle** → §{section.standing-principles}, the Standing-Principles catalog.

---
## 3. Architecture mechanics
<a id="section-architecture-mechanics"></a>

v2.0's architecture is the operating skeleton: two session types, the triple
contract that lets them interoperate cleanly, two artifacts (Master and
*What's next*) that carry state across turns and sessions, forward-compat
slots for things v2.0 doesn't yet have machinery for, and Vendor Selection
as the live currency check at dispatch time.

### 3.1 Two session types `[structural | stable]`
<a id="section-two-session-types"></a>

**Orchestration session.** A Claude session with the framework attached.

- *Loaded artifacts at session open*: this framework file (or the PRISM v2
  Skill that loads it); the Master; the Lens Library
  (`PRISM_lens_library.md` v0.14); the Prompt Strategy (when separate from
  the Master); subject-brief documents.
- *Session-open verification*: SP-13 substrate self-check (§{section.sp-13-substrate-declaration}) — Claude
  declares model identity and confirms it matches the declared orchestration
  target (Claude, Opus-class). Halt and ask the operator on mismatch or
  cannot-determine.
- *Outputs*: Master updates, *What's next* artifacts, Envelopes for next
  dispatch, convergence findings, Monitor fires.
- *Closes by*: writing *What's next* to the Master and surfacing it for the
  operator. Operator hint emitted: `Save Master to cloud drive (MO-5).`
- *Vendor*: Claude, Opus-class (flagship tier; version-agnostic, latest by
  default — lighter-tier Claude report-worthy per DD §{section.forward-compatibility-commitments} beta posture).

**Execution session.** A vendor session running a single dispatched prompt.

- *Loaded artifacts*: only what the Envelope's `Attachments:` field names.
  Framework not attached.
- *Session-open verification*: PRISM Execution Self-check (§{section.prism-execution-self-check}) — vendor
  declares model identity and confirms match against the Envelope's
  `Vendor:` and `Vendor config:` fields. Halt and report on mismatch.
- *Outputs*: a single `.md` file wrapped in PRISM Execution Output signature
  (§{section.prism-execution-output}).
- *Closes by*: producing the file and instructing the operator on filename
  and next action (per Envelope's `Expected output:` and the Output's
  `Operator next:`).
- *Vendor*: per the Envelope's `Vendor:` field. Any LLM the strategy
  specified.

**Why the split.** Orchestration is the framework's home — Master state,
Monitor fires, Setup probes, convergence reasoning. Execution is purpose-
built single-shot work — one prompt, one file out, no framework overhead.
Crossing the boundary is the triple contract (§{section.the-triple-contract}). v1.x ran convergence
inside execution sessions under SP-3; v2 dissolved SP-3 because it was
incompatible with the split.

### 3.2 The triple contract `[structural | stable]`
<a id="section-the-triple-contract"></a>

Three blocks — Envelope (inbound), Self-check (between envelope and task
body), Output (outbound). All three are visually distinctive, self-contained,
and produced by orchestration's Vendor Selection step (§{section.vendor-selection-at-dispatch}) at dispatch
time. The contract is the load-bearing interface between sessions; it
survives mode changes (manual paste-chat today; automated dispatch later)
unchanged.

#### 3.2.1 PRISM Execution Envelope
<a id="section-prism-execution-envelope"></a>

```
━━━ PRISM EXECUTION ENVELOPE ━━━
Prompt ID:          [identifier — purpose/title]
Project:            [project name]
Master version:     [filename of Master at dispatch time]
Prompt digest:      [orchestration-generated at dispatch; copy verbatim; never recomputed]
Posture:            epistemic | investigation
Vendor:             [vendor] | multi-vendor          ← epistemic posture
Dispatch shape:     equivalence | split | limitation-named   ← epistemic posture
Dispatch rationale: [one positive-framing line per variant; see §4.2]   ← epistemic posture
Vendor config:      [vendor-specific config flags]
Session hygiene:    [fresh session, project attachment posture, web search on/off]
Tools:              [vendor tools requested; reserved slot for plugins/skills]
Attachments:        [filename, filename, ...]
Expected output:    [filename to download as]
Operator hints:     [zero or more one-line cues; see §3.2.4]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Field semantics.**

- `Prompt ID` — short unique identifier + purpose/title, unrelated to phase.
- `Master version` — the filename of the Master that was current when this
  Envelope was produced. Used for reconciliation if state drifts.
- `Posture` — `epistemic` or `investigation`. *Epistemic* Envelopes dispatch a
  prompt body for a vendor to reason over and carry the triangulation fields
  (`Vendor`, `Dispatch shape`, `Dispatch rationale`). *Investigation* Envelopes
  retrieve material rather than reason over it — corpus-access lookups
  (§{section.corpus-access-dispatch}, the external-reference-corpus lookup) and
  the subagent-investigation uses (§{section.cowork-surface-capabilities}, the
  Cowork capability surface) — and carry **none** of those fields. An Envelope
  with no `Dispatch shape` cannot fire Vendor Triangulation
  (§{section.vendor-triangulation}) and never counts as a triangulation seat
  (SP-15, §{section.sp-15-triangulation-integrity}). Default for a standard
  dispatch is `epistemic`.
- `Vendor` — single vendor name (`Claude Opus 4.7`, `Gemini Pro Deep
  Research`, `Perplexity`, `ChatGPT o-series`) or the literal `multi-vendor`.
- `Dispatch shape` — see §{section.single-envelope-with-spectrum-shape} for the three modes.
- `Dispatch rationale` — one positive-framing line per variant. See §{section.rationale-discipline-per-dispatch-variant}.
- `Vendor config` — vendor-specific configuration (e.g., `Deep Research ON,
  extended thinking ON`).
- `Session hygiene` — substrate setup the vendor session must satisfy.
- `Tools` — vendor tool slot. v2 default: `web search ON/OFF`. Reserved
  structural slot for future plugin/skill specification.
- `Attachments` — comma-separated filenames the operator must attach. Order
  is significant where the prompt body references attachments by position.
- `Expected output` — the filename the operator should download the produced
  file as. Naming convention per §{section.filename-conventions-and-bump-atomicity}: `[project]_[promptID]_[vendor].md`.
- `Operator hints` — zero or more one-line cues. See §{section.operator-hints-emission-discipline}.

#### 3.2.2 PRISM Execution Self-check
<a id="section-prism-execution-self-check"></a>

Operationalizes SP-13 (§{section.sp-13-substrate-declaration}) inside the execution session, and carries
the SP-16 negation audit (§{section.sp-16-the-elephant-rule}, the Elephant
Rule) as its output-side step. Sits between the Envelope and the task
body; steps 1–4 fire before the task, step 5 fires before the Output is
emitted.

```
━━━ PRISM EXECUTION SELF-CHECK ━━━
Before doing the task:

1. State what model/vendor you are and what session
   state you can introspect (mode, thinking setting,
   tools enabled).
2. Compare to the Envelope's Vendor and Vendor config
   fields above.
3. If anything does not match, or if self-identification
   is incomplete, STOP. Report what you found and ask
   the operator whether to proceed, switch sessions,
   or abort. Do not proceed to the task silently.
4. Proceed only if (a) the substrate matches, or
   (b) the operator has explicitly confirmed to proceed
   despite mismatch.
5. Before emitting the Output: enumerate every
   negation in the findings content ("not Y",
   "X, not Y", "rather than Y", "no Y"); tag
   each called-for (naming the live alternative
   it answers) or uncalled-for (rewrite
   positively before release). Headings and
   opening sentences first (SP-16, the
   Elephant Rule).
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Behavior contract.**

- The vendor session must self-identify before touching task content.
  Self-identification is best-effort honest — vendors that cannot introspect
  a field hedge on it rather than fabricate.
- Mismatch halts the task and emits a Self-check report. The report is the
  deliverable until the operator confirms.
- "Confirmation to proceed" is a positive operator action (a message in the
  conversation), not an inferred consent from continued attachment (§{principle.SP-9}).
- Step 5 is an output gate, not substrate verification: it fires once
  the findings content is drafted, before the Output block is emitted.
  Uncalled-for negations are rewritten positively, not annotated
  (§{section.sp-16-the-elephant-rule}, the Elephant Rule).

**Multi-vendor empirical footing.** Verified on Claude Opus-class and
Sonnet-class models. Gemini, ChatGPT, Perplexity behavior under this
block is **report-worthy finding** per DD.§3.5 — operators report
divergences. See §{section.empirical-calibration-items}.

#### 3.2.3 PRISM Execution Output
<a id="section-prism-execution-output"></a>

Every execution session produces a `.md` file whose contents are wrapped in
this signature.

```
━━━ PRISM EXECUTION OUTPUT ━━━
Prompt ID:        [identifier — purpose/title]
Project:          [project name]
Master version:   [from Envelope]
Vendor:           [vendor that actually executed; see §4.10]
Vendor config:    [config actually applied at execution]
Schema version:   output-v1
Date:             [YYYY-MM-DD]
Prompt digest:    [copied verbatim from Envelope]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[findings content]

━━━ END PRISM EXECUTION OUTPUT ━━━
Operator next:        [download instruction; attach instruction]
Attachment warnings:  [optional; one line per warning; see §9.2 spec / §13]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Field semantics.**

- `Vendor` and `Vendor config` reflect *executed* state, not *recommended*
  state. This is the field orchestration reads for recommended-vs-executed
  reconciliation (§{section.recommended-vs-executed-reconciliation}).
- `Schema version` — currently `output-v1`. Bumps when the Output block's
  structure changes; orchestration's Layer-1 convergence flags
  incompatibilities at ingestion.
- `Prompt digest` — detects wrong-prompt / wrong-attachment delivery at
  dispatch boundaries. Mechanism: orchestration generates the digest at
  dispatch time and writes it into the Envelope; execution copies it
  verbatim from the Envelope into the Output signature; orchestration
  compares the returned copy against the original. Verifies copy-through,
  not cryptographic computation by the execution model. Generating the
  digest at return time provides zero integrity check — there is nothing
  to compare against.
- `Operator next` — download filename + attachment instruction for the next
  orchestration turn.
- `Attachment warnings` — populated only when warranted. See §{section.operator-hint-catalog} for
  emission rules and severity tags.

**Production discipline.** The execution session produces the file via the
vendor's file-creation surface (Claude `create_file`; ChatGPT Canvas;
Gemini's file generation). Where the vendor cannot produce a file, fallback
is delimited content rendering with explicit warning that paste fallback has
known clipboard-fidelity issues (DD.§4.1.1).

**Exhibits manifest (corpus-access bundle returns).** A corpus-access lookup
(§{section.corpus-access-dispatch}, the external-reference-corpus lookup) returns
a *bundle*: the synthesized finding stays the canonical Output above — same
signed `.md`, same signature, same digest — and any captured artifacts
(screenshots, downloaded decks, exported record tables) travel as companion
files named per SP-14 (§{section.sp-14-filename-discipline}, filename
discipline). When the Envelope's `Archive:` field is `requested`, the Output
carries a mandatory `Exhibits` manifest section inside the findings content, one
entry per artifact:

```
━━━ EXHIBITS ━━━
[filename] · [source] · [capture date]
   query answered: [the scoped question this artifact substantiates]
   caveat:         [the applicable framing + temporal caveat]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

The manifest is mandatory rather than optional for the same reason `Source
framing` and `Temporal frame` are mandatory on the lookup Envelope: an exhibit
stripped of its provenance is, weeks later in the report, an artifact nobody can
cite because nobody knows what it shows or what caveat applies. Findings return
caveat-attached; exhibits return provenance-attached. The Output signature and
`Schema version: output-v1` are unchanged — the manifest is an added section
within the findings content, not a new return contract.

#### 3.2.4 Operator hints — emission discipline
<a id="section-operator-hints-emission-discipline"></a>

Hints are optional one-line cues keyed to the upcoming action.

**Emission rules.**

- Fire only when a cue applies to *this* dispatch. Routine dispatches carry
  zero hints. Signal-to-noise discipline.
- One line per hint; pointer to §{section.mobile-operator-survival-guide} (mobile operator survival guide), not an
  inline essay.
- No hint that duplicates a Monitor fire.
- Substrate calibration attribution where non-obvious — `(Claude mobile,
  Samsung)`. Mismatched substrates self-diagnose rather than silently
  confuse.
- Hints surface in two places: in the Envelope's `Operator hints:` field
  when the next action is a dispatch; in the *What's next* artifact (§{section.whats-next})
  when the next action is not a dispatch (review, ratify, save-to-cloud).

The full operator hint catalog is in §{section.operator-hint-catalog}.

### 3.3 The Master `[structural | stable]`
<a id="section-the-master"></a>

The Master is the single canonical project state file. Operator workflow
treats it as the project — not the chat, not the session, not what
orchestration remembers.

**Filename convention** (per §{section.filename-conventions-and-bump-atomicity}, SP-14):
`[project_name]_prism[version]_master_[phase-derived versioning].md`. E.g.,
`acme_audit_prism2.0_master_p2.3.md`.

**Lifecycle.**

- *Created* at Setup P0.1 (first orchestration turn).
- *Updated* at every orchestration turn-close, regardless of band state.
  Updates are append-mostly: the Changelog gains a line; relevant register
  sections gain entries. Continuous-state mechanic per §{section.failsafe-recovery-continuous-state-mechanics}.
- *Filename version bumps* at phase boundaries (P0→P1, P1→P2). Sub-version
  increments at convergence rounds within a phase (P2.1 → P2.2). Schema
  version increments tracked in the Master's metadata header. Bump
  atomicity rules in §{section.filename-conventions-and-bump-atomicity}.
- *Single file by principle* — no parallel Masters. Multiple-Master state is
  itself a Monitor fire (§{monitor.M2} Version Drift, §{section.m2-version-drift}).
- *Authoritative copy* — operator's locally-attached Master at session open
  is authoritative for that session. Cloud-drive copies (§{section.mobile-operator-survival-guide} MO-5) are
  durable persistence, not authority.

**Required sections.**

- Metadata header: project name, current Master version, Schema version,
  last updated.
- Decision brief (Setup artifact, §{section.decision-brief}).
- Stakeholder register (Setup artifact, §{section.stakeholder-register}).
- Claim inventory (Setup artifact, §{section.claim-inventory}).
- Jurisdiction map (Setup artifact, §{section.jurisdiction-map}).
- Prompt Strategy — current ratified version.
- Dispatch register — table of recommended-vs-executed state per prompt
  (§{section.master-tracking-dispatch-register}).
- Findings sections — per-prompt converged findings, with provenance.
- Open dispatches list — prompts not yet closed.
- Active probes list — Setup probes still iterating (P0 only).
- Open monitors list — M2/M3/M4/M6/M7/M8/M9/M10/M11/M12 fires not yet
  resolved.
- Rerun Register (§{section.m10-rerun-fix-required}) — overdue/scheduled/running/complete/cancelled.
- Learnings Register — cross-project pattern accumulator.
- Changelog.

**Optional sections** (populated when applicable to the project):

- Falsifier probe outputs (Probe 5).
- Layer-2 synthesis (when Layer 2 has run).
- External-stakeholder deliverable drafts (when applicable).

**Proportionality.** Lean projects keep a lean Master — small dispatch
sequences need only a subset of the required sections (metadata, decision
brief, dispatch register, findings, Changelog). Spec inclusion of optional
sections is operator-discretion at Setup; default is *include sections that
earn their place*.

### 3.4 *What's next* `[structural | stable]`
<a id="section-whats-next"></a>

*What's next* is the operator's single source of "what to do next." Not by
scrolling chat. Not by reading the Master in detail. Just *What's next*.

**Lifecycle.** Written at every orchestration turn-close. Replaces in-place;
old *What's next* is overwritten. Historical pointers live in the Master's
Changelog.

**Repo-resident variant.** Under `persistence: repo_backed`
(§{section.repo-backed-mechanics}), *What's next* is written to a fixed path
in the engagement's repo work folder instead of living only in chat. Same
artifact, same content, same per-turn-close lifecycle; repo-residence changes
only where it is stored, making it the pickup point a session on any surface
reads on resume. Nothing else about *What's next* changes.

**Required content.**

```
━━━ WHAT'S NEXT ━━━
Master version:        [current Master filename]
Context band:          🟢 | 🟡 | 🟠 | 🔴 (per §5)

Current state summary:
  Active prompt(s):    [prompt IDs in flight]
  Open dispatches:     [prompts in dispatch register, status != closed]
  Pending Adaptations: [list]
  Recent Monitor fires: [last 3 turn-closes' Monitor fires]
  Active probes:       [Setup probes still iterating, if in P0]

Candidate next actions (priority-ranked):
  1. [candidate] — [rationale, 1 line]
  2. [candidate] — [rationale]
  ...

Recommended next action:
  [pick from candidates] — [why]

Operator hints:        [zero or more; emission discipline §3.2.4]

Dispatch-ready payload (if applicable):
  [full Envelope + Self-check + prompt body, ready to paste]
━━━ END WHAT'S NEXT ━━━
```

**Candidate ranking ladder** (priority order; ties surface to operator):

1. 🔴 context-pressure migration handoff (when band = 🔴).
2. M2 / M3 / M4 fires (operator-side checks-and-balances) unresolved.
3. Open Rerun Register items overdue (§{monitor.M10} active).
4. M6 HIGH (Premise Shift) unresolved at convergence.
5. Adaptation pending operator approval.
6. Layer 2 readiness (§{monitor.M11}) when conditions met *and* operator has not
   deferred.
7. Next canonical Setup probe iteration (when in P0).
8. Next canonical dispatched prompt (when in §{probe.P1}+ execution).
9. Convergence-round consolidation (Layer 1 batch when ≥2 returns are in).
10. Curation and migration at natural seam (when band ≥ 🟡).

**Tie-handling.** When two or more candidates are within the same priority
tier, *What's next* surfaces all of them and asks the operator. SP-9
lineage: silence is never consent.

**Operator escalation format** (when ties surface):

```
Multiple candidates at priority [tier]:
  - A: [candidate] — [rationale]
  - B: [candidate] — [rationale]
Operator pick required before proceeding.
```

### 3.5 Forward-compatibility commitments `[structural | stable]`
<a id="section-forward-compatibility-commitments"></a>

These commitments cost the v2.0 build essentially nothing now and prevent
later architectural rework when v2.x or v3 wants to plug in automation,
plugin-equipped execution, or cross-vendor orchestration.

- **Vendor-agnostic execution contract.** The Envelope/Self-check/Output
  triple is vendor-agnostic by construction. Future automated dispatch
  plugs in by replacing the operator with an automation layer; contract
  unchanged.
- **Tools slot in Envelope.** The `Tools:` field is a structural reservation.
  v2.0 defaults to `web search ON/OFF`. Future desktop-mode extensions use
  this slot for plugin/skill enumeration (e.g., `Tools: web search ON,
  Playwright, Firecrawl`). v2.0 adds no machinery for this beyond the slot.
- **Execution-configuration axes at Setup.** The v2.0 single
  `execution_mode` flag is retired in favor of three orthogonal axes set at
  Setup — orchestration surface, execution driver, and persistence — each a
  closed validated enum. The default cell
  (`single_chat` / `manual` / `ephemeral`) reproduces v2.0 behavior exactly;
  the non-default values are the reserved forward-compatibility surface.
  Full schema in §{section.orchestration-driver-and-persistence-axes}.

#### 3.5.1 Orchestration, driver, and persistence axes
<a id="section-orchestration-driver-and-persistence-axes"></a>

What v2.0 carried as a single `execution_mode` flag is really three
independent concerns. v2 splits them into three orthogonal axes, each set at
Setup and each a **closed validated enum** — Setup validates the value
against that axis's set and halts with an operator escalation on anything
unrecognized (the halt-on-unrecognized discipline is preserved *per axis*,
not abandoned). All three describe the driver/config layer **above** the
triple contract; the Envelope/Self-check/Output contract stays
vendor-agnostic and unchanged regardless of axis values
(§{section.the-triple-contract}).

**Axis 1 — Orchestration surface.** *Where the orchestration session runs;
gates which capabilities are available.*

- `single_chat` *(default)* — mobile or desktop single chat; prompts and
  files passed between sessions by hand. No added memory or SI.
- `projects` — the single-chat surface plus a dedicated SI and a
  *lightweight* Claude Project memory (in-flight directives, state, and
  pointers to fuller context held elsewhere). A genuine surface, not a
  persistence layer — the limited memory is explicitly not an `.md` or
  long-context store, which is why it sits on this axis and not on
  persistence.
- `cowork` — desktop agent surface; carries the broadest capability set
  (§{section.cowork-surface-capabilities}).

**Axis 2 — Execution driver.** *How the Envelope is executed against the
chosen LLM(s).*

- `manual` *(default; the only built value)* — the operator follows the
  Envelope: copies the prompt, downloads named attachments, pastes and
  attaches at the execution LLM(s). Manual by deliberate choice.
- `auto_drive` *(reserved; roadmap, not priority)* — Computer Use and/or the
  Chrome MCP drive the execution LLM's app on the operator's behalf,
  delegated to per-LLM auto-drive skills rather than one monolith. **Gated
  to `cowork`** — auto-drive needs the desktop substrate; `single_chat` and
  `projects` cannot drive another app. Reserved in the sense above: the slot
  is committed, the machinery is not built. *SP-15 boundary: auto-driving N
  distinct vendor apps triangulates; auto-drive that collapses to
  single-vendor sub-agent fan-out does not
  (§{section.sp-15-triangulation-integrity}).*

**Axis 3 — Persistence.** *Where durable state lives across sessions and
surfaces.*

- `ephemeral` *(default)* — state lives in chat scrollback, project
  knowledge, or a local or Cowork folder; not designed for cross-surface
  continuity.
- `repo_backed` — durable state lives in a GitHub repo and **layers across
  any orchestration surface** (the point of the axis: it is orthogonal to
  *where* orchestration runs). The repo-resident *What's next*
  (§{section.whats-next}) is the cross-surface pickup point. The value and
  its contract are fixed here; the mechanics are specified in
  §{section.repo-backed-mechanics}.

**Reserved-token re-homing.** The v2.0 `execution_mode` reserved values are
re-expressed across the axes rather than carried as mode tokens:

- `agentic_orchestration` → the `auto_drive` execution-driver value.
- `automated_cross_vendor` → retired as a token. It decomposes into
  (`auto_drive` × cross-vendor equivalence dispatch); the capability is
  fully expressible without a dedicated token, so nothing is lost.
- `plugin_equipped` → retired as a token. Plugin and skill enumeration is
  already the job of the dispatch-time `Tools:` slot in the Envelope
  (§{section.prism-execution-envelope}); a Setup-time mode token would be
  redundant and at the wrong altitude — tooling is a per-dispatch property,
  like Vendor Selection, not a Setup fixture.

**Cross-vendor equivalence is methodology, not an axis value.** Dispatching
one prompt body to multiple *vendors* and converging on the returns is
`equivalence` dispatch (§{section.single-envelope-with-spectrum-shape}) — a
property of the Envelope that rides *any* cell of this matrix, independent
of surface, driver, and persistence. It is never a mode value. This is the
SP-15-safe home for triangulation: the asymmetry is carried by the vendor
set, and `auto_drive` changes only *who pastes*, never how many
distributions a prompt reached (§{section.sp-15-triangulation-integrity}).

### 3.6 Vendor Selection at dispatch `[methodological | review-if: vendor landscape changes]`
<a id="section-vendor-selection-at-dispatch"></a>

Vendor Selection runs every time orchestration is about to produce a
dispatch-ready Envelope. Not at Setup time; at dispatch time. The mechanic
operationalizes SP-10 (§{section.sp-10-verify-state-before-recommending}) at the moment a vendor recommendation
matters.

**Three-step routine.**

1. **Refresh.** Run a web-search-based currency check on the specific
   decision: is the recommended vendor still the right call for this prompt
   shape? Are there known issues this week? Has a newer vendor capability
   changed the calculus? Output: a 2–4 line refresh note with citations.
2. **Structured outcomes.** Where refresh produces a confident specific
   recommendation, the configuration is written into the Envelope
   (`Vendor:`, `Vendor config:`, `Tools:`). No operator decision required.
3. **Soft outcomes — recommendation bubble.** Where refresh produces a
   judgment call (vendor X usually but has had issues; vendor Y is a
   fallback), the soft outcome surfaces as a non-blocking note attached to
   the Envelope. Operator reads, agrees or overrides via reply.

**Output structure** (visible to operator):

```
━━━ VENDOR SELECTION ━━━
Prompt ID:           [...]
Refresh check:       [2-4 lines, what was checked, what was found]
Recommended:         [Vendor / Vendor config / Tools]
Rationale:           [1-2 lines, positive framing]
Soft notes:          [optional; concerns or alternatives the operator should know]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

This block is visible in the orchestration session but does not travel into
the execution session. The Envelope (without the Vendor Selection block) is
what the operator pastes.

**Why live, not Setup-baked.** Vendor capability shifts faster than
projects. A Setup-time vendor pick goes stale before dispatch on long
projects; a dispatch-time pick is current to the day. The cost (one web
search per dispatch) is small.

**SP-10 inheritance.** The principle is verify-state-before-recommending;
Vendor Selection is the named application. Other applications inherit:
point refresh (§{section.currency-maintenance-point-refresh}), Update sessions (§{section.currency-maintenance-update-session}), and any future recommendation
surface.

---

## 4. Prompt-package engine
<a id="section-prompt-package-engine"></a>

The prompt-package engine is the set of mechanics around how prompts are
shaped, dispatched, and reconciled. The triple contract (§{section.the-triple-contract}) is the
interface; this section is the dispatch logic that decides what to send,
how many vendors to send it to, how to read back what came in, and how to
handle failure.

### 4.1 Single-Envelope-with-spectrum shape `[structural | stable]`
<a id="section-single-envelope-with-spectrum-shape"></a>

A single Envelope shape across all dispatch shapes. The mode field tells
operator and vendor what kind of run this is.

`Dispatch shape:` carries one of three values: `equivalence`, `split`,
`limitation-named`.

**Mode semantics.**

- **`equivalence`** — dispatch the same prompt body to N vendors, expect
  comparable outputs. Orchestration's Vendor Triangulation fires at N≥2
  (§{section.vendor-triangulation}).
  - `Vendor:` field reads `multi-vendor`.
  - A `Vendor list:` sub-field enumerates the vendors and configs:
    ```
    Vendor list:
      - Claude Opus 4.7 / standard
      - Gemini Pro Deep Research / Deep Research ON
      - Perplexity / Sonar Pro
    ```
  - `Dispatch rationale:` carries one positive-framing line per vendor
    (§{section.rationale-discipline-per-dispatch-variant}).
  - The operator dispatches to each vendor sequentially or in parallel; each
    return carries its own Output signature. Orchestration tracks N expected
    returns.

- **`split`** — split the prompt into vendor-specific sub-prompts; each
  vendor gets a piece. Synthesis happens orchestration-side.
  - `Vendor:` field reads `multi-vendor (split)`.
  - The Envelope contains nested sub-Envelopes, one per piece, each with
    its own `Vendor`, `Vendor config`, `Attachments`, `Expected output`.
  - Parent declares synthesis approach: how the pieces compose (sequential
    dependency, parallel + merge, hierarchical).

- **`limitation-named`** — single vendor; explicit acknowledgment of what is
  intentionally not chosen and why.
  - `Vendor:` field reads the single vendor.
  - `Dispatch rationale:` includes a `Not chosen:` line naming the
    alternative considered and the analytical reason for not choosing it
    (per §{section.rationale-discipline-per-dispatch-variant} positive-framing rule). Not the access reason — the framework
    does not gate on operator vendor access (DD.§3.6).

**Content rule.** Envelope content carrying PRISM-native shorthand
follows the self-containment rule (§{section.atomic-prompt-self-containment}).

**Posture scope.** The three dispatch shapes are an *epistemic-posture*
partition — they describe how a prompt body distributes across vendors for
triangulation. An *investigation-posture* Envelope (a corpus-access lookup,
§{section.corpus-access-dispatch}, the external-reference-corpus lookup) carries
no dispatch shape at all: it retrieves material rather than distributing a prompt
for judgment. The `Posture:` field (§{section.prism-execution-envelope}, the
Execution Envelope) selects between the two; only `epistemic` Envelopes carry a
`Dispatch shape`.

### 4.2 Rationale discipline per dispatch variant `[methodological | stable]`
<a id="section-rationale-discipline-per-dispatch-variant"></a>

`Dispatch rationale:` field holds one positive-framing line per dispatch
variant component. Mobile-legible. No deficit framing.

**Per-mode templates.**

- *equivalence*:
  ```
  Dispatch rationale:
    Claude — analytical depth and red-team posture
    Gemini — long-context many-source synthesis
    Perplexity — live-web breadth and recency
  ```
- *split*:
  ```
  Dispatch rationale:
    Sub-1 (Claude) — claim adjudication
    Sub-2 (Gemini) — source-base assembly
    Synthesis (Claude) — merge into Layer-1 finding
  ```
- *limitation-named*:
  ```
  Dispatch rationale:
    Gemini — long-context source synthesis
    Not chosen: Claude — context window insufficient for this prompt's
                source base
  ```

**Discipline rules.**

- Each line ≤ 80 characters where possible (mobile legibility).
- Verb-first, value-first phrasing.
- "Not chosen" lines explain the analytical reason, not the access reason.

### 4.3 Vendor Triangulation `[structural | stable]`
<a id="section-vendor-triangulation"></a>

Vendor Triangulation is a Layer-1 convergence pass that fires when the
second return arrives in an `equivalence` dispatch. Re-fires as each
subsequent return arrives. Tracked via the Master's Dispatch register.
Triangulation integrity discipline is named in SP-15
(§{section.sp-15-triangulation-integrity}).

**Posture guard.** Vendor Triangulation fires only on *epistemic-posture*
`equivalence` dispatch. A *coverage fan* — `Fan: coverage (N)` on a
corpus-access lookup (§{section.corpus-access-dispatch}, the
external-reference-corpus lookup) — is investigation posture: the N vendors each
*retrieve* the same material rather than *reason over* it, so multiplicity buys
recall, not falsification across distributions. A coverage fan is handled by
recall-merge with a retrieval-consistency note and is **never** routed here.
Because an investigation-posture Envelope structurally lacks `Dispatch shape`,
this guard is mechanical, not a matter of operator discipline (SP-15,
§{section.sp-15-triangulation-integrity}).

**Lives outside the probe taxonomy.** Operates against returned findings,
not draft strategy. Single-responsibility separation from Probe 2
Adversarial Scope (§{section.probe-2-adversarial-scope-iterates}). Different surfaces (draft strategy vs returned
findings), different lifecycles (Setup-only vs per Layer-1 batch),
different output shapes (omission list vs agreement/divergence delta).

**Trigger.**

- N=1 return: ingested as a single finding, not triangulated. Master
  records `partial-equivalence: N/expected_N`.
- N=2: Vendor Triangulation fires. Convergence delta produced (§{section.convergence-delta-document}).
- N=3+: Re-fires; convergence delta updates incrementally.
- N=expected_N: Delta finalizes; Vendor Triangulation closes for this
  prompt.

#### 4.3.1 Convergence delta document
<a id="section-convergence-delta-document"></a>

```
━━━ VENDOR TRIANGULATION DELTA ━━━
Prompt ID:           [identifier]
Returns received:    N/expected_N
Vendors converged:   [list]

Agreement claims:    [findings agreed across all vendors]
Divergent claims:    [findings where vendors disagree; per-vendor citation]
Vendor-unique:       [findings only one vendor surfaced; per-vendor citation]
Method-significant:  [where divergence reflects vendor methodology, not subject content]

Operator action:     [recommended next step — accept, dig, or escalate]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Iterative re-firing.** Each new return triggers a re-run of the delta.
Old delta is replaced; the Changelog records the iteration.

**Delta finalization.** When all expected returns are in *and* no new return
is expected, the delta finalizes. The Master's findings section absorbs the
final delta.

### 4.4 Asymmetric parallel return handling `[structural | stable]`
<a id="section-asymmetric-parallel-return-handling"></a>

Convergence proceeds with whatever returned. Failed dispatches are flagged
with named gaps; operator decides whether to re-dispatch.

**Failure handling.**

- Operator declares a dispatch failed via the close-loop mechanic (§{section.operator-declaration-close-loop}):
  `P2.3 Gemini failed — Deep Research timed out`.
- Master's Dispatch register status: `failed: [reason]`.
- Vendor Triangulation proceeds with available returns. Convergence delta
  notes the dimension that's missing-due-to-failure:
  ```
  Vendor coverage gap: Gemini failed (timeout); Claude + Perplexity
  converged. Long-context many-source synthesis dimension is absent
  from this delta.
  ```
- *What's next* surfaces re-dispatch as a candidate at next turn-close,
  ranked by whether the gap materially affects the finding.

**No automatic retry.** Re-dispatch is an operator decision, surfaced as a
candidate. Per DD.§3.6 — design-authority-without-access-gating — the
framework does not assume the operator can retry on the same vendor.

### 4.5 Claude-baseline feasibility with named-limitation escape hatch `[vendor-dependent | review-if: vendor landscape changes]`
<a id="section-claude-baseline-feasibility-with-named-limitation-escape-hatch"></a>

Default execution stance is "Claude alone is feasible." Multi-vendor or
non-Claude is invoked via explicit declaration in the Prompt Strategy. The
named-limitation escape hatch (§{section.single-envelope-with-spectrum-shape} `limitation-named`) fires when Claude
is genuinely insufficient for the prompt shape.

**When non-Claude default escapes apply** (Vendor Selection refreshes per
dispatch):

- *Live-web breadth* — Perplexity (Sonar / Sonar Pro). Claude's web search
  exists but is shallower for breadth-recency tasks.
- *Long-context many-source synthesis* — Gemini Pro Deep Research. When
  source base materially exceeds Claude's context window.
- *Adversarial-style alternative reasoning* — ChatGPT o-series. When the
  strategy benefits from a structurally different reasoning posture for
  red-teaming.

**When multi-vendor (`equivalence`) is invoked.**

- Strategy declares it explicitly per prompt.
- Vendor Triangulation is the analytical goal.
- Operator strategy preference for a specific prompt class.

**Default behavior absent declaration.** Single-vendor Claude dispatch.

### 4.6 Cost signaling `[methodological | stable]`
<a id="section-cost-signaling"></a>

Implicit. No separate `cost:` field. Cost is signaled by:

- *Dispatch shape*: `equivalence` mode N=3 implies ~3× the operator effort
  and vendor-cost of single dispatch.
- *Vendor selection*: Gemini Deep Research is more time-expensive than
  Claude default; Vendor Selection's recommendation bubble (§{section.vendor-selection-at-dispatch}) carries
  this implicitly via mode rationale.
- *Mode rationale lines*: positive framing + named alternatives carry
  enough information for the operator to understand the cost tradeoff
  without an explicit field.

**Why no explicit field.** A `cost_estimate:` field would either be
inaccurate (vendor pricing changes faster than the framework) or
operator-specific (subscription tiers vary). Both fail the
contract-minimum test. Operator override: if operator wants explicit cost
framing in *What's next*, they can ask for it; orchestration produces it
on-demand.

### 4.7 Recommended-vs-executed reconciliation `[structural | stable]`
<a id="section-recommended-vs-executed-reconciliation"></a>

The Output signature carries `Vendor:` and `Vendor config:` reflecting
executed state. Orchestration auto-reconciles against the Envelope's
recommended state at Layer-1 ingestion.

**Reconciliation states** (recorded in the Dispatch register):

- *Match* — executed Vendor/config equals recommended. Status: `returned`.
- *Substitution* — executed Vendor or config differs. Status:
  `substituted`. Both recommended and executed values logged.
- *Missing* — no Output ever returned. Status: `failed` or `skipped` (per
  close-loop §{section.operator-declaration-close-loop}).

**Reconciliation algorithm** (orchestration-side, at Layer-1 ingestion):

```
1. Read Output signature fields: Executed Vendor, Executed Vendor config,
   Schema version, Prompt digest.
2. Look up Dispatch register entry for Prompt ID.
3. Verify Schema version compatible.
4. Verify Prompt digest equals the digest orchestration wrote into the
   dispatched Envelope (copy-through verification).
   - If mismatch: flag as "wrong prompt or wrong attachment" — operator
     escalation.
5. Compare Executed Vendor/config to Recommended Vendor/config.
   - If match: status = returned.
   - If differs: status = substituted; log both.
6. Ingest findings into Master's findings section with provenance:
   "P2.3 — executed on [Executed Vendor / config]; recommended was
    [Recommended]; absorbed without re-dispatch."
7. Vendor Triangulation (if equivalence mode) updates with this return.
```

### 4.8 Master tracking — Dispatch register `[structural | stable]`
<a id="section-master-tracking-dispatch-register"></a>

Master gains a `Dispatch register` table that tracks recommended-vs-executed
state per prompt. Required Master section (§{section.the-master}).

**Schema.**

| Prompt ID | Recommended (Vendor / config) | Executed (Vendor / config) | Status | Convergence ref |
|---|---|---|---|---|
| P2.3 | Gemini Pro DR / DR ON | Claude Opus 4.7 / standard | substituted | layer1-p2.3 |
| P2.4 | Claude Opus 4.7 / standard | — | dispatched | — |
| P2.5 | multi-vendor / equivalence | partial (2 of 3) | partial | layer1-p2.5 |

**Status values** (closed set):

- `dispatched` — Envelope produced; no return yet.
- `scheduled` — operator declared deferral (§{section.operator-declaration-close-loop}).
- `returned` — single-vendor return absorbed; Match.
- `substituted` — return absorbed; Vendor or config differs from
  recommended.
- `partial` — multi-vendor (`equivalence`) dispatch with N < expected_N
  returns absorbed.
- `failed` — operator declared failed (§{section.operator-declaration-close-loop}); reason recorded.
- `skipped` — operator declared skipped (§{section.operator-declaration-close-loop}); rationale recorded.
- `closed` — all expected returns received and convergence finalized.

**Status transitions** (machine-readable for orchestration's *What's next*
logic):

```
dispatched → returned | substituted | partial | failed | skipped | scheduled
scheduled → returned | substituted | partial | failed | skipped
returned → closed
substituted → closed
partial → returned | substituted | partial | closed (when expected_N met or operator declares closed)
failed → dispatched (re-dispatch) | skipped | closed
skipped → closed
```

### 4.9 Operator-declaration close-loop `[structural | stable]`
<a id="section-operator-declaration-close-loop"></a>

Defined declaration set. Each declaration closes an open dispatch in a
defined way.

**Declarations and effects.**

- **`Done`** — operator attached the Output. Triggers Output reconciliation
  (§{section.recommended-vs-executed-reconciliation}). Dispatch register status updates per §{section.master-tracking-dispatch-register}.
- **`Running later`** — dispatch deferred. Status: `scheduled`. Master keeps
  slot open. *What's next* surfaces it as a candidate at next turn-close
  (priority tier 8 per §{section.whats-next}).
- **`Skipping`** — dispatch abandoned. Status: `skipped`. Operator provides
  rationale (one line). Convergence absorbs the gap.
- **`Failed: [reason]`** — dispatch attempted but failed (vendor error,
  timeout, format failure). Status: `failed`. *What's next* surfaces
  re-dispatch as a candidate.
- **`Substituted: [vendor]`** — operator preempts auto-detection by
  declaring upfront. Status: `substituted`. Operator attaches the Output
  produced by the substitute vendor.

**Declaration syntax.** Free-form prose; orchestration parses for the
declaration keywords. Examples that orchestration recognizes:

- `P2.3 done` / `P2.3 — done, attached`
- `P2.3 running later` / `Will run P2.3 tomorrow`
- `P2.3 skipping — out of scope after P2.2 finding`
- `P2.3 failed — Gemini Deep Research timed out twice`
- `P2.3 substituted — ran on Claude instead, attaching now`

**Ambiguous declarations.** If orchestration cannot confidently parse the
declaration, M4 (Ambiguous Ask, §{section.m4-ambiguous-ask}) fires and asks the operator to
clarify before updating Dispatch register. SP-9 lineage.

### 4.10 Substitution absorption `[structural | stable]`
<a id="section-substitution-absorption"></a>

Substitution is absorbed at convergence; no re-dispatch demanded. Mechanics
integrate with §{section.recommended-vs-executed-reconciliation} reconciliation and §{section.master-tracking-dispatch-register} Dispatch register.

**Operating sequence.**

1. Output's `Vendor` field differs from Envelope's recommended `Vendor`.
2. §{section.recommended-vs-executed-reconciliation} reconciliation detects substitution; logs in Dispatch register with
   Status `substituted`.
3. Layer 1 convergence ingests the output as-is. Findings absorb into
   Master with provenance noting the substitution: *"P2.3 — executed on
   Claude (substituted from Gemini Pro DR recommendation); finding
   absorbed."*
4. If the prompt was `equivalence` mode, Vendor Triangulation delta notes
   the diversity collapse:
   ```
   Triangulation note: P2.5 was specified as equivalence/3-vendor.
   Returns received: 2 Claude (one substituted from Gemini), 1 Perplexity.
   Vendor-diversity dimension is reduced; cross-vendor convergence is
   weaker than designed.
   ```
5. *What's next* surfaces the diversity-collapse as a soft note. Operator
   decides whether the collapse materially affects confidence and whether
   to re-dispatch on the original recommended vendor.

**No automatic re-dispatch.** Per DD.§3.6 — substitution is an operator-
access reality the framework absorbs, not a defect the framework demands
be cured.

### 4.11 Prompt body convergence provisions `[structural | stable]`
<a id="section-prompt-body-convergence-provisions"></a>

Composition rules for the prompt body that make convergence orchestration-
side robust to partial returns.

**Composition rules.**

1. **Discrete attributable findings.** Each finding is self-contained:
   claim + evidence + provenance, in one paragraph or bullet. No finding
   depends on a prior finding having been received.
2. **Numbered/IDed sections.** Returns are sectioned (`Finding 1`,
   `Finding 2`, ...). Orchestration can ingest any subset by ID without
   re-issuing the prompt.
3. **No cross-section dependency.** A return that includes Findings 1, 2,
   4 (skipping 3) is valid and ingestable; orchestration absorbs what's
   there and notes the gap.
4. **Vendor-neutral phrasing.** No Claude-specific tool references in the
   body. Tool requests live in the Envelope's `Tools:` field.
5. **Evidence-class explicit.** Each finding names its evidence class (per
   LL schema field `evidence_class`): document, trace, probe,
   empirical-test, expert-interview, cross-check.
6. **Confidence calibration.** Each finding self-rates confidence on a
   3-point scale (low/medium/high). Calibration is *relative signal*, not
   ground truth — used for triangulation weighting in Vendor Triangulation.

**Required output structure** (the prompt body specifies this):

```
## Findings

### Finding 1 — [short title]
- Claim: [...]
- Evidence: [...]
- Provenance: [source, citation, date]
- Evidence class: [document | trace | probe | empirical-test | expert-interview | cross-check]
- Verification status: [verified | partially verified | unverified | not found]
- Confidence: [low | medium | high]
- Null results: [surfaces checked where nothing material was found; optional]
- Could not verify: [claims, sources, attachments, or tools unavailable/inconclusive; optional]
- Notes: [optional]

### Finding 2 — ...
```

**Verification ≠ confidence.** Verification status records what evidence
actually established the claim; confidence records the calibrated signal
strength. They are orthogonal axes: a high-confidence inference may be
*unverified* (no source confirmed it directly), and a *verified* finding
may be low-confidence because the source itself is ambiguous. Keeping
the axes separate is what v1.x's `[UNVERIFIED]` tagging gave up when
it was folded into confidence; v2.0.1 restores the separation explicitly.

**Null results and could-not-verify are first-class.** Surfaces where the
vendor checked and found nothing, and surfaces where the vendor could not
check at all (missing attachment, blocked tool, source paywalled), are
both load-bearing inputs to orchestration's convergence and Master
ingestion. They do not inflate finding count and they do not require a
claim. Empty / not applicable on a given finding is fine; orchestration
ingests the omission.

**Adaptable.** Where the prompt's analytical shape requires a different
finding structure, the prompt body specifies the alternative explicitly.
Default is the structure above.

**Self-containment.** Convergence across dispatch variants does not exempt
envelope content from the self-containment rule
(§{section.atomic-prompt-self-containment}); each variant's body remains
self-contained.

### 4.12 Atomic-prompt self-containment `[structural | stable]`
<a id="section-atomic-prompt-self-containment"></a>

Dispatched envelope text reaches executing vendors that may not share
PRISM context. PRISM-native shorthand (M-codes, SP-codes, monitor names,
claim IDs) carries strong competing priors in some vendors' training
distributions and will be misinterpreted when shipped bare. The atomic
prompt must be self-contained for the executing vendor.

**Rule.** Any PRISM-native shorthand appearing in dispatched envelope text
must carry an inline operational definition at first use within that
envelope. Subsequent uses within the same envelope may be bare.
Definitions need not be verbose — the shortest phrase that makes the
operative question clear is sufficient.

**Example.** Bare shorthand `M-monitor flags (M6 / M7 / M8 / M12)` gives
executing vendors no PRISM context. Inline-expanded *"M-monitor flags:
M6 (does the actual profile contradict DD Answers' placement?),
M7 (does anything else contradict the brief's framework?),
M8 (any stale attribution?),
M12 (any material gap not addressed?)"* gives the executing vendor the
operative questions directly.

**Rationale.** The fix is asymmetric: token cost is modest, eliminated
failure mode is systematic. Vendors with PRISM context
(orchestration-tier Claude with PRISM.md attached) are unaffected by the
rule because they already know the codes. Vendors without PRISM context
are protected.

**Scope.** The rule applies to M-codes
(§{section.monitor-specifications}), SP-codes
(§{section.standing-principles}), claim and anchor IDs introduced in the
envelope, and monitor names used as scrutiny gates (e.g., "apply M6
scrutiny"). It does not apply to vendor-native shorthand, common-language
terms, or Envelope field names themselves. Future PRISM-native shorthand
additions inherit this rule; the scope set here is illustrative, not
exhaustive.

**Bidirectional for corpus-access.** A corpus-access lookup
(§{section.corpus-access-dispatch}, the external-reference-corpus lookup) applies
self-containment in *both* directions. The `Question` goes out self-contained, as
any dispatched body must. The `Return` must also come *back* self-contained —
caveat-attached: a bare retrieved fact ("raised $12M Series A in 2019") stripped
of its source framing and temporal caveat is itself the silent-omission failure
the rule exists to prevent. Outbound the risk is bare shorthand; inbound the risk
is a bare fact.

**Optional template.** Operators may include a per-envelope glossary
block listing all codes referenced in that envelope and their
definitions, in lieu of inline expansion at first use. The glossary-block
pattern is operator discretion; the inline-at-first-use rule is the
framework default.

### 4.13 Corpus-access dispatch `[structural | review-if: corpus-access Phase 3 lands]`
<a id="section-corpus-access-dispatch"></a>

During a live engagement, a material question is sometimes best answered by an
*external reference corpus* — a startup-idea database, a pitch-deck library, a
funding-record service — rather than by a vendor reasoning from its own training.
Corpus-access dispatch is the **investigation-posture** Envelope that performs a
targeted lookup against such a source, scoped to the engagement's actual
question, and brings the result back caveat-attached. The corpus stays external
and is queried on demand; nothing is mined into the framework or a lens.

It is *investigation*, not execution: no prompt body is distributed across vendors
and there is no triangulation question, so the Envelope carries
`Posture: investigation` (§{section.prism-execution-envelope}, the Execution
Envelope) and none of the triangulation fields. That absence is what keeps a
retrieval step from masquerading as a judgment step.

**The Envelope.**

```
━━━ PRISM CORPUS-ACCESS ENVELOPE ━━━
Prompt ID:        [identifier — purpose/title]
Project:          [project name]
Master version:   [filename at dispatch]
Prompt digest:    [orchestration-generated; copy verbatim]
Posture:          investigation        ← no Dispatch shape exists
Source:           [named corpus]
Corpus kind:      narrative | structured-record
Source access:    open-web | operator-authenticated   ← routes the path
Driver:           vendor-executed | cowork-mcp | manual
Fan:              none | coverage (N)   ← coverage only; never equivalence
Tools:            web search ON [, Playwright]         ← vendor-executed path
Question:         [engagement question, scoped, self-contained]
Extract:          [exactly what to pull; fields / form]
Return form:      [finding structure]
Archive:          requested | none      ← screenshots / downloads / exports
Source framing:   [mandatory bias caveat — e.g. survivor bias]
Temporal frame:   [mandatory recency / coverage-window constraint]
Return handling:  [recall-merge; agreement = retrieval-consistency note]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Corpus-access fields.**

- `Source` — the named corpus (e.g. a startup-idea database, a funding-record
  service).
- `Corpus kind` — `narrative` (read/search corpora returning prose findings or
  artifact patterns) or `structured-record` (queryable databases returning
  records — funding rounds, comparable transactions). The kind conditions
  `Extract`, `Return form`, and `Temporal frame`; it is not a fork into two
  capabilities.
- `Source access` — `open-web` or `operator-authenticated`. Routes the lookup
  path (below).
- `Driver` — `vendor-executed | cowork-mcp | manual`. The locus that performs the
  retrieval (below).
- `Fan` — `none` or `coverage (N)`. A coverage fan retrieves the same material
  across N vendors for recall; it is **never** equivalence dispatch and never
  triangulates (see *Coverage fan*).
- `Tools` — on the vendor-executed path, the vendor tools the lookup requests
  (`web search ON`, optionally `Playwright`); rides the reserved `Tools:` slot
  (§{section.prism-execution-envelope}, the Execution Envelope).
- `Question` — the engagement question, scoped and **self-contained**
  (§{section.atomic-prompt-self-containment}, atomic-prompt self-containment): no
  bare PRISM shorthand, since the executing locus may not share PRISM context.
- `Extract` — exactly what to pull: fields/records for the structured-record
  kind, the prose finding or pattern for the narrative kind.
- `Return form` — the structure the finding comes back in (tabular for records,
  prose for narrative).
- `Archive` — `requested` or `none`. `requested` triggers the mandatory Exhibits
  manifest on return (§{section.prism-execution-output}, the Execution Output).
- `Source framing` *(mandatory)* — the bias caveat the source carries (e.g.
  survivor bias in a startup-idea corpus). Mandatory because a finding stripped of
  it is a silent-omission failure.
- `Temporal frame` *(mandatory)* — the recency / coverage-window constraint.
  Narrative corpora *age* (era-conditional vs durable: "is this stale?");
  structured-record databases are continuously updated ("what historical depth —
  does it cover my era?"). Same field, different question per kind.
- `Return handling` — how the return routes: recall-merge for a coverage fan,
  with agreement recorded as a retrieval-consistency note — never the Vendor
  Triangulation delta (§{section.vendor-triangulation}, Vendor Triangulation).

**Lookup-path `Driver` — a capability-local enum, distinct from the Axis-2
execution driver.** The corpus-access `Driver` answers a different question than
the Axis-2 execution-driver enum
(§{section.orchestration-driver-and-persistence-axes}, the orchestration / driver
/ persistence axes). Axis-2 (`manual | auto_drive`) governs *who moves the
Envelope into the execution vendor's chat* — the paste-driver. Corpus-access
`Driver` governs *what locus performs the retrieval against the source*. The two
compose orthogonally rather than collapsing: a `vendor-executed` lookup still
reaches the vendor via the paste-driver (Axis-2 `manual` today, `auto_drive`
later), so it is not a third Axis-2 value. The enum is therefore capability-local,
not an Axis-2 extension:

- `manual` — the operator runs the lookup in their own authenticated browser and
  pastes the result back. The universal fallback; coincides with Axis-2 `manual`
  (the operator does the legwork). Not surface-gated.
- `vendor-executed` — the lookup is dispatched to an execution vendor that
  performs it with its own **web search**, escalating to **Playwright**
  (vendor-side browser automation in its code-execution sandbox) when retrieval
  needs live page interaction. Rides the `Tools:` slot; orthogonal to the
  paste-driver. **Open-web only.** Not surface-gated.
- `cowork-mcp` — PRISM drives the Chrome MCP under the `cowork` surface
  (§{section.cowork-surface-capabilities}, the Cowork capability surface) to
  operate the source directly, including the operator's own authenticated session
  for paywalled sources. App-under-test-shaped, **not** `auto_drive`'s per-vendor
  machinery. `cowork`-gated; reserved for Phase 3.

**Path routing (by `Source access`).**

| Source access | Default path | Fallbacks | Barred |
|---|---|---|---|
| open-web | vendor-executed | cowork-mcp, manual | — |
| operator-authenticated | cowork-mcp | manual | vendor-executed |

The credential boundary is hard: a vendor-executed lookup is **open-web only**,
because authenticating a paywall would mean handing the operator's seat
credentials to an execution vendor, which is never done. Whether a given vendor
honors a `Playwright` request, and whether captured binaries return across the
dispatch boundary, is vendor-empirical — the same class as the Self-check
substrate-declaration items (§{section.prism-execution-self-check}, the Execution
Self-check): the Envelope *requests* the tool, the Self-check *confirms* what the
vendor actually has, and the rationale names the fallback.

**Coverage fan.** Fanning a lookup across N vendors looks like equivalence
dispatch, but posture decides routing, not vendor count. In a coverage fan the N
vendors each *retrieve* the same material — different web-search indexes surface
different sources — so multiplicity buys **recall**, not judgment. Agreement
across the fan is a **retrieval-consistency** signal ("this fact is robustly
findable") recorded as a note, never promoted to convergence. The marker is
`Fan: coverage (N)`, structurally distinct from `Dispatch shape: equivalence`, so
Vendor Triangulation cannot fire on it (§{section.vendor-triangulation}, Vendor
Triangulation). If the engagement then wants multi-vendor *judgment on* the
retrieved material, that is a *separate* `equivalence` dispatch with the retrieved
corpus as its attachment — epistemic posture, routed to Vendor Triangulation
normally.

**Self-containment is bidirectional here**
(§{section.atomic-prompt-self-containment}, atomic-prompt self-containment): the
`Question` goes out self-contained, and the `Return` must come back
caveat-attached — a bare fact stripped of its framing and recency caveat is itself
the silent-omission failure.

**Storage.** A corpus-access return is durable engagement state. Corpus-access
emits the bundle; the persistence axis (§{section.repo-backed-mechanics},
repo-backed mechanics) decides where it lives. Its archive value is fullest under
`repo_backed`, where exhibits survive across sessions and surfaces to reach the
eventual report; under `ephemeral` it degrades to the local or Cowork folder. Not
a hard dependency — a reason to recommend `repo_backed` whenever corpus-access is
in play.

**Lens-anchored auto-trigger.** Phase 1 waits to be told ("look this up in
[source]"); the lens-anchored auto-trigger lets orchestration recognize, on its
own, that a material question warrants a corpus lookup, and *propose* one. The
trigger is anchored to a lens: a lens carrying a `recommended_sources:` entry —
the Lens Library field that binds framework-curated external sources to the lens's
material question (§{section.library-integration}, the Library-integration surface
that bundles the Lens Library) — is, by virtue of that field,
trigger-capable.

*Recognition is the only automatic step.* Orchestration recognizes, on its own,
the conjunction of three conditions: **(i)** the lens is *in play* — it has fired
and its disposition is live; **(ii)** the engagement is actively working that
lens's `material_question:` (a prompt is being shaped against it, or a finding is
being sought for it); and **(iii)** a recommended source's `answers:` binding
matches that question. Nothing beyond this recognition becomes automatic.

*Dispatch stays advisory and operator-ratified.* Recognition produces a
**candidate dispatch, not a dispatch.** Orchestration shapes the
investigation-posture Envelope — every corpus-access field auto-populated from the
matched source record (below) — and surfaces it as a ready-to-ratify proposal,
e.g.: *"The LL-D-008 lens ('Compared to what?', the competitive-substitution lens)
is in play and your substitution question matches its recommended corpus,
ideas.rip. Here is a shaped corpus-access dispatch. Ratify to run, edit, or
skip."* The shaped Envelope is investigation posture, so it routes to a
recall-merge and never the Vendor Triangulation delta
(§{section.vendor-triangulation}, the convergence machinery — a coverage fan
retrieves, it does not triangulate). The operator ratifies, edits, or declines.
**Silence does nothing.**

*Squaring with SP-9.* The autonomy is in the recognition, never the dispatch.
SP-9 (§{principle.SP-9}, the "silence is never consent" Standing Principle)
forbids treating an absent objection as license to act; an auto-*dispatching*
trigger would spend operator resources — vendor calls, time, possibly
authenticated-session access — on inferred consent, violating it directly. An
advisory trigger requires the same explicit ratification SP-9 demands everywhere
else, reusing the framework's existing propose-then-ratify spine: the Layer-3
operator-ratification posture at the P0→P1 boundary
(§{section.three-layer-readiness}, the three-layer-readiness gate, whose Layer 3
parses for an explicit "ratify / approved / go" and treats silence as
non-ratification). No new consent model is introduced. Phase 1 is
operator-initiated ("look this up"); the auto-trigger is
orchestration-initiated-but-operator-ratified ("you'll want to look this up —
shall I?"). It moves the *initiative* to orchestration while leaving *authority*
with the operator.

**Auto-populate — closing the Phase 1 hand-written loop.** When the trigger fires,
the Envelope's corpus-access fields populate from the matched source record rather
than being hand-written each dispatch:

| Source record field | Envelope field | Effect |
|---|---|---|
| `source` | `Source` | identity |
| `kind` | `Corpus kind` | conditions Extract / Return form / Temporal frame |
| `access` | `Source access` | routes the `Driver` via the path-routing table above |
| `framing` | `Source framing` *(mandatory)* | bias caveat travels by default |
| `recency` | `Temporal frame` *(mandatory)* | recency / era posture travels by default |

This closes a loop Phase 1 left open. Phase 1 made `Source framing` and `Temporal
frame` mandatory on the Envelope but hand-written each time; the auto-trigger makes
them populate from recorded metadata, so the caveat is structurally impossible to
silently omit — the operator may still edit, but the default is caveat-attached.
It is the outbound half of the bidirectional self-containment point above
(§{section.atomic-prompt-self-containment}, atomic-prompt self-containment): the
`Question` already goes out self-contained, and now the *outbound caveat* travels
automatically too, so the bare-fact silent-omission failure is prevented at the
source rather than relying on hand-entry. This is also why the source record's
`framing:` and `recency:` are mandatory in the lens schema — a blank there would
become a blank in a *mandatory* Envelope field.

**Where a surfaced candidate lives, and the noise guard.** A surfaced-but-
unratified candidate is *What's next* material (§{section.whats-next}, the
*What's next* artifact — the open-loop surface that lists open options and asks the
operator, on the SP-9 "silence is never consent" lineage), **not** a
Dispatch-register entry (§{section.master-tracking-dispatch-register}, the
Dispatch register, which records actually-dispatched prompts). This keeps the
register clean and reuses the existing open-loop machinery rather than inventing a
parallel log. The candidate surfaces under *What's next*'s advisory, non-blocking
candidates, in this shape:

```
Corpus-access candidate (advisory):
  Lens:              [LL-code + name] — in play
  Material question: [the question being worked]
  Source:            [matched corpus]  (answers: [the matched binding])
  Shaped Envelope:   [investigation-posture Envelope, auto-populated]
  Disposition:       awaiting ratification | declined (turn [n])
```

A material-question-level trigger can fire often, and over-surfacing is its own
failure — the operator tunes out, which is silent omission in reverse. The noise
guard: **surface a candidate once per `{lens, source, material-question}` per
engagement; record a decline; re-surface only on a material change to the
question.** The re-surface predicate reuses the saturation test the framework
already applies to Library coverage at the P0→P1 boundary
(§{section.three-layer-readiness}, the three-layer-readiness gate — its Layer 2
reaches saturation when two consecutive iterations produce no material change to
coverage or strategy): a *material change* here is a shift in the question's
framing, scope, or the finding sought, enough that a prior decline no longer
settles it; a re-worded restatement of the same question does not re-surface. No
new bound is introduced.

**Phase status.** Phase 1 (the v2.6.0 release) made the `manual` and
`vendor-executed` paths operational under manual invocation ("look this up in
[source]" → orchestration shapes a self-contained investigation-posture Envelope →
the operator or an execution vendor runs it → the result returns caveat-attached,
with an Exhibits bundle where capturable). Phase 2 (this release) adds the
lens-anchored auto-trigger above: orchestration recognizes the need itself and
surfaces an operator-ratified candidate, rather than waiting to be told. The
`cowork-mcp` path remains defined-but-reserved (Phase 3, gated on the Cowork
substrate maturing), exactly as the `auto_drive` execution driver is reserved.

---

## 5. Context-pressure framework
<a id="section-context-pressure-framework"></a>

The context-pressure framework is the always-on background mechanism that
keeps long-running orchestration sessions honest about their own
degradation. Seven signals, qualitative compounding, four bands. Asymmetric
bet: the cost of running it is small (some Master bookkeeping); the cost of
not running it is a session that produces silently-wrong work because
recall has frayed.

### 5.1 Telemetric framework — signal weighting and compounding `[methodological | review-if: substrate shifts]`
<a id="section-telemetric-framework-signal-weighting-and-compounding"></a>

Qualitative compounding: each signal evaluated as *quiet*, *active*, or
*strong* per turn-close; band state computed from compounded signals via
rules below. Behavioral signals weight higher than volumetric.

#### Volumetric signals (weak-signal: alone they don't move bands)

1. **Attached content size** — total `.md` file content attached to the
   orchestration session.
   - quiet: < 50KB
   - active: 50–200KB
   - strong: > 200KB

2. **Conversation accumulation** — turn count + estimated message length in
   the orchestration session.
   - quiet: < 20 turns AND short-medium messages
   - active: 20–40 turns OR sustained long messages
   - strong: > 40 turns OR sustained very-long messages

3. **Reasoning accumulation** — extended thinking blocks accumulated
   in-session (proxy: explicit reasoning sections in turn-bodies,
   multi-step monitor cascades).
   - quiet: minimal reasoning per turn
   - active: sustained reasoning per turn, multi-monitor cascades visible
   - strong: every turn carries deep reasoning, monitor cascades dominate

#### Behavioral signals (strong-signal: one alone can move bands)

4. **Quality-degradation self-check** — orchestration's self-rating of its
   current cognitive sharpness (orchestration explicitly checks itself at
   turn-close).
   - quiet: "feels sharp; recall and synthesis intact"
   - active: "noticing some lag on cross-section recall; minor"
   - strong: "context-recall failing; producing inconsistent answers
     across turns"

5. **Task-completion friction** — observed friction in performing routine
   moves.
   - quiet: edits applying cleanly, cross-links intact, no repeated-ask
     pattern
   - active: occasional edit-not-applying, occasional re-ask of established
     state
   - strong: frequent edit failures, repeated requests to re-state
     established state, broken cross-references

6. **Platform UX signals** — vendor-side cues.
   - quiet: no compaction events, normal response times
   - active: response time stretching, occasional truncation warnings
   - strong: compaction events, repeated truncation, platform warnings

7. **Operator-reported signals** — operator declares state.
   - quiet: no signal
   - active: operator notes "feels slow" or "responses getting repetitive"
   - strong: operator declares "let's migrate" or names a specific failure

#### Compounding rules

| Compound signal pattern | Band assignment |
|---|---|
| All signals quiet | 🟢 |
| Two volumetric *active*, no behavioral | 🟢 → 🟡 |
| Two volumetric *strong* | 🟡 → 🟠 |
| One behavioral *active* | 🟢 → 🟡 |
| One behavioral *strong* OR two behavioral *active* | 🟡 → 🟠 |
| Operator-reported *strong* | 🟠 minimum (override floor) |
| Platform UX *strong* (compaction loop, repeated truncation) | 🟠 minimum |
| Two *strong* signals (any combination) | 🔴 |
| Operator-reported 🔴 | 🔴 (operator override is authoritative) |
| Three or more *active* signals across categories | 🟠 |

**Hysteresis** — bands de-escalate only after two consecutive turn-closes
show lower signal. Prevents flicker. Escalation is immediate.

**Calibration is empirical.** The thresholds above are rev. 1 draft
estimates. Real-use calibration is a post-release item (§{section.empirical-calibration-items}).

### 5.2 M5 — Context Pressure monitor `[structural | stable]`
<a id="section-m5-context-pressure-monitor"></a>

Single Monitor (§{monitor.M5}) absorbs the retired v1.x M12 (Conversation Pressure).
Fires at every orchestration turn-close.

**M5 spec.**

- **Trigger.** Every orchestration turn-close. M5 evaluates the seven
  signals (§{section.telemetric-framework-signal-weighting-and-compounding}) and assigns a band.
- **Output.** Band assignment as a header field on *What's next*:
  ```
  Context band: 🟡 — getting warm
  Driver(s): conversation-accumulation active; quality-self-check active
  ```
- **Fire emission discipline.**
  - 🟢: silent (no fire line; just header).
  - 🟡: advisory line — "Migration available at next natural seam."
  - 🟠: active line — "Curate now. Next natural seam: [seam]. Migration
    strongly recommended."
  - 🔴: handoff line — "Migration is the correct next action. Producing
    handoff (§{section.migration-handoff})."
- **Hysteresis** per §{section.telemetric-framework-signal-weighting-and-compounding}.
- **Interaction with other Monitors.** M5 fires regardless of other
  Monitors. When M5 ≥ 🟠, M5's curation-now directive ranks at priority
  tier 1 in *What's next* (above other Monitor fires).

### 5.3 Continuous-curation posture `[methodological | stable]`
<a id="section-continuous-curation-posture"></a>

From band 🟡 onward, every orchestration turn-close ends with a one-line
curation observation in *What's next*.

**Per-band curation behavior.**

- **🟢** — no curation note. No intervention.
- **🟡** — curation observation line:
  ```
  Curation: [what could be deprioritized in this session;
   what canonical state is worth migrating to fresh session if seam
   approaches]
  ```
- **🟠** — curation directive:
  ```
  Curation: ACTIVE. [specific items to deprioritize or compact now;
   specific seam to target for migration]
  ```
  Active curation in this band means orchestration:
  - Stops producing detailed exploratory reasoning unless asked.
  - Compacts state-summary output.
  - Defers non-essential probe iterations.
  - Pushes toward the next natural seam to enable migration.
- **🔴** — curation has been overrun. Migration is the action (§{section.migration-handoff}).

**Natural seams** (defined set):

- Convergence round complete (Layer-1 batch absorbed; Vendor Triangulation
  delta finalized).
- Phase boundary (P0→P1, P1→P2, etc.).
- Deliverable shipped (Layer 2 synthesis emitted).
- Setup iteration complete (P0.x finalized).

**Curation operations** (what orchestration deprioritizes or compacts):

- Verbose reasoning chains → terse conclusions.
- Multi-paragraph state summaries → bullet summaries.
- Tangential probe outputs → archived in Master, not re-summarized.
- Speculative What-if exploration → deferred to a fresh session.

### 5.4 Migration handoff `[structural | stable]`
<a id="section-migration-handoff"></a>

Defined handoff artifact. Produced by orchestration at 🔴 (mandatory) and
offered at 🟠 (operator-elective).

**Handoff format.**

```
━━━ PRISM SESSION HANDOFF ━━━
Project:                [name]
Master version:         [filename of attached Master]
Lens Library version:   [v0.14 | filename pinned]
Producing session:      [orchestration session URL or descriptor, if known]
Reason for migration:   [band-state, named driver(s)]
Migration timestamp:    [YYYY-MM-DD]

Current state summary:
  Active prompt(s):     [...]
  Open dispatches:      [from Dispatch register]
  Pending Adaptations:  [...]
  Active probes:        [Setup probes still iterating]

Open monitors:          [unresolved fires by Monitor ID]

What's next (current):
  [the current What's next artifact, pasted in full]

Operator state:         [optional operator note —
                         "I'm at lunch; resume with P2.5 tomorrow"]

Next session opens with:
  Attach: Master, Lens Library, this handoff.
  Read: this handoff first, then proceed per "What's next."
━━━ END SESSION HANDOFF ━━━
```

**Production discipline.**

- Produced at 🔴 automatically as the closing act of the orchestration
  session.
- Offered at 🟠 in *What's next* as a candidate next action: "Migrate now
  to fresh session — produce handoff?"
- Available at 🟢 / 🟡 on operator request.
- The handoff *plus* the current Master *plus* the Lens Library are the
  three artifacts the new session opens with attached. Together: complete
  context restoration.

**Handoff vs. Master.** The Master is canonical project state; the handoff
is migration context. The handoff is short (≤ 1 page) and points into the
Master for detail. New session reads the handoff first to orient, then
works with the Master as canonical reference.

### 5.5 Failsafe recovery — continuous-state mechanics `[structural | stable]`
<a id="section-failsafe-recovery-continuous-state-mechanics"></a>

"Always written" defined mechanically: Master and *What's next* are written
at every orchestration turn-close, regardless of band state, regardless of
whether the operator asks for them. Misreads of context band cost
essentially nothing because state is always recoverable.

**Mechanics.**

- **Master update at every orchestration turn-close.**
  - Always emitted at turn-close, regardless of whether material state
    changed. Continuous-state safety property (operator never picks the
    wrong Master because the latest is always the most recent emission)
    is preserved.
  - **No-state-change marker (v2.0.1).** When no material Master state
    changed during the turn (no Dispatch register change, no findings
    ingestion, no probe disposition change, no monitor state change, no
    strategy change, no new Changelog entry), the emitted filename
    carries the `_no_change` suffix immediately before the extension —
    e.g., `acme_audit_prism2.0_master_p2.3_no_change.md`. The operator
    can defer cloud-save and attachment-swap on these emissions; the
    prior Master remains current. This addresses mobile churn cost
    without giving up the always-emit safety property.
  - Append-mostly when content does change: Changelog gains a line;
    relevant register sections gain entries; Dispatch register status
    updates per §{section.master-tracking-dispatch-register}; findings sections absorb any newly-converged
    Layer-1 outputs.
  - Filename version bump only at phase boundaries or convergence-round
    increments (per §{section.filename-conventions-and-bump-atomicity} bump atomicity). The `_no_change` suffix is
    orthogonal to the version field — a no-change emission keeps the
    same version number as the prior content-bearing emission.
  - Operator must *download* the updated Master at session close when
    the emission is content-bearing (no `_no_change` suffix) to make it
    the authoritative canonical copy. (Manual step under v2.0.1
    plain-chat substrate.)
  - Cloud-drive save is the Operator hint emitted at every
    content-bearing turn-close: `Save Master to cloud drive (§{section.mobile-operator-survival-guide} MO-5).`

- ***What's next* rewrite at every orchestration turn-close.**
  - Replaces in place; no history kept (Changelog carries the historical
    pointer).
  - Always reflects the current state, not a future or planned state.
  - Operator reads *What's next* as the sole source of "what to do next" —
    not by scrolling chat, not by reading the Master in detail.

**Consequence — asymmetric bet.**

- If the framework misreads band: operator migrates → fresh session
  attaches Master + handoff + Lens Library → work continues, no loss.
- If the framework reads correctly: the recovery infrastructure wasn't
  needed but wasn't costly either (writing the Master + *What's next* is
  part of the orchestration turn anyway).
- If the operator declines to migrate at 🔴: operator-discretion override
  (the framework cannot force migration); the framework continues but
  flags continuing-at-🔴 in *What's next* and increments a turn-counter
  that escalates the migration recommendation.

### 5.6 Defensive migration at natural seams `[structural | stable]`
<a id="section-defensive-migration-at-natural-seams"></a>

Migration posture keyed to band × seam.

| Band | Migration posture | Seam discipline |
|---|---|---|
| 🟢 | Available | At any natural seam; no urgency. Operator-elective. |
| 🟡 | Recommended | At the next natural seam; if no seam approaching, finish current sub-task to create one. |
| 🟠 | Strongly recommended | At the immediate next opportunity; framework actively closes current curation to reach a seam. |
| 🔴 | Correct action now | Framework produces handoff (§{section.migration-handoff}); operator opens fresh session and attaches handoff + Master + Lens Library. |

**Operator override.** Operator can decline migration at any band.
Framework respects but flags continuing-at-band in *What's next*. At 🔴,
the per-turn flag escalates to a migration-overdue counter.

---

## 6. Setup mechanics
<a id="section-setup-mechanics"></a>

Setup is iterative refinement against the Lens Library. Not waterfall. The
P0→P1 boundary clears when three independent layers all read ready
simultaneously.

### 6.1 From waterfall to library-graded iterative refinement `[structural | stable]`
<a id="section-from-waterfall-to-library-graded-iterative-refinement"></a>

**Setup iteration loop.**

1. Operator provides initial subject brief.
2. Orchestration produces draft Prompt Strategy P0.1.
3. Probes 6, 7 iterate early in P0.1 (Domain Reconnaissance + User Voice);
   Probes 1, 2, 4 iterate per turn; Probes 3 and 5 run once.
4. Probe 1 (Coverage grading) outputs tri-state dispositions per Lens
   (§{section.probe-1-coverage-grading-iterates}).
5. Operator reviews probe outputs.
6. Orchestration produces P0.2 incorporating closures.
7. Repeat until §{section.three-layer-readiness} readiness clears.

**Iteration numbering** — P0.1, P0.2, …. No artificial cap. Floor: minimum
2 iterations. Soft ceiling: at 4 iterations without saturation, flag
*something structural may be wrong — operator intervention recommended*.

### 6.2 Three-layer readiness `[structural | stable]`
<a id="section-three-layer-readiness"></a>

All three layers must clear before P0 → P1 boundary.

#### Layer 1 — Structural completeness

Every planned prompt has the following fields populated:

- Single objective (one-sentence statement).
- Output format (structured findings per §{section.prompt-body-convergence-provisions}).
- Dependency list (which prior prompts' outputs are inputs; can be empty).
- Attachment map (filenames per attachment).
- Enrichment decision (single-vendor / equivalence / split /
  limitation-named).
- Execution envelope (full Envelope per §{section.prism-execution-envelope}).

Verification: orchestration walks the strategy and confirms each prompt has
all six fields. Any missing field halts P0 → P1.

#### Layer 2 — Library coverage saturation

Every applicable Lens from the Lens Library v0.14 is either:

- Covered by at least one planned prompt (Probe 1 disposition:
  *fires-covered*), OR
- Explicitly marked out of scope with rationale (Probe 1 disposition:
  *doesn't-fire* with rationale captured, OR *fires-maybe* closed via
  *opt-out* per §{section.probe-1-coverage-grading-iterates}).

**Saturation signal.** Two consecutive iterations produce no material
change to coverage or strategy.

**Material change criteria.**

- New Lens added to coverage map (P0.x → P0.x+1).
- Existing Lens disposition changes from *fires-uncovered* to
  *fires-covered* (or *opt-out*).
- New planned prompt added or merged.
- Prompt's Vendor or Vendor config changed.

If two consecutive iterations show none of the above, saturation reached.

#### Layer 3 — Operator ratification

Operator confirms the strategy matches intent. Free-form confirmation;
orchestration parses for explicit ratification ("ratify", "approved", "go",
"looks good — proceed"). SP-9 lineage: silence is not ratification.

**Ratification triggers P0 → P1.** Master filename bumps to P1 (e.g.,
`acme_audit_prism2.0_master_p1.0.md`). Setup probes close. Strategy moves
to "presumed stable, revisable at convergence" per §{section.strategy-stability}.

### 6.3 The seven probes
<a id="section-the-seven-probes"></a>

Probes operate against the draft Prompt Strategy at Setup. Vendor
Triangulation (§{section.vendor-triangulation}) — convergence-time cross-vendor reconciliation —
lives outside the probe taxonomy because it operates against returned
findings, not draft strategy. Result Completeness Check (§{monitor.M12}, §{section.m12-result-completeness-check}) is
a convergence-time monitor. Single-responsibility discipline: probes are
Setup-time grading constructs only.

#### 6.3.1 Probe 1 — Coverage grading (iterates) `[structural | stable | ✅]`
<a id="section-probe-1-coverage-grading-iterates"></a>

Grade the draft strategy against the Lens Library v0.14. Universal lenses
(5) always evaluated. Domain lenses (18) evaluated where their `trigger:`
predicate is met by the subject.

**Per-lens disposition** (tri-state with maybe sub-state):

- **`fires-covered`** — lens applies, draft already covers it, and the
  Scope-Integrity Test passes (see below). Silent pass; recorded for
  audit trail.
- **`fires-uncovered`** — lens applies, draft does not cover it. Surfaces
  as a flag; closed by adding coverage in next iteration.
- **`doesn't-fire`** — trigger predicate not met; rationale captured (one
  line).
- **`fires-maybe`** — applicability or coverage ambiguous.
  - **`fires-maybe — dig-in`** — judging LLM does targeted research on the
    lens-subject intersection. Produces an expanded lens framing or a
    scoped specialist pass to add to the strategy. Closes by becoming
    *fires-covered* in next iteration.
  - **`fires-maybe — opt-out`** — documented exclusion with rationale.
    Closes by becoming a recorded out-of-scope decision.

**Scope-Integrity Test — the `fires-covered` gate.** A lens cannot be
marked `fires-covered` on assertion alone. Before the disposition is
recorded, restate the lens's own `minimum_scope_binding:` as a yes/no
falsifier — *every clause satisfied with evidence, or any clause unmet?* —
and answer it in context. A clause-by-clause pass is required; any unmet or
undocumented clause forces `fires-uncovered` (or a documented
`fires-maybe — opt-out`) instead. A lens carrying a `scope_integrity_probe:`
field uses that sharpened falsifier in place of the generic restatement.
This inline self-check is the always-on floor of the Scope-Integrity Test;
its rigor ladder and home are specified in §{section.scope-integrity-test-sit}.

**Disposition output format** (per turn-close in P0):

```
━━━ PROBE 1 — COVERAGE GRADING ━━━
Iteration: P0.x
Universal lenses (5):
  LL-U-001 Who gets hurt?           — fires-covered (P2.1)
  LL-U-002 What's the thesis?       — fires-covered (decision brief)
  LL-U-003 What would refute?       — fires-uncovered (FLAG)
  LL-U-004 Who acts on this?        — fires-covered (decision brief)
  LL-U-005 What laws touch this?    — fires-maybe → dig-in
Domain lenses (triggered):
  LL-D-002 Can anyone use?          — fires-covered (P3.4 a11y pass)
  LL-D-005 Can attackers get in?    — fires-uncovered (FLAG)
  LL-D-011 Is data handled lawfully? — fires-maybe → opt-out
                                       (rationale: subject is read-only
                                       informational service; no PII)
  ...
Domain lenses (not triggered):
  LL-D-016 Is the ledger safe?      — doesn't-fire (no custody/payments)
  ...
Saturation flag: not-yet (3 changes from P0.2)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Operator-fatigue mitigation.** Judging LLM resolves clear cases silently
(covered or doesn't-fire with obvious rationale). Escalates to operator
only on genuine ambiguity (*fires-maybe* requiring dig-in vs. opt-out
decision). Empirical calibration deferred — see §{section.empirical-calibration-items}.

#### 6.3.2 Probe 2 — Adversarial Scope (iterates) `[structural | stable | ✅]`
<a id="section-probe-2-adversarial-scope-iterates"></a>

Hunt for silent omissions and under-scoped treatments in the draft Prompt
Strategy. Library-driven (uses Library entries as starting prompts but
goes beyond catalog); informed by domain context.

**Lifecycle.** Setup-only. Iterates per P0.x turn-close. Does not fire at
Layer-1 convergence — cross-vendor finding triangulation is a separate
mechanism (Vendor Triangulation, §{section.vendor-triangulation}) with its own trigger and output
shape.

**Multi-vendor recommendation.** Independent adversarial passes across
vendors; divergence between passes is signal about scope blind spots. Not
the same as cross-vendor finding reconciliation.

**Output.** List of silent-omission candidates the strategy did not
address. Operator reviews; orchestration converts surviving candidates
into Lens references or new prompt additions in the next iteration.

#### 6.3.3 Probe 3 — Decision Framing (once) `[structural | stable | ✅]`
<a id="section-probe-3-decision-framing-once"></a>

Does the strategy answer what the stakeholder actually needs to decide?

Outputs the Decision brief and Stakeholder register Setup artifacts
(§{section.decision-brief}, §{section.stakeholder-register}).

#### 6.3.4 Probe 4 — Pre-mortem (iterates) `[structural | stable | ✅]`
<a id="section-probe-4-pre-mortem-iterates"></a>

Imagine execution completes. How would the finding fail to answer the
original question?

**Output.** A list of pre-mortem failure modes; each surviving mode either
becomes a new probe in the strategy or is dismissed with rationale.

#### 6.3.5 Probe 5 — Falsifier (once) `[structural | stable | ✅]`
<a id="section-probe-5-falsifier-once"></a>

What findings would invalidate the thesis?

**Output.** Decision brief gains a Falsifiers section listing findings
that, if observed, would refute the thesis. These become explicit
success/failure criteria for Layer 2 synthesis.

#### 6.3.6 Probe 6 — Domain Reconnaissance (iterates early) `[structural | stable | ✅]`
<a id="section-probe-6-domain-reconnaissance-iterates-early"></a>

What do practitioners, researchers, and serious analysts of this domain
actually investigate? What lenses does the domain's own literature treat
as default?

**Imports domain-external signal that the Library cannot carry.**

Asks whether an authoritative canonical source exists for the domain:

- Regulated registry?
- Standards body with testable criteria?
- Curated research corpus?
- Benchmark dataset?

If yes: strategy brings it in as primary evidence; Probe 6 outputs a
citation.

**Multi-vendor recommended.** Different vendors have different exposure to
domain-specific literature.

Outputs the Jurisdiction map Setup artifact (§{section.jurisdiction-map}).

#### 6.3.7 Probe 7 — User Voice (iterates early) `[structural | stable | ✅]`
<a id="section-probe-7-user-voice-iterates-early"></a>

Imports real end-user / customer / affected-user perspectives into Setup.
Mines actual user signal from forums, reviews, support tickets, public
commentary, social platforms — whatever surfaces are available for the
subject's user base.

**Why a probe.** Strategies built only on the project brief plus Library
lenses risk being shaped by what the framework *expects* users to care
about rather than what they actually do. User Voice surfaces friction
points, pain patterns, and lived-experience signal the brief misses.

**Lifecycle.** Setup-only. Iterates early in P0 alongside Probe 6 (Domain
Reconnaissance) — both import external signal before the strategy hardens.

**Multi-vendor recommended.** Different vendors have different exposure to
user-generated content (Perplexity is strong on live web; Claude on
synthesis from quoted text; Gemini on long-context corpus).

**Output.** A list of user-surfaced concerns, friction points, and
reality-checks that feed the strategy. Surviving items either become new
prompts, become flagged-for-coverage Library lenses, or refine the
Decision brief's stakeholder section.

**v1.x lineage.** v1.x had User Voice as a Phase 2 enrichment role
("mine real user perspectives — reality check"). v2 promotes it to Setup
probe so user signal informs strategy *before* execution rather than
enriching findings *after*.

#### 6.3.8 Probe ordering — recommended sequence
<a id="section-probe-ordering-recommended-sequence"></a>

P0.1: Probe 6 (Domain Reconnaissance — establishes domain context); Probe
7 (User Voice — imports user signal); Probe 1 (initial coverage); Probe 3
(Decision Framing).
P0.2: Probe 4 (pre-mortem); Probe 1 (re-grade); Probe 2 (adversarial
scope).
P0.3: Probe 1 (re-grade for saturation); Probe 5 (falsifier).
P0.4+: Probes 1, 2, 4, 6, 7 iterate as needed until saturation.

Order is a default; operator may re-sequence per project shape.

**Probe taxonomy notes.** P5 Consolidation (rev. 1 of the spec) dissolved —
structural overlap-spotting is judgment work the LLM does inside Probe 1
and Probe 2 grading rather than a checkbox-shaped standalone probe.
Aligns with v2's principle-heavy / specification-light philosophy. Vendor
Triangulation extracted from rev. 1's Probe 2 and lives in §{section.vendor-triangulation}, not in
the probe taxonomy.

### 6.4 Setup artifacts
<a id="section-setup-artifacts"></a>

Four instance-specific artifacts populated during Setup. Live in the
Master (§{section.the-master} required sections).

#### 6.4.1 Decision brief
<a id="section-decision-brief"></a>

Populated by Probe 3 primarily; refined by Probe 5 (Falsifiers section).

```
## Decision brief

Subject:           [name]
Decision under test: [one sentence]
Decision-maker:    [name or role]
Deadline:          [date or trigger]
Cost of error:    
  - False positive: [cost]
  - False negative: [cost]
Stakes / blast radius: [one paragraph]
Falsifiers:        [list — findings that would refute the thesis]
```

#### 6.4.2 Stakeholder register
<a id="section-stakeholder-register"></a>

Populated by Probe 3 primarily.

```
## Stakeholder register

| Role | Stake | Decision power | Communication channel |
|---|---|---|---|
| [name] | [decision/outcome stake] | [yes/advisory/none] | [channel] |
| ... | ... | ... | ... |
```

#### 6.4.3 Claim inventory
<a id="section-claim-inventory"></a>

Populated by Setup orchestration as it parses subject brief; refined by
Probe 6 (Domain Reconnaissance).

```
## Claim inventory

| Claim type | Specific claim | Source | Audit pass(es) |
|---|---|---|---|
| Efficacy | [...] | [where claim is made] | P2.x |
| Compliance | [...] | [...] | P3.x |
| Positioning | [...] | [...] | P4.x |
| ... | ... | ... | ... |
```

#### 6.4.4 Jurisdiction map
<a id="section-jurisdiction-map"></a>

Populated by Probe 6 (Domain Reconnaissance) primarily.

```
## Jurisdiction map

| Jurisdiction | Triggered regimes | Material to scope? | Pass(es) |
|---|---|---|---|
| US (federal) | FTC, ADA | yes | P3.1 |
| EU | GDPR, EU AI Act | yes | P3.2 |
| US-CA | CCPA/CPRA | yes | P3.1 |
| ... | ... | ... | ... |
```

### 6.5 Strategy stability `[structural | stable]`
<a id="section-strategy-stability"></a>

**At P0 → P1 boundary.** Strategy moves to "presumed stable, revisable at
convergence."

**Convergence-time strategy revisions** trigger when Layer-1 convergence
produces:

- A premise invalidation (§{monitor.M6} Premise Shift fires HIGH).
- A newly-surfaced domain area (e.g., a regulatory regime not in the
  Jurisdiction map).
- A falsifier hit (one of the Decision brief's Falsifiers is observed).
- An assumption conflict between two findings (§{monitor.M7}).

**Revision mechanic** (lighter than v1.x major-bump Adaptation).

1. Convergence finding triggers Monitor (§{monitor.M6} / M7) HIGH.
2. Orchestration drafts a revision: adds/modifies prompts, updates attach
   maps, updates Setup artifacts as needed.
3. Operator ratifies (per Layer 3 §{section.three-layer-readiness}).
4. Master version increments (sub-version bump within phase, e.g., P2.2
   → P2.3).
5. Strategy continues with revised state.

**Attach map travels with each prompt.** When a prompt adapts, its attach
map adapts with it (§{section.prism-execution-envelope}).

---

## 7. Library integration
<a id="section-library-integration"></a>

The Lens Library v0.14 is canonical and bundled at
`lens/PRISM_lens_library.md` (tag `prism-lens-v0.14`). In this Skill
archive the Library is a bundled file fetched on demand — the default
Library source for orchestration — not embedded in the core. The bundled
file is also authoritative for the artifact's own evolution: Update
sessions (§{section.currency-maintenance-update-session}) produce new versions of it. Operators on a newer
Library version pin to it explicitly (§{section.library-reference-at-setup}).

### 7.1 Library reference at Setup `[structural | stable]`
<a id="section-library-reference-at-setup"></a>

**Required Library source.** By default, orchestration fetches the bundled
Lens Library v0.14 (`lens/PRISM_lens_library.md`, tag `prism-lens-v0.14`)
on demand. A newer standalone Library version is used only when the
operator explicitly pins the project to it, overriding the bundled copy
for that session. Recommended: if a newer Library is used, live in the
Claude Project alongside the Master (see §{section.claude-project-as-setup-recommendation}).

**Probe 1 grades against Library entries.** Mechanics in §{section.probe-1-coverage-grading-iterates}.

### 7.2 Lens schema — what orchestration consumes
<a id="section-lens-schema-what-orchestration-consumes"></a>

Per LL.§Schema:

- `id:` — identifier orchestration uses to reference the lens.
- `name:` — short colloquial title for human-legible operator output.
- `material_question:` — the question Probe 1 grades the strategy against.
- `tier:` — universal | domain. Universal always-evaluated; domain
  evaluated when trigger predicate met.
- `trigger:` — predicate the judging LLM evaluates against the subject for
  domain lenses.
- `evidence_class:` — one of {document, trace, probe, empirical-test,
  expert-interview, cross-check}. Used in finding output structure
  (§{section.prompt-body-convergence-provisions}).
- `specialist_type:` — open taxonomy. Used by judging LLM to promote
  relevant entries as specialist passes under Probe 1.
- `rubric_anchor:` — optional; version-pinned external spec where present.
  Two entries at v0.9 (§{lens.LL-D-002} "Can anyone use?" — WCAG 2.2; LL-D-005 "Can attackers get in?" — OWASP ASVS 5.0.0).
- `last_verified:` — populated on entries with `rubric_anchor:`.
  Maintenance signal per §{section.currency-maintenance-point-refresh}.
- `verification_basis:` — populated on entries with `last_verified:`;
  one of `{schema-introduction-only, independent-review}`. Gates §{section.currency-maintenance-point-refresh}
  freshness logic so a schema-introduction date is not silently treated
  as a performed currency check (v0.10).
- `informed_by:` — provenance only; not a runtime rubric.
- `failure_mode:` — used in operator-facing flag explanations.
- `minimum_scope_binding:` — what counts as "covered" for Probe 1
  disposition.
- `scope_integrity_probe:` — optional sharpened falsifier. When present on a
  lens, the Scope-Integrity Test (§{section.scope-integrity-test-sit}) poses it
  in place of the generic `minimum_scope_binding:` restatement when grading
  that lens to `fires-covered`.

### 7.3 Scope-Integrity Test (SIT) `[structural | stable]`
<a id="section-scope-integrity-test-sit"></a>

A lens's `minimum_scope_binding:` *states* what coverage requires; it does not
*enforce* it. Probe 1 (§{section.probe-1-coverage-grading-iterates}) can mark a
lens `fires-covered` on the strength of an enumeration that looks complete but
quietly scoped the question too narrowly. The **Scope-Integrity Test (SIT)** is
the enforcement layer: a coverage-time falsifier gate that the binding was
actually satisfied, not waved through. PRISM is an orchestration layer, not
running code, so SIT is a prompt-level adversarial question that gates coverage —
not a test runner.

**The failure it prevents.** The cleanest case is the category-vs-audience
substitution trap that §{lens.LL-D-008} "Compared to what?" already names in its
`failure_mode:`. A competitor scan scoped by *product category* — rather than by
*audience and job* — can converge on a confident "this is unique" finding while a
same-audience substitute in a different form factor (a hardware device, a manual
workflow, a do-nothing default) goes unnamed. Enumeration depth does not catch
this; more passes inside the wrong scope only harden the wrong boundary. The miss
is structural, so the check is structural — applied at the moment coverage is
claimed.

**Mechanism — a rigor ladder.** SIT runs at one of three rigor levels; the
operator escalates by stakes.

1. **Inline self-check (the floor — always on).** Before Probe 1 records
   `fires-covered`, the orchestrator restates the lens's `minimum_scope_binding:`
   as a yes/no falsifier and answers it in context: *has every clause been
   satisfied with evidence, or is any clause unmet?* Coverage is invalid without a
   structured falsifier-response. This is a **floor, not triangulation**: the same
   agent that did the enumeration is certifying its own work — the
   single-distribution trap SP-15 (Triangulation integrity,
   §{section.sp-15-triangulation-integrity}) warns about. Naming that limit
   honestly is part of the mechanism.
2. **Fresh-context probe (independent, single-vendor).** Dispatch the falsifier to
   a context that did *not* perform the enumeration. A fresh context catches what
   self-certification cannot, but it shares the orchestrator's training
   distribution, so it is the *minimum* independent rigor, not full triangulation.
3. **Cross-vendor probe (independent, cross-distribution).** Dispatch the falsifier
   to a different vendor. Distinct priors and failure modes make this **full SP-15
   triangulation** (§{section.sp-15-triangulation-integrity}) — the strongest
   level.

Levels 2 and 3 are operator-invokable today in a single chat: dispatch the probe
as its own prompt to a fresh context or a second vendor. A future `auto_drive`
execution driver (§{section.orchestration-driver-and-persistence-axes}) would only
*automate* that dispatch; it is not a prerequisite, and the SIT path carries no
`auto_drive` dependency.

**Home — lens-anchored, at coverage time.** SIT lives where coverage is marked:
the Probe 1 disposition gate (§{section.probe-1-coverage-grading-iterates}). It is
**not** a Monitor (those scan continuously) and **not** a Standing Principle (those
are posture). SIT is mechanical and condition-triggered — it fires exactly when a
lens is about to be marked covered — so it is anchored to the lens and the grading
step, not to the always-on machinery.

**Scope — a generic gate for all 23 lenses, plus optional sharpened probes.**

- **Generic gate (day one, every lens).** The falsifier is the lens's own
  `minimum_scope_binding:`, restated as the yes/no challenge above. Free,
  full-scope, runs immediately.
- **Sharpened per-lens probe (`scope_integrity_probe:`).** A lens may carry a
  `scope_integrity_probe:` field (§{section.lens-schema-what-orchestration-consumes})
  — a falsifier sharpened to that lens's known failure. When present it
  **overrides** the generic restatement for that lens. Additive: lenses without it
  use the generic gate.
- **First probe ships on §{lens.LL-D-008} "Compared to what?".** The one lens with
  a ground-truth worked miss carries the first hand-authored probe; its
  `scope_integrity_probe:` requires naming a cross-form-factor audience-job
  substitute the comparator set omits, or documenting its absence with rationale.
  The other 22 ride the generic gate. Sharpened probes accrete over time: a lens
  earns one when a live engagement surfaces a miss the generic gate let through.

### 7.4 Specialist-pass promotion
<a id="section-specialist-pass-promotion"></a>

The Library *is* the specialist enumeration. Each lens's `specialist_type:`
field names the practitioner role whose framing the lens channels.
Orchestration's Probe 1 grading promotes relevant entries as specialist
passes within the Prompt Strategy (e.g., "P3.4 — accessibility pass per
LL-D-002 "Can anyone use?", specialist framing: WCAG-qualified accessibility auditor").

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
          via web search; PRISM Lens Library v0.14 last_verified
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

## 9. Monitor specifications
<a id="section-monitor-specifications"></a>

All Monitors fire orchestration-side. Twelve Monitor slots specified;
v1.x M12 (Conversation Pressure) retired and absorbed into M5; the M12
slot reused in v2 for Result Completeness Check. Three presentation
groupings.

**Dispatched-text note.** M-codes are PRISM-internal labels. When used
in dispatched envelope text reaching executing vendors, they require
inline expansion per §{section.atomic-prompt-self-containment}.

### 9.1 Standalone monitors (M1, M2, M4, M5, M9)
<a id="section-standalone-monitors-m1-m2-m4-m5-m9"></a>

#### 9.1.1 M1 — Missing Inputs `[structural | stable | ⚠️]`
<a id="section-m1-missing-inputs"></a>

- **Trigger.** Every orchestration session-open and turn-close.
- **Detects.** Required attachments missing from current orchestration
  session; attachments declared in Envelopes but not present in returned
  Outputs (via §{section.operator-hint-catalog} Attachment warnings).
- **Severity.** HIGH on missing canonical attachments (Master, Lens
  Library, Prompt Strategy if separate). MEDIUM on missing prompt-specific
  attachments. LOW on schema mismatches.
- **Resolution.** Halt until attachments provided; or operator confirms
  intentional absence.

#### 9.1.2 M2 — Version Drift `[structural | stable | ⚠️]`
<a id="section-m2-version-drift"></a>

- **Trigger.** Every orchestration session-open. Compares attached
  Master's metadata header to expected.
- **Compare against.** The version *What's next* predicted at last close
  (orchestration sees its own prior closing turn via session history if
  available; else operator declaration).
- **Fire conditions.**
  - Attached Master version < expected: HIGH (older than expected;
    rollback risk).
  - Attached Master version > expected: HIGH (newer than expected; ghost
    session ran in between).
  - Schema version mismatch: HIGH.
  - Attached Master == expected: silent pass.
- **Resolution.** M2 HIGH halts orchestration until operator clarifies.
  Optional: consult session history per §{section.session-history-as-validation-recovery}.
- **Framework-stamp clarification (operator-ratified, 2026-06-05).** The fire
  conditions above evaluate the *Master's project-state version*, not the
  *framework version* the Master was stamped under. A Master stamped under a
  framework **older** than the running session's is **not** drift: by PRISM's
  SemVer contract the running framework is a behavior-preserving superset of
  the older stamp, so M2 does not fire — orchestration proceeds (optionally
  surface a 🟢 advisory note; no halt). This pins a case the conditions above
  left undefined; it adds no halt.

**Why retained despite bump atomicity (§{section.filename-conventions-and-bump-atomicity}).** Bump atomicity makes drift
unlikely *by construction* but not impossible. Residual failure modes:

- Operator attaches an old Master from cloud archive by mistake.
- OS-level filename collisions serve a stale file.
- Cross-device syncing serves a previous version.
- Multiple Masters from forked sessions (anti-pattern but not impossible).

#### 9.1.3 M4 — Ambiguous Ask `[methodological | stable | ⚠️]`
<a id="section-m4-ambiguous-ask"></a>

- **Trigger.** Every orchestration turn that processes operator input.
- **Detects.** Operator declaration that orchestration cannot confidently
  parse (close-loop §{section.operator-declaration-close-loop} ambiguity; intent unclear; conflicting
  instructions).
- **Severity.** HIGH if the next action depends on the ambiguity. LOW if
  orchestration can proceed and clarify post-hoc.
- **Resolution.** Orchestration explicitly asks for clarification before
  proceeding. SP-9 lineage: silence not consent.
- **No execution mirror.** Execution sessions receive pre-resolved
  dispatched prompts; M4 is orchestration-only.

#### 9.1.4 M5 — Context Pressure `[structural | stable]`
<a id="section-m5-context-pressure"></a>

Spec per §{section.m5-context-pressure-monitor}.

#### 9.1.5 M9 — Convergence Type Drift `[methodological | stable]`
<a id="section-m9-convergence-type-drift"></a>

- **Trigger.** Layer-1 convergence and Layer-2 synthesis steps.
- **Detects.** Convergence treating findings as if they were a different
  convergence type than declared (e.g., treating multi-vendor `equivalence`
  as a `split`-style synthesis; treating a single-vendor return as if it
  had been triangulated).
- **Severity.** MEDIUM (analytical posture wrong but recoverable). HIGH if
  the wrong posture has materially affected a finding's claim.
- **Resolution.** Re-run convergence with correct posture; updates
  findings sections.
- **Why retained.** Per DD.§7.2 — checks-and-balances on the LLM side
  (M1/M4 check operator side; M9 checks LLM side). Neither side gets
  unconditional benefit of the doubt.

### 9.2 Convergence-time monitors (M6, M7, M8, M12)
<a id="section-convergence-time-monitors-m6-m7-m8-m12"></a>

Fire during Layer-1 integration of new findings into the Master. Can chain
to M10.

#### 9.2.1 M6 — Premise Shift `[structural | stable | ⚠️]`
<a id="section-m6-premise-shift"></a>

- **Trigger.** Layer-1 convergence — new finding ingested.
- **Detects.** Finding invalidates a premise the strategy was built on.
  Premises documented in Decision brief, Stakeholder register, Claim
  inventory, Jurisdiction map.
- **Severity.** HIGH — strategy revision required (§{section.strategy-stability}).
- **Resolution.** Strategy revision mechanic per §{section.strategy-stability}. Chains to M10
  (Rerun) for prompts whose premise has shifted.
- **v1.x → v2 surface drift.** v1.x M6 read premises from prompt context
  sections. v2 M6 reads premises from Setup artifacts. Surface broadened;
  name unchanged because face value still describes the work.

#### 9.2.2 M7 — Claim Conflict `[structural | stable | ⚠️]`
<a id="section-m7-claim-conflict"></a>

- **Trigger.** Layer-1 convergence — new finding ingested.
- **Detects.** Two findings make incompatible claims on the same surface.
- **Severity.** HIGH if the conflict materially affects a falsifier or
  decision-brief item; MEDIUM otherwise.
- **Resolution.** Orchestration surfaces the conflict; operator decides
  whether to (a) re-dispatch one or both prompts, (b) accept the conflict
  and document, (c) escalate to a tie-breaker pass. May chain to M10.
- **v1.x → v2 rename.** v1.x called this "Assumption Conflict" because
  v1.x had an Assumption Register that M7 read against. v2 has no
  Assumption Register; M7 reads finding-vs-finding directly. Renamed to
  match the actual surface.

#### 9.2.3 M8 — Stale Source `[structural | stable | ⚠️]`
<a id="section-m8-stale-source"></a>

- **Trigger.** Layer-1 convergence — orchestration ingesting findings from
  execution sessions.
- **Detects.** A returned finding cites a source (document, study,
  regulation, vendor product) dated before some material event affecting
  its validity for the current audit.
- **Material event examples.**
  - Cited regulation has been amended/repealed since source date.
  - Cited study has been superseded by a published replication or
    correction.
  - Cited vendor product has been retired/end-of-lifed.
  - Cited statistic comes from a dataset that has been corrected.
- **Detection mechanic.** Orchestration runs a focused web search on cited
  source(s) at convergence time. If the search surfaces a material event
  invalidating the source, M8 fires.
- **Severity.**
  - HIGH: source is invalidated; finding's claim no longer supported.
  - MEDIUM: source is dated but still substantively current; finding's
    claim weakened, not invalid.
  - LOW: source is dated but the field hasn't moved; informational.
- **Resolution.** HIGH M8 fires trigger re-dispatch of the prompt with
  current sources as required attachments. MEDIUM/LOW recorded in Master's
  findings sections as confidence caveats.

**Scope distinction from §{section.currency-maintenance-point-refresh} point refresh.** M8 looks at *evidence inside
the audit*. §{section.currency-maintenance-point-refresh} looks at *framework anchors used to grade the audit's
scope*. Different artifacts, different lifecycles, different resolutions.

| Mechanism | Surface | Lifecycle | Resolution |
|---|---|---|---|
| **M8** | Cited evidence sources in returned findings | Per finding, at Layer-1 convergence | Re-dispatch with current sources |
| **§{section.currency-maintenance-point-refresh} point-refresh** | Lens Library entry's `rubric_anchor:` / `informed_by:` | Per Setup probe iteration | Inline refresh in Prompt Strategy; advisory signal toward Update session |

#### 9.2.4 M12 — Result Completeness Check `[structural | stable | ⚠️]`
<a id="section-m12-result-completeness-check"></a>

- **Trigger.** Layer-1 convergence — new finding ingested.
- **Detects.** Returned findings within a single prompt's declared domain
  leave domain-relevant surfaces unaddressed. Concrete: a P3.4
  accessibility pass produces findings on WCAG criteria 1-3 but does not
  touch keyboard navigation, cognitive load, motor disabilities, or color
  independence — surfaces inside the pass's stated domain.
- **Distinct from.** M6 (premise invalidated), M7 (claim vs claim), M8
  (cited evidence stale), P1 Coverage grading (strategy-level coverage
  against Library), Vendor Triangulation (cross-vendor agreement). M12
  asks: *did this finding cover its own declared domain?*
- **Severity.** HIGH if uncovered surfaces are material to the finding's
  claim. MEDIUM if uncovered surfaces are adjacent. LOW if uncovered
  surfaces are tangential.
- **Resolution.** HIGH chains to M10 (rerun with expanded scope).
  MEDIUM/LOW recorded in Master findings sections as scope caveats.
  Operator decides re-dispatch or accept-with-caveat.
- **v1.x lineage.** v1.x had **Coverage** as a Phase 2 enrichment role:
  *"Find what a specific prompt's narrower analysis missed within its
  domain."* Same job, relocated from per-prompt enrichment to convergence-
  time monitor. Run on multi-vendor: divergence between independent passes
  is signal about within-domain blind spots.
- **Numbering note.** v1.x M12 was Conversation Pressure (retired in v2;
  absorbed into M5's telemetric framework). The M12 slot is reused in v2
  for Result Completeness Check.

### 9.3 *What's next* input monitors (M3, M10, M11)
<a id="section-whats-next-input-monitors-m3-m10-m11"></a>

Feed the priority-ranked candidate list at each orchestration turn-close.

#### 9.3.1 M3 — Sequence Violation `[structural | stable | ⚠️]`
<a id="section-m3-sequence-violation"></a>

- **Trigger.** Operator declaration or strategy state.
- **Detects.** A canonical sequence step has been performed before its
  prerequisite; a step has been skipped.
- **Severity.** HIGH if the skipped step is on the critical path; MEDIUM
  otherwise.
- **Output.** Surfaces in *What's next* candidate list at appropriate
  priority tier.
- **Resolution.** Operator decides: backfill the skipped step, declare it
  intentionally skipped, or accept the out-of-order sequence with
  documented rationale.

#### 9.3.2 M10 — Rerun / Fix Required `[structural | stable | ⚠️]`
<a id="section-m10-rerun-fix-required"></a>

- **Trigger.** Triggered by chain from M6 / M7 / M8 / M12 HIGH; or by
  operator declaration of `failed` (§{section.operator-declaration-close-loop}); or by Probe 5 falsifier hit; or
  by Layer-2 synthesis revealing a Layer-1 gap.
- **Detects.** A previously-completed prompt needs to be rerun (with
  corrections) or a prompt's output needs explicit fix.
- **Output.** Rerun Register entry in Master:
  ```
  ## Rerun Register
  | Prompt ID | Reason | Source Monitor | Status |
  |---|---|---|---|
  | P2.1 | M6 — premise shifted | M6 HIGH P2.4 ingestion | overdue |
  | ... | ... | ... | ... |
  ```
- **Status values.** `overdue` | `scheduled` | `running` | `complete` |
  `cancelled`.
- **Surfaces in *What's next*.** Overdue Rerun Register items rank at
  priority tier 3 per §{section.whats-next}.

#### 9.3.3 M11 — Layer 2 Readiness `[structural | stable | ✅]`
<a id="section-m11-layer-2-readiness"></a>

- **Trigger.** Every orchestration turn-close.
- **Detects.** Conditions for Layer 2 cold synthesis met: all Layer-1
  prompts closed; Rerun Register clear; convergence saturated; no
  unresolved M6 / M7 HIGH; operator has not deferred Layer 2.
- **Output.** Surfaces in *What's next* as a candidate at priority tier 6.
- **Resolution.** Operator decides at *What's next* moment whether to run
  Layer 2.

### 9.4 Monitor severity report format
<a id="section-monitor-severity-report-format"></a>

When any Monitor fires HIGH, *What's next* surfaces it with this format:

```
Monitor: M6 — Premise Shift
Severity: HIGH
Trigger: Layer-1 convergence on P2.4 finding
Driver: Finding invalidates Decision brief premise "Atlas operates
  only in US." Brief premise: US-only. Finding: EU users >15% of
  active.
Recommended next action: Strategy revision per §6.5; chain to
  M10 — rerun P3.x regulatory pass for EU.
```

MEDIUM and LOW Monitor fires surface in compressed form on *What's next*
state summary line.

---

## 10. Standing Principles
<a id="section-standing-principles"></a>

Standing Principles are persistent posture, not discrete fires. They live
in the orchestration LLM's behavior at all times. Each principle has a
defined application surface; the principle travels even when specific
mechanics evolve.

### 10.1 Standing Principles introduced or extended in v2
<a id="section-standing-principles-introduced-or-extended-in-v2"></a>

#### 10.1.1 SP-1 extended — Canonicity preservation `[operator-scaffolding | stable | 🚫]`
<a id="section-sp-1-extended-canonicity-preservation"></a>

- v1.x's SP-1 forbade silently reconstructing missing files from memory.
- v2 extends to cover *offers* to reconstruct.
- Order of operations when a canonical artifact is missing:
  1. Locate the original — session history, file system, past chats.
  2. If location fails, surface specific consequences: authenticity loss,
     schema drift, silent contamination.
  3. Offer regeneration only as a documented last resort, with consequences
     named.
- Never frame regeneration as "deterministic" or "low-cost" unless it
  genuinely is.

#### 10.1.2 SP-12 — Bounded-Search Disclosure `[operator-scaffolding | stable | ✅]`
<a id="section-sp-12-bounded-search-disclosure"></a>

- When orchestration answers on the basis of a bounded retrieval, the
  default posture is to disclose the bound.
- "I found no evidence" insufficient; "I found no evidence within [named
  scope]; confirm before I proceed" is required.
- Applies to: past-conversation search, file listing, web search with
  date/site filters, project knowledge lookup, any retrieval with
  implicit scope.
- Not a Monitor that fires discretely; a posture held at every retrieval.

**Spec form** (phrasing template):

```
[Result]. SP-12 disclosure: Searched within [explicit scope].
[N matches | null]. The target may live outside this scope;
confirm before I conclude.
```

#### 10.1.3 SP-13 — Substrate Declaration `[operator-scaffolding | stable | ⚠️]`
<a id="section-sp-13-substrate-declaration"></a>

- PRISM-loaded sessions verify substrate against declared target before
  executing dependent work.
- The declared target is expressed by **vendor and tier, not version**: the
  orchestrating model must be **Claude** (not ChatGPT, Gemini, or another
  vendor) and of **Opus-class / flagship tier** — a capability floor, not a
  lightweight Claude. Version-agnostic; latest by default.
- If self-identification doesn't match declared target (wrong vendor, or
  below the tier floor), or can't be determined, session halts and asks operator.
- Operationalized inside execution sessions via the Self-check block
  (§{section.prism-execution-self-check}).
- In orchestration sessions: operationalized as a session-open
  verification — orchestration self-identifies and confirms it matches
  the declared orchestration target (Claude, Opus-class).

**Orchestration-side spec.**

```
[At every orchestration session-open:]
SP-13 verification:
  Self-identification: [model, vendor, mode]
  Declared target: vendor = Claude; tier = Opus-class (flagship);
                   version = any (latest by default)
  Match: [yes / no / cannot-determine]
[If no or cannot-determine: halt; ask operator.]
```

#### 10.1.4 SP-10 — Verify state before recommending `[operator-scaffolding | stable | ✅]`
<a id="section-sp-10-verify-state-before-recommending"></a>

Carries forward from v1.10.4 as a named principle. The principle's
mechanics live primarily in Vendor Selection (§{section.vendor-selection-at-dispatch}) — but holding it as a
named SP keeps it portable: point refresh (§{section.currency-maintenance-point-refresh}), Update sessions (§{section.currency-maintenance-update-session}),
and any future recommendation surface inherit the discipline rather than
re-deriving it.

- When orchestration generates recommendations that depend on current
  platform / vendor / model / best-practice state, verify before
  recommending.
- Training knowledge is reliably out of date for fast-moving domains.
- Verification pattern: targeted web search at recommendation-generation
  moments.
- Calibrated output: search result is *input* to recommendation, not
  substitution; reconcile with operator observations and remaining
  uncertainty.
- Graceful degradation when verification fails: frame as best-effort, name
  the staleness risk.
- Budget discipline: verification searches return substantial context;
  only trigger on fast-moving state, not on stable defaults.

#### 10.1.5 SP-14 — Filename Discipline `[operator-scaffolding | stable | ✅]`
<a id="section-sp-14-filename-discipline"></a>

Extracted from v1.x SP-8 (which bundled two concerns under one number).
v2 splits SP-8 into Canonical Authority (the original SP-8) and Filename
Discipline (this new SP-14).

- Look-alike files produced by multi-vendor execution use the structured
  filename pattern: `[project]_[promptID]_[vendor].md` for Outputs,
  `[project_name]_prism[version]_master_[phase-versioning].md` for Masters,
  `PRISM_lens_library_[version].md` for Library files, dated handoffs for
  migrations.
- Corpus-access companion artifacts (the captured exhibits a corpus-access
  bundle returns, §{section.corpus-access-dispatch}) extend the Output pattern to
  `[project]_[promptID]_[source]_[seq].{png,pdf,xlsx}`, so the archive is a
  provenance-bearing set rather than a bag of `screenshot1.png`.
- The em-dash (` — `) separator stays cross-platform safe (pipe is illegal
  on Windows, shell-active on Unix).
- M1 (Missing Inputs) parses attached filenames against expected patterns;
  mis-named files are flagged at session-open.
- "Wrong-file-that-looks-similar" is a specific failure mode v2 creates by
  design (multi-vendor equivalence dispatches produce N similarly-named
  outputs); the naming convention is the defense.

**Surface in v2** (narrower than v1.x; principle still earns its place):

- Equivalence-mode Outputs (one file per vendor for the same prompt).
- Master versions across phases accumulating in cloud drive.
- Migration handoffs (one per migration, dated).
- Update-session Library output versions.

Full filename-convention canonical reference table in §{section.filename-conventions-and-bump-atomicity}.

#### 10.1.6 SP-15 — Triangulation integrity `[operator-scaffolding | stable]`
<a id="section-sp-15-triangulation-integrity"></a>

PRISM's Vendor Triangulation premise is adversarial, not parallel: different
vendors carry different priors, training distributions, and failure modes,
which is what makes their convergence (or divergence) load-bearing for
falsifier-grade findings. Four corollaries follow.

- **Single-vendor multi-agent is not cross-vendor triangulation.** Sub-agents
  from one vendor — native multi-agent / sub-agent coordination features
  notwithstanding — share priors with their orchestrating model. They
  parallelize work; they do not falsify each other across distributions.
  Equivalence dispatch (§{section.single-envelope-with-spectrum-shape})
  requires distinct vendors, not distinct sessions on the same vendor.

- **Self-triangulation carries no asymmetric weighting.** When the
  orchestration vendor is also one of the triangulated execution vendors,
  convergence remains mechanical: Layer-1 reconciliation, the Vendor
  Triangulation delta (§{section.convergence-delta-document}), and M6/M7/M8
  monitors apply identically to every vendor regardless of which substrate
  also runs orchestration. No finding is up- or down-weighted by virtue of
  vendor identity matching the orchestrator.

- **Auto-driven multiplicity must be cross-vendor to triangulate.** When
  the `auto_drive` execution driver
  (§{section.orchestration-driver-and-persistence-axes}) drives N *distinct
  vendor* apps with one Envelope, that is cross-vendor equivalence
  dispatch — triangulation as intended. When auto-drive instead fans out to
  sub-agents on the orchestrating vendor, it is parallel execution on a
  single distribution: no falsification across distributions, hence not
  triangulation. The driver automates who dispatches; it does not change how
  many distributions a prompt reached.

- **A corpus-access / coverage-fan lookup adds no triangulation seat.** A
  corpus-access dispatch (§{section.corpus-access-dispatch}, the
  external-reference-corpus lookup) is investigation posture: it retrieves
  material rather than reasoning over it. A fan across N vendors
  (`Fan: coverage (N)`) buys recall, not falsification across distributions, so it
  is recorded as a retrieval-consistency note and never counted as a
  triangulation seat. The guardrail is structural — an investigation-posture
  Envelope lacks `Dispatch shape`, so Vendor Triangulation
  (§{section.vendor-triangulation}) cannot fire on it.

Cross-ref: §{section.vendor-triangulation},
§{section.claude-baseline-feasibility-with-named-limitation-escape-hatch},
§{section.orchestration-driver-and-persistence-axes},
§{section.corpus-access-dispatch}.

#### 10.1.7 SP-16 — The Elephant Rule `[methodological | stable | 🚫]`
<a id="section-sp-16-the-elephant-rule"></a>

New in v2.13.0. Negation is a targeting decision, not a style choice
(Lakoff: don't think of an elephant).

- A sentence may negate only a **live** alternative — a belief the
  reader demonstrably brings: a common prior, a named risk, or an
  inference the document's own numbers invite.
- Negating anything else plants the accusation it denies: the reader
  leaves carrying the frame, the author reads as defensive, and the
  text implies a critic nobody heard from.

**Test** — run on every negation ("not Y", "X, not Y", "rather than
Y", "no Y"):

1. Would a cold reader plausibly arrive believing Y, or derive Y from
   the document itself?
2. Yes → **called-for**. Keep; the contrast carries information.
   Record which live alternative it negates.
3. No → **uncalled-for**. Rewrite positively: assert what is true
   without referencing Y at all.

**Called-for (keep) — examples.**

- "The limit is export permission, not customer demand." (Both
  hypotheses are live; the contrast names the binding constraint.)
- "Maximum at full coverage (not current revenue)." (Prevents a real
  chart misread.)
- "~40 accounts is roughly one per country, not a near-monopoly."
  (Pre-empts arithmetic the reader will actually do.)

**Uncalled-for (rewrite) — examples.**

- "Why it's a real market, not a hyped one" → "What anchors the $2.0
  billion." (Nobody alleged hype; the heading now asserts the anchor.)
- "…lowers the figure to 45–60% of the total, rather than inflating
  it" → end the sentence at "of the total." ("Inflate" existed only
  to be denied.)
- "This is X — not the giant Z it's often confused with" → "This is X
  of its own — far narrower than Z." (Scoping kept, denial form
  dropped.)

**Application surfaces.**

- Every prose deliverable PRISM produces: Layer-2 synthesis, findings
  content inside Execution Outputs, Setup artifacts, *What's next*
  bodies. Headings, titles, and opening sentences get the strictest
  scrutiny — they set frames the rest of the document inherits.
- Execution-side operationalization: step 5 of the Execution
  Self-check (§{section.prism-execution-self-check}) — before emitting
  the Output, enumerate every negation; tag each called-for (naming
  the live alternative) or uncalled-for (rewrite before release).
- Audit-side: the Lens Library carries the same discipline as a
  document-review lens (LL-D-019 "Who said otherwise?", Pack 1) for
  reviewing existing documents.

### 10.2 v1.x Standing Principles — carryforward catalog
<a id="section-v1-x-standing-principles-carryforward-catalog"></a>

Per-SP disposition explicit:

| SP | v1.10.4 name | v2 disposition | Notes |
|---|---|---|---|
| SP-1 | Never reconstruct files from memory | Extended in v2 | Now covers *offers* to reconstruct. See §{section.sp-1-extended-canonicity-preservation} |
| SP-2 | Defer non-critical fixes to natural touchpoint | Carryforward | Direct; principle unchanged |
| SP-3 | Convergence is part of prompt delivery | **Dissolved** | Incompatible with orchestration/execution split |
| SP-4 | Every Monitor produces visible output | Carryforward | Direct; applies to v2 monitors at orchestration |
| SP-5 | No heuristic guessing on ambiguous input | Carryforward | Direct; pairs with SP-9 |
| SP-6 | Rebuild at threshold (build-method discipline) | Carryforward | Direct; applies to spec/framework builds |
| SP-7 | File delivery is mandatory | Carryforward | Direct; reinforced by triple contract's file-based Output |
| SP-8 | (a) Canonical authority + (b) Filename discipline | **Split** | (a) stays SP-8; (b) becomes SP-14 |
| SP-9 | Silence is never consent | Carryforward | Direct; applies to operator close-loop, ratification, ambiguity escalation |
| SP-10 | Verify state before recommending | Carryforward as named principle | Mechanics in Vendor Selection; principle stays SP-tier |
| SP-11 | *(never assigned)* | — | No SP-11 existed in v1.x or v2; the principle series continues at SP-12 |
| SP-12 | Bounded-Search Disclosure | New in v2 | See §{section.sp-12-bounded-search-disclosure} |
| SP-13 | Substrate Declaration | New in v2 | See §{section.sp-13-substrate-declaration} |
| SP-14 | Filename Discipline | New in v2 (extracted from SP-8) | See §{section.sp-14-filename-discipline} |
| SP-15 | Triangulation integrity | New in v2.1.1 | See §{section.sp-15-triangulation-integrity} |
| SP-16 | The Elephant Rule (negation discipline) | New in v2.13.0 | See §{section.sp-16-the-elephant-rule} |

#### 10.2.1 SP-8 narrowed — Canonical Authority `[operator-scaffolding | stable | ✅]`
<a id="section-sp-8-narrowed-canonical-authority"></a>

After the v2 split, SP-8 carries one concern:

- The file delivered via `present_files` is canonical for that project
  state.
- Any edit made outside a Claude session (desktop editor, phone
  annotation, external LLM) must be flagged at the start of the next
  session so M2 (Version Drift) can reconcile.
- Filename discipline (the look-alike disambiguation pattern) extracted to
  SP-14 (§{section.sp-14-filename-discipline}).

#### 10.2.2 Carryforward SPs — application surfaces
<a id="section-carryforward-sps-application-surfaces"></a>

The six pure-carryforward SPs (§{principle.SP-2}, SP-4, SP-5, SP-6, SP-7, SP-9) carry
forward from v1.10.4 verbatim in principle. Each is stated in full with its
v2 application surface:

<a id="section-sp-2-defer-non-critical-fixes-to-natural-touchpoint"></a>
- **SP-2 (Defer non-critical fixes to natural touchpoint).** Applies in
  orchestration's *What's next* ladder — non-critical issues queue against
  priority tiers, fix at next aligned step. M10 fires when no natural
  touchpoint exists.
- **SP-4 (Every Monitor produces visible output).** Silent monitors are
  useless monitors. Applies to all M1–M12 monitor fires in orchestration;
  *What's next* surfaces every fire at appropriate severity.
- **SP-5 (No heuristic guessing on ambiguous input).** Wherever
  orchestration parses operator input, ambiguity halts and asks. Pairs
  with M4 (Ambiguous Ask) firing.
- **SP-6 (Rebuild at threshold).** Build-method discipline: threshold ≤~8
  sequential edits → str_replace; above → create_file rebuild via a
  deterministic transformation script. Applies to v2 framework builds
  (spec → PRISM_v2_0.md), Library Update sessions, large Master rewrites.
- **SP-7 (File delivery is mandatory).** Applies to every orchestration
  session that updates Master, every execution session that produces
  Output, every Update session that produces a new Library file.
  Reinforced structurally by the triple contract's file-based Output
  (§{section.prism-execution-output}).
<a id="section-sp-9-silence-is-never-consent"></a>
- **SP-9 (Silence is never consent).** Applies wherever operator decision
  is required: close-loop declarations, ratification, ambiguity
  escalation, migration override at 🔴, Project recommendation
  accept/decline. Active operator action required; no defaults-on-timeout.

<a id="section-sp-3-dissolved"></a>
**SP-3 — dissolved.** v1.10.4's SP-3 ("Convergence is part of prompt
delivery") is incompatible with v2's orchestration/execution split.
Convergence moves to orchestration; per-prompt convergence checklists drop
from the atomic prompt template (§{section.atomic-prompt-template-v2-form}).

---

## 11. Filename conventions and bump atomicity `[structural | stable]`
<a id="section-filename-conventions-and-bump-atomicity"></a>

Canonical reference table for every PRISM v2 artifact's filename pattern,
plus the atomic-bump routine that produces version increments.

### 11.1 Filename patterns
<a id="section-filename-patterns"></a>

| Artifact | Pattern | Example |
|---|---|---|
| Master | `[project]_prism[major.minor]_master_[phase-versioning].md` | `acme_audit_prism2.0_master_p2.3.md` |
| Execution Output | `[project]_[promptID]_[vendor].md` | `acme_audit_p2.3_gemini.md` |
| Corpus-access exhibit | `[project]_[promptID]_[source]_[seq].{png,pdf,xlsx}` | `acme_audit_p3.1_ideasrip_01.png` |
| Migration handoff | `[project]_handoff_[YYYY-MM-DD]_[seq].md` | `acme_audit_handoff_2026-04-25_01.md` |
| Lens Library file | `PRISM_lens_library_[version].md` | `PRISM_lens_library_v0_9.md` |
| Update session output | `PRISM_lens_library_[new-version].md` + delta document | `PRISM_lens_library_v0_9_1.md` |
| Subject brief | `[project]_brief.md` | `acme_audit_brief.md` |
| Prompt Strategy (when separate) | `[project]_prompt_strategy_[phase-versioning].md` | `acme_audit_prompt_strategy_p1.0.md` |

**Separator.** Underscores within tokens (`prism2.0`, `master_p2.3`); the
em-dash (` — `) is reserved for the Output's `Vendor` rendering and inside
prose. No pipes (illegal on Windows). No spaces in filenames (shell-
active).

**Phase versioning.**

- Setup iterations: `p0.1`, `p0.2`, `p0.3`, ... (no cap)
- Phase 1 runs: `p1.0`, `p1.1`, `p1.2`, ... (sub-version per convergence
  round)
- Phase 2+: `p2.0`, `p2.1`, ...

### 11.2 Bump atomicity routine
<a id="section-bump-atomicity-routine"></a>

Master version bumps are mechanically tied to defined triggers. Produced
atomically at every orchestration turn-close:

1. Compute the new Master filename per the bump rule:
   - **Phase transitions** (P0→P1, P1→P2, etc.) — major filename version
     advances: `…_master_p0.4.md` → `…_master_p1.0.md`.
   - **Convergence rounds within a phase** — sub-version increments:
     `…_master_p2.1.md` → `…_master_p2.2.md`.
   - **Setup probe iterations** — sub-version increments within P0:
     `…_master_p0.1.md` → `…_master_p0.2.md`.
   - **Schema version changes** — Schema version field in Master metadata
     header increments. Filename does *not* bump on schema-only changes;
     the metadata field tracks it.
2. Produce the updated Master content.
3. Write a Changelog entry: `[date] | [old version] → [new version] |
   [trigger: phase transition / convergence round / probe iteration /
   state update]`.
4. Emit *What's next* with the new Master version embedded.
5. Operator hint: `Download as [new filename]; attach next session.`

This atomic routine + the M2 silent-safeguard makes drift very unlikely
by construction without abandoning the safeguard.

---

## 12. Atomic prompt template — v2 form
<a id="section-atomic-prompt-template-v2-form"></a>

The atomic prompt template wraps the triple contract around the prompt
body. It's the unit operators paste into execution sessions.

### 12.1 Template shape `[structural | stable]`
<a id="section-template-shape"></a>

```
━━━ PRISM EXECUTION ENVELOPE ━━━
[Envelope per §3.2.1]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━

━━━ PRISM EXECUTION SELF-CHECK ━━━
[Self-check per §3.2.2]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# [Prompt body title]

## Context

[Background the vendor session needs. References Setup artifacts by
section. Pulls minimum content from Master into the prompt body — the
operator cannot rely on the vendor having access to anything not in the
attached files.]

## Task

[One-sentence statement of what the vendor must produce.]

## Method

[How the vendor should approach. References specialist framing per
LL.specialist_type if applicable. Names the Library lens(es) being
graded.]

## Output

[Reference to §4.11 finding structure. Specifies number of findings if
known, or "as many as warranted." Confidence calibration and verification
status discipline named explicitly.]

## Success criteria

[Names what a good execution output must accomplish. Default block,
adapted by the prompt body when shape demands:

  - Covers every surface named in the task and attachments.
  - Separates verified findings from plausible-but-unverified inferences
    via the Verification status field (§4.11).
  - Names null results and could-not-verify areas explicitly.
  - Produces findings that orchestration can ingest independently
    (no cross-finding dependencies, per §4.11 composition rules).
  - Flags attachment, tool, or source-access limits in Could not verify
    or in Attachment warnings, not silently.]

## Output signature instruction

When you finish, wrap your findings in the PRISM Execution Output
signature block per §3.2.3:

[Output block template here, with placeholders the vendor fills.]
```

### 12.2 Composition rules
<a id="section-composition-rules"></a>

- **No convergence checklists in the prompt body.** Convergence is
  orchestration-side per the triple-contract split. v1.x's per-prompt
  convergence checklists drop in v2 (§{principle.SP-3} dissolution).
- **No vendor-specific machinery in the body.** Tool requests live in the
  Envelope's `Tools:` field; vendor-specific config in `Vendor config:`.
- **Attachments referenced by name and order.** When the body references
  `Attachment 1`, that maps to the first filename in the Envelope's
  `Attachments:` list.
- **Findings discipline per §{section.prompt-body-convergence-provisions}.** Numbered, attributable, evidence-
  classed, confidence-calibrated.

### 12.3 What v1.x's atomic template carried that v2 reshapes
<a id="section-what-v1-xs-atomic-template-carried-that-v2-reshapes"></a>

- *Hygiene block* → folded into Envelope and Self-check (substrate
  verification is now structural, not prose discipline).
- *[UNVERIFIED] tagging* → restored as an explicit Verification status
  axis in the §{section.prompt-body-convergence-provisions} finding structure (v2.0.1). Orthogonal to confidence;
  see §{section.prompt-body-convergence-provisions} *Verification ≠ confidence*.
- *Discrepancy Check* → orchestration-side at Layer-1 (§{monitor.M7} Claim Conflict).
- *Live watch for preemptive scope-down* → orchestration-side via §{monitor.M5} +
  M6.
- *Convergence (Layer 1 — mandatory)* → orchestration-side; SP-3
  dissolved.

The body now carries only what a vendor session actually needs: context,
task, method, output shape. Everything else is in the Envelope or
orchestration-side.

---

## 13. Operator hint catalog `[methodological | stable]`
<a id="section-operator-hint-catalog"></a>

Hints are optional one-line cues keyed to the upcoming action. Emission
discipline per §{section.operator-hints-emission-discipline}. The catalog below is the canonical reference; new
hints accrue here as patterns surface.

### 13.1 Cloud drive and persistence
<a id="section-cloud-drive-and-persistence"></a>

- `Save output to cloud drive after download, before switching to the
  next vendor (see MO-5).`
- `Save Master to cloud drive at session close (see MO-5).`

### 13.2 Mobile platform cues
<a id="section-mobile-platform-cues"></a>

- `On Samsung, expect indexing delay on the downloaded file (MO-1).`
- `If [vendor] mobile fails to download, retry in Firefox Desktop mode
  (MO-2).`
- `On iOS, the download lands in Files → Downloads folder (vendor-
  specific).`

### 13.3 Session hygiene cues
<a id="section-session-hygiene-cues"></a>

- `Run [vendor] outside any project so it isn't distracted by project
  memory.`
- `Re-attach Master and Lens Library at session open.`
- `New session — paste handoff first, then attach Master and Library.`

### 13.4 Multi-vendor cues
<a id="section-multi-vendor-cues"></a>

- `Equivalence dispatch — N=3. Send to all three before attaching any
  return.`
- `Vendor [X] substituted at last dispatch — note this for triangulation
  weighting.`

### 13.5 Recovery cues
<a id="section-recovery-cues"></a>

- `Master version mismatch — verify which file is current before
  attaching.`
- `Session history search may be needed — confirm scope before
  concluding.`

### 13.6 Attachment warnings
<a id="section-attachment-warnings"></a>

These are emission targets — the Output's `Attachment warnings:` field
(§{section.prism-execution-output} footer) populates with severity-tagged lines:

- `MISSING:` — declared in Envelope but not attached.
- `UNREADABLE:` — present but the vendor session couldn't read it (format
  unsupported; subagent file-access bug).
- `CORRUPTED:` — present and readable but content is corrupted or
  truncated.
- `SCHEMA_MISMATCH:` — present and readable but content didn't match the
  expected schema (for structured attachments like prior Outputs).

**Format** (one line per warning):

```
Attachment warnings:
  MISSING: regulatory_context.md (declared in Envelope but not attached)
  UNREADABLE: acme_brief.pdf (Deep Research subagent file-access)
```

**Orchestration response.** M1 fires HIGH on `MISSING:`, MEDIUM on
`UNREADABLE:` / `CORRUPTED:`, LOW on `SCHEMA_MISMATCH:`. *What's next*
surfaces re-dispatch with corrected attachment list as a candidate.

---

## 14. Missing-handoff recovery
<a id="section-missing-handoff-recovery"></a>

What happens when the operator opens a fresh orchestration session
without a handoff (operator skipped the migration step at 🔴; handoff
was lost; mid-project session was opened cold)?

### 14.1 Recovery flow `[methodological | stable]`
<a id="section-recovery-flow"></a>

1. **Session-open verification fires.** SP-13 substrate check passes;
   M1 detects no handoff attached.
2. **Orchestration searches for the canonical Master.** Per §{principle.SP-1}
   protocol:
   - Past-conversation search for the project name and likely Master
     filenames (`conversation_search`, bounded by current Project per
     §{section.claude-project-as-setup-recommendation}; SP-12 disclosure on bound).
   - If a past session is identified that produced a Master version,
     surface the session URL and the Master filename to operator.
3. **Operator attaches the located Master.** Orchestration runs M2
   (Version Drift) verification against operator's expected version
   (operator-declared on resume).
4. **Orchestration reconstructs `What's next` from the Master.** The
   Master's Open dispatches list, Active probes list, Open monitors list,
   and Rerun Register together carry sufficient state to reproduce a
   *What's next*. Decision brief / Stakeholder register / Claim inventory
   / Jurisdiction map carry the Setup artifacts.
5. **No silent regeneration.** Per §{principle.SP-1}: orchestration does not
   reconstruct what's missing from memory. Surface what was located,
   surface what couldn't be located, ask operator how to proceed.
6. **If Master itself cannot be located.** Escalate per §{principle.SP-1}: name the
   consequences of regenerating from memory (authenticity loss, schema
   drift, silent contamination); ask operator whether to proceed with
   reconstruction (and document the reconstruction explicitly in the
   Master's Changelog), or whether to re-Setup.

### 14.2 Why this matters
<a id="section-why-this-matters"></a>

The continuous-state mechanic (§{section.failsafe-recovery-continuous-state-mechanics}) is the front-line defense — every
turn-close writes the Master and *What's next*. The recovery flow is the
backstop when the front-line defense is bypassed (handoff lost, session
opened from outside the Project, cross-device churn). SP-1's discipline
makes the recovery flow safe rather than seductive: it's harder than
recreating from memory, and it should be — recreation is the failure
mode the discipline exists to prevent.

---

## 18. Project, feedback, updates `[structural | stable]`
<a id="section-project-feedback-updates"></a>

PRISM is an open framework. This file ships with enough information to
locate the project, check for newer versions, and feed observations back
to the maintainer.

### 18.1 Project identity
<a id="section-project-identity"></a>

- **Repository.** `https://github.com/Ronkupper/PRISM`
- **Maintainer.** Ron Kuper ([@Ronkupper](https://github.com/Ronkupper))
- **Framework version.** v2.13.0 (this file)
- **Bundled Lens Library version.** v0.14 (`lens/PRISM_lens_library.md`)
- **Release date.** 2026-06-10
- **Licensing.** Documentation under CC BY 4.0; any code under MIT;
  Code of Conduct under CC BY-SA 4.0. Full license texts in the repository.

### 18.2 Resource fetch convention
<a id="section-resource-fetch-convention"></a>

The framework and its companion artifacts are addressable on `main` of the
public repository under stable raw URLs. Orchestration sessions running on
substrates with web access can fetch these directly; mobile operators
without that capability can paste the URLs into a browser and download.

| Resource | Stable URL | Pinned URL |
|---|---|---|
| Framework (this file) | `https://raw.githubusercontent.com/Ronkupper/PRISM/main/PRISM.md` | `…/PRISM_v2_13_0.md` |
| Lens Library | `https://raw.githubusercontent.com/Ronkupper/PRISM/main/lens/PRISM_lens_library.md` | `…/lens/PRISM_lens_library_v0_14.md` |
| Framework version stamp | `https://raw.githubusercontent.com/Ronkupper/PRISM/main/VERSION` | — |
| Lens version stamp | `https://raw.githubusercontent.com/Ronkupper/PRISM/main/lens/VERSION` | — |
| Releases index | `https://github.com/Ronkupper/PRISM/releases` | — |
| Release at this version | — | `https://github.com/Ronkupper/PRISM/releases/tag/v2.13.0` |

The two `VERSION` endpoints exist as cheap currency checks: each is a
single-line file containing the current version on the corresponding
release track. Reading them does not require parsing the framework or
the Lens body. New resources added to the project follow the same path
pattern (a stable file on `main`, a `VERSION` stamp where versioned).

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
   `Framework v2.13.0 attached; v{published} available at {releases URL}.`
   `Lens v0.14 attached; v{published} available at {releases URL}.`
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

### 18.4 Feedback and contribution
<a id="section-feedback-and-contribution"></a>

- **Bugs and concrete defects.** GitHub Issues on the public repository,
  using the issue templates under `.github/ISSUE_TEMPLATE/`.
- **Ideas, proposals, observations from real use.** GitHub Discussions
  on the public repository, *Ideas* category. Field observations from
  applying PRISM to real audits are particularly valuable: the framework
  ships with several rev. 1 draft thresholds (§{monitor.M5} bands, Update session
  triggers, probe iteration ceilings) that calibrate against use, not
  introspection.
- **Show and tell.** Discussions, *Show-and-tell* category. Adaptations
  for non-Claude vendors, surface drift maps for new substrates, and
  Lens additions discovered in the field are all welcome.
- **Questions.** Discussions, *Q&A* category.
- **Security concerns.** Private vulnerability reporting via the
  repository's *Security* tab. Do not file security issues publicly.

The four-channel split is codified in `CONTRIBUTING.md`. The Code of
Conduct is in `CODE_OF_CONDUCT.md`.

### 18.5 Citation
<a id="section-citation"></a>

To cite PRISM in published work, see `CITATION.cff` in the repository.
A short attribution suitable for inline use:

> Kuper, R. (2026). *PRISM: A Framework for LLM Research and Audits*
> (v2.13.0). https://github.com/Ronkupper/PRISM

---

*End of PRISM v2.13.0 framework operating document.*
