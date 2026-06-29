---
# Framework metadata (consumed by PRISM maintenance tooling)
version: 2.21.0
released: 2026-06-29
supersedes: 2.20.2
lens_library_bundled: "0.16"
substrate_target:
  vendor: claude
  tier: opus-class       # flagship/frontier tier — a capability floor, not a lightweight model
  version: latest        # version-agnostic; the latest Opus-class Claude by default
normativity:
  strength_vocabulary: [required, recommended, optional]
  strength_default: required
  polarity_vocabulary: ["✅", "⚠️", "🚫"]
  polarity_default: null
lint_catalog_version: 5
---

<!-- PRISM v2.21.0 Skill core (lean, always-loaded). Generated from the assembled
     PRISM.md by scripts/decompose/project_skill_archive.py — edit PRISM.md, not this.
     Reference-grade material is in reference/*.md and lens/, fetched on demand. -->

# PRISM v2.21.0 — Framework operating document

**Status:** v2.21.0 release. Canonical framework for Claude orchestration sessions.
**Date:** June 2026
**Supersedes:** PRISM v2.20.2 (MINOR — external-review hardening, methodology lane: turn-close evaluate-then-emit ordering; a Self-check visible-recompute line (Step 6) and a first-token Dispatch-ID echo (Step 0); the orchestration dispatch-record vs. execution-seat-paste split (new template E.1a); a `━`-vs-XML dispatch-delimiter rationale (Appendix J.2 plus a new Appendix H heavy-line section) and a J.3 newline-normalization clarifier; and a runtime front door — the `/prism-help` command plus an orientation-before-engagement core behavior. Framework prose changes this release; Lens Library stays v0.16; lint catalog stays v5.). PRISM v1.10.4 is terminal on the v1.x line (pinned per DD §{section.standing-principles-introduced-or-extended-in-v2}).
**Required attachments at every orchestration session:** the PRISM Skill
(its core loads automatically) and the project's Master. The Skill bundles
Lens Library v0.16 at `lens/PRISM_lens_library.md`, fetched on demand. Pin a
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

1. **§{section.scope} Scope** (this section group) — what v2.21.0 is and what it isn't.
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

Reading order for an operator returning to v2.21.0 after running a session:
*What's next* → relevant §{section.architecture-mechanics}–§{section.library-integration} mechanics → §{section.monitor-specifications} Monitors if a fire surfaced.

---

## 1. Scope
<a id="section-scope"></a>

### 1.1 What v2.21.0 covers `[structural | stable]`
<a id="section-what-v2-8-0-covers"></a>

PRISM v2.21.0 is a structured multi-session, multi-vendor LLM-orchestrated audit
and research framework. v2.21.0 covers:

- **Two session types** (orchestration on Claude; execution on selected vendor per Vendor Selection)
  with explicit role separation (§{section.two-session-types}).
- **The triple contract** (Envelope inbound, Self-check, Output outbound) as
  the load-bearing interface between sessions (§{section.the-triple-contract}).
- **Master + *What's next* as continuous-state artifacts** written at every
  orchestration turn-close, regardless of band state (§{section.the-master}, §{section.whats-next}, §{section.failsafe-recovery-continuous-state-mechanics}).
- **Vendor Selection at dispatch** with live web-search currency check
  (§{section.vendor-selection-at-dispatch}).
- **Setup as iterative refinement** against the Lens Library v0.16, with
  three-layer readiness clearing the P0→P1 boundary (§{section.setup-mechanics}).
- **Seven Setup probes** (§{probe.P1} Coverage grading, P2 Adversarial Scope, P3
  Decision Framing, P4 Pre-mortem, P5 Falsifier, P6 Domain Reconnaissance,
  P7 User Voice) — Setup-time grading constructs only (§{section.the-seven-probes}).
- **Library integration** — the Lens Library v0.16 as canonical reference
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

### 1.2 What v2.21.0 does not cover
<a id="section-what-v2-8-0-does-not-cover"></a>

- **Re-debating direction.** v2.21.0 implements the spec; the spec implements
  the design document. Direction is settled. New direction goes through a
  fresh design cycle.
- **Standalone Library evolution.** The Lens Library catalog is bundled at
  `lens/PRISM_lens_library.md` (tag `prism-lens-v0.16`, v0.16 at this release),
  fetched on demand. The bundled file remains authoritative for the Library's
  own evolution and for projects that explicitly pin to a newer Library version.
- **Empirical calibration.** Several thresholds in v2.21.0 are rev. 1 draft
  estimates: M5 band thresholds (§{section.telemetric-framework-signal-weighting-and-compounding}), Update session trigger (§{section.currency-maintenance-update-session}),
  probe iteration ceilings (§{section.from-waterfall-to-library-graded-iterative-refinement}). Calibration against real use is a
  post-release item (§{section.empirical-calibration-items}).
- **Multi-vendor Self-check empirical footing.** Verified on Claude
  Opus-class and Sonnet-class models. Behavior on Gemini, ChatGPT, Perplexity
  is report-worthy (§{section.empirical-calibration-items}).
- **Non-Claude orchestration.** v2.21.0's machinery uses Claude-specific
  affordances (`present_files`, `create_file`, `str_replace`,
  `ask_user_input`, `conversation_search`, Skill packaging). Non-Claude
  orchestration is graceful-degradation, not a design target (DD.§3.1).

### 1.3 Three-leg constraint `[structural | stable]`
<a id="section-three-leg-constraint"></a>

v2.21.0 honours the constraint inherited from the design document (DD.§8.3):

- **Operator constraint.** Mobile-first; plain-chat substrate; manual
  artifact handling between sessions.
- **Substrate constraint.** Claude Opus-class (flagship tier) in orchestration; multi-
  vendor on the execution side.
- **Methodology constraint.** Structured audit-and-research with explicit
  scope-completeness and convergence discipline.

Mechanics that violate any leg do not earn their place in v2.21.0. Roadmap
adjacencies (DD.§9: automated cross-vendor orchestration, plugin-equipped
execution, multi-vendor skill ecosystems) live in reserved structural
surfaces — the `Tools:` slot and the reserved values on the
execution-configuration axes (§{section.orchestration-driver-and-persistence-axes}) —
but no machinery beyond the reservation.

---
## 2. System overview
<a id="section-system-overview"></a>

**Read this section first if you are encountering v2.21.0 mechanics for the
first time, and re-read it any time you need to locate a specific construct.**
This section is a map. Definitions live in the per-construct sections (§{section.architecture-mechanics}–§{section.missing-handoff-recovery}).

### 2.1 Construct list
<a id="section-construct-list"></a>

PRISM v2.21.0 has the following constructs, grouped by category.

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
- v2-new/extended: SP-1 ext, SP-12, SP-13, SP-14, SP-15, SP-16, SP-17,
  SP-18, SP-19, SP-20, SP-21, SP-22
- Carryforward: SP-2, SP-4, SP-5, SP-6, SP-7, SP-8 (narrowed), SP-9, SP-10
- Dissolved: SP-3

**Mechanisms**
- Vendor Selection (§{section.vendor-selection-at-dispatch}) · Vendor Triangulation (§{section.vendor-triangulation}) · Bump atomicity
  (§{section.standalone-monitors-m1-m2-m4-m5-m9} spec / §{section.filename-conventions-and-bump-atomicity}) · Telemetric framework (§{section.telemetric-framework-signal-weighting-and-compounding}) · Point refresh (§{section.currency-maintenance-point-refresh}) ·
  Update session (§{section.currency-maintenance-update-session}) · Continuous-curation (§{section.continuous-curation-posture}) · Strategy stability
  (§{section.strategy-stability}) · Three-layer readiness (§{section.three-layer-readiness}) · Two-layer convergence · Triple
  contract · Independent Validation Dispatch (§{section.independent-validation-dispatch}) · Engagement closure
  (§{section.engagement-closure})

**Deliverables** (§{appendix.report-architecture}, §{appendix.external-share})
- Comprehensive final report · interactive engagement workbook · external share
  archive

**Operating model** (§{section.lanes-roles-and-the-prism-ui})
- Lane (object · meta) · Role × context-tier matrix · PRISM Desk
  (Planner/Steward) · PRISM Meta · OPEN_ITEMS cross-lane inbox · PRISM UI
  (View + Controller) · `<Lane>-<N>` session numbering

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
| SP-16 The Elephant Rule (uninvited-frame discipline) | New in v2.13.0 | §{section.sp-16-the-elephant-rule} |
| SP-17 Plain words first | New in v2.14.0 | §{section.sp-17-plain-words-first} |
| SP-18 It must recompute | New in v2.14.0 | §{section.sp-18-it-must-recompute} |
| SP-19 Claims carry their basis | New in v2.14.0 | §{section.sp-19-claims-carry-their-basis} |
| SP-20 Editions stand alone | New in v2.14.0 | §{section.sp-20-editions-stand-alone} |
| SP-21 Trust structure, self-report advisory | New in v2.15.0 | §{section.sp-21-trust-structure-self-report-advisory} |
| SP-22 Surface translation | New in v2.15.0 | §{section.sp-22-surface-translation} |

**Operating model** (the lanes/roles backbone, §{section.lanes-roles-and-the-prism-ui})

| Construct | Lifecycle | Reads | Writes | Detail |
|---|---|---|---|---|
| Lane | Per engagement (object · meta) | Pointer, log, inbox | The lane's worker | §{section.lanes} |
| PRISM Desk | Per round or periodic | Master, pointer, logs, inbox | *What's next*, UI render | §{section.prism-desk-and-prism-meta} |
| PRISM Meta | Periodic | Worksheet, ML-log, meta inbox | Meta artifacts | §{section.prism-desk-and-prism-meta} |
| OPEN_ITEMS inbox | Append per writer; drain per owner-turn | Any session | Any session (append) | §{section.cross-lane-inbox} |
| PRISM UI | Per Desk render | The repo Model | (view only) | §{section.prism-ui} |

### 2.4 Lifecycle slots
<a id="section-lifecycle-slots"></a>

Every construct fires in exactly one lifecycle slot.

| Slot | What fires here |
|---|---|
| Setup-only | All probes (P1–P7) |
| Per session-open | M1 (also fires per-turn), M2, SP-13 substrate verification |
| Per orchestration turn | M3, M4, M5, M11, *What's next* write, Master append, inbox drain (repo_backed lanes) |
| Per dispatch | Envelope production, Self-check execution, Output return, Vendor Selection |
| Per Layer-1 ingestion | M6, M7, M8, M12, Vendor Triangulation (if applicable), reconciliation |
| Per Layer-2 synthesis | M9 (also Layer-1) |
| Out-of-band | Update session, point refresh (in-Setup) |
| 🔴 band | Migration handoff |
| Per standing-lane session-open | Lane resume + inbox drain + M5 self-band (§{section.lanes-roles-and-the-prism-ui}) |
| Engagement close | Closure gate — three-layer close sweep (§{section.engagement-closure}) |
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
- **How to run parallel lanes, the Desk, or the cross-lane inbox** → §{section.lanes-roles-and-the-prism-ui}.
- **The Setup onboarding flow or quick mode** → §{section.setup-onboarding-and-mode-selection}.
- **How to close an engagement** → §{section.engagement-closure}.
- **The report architecture, the workbook, or the presentation house-style** → §{appendix.report-architecture}.
- **How to share the engagement externally** → §{appendix.external-share}.

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
  (`PRISM_lens_library.md` v0.16); the Prompt Strategy (when separate from
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

**Front door — orientation before engagement entry** `[operator-scaffolding | stable | ✅]`

When the operator's opening message is an *orientation question* ("how do I
use PRISM", "where do I start", "what is this", "how does this work") rather
than a named construct or an audit request, **and** there is no active
engagement context (no Master attached, no subject), answer with a 30-second
orientation — not the full engagement entry, and never a framework dump: (1)
what it is — a structured multi-session, multi-vendor LLM-orchestrated audit
and research framework; (2) the reassurance — you don't need to read it all,
a lean always-loaded core pulls reference bundles on demand; (3) the one
action — `/prism-start [subject]`, or "Run a PRISM audit/brief on [subject]";
(4) the heaviness choice — a quick brief or a full audit (same rigor, less
machinery; you can graduate later). Then offer to begin. Treat "the operator
asks how to use it" as the intended front door, not a malformed open.

This orientation is informational, not dependent work, so it is answered
**before** the M1 / M2 missing-input halts (§{section.m1-missing-inputs}) — it
is not an engagement open; SP-13 substrate verification
(§{section.sp-13-substrate-declaration}) still applies. `/prism-help` renders the
same orientation; beginning an engagement hands off to `/prism-start` (Setup is
not duplicated here).

### 3.2 The triple contract `[structural | stable]`
<a id="section-the-triple-contract"></a>

Three blocks — Envelope (inbound), Self-check (between envelope and task
body), Output (outbound). All three are visually distinctive, self-contained,
and produced by orchestration's Vendor Selection step (§{section.vendor-selection-at-dispatch}) at dispatch
time. The contract is the load-bearing interface between sessions; it
survives mode changes (manual paste-chat today; automated dispatch later)
unchanged. The dispatched paste is additionally wrapped by a
**transport-integrity bracket** (§{section.transport-integrity-bracket}) — a
top-of-paste integrity anchor and a terminal sentinel — that frames the contract
so the execution session can detect a truncated copy, but is **not** a fourth
contract block.

#### 3.2.1 PRISM Execution Envelope
<a id="section-prism-execution-envelope"></a>

```
━━━ PRISM EXECUTION ENVELOPE ━━━
Prompt ID:          [identifier — purpose/title]
Dispatch ID:        [unique per dispatch instance; orchestration-generated; copy verbatim]
Project:            [project name]
Master version:     [filename of Master at dispatch time]
Prompt digest:      [orchestration-generated at dispatch; copy verbatim; never recomputed]
Posture:            epistemic | investigation
Vendor:             [vendor] | multi-vendor          ← epistemic posture [do-not-paste]
Dispatch shape:     equivalence | split | limitation-named   ← epistemic posture [do-not-paste]
Dispatch rationale: [one positive-framing line per variant; see §4.2]   ← epistemic posture [do-not-paste]
Vendor config:      [vendor-specific config flags]
Session hygiene:    [fresh session, project attachment posture, web search on/off]
Tools:              [vendor tools requested; reserved slot for plugins/skills]
Attachments:        [filename, filename, ...]
Expected output:    [filename to download as]
Operator hints:     [zero or more one-line cues; see §3.2.4]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Orchestration-side record.** This is the orchestration-side record of a
dispatch; it is **never pasted whole** to an execution seat — the execution
session receives the seat view (E.1a, §{appendix.execution-seat-paste-envelope-view}),
the Envelope minus the triangulation fields. The record pairs with the
never-copyable dispatch card (§{appendix.outbound-dispatch-card}).

**Field semantics.**

- `Prompt ID` — short unique identifier + purpose/title, unrelated to phase.
  Identifies the *pass*, not the dispatch instance — a re-dispatch of the same
  pass (§{section.asymmetric-parallel-return-handling}, the failure leg) reuses
  the Prompt ID.
- `Dispatch ID` — a unique identifier minted per *dispatch instance*, distinct
  from the Prompt ID and travelling *paired with* the `Prompt digest`. The
  digest verifies the body was copied through faithfully; the Dispatch ID
  identifies *which dispatch* a return belongs to. Two dispatches of the same
  pass (same body ⇒ same digest) carry distinct Dispatch IDs, so a return
  reconciles to the exact dispatch that produced it
  (§{section.recommended-vs-executed-reconciliation}) — closing the
  re-dispatch ambiguity a digest-only check cannot. Orchestration generates it
  at dispatch; execution copies it verbatim into the Output signature; it is
  never recomputed at return.
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
the SP-16 uninvited-frame audit (§{section.sp-16-the-elephant-rule}, the
Elephant Rule) and the SP-18 recompute gate (§{section.sp-18-it-must-recompute})
as its output-side steps, and opens with the transport-integrity check
(§{section.transport-integrity-bracket}) as a pre-task Step 0. Sits between the
Envelope and the task body; step 0 and steps 1–4 fire before the task,
steps 5–6 fire before the Output is emitted.

```
━━━ PRISM EXECUTION SELF-CHECK ━━━
Before doing the task:

0. Transport-integrity check (completeness of INPUT).
   Before step 1, scroll to the very end of this paste.
   Confirm the last line is the terminal sentinel
   "━━━ END PRISM DISPATCHED PASTE — <Dispatch ID> ━━━"
   and that its Dispatch ID matches the Dispatch ID in the
   PRISM PROMPT INTEGRITY anchor at the top — and is a real
   value, not the literal "<Dispatch ID>" placeholder. If
   the sentinel is absent, the two Dispatch IDs differ, or
   either is still the placeholder, the paste was truncated
   or corrupted in transport — STOP. Emit a one-line
   truncation report and do not start the task. Presence and
   string-match only; never recompute the digest. (Restates
   the top-of-paste anchor, the truncation-surviving copy,
   which governs on any disagreement.)
   On a clean Step 0, emit the matched Dispatch ID
   as your first token, before any task output; on
   a failed/truncated Step 0, the one-line
   truncation report is your first token instead.
   Any other first token means the gate did not run.
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
   negation ("not Y", "X, not Y", "rather than
   Y", "no Y"), defensive intensifier ("real",
   "actual", "truly"), and temporal hedge ("for
   now", "currently") in the findings content;
   tag each called-for (naming the live
   alternative it answers) or uncalled-for
   (rewrite positively before release). A
   self-bounding verb ("shrink", "slow",
   "narrow") makes a trailing denial of the
   unbounded case uncalled-for by default; a
   worst-case section makes the extreme a
   called question. Headings and opening
   sentences first (SP-16, the Elephant Rule).
6. Before emitting the Output: recompute every
   stated quantitative relationship from the
   document's own numbers; re-count every
   enumeration intro against its list; verify
   repeated structures as a set; re-read every
   sourced claim against its source — same
   noun, same metric. Exact match or rewrite;
   never round silently (SP-18, It must
   recompute).
   Write each recompute out in full — operands
   and operation on their own line, in the
   Appendix K form (e.g. "share = 11 = 6+2+1+2") —
   and compare that written line to the stated
   value; do not assert "recomputed/matches"
   without the line. Worked lines stay in the
   working pass, not the shipped deliverable
   (SP-17).
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Behavior contract.**

- Step 0 is the transport-integrity input-gate
  (§{section.transport-integrity-bracket}): the completeness-of-INPUT halt the
  dispatch conventions sanction (§{appendix.dispatch-conventions}, J.2 — INPUT
  is the only place the vendor may halt). It restates the top-of-paste anchor,
  which is the truncation-surviving copy and governs on disagreement; absent or
  mismatched, it halts with a one-line truncation report as the deliverable,
  mirroring the mismatch-halts-task contract of steps 1–4. The echo
  (first-token Dispatch-ID emission) makes a silent Step-0 skip
  detectable; it is the lowest-capability, vendor-agnostic observability
  demand and adds no new halt class. The echoed line sits **outside** the
  `PRISM EXECUTION OUTPUT` block and is **not** a reconciliation handle —
  return reconciliation still reads the Dispatch ID + digest from the
  Output signature only (§{section.transport-integrity-bracket}); the echo
  is observability-only, discarded on convergence.
- The vendor session must self-identify before touching task content.
  Self-identification is best-effort honest — vendors that cannot introspect
  a field hedge on it rather than fabricate.
- Mismatch halts the task and emits a Self-check report. The report is the
  deliverable until the operator confirms.
- "Confirmation to proceed" is a positive operator action (a message in the
  conversation), not an inferred consent from continued attachment (§{principle.SP-9}).
- Steps 5–6 are output gates, not substrate verification: they fire once
  the findings content is drafted, before the Output block is emitted.
- Step 5 audits framing across the full uninvited-frame family —
  negations, defensive intensifiers, temporal hedges. Uncalled-for
  frames are rewritten positively, not annotated
  (§{section.sp-16-the-elephant-rule}, the Elephant Rule).
- Step 6 is mechanical only (§{section.sp-18-it-must-recompute}, It
  must recompute): recompute arithmetic, re-count enumerations, verify
  repeated structures as a set, re-read sourced claims for
  noun-and-metric congruence. Exact match or rewrite; silent rounding
  is a violation. Writing the line out is the mechanism, not a bare
  assertion that it was checked; the notation reuses the visible-recompute
  form of §{appendix.report-architecture} (Appendix K). The worked lines
  belong to the working pass, kept out of the shipped deliverable per
  §{principle.SP-17}.
  Judgment-class principles (§{principle.SP-17},
  §{principle.SP-19}, §{principle.SP-20}) enforce via the Independent
  Validation Dispatch (§{section.independent-validation-dispatch}) and
  the Lens Library, with no Self-check step.

**Multi-vendor empirical footing.** Verified on Claude Opus-class and
Sonnet-class models. Gemini, ChatGPT, Perplexity behavior under this
block is **report-worthy finding** per DD.§3.5 — operators report
divergences. See §{section.empirical-calibration-items}. Step 0's
pre-task STOP is a stronger instruction-following demand than self-ID, so
non-Claude adherence to the transport-integrity halt — and to the first-token
Dispatch-ID echo a clean Step 0 emits before any task output — is itself a
report-worthy calibration item, and a vendor that ignores Step 0 is no worse
off than before the gate existed.

#### 3.2.3 PRISM Execution Output
<a id="section-prism-execution-output"></a>

Every execution session produces a `.md` file whose contents are wrapped in
this signature.

```
━━━ PRISM EXECUTION OUTPUT ━━━
Prompt ID:        [identifier — purpose/title]
Dispatch ID:      [copied verbatim from Envelope]
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

- `Vendor` and `Vendor config` reflect the vendor's *self-reported* executed
  state, not *recommended* state. These are an **advisory self-ID cross-check**
  for
  recommended-vs-executed reconciliation
  (§{section.recommended-vs-executed-reconciliation}); the authoritative
  handle is the operator-set filename (§{principle.SP-14}, §{principle.SP-21}).
  A self-ID that disagrees with the filename is logged as a drift signal, not
  an error.
- `Schema version` — currently `output-v1`. Bumps when the Output block's
  structure changes; orchestration's Layer-1 convergence flags
  incompatibilities at ingestion.
- `Dispatch ID` — copied verbatim from the Envelope. It is the dispatch-
  instance handle: reconciliation (§{section.recommended-vs-executed-reconciliation})
  matches a return to its dispatch on the triple of operator-set **filename**
  (which seat/vendor, §{principle.SP-14}), **Dispatch ID** (which dispatch
  instance), and **Prompt digest** (body copy-through integrity). The Dispatch
  ID is the identifier the digest deliberately is *not* — so a re-dispatch of
  the same pass (§{section.asymmetric-parallel-return-handling}, the failure
  leg), which produces an identical digest, still reconciles unambiguously to
  the right instance.
- `Prompt digest` — detects wrong-prompt / wrong-attachment delivery at
  dispatch boundaries. Mechanism: orchestration generates the digest at
  dispatch time and writes it into the Envelope; execution copies it
  verbatim from the Envelope into the Output signature; orchestration
  compares the returned copy against the original. Verifies copy-through,
  not cryptographic computation by the execution model. Generating the
  digest at return time provides zero integrity check — there is nothing
  to compare against. The digest **preimage is pinned** so the same value
  reproduces on a re-stage: the byte scope is the content between the paste
  fences, with the Envelope's (and Output's) `Reference:`/`Prompt digest:` line
  set to the sentinel `sha256:PENDING`, the transport-integrity bracket
  (§{section.transport-integrity-bracket}) — the `PRISM PROMPT INTEGRITY` anchor
  block in full and the terminal `━━━ END PRISM DISPATCHED PASTE` sentinel —
  **excluded** from the byte scope as transport framing, and no trailing-newline
  normalization. (The bracket's own `Prompt digest:` line is display-only and is
  not normalized, because the whole anchor block is excluded.) An unpinned
  preimage stays consistent *within* a session but a later re-stage cannot
  reproduce it; the pinned recipe is in §{appendix.dispatch-conventions}
  (dispatch conventions).
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

#### 3.2.5 Transport-integrity bracket `[structural | stable]`
<a id="section-transport-integrity-bracket"></a>

The triple contract (§{section.the-triple-contract}) is what a dispatch
*means*; the **transport-integrity bracket** is what lets the execution session
confirm the whole paste *arrived*. A dispatched paste can be copied while it is
still streaming — the operator grabs the text before the tail has finished
writing — and a bottom-placed integrity instruction is then silently absent
exactly when it is needed. The bracket wraps the paste between two
transport-framing lines, with the load-bearing check declared at the very
**top** so it survives a truncated copy.

**Open — the integrity anchor.** Orchestration renders, as the literal **first
line** of the dispatched paste (inside the outer fence, so a copy-all captures
it; below the never-copy-able dispatch card, §{appendix.outbound-dispatch-card}),
a `PRISM PROMPT INTEGRITY` block declaring the `Dispatch ID` — and the `Prompt
digest`, for the operator's reference — and the completeness rule:

```
━━━ PRISM PROMPT INTEGRITY ━━━
Dispatch ID:    [orchestration-minted; a real value, never a placeholder]
Prompt digest:  [display-only copy; the Dispatch ID is what Step 0 matches]
Completeness:   This paste is complete ONLY if its LAST line is the terminal
                sentinel "━━━ END PRISM DISPATCHED PASTE — <Dispatch ID> ━━━"
                carrying THIS Dispatch ID. Before any task work, scroll to the
                end and confirm that line is present and its Dispatch ID matches
                the one above (and is a real value, not the literal text
                "<Dispatch ID>"). If it is absent, the Dispatch ID differs, or
                either is still the placeholder, the paste was truncated or
                corrupted in transport — STOP, emit a one-line truncation
                report, and do not begin the task. Presence + string-match
                only — never recompute the digest.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Close — the terminal sentinel.** Orchestration renders, as the literal
**last line** of the dispatched paste (after the Output-signature instruction
and a blank separator, so a vendor cannot fold it into the Output block it
produces):

```
━━━ END PRISM DISPATCHED PASTE — <Dispatch ID> ━━━
```

**The check — Self-check Step 0.** The execution session runs Step 0
(§{section.prism-execution-self-check}) before any other work: confirm the
terminal sentinel is present and its Dispatch ID matches the anchor's (and is
not the placeholder). This is a **presence + string-match**, never a hash
recompute — an execution model cannot reliably compute a digest
(§{section.prism-execution-output}). It makes concrete the completeness-of-INPUT
halt the dispatch conventions already sanction (the "only INPUT may halt"
discipline, §{appendix.dispatch-conventions}, J.2), not a new halt class.
**Scope.** Step 0 catches a *truncated tail* — the copied-before-finished case,
detected by the missing terminal sentinel; it does **not** detect interior body
corruption, which the return-side digest copy-through catches at reconciliation
(§{section.recommended-vs-executed-reconciliation}).

**It frames the contract; it is not part of it.** The bracket is transport
framing around the three contract blocks (Envelope / Self-check / Output), not a
fourth block — every "three blocks" / "first block" / "bookending" statement
stays true. It names no vendor, arm-count, or shape, so it keeps the vendor
PRISM-unaware and survives the single-arm strip
(§{section.atomic-prompt-self-containment}). It wraps **any** dispatched paste
carrying a Dispatch ID + digest — the epistemic Envelope and the
investigation-posture corpus-access paste (§{section.corpus-access-dispatch})
alike — but **not** envelope-less sub-agent fan-out, which carries no Dispatch
ID to bracket.

**Preimage and reconciliation are untouched.** The anchor block and the
terminal sentinel are **excluded from the digest preimage**
(§{appendix.dispatch-conventions}, J.3), so they introduce no new value and the
digest stays reproducible; the anchor's digest is **display-only**, never
compared execution-side and never a return handle — return reconciliation reads
the Dispatch ID + digest from the **Output signature** only
(§{section.recommended-vs-executed-reconciliation}).

**Convention, not a Standing Principle.** Like the copy-through digest and the
Dispatch-ID pairing, this is a contract mechanic with a single artifact and a
binary surface (present/absent, match/not) — it earns a Self-check step, not an
SP, and is **not** an extension of §{principle.SP-22} (a rendering discipline
with no Self-check step). Adherence on non-Claude substrates is a report-worthy
calibration item, as for the rest of the Self-check.

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

**Concurrency split (repo_backed lanes).** *What's next* is the lane's
single-writer pointer (tier 2): only its owner rewrites it, once per turn,
carrying the live pointer forward. Multi-writer content — standing FM-watches,
open items, and cross-lane candidates — moves OUT to the append-only
`OPEN_ITEMS` inbox (§{section.cross-lane-inbox}); the body keeps the `Master
version:` pointer, band, current-state summary, recommended next action, the
dispatch-ready payload, and this-turn hints. The resume protocol gains one
step: read *What's next* → **drain `OPEN_ITEMS`** → Master.

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

**Four-step routine.**

1. **Retrieval shape.** Classify the dominant retrieval shape of the
   load-bearing evidence: *synthesis* (reason/triangulate over many sources)
   vs *fetch* of specific known documents. Synthesis mode and fetch capability
   are different axes — "Research mode" is a synthesis posture, not a fetch
   capability, and must not stand in for one. When the load-bearing evidence is
   specific known-URL documents, name the fetch capability using the
   corpus-access `Driver` enum (`vendor-executed | cowork-mcp | manual`,
   §{section.corpus-access-dispatch}) rather than folding the fetch under a
   research pick, and prefer capture-then-attach (capture once, attach to the
   paste) to remove the fetch dependency. A capability-caused "could not fetch"
   is a capability null, not a substantive null. An **operator-run agentic
   browser** (Comet, Atlas, and the like) is a *distinct driver class* from the
   enum's `cowork-mcp` value, where PRISM drives the Chrome MCP itself: the
   third-party agent runs outside PRISM's control, is investigation-posture
   single-source (§{principle.SP-15}) and never a triangulation seat, and
   everything it returns needs first-hand verification (confident prose ≠
   verified). Its per-driver reliability profile accrues to
   §{appendix.vendor-parsing-observations} (vendor parsing observations).
2. **Refresh.** Run a web-search-based currency check on the specific
   decision: is the recommended vendor still the right call for this prompt
   shape? Are there known issues this week? Has a newer vendor capability
   changed the calculus? Output: a 2–4 line refresh note with citations.
3. **Structured outcomes.** Where refresh produces a confident specific
   recommendation, the configuration is written into the Envelope
   (`Vendor:`, `Vendor config:`, `Tools:`). No operator decision required.
4. **Soft outcomes — recommendation bubble.** Where refresh produces a
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

### 3.7 Lanes, roles, and the PRISM UI `[structural | stable]`
<a id="section-lanes-roles-and-the-prism-ui"></a>

An engagement is not one session in sequence; it is **parallel lanes of
work**, each resumed and advanced by sessions occupying distinct **roles**,
with a single operator-facing surface — the **PRISM UI** — rendered over the
repo. This section is the operating model. Reference-grade detail (the full
role matrix, the UI rendering and trajectory views, the Setup-onboarding SI
template and install cards) lives in Appendix I
(§{appendix.lanes-roles-prism-ui}), fetched on demand.

**The net-helpful bar (the load-bearing constraint).** The lane/role
machinery is the *session's* bookkeeping, never the *operator's*. A session
decides which lane and role it occupies and whether to isolate or work
inline; it drives the operator only through plain nudges (the *What's next*
recommended action, the dispatch-ready payload, operator hints, the band).
**Success criterion: if a construct makes the operator track which lane or
role they are in, it has failed.** This is SP-22 (§{principle.SP-22}) applied
to the operating model.

#### 3.7.1 Lanes — the unit of parallel work
<a id="section-lanes"></a>

A **lane** = {a resume pointer, an append-only log, an inbox, one concern}.
A session is a worker that resumes a lane, appends to its log, drains its
inbox, and updates its pointer.

- **Object lane** — the engagement itself: *What's next*
  (§{section.whats-next}, the pointer) + the Master (§{section.the-master}) +
  the findings / E-log + `OPEN_ITEMS.md` (§{section.cross-lane-inbox}).
- **Meta lane** — methodology work on PRISM itself: the meta resume-pointer
  (the latest meta handoff) + the worksheet + the ML-log +
  `OPEN_ITEMS_meta.md`.

`persistence: repo_backed` (§{section.repo-backed-mechanics}) is the enabler —
it makes any lane resumable from any surface; without it, lane work degrades
to file-carrying. The general resume protocol is: **identify your lane →
resume from its pointer → drain its inbox → honor lane boundaries.**
Cross-lane work travels by inbox append, never by editing another lane's
pointer (§{section.cross-lane-inbox}).

#### 3.7.2 Roles × context-tier — a flexible matrix
<a id="section-roles-context-tier"></a>

A lane is worked by sessions in distinct **roles**, and **role and
context-tier are independent axes**. Context-tier = PRISM-loaded
*orchestration* vs clean *execution*. The object-lane roles — Setup,
Planner/Steward (the PRISM Desk), Dispatch-builder, Dispatch-consumer,
Execution-run, Convergence-run, Validation-run — and their tier anchoring are
tabulated in Appendix I (§{appendix.lanes-roles-prism-ui}). The proof the axes
are independent: a convergence run is an orchestration-*class* role run in a
clean execution-*style* context.

**Flexibility is the point.** Lanes × roles is a matrix a session occupies
*flexibly* — a session decides what it needs and may cross roles in one
sitting (a dispatch session can also converge and write the Master).
Separation is a **tool the session chooses**, not a mandatory partition.

**Three isolate options** (when a session chooses to separate): inline · a
separate session · a **clean-context sub-agent** (reads returns from
`outputs/` by path — no re-attach, no handoff). The sub-agent's bound: clean
context but **same distribution** (§{principle.SP-15}) — a fine converger or
clean reader, **never a triangulation seat**, and weaker than a
distinct-vendor Independent Validation Dispatch
(§{section.independent-validation-dispatch}).

**The sub-agent is the DEFAULT, not merely an option, for a clean-context
role.** A framework-loaded orchestration session (full PRISM core in context)
is **contaminated** for any clean-context-class role — a convergence run
especially, also a fresh independent read or clean drafting. The session must
**self-trigger** the sub-agent on that recognition ("core in context → a
clean-context role goes to a sub-agent"), not wait for an operator prompt.
Hand the sub-agent return-paths + method only — never your own conclusions —
so its read stays independent. The convergence leg specifically: the
dispatch-consumer saves and verifies the N returns, then launches a
clean-context sub-agent to converge; the sub-agent writes its convergence to
`outputs/` and the **parent** absorbs it and writes the Master (the sub-agent
never touches canonical state). Convergence ≠ validation: the IVD remains a
separate, distinct-vendor adversarial step on the deliverable.

#### 3.7.3 The cross-lane inbox — `OPEN_ITEMS` `[structural | stable]`
<a id="section-cross-lane-inbox"></a>

Multi-writer content does not belong in a single-writer replace-in-place
file. Classify every `repo_backed` artifact by **concurrency shape**:

| Tier | Shape | Examples | Discipline |
|---|---|---|---|
| 1 | Append-only (many disjoint writers) | E-log, ML-log, **`OPEN_ITEMS.md`** | per-writer namespaced IDs (no shared counter); one canonical line format; rebase on the live tail |
| 2 | Single-writer pointer (replace-in-place) | *What's next* body | the lane owner rewrites once per turn; every write carries the live pointer forward |
| 3 | Single-lineage canonical state | the Master (one file; do not decompose) | bump-from-live + reset-on-reject; append-mostly |

**The inbox.** Each lane gets an append-only inbox at a fixed repo path
beside its pointer (object lane `OPEN_ITEMS.md`; meta lane
`OPEN_ITEMS_meta.md`). One canonical item-line format so a tail scan is never
format-blind:

```
- [<writer-ns-id>] · <YYYY-MM-DD> · <kind> · <text> · disposition: open
```

- `<writer-ns-id>` is **namespaced per writer** (`E-87`, `ML-46`,
  `Desk-15-03`) — never a global counter.
- `<kind>` ∈ `open-item` | `fm-watch` | `cross-lane` | `bundle-miss`
  (§{section.bundle-load-integrity}).
- **Dispositions are append-only too** — a transition is a new appended line,
  never an in-place edit; the original block stays as the audit trail. `open`
  → `drained(<lane/session>, <note>)` | `declined(<reason>)`. A drained or
  declined item is retained (optionally archived at close); draining ≠
  deleting.

**Append discipline (tier-1).** Any session — dispatch, Desk, meta, or
sub-agent — *appends*, rebasing on the live tail first. An append is
structurally unable to clobber a pointer because it never touches the pointer
file.

**Drain protocol (the single-writer act).** At its turn the lane **owner**
(the Planner/Steward — the PRISM Desk for the object lane) reads the pointer
*and* the inbox; for each non-terminal item it **folds** the item into the
Strategy / next-action / register, then **appends a `drained` line**. Draining
is part of resume *and* of every turn-close
(§{section.failsafe-recovery-continuous-state-mechanics}).

**Cross-lane handoffs.** When lane A produces something lane B must action (an
object session spots a candidate-ML for the meta lane), A appends a
`cross-lane` item to B's inbox; B drains on resume. Promotion becomes
pull-on-resume, not push-on-operator-memory — which kills the orphan risk. The
close-time both-logs merge is the backstop.

**Commit discipline (the companion rule; closes the stale-snapshot clobber).**
Promoted to `repo_backed` mechanics: (a) **rebase on the live tail** before
every push; (b) **commit only the files you mutated** — explicit paths, never
a full-folder snapshot; a session that did not change a log / state / Master
does not stage it; (c) **commit-then-confirm** — read the file back or verify
the SHA on `origin` before reporting it written. Append-only files are
merge-safe under this rule: disjoint appends never conflict once each writer
rebases. *(Repo-integrity commit-discipline for the maintainer environments
themselves also lives in the engagement SI and the multi-committer protocol,
which the framework references rather than re-specifies.)*

**M2 tie-break.** Once the inbox + commit-discipline are in force, the
pointer-clobber that the M2 clobbered-pointer tie-break
(§{section.m2-version-drift}) repairs stops occurring; the tie-break remains
the safety net for legacy cases.

#### 3.7.4 PRISM Desk and PRISM Meta — the standing lanes `[structural | stable]`
<a id="section-prism-desk-and-prism-meta"></a>

Two **standing lanes** are first-class framework constructs, re-opened by the
operator over the life of an engagement:

- **PRISM Desk** — the object lane's **Planner/Steward** ("your what's-next
  desk"). It owns the *What's next* pointer and the drain, and renders the
  PRISM UI (§{section.prism-ui}). Re-opened per round **or periodically**; a
  Desk opened after a gap **catches up by re-syncing from the canonical repo**
  — render-from-verified-model (verify repo state, *then* render; the repo
  accumulates, so the Desk rebuilds from artifacts, not memory).
- **PRISM Meta** — the methodology lane (reflection / synthesis /
  worksheet-building), opened periodically.

**Desk role discipline.**

- **Dispatches, never executes inline** — the Desk plans and stages;
  vendor / execution work goes to an execution run or a sub-agent.
- **State-correction is in remit, not only advancement** — the Desk may
  correct a stale or clobbered pointer (reconcile to the corroborated maximum,
  §{section.m2-version-drift}), not just move state forward.
- **Propagate to all dependents; never make the operator the
  coherence-checker** — when state changes, the Desk updates every dependent
  artifact and the staged next-opener, rather than leaving the operator to
  notice the incoherence.
- **Catch-one → propose-a-sweep.** When any orchestration session catches one
  instance of a recurring defect (an opaque code, an unverified claim, a stale
  pointer), it proposes a *systematic* sweep / reusable prompt / codification
  rather than fixing only the one — internalizing vigilance the framework would
  otherwise externalize onto the operator.

**The stop-set (auto vs ask).** The Desk and standing sessions **pause only at
real gates** — ratify strategy (P0→P1), any scope change, ratify close, and
anything sent outward to the client (an external deliverable; a push to a
shared `main` is a coordination / outward act) — and otherwise **auto-handle
routine work** (save / verify / converge returns, stage the next pass, file
bookkeeping, drain the inbox) and report. This is the net-helpful bar made
concrete: do the routine, surface the consequential.

**`<Lane>-<N>` session numbering.** Number standing-lane sessions
`<Lane>-<N>` (e.g. `Meta-4`, `Desk-12`). **N is assigned by the opening
handoff / pointer** (hand-forward, not self-grabbed — the same
single-writer-pointer discipline as *What's next*, so no shared-counter race),
stamped on every log entry and handoff, and backed by the immutable
commit-range (the friendly label is a rendering; the commit-range is the
race-proof anchor). Ephemeral roles are not numbered — they carry identity as
SP-14 filenames (§{principle.SP-14}) on their outputs.

**`/prism-meta` (lane-entry command).** The meta-lane sibling of
`/prism-start` and `/prism-whats-next`: it pulls canonical repo state, reads
the meta resume-pointer, drains `OPEN_ITEMS_meta.md`, adopts the session
number `N` from the pointer, and announces it ("Meta-4, resuming from
ML-45"). "Command vs carry-over file" is a false choice — the command *reads*
the carry-over pointer; under `repo_backed` no push-handoff is needed, and it
degrades to ask / paste off-repo.

#### 3.7.5 The PRISM UI — the operator-facing view `[structural | stable]`
<a id="section-prism-ui"></a>

Rendered consistently round-to-round, the Desk **is** the operator's single
pane of glass — a **View + Controller** over the repo **Model** (Master /
pointer / logs / worksheet). The lanes / roles / concurrency are the internal
model; the PRISM UI is the view that hides them and shows only rendered state
+ next action.

**Three surfaces.**

- **STATE view** — the trajectory / arc-to-close map (where the engagement is
  and what remains, with the critical path and the bottleneck).
- **HEALTH view** — the re-sync: HEAD == mirror, pointer present, no ghost
  session, the band, **pending cross-lane inbox items**, and the bundle-load
  audit (§{section.bundle-load-integrity}).
- **ACTION surface** — the staged paste + nudges (the dispatch-ready payload,
  the next opener).

**Make-it-a-real-UI discipline.** (1) **Consistent rendered component
schemas** — a stable visual language round-to-round, so the operator scans at
low load; swapping the metaphor each render imposes a re-learning tax. (2)
**Render-from-verified-model** — the re-sync integrity check runs *before*
rendering, so the view cannot drift or hallucinate state. (3) **Generated /
conversational** — the operator can ask for any view ("trajectory") and get it
on demand. The STATE view's two modes (a dependency / critical-path map and a
progress timeline, shown side by side with a colored status encoding and a
code → real-name legend) and the worked renders are in Appendix I
(§{appendix.lanes-roles-prism-ui}).

#### 3.7.6 Bundle-load integrity `[structural | stable]`
<a id="section-bundle-load-integrity"></a>

The core is lean and fetches reference bundles on demand
(§{section.resource-fetch-convention}); a session must reliably load the right
bundle for the role it occupies. Order-keeping is **not centralized in the
Desk** — it is distributed across every session, defense-in-depth:

- **Front line (every session, real-time).** The core carries a **phase →
  bundle manifest** and each session runs a **visible self-check** on entry
  against it ("role = Setup → load `reference/setup.md` ✓"), the same
  verify-don't-assert posture as the SP-13 substrate check. Operating without a
  required bundle is **fail-loud**, not a silent gap: the core stub for a
  gutted area says "you cannot run this from core alone — fetch the bundle."
- **Opportunistic (any session).** A session that notices a *prior* pass ran
  phase-work without its bundle **flags it** — appends a `bundle-miss` item to
  the inbox (§{section.cross-lane-inbox}) — and fixes it if the correction is
  simple and safe.
- **Backstop (the Desk, periodic).** The Desk's HEALTH-view re-sync
  (§{section.prism-ui}) gains a **bundle-load audit**: read the manifest
  against the Master's record of what ran since the last re-sync, flag any pass
  that did phase-work without its bundle, and propagate the correction
  (surface-translated — the operator sees "re-check pass X," not the
  machinery).

**Phase → bundle manifest (kept in core).**

| Role / occasion | Required bundle |
|---|---|
| Setup session · probe iteration · P0→P1 | `reference/setup.md` (Setup mechanics — probes, three-layer readiness, Setup-artifact procedures); `lens/PRISM_lens_library.md` (Probe 1 grading); `reference/templates.md` (Setup artifacts) |
| Producing a Setup / dispatch artifact | `reference/templates.md` |
| Update session · currency check at session open | `reference/currency.md` (point-refresh, the Update session, the session-open currency check) |
| Resume / missing handoff · M5 band 🟠 / 🔴 | `reference/continuity.md` (migration handoff, failsafe recovery, defensive migration) — the in-core recovery floor stays resident |
| A pass classified corpus-access | `reference/corpus-access.md` (the corpus-access dispatch) |
| Non-default surface · `repo_backed` | `reference/modes-and-surfaces.md` |
| Lanes / Desk / UI / onboarding work | `reference/lanes-ui.md` |
| Vendor parsing on returns | `reference/vendor-parsing.md` |
| Tracing a decision's rationale | `reference/provenance.md` |

The manifest is the structural contract the core-slimming refactor populates as
it moves phase-scoped sections (Setup, currency, continuity, corpus-access)
into their own bundles; this integrity layer is its safety net.

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
external-reference-corpus lookup) — is investigation posture: the N loci each
*retrieve* the same material rather than *reason over* it, so for **retrieved**
facts (routes, records, policies read off the page) multiplicity buys recall,
not falsification across distributions. A retrieval-only coverage fan is handled
by recall-merge with a retrieval-consistency note and is **never** routed here.
Because an investigation-posture Envelope structurally lacks `Dispatch shape`,
this guard is mechanical, not a matter of operator discipline
(§{principle.SP-15}, §{principle.SP-21}).

**Scope — retrieved vs inferred.** The recall-not-falsification rule scopes to
*retrieved* facts only. When the fanned loci do not merely read material back
but **infer** over it — a tool asserting "this site is mobile-responsive," a
browser reasoning a form-factor — their disagreements *are* a cross-check, not
a retrieval-consistency note. Such an inferred claim carries the `inferred`
side of the retrieved|inferred axis
(§{section.prompt-body-convergence-provisions}) and is treated as
triangulation-grade: convergence is load-bearing, and a contested inferred
claim is verified first-hand before it enters the Master. Multiplicity over
inferring loci buys falsification, not merely recall.

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
with named gaps; operator decides whether to re-dispatch. This is Stage 4–5
of the dispatch lifecycle (§{section.dispatch-lifecycle}): the inbound half of
the round-trip, specified as deliberately as the outbound half.

**The return-handling card.** The inbound mirror of the outbound dispatch
card — authored *at dispatch-build* and surfaced **proactively** when the
returns are due, never waiting for the operator to ask "what do I do with
these?" Default posture is **attach-and-the-session-handles**: the operator
attaches the N returns and the session does the bookkeeping — save each per
filename discipline (§{principle.SP-14}, `[project]_[promptID]_[vendor].md`),
reconcile each on filename + Dispatch ID + digest
(§{section.recommended-vs-executed-reconciliation}), converge in a
clean-context sub-agent (§{section.roles-context-tier}, the seam-③ default;
the sub-agent never touches canonical state), then continue. File bookkeeping
is the session's job, never the operator's. The card schema is in
§{appendix.templates-compendium} (templates compendium); on a thin orchestration
surface it degrades to operator-as-committer.

**Happy path.** All N clean returns arrive; Vendor Triangulation
(§{section.vendor-triangulation}) fires at N≥2 and the convergence proceeds.

**Failure leg — branch by type (do not conflate the branches).** When fewer
than N clean returns arrive, the card routes by *failure type*:

- **Seat failure** — a vendor errored, timed out, or returned an unusable
  format. This is a **capability null, not a substantive negative**: converge
  on the available returns and name the missing dimension as a coverage gap.
  Operator declares it via the close-loop mechanic
  (§{section.operator-declaration-close-loop}): `P2.3 Gemini failed — Deep
  Research timed out`; Dispatch register status `failed: [reason]`; the
  convergence delta notes the absent dimension:
  ```
  Vendor coverage gap: Gemini failed (timeout); Claude + Perplexity
  converged. Long-context many-source synthesis dimension is absent
  from this delta.
  ```
  *What's next* (§{section.whats-next}) surfaces re-dispatch as a **ranked**
  candidate at next turn-close — material only when the gap touches a falsifier
  or decision-brief item. **No automatic retry** — re-dispatch is an operator
  decision (§{principle.SP-9}; per DD.§3.6 design-authority-without-access-
  gating, the framework does not assume the operator can retry the same vendor).
- **Digest mismatch** — a return arrived but its copied-through digest (or
  Dispatch ID) does not match what was dispatched. This is the **anchor catch**
  for a wrong-prompt or mis-paste: re-grab *that one* return before converging,
  rather than absorbing a return that answers a different dispatch
  (§{section.recommended-vs-executed-reconciliation} step 4).
- **Substitution** — the operator ran a different vendor than recommended. This
  is **not a failure**: it is absorbed at convergence with no re-dispatch
  demanded (§{section.substitution-absorption}); the delta notes the diversity
  collapse.

**Substantive divergence is not failure.** Returns that *disagree* are the
normal Vendor Triangulation delta (§{section.vendor-triangulation}), not a
failure branch. Conflating disagreement-across-distributions with a seat
failure would itself be the error — the first is the load-bearing signal the
triangulation exists to surface.

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

Reconciliation keys a return on a **structural triple**: the operator-set
**filename** is the authoritative handle for *which vendor* produced it
(§{principle.SP-14} pattern `[project]_[promptID]_[vendor].md`); the copied-
through **Dispatch ID** identifies *which dispatch instance* it answers
(§{section.prism-execution-envelope}, the Execution Envelope) — so a re-dispatch
of the same pass reconciles unambiguously even though its body, and therefore
its digest, is identical to the original; and the **Prompt digest** verifies
the body was copied through faithfully. The Output signature's `Vendor:` /
`Vendor config:` self-ID is an **advisory cross-check, never the authority** —
substrate self-report is unreliable (vendors self-ID wrongly, e.g. Gemini
reporting "GPT-4o"). This is §{principle.SP-21} applied at reconciliation:
trust the structural anchors, treat self-report as advisory. Orchestration
auto-reconciles against the Envelope's recommended state at Layer-1 ingestion.
The execution-side transport-integrity anchor
(§{section.transport-integrity-bracket}) validates the *inbound* paste only and
is **never** the return-side authority — reconciliation reads the Dispatch ID
and Prompt digest from the **Output signature**, as here.

**Reconciliation states** (recorded in the Dispatch register):

- *Match* — filename-resolved vendor/config equals recommended. Status:
  `returned`.
- *Substitution* — filename-resolved vendor or config differs from
  recommended. Status: `substituted`. Both recommended and executed
  (filename-resolved) values logged.
- *Missing* — no Output ever returned. Status: `failed` or `skipped` (per
  close-loop §{section.operator-declaration-close-loop}).

*Self-ID drift* is an **orthogonal overlay**, not a fourth status: when the
signature's self-reported `Vendor`/`Vendor config` disagrees with the
operator-set filename, the **filename governs** and sets the status (Match or
Substitution) while the disagreement is logged as a **drift signal** (the
filename/self-ID mismatch *is* the vendor-drift detector) — never an error or a
halt.

**Reconciliation algorithm** (orchestration-side, at Layer-1 ingestion):

```
1. Resolve vendor/config from the operator-set FILENAME (authoritative;
   §{principle.SP-14}). Read the copied-through Dispatch ID and Prompt digest
   as STRUCTURAL ANCHORS; read Output signature self-ID fields as advisory:
   self-reported Vendor, self-reported Vendor config, Schema version.
2. Look up the Dispatch register entry by Prompt ID + Dispatch ID — the
   dispatch INSTANCE, not just the pass. A return whose Dispatch ID matches a
   superseded instance (e.g. a re-dispatched seat) reconciles to THAT instance,
   never silently to the latest dispatch of the same pass.
3. Verify Schema version compatible.
4. Verify Prompt digest equals the digest orchestration wrote into the
   Envelope dispatched under that Dispatch ID (copy-through verification — the
   structural anchor for copy integrity).
   - If mismatch: flag as "wrong prompt or wrong attachment" — operator
     escalation; re-grab this return before converging.
5. Compare filename-resolved Vendor/config to Recommended Vendor/config.
   - If match: status = returned.
   - If differs: status = substituted; log both.
6. Cross-check the signature self-ID against the filename-resolved vendor.
   - If they agree: no action.
   - If they disagree: log a drift signal in the Dispatch register (annotate
     the Executed cell, e.g. "filename-resolved X; self-ID reported Y —
     drift"); the filename's value stands. Never halt or re-dispatch on
     self-ID drift alone (a contested substantive claim is verified first-hand
     per §{principle.SP-21}, not adjudicated by self-report).
7. Ingest findings into Master's findings section with provenance keyed to the
   filename-resolved vendor:
   "P2.3 — executed on [filename-resolved Vendor / config]; recommended was
    [Recommended]; self-ID reported [self-ID] (advisory); absorbed without
    re-dispatch."
8. Vendor Triangulation (if equivalence mode) updates with this return.
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

1. The filename-resolved executed vendor (operator-set filename,
   §{principle.SP-14}) differs from the Envelope's recommended `Vendor`; the
   Output `Vendor` field is advisory self-ID (§{principle.SP-21}).
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
7. **Finding basis explicit.** Each finding marks whether its claim was
   *retrieved* (read off a source) or *inferred* (reasoned to). This axis
   decides convergence routing — recall-merge for retrieved, triangulate for
   inferred (§{principle.SP-15}); see *Finding basis — retrieved vs inferred*
   below.

**Required output structure** (the prompt body specifies this):

```
## Findings

### Finding 1 — [short title]
- Claim: [...]
- Evidence: [...]
- Provenance: [source, citation, date]
- Evidence class: [document | trace | probe | empirical-test | expert-interview | cross-check]
- Finding basis: [retrieved | inferred]
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

**Finding basis — retrieved vs inferred.** Each finding also classifies how
its claim was *obtained*: **retrieved** (a fact read off a source — routes,
slugs, policies, sub-processors, counts) or **inferred** (a conclusion
*reasoned to* — form-factor, "iOS-only", "responsive", "real labels"). The
unit is the claim, not the producer: one return routinely carries both a
retrieved layer and an inferred layer. The axis decides convergence routing.
Retrieved findings that agree across a coverage fan are **recall-merged**
(agreement recorded as a retrieval-consistency note, per the corpus-access
corollary of §{principle.SP-15}; §{section.corpus-access-dispatch}). Inferred
findings are **triangulation-grade**: a fan of inferring producers can surface
genuine falsifiable disagreement, and a contested inferred claim is verified
first-hand before it enters the Master. Orthogonal to evidence class,
verification status, and confidence — basis records *how* a claim was
obtained, not how strongly or by what evidence class.

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
prompt must be self-contained for the executing vendor. This is the
vendor-surface instance of §{principle.SP-22} (surface translation — no raw
cross-surface leakage).

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

**Single-arm — strip the orchestration machinery.** A dispatched paste is a
*single self-contained arm*: the executing vendor must not know it is one of N.
Strip the orchestration triangulation fields from the paste — `Vendor
list:` / `Dispatch shape:` (`equivalence` / `split` / `limitation-named`) /
`Dispatch rationale:` — while **retaining** the single `Vendor:` and
`Vendor config:` (required by Self-check Step 2,
§{section.prism-execution-self-check}). The arm-count and the triangulation are
orchestration-side bookkeeping; they live in the Envelope record's
do-not-paste design block (§{section.single-envelope-with-spectrum-shape}),
never in the execution unit. Pasting the orchestration envelope *as* the
execution unit is a systematic failure mode — vendors stall or abort on the
multi-vendor framing (the E35 catch). Stage 3 of the dispatch lifecycle
(§{section.dispatch-lifecycle}) dispatches this stripped single-arm paste. The
strip removes orchestration triangulation fields only; it does **not** remove
the transport-integrity bracket (§{section.transport-integrity-bracket}), which
names no vendor, arm-count, or shape and frames every dispatched paste including
the single arm.

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

### 4.13 Corpus-access dispatch (on-demand bundle) `[structural | review-if: corpus-access Phase 3 lands]`

> **Phase bundle — fetch when a pass needs corpus access.** The corpus-access
> dispatch (the `Posture: investigation` Envelope for a targeted lookup
> against an external reference corpus, brought back caveat-attached) is in
> **`reference/corpus-access.md`**, fetched on demand. **Trigger:** the
> dispatch-builder classifies a pass as corpus-access (the Vendor-Selection /
> D5 retrieval-shape step makes this explicit). You **cannot build a
> corpus-access Envelope from the core alone** — load
> `reference/corpus-access.md`. SP-4: `pass = corpus-access →
> reference/corpus-access.md loaded ✓`.

### 4.14 Independent Validation Dispatch `[methodological | stable | ✅]`
<a id="section-independent-validation-dispatch"></a>

A post-synthesis validation pattern: after substantial deliverable work
completes, orchestration generates a very short prompt for a fresh
execution session whose only context is the deliverable itself, plus the
project's other client-facing materials when cross-document consistency
is in scope. The validator checks logic, defensibility, internal
consistency, consistency against the attached materials, readability,
and overall quality — and returns a severity-tagged findings list,
routed back to the producing thread for disposition.

**Validation target — shipped equals validated.** The artifact validated is the
**complete** deliverable (the comprehensive report's body + appendices,
§{appendix.report-architecture}), not a summary. What ships must equal what was
validated: a correction made *after* validation re-stamps the revision and
re-validates-if-material before send (the deliverable bump-atomicity invariant,
§{section.bump-atomicity-routine}).

**The independence rule is the point of the construct.** The validation
prompt stays minimal, and the author's rationale, structure notes, and
known-weak-spots list stay out of the validator's context: a validator
told where to look confirms the author's map; a validator given only
the artifact draws its own. For the same reason the producing session
never validates its own output — the dispatch always lands on a fresh
session.

**Kinship and distinction.** M12 (§{section.m12-result-completeness-check},
Result Completeness Check) audits each Layer-1 return for within-domain
coverage gaps at convergence; the Validation Dispatch fires once per
deliverable, post-production, and audits the finished artifact as its
audience will read it. The Setup probes (P1–P7, §{section.the-seven-probes})
grade the draft Prompt Strategy before execution; this construct grades
the output after it.

**Default lens kit.** LL-D-019 "Who said otherwise?", LL-D-020 "Help or
ammunition?", LL-D-021 "Does a stranger follow?", and LL-D-022 "Does this
respect the reader?" — the reader-respect family — from the Lens
Library (§{section.library-integration}), plus an SP-18-style recompute
sweep (§{section.sp-18-it-must-recompute}) over the deliverable's
arithmetic, counts, and sourced claims.

**Mechanics.** The dispatch uses its own Envelope template
(§{appendix.validation-dispatch-envelope}, Appendix E.13). Posture is
epistemic; the Dispatch shape is `limitation-named` with the producing
session as the named limitation — single-vendor by design, so it fires
no Vendor Triangulation and never counts as a triangulation seat
(§{principle.SP-15}). Web search stays off unless the validation scope
includes source-checking.

**Fanned for recall — adjudicate by re-derivation.** A validation dispatch may
be *fanned* across N seats to catch more. A fanned IVD is a **coverage fan, not
a cross-vendor triangulation**: every seat reads the same finished deliverable
as ground truth, so agreement buys *recall*, not falsification across
distributions (§{principle.SP-15}, the coverage-fan corollary). Converge its
returns by **dedup + agreement-RANK + adjudicate-each-catch-by-RE-DERIVATION**
against the document (the recompute discipline of
§{section.sp-18-it-must-recompute} as the ground truth) — never an agreement
*vote* on correctness. Agreement sets *priority*, not truth: a lone-seat catch
that survives re-derivation **stands**; a multi-seat catch that fails
re-derivation is **declined**. This is the "verify contested first-hand"
discipline applied to the validator's own findings — the same posture
§{principle.SP-21} applies to vendor self-report and
§{section.prompt-body-convergence-provisions} applies to a contested inferred
claim. When the producers were themselves N (a fanned equivalence run), the
independence rule sharpens: the validator must be **distinct from all N
producers**, not merely from one. **Seat strength is not uniform.** For a
*closed-document* deliverable (validate this artifact's arithmetic and internal
consistency, no web), prefer **strong closed-document reasoners** as the IVD
seats, and weight a web-oriented seat's *miss* on a closed-document point
lightly — its strength is live-web breadth, not closed-doc recompute. Per-seat
selection guidance for the closed-document case is in
§{appendix.vendor-parsing-observations} (vendor parsing observations).

### 4.15 Dispatch lifecycle `[structural | stable]`
<a id="section-dispatch-lifecycle"></a>

A dispatch is a **bounded round-trip**, not a one-way send. PRISM historically
specified the *outbound* half well (the Envelope, operator hints, the
dispatch-ready payload) and the *inbound* half — "the N returns are back; here
is exactly what to do with them" — barely at all, so an operator had to *ask*.
The **dispatch lifecycle** names the whole round-trip as one construct: five
stages, the dispatch-scoped sibling of the engagement lifecycle (Setup →
Desk/Meta run → Closure, §{section.engagement-closure}). It is a **frame**, not new machinery — it subsumes
the existing rules **by reference** (no renumbering, which would orphan the
cross-refs): the detailed rules stay where they live.

1. **Build** (outbound, late-bound). The Desk *stages* intent — which pass, its
   inputs, the decisive caveats, a bootstrap — and a **fresh Dispatch-builder
   session renders** the Envelope + Self-check + body *just-in-time* from the
   live Master, the current conventions, and a fresh Vendor Selection
   (§{section.vendor-selection-at-dispatch}), wrapping the paste in the
   transport-integrity bracket (§{section.transport-integrity-bracket}). It does **not** replay a prompt
   frozen at Setup; it anchors to the pass **spec** so it cannot silently
   re-scope (§{section.three-layer-readiness}, Layer-1 — the late-binding rule).
2. **Dispatch** (the operator card). Above the paste sits a **rendered,
   never-copy-able** dispatch card with a fixed schema (Prompt ID · Dispatch ID
   · Posture · Dispatch shape · recommended Seats, N≥2 and never a cap ·
   Attachments|NONE · Send rule · Save-returns-as · Reconciliation ·
   Reminders); null fields are stated (`NONE`), never omitted. Schema in
   §{appendix.templates-compendium} (templates compendium). The card *recommends*
   seats; the operator's actual set governs. Every paste-ready block the Desk
   emits carries such a guide card — including the next-session **opener**,
   whose card must say *"open a NEW session and paste this there — not into this
   Desk session."*
3. **Execute** (run). The operator dispatches the **self-contained single-arm**
   paste (§{section.atomic-prompt-self-containment}) to the N seats,
   deliberately PRISM-unaware (§{section.two-session-types}) — pasting the
   orchestration envelope as the execution unit is the systematic failure mode
   the single-arm rule prevents. The paste's terminal sentinel lets a seat that
   received a truncated mid-copy halt before working (Self-check Step 0,
   §{section.transport-integrity-bracket}). Surface-degrading: Cowork can
   auto-drive; manual paste is the default.
4. **Return / converge** (inbound, happy path). A **return-handling card**,
   authored at Build and surfaced **proactively**, mirrors the outbound card.
   Default = attach-and-the-session-handles
   (§{section.asymmetric-parallel-return-handling}): the Dispatch-consumer saves
   and verifies the N returns, then converges in a **clean-context sub-agent**
   (§{section.roles-context-tier}, the seam-③ default — a core-loaded session is
   contaminated for a clean read; the sub-agent never touches canonical state),
   and the parent absorbs and writes the Master.
5. **Reconcile** (inbound, close). Each return reconciles on the structural
   triple — filename + Dispatch ID + digest
   (§{section.recommended-vs-executed-reconciliation}); the **failure leg**
   branches by type — seat-failure, digest-mismatch, substitution — without
   conflating any of them with substantive divergence
   (§{section.asymmetric-parallel-return-handling}). A verdict-critical pass
   then closes with an Independent Validation Dispatch
   (§{section.independent-validation-dispatch}), distinct from every producer.

**Cross-cutting.** The whole round-trip is **render-from-live-model**: every
stage's artifact is recomputed from live state, never cached-and-replayed. The
rendered UI view (§{section.prism-ui}), the live vendor pick
(§{section.vendor-selection-at-dispatch}), and the dispatch paste are three
faces of that one principle. The lifecycle's two object-lane roles are the
**Dispatch-builder** (renders Build) and the **Dispatch-consumer** (owns the
inbound card and absorbs the returns), tabulated with the other roles in
§{section.roles-context-tier}; session-IDs tag each session in the round-trip.

**Proportionality.** Late binding earns its keep proportional to *engagement
length × convention-accretion rate*. Freezing the Envelope at Setup is fine for
a short engagement or a pass dispatched right after Setup; the JIT rebuild pays
off when conventions and findings have accreted enough that a Setup-time render
would be stale at dispatch. The reference detail for the convention set the
stages draw on is in §{appendix.dispatch-conventions} (dispatch conventions).

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

**Self-band (per standing session / lane).** M5 fires not only on the
engagement band carried in *What's next* but on **each standing session's own
context** — every standing lane (the PRISM Desk, PRISM Meta;
§{section.prism-desk-and-prism-meta}) emits its own band read against its
numbered identity ("Meta-4 hit 🟠 at a seam → hand to Meta-5"). A standing
session **proactively calls its own handoff at a seam** when its self-band
warrants — the bookend to the SP-13 substrate check (SP-13 opens a session;
the self-band closes it). This is a Monitor extension, not a new Standing
Principle: the "heed your amber" posture is already SP-4 (monitors produce
visible output) plus M5's emission.

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

### 5.4 Migration handoff · 5.5 Failsafe recovery · 5.6 Defensive migration `[continuity → on-demand, with in-core recovery floor]`

> **In-core recovery floor (a session in trouble is never stranded).** The
> continuous-state guarantee stays resident: **the Master and *What's next*
> are written at every orchestration turn-close**, so the latest canonical
> state is always the most recent emission in the repo. If a session resumes
> without a handoff, do not regenerate from memory (SP-1) — **recover from
> the repo**: read the latest Master + *What's next*, run M2 (Version Drift)
> against the operator-declared version, and proceed from *What's next*.
>
> **Phase bundle — fetch for the full procedure.** The detailed migration-
> handoff format, the failsafe-recovery mechanics, and defensive migration at
> natural seams are in **`reference/continuity.md`**, fetched on demand.
> **Trigger:** a session resumes with a missing / abnormal handoff, or **M5
> band 🟠 / 🔴**. SP-4: `resume or M5 🟠🔴 → reference/continuity.md loaded ✓`.

## 6. Setup mechanics (on-demand bundle) `[setup phase]`

> **Phase bundle — fetch before Setup work.** The Setup-phase mechanics —
> the waterfall→iterative refinement model, **three-layer readiness**, the
> **seven probes (P1–P7)**, the Setup-artifact procedures (Decision brief /
> Stakeholder register / Claim inventory / Jurisdiction map), strategy-
> stability triggers, and onboarding / mode selection — live in
> **`reference/setup.md`**, fetched on demand. **Trigger:** no Master yet, or
> the operator initiates an engagement (the P0 boundary). You **cannot run
> the probes or clear the P0→P1 boundary from the core alone** — load
> `reference/setup.md` first. **SP-4 self-check:** `phase = Setup →
> reference/setup.md loaded ✓`. (The Engagement-closure gate stays in core;
> only the Setup-phase mechanics move.)

### 6.7 Engagement closure `[structural | stable]`
<a id="section-engagement-closure"></a>

Setup is the gate **in** — three-layer readiness (§{section.three-layer-readiness}).
Closure is the symmetric gate **out**: the same three-layer shape, opposite in
direction, and **lighter in machinery** — a verification *sweep*, not a probe
battery. An engagement does not just stop when a verdict ships; it **closes
through a gate** that leaves no loose end on any lane and hands forward to the
next engagement. This is the engagement-lifecycle bookend — Setup opens, the
PRISM Desk runs (§{section.lanes-roles-and-the-prism-ui}), closure closes — the
same arc the dispatch lifecycle mirrors at dispatch scope
(§{section.dispatch-lifecycle}).

#### Layer 1 — Object completeness

The engagement's own work is finished and shippable:

- Every dispatch-register pass (§{section.master-tracking-dispatch-register}) is
  **closed, or deferred with rationale**; the Rerun Register
  (§{section.m10-rerun-fix-required}) is clear; no monitor is left firing at HIGH.
- Every Decision-brief **falsifier** (Probe 5, §{section.probe-5-falsifier-once})
  is explicitly checked off — observed or not-observed, never silently dropped.
- The verdict(s) ship as the **comprehensive final report** — the deliverable of
  record, reflecting all the work, verdict-first and executive-scannable
  (§{appendix.report-architecture}) — plus the interactive workbook when the
  decision has a quantitative core, and any developer / action artifacts the
  engagement produced. Editions are self-contained (§{principle.SP-20}) and plain
  (§{principle.SP-17}).
- The deliverable is **polished only after it validates** — the presentation
  house-style (§{appendix.report-architecture}) runs on a deliverable the
  Independent Validation Dispatch (§{section.independent-validation-dispatch}) has
  already passed (§{principle.SP-18}); never beautify an unvalidated artifact.
- **Shipped == validated** — the revision that ships equals the revision the IVD
  validated; a post-validation correction re-stamps and re-validates-if-material
  before send (§{section.bump-atomicity-routine}).

#### Layer 2 — Lane / meta completeness

No loose end on any lane, and every learning codified:

- Every lane's cross-lane inbox is **drained** (§{section.cross-lane-inbox}) — the
  orphan sweep is now a *gate*, not only a backstop: every candidate promoted,
  none left buried in a log.
- The methodology worksheet is finalized; both logs are merged.
- **Reconcile-at-close.** Diff the finished deliverable against its reference
  architecture (§{appendix.report-architecture}) in **one** pass and codify every
  craft element that landed via production / operator polish but is not yet
  codified — the reference is reconciled against the deliverable of record, which
  closes the applied-but-not-codified pattern structurally (a learning lands in an
  artifact without being codified so it recurs). Its in-flight sibling is
  **catch-one → propose-a-sweep**.

#### Layer 3 — Operator close ratification

Explicit operator **close** ratification — silence is not closure
(§{principle.SP-9}). The engagement is left **externally share-ready**
(§{appendix.external-share}): one repo per engagement, an audience-facing README,
the de-coded share archive, and a passed redaction review — produced as a
derived, operator-gated artifact (present it; do not auto-commit unless directed).
In the PRISM UI (§{section.prism-ui}) closure is the **all-clear** state —
remaining work ∅ across every lane — at which the Desk hands forward to the next
engagement.

The closure checklist, the report architecture + craft conventions, the workbook
cockpit pattern, and the reconcile-at-close sweep are in
§{appendix.report-architecture}; the share-archive recipe, the share modes, and
the image-redaction procedure are in §{appendix.external-share}.

---

## 7. Library integration
<a id="section-library-integration"></a>

The Lens Library v0.16 is canonical and bundled at
`lens/PRISM_lens_library.md` (tag `prism-lens-v0.16`). In this Skill
archive the Library is a bundled file fetched on demand — the default
Library source for orchestration — not embedded in the core. The bundled
file is also authoritative for the artifact's own evolution: Update
sessions (§{section.currency-maintenance-update-session}) produce new versions of it. Operators on a newer
Library version pin to it explicitly (§{section.library-reference-at-setup}).

### 7.1 Library reference at Setup (on-demand) `[setup phase]`

> Detail in **`reference/setup.md`** (fetched at Setup / scope revision).
> SP-4: `setup.md loaded ✓`.

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
- `recommended_sources:` — optional; a framework-curated list of external
  reference sources the lens recommends consulting, each bound to the lens's
  `material_question:`. Populated only on lenses with a high-signal source;
  absent on the rest (like `rubric_anchor:`). Each source record carries
  `source:`, `kind:` (`narrative | structured-record`), `access:`
  (`open-web | operator-authenticated`), `framing:` (mandatory bias/handling
  caveat), `recency:` (mandatory source-scoped era/recency posture), and
  `answers:` (the material question(s) the source helps address). Consumed by
  the lens-anchored corpus-access auto-trigger
  (§{section.corpus-access-dispatch}).
- `informed_by:` — provenance only; not a runtime rubric.
- `failure_mode:` — used in operator-facing flag explanations.
- `minimum_scope_binding:` — what counts as "covered" for Probe 1
  disposition.
- `scope_integrity_probe:` — optional sharpened falsifier. When present on a
  lens, the Scope-Integrity Test (§{section.scope-integrity-test-sit}) poses it
  in place of the generic `minimum_scope_binding:` restatement when grading
  that lens to `fires-covered`.

### 7.3 Scope-Integrity Test (SIT) · 7.4 Specialist-pass promotion `[setup phase → on-demand]`

> The SIT and specialist-pass-promotion mechanics are in
> **`reference/setup.md`**, fetched when a scope-impact check or a specialist
> pass is in play. SP-4: `setup.md loaded ✓`.

### 7.5 Currency maintenance — point refresh · 7.6 Update session `[maintenance phase → on-demand]`

> Point-refresh and Update-session mechanics are in
> **`reference/currency.md`**, fetched for a currency refresh or an Update
> session. SP-4: `currency.md loaded ✓`.

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
- **Clobbered-pointer tie-break.** When the drift is a *clobbered* version
  pointer (a replace-in-place state pointer silently rolled back from a stale
  checkout, so the attached version reads *older* than a prior turn already
  advanced past), resolution is **not** a literal "repo wins" rollback to the
  attached value. Reconcile by **version-ordering** (the highest coherent
  version any corroborating artifact attests is the live state) corroborated
  **across files** (cross-check the pointer against the canonical state file's
  own stamp, the changelog, and any sibling lane's record); adopt the
  version-ordered, cross-file-corroborated value as live and treat the
  rolled-back pointer as the clobber to repair. The linchpin "repo is
  authoritative" posture still holds — but "the repo" is the corroborated
  maximum across the state, not whichever stale checkout last touched the
  pointer.

- **Inbox removes the clobber source.** Under `repo_backed` lanes, multi-writer
  watches live in the append-only `OPEN_ITEMS` inbox
  (§{section.cross-lane-inbox}), not in the replace-in-place pointer, so the
  pointer-clobber this tie-break repairs stops occurring by construction. The
  tie-break is the safety net for legacy / pre-inbox cases.

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

Spec per §{section.m5-context-pressure-monitor} — including the per-standing-session **self-band** (each standing lane's session monitors its own context, not only the engagement band) and the self-stewardship seam-handoff (§{section.prism-desk-and-prism-meta}).

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
  corrections) or a prompt's output needs explicit fix. *Not a Follow-up:*
  when a *sound* run simply wants a new or expanded dimension, that is an
  additive strategy revision (§{section.strategy-stability}, Follow-up), not
  an M10 re-run — it is not entered in the Rerun Register.
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
- **Extends to inferences, not only retrieved facts.** A probe or
  investigation that *reasons to* a conclusion (an inferred finding per
  §{section.prompt-body-convergence-provisions}) carries the same
  bounded-search disclosure: a probe's null is a **bounded null, not a
  negative** — "did not find X in the scope searched" ≠ "X is absent."
  Absence of evidence within a named scope is not evidence of absence;
  disclose the bound on the inference exactly as on the retrieval.
- Not a Monitor that fires discretely; a posture held at every retrieval
  and at every bounded inference.

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

**Note — substrate self-ID is corroboration-only (v2.15.0).** A session's
self-reported identity is unreliable as ground truth: vendors confabulate
identity (a post-training release name is absent from training data, so the
model pattern-completes to its most-discussed older sibling — e.g.
Gemini → "Gemini 1.5 Pro") and have no privileged access to their own runtime
config (they cannot reliably report mode / thinking on or off). The
authoritative seat substrate is the operator UI / API `modelVersion`, recorded
at dispatch. Treat the return self-ID (the Execution Output `Vendor:` /
`Vendor config:` fields, §{section.prism-execution-output}) as **corroboration
only**: never weight
or discount a triangulation seat on its self-report. This squares with SP-13's
best-effort-honest, hedge-don't-fabricate posture and adds: don't trust the
hedge either. See §{principle.SP-21} (trust structure, self-report advisory),
of which this is the substrate instance.

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

**Widened in v2.15.0 — operator-world state and external-send events.** The
same verify-before-asserting discipline covers orchestration's assertions
about the operator's *environment / session / self*, not only its
recommendations. Assert only checked state about the operator's world; when a
claim about login / app / version state or "what the operator is doing" is
unverified, hedge and check (a targeted probe or a version check) before
stating it — never narrate the operator's state as fact from inference.

- *Environment / session state.* "You need to log in" when already logged in;
  "you're current / sideloaded" when a newer version was published;
  "you're mid-review" fabricated from the model's own prior suggestion — each
  is an un-checked assertion about the operator's world. Hedge + check before
  asserting.
- *External-send / off-system events.* An external send or delivery is an
  operator action no working session observes, so canonical state can show it
  "pending" indefinitely. At closure / finalize, before recording such an
  event in canonical state, verify it *with the operator*
  (§{principle.SP-9} positive confirmation; never write an unverified event
  into canonical state, §{principle.SP-1}), then record it once confirmed —
  because no other session will.

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
- The cross-lane inbox (`OPEN_ITEMS.md`, §{section.cross-lane-inbox}) takes a
  fixed repo path per lane (object lane `OPEN_ITEMS.md`; meta lane
  `OPEN_ITEMS_meta.md`); a drained or declined item is retained, optionally
  archived to a `## Closed` section at engagement close.
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
  (`Fan: coverage (N)`) over *retrieved* facts buys recall, not falsification
  across distributions, so it is recorded as a retrieval-consistency note and
  never counted as a triangulation seat. (When the fanned loci *infer* over the
  material rather than read it back, their disagreements are
  triangulation-grade — the `inferred` side of the finding-basis axis,
  §{section.prompt-body-convergence-provisions}; see §{section.vendor-triangulation}.)
  The guardrail is structural — an investigation-posture
  Envelope lacks `Dispatch shape`, so Vendor Triangulation
  (§{section.vendor-triangulation}) cannot fire on a retrieval-only fan.

**Verify contested first-hand (the load-bearing anchor).** One discipline runs
through all four corollaries: a *contested* claim is settled by **first-hand
re-derivation against the evidence**, never by self-report, an agreement vote,
or a producer's say-so. A contested **inferred** finding is verified first-hand
before it enters the Master (§{section.prompt-body-convergence-provisions}); a
fanned validator's **catch** is adjudicated by re-derivation, not by how many
seats raised it (§{section.independent-validation-dispatch}); a substrate
**self-ID** that disagrees with the structural anchor is logged, not trusted
(§{principle.SP-21}). Triangulation integrity is what *surfaces* the contest;
first-hand verification is what *settles* it.

Cross-ref: §{section.vendor-triangulation},
§{section.claude-baseline-feasibility-with-named-limitation-escape-hatch},
§{section.orchestration-driver-and-persistence-axes},
§{section.corpus-access-dispatch}.

#### 10.1.7 SP-16 — The Elephant Rule `[methodological | stable | 🚫]`
<a id="section-sp-16-the-elephant-rule"></a>

New in v2.13.0; broadened to the uninvited-frame family in v2.14.0;
extended to the visual-polarity channel in v2.15.0.
Framing is a targeting decision, not a style choice (Lakoff: don't
think of an elephant). A sentence may invoke an adverse frame — by
denying it, defending against it, or conceding it — only when that
frame is **live**: a belief the reader demonstrably brings (a common
prior, a named risk, or an inference the document's own content
invites). Invoking anything else plants the frame it answers: the
reader leaves carrying it, the author reads as defensive, and the text
implies a critic nobody heard from.

**Test** — run on every member of the family:

1. Would a cold reader plausibly arrive holding Y, or derive Y from
   the document itself?
2. Yes → **called-for**. Keep; the contrast carries information.
   Record which live alternative it answers.
3. No → **uncalled-for**. Rewrite positively: assert what is true
   without referencing Y at all.

**SP-16(a) — Negations** ("not Y", "X, not Y", "rather than Y",
"no Y"). The shipped rule, with two refinements:

- *Self-bounding-verb fast path*: when the positive verb already
  bounds the claim ("shrink", "slow", "narrow", "delay"), a trailing
  denial of the unbounded case ("…they don't eliminate it") is
  uncalled-for by default — the verb did the bounding; the denial
  only plants the extreme.
- *Context can call the question*: inside a section whose explicit
  job is worst-case assessment, "how bad can it get?" is a called
  question — the document itself makes the extreme live. Section
  purpose is a legitimate source of liveness.

Called-for (keep) — examples:

- "The limit is export permission, not customer demand." (Both
  hypotheses are live; the contrast names the binding constraint.)
- "Maximum at full coverage (not current revenue)." (Prevents a real
  chart misread.)
- "~40 accounts is roughly one per country, not a near-monopoly."
  (Pre-empts arithmetic the reader will actually do.)

Uncalled-for (rewrite) — examples:

- "Why it's a real market, not a hyped one" → "What anchors the $2.0
  billion." (Nobody alleged hype; the heading now asserts the anchor.)
- "…lowers the figure to 45–60% of the total, rather than inflating
  it" → end the sentence at "of the total." ("Inflate" existed only
  to be denied.)
- "This is X — not the giant Z it's often confused with" → "This is X
  of its own — far narrower than Z." (Scoping kept, denial form
  dropped.)

**SP-16(b) — Defensive intensifiers** ("real", "actual", "genuine",
"truly", "clearly"). These defend rather than inform; they imply a
doubt nobody raised. When the sentence's evidence already proves the
property, the intensifier signals insecurity. Remedy: replace with an
informative qualifier, or delete.

- "public companies with real reported revenue" → "public companies
  with disclosed revenue." (Listing already guarantees realness;
  "disclosed" adds information.)

**SP-16(c) — Temporal hedges** ("for now", "today", "currently").
These concede an adverse trajectory the evidence may never have put
on the table. Same test: does the reader bring the adverse
expectation, or do the document's own numbers invite it? Where the
evidence supports stability, replace with the present-tense fact plus
its support ("— and they are not: the picture is stable, and the EU's
2025 plan actively supports demand").

**SP-16(d) — Visual polarity & render-integrity** (colour, badge, icon,
glyph). Framing is also carried visually — the reader's eye reads the colour
before the words. The same called-for / uncalled-for test runs on the visual
channel:

- *Visual polarity must match semantic polarity.* Colour, badge, and icon
  carry an adverse / neutral / favourable polarity. An adverse visual
  treatment (red, ⚠, "warning") on a favourable or neutral finding is an
  uninvited adverse frame — the visual-channel sibling of a prose negation —
  and is rewritten to neutral or matching polarity. The test is identical: is
  the frame this colour/badge plants one the reader brings, or one the
  artifact invents?
- *Render-integrity is a framing concern, not only a cosmetic one.* A
  CSS/templating regression that flips a glyph's intended polarity (a neutral
  ●◐○ coverage ball rendered red; a status pill losing its class) is a framing
  defect — the reader reads the broken polarity as meaning — so it belongs in
  the framing audit, not only the presentation-quality pass.
- *Requires a rendered artifact.* Unlike (a)–(c), this check reads a rendered
  artifact (PDF / screenshot), not source text, so it runs at deliverable
  validation — e.g. the Independent Validation Dispatch
  (§{section.independent-validation-dispatch}) — rather than in the per-Output
  Self-check.

**Application surfaces.**

- Every prose deliverable PRISM produces: Layer-2 synthesis, findings
  content inside Execution Outputs, Setup artifacts, *What's next*
  bodies. Headings, titles, and opening sentences get the strictest
  scrutiny — they set frames the rest of the document inherits.
- Execution-side operationalization: step 5 of the Execution
  Self-check (§{section.prism-execution-self-check}) — before emitting
  the Output, enumerate every negation, defensive intensifier, and
  temporal hedge; tag each called-for (naming the live alternative)
  or uncalled-for (rewrite before release).
- Audit-side: the Lens Library carries the same discipline as a
  document-review lens (LL-D-019 "Who said otherwise?", Pack 1) for
  reviewing existing documents.
- Visual channel: SP-16(d) extends the audit to colour / badge / icon
  polarity and render-integrity on rendered deliverables — caught at
  deliverable validation, not in the prose Self-check pass.

#### 10.1.8 SP-17 — Plain words first `[methodological | stable | ✅]`
<a id="section-sp-17-plain-words-first"></a>

New in v2.14.0. Prefer the plain word. Compression that costs
comprehension is a defect with the same standing as an arithmetic
defect — a reader who has to decode a phrase pays a tax the document
imposed for no return.

- "sellable-country discipline intact" → "the approved-country list
  stays tightly controlled."

Production-side rule for every prose deliverable PRISM produces. The
review-side check lives in the Lens Library's per-sentence clarity
audit (LL-D-020 "Help or ammunition?", Pack 1) and in the Independent
Validation Dispatch's readability axis
(§{section.independent-validation-dispatch}); SP-17 carries no
Self-check step.

#### 10.1.9 SP-18 — It must recompute `[methodological | stable | 🚫]`
<a id="section-sp-18-it-must-recompute"></a>

New in v2.14.0. Every stated relationship recomputes exactly from the
document's own content and cited sources. Three clauses:

- **SP-18(a) Arithmetic.** Every quantitative relationship recomputes
  from the document's own numbers. Silent rounding is a violation —
  "we use the midpoint" of 105 and 130 ≠ 115; reword to "just under
  the midpoint" or use 117.5.
- **SP-18(b) Structure.** Enumeration intros ("Three things drive…")
  track their lists through every edit; counts, parallel
  capitalization, and label styles in repeated structures verify as a
  set, never per-instance.
- **SP-18(c) Citation-claim congruence.** The sentence claims
  precisely what its source supports — same noun, same metric
  ("investment tripled" vs. the source's "number of investors
  tripled"; "revenue" vs. "ARR").

One test shape — re-derive, compare, zero silent drift — across three
target classes. Mechanical and machine-assistable; enforced at step 6
of the Execution Self-check (§{section.prism-execution-self-check}).

**Deliverable-transform tooling (new in v2.18.0).** When the recompute gate runs
over a deliverable *transform* (an HTML / Markdown → shipped-artifact build),
tokenize **standalone figures only**: exclude digits embedded in acronyms or codes
(`B2B2C`, `A8`, `GPT-5.5`) and strip tags first (so an `href` / anchor edit is not
read as figure drift) — otherwise a legitimate clarity edit trips a *false*
figure-drift halt. HTML→PDF render hazards for deliverable builds are catalogued in
§{appendix.vendor-parsing-observations}.

#### 10.1.10 SP-19 — Claims carry their basis `[methodological | stable | 🚫]`
<a id="section-sp-19-claims-carry-their-basis"></a>

New in v2.14.0. The reader sees what supports a claim at the point of
reading it. Three clauses:

- **SP-19(a) Hint, don't assert, under uncertainty.** Where a
  rationale is plausible but unconfirmed, place the facts so the
  reader can connect them; the document never states the rationale as
  its own claim. "The asymmetry of the range above leans the same
  way" — rather than "the ceiling is allowance for unobserved
  demand."
- **SP-19(b) Method-not-target front matter.** Cover and meta lines
  describe how a figure was built; a headline number leading the
  "build basis" reads as reverse-engineered from a target. The figure
  is stated where it is derived.
- **SP-19(c) Mixed-basis ratios labeled at point of use.** When
  numerator and denominator rest on different assumptions
  (conservative pricing ÷ target pricing), say so where the ratio
  appears — especially when the mixing is conservative, since stating
  it converts a vulnerability into credibility.

All three are positioning rules for the claim/basis relationship —
epistemic weight (a), derivation order (b), basis disclosure (c).
Judgment-class: enforced by the Independent Validation Dispatch
(§{section.independent-validation-dispatch}) and the Lens Library's
named-audience review (LL-D-020 "Help or ammunition?"), with no
Self-check step.

#### 10.1.11 SP-20 — Editions stand alone `[methodological | stable | 🚫]`
<a id="section-sp-20-editions-stand-alone"></a>

New in v2.14.0. When work forks into versions for the client to
choose between, each is fully self-contained: it carries everything
its reader needs and reads as the only document — the choice between
editions belongs to the presenter, invisibly. A cross-reference to a
sibling ("a longer version is available separately") hands the
audience a decision that was the presenter's to make.

**Vocabulary.** The framework term is **deliverable editions**.
"Variant" stays reserved for dispatch variants — the per-vendor
branches of a dispatched prompt and their rationale records
(§{section.rationale-discipline-per-dispatch-variant}). The two live
at different layers: editions face the client; dispatch variants face
the execution fleet.

Judgment-class: enforced by the Independent Validation Dispatch
(§{section.independent-validation-dispatch}), with no Self-check step.

#### 10.1.12 SP-21 — Trust structure, self-report advisory `[methodological | stable]`
<a id="section-sp-21-trust-structure-self-report-advisory"></a>

New in v2.15.0. Load-bearing mechanisms rest on **structure** (delimited
blocks), **operator-controlled handles** (the filename), and **copy-through
integrity** (the prompt digest) — never on a producer's self-description. A
producer's self-report (a substrate's self-ID, a self-reported date, an
agent's inferred assertion) is kept as an **advisory cross-check, never the
authority**. This is the *anchor* face of the epistemic root: trust is earned
by external check, not by self-assertion.

- **SP-21(a) Reconciliation precedence (the mechanizable corollary).** At
  §{section.recommended-vs-executed-reconciliation}: filename authoritative →
  self-ID advisory cross-check → a filename/self-ID mismatch is a logged
  **drift signal**, never an error or a halt. The disagreement itself *is* the
  vendor-drift detector.
- **SP-21(b) Extends to tool output.** Not only a vendor's self-ID but a
  tool's output — the orchestrator's own probe inference and an agent's
  exploration alike — can be confidently wrong. A contested claim is verified
  first-hand before it enters the Master, never accepted on the tool's own
  account of itself.

**Position.** Complements §{principle.SP-13} (which *obtains* the self-report
at session-open) and §{principle.SP-15} (triangulation integrity); SP-21 is
the **reconciliation-side** principle that says treat the self-report as
advisory. It generalizes the structural handle §{principle.SP-14} makes
canonical — the operator-set filename — into a trust posture at convergence.
It is the posture; the mechanics live in
§{section.recommended-vs-executed-reconciliation}.

#### 10.1.13 SP-22 — Surface translation `[methodological | stable | ✅]`
<a id="section-sp-22-surface-translation"></a>

New in v2.15.0. Nothing reaches a vendor, operator, or orchestration surface
without being re-rendered for that reader. Every boundary between surfaces is
a translation boundary: raw artifacts native to one surface — orchestration
machinery, framework codes, enforcement framings — are translated to the
target reader's frame, never passed through bare. This is a
communication/rendering discipline, a sibling axis to the epistemic
principles, not an epistemic check itself.

**Parent of three surface instances.** SP-22 states once what three existing
mechanics each enforce at one boundary:

- **Vendor surface** — atomic-prompt self-containment
  (§{section.atomic-prompt-self-containment}). PRISM-native shorthand
  (M-codes, SP-codes, claim IDs) carries competing priors in a vendor's
  training distribution and is inline-defined before it ships; the
  orchestration envelope is never pasted to the vendor as the execution unit.
- **Operator surface** — plain words first (§{principle.SP-17}). Framework
  codes are re-rendered into plain language before they reach the operator;
  ratification happens in the operator's frame, not in PRISM's.
- **Card surface** — the dispatch-card rendering rule (PRISM-UI layer): a card
  is rendered for reading, never handed over as copyable orchestration
  metadata, and seat counts are presented as recommended, never as an enforced
  cap.

The instances differ by reader; the discipline is one. Future surfaces inherit
it rather than re-deriving a per-surface rule. Judgment-class: no Self-check
step — the vendor-surface instance is enforced structurally at dispatch; the
operator- and card-surface instances are held as posture.

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
| SP-16 | The Elephant Rule (uninvited-frame discipline) | New in v2.13.0 | See §{section.sp-16-the-elephant-rule} |
| SP-17 | Plain words first | New in v2.14.0 | See §{section.sp-17-plain-words-first} |
| SP-18 | It must recompute | New in v2.14.0 | See §{section.sp-18-it-must-recompute} |
| SP-19 | Claims carry their basis | New in v2.14.0 | See §{section.sp-19-claims-carry-their-basis} |
| SP-20 | Editions stand alone | New in v2.14.0 | See §{section.sp-20-editions-stand-alone} |
| SP-21 | Trust structure, self-report advisory | New in v2.15.0 | See §{section.sp-21-trust-structure-self-report-advisory} |
| SP-22 | Surface translation | New in v2.15.0 | See §{section.sp-22-surface-translation} |

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
- **Read canonical, not a mirror (new in v2.18.0).** A convenience
  working-folder mirror lags the canonical repo *by construction* (a file
  committed to the repo is not auto-copied to a flat mirror). A consumer — a
  Builder, an Independent Validation seat, a fresh session — that reads the mirror
  instead of the canonical repo can see stale / incomplete state and infer a false
  defect. Read from a fresh repository clone, never the convenience mirror, with a
  completeness sanity-check on entry. The multi-surface engagement recipe is in
  §{appendix.external-share}.

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
| Cross-lane inbox | `OPEN_ITEMS.md` (object) · `OPEN_ITEMS_meta.md` (meta) | `OPEN_ITEMS.md` |
| Lane bootstrap / handoff | `[project]_[lane]_bootstrap.md` · `[project]_[lane]_handoff_[YYYY-MM-DD].md` | `alumnite_desk_bootstrap.md` |
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

**Accumulate, never overwrite (edit-scoped).** Every edit to a canonical
engagement artifact — Master *and* deliverables — produces a *new version*
under the bump rule above; it never overwrites a prior version in place.
Review-iteration rounds in particular accumulate versions (each round is a
sub-version bump, e.g. a report `_r6 → _r7`), so the version history is
recoverable and SP-1 canonicity (§{principle.SP-1}) is preserved. An in-place
overwrite of canonical state is a defect, not a convenience.

**Deliverable revisions: shipped == validated (new in v2.18.0).** Bump atomicity
governs the client-facing **deliverable**, not only the Master. Every content
change to a versioned deliverable — *including cosmetic and text corrections* —
bumps its revision (`_r7 → _r8`); a revision label that stays put while content
changes is a stale, lying label — the same look-alike failure §{principle.SP-14}
guards against, now on the artifact the client receives. The **shipped revision
must equal the validated revision**: a correction made *after* the Independent
Validation Dispatch (§{section.independent-validation-dispatch}) validated a
revision means validated ≠ shipped, so it requires a re-stamp + a decision —
re-validate if material, note if cosmetic — and never ships a
post-validation-corrected file under the validated label. Keep exactly one current
file per revision (remove superseded / un-versioned leftovers). The report-craft
home for this discipline is §{appendix.report-architecture}.

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
━━━ PRISM PROMPT INTEGRITY ━━━
[anchor per §3.2.5 — Dispatch ID + display-only digest + completeness rule;
 the literal first line of the paste, below the never-copy-able dispatch card]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━

━━━ PRISM EXECUTION ENVELOPE ━━━
[Execution seat paste — Envelope view, per E.1a (the §3.2.1 record minus the triangulation fields)]
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

━━━ END PRISM DISPATCHED PASTE — <Dispatch ID> ━━━
```

The first and last lines are the **transport-integrity bracket**
(§{section.transport-integrity-bracket}): the `PRISM PROMPT INTEGRITY` anchor
opens the paste and the `END PRISM DISPATCHED PASTE` sentinel closes it. They
frame the paste for safe transport — Self-check Step 0 confirms the sentinel is
present before any work — but are **not** contract blocks and are excluded from
the digest preimage.

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

## 14. Missing-handoff recovery (on-demand bundle) `[continuity]`

> The cold-open recovery flow (no handoff attached → locate the canonical
> Master, M2-verify, resume) is in **`reference/continuity.md`** — see the
> in-core recovery floor above (the continuity recovery stub). **Trigger:** a fresh
> session opened without a handoff. SP-4:
> `missing handoff → reference/continuity.md loaded ✓`.

## 18. Project, feedback, updates `[structural | stable]`
<a id="section-project-feedback-updates"></a>

PRISM is an open framework. This file ships with enough information to
locate the project, check for newer versions, and feed observations back
to the maintainer.

### 18.1 Project identity
<a id="section-project-identity"></a>

- **Repository.** `https://github.com/Ronkupper/PRISM`
- **Maintainer.** Ron Kuper ([@Ronkupper](https://github.com/Ronkupper))
- **Framework version.** v2.21.0 (this file)
- **Bundled Lens Library version.** v0.16 (`lens/PRISM_lens_library.md`)
- **Release date.** 2026-06-28
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
| Framework (this file) | `https://raw.githubusercontent.com/Ronkupper/PRISM/main/PRISM.md` | `…/PRISM_v2_21_0.md` |
| Lens Library | `https://raw.githubusercontent.com/Ronkupper/PRISM/main/lens/PRISM_lens_library.md` | `…/lens/PRISM_lens_library_v0_16.md` |
| Framework version stamp | `https://raw.githubusercontent.com/Ronkupper/PRISM/main/VERSION` | — |
| Lens version stamp | `https://raw.githubusercontent.com/Ronkupper/PRISM/main/lens/VERSION` | — |
| Releases index | `https://github.com/Ronkupper/PRISM/releases` | — |
| Release at this version | — | `https://github.com/Ronkupper/PRISM/releases/tag/v2.21.0` |

The two `VERSION` endpoints exist as cheap currency checks: each is a
single-line file containing the current version on the corresponding
release track. Reading them does not require parsing the framework or
the Lens body. New resources added to the project follow the same path
pattern (a stable file on `main`, a `VERSION` stamp where versioned).

### 18.3 Currency check at session open (on-demand bundle) `[maintenance phase]`

> **Phase bundle.** The session-open currency-check mechanics (version-stamp
> comparison against the published repo, soft-flag surfacing in *What's
> next*) are in **`reference/currency.md`**, fetched on demand. **Trigger:**
> the currency-check fires at session open (substrate with web access), or the
> operator runs an Update. SP-4: `currency.md loaded ✓`.

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
> (v2.21.0). https://github.com/Ronkupper/PRISM

---

*End of PRISM v2.21.0 framework operating document.*
