---
# Skill metadata (consumed by Claude.ai skill loader)
name: prism
description: "PRISM — structured multi-session, multi-vendor LLM-orchestrated audit and research framework. Currently v2.19.0. Trigger this skill whenever the user invokes PRISM mechanics by name or by recognizable construct: PRISM, PRISM audit, PRISM v2, begin a PRISM audit, Master file, any filename matching *_master_p*.md or *_starter_v*.md (v1.x), Prompt Strategy, Lens Library, Vendor Selection, Vendor Triangulation, Setup probes or any of P1-P7 by number, Monitor M* or any of M1-M12 by number, Standing Principle SP-*, Execution Envelope, Execution Self-check, Execution Output, Dispatch register, Dispatch shape (equivalence/split/limitation-named), the What is next artifact, context band or 🟢🟡🟠🔴, migration handoff, P0/P1 boundary, three-layer readiness, Claude Project recommendation, Update session, point refresh, Setup artifacts (Decision brief / Stakeholder register / Claim inventory / Jurisdiction map). Also trigger when the user attaches a Master file or a Lens Library file. Read this file in full at the start of any PRISM session before doing any work."

# Framework metadata (consumed by PRISM maintenance tooling)
version: 2.19.0
released: 2026-06-28
supersedes: 2.18.0
lens_library_embedded: "0.15"
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

# PRISM v2.19.0 — Framework operating document

**Status:** v2.19.0 release. Canonical framework for Claude orchestration sessions.
**Date:** June 2026
**Supersedes:** PRISM v2.17.0 (MINOR — "Lifecycle & deliverables": adds the symmetric **engagement closure** gate (§{section.engagement-closure}) — a three-layer close sweep bookending Setup's three-layer readiness (§{section.three-layer-readiness}), home of the orphan-sweep, the **reconcile-at-close** codification sweep, and the deliverable polish. Names the **comprehensive final report** as the engagement's deliverable of record plus the optional **interactive workbook** (§{section.decision-brief}), with the report architecture, the craft conventions, the workbook cockpit pattern, and the presentation house-style routed to a new **report-architecture** reference bundle (§{appendix.report-architecture}); extends bump atomicity to client-facing deliverables with the shipped-equals-validated invariant (§{section.bump-atomicity-routine}, §{section.independent-validation-dispatch}); adds the §{principle.SP-18} standalone-figure tokenization guard for deliverable transforms; lands the external-share family — one-repo-per-engagement, the de-coded share archive, operator-selectable share modes, and the image-redaction procedure — in a new **external-share** reference bundle (§{appendix.external-share}) with the read-the-repo-not-the-mirror tie on §{principle.SP-8}; and adds a multi-lane session-legibility operator guide. Additive; no construct renumbering.). PRISM v1.10.4 is terminal on the v1.x line (pinned per DD §{section.standing-principles-introduced-or-extended-in-v2}).
**Required attachments at every orchestration session:** this file (or the
PRISM v2 Skill that loads it) and the project's Master. This file embeds
Lens Library v0.15 in Appendix G; a singleton PRISM.md attachment is
sufficient for normal operation. Attach a standalone Lens Library only
when the project explicitly pins to a newer Library version than the
embedded copy (see §{section.library-reference-at-setup}).
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
The full tag index is Appendix C.

**Voice.** This is operating instruction for Claude in an orchestration session.
Imperative where Claude must act; declarative where defining shape; descriptive
where pointing. Section headers carry the operative scope.

---

## Quick reference — first-time reader

Reading order for first encounter:

1. **§{section.scope} Scope** (this section group) — what v2.19.0 is and what it isn't.
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

Reading order for an operator returning to v2.19.0 after running a session:
*What's next* → relevant §{section.architecture-mechanics}–§{section.library-integration} mechanics → §{section.monitor-specifications} Monitors if a fire surfaced.

---

## 1. Scope
<a id="section-scope"></a>

### 1.1 What v2.19.0 covers `[structural | stable]`
<a id="section-what-v2-8-0-covers"></a>

PRISM v2.19.0 is a structured multi-session, multi-vendor LLM-orchestrated audit
and research framework. v2.19.0 covers:

- **Two session types** (orchestration on Claude; execution on selected vendor per Vendor Selection)
  with explicit role separation (§{section.two-session-types}).
- **The triple contract** (Envelope inbound, Self-check, Output outbound) as
  the load-bearing interface between sessions (§{section.the-triple-contract}).
- **Master + *What's next* as continuous-state artifacts** written at every
  orchestration turn-close, regardless of band state (§{section.the-master}, §{section.whats-next}, §{section.failsafe-recovery-continuous-state-mechanics}).
- **Vendor Selection at dispatch** with live web-search currency check
  (§{section.vendor-selection-at-dispatch}).
- **Setup as iterative refinement** against the Lens Library v0.15, with
  three-layer readiness clearing the P0→P1 boundary (§{section.setup-mechanics}).
- **Seven Setup probes** (§{probe.P1} Coverage grading, P2 Adversarial Scope, P3
  Decision Framing, P4 Pre-mortem, P5 Falsifier, P6 Domain Reconnaissance,
  P7 User Voice) — Setup-time grading constructs only (§{section.the-seven-probes}).
- **Library integration** — the Lens Library v0.15 as canonical reference
  catalog (embedded as Appendix G; standalone at `lens/PRISM_lens_library.md`
  for explicit override); point-refresh in Setup; Update sessions for
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

### 1.2 What v2.19.0 does not cover
<a id="section-what-v2-8-0-does-not-cover"></a>

- **Re-debating direction.** v2.19.0 implements the spec; the spec implements
  the design document. Direction is settled. New direction goes through a
  fresh design cycle.
- **Standalone Library evolution.** The Lens Library catalog ships embedded
  in Appendix G (v0.15 at this release) for singleton-attachment use. The
  standalone file at `lens/PRISM_lens_library.md` (tag `prism-lens-v0.15`)
  remains authoritative for the Library's own evolution and for projects
  that explicitly pin to a newer Library version than the embedded copy.
- **Empirical calibration.** Several thresholds in v2.19.0 are rev. 1 draft
  estimates: M5 band thresholds (§{section.telemetric-framework-signal-weighting-and-compounding}), Update session trigger (§{section.currency-maintenance-update-session}),
  probe iteration ceilings (§{section.from-waterfall-to-library-graded-iterative-refinement}). Calibration against real use is a
  post-release item (§{section.empirical-calibration-items}).
- **Multi-vendor Self-check empirical footing.** Verified on Claude
  Opus-class and Sonnet-class models. Behavior on Gemini, ChatGPT, Perplexity
  is report-worthy (§{section.empirical-calibration-items}).
- **Non-Claude orchestration.** v2.19.0's machinery uses Claude-specific
  affordances (`present_files`, `create_file`, `str_replace`,
  `ask_user_input`, `conversation_search`, Skill packaging). Non-Claude
  orchestration is graceful-degradation, not a design target (DD.§3.1).

### 1.3 Three-leg constraint `[structural | stable]`
<a id="section-three-leg-constraint"></a>

v2.19.0 honours the constraint inherited from the design document (DD.§8.3):

- **Operator constraint.** Mobile-first; plain-chat substrate; manual
  artifact handling between sessions.
- **Substrate constraint.** Claude Opus-class (flagship tier) in orchestration; multi-
  vendor on the execution side.
- **Methodology constraint.** Structured audit-and-research with explicit
  scope-completeness and convergence discipline.

Mechanics that violate any leg do not earn their place in v2.19.0. Roadmap
adjacencies (DD.§9: automated cross-vendor orchestration, plugin-equipped
execution, multi-vendor skill ecosystems) live in reserved structural
surfaces — the `Tools:` slot and the reserved values on the
execution-configuration axes (§{section.orchestration-driver-and-persistence-axes}) —
but no machinery beyond the reservation.

---
## 2. System overview
<a id="section-system-overview"></a>

**Read this section first if you are encountering v2.19.0 mechanics for the
first time, and re-read it any time you need to locate a specific construct.**
This section is a map. Definitions live in the per-construct sections (§{section.architecture-mechanics}–§{section.missing-handoff-recovery}).

### 2.1 Construct list
<a id="section-construct-list"></a>

PRISM v2.19.0 has the following constructs, grouped by category.

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
- **What changed from v1.10.4** → Appendix D v1.x → v2 surface drift.
- **Decision rationale on something** → Appendix C tag index → Spec.§
  reference for chosen alternative + rationale.
- **A template to paste** → Appendix E template compendium.
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
  (`PRISM_lens_library.md` v0.15); the Prompt Strategy (when separate from
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
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Behavior contract.**

- Step 0 is the transport-integrity input-gate
  (§{section.transport-integrity-bracket}): the completeness-of-INPUT halt the
  dispatch conventions sanction (§{appendix.dispatch-conventions}, J.2 — INPUT
  is the only place the vendor may halt). It restates the top-of-paste anchor,
  which is the truncation-surviving copy and governs on disagreement; absent or
  mismatched, it halts with a one-line truncation report as the deliverable,
  mirroring the mismatch-halts-task contract of steps 1–4.
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
  is a violation. Judgment-class principles (§{principle.SP-17},
  §{principle.SP-19}, §{principle.SP-20}) enforce via the Independent
  Validation Dispatch (§{section.independent-validation-dispatch}) and
  the Lens Library, with no Self-check step.

**Multi-vendor empirical footing.** Verified on Claude Opus-class and
Sonnet-class models. Gemini, ChatGPT, Perplexity behavior under this
block is **report-worthy finding** per DD.§3.5 — operators report
divergences. See §{section.empirical-calibration-items}. Step 0's
pre-task STOP is a stronger instruction-following demand than self-ID, so
non-Claude adherence to the transport-integrity halt is itself a report-worthy
calibration item — and a vendor that ignores Step 0 is no worse off than before
the gate existed.

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

#### 3.5.2 Cowork surface capabilities
<a id="section-cowork-surface-capabilities"></a>

Under `orchestration_surface: cowork`, Computer Use and the Chrome MCP (the
Claude Chrome Extension) are exposed as a substrate. Its uses are
deliberately an **open set** — documented as a capability surface rather
than a fixed enum, so a new use does not force a schema change. The
closed-enum discipline governs axis *values*; this capability surface is
intentionally open. Known uses today:

- **Auto-drive execution** — drive other vendors' execution apps (the
  Axis-2 `auto_drive` value).
- **App-under-test** — when the work's scope includes auditing a web (or
  other) application, Computer Use / Chrome MCP operate the target itself.
  This is the audit *subject*, distinct from driving execution.
- **Isolated-context execution of the Claude seat** — in a cross-vendor
  equivalence run, the Claude seat can execute in a Cowork sub-agent with
  its own context window rather than inline. This shifts only the
  context-isolation axis, not epistemic posture — triangulation asymmetry
  stays carried by the vendor set — so it is SP-15-clean
  (§{section.sp-15-triangulation-integrity}). It depends on atomic-prompt
  self-containment (§{section.atomic-prompt-self-containment}): a
  fresh-context sub-agent carries none of the orchestrator's assumptions,
  so bare shorthand misreads exactly as it would across vendors.
- **Subagent investigation** — bounded investigation work
  (candidate-credibility checks, single-source extraction, methodology
  lookups, pre-dispatch scoping). Investigation posture only, never a
  triangulation substitute.
- **Future uses** — any later capability that benefits from or depends on
  these primitives lands here without a schema change.

Every sub-agent use lands on the context-isolation axis, never the
epistemic-posture axis — consistent with SP-15
(§{section.sp-15-triangulation-integrity}).

**Posture, now a first-class Envelope field.** The investigation-vs-epistemic
distinction described in this surface as prose is, as of the corpus-access
capability, carried structurally as the Envelope's `Posture:` field
(§{section.prism-execution-envelope}, the Execution Envelope). Corpus-access
(§{section.corpus-access-dispatch}, the external-reference-corpus lookup) is the
first investigation use to earn its own first-class Envelope, which is what forced
the distinction up from prose into the schema. Its `cowork-mcp` lookup path —
PRISM driving the Chrome MCP to operate a source directly, including the
operator's authenticated session — lands in this open capability set (Phase 3,
reserved) and is App-under-test-shaped, not the `auto_drive` per-vendor
machinery.

#### 3.5.3 `repo_backed` mechanics
<a id="section-repo-backed-mechanics"></a>

`persistence: repo_backed` makes a GitHub repo the durable home for an
engagement's state. It earns its place even on a single surface: in a plain
`single_chat` or `projects` session, the repo is where the Master
(§{section.the-master}) and *What's next* (§{section.whats-next}) survive
across chats that would otherwise lose them to scrollback. The cross-surface
payoff — switching between, say, a Cowork session and a mobile Project and
having each pick up exactly where the last left off — is an *additional*
benefit repo-residence unlocks, not the baseline justification. The axis is
orthogonal to the orchestration surface by construction
(§{section.orchestration-driver-and-persistence-axes}).

**Setup flow.** When `repo_backed` is selected at Setup, orchestration:

1. **Asks the operator for a repo and a scoped PAT.** A GitHub repository (new
   or existing) to hold the engagement, and a Personal Access Token the
   orchestration session uses to read and write it. PAT hygiene is
   operator-side and is spelled out below — this is the operator's own
   credential for their own repo, distinct from any maintainer credential.
2. **Creates a work folder** for this engagement in the repo (e.g.
   `prism/<engagement-slug>/`) — the canonical home for every artifact the
   engagement produces.
3. **Writes an engagement SI file** into that folder codifying the repo
   workflow (skeleton below), so any session that loads it operates the
   engagement identically regardless of surface.
4. **Asks the operator to configure that SI in a Project** — one per surface
   the operator intends to use (e.g. a desktop Cowork Project and a mobile
   Project both pointing at the same repo).
5. **Saves the engagement's whole state to the repo** — everything the work
   touches, inputs in and outputs out. The set is illustrative, not closed:
   operator-supplied **Inputs** (the subject brief and any reference material),
   the Master, Envelopes, handoffs, execution Outputs, and the *What's next*
   artifact, which becomes **repo-resident** (§{section.whats-next}): same
   artifact, same per-turn-close lifecycle, written to a fixed path in the work
   folder rather than living only in chat.
6. **Lets the operator switch surfaces freely.** Each surface reads the
   repo-resident *What's next* on resume and continues from it. The repo is
   the shared state; the surface is interchangeable.

**Committer model.** The orchestration session commits artifacts directly
using the operator-supplied PAT — the operator delegates the GitHub mechanics
the same way *What's next* spares them from scrolling chat. An operator who
prefers not to place a PAT in a Project can instead run
**operator-as-committer**: orchestration produces each artifact as a file and
the operator commits it by hand. This is the conservative fallback; it
reintroduces the manual round-trip `repo_backed` exists to remove, so it is
not the default.

**Operator inputs.** Anything the operator supplies to the engagement — the
subject brief, reference documents, spreadsheets, decks, and information given
in a chat prompt — is captured to the work folder, at Setup or any time after.
Information pasted into chat is written to a file rather than left in
scrollback; otherwise it is exactly the cross-surface state a different surface
could not pick up, which is the loss `repo_backed` exists to prevent.

**Execution returns.** Execution Outputs — the reports a vendor produces from a
dispatched Envelope, in whatever form they come back (Markdown, a Word or PDF
document, pasted text) — persist the same way as every other artifact. Under
the manual execution driver (§{section.orchestration-driver-and-persistence-axes},
the only built driver), the operator attaches the returned Output to the
orchestration session as it already does in the normal lifecycle, and
orchestration commits it to the work folder; this works today under the
Claude-as-committer model with no extra machinery. A future git-enabled
execution session that commits its own returns directly is a possible later
direction — lower priority, not built — the persistence-side parallel to the
reserved `auto_drive` execution driver. Either way the returns land in the same
work folder as the operator's Inputs, the Master, Envelopes, handoffs, and
*What's next*.

**Operator PAT hygiene.** The PAT is the operator's credential for the
operator's repo. The discipline below mirrors token handling PRISM's own
maintenance has used reliably; it is guidance for the operator's setup, not a
prescription of any particular maintainer flow:

- **Minimum scope.** A fine-grained PAT scoped to the single engagement repo
  only (never account-wide), granting Contents read/write and Metadata read —
  nothing further unless the engagement specifically needs it.
- **Storage.** Held in the Project's credential surface (its files), never
  pasted into chat, never committed to the repo, never echoed into an
  artifact. Treat it as a password.
- **Injection and strip.** When the session pushes, the PAT is embedded in the
  remote URL for the push only and stripped from the remote immediately after.
  It is never written to a tracked file.
- **Rotation.** Give the token an expiry (90 days is a reasonable default),
  track that date, and regenerate before it lapses. Avoid no-expiry tokens.

**Engagement SI skeleton.** The file written in step 3 is the per-engagement
operating document. Its sections:

1. **Purpose & repo model** — what this engagement is; the repo; the
   work-folder path.
2. **Source of truth** — the repo is canonical; the repo-resident *What's
   next* is the single state pointer.
3. **Surface registry** — which surfaces are configured and any per-surface
   setup notes. A single entry in the baseline single-surface case; one row
   per surface when the operator runs more than one.
4. **Persistence workflow** — fetch-on-resume, write-on-turn-close; the
   *What's next* read/write path and protocol; artifact placement rules within
   the work folder.
5. **PAT & credential hygiene** — the operator-side rules above.
6. **Commit discipline** — commit author and message conventions; signing
   left to the operator (their repo); the committer model in force.
7. **Redaction note** *(conditional)* — heavier if the operator's repo is
   public, lighter if private.
8. **Resume protocol** — the literal session-start instruction: fetch *What's
   next* from its path, read it, proceed.

The value and contract for `repo_backed` are fixed in
§{section.orchestration-driver-and-persistence-axes}; this subsection is the
mechanics that realize them. The triple contract
(§{section.the-triple-contract}) is untouched: `repo_backed` changes only
where durable state lives, never how the Envelope/Self-check/Output interface
works.

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
Strip every orchestration-side field from the paste — `Vendor:` /
`Vendor list:` / `Dispatch shape:` (`equivalence` / `split` / `limitation-
named`) / dispatch rationale. The arm-count and the triangulation are
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
Dispatch ID:      [unique per dispatch instance; copy verbatim]
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
vendor actually has, and the rationale names the fallback. Because the
corpus-access paste is itself a dispatched paste carrying a Dispatch ID and
digest, it is wrapped by the same transport-integrity bracket
(§{section.transport-integrity-bracket}); the executing locus runs Self-check
Step 0 before the lookup.

**Coverage fan.** Fanning a lookup across N vendors looks like equivalence
dispatch, but posture decides routing, not vendor count. In a coverage fan the N
vendors each *retrieve* the same material — different web-search indexes surface
different sources — so for *retrieved* facts multiplicity buys **recall**, not
judgment. Agreement across the fan is a **retrieval-consistency** signal ("this
fact is robustly findable") recorded as a note, never promoted to convergence.
The marker is `Fan: coverage (N)`, structurally distinct from
`Dispatch shape: equivalence`, so Vendor Triangulation cannot fire on a
retrieval-only fan (§{section.vendor-triangulation}, Vendor Triangulation). (A
fan whose loci *infer* over the material is the different case — its
disagreements are triangulation-grade, the `inferred` side of the finding-basis
axis, §{section.prompt-body-convergence-provisions}.) If the engagement then wants multi-vendor *judgment on* the
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
that embeds the Lens Library as Appendix G) — is, by virtue of that field,
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

**Passive pre-fill of self-report.** When a pass depends on a subject's
*self-report* — a founder questionnaire, a management interview, a data-room
claim set — and especially when it is gated on a person returning, pre-fill
what is externally knowable *before* the self-report arrives. Run passive
external detection (the Chrome-MCP / authenticated-browse surface,
§{section.cowork-surface-capabilities}, plus public records — DNS,
certificate-transparency, IP-WHOIS, app-store listings) and pre-answer the
items observation can reach. This turns gate-blocked waiting into
subject-independent, de-risking progress, and one detection pass feeds many.
It is a **browse/retrieval** job: name the browse capability per the
retrieval-shape step (§{section.vendor-selection-at-dispatch}); do **not**
route it to a synthesis/Deep-Research mode, which silently fails to fetch. Tag
every pre-filled item by provenance — `[OBS]` observed first-hand, `[INF]`
inferred from observed signals, `[ask]` not passively knowable
(§{section.prompt-body-convergence-provisions}, the finding-basis axis). The
self-report is then **triangulated against this independent baseline** when it
arrives (the external check pre-positioned over the claim — §{principle.SP-21};
the detection is investigation-posture single-source, §{principle.SP-15}, never
a triangulation seat). **Passive-only by default** on a trust-relationship
subject: honor the questionnaire's own promise — no scanning, no
ID/parameter manipulation (IDOR), no auth-bypass / rate-limit / upload /
state-changing actions; read key *names*, never token *values*. Active tests
require explicit operator authorization and are marked `[not tested — out of
passive scope → ask or authorized test]`. The paste-ready detection template
and per-vendor browse recipes are in §{appendix.vendor-parsing-observations}
(vendor parsing observations).

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
ammunition?", and LL-D-021 "Does a stranger follow?" from the Lens
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

### 5.4 Migration handoff `[structural | stable]`
<a id="section-migration-handoff"></a>

Defined handoff artifact. Produced by orchestration at 🔴 (mandatory) and
offered at 🟠 (operator-elective).

**Handoff format.**

```
━━━ PRISM SESSION HANDOFF ━━━
Project:                [name]
Master version:         [filename of attached Master]
Lens Library version:   [v0.15 | filename pinned]
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

- **Inbox drain at every orchestration turn-close (repo_backed lanes).**
  The lane owner reads its `OPEN_ITEMS` inbox alongside *What's next*, folds
  each non-terminal item into the Strategy / next-action / register, and
  appends a `drained` disposition line (§{section.cross-lane-inbox}). The drain
  is a turn-close peer of the Master and *What's next* writes, and part of
  resume. An un-drained inbox at turn-close is a turn-close self-check surfaced
  on the resume line and via SP-4 emission — not a separate Monitor (it does
  not warrant a numbered slot).

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

Every planned prompt has a complete pass **spec** — **not** a frozen Envelope.
The Envelope is *rendered just-in-time at dispatch* (the dispatch lifecycle's
Build stage, §{section.dispatch-lifecycle}); requiring a populated Envelope here
would force a Setup-time render to be replayed stale on a long engagement, the
opposite of late binding. The spec is the durable, Setup-graded,
convergence-revisable (§{section.strategy-stability}) contract; it carries:

- Single objective (one-sentence statement).
- Output format (structured findings per §{section.prompt-body-convergence-provisions}).
- Dependency list (which prior prompts' outputs are inputs; can be empty).
- Attachment map (filenames per attachment).
- Enrichment decision (single-vendor / equivalence / split /
  limitation-named).
- Success criteria + the applicable conventions and lenses — what "done" means
  and what binds. This is the **anchor** the just-in-time Envelope render must
  preserve (objective + lens-coverage + success-criteria), so a late-bound
  rebuild refreshes the *rendering* without re-scoping the Setup grading.

Verification: orchestration walks the strategy and confirms each prompt has a
complete spec across these six fields. Any missing field halts P0 → P1. The
Envelope itself is not required to clear this gate — it is built at dispatch
from the live Master and current conventions (§{section.prism-execution-envelope}),
anchored to this spec, with the decisive caveats carried forward explicitly so
the fresh Dispatch-builder loses nothing the Desk knew.

#### Layer 2 — Library coverage saturation

Every applicable Lens from the Lens Library v0.15 is either:

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

Grade the draft strategy against the Lens Library v0.15. Universal lenses
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

**Operator-positioning question (new in v2.15.0).** Who commissioned this and
why? What is their relationship to the subject and to the decision? What angle
or conflict does that create, and how should the brief be framed to be true to
it? Answer positively (§{principle.SP-16}) — state what each stakeholder *is*
and the conflict it creates, never a denial of what they are not. Every
stakeholder *and the operator/commissioner* is captured with role, motivation,
and positioning/angle.

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

**Commissioner positioning is an explicit premise (new in v2.15.0).** The
verified operator/commissioner positioning — role, motivation, and
angle/conflict relative to the subject and the decision — is recorded as a
Decision-brief premise, stated positively (§{principle.SP-16}). M6
(§{monitor.M6}) then guards the right premise: a finding that contradicts the
pinned positioning fires M6 correctly, but the frame is correct from P0, so M6
is a backstop, not the primary catch.

```
## Decision brief

Subject:           [name]
Decision under test: [one sentence]
Decision-maker:    [name or role]
Commissioner positioning: [operator/commissioner role, motivation, angle/conflict — stated positively]
Deadline:          [date or trigger]
Cost of error:    
  - False positive: [cost]
  - False negative: [cost]
Stakes / blast radius: [one paragraph]
Falsifiers:        [list — findings that would refute the thesis]
```

**Quantitative core → an interactive workbook (new in v2.18.0).** When the
decision under test has a quantitative, operator-tunable core (unit economics, a
threshold / corner case, a returns or break-even model), the finding may be
delivered **also** as a live operator-drivable **workbook** — editable assumption
cells driving the brief's decision gate in real time, color-coded — so the
decision-maker explores the verdict against their own numbers. The report
*states* the finding; the workbook lets them *drive* it. Trigger (one per
engagement, on the central quantitative gate) and the cockpit pattern
(editable-cells-only + live gate + opens-at-the-report's-case + §{principle.SP-18}
tie-back) are in §{appendix.report-architecture}.

#### 6.4.2 Stakeholder register
<a id="section-stakeholder-register"></a>

Populated by Probe 3 primarily. Every stakeholder is pinned, and the
**operator/commissioner is a mandatory row — never omitted** (they hold a
stake, a motivation, and an angle that shapes the brief). Motivation and
Positioning/angle are mandatory for the decision-maker and the operator, and
stated positively (§{principle.SP-16}) — what the stakeholder *is* and the
conflict it creates, never a denial of what they are not.

```
## Stakeholder register

| Role | Stake | Motivation | Positioning/angle | Decision power | Communication channel |
|---|---|---|---|---|---|
| [operator/commissioner] | [decision/outcome stake] | [why they want this engagement / this outcome] | [advisor / investor / competitor / partner / regulator / arms-length / advocacy; + any conflict] | [yes/advisory/none] | [channel] |
| [name] | [decision/outcome stake] | [motivation] | [positioning/angle; + any conflict] | [yes/advisory/none] | [channel] |
| ... | ... | ... | ... | ... | ... |
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

**Strategy revisions** trigger from two sources. *Convergence-time
revisions* trigger when Layer-1 convergence produces:

- A premise invalidation (§{monitor.M6} Premise Shift fires HIGH).
- A newly-surfaced domain area (e.g., a regulatory regime not in the
  Jurisdiction map).
- A falsifier hit (one of the Decision brief's Falsifiers is observed).
- An assumption conflict between two findings (§{monitor.M7}).

*Operator-initiated revisions* trigger independently of convergence:

- **Operator-initiated scope expansion** — the operator adds new prompts or a
  new pass to the strategy (e.g., extending coverage to an additional subject
  area or comparison set), with no premise break, conflict, or falsifier in
  play. It reuses the same draft → ratify → version-bump spine below; the
  revision mechanic does not require a convergence event to fire.

**Follow-up vs M10 re-run.** A *Follow-up* and an §{monitor.M10} re-run
(§{section.m10-rerun-fix-required}) are different operations and must not be
conflated:

- **M10 re-run** — the prior run was *defective or incomplete*; redo that same
  dispatch with corrections. Logged in the Rerun Register
  (§{section.m10-rerun-fix-required}).
- **Follow-up** — the prior run was *sound*, but a new or expanded dimension is
  now wanted. Do **not** augment-and-re-run the completed producer; route the
  scope-addition to the next consuming pass (the natural carrier) or a new
  dedicated pass, as an operator-initiated revision above. The strategy
  progresses additively per results.

Verify live engagement state before advising on either (§{principle.SP-10},
verify-before-recommend, applied to engagement state — not only vendor
currency).

**Revision mechanic** (lighter than v1.x major-bump Adaptation).

1. A revision trigger fires — a convergence-time trigger (above: a premise
   invalidation or assumption conflict via §{monitor.M6} / M7 HIGH, a falsifier
   hit, or a newly-surfaced domain area), or an operator-initiated scope
   expansion.
2. Orchestration drafts a revision: adds/modifies prompts, updates attach
   maps, updates Setup artifacts as needed.
3. Operator ratifies (per Layer 3 §{section.three-layer-readiness}).
4. Master version increments (sub-version bump within phase, e.g., P2.2
   → P2.3).
5. Strategy continues with revised state.

**Attach map travels with each prompt.** When a prompt adapts, its attach
map adapts with it (§{section.prism-execution-envelope}).

**Setup-artifact re-audit (new in v2.15.0).** A Setup premise that is
*mis-scoped at the root* — wrong actor, wrong decision-maker, wrong audience,
wrong frame — and that no returned finding happens to contradict is invisible
to §{monitor.M6} and to every other monitor: nothing re-questions the Setup
artifacts against accumulating reality. Re-audit them proactively at the
P0 → P1 boundary and again before the report is assembled: re-pose the Decision
brief's and Stakeholder register's actor / decision-maker / commissioner
positioning / audience / frame as a falsifier against the evidence gathered
since Setup ("is the named decision-maker still right? whose decision is this
actually? is the commissioner positioning still true?"). A mis-scope found here
is corrected via the revision mechanic above, restated positively
(§{principle.SP-16}) — correct the actor/frame, never plant a denial. This is
the premise-side complement to the P5 falsifier
(§{section.probe-5-falsifier-once}, which tests the *thesis*); M6 stays the
finding-driven backstop.

### 6.6 Setup onboarding and mode selection `[structural | stable]`
<a id="section-setup-onboarding-and-mode-selection"></a>

Setup is the workspace **scaffolder**: the operator should run the system
without learning lanes and roles (§{section.lanes-roles-and-the-prism-ui}).
Two completions of that scaffolding role land here — the onboarding flow
(which generates the engagement's SI and stands up its project(s)) and the
mode offer (full engagement vs quick brief). Reference-grade detail — the SI
template, the project-create / install cards, and the quick-mode procedure —
is in Appendix I (§{appendix.lanes-roles-prism-ui}); this section is the rule.

**Mode offer (first thing Setup does).** Setup offers **full engagement vs
quick brief** at the very top. The mode is **operator-selected**, not
auto-detected — auto-detection risks mis-classifying a real engagement as a
brief.

#### Full-engagement onboarding (Setup-as-scaffolder)

For a full engagement, Setup runs once at engagement creation: **gather →
generate → ratify → commit → emit cards.**

1. **Gather** the per-subject config — mostly already collected by the probes
   that build the Decision brief and Stakeholder register
   (§{section.setup-artifacts}): subject +
   decision tracks; repo + work folder (the `repo_backed` locus); the surface
   registry; credential location + redaction regime; any engagement-specific
   standing directives.
2. **Generate the SI draft** by instantiating the framework **SI template** —
   framework-native sections collapse to one-line references (persistence,
   resume, commit-discipline, the cross-lane inbox, lanes / roles per the
   framework); per-subject sections are filled from the gathered config.
   Engagement-specific standing directives are **embedded verbatim** (memory
   does not cross projects; the SI is the only cross-project carrier).
3. **Operator ratification — a hard gate (SP-9, §{principle.SP-9}).** Setup
   presents the draft SI to ratify or edit before install: **auto-draft, not
   auto-install** — generated so the operator never hand-writes boilerplate,
   ratified so a bespoke SI is still possible. Silence is not ratification.
4. **Commit the SI to the repo** as the canonical copy from day one (the
   resume-time reconcile then catches later drift).
5. **Emit the project-create + install card(s)** — one per surface, in the
   "open a session, paste this" family, naming WHERE / WHAT / RESULT in plain
   language. The SI installs as a **full wholesale paste, never a splice**
   (manual splice-edits are risky; re-issue on change is always a full
   replacement). The PAT is **guidance-only** — placed by the operator, never
   handled by the session.

**Two-project model (on Cowork).** A full engagement runs as **two
projects**: an **orchestration project** (the SI installed, core-load
enforced; it hosts the standing PRISM Desk and PRISM Meta lanes) and an
**execution project** (**SI-less, memory off, organization-only**) so the
ephemeral, PRISM-unaware vendor-execution runs have a home and their returns
land somewhere. Memory-off and a working folder kept separate from the
orchestration mirror are **recommended, not merely allowed** — they preserve
the execution run's clean-context independence (the
§{section.independent-validation-dispatch} premise: a shared SI or memory would
let run N inherit run N-1's framing). This graduates the
Claude-Project-at-Setup recommendation
(§{section.claude-project-as-setup-recommendation}) to active. The SI's
repo-canonical sync and opener machinery are framework-native from here, not
engagement-local interim.

#### Quick mode (`SETUP_QUICKMODE`)

A first-class **proportionality** option — the light end of the lean-Master
principle — for a task that wants *some* rigor but not the full apparatus (a
meeting brief, a quick analysis). Without it, the activation cost is paid in
full or the rigor is skipped entirely.

**Shape:** one Cowork session, `ephemeral` persistence, with **clean-context
sub-agent fan-out** for the work (one sub-agent per research / extraction /
drafting strand, returning only grounding facts;
§{section.lanes-roles-and-the-prism-ui}).

**Dropped (the heavy machinery):** `repo_backed` persistence; Master
accumulation and bump atomicity; multi-vendor equivalence dispatch and Vendor
Triangulation; multi-session handoff; the full seven-probe Setup and
three-layer readiness.

**Kept (the cheap, load-bearing rigor):** a **mini decision-brief** (two
lines — the audience and the decision it serves); a **lite Probe-1** (name the
handful of lenses that actually bear, plus any deliberately out of scope; no
coverage-saturation loop); and the **output-discipline gates on the
deliverable** — SP-16 (§{principle.SP-16}), SP-17 (§{principle.SP-17}), SP-18
(§{principle.SP-18}) — which are exactly the part that protects a brief from
being confidently wrong or mis-framed. The deliverable is self-contained
(SP-20, §{principle.SP-20}).

**Sub-agents need no envelope.** The triple contract exists for cross-vendor /
cross-session boundaries that quick mode does not cross; fan-out delegation is
free-form internal.

**Graduation (the load-bearing line).** When a quick brief turns out to be a
real engagement, it is promoted **without losing work**: the quick-mode output
**seeds a `repo_backed` Master** — the mini decision-brief becomes the Decision
brief, the lite lens pick seeds the Prompt Strategy, and the deliverable
becomes the first finding — and full Setup continues from there.

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

The Lens Library v0.15 is canonical at `lens/PRISM_lens_library.md`
(tag `prism-lens-v0.15`). The v0.15 catalog is also embedded in this
file as **Appendix G** for singleton-attachment use; that embedded copy
is the default Library source for orchestration. The standalone Library
file remains authoritative for the artifact's own evolution: Update
sessions (§{section.currency-maintenance-update-session}) produce new versions of the standalone file, and the
next PRISM minor version embeds the new content into Appendix G.
Operators on a newer standalone Library version pin to it explicitly
and override Appendix G (§{section.library-reference-at-setup}).

### 7.1 Library reference at Setup `[structural | stable]`
<a id="section-library-reference-at-setup"></a>

**Required Library source.** By default, orchestration uses the embedded
Lens Library v0.15 in Appendix G (this file). A standalone Lens Library
file (`lens/PRISM_lens_library.md`, tag `prism-lens-v0.15` or newer) is
attached only when the operator explicitly pins the project to a newer
standalone Library version than the embedded copy. When standalone is
attached, it overrides Appendix G for that session. Recommended: if a
standalone newer Library is used, live in the Claude Project alongside
the Master (see §{section.claude-project-as-setup-recommendation}).

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
          via web search; PRISM Lens Library v0.15 last_verified
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

## 8. Parked v2 design ideas
<a id="section-parked-v2-design-ideas"></a>

These two ideas were parked for v2 from the design-doc-level discussion
(DD.§13.3): they earn their place but the framework treats them as
recommendations and graceful-degradation paths rather than hard machinery.

### 8.1 Claude Project as Setup recommendation `[vendor-dependent | review-if: orchestration vendor changes]`
<a id="section-claude-project-as-setup-recommendation"></a>

Setup at P0.1 includes a recommendation to create a Claude Project as the
home for project state.

**Graduated under SETUP_ONBOARDING (v2.16.0).** This recommendation is now
active rather than parked: an engagement runs as the two-project model
(orchestration + execution) that Setup onboarding stands up — see
§{section.setup-onboarding-and-mode-selection}.

**Recommendation surfacing — when.**

- At P0.1, before the first probe iteration runs.
- *What's next* surfaces it as the first operator action:
  ```
  Setup recommendation: Create a Claude Project named "[subject] audit"
  (or per your naming convention). Reasons:
    - Project knowledge auto-attaches Master, Lens Library, and brief
      documents to every session you open inside the Project.
    - Past-conversation search becomes bounded to the Project, which
      pairs cleanly with SP-12 bounded-search disclosure.
    - Reduces re-attach friction across multi-session work.
  Proceed without a Project? [yes/no]
  ```

**Project contents at Setup completion** (recommended):

- `[project]_prism2.0_master_p0.1.md` (Master, current version)
- `PRISM_lens_library.md` (v0.15 or pinned tag)
- `[project]_brief.md` (subject brief)
- `[project]_prompt_strategy_p0.1.md` (current Prompt Strategy, optional —
  Master can carry this)
- Any subject-supplied reference documents

**Master in the Project** — operator workflow:

- Each orchestration session updates the Master.
- At session close, operator downloads the updated Master to the device.
- Operator uploads the new version to project knowledge (replacing or
  adding).
- Old version retained in project knowledge as audit trail (or archived to
  cloud drive per §{section.mobile-operator-survival-guide} MO-5).

This is a manual sync step under v2.0's plain-chat substrate. Auto-sync is
a roadmap adjacency.

**Fallback (operator declines or cannot create a Project).**

- Setup proceeds. P0.1 continues without Project.
- Every subsequent *What's next* emits an Operator hint: `Re-attach Master
  and Lens Library at session open.`
- The Project recommendation does not re-surface unless operator asks;
  framework respects the decline.

**SP-12 bounded-search disclosure interaction.** When a Project is in
place, Claude's `conversation_search` is bounded to the Project. SP-12
disclosure language adjusts:

> *"Searched within the [project name] Project. [Result]. The session may
> live outside this Project; confirm before I conclude."*

When no Project is in place, search covers non-project conversations.
SP-12 disclosure language:

> *"Searched outside any Project's scope. [Result]. The session may live
> inside a Project I cannot see from here; confirm before I conclude."*

### 8.2 Session history as validation/recovery `[vendor-dependent | review-if: orchestration vendor changes]`
<a id="section-session-history-as-validation-recovery"></a>

Session history (Claude's `conversation_search`) is consulted when state is
unexpected, ambiguous, or out-of-order. Results are advisory; SP-1 governs
canonicity.

**Triggers** (Monitors that consult session history):

- **M2 fires** (Version Drift) — Master version doesn't match expected.
  Consult session history for the last session that saved the expected
  version.
- **M3 fires** (Sequence Violation) — operator declared a step out of
  order. Consult session history for the canonical sequence in this
  project.
- **Master / *What's next* mismatch** — attached Master's version differs
  from what *What's next* predicted at last close. Consult session history
  for the closing turn that produced the mismatch.
- **Strategy-finding mismatch** — a finding references a prompt not in the
  Prompt Strategy. Consult session history for when the prompt was added
  or removed.
- **Attach-conversation disagreement** — attach map and conversation
  disagree about which file is canonical. Consult session history for the
  last canonical statement.

**Query construction.** Orchestration's `conversation_search` query is
derived from the ambiguity. Examples:

- M2: `"[Master version expected]" "[project name]"`
- M3: `"[prompt ID]" "[project name]"`
- Strategy-finding mismatch: `"[finding text]" "[project name]"`

Query length: 3–6 words distinctive content. No long passages.

**Results handling — advisory not authoritative.**

1. Orchestration reports what session history found:
   ```
   Session history check (per [Monitor or trigger]):
   Searched: "[query]"
   Scope: within [Project name | non-project conversations]
   Found: [N matches]
     - [session URL or descriptor] — [snippet]
     - ...
   ```
2. Orchestration does *not* silently update Master from session-history
   evidence. Per §{principle.SP-1}: canonical artifacts are not regenerated without
   operator confirmation.
3. Orchestration surfaces a recommendation: "Session history suggests
   [interpretation]. Update Master to reflect? [yes/no/clarify]"
4. Operator confirms; orchestration updates Master.

**Reconciliation when session history disagrees with attached Master.**
Both surfaced; named as discrepancy; escalated to operator.

- *Default posture*: attached Master is authoritative; session history is
  corroborating evidence.
- *Operator decides*: whether to update Master per session history, keep
  Master as-is, or open the older session and reconstruct.
- *SP-1 governance*: never silently regenerate canonical state from session
  history.

**SP-12 disclosure on every consult.**

```
Session history search note (SP-12):
Searched within [scope]. [N found / null]. The session may live in a
different scope I cannot see from here; confirm before concluding.
```

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

## 15. Worked example flow
<a id="section-worked-example-flow"></a>

This section walks a complete audit through v2.0's mechanics. Subject:
hypothetical career-coaching SaaS audit ("Atlas"). Sketch, not rubric;
illustrates how the constructs chain in real use.

```
Session 1 — Orchestration. Operator: "Begin PRISM v2 audit on
Atlas career coaching SaaS. Brief attached: atlas_brief.md."

[SP-13 substrate self-check fires: Claude, Opus-class, match.]
[Setup recommendation surfaces (§8.1):]
  "Recommend creating Claude Project 'Atlas Audit'. [...]
   Proceed without? [yes/no]"
[Operator: yes, create.]

[P0.1 — Probes 6, 7, 1, 3 fire.]
  Probe 6 (Domain Reconnaissance) surveys career-coaching domain
    practice. Surfaces: ICF competencies; CLAS multicultural standards;
    APA ethics for coaching adjacent to therapy. Outputs Jurisdiction
    map (§6.4.4): US (federal) FTC + state UPL rules; EU AI Act for
    any algorithmic matching.
  Probe 1 grades against Lens Library v0.15. Initial coverage map:
    LL-U-001..005 — three covered, two uncovered. Domain triggers:
    Pack 1 (using product), Pack 4 (proving results), Pack 5 (laws).
    Pack 2 partial, Pack 6 doesn't-fire.
  Probe 3 produces Decision brief: "Should sponsor invest additional
    capital in Atlas?" Stakeholder register: founders, investors,
    current users, prospective users, regulator.
[Master P0.1 written. What's next emits: P0.2 with probe iteration.]

[P0.2 — Probes 4, 1, 2 fire. Saturation not yet reached.]
[P0.3 — Probes 1 (re-grade), 5 (falsifier) fire. Coverage saturates.
 Layer 1 clears.]
[P0.4 — Operator ratifies. P0 → P1.]
[Master bumps from p0.4 to p1.0.]

Session 2 — Orchestration. Operator: "Continue Atlas. Master
attached."

[M2 fires silent (version match).]
[Vendor Selection runs for P2.1 — efficacy claim review.]
  Refresh: confirms Claude analytical depth fits; multi-vendor not
    needed at this prompt; adversarial-style alternative not
    material.
  Recommended: Claude Opus 4.7 / standard. Dispatch rationale:
    analytical claim adjudication.
[Envelope produced. What's next emits dispatch-ready payload.]
[Operator dispatches Claude. Output returned. Reconciliation: match.]
[Layer-1 convergence ingests. Master findings section P2.1
 populated.]

[P2.2 — efficacy evidence base. Vendor Selection recommends:
  multi-vendor (equivalence) — Claude + Gemini Pro DR + Perplexity.
  Rationale: source breadth (Perplexity), long-context synthesis
  (Gemini), analytical depth (Claude).]
[Operator dispatches all three. Two return; Perplexity fails.]
[§4.4 graceful degradation: Vendor Triangulation fires at N=2;
 delta notes the live-web breadth dimension is missing.]
[What's next surfaces Perplexity re-dispatch as a candidate.]
[Operator declares "running later" on Perplexity. Status:
 scheduled.]

[Multiple sessions. M5 band 🟡 from session 4. Curation observations
 in What's next from then on. Cloud-drive saves at every session
 close. Master updated continuously.]

[Session 7. M5 reads 🟠 mid-session. Curation directive: "Active.
 Defer further Layer-1 ingestion to fresh session. Next natural
 seam: P3.1 convergence in 2 turns."]
[P3.1 convergence completes. Migration handoff produced.]
[Operator opens Session 8 fresh. Attaches handoff + Master + Library.
 Continues seamlessly.]
```

What this illustrates:

- **Setup is iterative, not waterfall.** Three or four P0 turns
  iterating against the Library before P0→P1 ratification.
- **Vendor Selection is per-dispatch.** Single-vendor on P2.1, multi-
  vendor on P2.2, decision driven by per-prompt analytical needs.
- **Asymmetric returns are absorbed gracefully.** Perplexity fails;
  Vendor Triangulation fires at N=2; the gap is named, not blocking.
- **M5's bands rise gradually.** Session 4 hits 🟡; session 7 reaches
  🟠; migration triggers at the next natural seam.
- **Migration is planning, not rescue.** Session 7 closes cleanly at
  the seam; session 8 opens fresh with full context.

---

## 16. Empirical calibration items
<a id="section-empirical-calibration-items"></a>

These items v2.0 does not fix because they require real-use signal.
Surfaces calibrate post-release on the dogfood run and operator
feedback channel.

1. **Probe iteration floors and ceilings.** Current: minimum 2, soft
   ceiling at 4. Calibrate against real Setup runs.
2. **Probe 1 *fires-maybe* operator-fatigue.** Volume of *maybes* per
   project; mitigation effectiveness of judging-LLM silent resolution.
3. **§{section.currency-maintenance-point-refresh} point-refresh fatigue.** Frequency of `stale-refresh` per
   project; threshold for advisory accumulation toward Update session.
4. **Probe 7 lens accretion path.** Lenses surfaced by domain-
   practitioner survey that aren't in the catalog. Where do they go:
   per-project Learnings Register, staging area for Update-session
   promotion, or other?
5. **Multi-vendor Self-check verification.** Verify Self-check block
   adherence on Gemini, ChatGPT, Perplexity. Currently Claude-family
   verified only.
6. **M5 band thresholds.** Volumetric thresholds (50KB / 200KB; 20 /
   40 turns; etc.) are rev. 1 draft estimates. Calibrate against real
   sessions.
7. **Update session trigger threshold.** Rev. 1 draft: 3 stale-pattern
   accumulations across 6+ months. Calibrate against real maintenance
   cadence.
8. **SP-16 negation-audit signal.** Volume of called-for /
   uncalled-for tags per Output; false-flag rate on legitimate
   contrastive framing; LL-D-019 ("Who said otherwise?") fire rate on
   document-review subjects. Calibrates Elephant-Rule strictness.
9. **SP-16-family and output-gate signal.** Intensifier and hedge
   false-flag rates on legitimate usage; step-6 recompute catch rate;
   validation-dispatch yield (findings per run that the producing
   session had passed); LL-D-020 ("Help or ammunition?") and LL-D-021
   ("Does a stranger follow?") fire rates. Calibrates family
   strictness and validation-dispatch cadence.

These ride into the dogfood run as flagged items. Telemetry on each
feeds the v2.1 minor version.

---

## 17. Mobile operator survival guide
<a id="section-mobile-operator-survival-guide"></a>

v2.0 is mobile-first. Mobile operators routinely encounter patterns —
both frictions and effective interaction moves — that desktop operators
either don't hit or don't need. This section catalogues two classes:
**vendor-client workarounds** (concrete responses to LLM-vendor
mobile-client limitations) and **operator interaction patterns** (ways
of asking and navigating that are more valuable on mobile than on
desktop). Living document: entries accumulate as patterns surface.

Entries here may be surfaced inline as **in-context operator hints** at
specific orchestration touchpoints — the Execution Envelope's
`Operator hints` field (§{section.operator-hints-emission-discipline}) and the *What's next* artifact (§{section.whats-next}) —
so an operator sees the relevant cue at the moment of acting rather
than from memory.

Each entry names the **Problem** or **Situation**, the **Workaround** or
**Pattern**, and **Why it works** (so an operator can extrapolate when
the exact case doesn't match).

### Vendor-client workarounds

#### MO-1 — Samsung file explorer: LLM-downloaded files invisible until indexing catches up

**Platform:** Android, Samsung devices (tested: Galaxy S25+).

**Problem.** Files downloaded from LLM mobile apps land in the Downloads
folder but do not appear in Samsung's built-in file manager immediately.
The system's indexing is delayed; a file you just downloaded may not be
visible to attach workflows for seconds to minutes. On the mobile-first
workflow (download output from one LLM, attach to orchestration
session), this stalls the loop.

**Workaround.** Install **MiX** (third-party Android file manager).
MiX sees new files immediately, independent of Samsung's indexing. It
also includes an HTML/Markdown reader ("HTML View") that renders `.md`
artifacts in place — useful for a quick sanity-check on an execution
output before attaching it to orchestration.

**Why it works.** MiX does its own directory scanning rather than
relying on the system indexing service. Same filesystem, different
reader; the file exists the moment the LLM app finishes writing it,
and MiX respects that.

#### MO-2 — Broken file/clipboard operations in LLM mobile apps

**Platform:** Android, varies by LLM vendor mobile app.

**Problem.** Some LLM mobile apps have incomplete implementations of
basic operations: copy-to-clipboard from rendered outputs, file
download of generated artifacts, attachment of certain file types. The
exact failures vary by vendor and change with app updates, but the
class of failure is consistent enough to plan around.

**Workaround.** Open the same vendor in **Firefox with Desktop Mode
enabled** on the mobile device. Desktop web rendering of the vendor's
site is typically more complete than the native mobile app for these
operations, and the actions that fail in-app usually succeed in the
desktop-rendered web version.

**Why it works.** Vendors' desktop web clients are generally more
mature and more uniformly implemented than their mobile apps; browser
rendering exposes the full web client regardless of the device's form
factor. Desktop Mode in Firefox spoofs the user-agent and viewport,
convincing the vendor's site to serve the full-featured client.

### Operator interaction patterns

#### MO-3 — Artifact + handoff together: "present document with instructions"

**Situation.** A session produces a deliverable that will feed into
another session's work (e.g., a walkthrough document that a fresh
session will react to; a setup strategy that a fresh session will
execute against). Requesting only the artifact leaves the operator to
reconstruct the handoff from memory later, which introduces drift and
loses precision about target model, session hygiene, attachment order,
scope boundaries, and so on.

**Pattern.** Ask for the artifact **and** the accompanying handoff
prompt in the same request. Example phrasing: *"Produce the walkthrough
document and an accompanying handoff prompt I can paste into a fresh
session."* Claude delivers both together; the handoff carries all the
context the next-session operator needs (which model, which mode, which
files to attach, what's in/out of scope), so there is no reconstruction
step later.

**Why it works.** Paired delivery creates self-contained packages that
travel together. The artifact is the deliverable; the handoff is the
operating context. Separating them is a mild form of session-forgetting
(the context is in the producing session's head; it has to be
reconstructed when the consumer session opens). Asking for both in one
shot eliminates the reconstruction step and leverages the producing
session's still-fresh context. This pattern pairs naturally with the
Execution Envelope discipline (§{section.prism-execution-envelope}) — same instinct, different
altitude: bake operating context into the artifact.

#### MO-4 — Session retrieval: "point me to the relevant session"

**Situation.** PRISM work routinely crosses sessions (artifact produced
in session A, used in session B). When an operator is in the wrong
session, or can't remember which session holds which artifact, mobile
manual navigation of the Claude chat list is slow — previews are
short, built-in search is limited, scrolling is tedious on a phone.

**Pattern.** Ask Claude directly: *"point me to the session where
[topic] happened"* or *"give me a clickable link to the [topic]
session."* Claude runs `conversation_search` on the topic, identifies
the referenced session, and returns a `https://claude.ai/chat/{uuid}`
URL. One tap to navigate.

**Why it works.** Claude has past-conversations search as a built-in
tool and can construct canonical session URLs from the UUIDs it
returns. Faster and more precise than mobile manual navigation. The
pattern also works as a disambiguation aid — if multiple sessions match
the topic, Claude can enumerate them with brief summaries before
committing to a link.

**Caveat — bounded-search disclosure (§{principle.SP-12}).** Past-conversations
search is scoped: if the operator is in a project, search is confined
to that project's chats; otherwise it covers non-project chats. If the
target session lives in a different scope, the search returns null.
Claude surfaces this bound rather than asserting a global null —
*"I didn't find it within this project's conversation scope; the
session may live in a different project or outside projects; confirm
before I conclude it doesn't exist."*

#### MO-5 — Persisting artifacts across device/session loss

*(v2.0.1: renamed from `E.5` to `MO-5` to disambiguate from Appendix E.5 — *What's next* template. v2.9.1 completed the rename: `E.1`–`E.4` → `MO-1`–`MO-4`. Mobile-guide subsections are now MO-1 through MO-5; Appendix E template subsections remain E.1 through E.5.)*

**Situation.** Mobile operators work primarily through vendor apps.
Execution outputs downloaded to the device live in local storage,
which is subject to events desktop operators rarely hit: device reset,
app storage clear, accidental delete, storage-quota cleanup, OS update
churn. Even absent those events, the mobile Downloads folder
accumulates cruft — overlapping versions, vendor-default filename
collisions, stale artifacts from prior sessions — that makes finding
the right file its own failure mode. An artifact that survives the
dispatch session can be gone, or effectively lost in the pile, by the
next orchestration turn if nothing external to the device holds a
structured copy. On a multi-session project, losing one converged
output is expensive; losing the Master is a project-reset event.

**Pattern.** Save execution outputs to a cloud drive (Google Drive,
Dropbox, OneDrive, or equivalent) immediately after download, before
switching to the next vendor or ending the session. Same move for the
Master at session close: cloud-save before dismissing the orchestration
session. Project-scoped folders on the cloud drive keep versions
separated and retrievable by name; superseded artifacts are archived
rather than deleted so the audit trail stays intact across the
project's lifetime. The local copy stays available for the immediate
next attach step; the cloud copy is the durable record.

**Why it works.** Cloud drives survive the device events local mobile
storage does not, and structured project folders give the operator a
navigable home rather than the flat Downloads-folder pile. On desktop
substrates this pattern is often redundant; on mobile it is
load-bearing, and the cost of the extra tap is negligible.

#### MO-6 — Multi-lane session legibility: rename and archive

**Situation.** A multi-lane engagement runs many sessions across the standing
lanes (PRISM Desk, PRISM Meta) and ephemeral roles. On a surface that
**auto-names** a session by summarizing its first message, the lane / phase
moniker (e.g. `Meta-7`, `Desk-3`) is **dropped** — two similarly-summarized
sessions become indistinguishable in the recents list, risking work in the wrong
session: the clobber class repo-backed lanes already fight.

**Pattern.** Two manual workflows keep the list legible:

- **Rename each session** `"<plain name> | <Lane>-<N>"` (e.g.
  `"Alumnite engagement retrospective | Meta-7"`) so the lane + number survive the
  auto-name.
- **Suffix superseded** Desk / Meta sessions `"_Archived"` to separate live from
  retired.

Name-disambiguation relies on this **explicit manual-rename step**, not on the
surface deriving the name from the front of the opener line — a summarizing
surface rewrites rather than taking a literal prefix, so front-loading the moniker
is best-effort, not load-bearing. Where a surface exposes no rename tool, the
rename is necessarily a manual operator step (or a surface feature request). The
next-session opener can carry the rename as a named first step so it is not
rediscovered each time.

**Why it works.** The lane + number is the disambiguator the surface discards;
restoring it by hand is cheap and removes the cross-lane-confusion risk. A
related discipline: a **chronic, un-actionable flag** — one only fixable
off-surface — is surfaced **once and tracked**, not re-emitted at every
turn-close (flag-fatigue dulls attention to the flags that matter).

---

## Appendix A — Glossary
<a id="appendix-glossary"></a>

Combines DD Appendix A and Spec Appendix A. Definitions live here;
mechanics live in the cross-referenced sections.

| Term | Definition |
|---|---|
| **Adversarial Scope Probe** | Setup-time probe (§{probe.P2}). Hunts silent omissions in draft strategy. Library-driven; multi-vendor recommended. §{section.probe-2-adversarial-scope-iterates}. |
| **Anchor disposition** | Currency state per `rubric_anchor:` entry. States: `fresh`, `stale-refresh`, `stale-accumulating`. §{section.currency-maintenance-point-refresh}. |
| **Atomic prompt template** | Template that wraps the triple contract around a prompt body. The unit operators paste into execution sessions. §{section.atomic-prompt-template-v2-form}. |
| **Band** | M5's output. Four states: 🟢 Comfortable, 🟡 Getting warm, 🟠 Curate now, 🔴 Migrate. §{section.defensive-migration-at-natural-seams}. |
| **Bump atomicity** | The mechanic that ties Master version increments to defined triggers (phase transitions, convergence rounds, probe iterations, schema changes). §{section.filename-conventions-and-bump-atomicity}. |
| **Claim Conflict** | M7's surface — two findings with incompatible claims on the same surface. v1.x called this Assumption Conflict. §{section.m7-claim-conflict}. |
| **Claim inventory** | Setup artifact. Table of claims the audit must adjudicate, with audit-pass mapping. §{section.claim-inventory}. |
| **Continuous-curation** | Per-turn-close curation observation (band ≥ 🟡) or directive (band ≥ 🟠) in *What's next*. §{section.continuous-curation-posture}. |
| **Continuous-state mechanic** | Master + *What's next* written at every orchestration turn-close, regardless of band state. §{section.failsafe-recovery-continuous-state-mechanics}. |
| **Convergence delta** | Vendor Triangulation output document for an `equivalence` dispatch. §{section.convergence-delta-document}. |
| **Decision brief** | Setup artifact. Captures the decision under test, decision-maker, commissioner positioning, deadline, cost-of-error, falsifiers. §{section.decision-brief}. |
| **Decision Framing Probe** | Setup-time probe (§{probe.P3}). Produces Decision brief + Stakeholder register. §{section.probe-3-decision-framing-once}. |
| **Delta finalization** | When all expected vendor returns are in for an `equivalence` dispatch and Vendor Triangulation closes the convergence delta. §{section.vendor-triangulation}. |
| **Dispatch ID** | Envelope/Output field: a unique per-dispatch-instance identifier, paired with the Prompt digest and copied through, that reconciles a return to the exact dispatch that produced it. Distinct from Prompt ID (which names the pass). §{section.recommended-vs-executed-reconciliation}. |
| **Dispatch lifecycle** | The bounded five-stage dispatch round-trip — build → dispatch → execute → return/converge → reconcile — the dispatch-scoped sibling of the engagement lifecycle; subsumes the late-bound build, the operator/return cards, and the failure leg by reference. §{section.dispatch-lifecycle}. |
| **Dispatch rationale** | Envelope field carrying one positive-framing line per dispatch variant component. §{section.rationale-discipline-per-dispatch-variant}. |
| **Dispatch register** | Master section tracking recommended-vs-executed state per prompt. §{section.master-tracking-dispatch-register}. |
| **Dispatch shape** | Envelope field carrying the dispatch structural shape: `equivalence`, `split`, or `limitation-named`. §{section.single-envelope-with-spectrum-shape}. |
| **Domain Reconnaissance Probe** | Setup-time probe (§{probe.P6}). Surveys domain practice + authoritative-source detection + Jurisdiction map. §{section.probe-6-domain-reconnaissance-iterates-early}. |
| **Engagement closure** | The symmetric gate *out* of an engagement — a three-layer close sweep (object / lane-meta / operator) mirroring three-layer readiness; home of the orphan-sweep, reconcile-at-close, and deliverable polish. §{section.engagement-closure}. |
| **Engagement report** | The comprehensive final report — the engagement's deliverable of record, reflecting all the work, verdict-first and executive-scannable; a tight body + curated appendices. §{appendix.report-architecture}. |
| **Engagement workbook** | An interactive, operator-drivable cockpit companion to the report, delivered when the decision has a quantitative core: editable cells drive the decision gate live. §{appendix.report-architecture}. |
| **Envelope** | The first block of the triple contract — inbound vendor instructions including dispatch metadata, attachments, and operator hints (the PRISM PROMPT INTEGRITY transport anchor renders above it but is not a contract block, §{section.transport-integrity-bracket}). §{section.prism-execution-envelope}. |
| **`equivalence` dispatch** | Same prompt body to N vendors; outputs comparable; triggers Vendor Triangulation at N≥2. §{section.single-envelope-with-spectrum-shape}. |
| **Execution session** | Vendor session running a single dispatched prompt. Framework not attached; loaded artifacts limited to Envelope's `Attachments:` field. §{section.two-session-types}. |
| **Falsifier** | A finding that, if observed, would refute the audit's thesis. Captured in the Decision brief. §{section.probe-5-falsifier-once}, §{section.decision-brief}. |
| **`fires-covered` / `fires-uncovered` / `doesn't-fire` / `fires-maybe`** | Probe 1's tri-state-with-maybe disposition per Lens. §{section.probe-1-coverage-grading-iterates}. |
| **Follow-up** | An additive strategy revision when a *sound* prior run wants a new or expanded dimension: route the scope-addition to the next consuming pass or a new pass — do not augment-and-re-run the completed producer. Distinct from an M10 re-run (which redoes a *defective* run). §{section.strategy-stability}. |
| **Jurisdiction map** | Setup artifact. Per-jurisdiction listing of triggered regulatory regimes and their materiality. §{section.jurisdiction-map}. |
| **Lane** | A unit of parallel work — {a resume pointer, an append-only log, an inbox, one concern}. Object lane (the engagement) and meta lane (methodology). §{section.lanes}. |
| **Layer 1** | Per-prompt convergence — orchestration absorbs returned findings into the Master. Monitors M6/M7/M8/M12 fire here. |
| **Layer 2** | Cold synthesis across all Layer-1 findings to produce the audit's external deliverable. M9 fires here. M11 surfaces readiness. |
| **Lens Library** | The reference catalog of audit-scope lenses. Universal (5) + Domain (21). v0.15 release pinned at `prism-lens-v0.15`. §{section.library-integration}. |
| **`limitation-named` dispatch** | Single-vendor dispatch with explicit `Not chosen:` rationale. §{section.single-envelope-with-spectrum-shape}. |
| **Master** | The single canonical project state file. Updated at every orchestration turn-close. §{section.the-master}. |
| **Migration handoff** | Defined artifact produced at 🔴 (mandatory) or 🟠 (optional) for fresh-session continuity. §{section.migration-handoff}. |
| **Monitor** | Orchestration-side check that fires at a defined lifecycle slot. M1–M12 specified in §{section.monitor-specifications}. |
| **Natural seam** | A transition point where migration is low-cost. Defined set: convergence round complete, phase boundary, deliverable shipped, setup iteration complete. §{section.continuous-curation-posture}. |
| **Orchestration session** | Claude session with the framework attached. Master state, Monitor fires, Setup probes, convergence reasoning all live here. §{section.two-session-types}. |
| **OPEN_ITEMS inbox** | A lane's append-only, tier-1 cross-lane inbox; any session appends, the lane owner drains at its turn. Closes the pointer-clobber class. §{section.cross-lane-inbox}. |
| **Output** | The third block of the triple contract — outbound finding signature with executed-state metadata and operator-next instructions. §{section.prism-execution-output}. |
| **Point refresh** | Per-project, in-Setup currency check on Library `rubric_anchor:` entries. §{section.currency-maintenance-point-refresh}. |
| **Pre-mortem** | Setup-time probe (§{probe.P4}). Imagines execution complete; surfaces failure modes. §{section.probe-4-pre-mortem-iterates}. |
| **PRISM** | Prompts · Research · Iteration · Synthesis · Master. The framework. |
| **PRISM Desk** | The object lane's standing Planner/Steward lane — owns *What's next* and the drain, renders the PRISM UI; re-opened per round or periodically. §{section.prism-desk-and-prism-meta}. |
| **PRISM Meta** | The standing methodology lane (reflection / synthesis / worksheet-building), opened periodically. §{section.prism-desk-and-prism-meta}. |
| **PRISM UI** | The operator-facing View+Controller over the repo Model, rendered by the Desk; STATE / HEALTH / ACTION surfaces. §{section.prism-ui}. |
| **Probe** | Setup-time grading construct against the draft Prompt Strategy. Seven probes specified: P1–P7. §{section.the-seven-probes}. |
| **Prompt Strategy** | The plan of dispatched prompts produced by Setup. Lives in the Master. Iterates in P0; ratifies at P0→P1; revisable at convergence (§{section.strategy-stability}). |
| **Quick mode** | `SETUP_QUICKMODE` — a first-class light Setup shape (one ephemeral session, clean-context sub-agent fan-out) keeping the cheap rigor; graduates to a full engagement without losing work. §{section.setup-onboarding-and-mode-selection}. |
| **Reconcile-at-close** | A closure-gate codification sweep: at engagement close, diff the finished deliverable against its reference architecture in one pass and codify every craft element not yet codified (closes the applied≠codified pattern). §{section.engagement-closure}. |
| **Result Completeness Check** | M12. Convergence-time monitor detecting within-domain coverage gaps in returned findings. §{section.m12-result-completeness-check}. |
| **Saturation** | Two consecutive iterations produce no material change to coverage or strategy. §{section.three-layer-readiness}. |
| **Role × context-tier** | The flexible matrix a session occupies — role (Setup / Desk / dispatch-builder / -consumer / execution / convergence / validation) × tier (orchestration vs execution). §{section.roles-context-tier}. |
| **Self-check** | The middle block of the triple contract — the transport-integrity input-gate (step 0, §{section.transport-integrity-bracket}), substrate verification per §{principle.SP-13}, plus the output-side gates: the §{principle.SP-16} uninvited-frame audit (step 5) and the §{principle.SP-18} recompute gate (step 6). §{section.prism-execution-self-check}. |
| **Setup artifacts** | Four instance-specific artifacts populated during Setup: Decision brief, Stakeholder register, Claim inventory, Jurisdiction map. §{section.setup-artifacts}. |
| **`split` dispatch** | Prompt split into vendor-specific sub-prompts; synthesis happens orchestration-side. §{section.single-envelope-with-spectrum-shape}. |
| **Setup onboarding** | `SETUP_ONBOARDING` — the Setup-as-scaffolder flow that generates the per-engagement SI from a template and emits project-create / install cards; the two-project model. §{section.setup-onboarding-and-mode-selection}. |
| **Share archive** | The default external-share artifact — a self-contained, de-coded, `Index.html`-navigated archive of the engagement's work-product, redacted for share (the canonical repo untouched). §{appendix.external-share}. |
| **Stakeholder register** | Setup artifact. Per-role listing of stake, motivation, positioning/angle, decision power, and communication channel; the operator/commissioner is a mandatory row. §{section.stakeholder-register}. |
| **Standing Principle (SP)** | Persistent posture; not a discrete fire. See the full roster in §{section.standing-principles} and §{section.v1-x-standing-principles-carryforward-catalog}. |
| **Status-glyph legend** | The report's published ● / ◐ / ○ visual vocabulary for capability / coverage / severity, with Confidence and Verification as separate axes; introduced on first use and decoded in the glossary. §{appendix.report-architecture}. |
| **Strategy stability** | At P0→P1 ratification, strategy is "presumed stable, revisable at convergence." §{section.strategy-stability}. |
| **Substitution** | The filename-resolved executed vendor/config (§{principle.SP-14}) differs from the Envelope's recommended vendor/config; the Output `Vendor` field is advisory self-ID (§{section.recommended-vs-executed-reconciliation}). Absorbed at convergence; no automatic re-dispatch. §{section.substitution-absorption}. |
| **Three-layer readiness** | The P0→P1 boundary clears when Structural completeness, Library coverage saturation, and Operator ratification all clear. §{section.three-layer-readiness}. |
| **Transport-integrity bracket** | A top-of-paste PRISM PROMPT INTEGRITY anchor + a terminal END PRISM DISPATCHED PASTE sentinel wrapping any dispatched paste; Self-check Step 0 validates completeness by presence + Dispatch-ID match, so a truncated mid-stream copy is caught before work. Transport framing, not a contract block; excluded from the digest preimage. §{section.transport-integrity-bracket}. |
| **Triple contract** | Envelope (inbound) + Self-check (substrate verify) + Output (outbound). The load-bearing interface between sessions; the dispatched paste wraps it in a transport-integrity bracket (§{section.transport-integrity-bracket}), which is not a contract member. §{section.the-triple-contract}. |
| **Update session** | Standalone, rare, operator-gated session that maintains Library currency. §{section.currency-maintenance-update-session}. |
| **User Voice Probe** | Setup-time probe (§{probe.P7}). Imports real end-user signal. §{section.probe-7-user-voice-iterates-early}. |
| **Vendor config** | Envelope/Output field carrying vendor-specific configuration flags. §{section.prism-execution-envelope}. |
| **Vendor Selection** | Live web-search currency check at every dispatch; produces Envelope. §{section.vendor-selection-at-dispatch}. |
| **Vendor Triangulation** | Layer-1 convergence pass that fires at N≥2 for `equivalence` dispatches. §{section.vendor-triangulation}. |
| ***What's next*** | Per-turn-close artifact. The operator's single source of "what to do next." §{section.whats-next}. |

---

## Appendix B — Spec → v2.0 source mapping
<a id="appendix-spec-v2-0-source-mapping"></a>

How sections of the v2 specification (`PRISM_v2_spec_rev2.md`) map into
this operating document. Use this when reading rationale-level
discussion in the spec and wanting to find the operating instruction
here, or vice versa.

| Spec section | Topic | This file |
|---|---|---|
| Spec.§{section.scope} | Scope of spec | §{section.scope} |
| Spec.§{section.system-overview} | System overview | §{section.system-overview} |
| Spec.§{section.two-session-types} | Two session types | §{section.two-session-types} |
| Spec.§{section.the-triple-contract} | Triple contract | §{section.the-triple-contract} |
| Spec.§{section.the-master} | Master | §{section.the-master} |
| Spec.§{section.whats-next} | *What's next* | §{section.whats-next} |
| Spec.§{section.forward-compatibility-commitments} | Forward-compatibility commitments | §{section.forward-compatibility-commitments} |
| Spec.§{section.vendor-selection-at-dispatch} | Vendor Selection | §{section.vendor-selection-at-dispatch} |
| Spec.§{section.single-envelope-with-spectrum-shape} | Single-Envelope-with-spectrum | §{section.single-envelope-with-spectrum-shape} |
| Spec.§{section.rationale-discipline-per-dispatch-variant} | Rationale discipline | §{section.rationale-discipline-per-dispatch-variant} |
| Spec.§{section.vendor-triangulation} | Vendor Triangulation | §{section.vendor-triangulation} |
| Spec.§{section.asymmetric-parallel-return-handling} | Asymmetric returns | §{section.asymmetric-parallel-return-handling} |
| Spec.§{section.claude-baseline-feasibility-with-named-limitation-escape-hatch} | Claude-baseline | §{section.claude-baseline-feasibility-with-named-limitation-escape-hatch} |
| Spec.§{section.cost-signaling} | Cost signaling | §{section.cost-signaling} |
| Spec.§{section.recommended-vs-executed-reconciliation} | Reconciliation | §{section.recommended-vs-executed-reconciliation} |
| Spec.§{section.master-tracking-dispatch-register} | Dispatch register | §{section.master-tracking-dispatch-register} |
| Spec.§{section.operator-declaration-close-loop} | Close-loop | §{section.operator-declaration-close-loop} |
| Spec.§{section.substitution-absorption} | Substitution absorption | §{section.substitution-absorption} |
| Spec.§{section.prompt-body-convergence-provisions} | Body convergence provisions | §{section.prompt-body-convergence-provisions} |
| Spec.§{section.telemetric-framework-signal-weighting-and-compounding} | Telemetric framework | §{section.telemetric-framework-signal-weighting-and-compounding} |
| Spec.§{section.m5-context-pressure-monitor} | M5 + M12 consolidation | §{section.m5-context-pressure-monitor} |
| Spec.§{section.continuous-curation-posture} | Continuous-curation | §{section.continuous-curation-posture} |
| Spec.§{section.migration-handoff} | Migration handoff | §{section.migration-handoff} |
| Spec.§{section.failsafe-recovery-continuous-state-mechanics} | Continuous-state mechanic | §{section.failsafe-recovery-continuous-state-mechanics} |
| Spec.§{section.defensive-migration-at-natural-seams} | Migration matrix | §{section.defensive-migration-at-natural-seams} |
| Spec.§{section.from-waterfall-to-library-graded-iterative-refinement}–6.5 | Setup mechanics | §{section.from-waterfall-to-library-graded-iterative-refinement}–§{section.strategy-stability} |
| Spec.§{section.library-reference-at-setup}–7.5 | Library integration | §{section.library-reference-at-setup}–§{section.currency-maintenance-update-session} |
| Spec.§{section.claude-project-as-setup-recommendation} | Claude Project recommendation | §{section.claude-project-as-setup-recommendation} |
| Spec.§{section.session-history-as-validation-recovery} | Session history | §{section.session-history-as-validation-recovery} |
| Spec.§{section.standalone-monitors-m1-m2-m4-m5-m9} | Bump atomicity / M2 | §{section.filename-conventions-and-bump-atomicity} + §{section.m2-version-drift} |
| Spec.§{section.convergence-time-monitors-m6-m7-m8-m12} | Attachment warnings | §{section.attachment-warnings} |
| Spec.§{section.whats-next-input-monitors-m3-m10-m11} | M8 vs §{section.currency-maintenance-point-refresh} boundary | §{section.m8-stale-source} |
| Spec.§{section.standing-principles} | Worked example | §{section.worked-example-flow} |
| Spec.§{section.filename-conventions-and-bump-atomicity} | Monitor specs | §{section.monitor-specifications} |
| Spec.§{section.template-shape} | New / extended SPs | §{section.standing-principles-introduced-or-extended-in-v2} |
| Spec.§{section.composition-rules} | SP carryforward catalog | §{section.v1-x-standing-principles-carryforward-catalog} |
| Spec.§{section.operator-hint-catalog} | Resolved direction summary | (provenance — not reproduced) |
| Spec.§{section.missing-handoff-recovery} | Empirical items | §{section.empirical-calibration-items} |
| Spec.§{section.worked-example-flow} | Build residuals | §{section.filename-conventions-and-bump-atomicity}, §{section.atomic-prompt-template-v2-form}, §{section.operator-hint-catalog}, §{section.missing-handoff-recovery}, App C |
| Spec.§{section.empirical-calibration-items} | Flagged-items register | (provenance — see Spec) |
| Spec.§{section.mobile-operator-survival-guide} | Status | (provenance — see Spec) |
| Spec.App A | Terminology | App A |
| Spec.App B | Tag index | App C |
| Spec.App C | v1.x → v2 surface drift | App D |
| DD.App E | Mobile operator survival guide | §{section.mobile-operator-survival-guide} |

Provenance items (where this file does not reproduce content from spec):

- **Resolved direction summary tables** (Spec.§{section.operator-hint-catalog}). Provenance only —
  every direction listed there is implemented in the body of this file.
- **Flagged-items register** (Spec.§{section.empirical-calibration-items}). Alternatives considered for
  each design decision live in the spec; this file carries only the
  chosen alternative with its tag.
- **Status section** (Spec.§{section.mobile-operator-survival-guide}). Build phase is past — this file is the
  build output.

---

## Appendix C — Decision tag index
<a id="appendix-decision-tag-index"></a>

Every decision in this document carries a two-axis tag. This appendix
indexes decisions by tag for easy review.

**Durability axis values:** `structural`, `methodological`,
`vendor-dependent`, `empirical`, `operator-scaffolding`.

**Review-trigger axis values:** `stable`, `review-if: <trigger>`,
`review-annually`.

### C.1 `[structural | stable]`
<a id="appendix-structural-stable"></a>

§{section.what-v2-8-0-covers} (scope), §{section.three-leg-constraint} (three-leg constraint), §{section.two-session-types} (two session types),
§{section.the-triple-contract} (triple contract), §{section.the-master} (Master), §{section.whats-next} (*What's next*), §{section.forward-compatibility-commitments}
(forward-compatibility commitments), §{section.single-envelope-with-spectrum-shape} (single-Envelope-with-
spectrum), §{section.vendor-triangulation} (Vendor Triangulation), §{section.asymmetric-parallel-return-handling} (asymmetric returns), §{section.recommended-vs-executed-reconciliation}
(reconciliation), §{section.master-tracking-dispatch-register} (Dispatch register), §{section.operator-declaration-close-loop} (close-loop), §{section.substitution-absorption}
(substitution absorption), §{section.prompt-body-convergence-provisions} (prompt body convergence provisions),
§{section.m5-context-pressure-monitor} (§{monitor.M5}), §{section.migration-handoff} (migration handoff format), §{section.failsafe-recovery-continuous-state-mechanics} (continuous-state
mechanic), §{section.defensive-migration-at-natural-seams} (defensive migration), §{section.three-layer-readiness} (three-layer readiness),
§{section.probe-1-coverage-grading-iterates} (Probe 1 Coverage grading), §{section.probe-2-adversarial-scope-iterates} (Probe 2 Adversarial Scope),
§{section.probe-7-user-voice-iterates-early} (Probe 7 User Voice), §{section.strategy-stability} (strategy stability), §{section.library-reference-at-setup} (Library
reference at Setup), §{section.m1-missing-inputs} (§{monitor.M1} Missing Inputs), §{section.m2-version-drift} (§{monitor.M2} Version
Drift), §{section.m6-premise-shift} (§{monitor.M6} Premise Shift), §{section.m7-claim-conflict} (§{monitor.M7} Claim Conflict), §{section.m8-stale-source}
(§{monitor.M8} Stale Source), §{section.m12-result-completeness-check} (§{monitor.M12} Result Completeness Check), §{section.m3-sequence-violation} (§{monitor.M3}
Sequence Violation), §{section.m10-rerun-fix-required} (§{monitor.M10} Rerun/Fix Required), §{section.m11-layer-2-readiness} (§{monitor.M11} Layer
2 Readiness), §{section.filename-conventions-and-bump-atomicity} (filename conventions and bump atomicity), §{section.template-shape}
(atomic prompt template), §{section.project-feedback-updates} (project, feedback, updates), §{section.project-identity}
(project identity), §{section.resource-fetch-convention} (resource fetch convention), §{section.feedback-and-contribution} (feedback
and contribution), §{section.citation} (citation), §{section.lanes-roles-and-the-prism-ui} (lanes,
roles, and the PRISM UI), §{section.cross-lane-inbox} (cross-lane OPEN_ITEMS
inbox), §{section.prism-desk-and-prism-meta} (PRISM Desk and PRISM Meta),
§{section.prism-ui} (PRISM UI), §{section.bundle-load-integrity} (bundle-load
integrity), §{section.setup-onboarding-and-mode-selection} (Setup onboarding
and mode selection), §{section.dispatch-lifecycle} (dispatch lifecycle), §{section.transport-integrity-bracket} (transport-integrity bracket), §{section.engagement-closure} (engagement closure).

### C.2 `[methodological | stable]`
<a id="appendix-methodological-stable"></a>

§{section.rationale-discipline-per-dispatch-variant} (rationale discipline), §{section.cost-signaling} (cost signaling), §{section.from-waterfall-to-library-graded-iterative-refinement} (iterative
refinement), §{section.currency-maintenance-point-refresh} (point refresh), §{section.currency-maintenance-update-session} (Update session), §{section.m4-ambiguous-ask} (§{monitor.M4}
Ambiguous Ask), §{section.m9-convergence-type-drift} (§{monitor.M9} Convergence Type Drift), §{section.operator-hint-catalog} (operator hint
catalog), §{section.recovery-flow} (missing-handoff recovery flow), §{section.currency-check-at-session-open} (currency check
at session open), §{section.sp-16-the-elephant-rule} (§{principle.SP-16} The
Elephant Rule — uninvited-frame discipline), §{section.sp-17-plain-words-first}
(§{principle.SP-17} Plain words first), §{section.sp-18-it-must-recompute}
(§{principle.SP-18} It must recompute), §{section.sp-19-claims-carry-their-basis}
(§{principle.SP-19} Claims carry their basis), §{section.sp-20-editions-stand-alone}
(§{principle.SP-20} Editions stand alone), §{section.sp-21-trust-structure-self-report-advisory}
(§{principle.SP-21} Trust structure, self-report advisory),
§{section.sp-22-surface-translation} (§{principle.SP-22} Surface translation),
§{section.independent-validation-dispatch}
(Independent Validation Dispatch).

### C.3 `[methodological | review-if: substrate shifts]`
<a id="appendix-methodological-review-if-substrate-shifts"></a>

§{section.telemetric-framework-signal-weighting-and-compounding} (telemetric framework — calibration thresholds empirical).

### C.4 `[methodological | review-if: vendor landscape changes]`
<a id="appendix-methodological-review-if-vendor-landscape-changes"></a>

§{section.vendor-selection-at-dispatch} (Vendor Selection routine).

### C.5 `[vendor-dependent | review-if: orchestration vendor changes]`
<a id="appendix-vendor-dependent-review-if-orchestration-vendor-changes"></a>

§{section.claude-project-as-setup-recommendation} (Claude Project recommendation), §{section.session-history-as-validation-recovery} (session history mechanism).

### C.6 `[vendor-dependent | review-if: vendor landscape changes]`
<a id="appendix-vendor-dependent-review-if-vendor-landscape-changes"></a>

§{section.claude-baseline-feasibility-with-named-limitation-escape-hatch} (Claude-baseline + escape hatch list).

### C.7 `[operator-scaffolding | stable]`
<a id="appendix-operator-scaffolding-stable"></a>

§{section.sp-1-extended-canonicity-preservation} (§{principle.SP-1} ext Canonicity), §{section.sp-12-bounded-search-disclosure} (§{principle.SP-12} Bounded-Search Disclosure),
§{section.sp-13-substrate-declaration} (§{principle.SP-13} Substrate Declaration), §{section.sp-10-verify-state-before-recommending} (§{principle.SP-10} Verify state
before recommending), §{section.sp-14-filename-discipline} (§{principle.SP-14} Filename Discipline), §{section.sp-8-narrowed-canonical-authority}
(§{principle.SP-8} Canonical Authority — narrowed).

### C.8 `[empirical | review-annually]`
<a id="appendix-empirical-review-annually"></a>

§{section.empirical-calibration-items} (empirical calibration items — collectively; individual items
inherit calibration trigger).

### C.9 `[methodological | review-if: release-sweep | recommended]`
<a id="appendix-methodological-review-if-release-sweep-recommended"></a>

§{appendix.vendor-parsing-observations} (Appendix H preamble — vendor parsing
observations: empirical, observation-driven; the preamble's maintenance
protocol carries the tag, the table rows are data).

**Tag count summary.**

The strength axis (`required` default; `recommended` / `optional` non-default)
and polarity glyphs (✅ / ⚠️ / 🚫) are introduced in v2.1.0 per the
frontmatter `normativity` block; only non-default strength values appear as
tokens in tags. The summary below indexes by the original two-axis pair
(durability × review-trigger); rows whose listed entries include non-default
strength are noted parenthetically. Each cell is a literal count of the
entries listed under the corresponding C-section above, and the totals are
their sums — keep them in lockstep when decisions are added or removed.

| Axis 1 \ Axis 2 | stable | review-if | review-annually | Total |
|---|---|---|---|---|
| structural | 50 | 0 | 0 | 50 |
| methodological | 18 | 3 (1 with `recommended`) | 0 | 21 |
| vendor-dependent | 0 | 3 | 0 | 3 |
| operator-scaffolding | 6 | 0 | 0 | 6 |
| empirical | 0 | 0 | 1 | 1 |
| **Total** | **74** | **6** | **1** | **81** |

---

## Appendix D — v1.x → v2 surface drift
<a id="appendix-v1-x-v2-surface-drift"></a>

Construct-by-construct mapping for operators familiar with v1.10.4.
Direct carryforwards (🔁) and new constructs (🆕) marked; surface drift
items documented with the change.

### D.1 Sessions and lifecycle
<a id="appendix-sessions-and-lifecycle"></a>

| v2 construct | v1.10.4 counterpart | Disposition |
|---|---|---|
| Orchestration session | Setup + convergence sessions (PRISM.md attached) | v2 names the split that v1.x ran inconsistently |
| Execution session | Phase 1 specialist prompt session | Hardened contract via triple |
| Update session | — | 🆕 |
| Master | Starter | Renamed; functionally same |
| *What's next* | TRI-21 progress pointer (single ID) | Reshaped to full artifact |
| Lens Library | — | 🆕 — core v2 architecture |

### D.2 Probes
<a id="appendix-probes"></a>

| v2 probe | v1.x counterpart | Notes |
|---|---|---|
| P1 Coverage grading | — | 🆕 Library-driven |
| P2 Adversarial Scope | Red Team (Phase 2 enrichment) — partial | Reshape — Red Team operated post-finding; P2 operates pre-execution |
| P3 Decision Framing | Implicit in Setup brief | Made explicit; full output is Decision brief + Stakeholder register |
| P4 Pre-mortem | — | 🆕 |
| P5 Falsifier | Red Team (in spirit) | Falsifier is at Setup; Red Team was post-finding |
| P6 Domain Reconnaissance | Discovery (Setup-phase enrichment) | Direct counterpart; covers practice survey + authoritative-source check + Jurisdiction map |
| P7 User Voice | User Voice (Phase 2 enrichment role) | Promoted from Phase 2 enrichment to Setup probe — informs strategy *before* execution |

**v1.x roles not migrating as probes:**

- **Coverage** (Phase 2 enrichment, "find what a specific prompt missed
  within its domain") → became **M12 Result Completeness Check**
  (convergence-time monitor).
- **Fact Check** (Phase 2 enrichment) → absorbed into M8 Stale Source +
  Layer-1 reconciliation.
- **Deep Research** (Phase 2 enrichment) → Vendor Selection mode field
  (§{section.vendor-selection-at-dispatch}).

### D.3 Monitors
<a id="appendix-monitors"></a>

| v2 | v1.x | Disposition |
|---|---|---|
| M1 Missing Inputs | M1 Missing Inputs | 🔁 |
| M2 Version Drift | M2 Version Drift | 🔁 — surface narrowed to filename version |
| M3 Sequence Violation | M3 Sequence Violation | 🔁 |
| M4 Ambiguous Ask | M4 Ambiguous Ask | 🔁 |
| M5 Context Pressure | M5 Attachment Pressure + M12 Conversation Pressure | Merged into single telemetric monitor |
| M6 Premise Shift | M6 Premise Shift | 🔁 — surface broadened (premises now read from Setup artifacts) |
| M7 Claim Conflict | M7 Assumption Conflict | Renamed — v1.x had Assumption Register; v2 reads finding-vs-finding directly |
| M8 Stale Source | M8 Stale Source | 🔁 — surface narrowed (audit evidence only; framework-anchor staleness is point refresh §{section.currency-maintenance-point-refresh}) |
| M9 Convergence Type Drift | M9 Convergence Type Drift | 🔁 — surface broadened (also catches dispatch-mode treatment errors) |
| M10 Rerun/Fix | M10 Rerun/Fix | 🔁 |
| M11 Layer 2 Readiness | M11 Layer 2 Readiness | 🔁 |
| M12 Result Completeness Check | (slot was M12 Conversation Pressure — retired) | 🆕 in v2 (slot reused; v1.x M12 absorbed into M5) |

### D.4 Standing Principles
<a id="appendix-standing-principles"></a>

| v2 SP | v1.x | Disposition |
|---|---|---|
| SP-1 ext | SP-1 (Never reconstruct from memory) | Extended in v2 — covers *offers* to reconstruct |
| SP-2 | SP-2 (Defer non-critical fixes) | 🔁 |
| (none) | SP-3 (Convergence in prompt session) | Dissolved — incompatible with orchestration/execution split |
| SP-4 | SP-4 (Monitors visible) | 🔁 |
| SP-5 | SP-5 (No heuristic guessing) | 🔁 |
| SP-6 | SP-6 (Rebuild at threshold) | 🔁 |
| SP-7 | SP-7 (File delivery mandatory) | 🔁 |
| SP-8 narrowed | SP-8 (Canonical authority + filename disambig) | Split — (a) stays SP-8; (b) becomes SP-14 |
| SP-9 | SP-9 (Silence is never consent) | 🔁 |
| SP-10 | SP-10 (Verify state before recommending) | 🔁 as named principle; mechanics live in Vendor Selection §{section.vendor-selection-at-dispatch} |
| SP-12 | — | 🆕 Bounded-Search Disclosure |
| SP-13 | — | 🆕 Substrate Declaration |
| SP-14 | (extracted from SP-8) | 🆕 — Filename Discipline |

### D.5 Other constructs
<a id="appendix-other-constructs"></a>

| v2 | v1.x | Disposition |
|---|---|---|
| Triple contract (Envelope/Self-check/Output) | Atomic prompt template + Execution notes | Reshape; Self-check is new |
| Vendor Selection | Execution notes (per-prompt prose at Setup, SP-10) | Reshape from Setup-prose to dispatch-time live step |
| Vendor Triangulation | (no v1.x mechanism for this) | 🆕 |
| Bands (🟢🟡🟠🔴) | Context Pressure Bands | 🔁 |
| Two-layer convergence | Two-layer convergence | 🔁 |
| Setup artifacts | Implicit in Setup brief | Made explicit and structured |
| Scope Flags | Scope Flags (5: SF1-SF5) | All dissolved |
| Runtime Profile | Runtime Profile | Dissolved into telemetric framework |
| GATE-0 / GATE-1 / GATE-2 | Gates | Folded into Monitors + What's next + M11 |
| Adaptations | Adaptations | Lighter — strategy-stability with revisable-at-convergence + Master version bump |
| Discrepancy Check | Discrepancy Check (prompt-template mechanic) | Absorbed into M7 Claim Conflict + Layer-1 reconciliation |
| Engagement closure (gate out) | (no v1.x close gate) | 🆕 — symmetric bookend to three-layer readiness |
| Comprehensive final report + interactive workbook | (informal final write-up) | 🆕 — codified deliverable architecture (verdict-first; cockpit) |
| External share archive | (no v1.x external-share) | 🆕 — de-coded archive + redaction regime |

### D.6 Nomenclature changes
<a id="appendix-nomenclature-changes"></a>

| Concept | v1.x | v2 |
|---|---|---|
| Project state file | Starter | Master |
| Progress pointer | (single ID, TRI-21) | *What's next* artifact |
| Inbound prompt header | (informal Execution notes) | Execution Envelope |
| Outbound finding signature | (informal — extracted by user) | Execution Output (file with structured signature) |
| Multi-vendor reconciliation | Discrepancy Check + Fact Check | Vendor Triangulation |
| Within-prompt scope check | Coverage role | M12 Result Completeness Check |
| Domain external signal import | Discovery role | P6 Domain Reconnaissance |
| User signal import | User Voice role | P7 User Voice |
| Filename look-alike defense | SP-8 (b) | SP-14 |
| Recommendation freshness check | SP-10 (in Setup execution notes) | SP-10 + Vendor Selection live check |

---

## Appendix E — Templates compendium
<a id="appendix-templates-compendium"></a>

All paste-ready blocks in one place.

### E.1 PRISM Execution Envelope
<a id="appendix-prism-execution-envelope"></a>

```
━━━ PRISM EXECUTION ENVELOPE ━━━
Prompt ID:          [identifier — purpose/title]
Dispatch ID:        [unique per dispatch instance; orchestration-generated; copy verbatim]
Project:            [project name]
Master version:     [filename of Master at dispatch time]
Prompt digest:      [orchestration-generated at dispatch; copy verbatim; never recomputed]
Posture:            epistemic | investigation
Vendor:             [vendor] | multi-vendor          ← epistemic posture
Dispatch shape:     equivalence | split | limitation-named   ← epistemic posture
Dispatch rationale: [one positive-framing line per variant]   ← epistemic posture
Vendor config:      [vendor-specific config flags]
Session hygiene:    [fresh session, project attachment posture, web search on/off]
Tools:              [vendor tools requested; reserved slot for plugins/skills]
Attachments:        [filename, filename, ...]
Expected output:    [filename to download as]
Operator hints:     [zero or more one-line cues]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### E.2 PRISM Execution Self-check
<a id="appendix-prism-execution-self-check"></a>

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
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### E.3 PRISM Execution Output
<a id="appendix-prism-execution-output"></a>

```
━━━ PRISM EXECUTION OUTPUT ━━━
Prompt ID:        [identifier — purpose/title]
Dispatch ID:      [copied verbatim from Envelope]
Project:          [project name]
Master version:   [from Envelope]
Vendor:           [vendor that actually executed]
Vendor config:    [config actually applied at execution]
Schema version:   output-v1
Date:             [YYYY-MM-DD]
Prompt digest:    [copied verbatim from Envelope]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[findings content]

━━━ END PRISM EXECUTION OUTPUT ━━━
Operator next:        [download instruction; attach instruction]
Attachment warnings:  [optional; one line per warning]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Exhibits manifest** — appended inside the findings content on a corpus-access
bundle return when `Archive: requested` (§{section.prism-execution-output}, the
Execution Output):

```
━━━ EXHIBITS ━━━
[filename] · [source] · [capture date]
   query answered: [the scoped question this artifact substantiates]
   caveat:         [the applicable framing + temporal caveat]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### E.4 Vendor Selection block
<a id="appendix-vendor-selection-block"></a>

```
━━━ VENDOR SELECTION ━━━
Prompt ID:           [...]
Refresh check:       [2-4 lines, what was checked, what was found]
Recommended:         [Vendor / Vendor config / Tools]
Rationale:           [1-2 lines, positive framing]
Soft notes:          [optional; concerns or alternatives the operator should know]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### E.5 *What's next*
<a id="appendix-whats-next"></a>

```
━━━ WHAT'S NEXT ━━━
Master version:        [current Master filename]
Context band:          🟢 | 🟡 | 🟠 | 🔴

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

Operator hints:        [zero or more]

Dispatch-ready payload (if applicable):
  [full Envelope + Self-check + prompt body, ready to paste]
━━━ END WHAT'S NEXT ━━━
```

### E.6 Vendor Triangulation delta
<a id="appendix-vendor-triangulation-delta"></a>

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

### E.7 Migration handoff
<a id="appendix-migration-handoff"></a>

```
━━━ PRISM SESSION HANDOFF ━━━
Project:                [name]
Master version:         [filename of attached Master]
Lens Library version:   [v0.15 | filename pinned]
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

Operator state:         [optional operator note]

Next session opens with:
  Attach: Master, Lens Library, this handoff.
  Read: this handoff first, then proceed per "What's next."
━━━ END SESSION HANDOFF ━━━
```

### E.8 Probe 1 Coverage grading output
<a id="appendix-probe-1-coverage-grading-output"></a>

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

### E.9 Setup artifacts (Master sections)
<a id="appendix-setup-artifacts-master-sections"></a>

#### Decision brief

```
## Decision brief

Subject:           [name]
Decision under test: [one sentence]
Decision-maker:    [name or role]
Commissioner positioning: [operator/commissioner role, motivation, angle/conflict — stated positively]
Deadline:          [date or trigger]
Cost of error:    
  - False positive: [cost]
  - False negative: [cost]
Stakes / blast radius: [one paragraph]
Falsifiers:        [list — findings that would refute the thesis]
```

#### Stakeholder register

```
## Stakeholder register

| Role | Stake | Motivation | Positioning/angle | Decision power | Communication channel |
|---|---|---|---|---|---|
| [operator/commissioner] | [decision/outcome stake] | [why they want this engagement / this outcome] | [advisor / investor / competitor / partner / regulator / arms-length / advocacy; + any conflict] | [yes/advisory/none] | [channel] |
| [name] | [decision/outcome stake] | [motivation] | [positioning/angle; + any conflict] | [yes/advisory/none] | [channel] |
| ... | ... | ... | ... | ... | ... |
```

#### Claim inventory

```
## Claim inventory

| Claim type | Specific claim | Source | Audit pass(es) |
|---|---|---|---|
| Efficacy | [...] | [where claim is made] | P2.x |
| Compliance | [...] | [...] | P3.x |
| Positioning | [...] | [...] | P4.x |
```

#### Jurisdiction map

```
## Jurisdiction map

| Jurisdiction | Triggered regimes | Material to scope? | Pass(es) |
|---|---|---|---|
| US (federal) | FTC, ADA | yes | P3.1 |
| EU | GDPR, EU AI Act | yes | P3.2 |
| US-CA | CCPA/CPRA | yes | P3.1 |
```

### E.10 Dispatch register
<a id="appendix-dispatch-register"></a>

```
## Dispatch register

| Prompt ID | Recommended (Vendor / config) | Executed (Vendor / config) | Status | Convergence ref |
|---|---|---|---|---|
| P2.3 | Gemini Pro DR / DR ON | Claude Opus 4.7 / standard | substituted | layer1-p2.3 |
| P2.4 | Claude Opus 4.7 / standard | — | dispatched | — |
| P2.5 | multi-vendor / equivalence | partial (2 of 3) | partial | layer1-p2.5 |
```

### E.11 Rerun Register
<a id="appendix-rerun-register"></a>

```
## Rerun Register

| Prompt ID | Reason | Source Monitor | Status |
|---|---|---|---|
| P2.1 | M6 — premise shifted | M6 HIGH P2.4 ingestion | overdue |
```

### E.12 Corpus-access Envelope
<a id="appendix-corpus-access-envelope"></a>

```
━━━ PRISM CORPUS-ACCESS ENVELOPE ━━━
Prompt ID:        [identifier — purpose/title]
Dispatch ID:      [unique per dispatch instance; copy verbatim]
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

### E.13 Validation Dispatch Envelope
<a id="appendix-validation-dispatch-envelope"></a>

```
━━━ PRISM VALIDATION DISPATCH ENVELOPE ━━━
Prompt ID:        [identifier — purpose/title]
Dispatch ID:      [unique per dispatch instance; copy verbatim]
Project:          [project name]
Master version:   [filename at dispatch]
Prompt digest:    [orchestration-generated; copy verbatim]
Posture:          epistemic
Dispatch shape:   limitation-named     ← never a triangulation seat
Not chosen:       [producing vendor/session] — the producing thread
                  cannot validate its own framing
Vendor:           [single vendor; fresh session mandatory]
Vendor config:    [vendor-specific flags; web search OFF unless
                  validation scope includes source-checking]
Tools:            [minimal — only what validation requires]
Attachments:      [deliverable(s); cross-consistency materials when
                  in scope]
Excluded context: author rationale, structure notes, known-weak-spots
                  list (the independence rule)
Validation axes:  logic | defensibility | internal consistency |
                  consistency against attached materials |
                  readability | quality
Lens kit:         LL-D-019, LL-D-020, LL-D-021 + SP-18-style
                  recompute sweep
Return form:      severity-tagged findings list, routed to the
                  producing thread
Expected output:  [filename to download as]
Operator hints:   [zero or more one-line cues]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### E.14 Outbound dispatch card
<a id="appendix-outbound-dispatch-card"></a>

The dispatch lifecycle's Stage-2 operator card (§{section.dispatch-lifecycle}).
**Rendered above the paste, never copy-able** (copying orchestration metadata
into the vendor is a failure mode); every field every run, nulls stated as
`NONE`; the card *recommends* seats and never enforces.

```
━━━ DISPATCH CARD — [Prompt ID] ━━━
Prompt ID:        [...]                 Project:  [project]
Dispatch ID:      [unique per dispatch instance]
Posture:          epistemic | investigation
Dispatch shape:   equivalence (N≥2 recommended) | split | limitation-named | single
Seats (RECOMMENDED — not enforced; add distinct vendors freely, absorbed at convergence §4.10/SP-15):
                  - [vendor · mode]
                  - [vendor · mode]      (add more seats as you choose — more arms = stronger triangulation)
Attachments:      [file, file | NONE]
Send rule:        send the SAME paste to EVERY seat you choose, BEFORE bringing any return back
Save returns as:  [outputs/<project>_<promptID>_<vendor>.md]
Reconciliation:   filename (which seat) + Dispatch ID (which dispatch) + digest (sha256:… body copy-through)
Reminders:        [… | NONE]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### E.15 Return-handling card
<a id="appendix-return-handling-card"></a>

The dispatch lifecycle's Stage-4/5 inbound card
(§{section.asymmetric-parallel-return-handling}) — authored at dispatch-build,
surfaced **proactively** when returns are due. Default = the session handles
the bookkeeping.

```
━━━ RETURN HANDLING — [Prompt ID] ━━━
Returns expected: N   (seats: [list])
When they arrive: attach all N here — this session saves + reconciles + converges; you do not file them
Save each as:     outputs/<project>_<promptID>_<vendor>.md   (filename = the seat; SP-14)
Reconcile each:   filename (seat) + Dispatch ID (instance) + digest (copy-through)
Converge:         clean-context sub-agent (seam-③); parent absorbs → Master
If fewer than N clean returns — branch by type (do not conflate):
  · seat failure    → capability null: converge on what returned, name the gap; re-dispatch RANKED, never auto
  · digest/ID miss  → re-grab THAT return before converging (the wrong-prompt anchor catch)
  · substitution    → absorb (operator ran a different vendor); no re-dispatch demanded
  (returns that merely DISAGREE are the triangulation delta, not a failure)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### E.16 Transport-integrity bracket
<a id="appendix-prism-prompt-integrity"></a>

The transport bracket (§{section.transport-integrity-bracket}) — the anchor as
the paste's first line, the terminal sentinel as its last; both excluded from
the J.3 digest preimage. Full paste order in §{section.template-shape}.

```
━━━ PRISM PROMPT INTEGRITY ━━━
Dispatch ID:    [orchestration-minted; a real value, never a placeholder]
Prompt digest:  [display-only copy; the Dispatch ID is what Step 0 matches]
Completeness:   This paste is complete ONLY if its LAST line is the terminal
                sentinel "━━━ END PRISM DISPATCHED PASTE — <Dispatch ID> ━━━"
                carrying THIS Dispatch ID. Before any task work, confirm that
                line is present and its Dispatch ID matches the one above (and
                is not the literal "<Dispatch ID>"). If absent, mismatched, or
                still a placeholder → STOP, report a truncated/corrupted paste,
                do not begin. Presence + string-match only; never recompute the
                digest.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
… Envelope · Self-check · body · Output-signature instruction …
━━━ END PRISM DISPATCHED PASTE — <Dispatch ID> ━━━
```

---

## Appendix G — Embedded Lens Library v0.15
<a id="appendix-embedded-lens-library-v0-15"></a>

The content below is an embedded, byte-for-byte copy of the canonical
`lens/PRISM_lens_library.md` v0.15 (tag `prism-lens-v0.15`) at the
time of this PRISM release. The standalone file remains authoritative
for the catalog's own evolution; this embedded copy is the **default
Library source** for orchestration so a single PRISM.md attachment is
sufficient (mobile-first singleton, per §{section.library-reference-at-setup}).

When PRISM and the embedded copy disagree (e.g., after the standalone
Library is bumped via an Update session, before the next PRISM minor
version embeds the new content), the standalone file is authoritative
on catalog content and PRISM.md's Appendix G is authoritative on
"what shipped with this PRISM version." Operators on the standalone
Library at a newer version pin to that version explicitly and attach
the standalone file alongside the Master (§{section.library-reference-at-setup}).

---

# PRISM Lens Library — v0.15 (pre-release)

**Version:** 0.15
**Release date:** 2026-06-10
**Status:** pre-release standalone artifact; awaiting real-world calibration before promotion to v1.0 stable
**Scope:** framework-neutral reference catalog; not a methodology, not a rubric, not framework-specific

---

## What this is

The PRISM Lens Library is a reference catalog of 26 audit-scope lenses. Each entry is a (material-question × evidence-class × specialist-type) triple that names a specific class of silent omission an audit can plausibly miss.

The Library is used as a coverage map at scope-definition time. For a given audit subject, an auditor evaluates every lens against the subject:

- **Universal lenses** (LL-U-*) fire always-on, on every engagement.
- **Domain lenses** (LL-D-*) fire when their `trigger:` predicate is met by the subject.

Each fire is tri-state:

- **fires-covered** — the lens's concern is already addressed by a planned scope pass.
- **fires-uncovered** — the lens's concern applies but no scope pass addresses it. Flag for inclusion.
- **fires-maybe** — the lens's concern applies at the edge. Operator judgment warranted, informed by subject detail.
- **doesn't-fire** — the trigger predicate is not met; no action.

The gap between fired-lenses and covered-lenses is the silent-omission risk.

## What this is not

- Not a methodology. It does not describe how to run an audit, what order to work in, or how to weight findings.
- Not framework-specific. Integration into any particular audit framework is a separate effort.
- Not self-updating. Version-pinned rubric anchors require human-verified currency checks before depth use.
- Not a completeness guarantee. It catches known silent-omission categories, not unknown-unknowns.
- Not a substitute for specialist competence. A lens flags that a specialist pass should be in scope; it does not ensure the pass is executed well.

## Known limitations

1. **Weak-brief blind spot.** If a subject brief understates facts so that domain predicates fail to fire (a hidden jurisdiction, an undersold efficacy claim, an unreported custody function), the triggering lens stays silent. The Library relies on honest brief population.
2. **Execution-quality blind spot.** A specialist pass included in scope but executed incompetently still checks the box. The Library catches scope-level omissions only.
3. **Novel-subject blind spot.** Subjects whose failure modes don't match any covered category may slip past the catalog entirely.
4. **Anchor currency.** Two entries carry version-pinned rubric anchors (§{lens.LL-D-002} "Can anyone use?" — WCAG 2.2; LL-D-005 "Can attackers get in?" — OWASP ASVS 5.0.0). At v0.10, both anchored entries carry `verification_basis: schema-introduction-only` to signal that `last_verified: 2026-04-24` reflects schema-introduction date, not an independently performed currency check. Run point refresh (per the adopting framework's Setup) before applying those lenses at the depth the anchor implies. The `verification_basis` field flips to `independent-review` after a real currency review is performed.
5. **Pack structure is a convention.** Lenses are grouped into six domain packs as a readability aid. The assignment rule is primary-failure-surface dictates placement; cross-pack concerns are handled via other lenses' triggers. Packs are not orthogonal by construction.

---

## Schema

Every entry uses the following fields:

- `id:` stable identifier of the form LL-{U|D}-NNN
- `name:` short question (the lens's colloquial title)
- `material_question:` the audit-scope question this lens forces scope to answer
- `tier:` universal | domain
- `trigger:` `always-on` (universal) or a predicate (domain)
- `evidence_class:` document | trace | probe | empirical-test | expert-interview | cross-check
- `specialist_type:` the specialist role the lens's pass would typically require (open taxonomy)
- `rubric_anchor:` optional — a version-pinned external rubric the lens recommends binding to
- `last_verified:` populated on entries carrying `rubric_anchor:`
- `verification_basis:` populated on entries carrying `last_verified:`; one of `{schema-introduction-only, independent-review}`. Gates freshness logic in adopting frameworks: a `schema-introduction-only` basis must not be treated as fresh on the strength of date alone
- `recommended_sources:` optional — a framework-curated list of external reference sources this lens recommends consulting, each bound to the lens's material question. Populated only on lenses with a high-signal source; absent on the rest (like `rubric_anchor:`). Each source record carries:
  - `source:` the named corpus or reference
  - `kind:` one of `{narrative, structured-record}`
  - `access:` one of `{open-web, operator-authenticated}`
  - `framing:` MANDATORY — the bias or handling caveat that must travel with any use of the source
  - `recency:` MANDATORY — the source-scoped era/recency posture (how the source's currency bears on its use; distinct from any lens-level findings-recency)
  - `answers:` the lens material-question(s) this source helps address
- `informed_by:` frameworks, standards, and practice traditions that inform the lens (indicative, not exhaustive; not a compliance claim)
- `failure_mode:` the silent omission this lens catches, in plain language
- `minimum_scope_binding:` the minimum scope commitment that counts as "covered" for this lens
- `scope_integrity_probe:` optional — a sharpened, lens-specific falsifier an adopting framework can pose at coverage time to test whether `minimum_scope_binding:` was genuinely satisfied rather than asserted. When present it overrides any generic scope-completeness challenge the adopting framework derives from `minimum_scope_binding:`; populated only on lenses with a ground-truth worked miss, absent on the rest (like `rubric_anchor:`). Backward-compatible: entries without it remain valid.

---

## Universal lenses (5 entries)

```yaml
- id: LL-U-001
  name: Who gets hurt?
  material_question: >
    Which people, groups, or roles bear material
    downside if this subject ships, continues, or
    is acted on as currently framed — including
    parties outside the buying audience?
  tier: universal
  trigger: always-on
  evidence_class: cross-check
  specialist_type: engagement lead / stakeholder analyst
  rubric_anchor: ~
  informed_by:
    - ISO 31000:2018 (stakeholder concept)
    - OECD Regulatory Impact Analysis (counterfactual harm)
    - IIA Standards (materiality)
  failure_mode: >
    Audit recommends ship, continue, or invest
    without naming who absorbs the downside or
    where harm lands unevenly; harmed parties
    surface post-launch.
  minimum_scope_binding: >
    At least one pass enumerates affected
    stakeholders and names at least one whose
    interests cut against the main thesis.

- id: LL-U-002
  name: What's the thesis?
  material_question: >
    What specific claim, decision, or defense is
    the audit testing — stated clearly enough
    that a finding could refute it?
  tier: universal
  trigger: always-on
  evidence_class: document
  specialist_type: engagement lead / audit methodologist
  rubric_anchor: ~
  informed_by:
    - PICO / PICOT (answerable-question structure)
    - PCAOB AS 2101 / ISA 300 (audit planning)
    - IIA Standards (engagement objectives)
  failure_mode: >
    Scope produces findings that cannot be refuted
    because the thesis was never stated; audit
    becomes a tour of the subject rather than a
    test of a proposition.
  minimum_scope_binding: >
    Scope names the thesis or decision under test
    in one sentence, and lists the evidence
    classes that would falsify it.

- id: LL-U-003
  name: What would refute?
  material_question: >
    What plausible observation, rival explanation,
    or contrary evidence would make the current
    thesis materially weaker or false, and where
    would that evidence be found?
  tier: universal
  trigger: always-on
  evidence_class: cross-check
  specialist_type: engagement lead / audit methodologist
  rubric_anchor: ~
  informed_by:
    - Cochrane RoB 2 (risk-of-bias structure)
    - GRADE (certainty-of-evidence tiers)
    - PCAOB / ISA audit-risk model
  failure_mode: >
    Audit becomes confirmatory and collects only
    evidence that agrees with the draft view;
    replication or second opinion trivially
    overturns it.
  minimum_scope_binding: >
    Scope names at least one disconfirming path
    and where that path would be checked.

- id: LL-U-004
  name: Who acts on this?
  material_question: >
    Who is the audit output written for, and what
    decision does it feed? Shape, depth, and tone
    should follow from that decision and its stakes.
  tier: universal
  trigger: always-on
  evidence_class: document
  specialist_type: engagement lead / audit communications
  rubric_anchor: ~
  informed_by:
    - IIA Standards (engagement communication)
    - PCAOB AS 1301 (communication with audit committees)
    - Decision-analysis tradition
  failure_mode: >
    Audit is technically correct but operationally
    useless because its depth, vocabulary, or
    framing does not match the decision it was
    supposed to serve.
  minimum_scope_binding: >
    Scope names the decision-maker, the decision,
    the deadline, and the cost of getting it wrong
    in each direction.

- id: LL-U-005
  name: What laws touch this?
  material_question: >
    Which legal, regulatory, or supervisory regimes
    plausibly apply to this subject, and does any
    rise to material depth requiring a specialist
    pass?
  tier: universal
  trigger: always-on
  evidence_class: document
  specialist_type: regulatory counsel (screening) / compliance analyst
  rubric_anchor: ~
  informed_by:
    - OECD Regulatory Impact Analysis (regulatory surface)
    - IIA Standards (compliance scope)
    - General compliance-audit tradition
  failure_mode: >
    Audit ships without having asked whether any
    law applies; material regulatory surface
    (privacy, advertising, discrimination,
    sector-specific) is discovered by a regulator,
    not the audit.
  minimum_scope_binding: >
    A regulatory screening pass is present in
    scope, naming plausibly applicable regimes and
    marking each as "material, specialist pass
    required" or "screened, immaterial" with reason.
```

---

## Domain lenses (21 entries across 6 packs)

### Pack 1 — Using the product

**Trigger:** `predicate: end users directly interact with a UI, workflow, or content experience`

```yaml
- id: LL-D-001
  name: Can they finish?
  material_question: >
    Can a target user move from entry to intended
    outcome without confusion, dead ends, or
    avoidable abandonment?
  tier: domain
  trigger: >
    predicate: end users must complete a sequence
    of actions to realize the subject's value
  evidence_class: empirical-test
  specialist_type: UX researcher / usability analyst
  rubric_anchor: ~
  informed_by:
    - Nielsen's 10 Usability Heuristics
    - ISO 9241-11 (usability definition)
  failure_mode: >
    Scope reviews features but misses a broken
    critical path that blocks conversion or task
    completion; production telemetry surfaces the
    failure, not the audit.
  minimum_scope_binding: >
    One pass maps at least one critical journey
    end to end and either tests it with
    representative users or reviews telemetry
    against success criteria.

- id: LL-D-002
  name: Can anyone use?
  material_question: >
    Can users with sensory, motor, cognitive,
    language, or assistive-technology constraints
    actually operate this product for its intended
    task?
  tier: domain
  trigger: >
    predicate: subject has a user interface
    intended for broad or public user populations
  evidence_class: probe
  specialist_type: accessibility auditor (WCAG-qualified)
  rubric_anchor: >
    WCAG 2.2 (October 2023); access mode:
    conformance audit combining automated scanning
    and manual assistive-technology testing
  last_verified: 2026-04-24
  verification_basis: schema-introduction-only
  informed_by:
    - WCAG 2.2
    - ARIA Authoring Practices
    - EN 301 549 (EU ICT accessibility)
  failure_mode: >
    Product launches excluding a meaningful
    fraction of users and exposes the sponsor to
    disability-discrimination liability.
  minimum_scope_binding: >
    An accessibility pass is present, names a
    target conformance level with version pin,
    and includes both automated and manual
    testing.

- id: LL-D-003
  name: Is guidance sound?
  material_question: >
    Where the product delivers expert content,
    advice, or recommendations, is that content
    accurate, current, and fit for the audience's
    stakes?
  tier: domain
  trigger: >
    predicate: subject provides instructional,
    advisory, editorial, or evaluative content
    that could materially shape user action
  evidence_class: expert-interview
  specialist_type: domain subject-matter expert (e.g., clinician, CFP, career counselor, as matched to content domain)
  rubric_anchor: ~
  informed_by:
    - GRADE
    - EEF toolkit (evidence of effect)
    - Cochrane (where clinical overlap)
    - Editorial-standards tradition
  failure_mode: >
    Polished experience passes as quality while
    the underlying guidance is wrong, outdated, or
    mis-scoped; users act on it at their cost.
  minimum_scope_binding: >
    One pass samples high-impact guidance against
    independent references or qualified
    subject-matter reviewers, with a sampling
    plan and accuracy criteria.

- id: LL-D-019
  name: Who said otherwise?
  material_question: >
    Does every uninvited frame in the document
    under review — a negation, a defensive
    intensifier, or a temporal hedge — answer
    a live alternative the reader demonstrably
    brings, rather than planting a doubt or
    trajectory nobody raised?
  tier: domain
  trigger: >
    predicate: subject is or includes a prose
    deliverable — report, pitch, marketing or
    position copy, expository document — whose
    framing shapes reader belief or action
  evidence_class: document
  specialist_type: communications editor / framing reviewer
  rubric_anchor: ~
  informed_by:
    - Lakoff, "Don't Think of an Elephant!" (frame activation by negation)
    - Misinformation-correction research (negation reinforces familiarity)
    - Plain-language editorial tradition
  failure_mode: >
    Scope reviews the document's claims but
    never audits its framing devices;
    uncalled-for denials plant the frames
    they deny, defensive intensifiers
    ("real", "actual", "truly") imply doubts
    nobody raised, and temporal hedges ("for
    now", "currently") concede adverse
    trajectories the evidence never put on
    the table.
  minimum_scope_binding: >
    One pass enumerates every negation ("not
    Y", "X, not Y", "rather than Y", "no Y"),
    defensive intensifier ("real", "actual",
    "genuine", "truly", "clearly"), and
    temporal hedge ("for now", "today",
    "currently") in the deliverable and tags
    each as called-for (naming the live
    alternative it answers) or uncalled-for
    (flagged for positive, informative
    rewrite). Where the positive verb already
    bounds the claim ("shrink", "slow",
    "narrow"), a trailing denial of the
    unbounded case is uncalled-for by
    default; inside a section whose explicit
    job is worst-case assessment, the extreme
    is a called question. Headings, titles,
    and opening sentences audited first.

- id: LL-D-020
  name: Help or ammunition?
  material_question: >
    Read sentence by sentence as the named
    audience — analyst, quant, banker, per the
    document's audience line — does every
    sentence make sense, read clearly, and
    land as positive or at least defensible
    for the subject, rather than handing a
    hostile expert ammunition?
  tier: domain
  trigger: >
    predicate: subject is or includes a prose
    deliverable addressed to a named expert
    audience whose reading affects the
    subject's interests
  evidence_class: document
  specialist_type: named-audience expert reviewer (hostile-but-fair posture)
  rubric_anchor: ~
  informed_by:
    - Hostile-review / red-team editorial practice
    - Equity-research and credit-memo review conventions
    - Plain-language editorial tradition
  failure_mode: >
    The deliverable is reviewed for accuracy
    but never read as its audience reads it;
    a sentence that is true and clear still
    hands a hostile-but-fair expert
    ammunition — an implied arithmetic that
    computes against the subject, a framing a
    quant reads as evasion — and the audit
    passes what the audience punishes.
  minimum_scope_binding: >
    One pass reads every sentence through
    three lenses in order: (1) does it make
    sense; (2) is it clear, preferring the
    plain word over compressed jargon;
    (3) read as the named audience, is it
    problematic or positive for the subject —
    recomputing any arithmetic the sentence
    implies and asking what a hostile-but-
    fair expert does with it. Findings route
    to rewrite, with the triggering lens
    named.

- id: LL-D-021
  name: Does a stranger follow?
  material_question: >
    Can a zero-context reader resolve every
    referent in the document — every quoted
    figure attributed, every acronym defined
    at first use, every premise the logic
    depends on stated on the page — without
    access to anything the author knows but
    the page omits?
  tier: domain
  trigger: >
    predicate: subject is or includes a prose
    deliverable intended to travel beyond its
    authors, reaching readers who arrive
    without the production context
  evidence_class: document
  specialist_type: cold reader / new-to-file editor
  rubric_anchor: ~
  informed_by:
    - Technical-writing review practice (cold-read pass)
    - Curse-of-knowledge research (Camerer et al.; Heath & Heath framing)
    - Plain-language editorial tradition
  failure_mode: >
    Everyone who reviews the document already
    knows the context, so nobody notices the
    often-quoted figure quoted nowhere, the
    acronym never defined, or the unstated
    premise an entire calculation silently
    assumes — a report whose export-limit
    arithmetic depended on the company's home
    jurisdiction, stated nowhere — until a
    real stranger reads it.
  minimum_scope_binding: >
    One pass reads the deliverable as a
    zero-context stranger: every third-party
    claim attributed (quoted where, by whom),
    every acronym defined at first use,
    insider jargon expanded, and every
    premise the document's logic depends on
    stated on the page. Headings and opening
    sentences audited first; unresolved
    referents and unstated premises route to
    rewrite.
```

### Pack 2 — Running the system

**Trigger:** `predicate: software, data processing, or model behavior materially affects delivery or outputs`

```yaml
- id: LL-D-004
  name: Will it hold up?
  material_question: >
    Under realistic load, failure, and maintenance
    conditions, will the system keep producing
    the intended result?
  tier: domain
  trigger: >
    predicate: backend services, integrations, or
    model/runtime behavior materially affect user
    outcome
  evidence_class: trace
  specialist_type: SRE / reliability engineer
  rubric_anchor: ~
  informed_by:
    - ISO/IEC 25010:2011 (software quality)
    - Google SRE principles (reliability, error budgets)
    - NIST CSF 2.0 (identify/protect structure)
  failure_mode: >
    Audit signs off on a demoable system that
    degrades under production reliability,
    performance, or maintenance pressure;
    scaling failures later attributed to market.
  minimum_scope_binding: >
    One pass inspects architecture, failure
    handling, performance, and maintainability
    under realistic conditions.

- id: LL-D-005
  name: Can attackers get in?
  material_question: >
    Could a reasonably capable attacker or abusive
    user compromise accounts, data, or core
    functions through the application as shipped?
  tier: domain
  trigger: >
    predicate: subject stores accounts, user data,
    money, or privileged actions, or is publicly
    deployed with attacker-reachable surface
  evidence_class: probe
  specialist_type: AppSec engineer / penetration tester
  rubric_anchor: >
    OWASP ASVS 5.0.0 (May 2025); access mode:
    requirements-based verification plus focused
    security testing at appropriate level
  last_verified: 2026-04-24
  verification_basis: schema-introduction-only
  informed_by:
    - OWASP ASVS 5.0.0
    - OWASP Top 10
    - NIST SSDF 1.1
    - MITRE ATT&CK (adversary behavior model)
  failure_mode: >
    Audit misses exploitable weaknesses in auth,
    session handling, input processing, or data
    exposure; first external researcher or
    attacker finds what the audit would have.
  minimum_scope_binding: >
    One pass verifies core security controls or
    maps them to an equivalent security
    verification scheme at a stated level.

- id: LL-D-006
  name: How would it fail?
  material_question: >
    How can the system's outputs be manipulated,
    misled, abused, or weaponized under
    adversarial, edge-case, or misuse conditions?
  tier: domain
  trigger: >
    predicate: subject produces personalized,
    ranked, model-mediated, or otherwise gameable
    outputs with real user consequences
  evidence_class: probe
  specialist_type: red team / adversarial-ML specialist
  rubric_anchor: ~
  informed_by:
    - MITRE ATLAS (adversarial ML)
    - NIST AI RMF 1.0
    - NIST AI 600-1 (generative AI risk profile)
    - FAIR (threat-scenario quantification)
  failure_mode: >
    Harmful edge-case behavior, leakage, or abuse
    pathways stay invisible until live users
    discover them; abuse scenarios never
    structured before launch.
  minimum_scope_binding: >
    One pass runs structured misuse, edge-case,
    or adversarial scenarios against high-stakes
    outputs and documents the threat model.

- id: LL-D-007
  name: What relies on others?
  material_question: >
    Which third-party APIs, external libraries,
    data feeds, or upstream dependencies must
    remain available and trustworthy for the
    subject's core loop to function?
  tier: domain
  trigger: >
    predicate: subject's core functionality
    depends on external APIs, data feeds, or
    third-party libraries that the sponsor does
    not control
  evidence_class: trace
  specialist_type: supply-chain / third-party risk analyst
  rubric_anchor: ~
  informed_by:
    - NIST CSF 2.0 (supply-chain function)
    - NIST SP 800-161 (supply-chain risk)
  failure_mode: >
    Audit exhaustively tests first-party code but
    misses that the core loop breaks when a
    single external API degrades, changes terms,
    or goes down.
  minimum_scope_binding: >
    One pass inventories external dependencies,
    identifies the critical path through them,
    and names at least one failure scenario with
    mitigation.

- id: LL-D-015
  name: Can you see it?
  material_question: >
    Can operators see what the system is doing in
    production well enough to detect problems,
    diagnose incidents, and support scale-up —
    and is that visibility matched to the system's
    maturity and blast radius?
  tier: domain
  trigger: >
    predicate: subject runs production services
    whose behavior, latency, error rate, or
    output quality must be monitored for
    operational or business continuity
  evidence_class: trace
  specialist_type: SRE / platform engineer
  rubric_anchor: ~
  informed_by:
    - Google SRE principles (observability, SLIs/SLOs)
    - OpenTelemetry (instrumentation patterns)
    - ISO/IEC 25010:2011 (operability)
  failure_mode: >
    Product runs but nobody can tell whether it
    is working; incidents surface via user
    reports rather than internal detection, and
    scale-up proceeds blind.
  minimum_scope_binding: >
    One pass inspects observability stance —
    logs, metrics, and traces coverage of
    critical paths; alerting on user-visible
    symptoms; and SLO/SLI maturity against the
    system's current stage.

- id: LL-D-016
  name: Is the ledger safe?
  material_question: >
    Where the subject holds user funds, settles
    payments, or records balances, are the
    ledger, reconciliation, and anti-fraud
    controls rigorous enough to prevent loss,
    theft, or silent corruption?
  tier: domain
  trigger: >
    predicate: subject custodies user funds,
    operates a digital wallet, processes
    payments directly, or records financial
    balances that users rely on
  evidence_class: trace
  specialist_type: financial-systems auditor / ledger engineer / SOC 1 reviewer
  rubric_anchor: ~
  informed_by:
    - SOC 1 (ICFR-relevant controls)
    - PCI DSS (where card data in scope)
    - Double-entry accounting and reconciliation practice
  failure_mode: >
    Ledger quietly drifts from reality; users
    lose funds to fraud, reconciliation errors,
    or adversarial manipulation of balance state
    because no one verified custodial controls
    end-to-end.
  minimum_scope_binding: >
    One pass inspects ledger integrity,
    reconciliation cadence, anti-fraud controls,
    and custody/segregation of user funds; at
    least one end-to-end transaction trace is
    verified.
```

### Pack 3 — Getting chosen

**Trigger:** `predicate: subject competes for adoption, revenue, budget, or strategic attention`

```yaml
- id: LL-D-008
  name: Compared to what?
  material_question: >
    Against the user's realistic alternatives —
    including substitutes and do-nothing — where
    is this materially better, worse, or merely
    different?
  tier: domain
  trigger: >
    predicate: users or buyers have realistic
    substitute products, workflows, or
    status-quo options
  evidence_class: cross-check
  specialist_type: competitive analyst / market researcher
  rubric_anchor: ~
  recommended_sources:
    - source: ideas.rip
      kind: narrative
      access: open-web
      framing: >
        Founder-selection bias; retrospective failure
        narratives optimized for teaching. Funded ≠
        correct — a documented startup is a survivor of
        the funding filter, not a validated answer.
      recency: >
        Era-conditional: capital-climate and
        category-maturity details age; substitution
        patterns are more durable. Weight recent cases
        for current priors.
      answers: >
        Substitute and do-nothing enumeration for an
        audience-job pair: what realistic alternatives
        a comparable subject was measured against.
    - source: pitch-deck libraries
      kind: narrative
      access: open-web
      framing: >
        Survivor bias — how a category presents itself
        to investors, not ground truth. Funded ≠
        correct. Premium tiers are paywalled; the
        free corpus is browsable.
      recency: >
        Era-conditional: deck conventions evolve with
        capital climate and category maturity. Match
        the library era to the question's era.
      answers: >
        "Compared to what?" framing patterns — how
        comparable subjects name their competitive set
        and differentiate against substitutes.
    - source: CB Insights / PitchBook / Tracxn
      kind: structured-record
      access: operator-authenticated
      framing: >
        Coverage gaps by region, stage, and era;
        stealth rounds absent and bootstrapped
        companies under-represented. Classification
        quality is platform-decided. Funding ≠
        business signal. Access via employer or
        library subscriptions; do not gatekeep on a
        free-only basis.
      recency: >
        Continuously updated, so the question is not
        "is this stale?" but "what historical depth
        does it carry, and does it cover my era?"
      answers: >
        Competitor and comparable-population selection:
        which firms constitute the realistic
        alternative set for the audience-job pair.
  informed_by:
    - Porter five-forces and strategy literature
    - Jobs-to-be-Done (substitute analysis)
    - Competitive-intelligence practice
  failure_mode: >
    Audit overstates novelty or fit because no
    realistic comparator set — especially
    substitutes and do-nothing — was named; a
    buyer-side read surfaces the gap. Common
    drift: category-bounded rival enumeration
    is mistaken for substitute analysis.
    Substitutes are defined by the audience and
    the job — not by product category — so a
    hardware device, a different workflow, or a
    do-nothing default can each be a substitute
    if it serves the same audience-job pair.
  minimum_scope_binding: >
    One pass names the audience and the job
    first, then names rivals, substitutes, and
    do-nothing as alternatives for that
    audience-job pair (substitutes defined by
    the job, not the product category);
    differentiation is stated in buyer-language
    and backed by evidence.
  scope_integrity_probe: >
    The named comparator set claims to cover
    this audience-job pair's realistic
    alternatives. Name at least one substitute
    that serves the same audience and the same
    job through a different form factor — a
    hardware device, a manual workflow, an
    adjacent-category product, or a do-nothing
    default — that the set omits. Pass only if
    either (a) at least one such audience-job
    substitute is named and incorporated, or
    (b) its absence is documented with explicit
    rationale for why no cross-form-factor
    substitute serves this audience-job pair.

- id: LL-D-009
  name: Does it pay back?
  material_question: >
    Can the subject sustain itself financially or
    operationally without assuming unreal
    conversion, retention, cost, or staffing
    behavior?
  tier: domain
  trigger: >
    predicate: audit must judge commercial
    viability, unit economics, or sustainability
    of the operating model
  evidence_class: document
  specialist_type: unit-economics analyst / FP&A
  rubric_anchor: ~
  recommended_sources:
    - source: ideas.rip
      kind: narrative
      access: open-web
      framing: >
        Founder-selection bias; retrospective failure
        narratives optimized for teaching. Funded ≠
        correct — a documented startup is a survivor of
        the funding filter, not a validated answer.
      recency: >
        Era-conditional: capital-climate and
        category-maturity details age; substitution
        patterns are more durable. Weight recent cases
        for current priors.
      answers: >
        Demand-validation and willingness-to-pay priors:
        whether comparable subjects found a market that
        actually paid, and where demand assumptions
        broke down.
    - source: pitch-deck libraries
      kind: narrative
      access: open-web
      framing: >
        Survivor bias — how a category presents itself
        to investors, not ground truth. Funded ≠
        correct. Premium tiers are paywalled; the
        free corpus is browsable.
      recency: >
        Era-conditional: deck conventions evolve with
        capital climate and category maturity. Match
        the library era to the question's era.
      answers: >
        TAM/SAM/SOM construction patterns and
        demand-claim conventions: how comparable
        subjects sized their market and framed the
        revenue opportunity.
    - source: CB Insights / PitchBook / Tracxn
      kind: structured-record
      access: operator-authenticated
      framing: >
        Coverage gaps by region, stage, and era;
        stealth rounds absent and bootstrapped
        companies under-represented. Classification
        quality is platform-decided. Funding ≠
        business signal. Access via employer or
        library subscriptions; do not gatekeep on a
        free-only basis.
      recency: >
        Continuously updated, so the question is not
        "is this stale?" but "what historical depth
        does it carry, and does it cover my era?"
      answers: >
        Comparable transactions, valuations, and
        funding history as a market-sizing and
        commercial-viability cross-check.
  informed_by:
    - SaaS unit-economics literature (CAC, LTV, payback)
    - OECD RIA (counterfactual analysis)
    - Valuation and forecast-audit practice
  failure_mode: >
    Audit recommends continuation or scaling on
    economics that fail outside optimistic
    assumptions; cash runs out before
    product-market fit.
  minimum_scope_binding: >
    One pass tests revenue, cost, conversion,
    retention, or staffing assumptions with
    sensitivity analysis on the two or three
    assumptions that dominate the outcome.
```

### Pack 4 — Proving results

**Trigger:** `predicate: subject makes causal, quantitative, comparative, or efficacy claims that could change behavior`

```yaml
- id: LL-D-010
  name: What's the evidence?
  material_question: >
    For each quantified efficacy or outcome claim,
    do the study design, sample, comparator,
    measurement, and reproducibility survive
    independent appraisal?
  tier: domain
  trigger: >
    predicate: subject or sponsor makes a measured
    outcome claim that could change buyer, user,
    regulator, or investor behavior
  evidence_class: cross-check
  specialist_type: evidence-synthesis methodologist / study-design reviewer
  rubric_anchor: ~
  informed_by:
    - Cochrane RoB 2 (risk of bias)
    - GRADE (certainty of evidence)
    - CONSORT (trial reporting)
    - PRISMA 2020 (synthesis reporting)
    - SPIRIT 2013 (study design)
  failure_mode: >
    Marketing claim is supported by a small,
    non-comparative, non-replicated internal
    study; the claim collapses on first external
    challenge because the audit never tested the
    underlying evidence.
  minimum_scope_binding: >
    One pass grades the strongest supporting
    evidence on design, sample, comparator,
    measurement, and reproducibility, then states
    the resulting confidence level.

- id: LL-D-017
  name: Is it clinically valid?
  material_question: >
    Where the subject makes a clinical,
    diagnostic, therapeutic, or physiological
    claim, does the evidence meet the clinical
    and regulatory standards for the relevant
    medical-device class and jurisdiction?
  tier: domain
  trigger: >
    predicate: subject performs a diagnostic,
    therapeutic, or physiological function, is
    marketed for medical use, or would plausibly
    meet the definition of a medical device
    under FDA, EU MDR, or comparable regime
  evidence_class: cross-check
  specialist_type: clinical regulatory reviewer / clinical biostatistician / medical device consultant
  rubric_anchor: ~
  informed_by:
    - ICH-GCP (clinical trial conduct)
    - FDA guidance on software as a medical device (SaMD)
    - IMDRF SaMD risk categorization
    - EU MDR (medical device regulation)
    - IEC 62304 (medical device software lifecycle)
  failure_mode: >
    Product makes a clinical claim supported by
    evidence that passes a general scientific-
    validity bar but fails the clinical-regulatory
    bar; regulator intervention, adverse events,
    or recall follow launch, and patients bear
    the downside.
  minimum_scope_binding: >
    One pass classifies the subject under the
    applicable medical-device regime, grades the
    clinical evidence against the required
    standard for that class, and verifies
    regulatory-submission adequacy.
```

### Pack 5 — Laws and rights

**Trigger:** `predicate: subject touches regulated data, advertising claims, automated decisions affecting users, employment, education, health, minors, or cross-border operations`

```yaml
- id: LL-D-011
  name: Is data handled lawfully?
  material_question: >
    Is each category of personal data collected,
    processed, stored, and shared on a defensible
    lawful basis, with consent patterns,
    retention, minimisation, and subject rights
    actually implemented?
  tier: domain
  trigger: >
    predicate: subject processes personal data,
    or special-category data such as health,
    disability, children's, biometric, financial,
    or employment data
  evidence_class: document
  specialist_type: DPO / privacy counsel
  rubric_anchor: ~
  informed_by:
    - GDPR / UK GDPR (lawful basis, rights)
    - ISO 27701 (privacy information management)
    - NIST Privacy Framework
    - CCPA / CPRA (US state privacy patterns)
  failure_mode: >
    Product is built on a consent or legal-basis
    pattern that fails scrutiny; regulator action,
    fines, or forced retooling follow launch, and
    the audit never examined it.
  minimum_scope_binding: >
    One pass covers lawful basis per data
    category, consent patterns, retention,
    cross-border transfer, and subject-rights
    implementation.

- id: LL-D-012
  name: Who does it disadvantage?
  material_question: >
    Does the subject's automated output, pricing,
    routing, or recommendation systematically
    disadvantage a group along a protected
    characteristic or legitimate interest?
  tier: domain
  trigger: >
    predicate: subject makes automated decisions,
    recommendations, prices, or routes that
    materially affect users
  evidence_class: empirical-test
  specialist_type: algorithmic-fairness analyst / civil-rights counsel
  rubric_anchor: ~
  informed_by:
    - NIST AI Risk Management Framework 1.0
    - EU AI Act (high-risk system framing)
    - US EEOC guidance on automated employment decisions
    - UK Equality Act 2010
    - ISO/IEC 24027 (AI bias)
  failure_mode: >
    Automated output produces disparate outcomes
    along age, gender, disability, or other
    protected lines; first external audit,
    journalist, or regulator surfaces the pattern.
  minimum_scope_binding: >
    One pass names the decision surface, the
    protected characteristics analysed, the
    metric used, and the thresholds for concern.

- id: LL-D-013
  name: Which rules apply where?
  material_question: >
    For each jurisdiction the subject operates in,
    which rules govern data residency, consumer
    protection, advertising substantiation,
    employment, and sector-specific regulation —
    and do the operational choices reflect them?
  tier: domain
  trigger: >
    predicate: subject operates across two or
    more regulatory jurisdictions, or markets
    quantified/comparative claims in any
    regulated jurisdiction
  evidence_class: document
  specialist_type: jurisdictional regulatory counsel / substantiation counsel
  rubric_anchor: ~
  informed_by:
    - GDPR / UK GDPR / CCPA-CPRA comparative practice
    - FTC advertising substantiation (US)
    - UK CAP / BCAP Codes, ASA precedent
    - EU Unfair Commercial Practices Directive
    - OECD cross-border data transfer guidance
  failure_mode: >
    Product applies its home-jurisdiction defaults
    abroad and violates a local rule no one
    examined — data residency, tax registration,
    local consent pattern, local advertising
    prohibition, or substantiation standard.
  minimum_scope_binding: >
    One pass names each live jurisdiction and
    the regimes triggered, including at least
    one requirement that materially cuts against
    current design or claim.

- id: LL-D-018
  name: Are kids protected?
  material_question: >
    Where minors use, are exposed to, or have
    data collected by the subject, are
    age-appropriate design, grooming-risk
    controls, parental-consent patterns, and
    child-specific safety features adequate —
    beyond the baseline privacy lawful basis?
  tier: domain
  trigger: >
    predicate: subject is likely to be accessed
    by minors, markets to minors, collects data
    from minors, or hosts content or interaction
    patterns where adult-minor contact or
    child-targeted harm is plausible
  evidence_class: cross-check
  specialist_type: child-safety specialist / age-appropriate-design (AADC) consultant
  rubric_anchor: ~
  informed_by:
    - UK ICO Age Appropriate Design Code
    - COPPA (US)
    - GDPR Article 8 (children's consent)
    - 5Rights Foundation design principles
  failure_mode: >
    Audit clears privacy and fairness gates but
    misses grooming risk, age-inappropriate
    monetization patterns, or absence of
    parental-consent flows; harm lands on
    children and draws regulatory and media
    response the sponsor cannot survive.
  minimum_scope_binding: >
    One pass evaluates age-appropriate design
    against applicable code(s), inspects
    grooming-risk surfaces (adult-minor contact
    channels, private messaging, user-generated
    content), and verifies parental-consent and
    age-verification patterns where required.
```

### Pack 6 — Physical context

**Trigger:** `predicate: device, sensor, location, bandwidth, or real-world environment materially changes behavior or risk`

```yaml
- id: LL-D-014
  name: Does context matter?
  material_question: >
    Do device, browser, network, location, or
    real-world use conditions materially change
    safety, usability, or performance?
  tier: domain
  trigger: >
    predicate: outcome quality or risk changes
    materially by device, browser, network,
    location, or physical environment
  evidence_class: probe
  specialist_type: field-conditions QA / real-world-testing analyst
  rubric_anchor: ~
  informed_by:
    - ISO/IEC 25010:2011 (context of use)
  failure_mode: >
    Audit signs off on desktop or lab behavior
    that breaks in the conditions where the
    subject is actually used.
  minimum_scope_binding: >
    One pass tests representative environments
    or explicitly justifies why context
    variation is immaterial.
```

---

## Summary counts

- **Total entries:** 26 (5 universal + 21 domain across 6 packs)
- **Rubric-anchored entries:** 2 (7.7%) — LL-D-002 (WCAG 2.2, October 2023), LL-D-005 (OWASP ASVS 5.0.0, May 2025)
- **`recommended_sources:`-bearing entries:** 2 (7.7%) — LL-D-008 ("Compared to what?"), LL-D-009 ("Does it pay back?")
- **`scope_integrity_probe:`-bearing entries:** 1 (3.8%) — LL-D-008 ("Compared to what?")
- **`specialist_type:` population:** 26 / 26
- **`last_verified:` population on anchored entries:** 2 / 2 (all dated 2026-04-24)
- **`verification_basis:` population on anchored entries:** 2 / 2 (all `schema-introduction-only` at v0.10; flips to `independent-review` after real currency review)

## Version and status

**v0.15 pre-release.** Awaiting at least one real-world calibration application before promotion to v1.0 stable. Calibration may occur either as standalone use on a real audit or through a framework-integration (Phase B) effort against a committed target audit framework.

v0.15 is an additive catalog bump on top of v0.14: two new domain lenses and one amended lens, no schema change. It broadens LL-D-019 ("Who said otherwise?") from negations alone to the full uninvited-frame family — negations, defensive intensifiers ("real", "actual", "truly"), and temporal hedges ("for now", "currently") — with a fast path for self-bounding verbs (a verb like "shrink" already bounds the claim, so a trailing denial of the unbounded case is uncalled-for by default) and an exception for sections whose explicit job is worst-case assessment, where the extreme is a called question. It adds LL-D-020 ("Help or ammunition?"), a per-sentence triple audit that reads a deliverable as its named expert audience reads it — sense, clarity, and effect for the subject, recomputing any implied arithmetic under a hostile-but-fair posture — and LL-D-021 ("Does a stranger follow?"), a cold-reader pass requiring every referent to resolve on the page: third-party claims attributed, acronyms defined at first use, and the premises the document's logic depends on stated rather than assumed. Both new lenses carry the standard fields only, and existing lenses beyond LL-D-019 are untouched. Total entries 24 → 26 (5 universal + 21 domain).

v0.14 is an additive catalog bump on top of v0.13: one new domain lens, no schema change. It adds LL-D-019 ("Who said otherwise?") to Pack 1 — a document-review lens that audits negation targeting in prose deliverables. Every negation must answer a live alternative the reader demonstrably brings (a common prior, a named risk, or an inference the document's own content invites); a denial of a belief nobody holds plants the very frame it denies, reads as defensive, and implies a critic nobody heard from. The lens carries the standard fields only — no rubric anchor, no recommended sources, no scope-integrity probe at introduction — and existing lenses are untouched, so v0.14 introduces no behavior change for them. Total entries 23 → 24 (5 universal + 19 domain).

v0.13 is an additive schema bump on top of v0.12: same 23 lenses, same triggers. It adds the optional `scope_integrity_probe:` field, which carries a sharpened, lens-specific falsifier an adopting framework poses at coverage time to test whether `minimum_scope_binding:` was genuinely satisfied rather than waved through. The field is populated on one lens (LL-D-008 "Compared to what?", whose category-vs-audience substitution trap has a ground-truth worked miss) and absent on the rest. Like `recommended_sources:`, it is optional and backward-compatible: entries without it remain valid and fall back to the generic scope-completeness challenge derived from `minimum_scope_binding:`, so v0.13 introduces no behavior change for existing lenses.

v0.12 is an additive schema bump on top of v0.11: same 23 lenses, same triggers. It adds the optional `recommended_sources:` field, which attaches a framework-curated list of external reference sources — each with a mandatory `framing:` and `recency:` caveat — to the lens's material question. The field is populated on two high-yield lenses (LL-D-008 "Compared to what?" and LL-D-009 "Does it pay back?") and absent on the rest. Like `rubric_anchor:`, it is optional and backward-compatible: entries without it remain valid, so v0.12 introduces no behavior change for existing lenses.

v0.11 is a lens-binding refinement on top of v0.10: same 23 lenses, no schema change. It sharpens LL-D-008 ("Compared to what?") to name the category-vs-audience substitution trap in `failure_mode`, and tightens `minimum_scope_binding` to require naming the audience and job before enumerating comparators — substitutes defined by the job, not the product category. The refinement is posture-facilitation, motivated by a real audit that reached a false-uniqueness finding after enumerating category-bounded rivals while an audience-defined substitute went unnamed.

v0.10 is a schema-fidelity bump on top of v0.9: same 23 lenses, same content, same triggers. The change is the addition of `verification_basis:` on the two rubric-anchored entries, gating any adopting framework's freshness logic against silently treating schema-introduction dates as performed currency checks.

Feedback, patches, and field-observations welcome. Ongoing currency of rubric anchors is the responsibility of the adopting framework or engagement; v0.15 ships with anchors current as of 2026-04-24 (`schema-introduction-only` basis) and does not include an automated currency-update mechanism.

*End of PRISM Lens Library v0.15.*

---

## Appendix H — Vendor parsing observations
<a id="appendix-vendor-parsing-observations"></a>

`[methodological | review-if: release-sweep | recommended]`

This appendix records empirical observations of how dispatched-content
vendors handle PRISM-shaped inputs (envelopes, atomic prompts, attached
artifacts). Entries are observations, not specifications: a status like
`stripped` documents what was seen on a given date, not what a vendor
guarantees. The appendix is consulted at dispatch time when shaping
envelopes for a target vendor and at release-sweep time to re-test stale
entries.

**Status taxonomy.** Status column values are drawn from a closed
vocabulary:

- **passthrough** — vendor preserves the content as-is.
- **stripped** — vendor removes the content silently from inputs (paste,
  upload, web fetch).
- **mangled** — vendor preserves the content but alters it in transit
  (re-encoding, restructuring, character substitution).
- **error** — vendor returns an error or refuses to process the content.
- **not-tested** — no observation on record; placeholder when other
  vendors in the section have entries.
- **observed-once** — single anecdotal observation; not generalizable;
  the entry exists to mark a sighting for follow-up confirmation.

**Maintenance protocol.** Entries are append-only between releases. Any
orchestration session that surfaces a vendor parsing gap creates a new
entry (or updates an existing one) under the relevant content-type
heading. At each MINOR or MAJOR PRISM release, entries with an `Observed`
date older than twelve months are re-tested or annotated `† stale`. The
appendix's maintenance surface is shared with the cross-vendor adaptation
workstream; contributions from that workstream land here as new H3
sections (new content types) or new rows in existing tables (new vendor
observations for an existing content type).

**Per-content-type sections.** Each content type is a separate H3
sub-section so per-vendor tables stay narrow and mobile-readable. New
content types are added as new H3 sections rather than as additional
columns in an existing table.

### Markdown / YAML fences in mobile-paste inputs

Behavior when an envelope sent via the mobile-app *paste* input path
contains fenced Markdown or YAML blocks (` ``` ` / `---`).

| Vendor | Status | Observed | Workaround |
|---|---|---|---|
| ChatGPT (mobile paste) | stripped | 2026-05-15 | Treat mobile paste as an unsupported input path for fenced content. Inline-expand per §{section.atomic-prompt-self-containment}; verify the envelope as received before relying on contract structure. |
| Perplexity DR | not-tested | — | — |
| Gemini DR | not-tested | — | — |
| Claude Research | not-tested | — | — |

The ChatGPT mobile observation prompted §{section.atomic-prompt-self-containment}
in v2.0.2: inline-expanded definitions of PRISM shorthand inside the
dispatched prompt body ensure semantic integrity even when fences are
silently dropped in transit. The `not-tested` rows are placeholders;
re-test at the next release sweep or when a session next dispatches
fenced content via mobile paste on those vendors.

### Per-vendor download / export recipes

The return-handling friction is per-vendor; pre-warn the operator (an operator
hint, not an inline essay). Observed recipes:

| Vendor | Recipe |
|---|---|
| Gemini (Deep Research) | Export to Google Docs → download as `.md`. |
| Claude / ChatGPT | The session creates the file; rename the download to the SP-14 name (rename optional — the return self-IDs via `Ran on`, reconciled on the filename). |
| Grok | Writes the file to its sandbox (e.g. `/home/workdir/artifacts/`); after it saves, ask "give me a download link" to surface the `.md` — a two-step. |

These are observations, not guarantees; re-test stale entries at the release
sweep.

### Passive detection of self-report — capability + template

For the passive pre-fill pattern (§{section.corpus-access-dispatch}, *Passive
pre-fill of self-report*): the load-bearing choice is **naming the right
capability**. Passive recon is a **browse / retrieval** job — name the
Chrome-MCP / authenticated-browse surface (§{section.cowork-surface-capabilities})
plus public web records (DNS, certificate-transparency, IP-WHOIS, app-store),
per the retrieval-shape step (§{section.vendor-selection-at-dispatch}). Do
**not** route it to a synthesis / Deep-Research mode — that silently fails to
fetch. Generalized paste-ready shape:

```
Using the Chrome MCP (authenticated browse) and online web tools, passively
examine and detect as much as possible about [subject]'s stack, server
environment, and [domain of interest], and pre-answer as many of the pending
[questionnaire / self-report] items as passive observation allows. Tag each
finding [OBS] (observed first-hand) / [INF] (inferred from observed signals) /
[ask] (not passively knowable). STRICTLY passive: no scanning, no ID/parameter
manipulation (IDOR), no rate-limit / auth-bypass / upload testing, no
state-changing actions; read key *names*, never token *values*.
```

### Agentic-browser drivers + closed-document IVD seats

**Agentic-browser drivers (Comet, Atlas).** Operator-run third-party agents are
a distinct driver class from PRISM-driven Chrome-MCP
(§{section.vendor-selection-at-dispatch}); investigation-posture single-source,
never a triangulation seat. Reliability is uneven and confident prose is **not**
verified output — every claim needs first-hand confirmation (field: agents
variously asserted no-RSVP / "responsive" / "real labels", each wrong; a probe
asserted "iOS-only", also wrong). Confirm agent-mode + login are actually
engaged before relying on a run.

**Closed-document IVD seats (§{section.independent-validation-dispatch}).** For a
closed-document validation (the deliverable's own arithmetic and internal
consistency, no web), prefer **strong closed-document reasoners** as seats; in
field runs the real in-document catches came from those, while web-oriented /
breadth-first seats produced mostly already-addressed or stylistic items on the
closed-document task. Accept a valid catch from any seat (recall is the point),
but weight a web-oriented seat's *miss* on a closed-document point lightly — its
strength is live-web breadth, not closed-doc recompute.

### HTML → PDF transform hazards for deliverable builds

The engagement report's primary form is single-file HTML rendered to PDF (the
presentation house-style, §{appendix.report-architecture}). Field-observed render
hazards on a WeasyPrint-class HTML→PDF engine — pre-warn for them when building or
validating a PDF deliverable:

- **Flex translucent-background double-paint.** A flex container with a
  translucent background can paint its background twice (parent + item), darkening
  the intended tint. Put the background on a single layer, or use an opaque value.
- **Flex `space-between` title mis-size.** A `justify-content: space-between` title
  row can mis-size or clip its items in the PDF engine where it renders fine in the
  browser. Verify titles in the rendered PDF, not only the browser preview.
- **`@page` vs `html`/`body` background mismatch.** The `@page` background and the
  document background are separate; setting one and not the other leaves a margin
  band in the off colour. Set both, or neither.
- **Real page hierarchy on flat HTML.** A flat HTML document has no native pages —
  use explicit `@page` rules + `page-break-inside: avoid` / `break-before` to force
  a real cover / section / page structure, and embed fonts so the PDF is portable.
- **Orphaned media on slide / section delete.** Deleting a slide or section from a
  built deck or document can leave its media embedded; rebuild from the kept
  content rather than deleting in place, and content-hash-verify the removed media
  is gone (the §{appendix.external-share} image-redaction procedure depends on
  this).

Pair these with the §{principle.SP-18} deliverable-transform guard
(§{section.sp-18-it-must-recompute}): tokenize standalone figures only (exclude
acronym / code digits; strip tags first) so a clarity edit during the transform
does not trip a false figure-drift halt.

---

## Appendix I — Lanes, roles, PRISM UI, and Setup onboarding (reference)
<a id="appendix-lanes-roles-prism-ui"></a>

Reference-grade detail for the operating model
(§{section.lanes-roles-and-the-prism-ui}) and Setup onboarding
(§{section.setup-onboarding-and-mode-selection}). The rules are in those
sections; this appendix is the matrix, the UI rendering, the trajectory-view
reference, and the onboarding artifacts. In the Skill archive it is the
`reference/lanes-ui.md` bundle, fetched when lanes / Desk / UI / onboarding
work is in front of you.

### I.1 The role × context-tier matrix

Context-tier = PRISM-loaded *orchestration* vs clean *execution*. Role and
tier are independent axes — a convergence run is an orchestration-*class* role
run in a clean execution-*style* context.

| Role | Context-tier | Anchored to |
|---|---|---|
| Setup | orchestration | the seven probes (§{section.setup-mechanics}) |
| Planner/Steward (the PRISM Desk) | orchestration | the *What's next* pointer + the drain (§{section.cross-lane-inbox}) |
| Dispatch-builder | orchestration | Vendor Selection (§{section.vendor-selection-at-dispatch}) + the Envelope (§{section.prism-execution-envelope}) |
| Dispatch-consumer | orchestration | Layer-1 absorption + reconciliation + the Master write |
| Execution-run | execution | the self-contained dispatched prompt (§{section.two-session-types}); PRISM-unaware by design |
| Convergence-run | execution-*style*, orchestration-*class* | clean-session Vendor Triangulation (§{section.vendor-triangulation}) |
| Validation-run | execution | the Independent Validation Dispatch (§{section.independent-validation-dispatch}) — adversarial, deliverable-only, distinct-vendor |

The meta lane has its own roles (reflection / synthesis / worksheet-building).

### I.2 Isolation — inline, session, or sub-agent

A session that chooses to separate has three options: **inline** (when the
work is light), **a separate session** (for a durable handoff), or a
**clean-context sub-agent** (the default when the holding session is
contaminated — see §{section.roles-context-tier}). Sub-agent bounds: clean
context but same distribution (§{principle.SP-15}) — a converger or clean
reader, never a triangulation seat. Hand it return-paths + method only; it
reads returns from `outputs/` by path and writes back to `outputs/`; the
parent absorbs and writes canonical state.

### I.3 The PRISM UI — rendering detail

The three surfaces (STATE / HEALTH / ACTION) and the make-it-a-real-UI
discipline are in §{section.prism-ui}. Rendering specifics:

- **Consistency.** The visual language is stable round-to-round; mode is
  operator-selectable but the component schemas do not silently change between
  renders.
- **Colored status encoding** (operator-liked): complete · you-are-here ·
  pending · critical-path · decisive.
- **Code → real-name legend.** The view carries a legend translating pass
  codes (e.g. `A11`, `R1`, `T1`) to their real objectives, rendered from the
  live Master's Prompt Strategy and Dispatch register — not re-transcribed.

### I.4 The trajectory STATE view — two modes (operator-reviewed reference)

The STATE view has **two modes answering different questions**, shown **side
by side, each in its own form — not fused** into one diagram:

- **Dependency / critical-path map** (an "engagement map"): rounded-rectangle
  nodes top→bottom with explicit fork / join arrows; a dedicated critical-path
  + bottleneck callout; a status / role legend. Optimized to show
  **structure** — what gates what, what runs in parallel, where the bottleneck
  is. The decision-relevant view when the engagement is blocked on one external
  event.
- **Progress timeline**: a single vertical spine with one status dot per node
  (● complete · ◉ you are here · ○ pending), a nested sub-box for parallel
  legs, a dashed "not on this trajectory" aside. Optimized to show **sequence +
  status** — where am I, what's done. Cleaner at a glance; lower-information at
  a blocked / branching phase.

Operator inputs that shaped this: liked both renders and wants both (side by
side, not converged); liked the colored encoding; wants the code → name legend
on the view; wants the visual language stable round-to-round. The Builder owns
the final rendering; this records the reviewed inputs.

### I.5 Setup onboarding — the SI template and install cards

**The framework SI template** is a generic skeleton with native-construct
references + typed config slots, shipping with the SI version machinery baked
in (`SI version` + changelog). Filling it yields a complete lean SI with zero
boilerplate re-authoring.

- **Native-construct sections (one-line references):** persistence
  (`repo_backed`, §{section.repo-backed-mechanics}); resume protocol;
  commit-discipline + the cross-lane inbox (§{section.cross-lane-inbox}); lanes
  / roles / the Desk (§{section.lanes-roles-and-the-prism-ui}).
- **Per-subject slots (Setup fills):** subject + decision tracks; repo + work
  folder; surface registry (the two-project model on Cowork — orchestration +
  execution); credential location (PAT path) + redaction regime;
  engagement-specific standing directives, **embedded verbatim**.

**The project-create + install card** (one per surface; the operator-guide
schema, plain-language WHERE / WHAT / RESULT):

- **Create the project(s)** — two on Cowork (orchestration: SI installed,
  core-load enforced, hosts Desk + Meta; execution: SI-less, memory-off,
  organization-only, working folder separate from the orchestration mirror).
  Automatable vs guidance-only is surface-dependent — default guidance-only,
  automate where a surface allows.
- **Install the SI** — the full SI as a single wholesale-paste block ("Project
  instructions, not a chat; paste the WHOLE thing"); never a splice.
- **Drop the PAT** — guidance to place the credential in the per-surface
  location; guidance-only, never handled by the session.
- **Seed the repo** — the work-folder layout + first commit (or confirm the
  repo exists).
- **Re-issue on change** — any later SI change ships as a full replacement for
  wholesale paste on every surface; the resume-time version reconcile is the
  drift detector.

### I.6 Quick mode — the mini-Setup procedure

The shape and the kept / dropped split are in
§{section.setup-onboarding-and-mode-selection}. Concretely:

1. **Frame (≤ 2 lines):** audience + the decision this serves. If this cannot
   be stated, the task is under-specified — surface it, don't proceed on a
   guess (SP-9, §{principle.SP-9}).
2. **Lite lens pick:** name the handful of lenses that bear; note any
   deliberately out of scope (one line each). No coverage-saturation loop.
3. **Fan out** clean-context sub-agents per strand; assemble grounding facts.
4. **Apply the output gates** (SP-16 / SP-17 / SP-18) to the assembled
   deliverable.
5. **Deliver** one self-contained artifact (SP-20); no repo write-back. If it
   grows into a real engagement, graduate per
   §{section.setup-onboarding-and-mode-selection}.

## Appendix J — Dispatch conventions (reference)
<a id="appendix-dispatch-conventions"></a>

Reference-grade detail behind the dispatch lifecycle
(§{section.dispatch-lifecycle}). The lifecycle's *rules* live in the core
sections; this appendix is the battle-tested recipe set the stages draw on,
plus the **promotion map** that records where each convention's rule landed —
so a working, field-proven convention set does not orphan as the framework
absorbs it. Entries are practice distilled from live dispatch rounds; consult
it when building or converging a dispatch.

### J.1 Promotion map — convention → framework home

Each item is **REFERENCE** (already core — cite it), **PROMOTE** (battle-tested
local practice lifted into the framework), or **PROMOTE-OR-DECIDE** (a
divergence sanctioned as an option or kept documented). Where a convention's
local practice and core diverged, the verdict follows the dispatch-lifecycle
source.

| Conv | Item | Disposition → framework home |
|---|---|---|
| A.1 | Single-arm self-contained paste (vendor unaware it is 1 of N) | PROMOTE → §{section.atomic-prompt-self-containment} — strip the orchestration machinery; arm-count is orchestration-side |
| A.2 | Inline small + available; attach large / not-yet-produced | PROMOTE → §{section.atomic-prompt-self-containment} composition guidance |
| A.3 | 3-way pre-flight: INPUT halts · SUBSTRATE declares · ANALYSIS proceeds | REFERENCE/PROMOTE → the Self-check (§{section.prism-execution-self-check}); the completeness limb of INPUT is operationalized as the **Step 0** transport-integrity check (§{section.transport-integrity-bracket}); "only INPUT may halt" preserved |
| A.3a | Transport-integrity bracket — truncation guard (top anchor + terminal sentinel) | PROMOTE → §{section.transport-integrity-bracket} (Self-check Step 0; template §{appendix.prism-prompt-integrity}) |
| A.4 | Lean delimited output signature beats prose | REFERENCE → the delimited Output signature (§{section.prism-execution-output}) is already the standard (empirical: ━━━ got 4/4 vendor adherence, prose 2/5) |
| A.5 | Per-seat mode + live currency at dispatch | REFERENCE → §{section.vendor-selection-at-dispatch} |
| A.6 | No bare PRISM shorthand in the paste | REFERENCE → §{section.atomic-prompt-self-containment} |
| A.7 | Per-vendor download / export recipes | PROMOTE → §{appendix.vendor-parsing-observations} |
| B.8 / B.8a | Converge in a dedicated clean session / clean-context sub-agent | REFERENCE → §{section.roles-context-tier} (seam-③); converger only, never a triangulation seat (§{principle.SP-15}) |
| B.9 | Adversarial review = Independent Validation Dispatch | REFERENCE → §{section.independent-validation-dispatch}; sharpened to "distinct from all N producers" (§{principle.SP-15}) |
| C.11 | Plain words to the operator | REFERENCE → §{principle.SP-17} |
| C.12 | Repo / write discipline (rebase-on-tail, commit-only-own, identity-before-commit) | engagement SI + the cross-lane inbox (§{section.cross-lane-inbox}); the repo mechanics are maintainer-protocol, not framework body |
| D.13–15 | Paste-as-own-file · fixed-schema operator card · in-paste guardrails | PROMOTE → the Stage-2 dispatch card (§{appendix.outbound-dispatch-card}) within the dispatch lifecycle (§{section.dispatch-lifecycle}) |
| E | Canonical execution-paste model (bookended ━━━ blocks) | REFERENCE → the reference paste shape, an instantiation of the atomic template (§{section.template-shape}); J.2 below |
| F.16–19 | Recon: probe-spine + one explore-agent; retrieved-vs-inferred; recon output discipline; agentic-browser driver class | PROMOTE → §{section.prompt-body-convergence-provisions} (finding basis) + §{section.vendor-selection-at-dispatch} (driver class) + §{appendix.vendor-parsing-observations} |
| G.20–22 | Match dispatch mode to retrieval shape; capture-then-attach; capability-null ≠ substantive-null | PROMOTE → §{section.vendor-selection-at-dispatch} retrieval-shape step |
| H.23–25 | Passive pre-fill of self-report; provenance tags; passive-only ethics | PROMOTE → §{section.corpus-access-dispatch} (passive pre-fill) + §{appendix.vendor-parsing-observations} (template) |

### J.2 Canonical execution-paste model (reference shape)

The reference shape for the execution unit a Stage-3 dispatch sends: **two lean
delimited `━━━` blocks bookending the task body**, all inside one fenced block,
themselves wrapped by the transport-integrity bracket
(§{section.transport-integrity-bracket}) — the `PRISM PROMPT INTEGRITY` anchor
above and the terminal sentinel below, transport framing rather than contract
blocks — with the operator dispatch card (§{appendix.outbound-dispatch-card})
rendered above the whole paste. It is an instantiation of the atomic template
(§{section.template-shape}), not a replacement: it restores the delimited
*inbound* structure (the Self-check, §{section.prism-execution-self-check}) that
a prose pre-flight loses, and keeps the delimited *outbound* signature (the
Output, §{section.prism-execution-output}).

- **Inbound — Self-check (§{appendix.prism-execution-self-check}).** Carries the
  3-way pre-flight: **INPUT** check is the *only* place the vendor may halt —
  completeness is the terminal-sentinel presence + Dispatch-ID match (Self-check
  Step 0, §{section.transport-integrity-bracket}); are named files present +
  readable?; **SUBSTRATE**
  declares mode + best-effort model and proceeds; **ANALYSIS** proceeds on
  defaults, recording any under "could not verify," never asking the operator.
- **Body.** Self-contained context (inline small + available priors, attach
  large / not-yet-produced), task, method (recompute — do not trust —
  arithmetic), output structure (the finding shape,
  §{section.prompt-body-convergence-provisions}), success criteria.
- **Outbound — Output signature (§{appendix.prism-execution-output}).** The
  vendor wraps its findings in the `━━━ PRISM EXECUTION OUTPUT ━━━` block and
  copies the `Dispatch ID` and `Prompt digest`/`Reference` lines verbatim.

Use `━━━` heavy-line delimiters, never triple-backtick fences, for the paste's
internal blocks — they are fence-safe, so the whole paste survives inside one
outer fenced block when rendered to the operator.

### J.3 Digest preimage — pin for re-stage reproducibility

The copy-through digest (§{section.prism-execution-output}) is only reproducible
on a **re-stage** if its preimage is pinned exactly: the byte scope is the
content between the paste fences, with the Envelope's (and Output's) `Reference:`
/ `Prompt digest:` line set to the sentinel `sha256:PENDING`, the
transport-integrity bracket (§{section.transport-integrity-bracket}) — the
`PRISM PROMPT INTEGRITY` anchor block in full and the terminal
`━━━ END PRISM DISPATCHED PASTE` sentinel — **excluded** from the byte scope as
transport framing, and **no trailing-newline normalization**. (The bracket is
*excluded*, not normalized — its own `Prompt digest:` line is display-only and
never enters the preimage; this differs from the `Reference:` line, which is
*included-with-value-blanked*.)
An unpinned preimage stays deterministic and consistent *within* a session, but
a later session that wants to re-stage the same dispatch and preserve the
original digest cannot reproduce it — the field catch behind this rule. The
digest pairs with the **Dispatch ID**
(§{section.recommended-vs-executed-reconciliation}): the digest verifies body
integrity, the Dispatch ID identifies the dispatch instance; together with the
operator-set filename they are the reconciliation triple.

## Appendix K — Report architecture (reference)
<a id="appendix-report-architecture"></a>

Reference-grade detail behind the engagement deliverable — the comprehensive
final report, the interactive workbook, and the presentation house-style. The
*rules* (the report is the deliverable of record; the close-time disciplines)
live in the closure gate (§{section.engagement-closure}) and the Decision brief
(§{section.decision-brief}); this appendix is the report skeleton, the craft
conventions, the workbook cockpit pattern, and the reconcile-at-close checklist.
In the Skill archive it is the `reference/report-architecture.md` bundle, fetched
when building or closing an engagement deliverable.

### K.1 The comprehensive final report — the deliverable of record

Every engagement concludes with **one comprehensive final report** reflecting
**all** the work — every dispatch-register pass / evidence area — in plain
English, optimized for **executive scanning**: a tight readable body + curated
appendices, never a thin verdict-only or summary-only close. A summary-only
close strands the engagement's real value (the per-pass findings, data, tables)
in internal artifacts the audience never sees and under-represents the work; the
report is the engagement's deliverable of record and must carry the whole
engagement. Conventions:

- **One report per engagement, all work reflected.** Every dispatch-register
  pass / evidence area appears; nothing material is left only in the Master or
  `outputs/`.
- **Plain English, executive-scannable (§{principle.SP-17}).** Verdict +
  decision up front; clear headings; summary-first; skimmable. Built for the
  decision-maker / client audience, assumed non-PRISM — jargon stripped, with a
  glossary; each edition self-contained (§{principle.SP-20}).
- **Tight body + comprehensive curated appendices.** A readable main body plus
  one appendix per pass / evidence area — **comprehensive in coverage, curated
  in form** (plain language; actual findings / data / tables, not one-line
  glosses). The body cross-references each appendix; a heavy artifact lives in
  full in its appendix with a compact version + cross-ref in the body.
- **Build discipline (heavy pass).** Fan out clean-context sub-agents, one per
  appendix (§{section.roles-context-tier}) — each returns a curated,
  citation-bearing section; the parent owns the spine + cross-links. Build →
  render → validate are clean migration seams (manage the context band).
- **PRISM attribution — a linkable credit.** The report cover / method line
  names PRISM as the method and **links it to the framework repo** (a "Created
  with PRISM" credit that both attributes the work and gives the reader a path
  to the framework) — on **every** report, not only the share-archive Index /
  README.
- **Methodology & disclosures (plain-language "how we worked").** A body section
  that translates the framework's rigor into audience-facing trust: multi-vendor
  reconciliation (verdict-critical passes run on several independent systems,
  agreement *and* divergence recorded — §{principle.SP-15}); independent
  validation (a separate reviewer whose only context is the deliverable, with a
  from-scratch recompute — §{section.independent-validation-dispatch});
  findings vs scenarios kept strictly separate (a verified finding vs a fenced
  modelled scenario — §{principle.SP-18} + §{section.prompt-body-convergence-provisions});
  evidence and confidence as separate axes
  (§{section.prompt-body-convergence-provisions}); and interim-by-honesty (gaps
  marked open, not filled with assumption, with exactly what closes each —
  §{principle.SP-12}).
- **Validation target.** The artifact the Independent Validation Dispatch
  (§{section.independent-validation-dispatch}) validates is the **complete**
  report (body + appendices), not a summary; the complete report is also what the
  close shares.
- **Version discipline (bump atomicity for deliverables).** Every content change
  to the versioned report — *including cosmetic and text corrections* — bumps its
  revision (§{section.bump-atomicity-routine}); the **shipped revision must equal
  the validated revision**; keep exactly one current file per revision. Front-load
  the disambiguating version token in the filename so a file-picker "…" truncation
  cannot hide it (the session-name front-loading principle generalized to
  filenames).

### K.2 Canonical body architecture (verdict-first)

The recommended default skeleton — adapt section names per engagement:

1. **Title + cover / meta block** — a plain-language title (a sentence, not a
   code), "Prepared for", date, and the method / attribution line (the PRISM
   credit, K.1).
2. **Table of contents.**
3. **"How to read this report"** — a short reader-onboarding.
4. **Executive summary — verdict FIRST:** the decision(s) under test, the verdict
   on each, and the single most-important fork in one line.
5. **Highlights band** — an at-a-glance strip of the landscape + key findings.
6. **One body section per decision track / major question** — each running
   *decision under test → verdict → risk register leg-by-leg → supporting
   picture*; heavy artifacts appear compact with a cross-ref to their full
   appendix.
7. **Open items — and how the reader's answers move the verdict**
   (interim-by-honesty made actionable).
8. **Update path** — what closes each open leg / how the report reaches final.
9. **Methodology & disclosures** (K.1) — with a **conflict-of-interest**
   sub-section and a **scope & limitations** sub-section.
10. **Appendices** — the methodology / registers appendix **first** (below), then
    one appendix per pass / evidence area.

**The methodology / registers appendix ("how this was built").** Exposes the
PRISM scaffolding in plain language as a dedicated lead appendix: the **four Setup
artifacts** (§{section.setup-artifacts}) — decision brief, stakeholder register,
claim inventory, jurisdiction map — plus the **Decision-brief falsifier
registers**, a fuller **Methodology**, a **conflict-of-interest disclosure** (the honesty controls,
stated **positively** — §{principle.SP-16}), an **evidence & source index**
(every research pass → its provenance), and a **glossary**. Turns the audit's own
rigor into audience-facing trust instead of leaving it in the Master.

### K.3 Craft conventions

Each recurred throughout the finished engagement report; codified so a future
report carries them by construction, not by re-derivation:

- **Per-section "in one breath" takeaway.** Every verdict, finding, and dense
  appendix opens with a one-sentence plain takeaway — section-level
  executive-scannability, distinct from the document-level summary-first rule.
- **"How to read this …" orientation on every complex artifact.** The report,
  each dense appendix, and each notation system open with a brief orientation; a
  reader is never dropped into a dense table or a glyph system without a legend.
- **A published status-glyph legend (the "Harvey balls").** A consistent visual
  vocabulary — ● full / yes · ◐ partial · ○ none — for capability / coverage /
  severity, **always** introduced with its legend on first use and decoded again
  in the glossary. Two qualifiers ride alongside and stay **separate axes**
  (§{section.prompt-body-convergence-provisions}): **Confidence** (LOW / MEDIUM /
  HIGH) and **Verification status** (verified / could-not-verify). Evidence-vs-
  confidence separation is not merely stated; it is rendered.
- **Findings vs. scenarios fenced VISUALLY.** Every modelled / simulated figure
  carries a visual scenario tag, so a modelled number cannot be misread as a
  finding at a glance — the visual-channel complement to the §{principle.SP-18} /
  §{section.prompt-body-convergence-provisions} discipline, and the positive
  production-side home for the visual-polarity channel §{principle.SP-16} names.
- **Visible recompute as a reader-facing trust signal.** The report shows its
  arithmetic and structural checks ("the boundary count: 11 = 6+2+1+2,
  recomputed") — turning the §{principle.SP-18} internal gate into a credibility
  move: a recomputed total is stated *with* its recomputation, not merely
  asserted.
- **A self-decoding glossary.** Defines not only domain jargon but the report's
  own notation — the risk legs, the trust-boundary terms, the audit passes by
  name, the label glyphs — so the deliverable is self-contained for a non-PRISM
  reader (§{principle.SP-20}).
- **Compact-in-body / full-in-appendix for every heavy artifact**, with an inline
  cross-reference tag (the body carries the read-off; the appendix carries the
  full table).

### K.4 The interactive engagement workbook (the cockpit)

When the decision turns on a **quantitative, operator-tunable core** — unit
economics, a threshold / corner case, a returns or break-even model, a
sensitivity surface — deliver the finding **also** as a live, operator-drivable
workbook: the report *states* the finding; the workbook lets the decision-maker
*explore* it against their own numbers. The trigger is narrow — at most one
workbook per engagement, on the central quantitative gate; skip it for a
qualitative decision (a workbook there is ceremony). The earned pattern:

- **Dashboard / cockpit (the one sheet the audience drives):** a small set of
  clearly-marked **editable input cells** (the operator-tunable assumptions only)
  + the engagement's **live decision gate** — the Decision brief's actual gate
  (§{section.decision-brief}), evaluating its conditions in real time, color-coded
  (green in / amber edge / red out) — + live results. It **opens at the report's
  actual case**, so it reconciles with the report on open (same gate state, same
  headline figures).
- **Supporting sheets — the finding unpacked, made live:** break-even by the
  decision's key driver; a sensitivity heat-map across the two assumptions that
  matter most (with the report's case cell outlined); and any cost / driver
  model. Each is the report's analysis made tunable.
- **Read Me** (plain-language, with guided "try this" nudges so the audience
  drives it without instruction — §{principle.SP-17}) + **Notes & Sources** (full
  provenance: every figure tied back to the report / Master).
- **Correctness contract (§{principle.SP-18}).** Every cell ties back to the
  report and re-verifies after recalc; the workbook reconciles exactly with the
  report on open; zero formula errors.
- **Posture.** A derived share artifact — operator-gated (present it; record its
  existence in the Master / *What's next*; do not auto-commit), the same posture
  as the report / archive. It joins the send-bundle (the share-modes' send shapes,
§{appendix.external-share}); it is **not** a substitute
  for the report.

### K.5 Presentation house-style (the deliverable's visual form)

Presentation is a quality axis run at close — a **closure convention, not a
Standing Principle**. The deliverable's visual form carries the same care as its
text:

- **HTML primary** (single-file, inline CSS — reads better, portable) → **PDF
  done well**: embed fonts; explicit `@page` rules + `page-break-inside: avoid` /
  `break-before` for a real page hierarchy on flat HTML; a cover page; a TOC for
  long documents; running headers / footers + page numbers.
- **Design language inspired by the engagement subject's own design system**,
  captured during reconnaissance and used at close (cross-pass inheritance).
- **Two caveats.** (1) **Order** — polish only a **validated** deliverable
  (§{principle.SP-18} / the Independent Validation Dispatch first); never beautify
  an unvalidated artifact. (2) **Inspired, not impersonating** — keep PRISM's own
  identity clear so the deliverable reads as an independent audit, not the
  subject's own self-assessment (form must not imply a false source).
- **Render hazards.** HTML→PDF transform hazards, and the §{principle.SP-18}
  standalone-figure tokenization guard for deliverable transforms, are in
  §{appendix.vendor-parsing-observations}.

### K.6 Reconcile-at-close (the codification sweep)

The discipline's *rule* is a closure-gate step (§{section.engagement-closure},
Layer 2); this is its checklist. At every engagement close, diff the finished
deliverable's structure and conventions against this appendix in **one** pass,
and codify every craft element that landed via production / operator polish but
is not yet here — the reference is reconciled against the deliverable of record,
not the reverse. This converts one-at-a-time manual catches (the
applied-but-not-codified pattern — a learning lands in an artifact, often via an
operator correction, without being codified so it recurs) into a standing
mechanism; its in-flight sibling is **catch-one → propose-a-sweep**, the standing
orchestration posture of offering a systematic pass when the operator flags one
instance. The sweep:

- [ ] Report follows the K.2 verdict-first architecture (cover → TOC →
  how-to-read → exec summary verdict-first → highlights → per-track sections →
  open items → update path → methodology & disclosures incl. COI + scope /
  limitations → appendices led by the methodology / registers appendix).
- [ ] Every verdict / finding / dense appendix opens with an "in one breath"
  takeaway; every complex artifact + notation system opens with a "how to read".
- [ ] Status-glyph legend published on first use + in the glossary; Confidence +
  Verification shown as separate axes.
- [ ] Modelled / simulated figures fenced visually; recomputed totals shown with
  their recomputation.
- [ ] Glossary decodes the report's own shorthand, not only domain jargon.
- [ ] Methodology / registers appendix exposes the Setup artifacts + methodology
  + COI + evidence / source index + glossary.
- [ ] PRISM linkable credit + the plain-language methodology & disclosures
  section are present.
- [ ] Shipped revision == validated revision (§{section.bump-atomicity-routine});
  exactly one current file per revision.
- [ ] Any craft element present in the deliverable but absent here is codified
  before the close completes.

## Appendix L — External share (reference)
<a id="appendix-external-share"></a>

Reference-grade detail behind the external-share close (§{section.engagement-closure})
and the canonical-source rule that §{principle.SP-8} carries. The *principle* —
the engagement is externally share-ready by close, and every consumer reads
canonical state — lives in those sections; this appendix is the share-archive
recipe, the operator-selectable share modes, the image-redaction procedure, and
the canonical-source handoff block. In the Skill archive it is the
`reference/external-share.md` bundle, fetched when preparing an external handoff.

### L.1 One repo per engagement, externally share-ready by close

Each engagement lives in (or splits out to) its **own** repository, externally
share-ready by close: an audience-facing README for non-PRISM readers (with the
"Created with PRISM" credit linking the framework repo), descriptive de-coded
artifact filenames as a presentation layer over §{principle.SP-14}, and a passed
privacy / PII-redaction review. Rationale: repository access is per-repo, not
per-folder — a multi-engagement umbrella cannot be shared with one engagement's
client without exposing the others *and* the entire commit history. An engagement
running inside an umbrella splits out at close (subtree split / history filter)
to its own repo, under the heavier external-share redaction regime (including any
carried history).

### L.2 The share archive (the default share artifact)

Rather than sharing a repository link, produce a self-contained **archive** of
the engagement — an easier and safer one-folder handoff (no account needed) that
curates exactly what is exposed:

- **A logical curated tree** — the findings Master · the independent-validation
  panel (§{section.independent-validation-dispatch}) · research passes (each with
  its convergence + per-pass validation) · source exhibits · methodology /
  dispatch envelopes · diligence instruments.
- **De-coded descriptive filenames** as a presentation layer over
  §{principle.SP-14}, with a name-map (friendly → canonical); the repo's
  canonical names stay unchanged.
- **A root `Index.html`** that frames the depth ("N independent AI validators
  reviewed the assessment — here is the complete evidence base"), links every
  artifact, and carries a read-me-first + a redaction note.
- **Expansive — to show the rigor.** Include the full work-product (all passes,
  the validation panel, envelopes, exhibits, the findings Master), precisely to
  evidence the depth of the work.

### L.3 Share modes (operator-selectable)

Three choices the operator sets per share; the image-redaction procedure (L.4) is
the standing **invariant** across all of them:

- **Persistence** — *present-only* (a derived artifact; record its existence, do
  not auto-commit) **or** *repo-committed* (the archive folder + the `.zip`
  committed to the engagement repo).
- **Report inclusion** — the final report (HTML + PDF) *in* the archive **or**
  shipped *separately*.
- **Send shape** — a *two-file* package (report + archive) **or** a fuller
  package (e.g. report PDF + developer action items + the interactive workbook +
  the archive ZIP).

### L.4 The image-redaction procedure (the invariant)

Redaction is **share-copy-only** — the repo's canonical artifacts are never
altered. A text grep cannot see PII inside an image, so screenshot / exhibit
material needs a **visual** pass:

1. Visually inspect every screenshot for member / third-party PII.
2. For a slide deck, **rebuild it from only the PII-safe screens** — do **not**
   merely delete slides, which leaves orphaned media embedded.
3. **Content-hash-verify** each removed image is absent from the rebuilt file.
4. Add a redaction-notice cover.
5. Then text-scrub names / affiliations / contacts and verify the scrub
   (`grep → 0`).

Credentials (a PAT, a `.secrets/` store) are excluded **absolutely**; framework
instrumentation (learnings / meta-learnings / state / the inbox) is a per-share
include / exclude choice, default exclude.

### L.5 Canonical source — read the repo, not the mirror

The canonical store is the engagement **repository**; a convenience
working-folder mirror **lags by construction** (a file committed to the repo is
not auto-copied to a flat mirror). A consumer — a Builder, an Independent
Validation seat, a fresh session — that reads the mirror instead of the canonical
repo can see stale / incomplete state and infer a false defect (e.g. "specs
undelivered" when the repo held them all along). So every consumer reads from a
**fresh repository clone**, never the convenience mirror, and runs a completeness
sanity-check on entry (a known artifact / file count, a manifest — "if you see
fewer than expected, you are on the stale mirror; re-clone"). This is the
read-side complement to write-side mirror staleness, and the application of
§{principle.SP-8} (canonical authority, §{section.sp-8-narrowed-canonical-authority})
to a multi-surface engagement.

## 18. Project, feedback, updates `[structural | stable]`
<a id="section-project-feedback-updates"></a>

PRISM is an open framework. This file ships with enough information to
locate the project, check for newer versions, and feed observations back
to the maintainer.

### 18.1 Project identity
<a id="section-project-identity"></a>

- **Repository.** `https://github.com/Ronkupper/PRISM`
- **Maintainer.** Ron Kuper ([@Ronkupper](https://github.com/Ronkupper))
- **Framework version.** v2.19.0 (this file)
- **Embedded Lens Library version.** v0.15 (Appendix G)
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
| Framework (this file) | `https://raw.githubusercontent.com/Ronkupper/PRISM/main/PRISM.md` | `…/PRISM_v2_19_0.md` |
| Lens Library | `https://raw.githubusercontent.com/Ronkupper/PRISM/main/lens/PRISM_lens_library.md` | `…/lens/PRISM_lens_library_v0_15.md` |
| Framework version stamp | `https://raw.githubusercontent.com/Ronkupper/PRISM/main/VERSION` | — |
| Lens version stamp | `https://raw.githubusercontent.com/Ronkupper/PRISM/main/lens/VERSION` | — |
| Releases index | `https://github.com/Ronkupper/PRISM/releases` | — |
| Release at this version | — | `https://github.com/Ronkupper/PRISM/releases/tag/v2.19.0` |

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

1. Read the attached framework's version (this file's header) and the
   embedded Lens Library version (Appendix G header).
2. If web access is available, GET the two `VERSION` endpoints from the
   repository's `main` branch. The endpoints return one line each.
3. Compare. If the published version is greater than the attached
   version on either track, surface a soft flag:
   `Framework v2.19.0 attached; v{published} available at {releases URL}.`
   `Lens v0.15 attached; v{published} available at {releases URL}.`
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
> (v2.19.0). https://github.com/Ronkupper/PRISM

---

*End of PRISM v2.19.0 framework operating document.*
