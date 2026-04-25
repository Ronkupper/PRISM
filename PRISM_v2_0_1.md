---
name: prism
description: "PRISM — structured multi-session, multi-vendor LLM-orchestrated audit and research framework. Currently v2.0.1. Trigger this skill whenever the user invokes PRISM mechanics by name or by recognizable construct: PRISM, PRISM audit, PRISM v2, begin a PRISM audit, Master file, any filename matching *_master_p*.md or *_starter_v*.md (v1.x), Prompt Strategy, Lens Library, Vendor Selection, Vendor Triangulation, Setup probes or any of P1-P7 by number, Monitor M* or any of M1-M12 by number, Standing Principle SP-*, Execution Envelope, Execution Self-check, Execution Output, Dispatch register, Dispatch shape (equivalence/split/limitation-named), the What is next artifact, context band or 🟢🟡🟠🔴, migration handoff, P0/P1 boundary, three-layer readiness, Claude Project recommendation, Update session, point refresh, Setup artifacts (Decision brief / Stakeholder register / Claim inventory / Jurisdiction map). Also trigger when the user attaches a Master file or a Lens Library file. Read this file in full at the start of any PRISM session before doing any work."
---

# PRISM v2.0.1 — Framework operating document

**Status:** v2.0.1 release. Canonical framework for Claude orchestration sessions.
**Date:** April 2026
**Supersedes:** PRISM v2.0.0 (release-hygiene patch; see §18 for surface and provenance). PRISM v1.10.4 is terminal on the v1.x line (pinned per DD §10.1).
**Required attachments at every orchestration session:** this file (or the
PRISM v2 Skill that loads it) and the project's Master. This file embeds
Lens Library v0.10 in Appendix G; a singleton PRISM.md attachment is
sufficient for normal operation. Attach a standalone Lens Library only
when the project explicitly pins to a newer Library version than the
embedded copy (see §7.1).
**Substrate:** Claude Opus 4.6 / 4.7 verified at v2.0; other Claude models
report-worthy per §3.1.

**Citation convention.** This file is self-contained operating instructions.
References to source artifacts: `Spec.§X.Y` points to PRISM_v2_spec_rev2.md;
`DD.§X.Y` points to PRISM_v2_rev8_design_document.md; `LL.LL-{U|D}-NNN`
points to a Lens Library entry.

**Tag convention.** Every decision in this document carries a two-axis tag —
durability axis (`structural` / `methodological` / `vendor-dependent` /
`empirical` / `operator-scaffolding`) × review-trigger axis
(`stable` / `review-if: <trigger>` / `review-annually`). The full tag index is
Appendix C.

**Voice.** This is operating instruction for Claude in an orchestration session.
Imperative where Claude must act; declarative where defining shape; descriptive
where pointing. Section headers carry the operative scope.

---

## Quick reference — first-time reader

Reading order for first encounter:

1. **§1 Scope** (this section group) — what v2.0 is and what it isn't.
2. **§2 System overview** — every construct, every lifecycle slot, the visual
   map. Use this to locate any specific mechanic later.
3. **§3 Architecture** — sessions, the triple contract, Master, *What's next*,
   Vendor Selection. The everyday machinery.
4. **§6 Setup** — what happens before any prompt is dispatched. Library-graded
   iterative refinement; the seven probes.
5. **§9 Monitors** + **§10 Standing Principles** — the always-on background
   posture.

After that, §4 (prompt-package engine), §5 (context-pressure framework), §7
(Library integration), §11 (filename conventions), §12 (atomic prompt template
v2 form), and §13 (operator hint catalog) carry the rest of the operating
mechanics. §15 walks a complete worked example.

Reading order for an operator returning to v2.0 after running a session:
*What's next* → relevant §3–§7 mechanics → §9 Monitors if a fire surfaced.

---

## 1. Scope

### 1.1 What v2.0.1 covers `[structural | stable]`

PRISM v2.0 is a structured multi-session, multi-vendor LLM-orchestrated audit
and research framework. v2.0 covers:

- **Two session types** (orchestration on Claude; execution on any vendor)
  with explicit role separation (§3.1).
- **The triple contract** (Envelope inbound, Self-check, Output outbound) as
  the load-bearing interface between sessions (§3.2).
- **Master + *What's next* as continuous-state artifacts** written at every
  orchestration turn-close, regardless of band state (§3.3, §3.4, §5.5).
- **Vendor Selection at dispatch** with live web-search currency check
  (§3.6).
- **Setup as iterative refinement** against the Lens Library v0.9, with
  three-layer readiness clearing the P0→P1 boundary (§6).
- **Seven Setup probes** (P1 Coverage grading, P2 Adversarial Scope, P3
  Decision Framing, P4 Pre-mortem, P5 Falsifier, P6 Domain Reconnaissance,
  P7 User Voice) — Setup-time grading constructs only (§6.3).
- **Library integration** — the Lens Library v0.10 as canonical reference
  catalog (embedded as Appendix G; standalone at `lens/PRISM_lens_library.md`
  for explicit override); point-refresh in Setup; Update sessions for
  currency maintenance (§7).
- **Twelve Monitor slots** (M1–M12, with v1.x M12 Conversation Pressure
  retired into M5 and the M12 slot reused for Result Completeness Check)
  firing orchestration-side at defined lifecycle slots (§9).
- **Telemetric context-pressure framework** (M5) — seven signals,
  qualitative compounding, four bands (🟢🟡🟠🔴), continuous-curation
  posture from 🟡 onward (§5).
- **Migration handoff** as a defined artifact at 🔴 (mandatory) and 🟠
  (operator-elective) (§5.4).
- **Standing Principles** governing posture across sessions (§10).
- **Filename discipline** — structured patterns for Outputs, Masters,
  handoffs, and Library files (§11, SP-14).
- **Forward-compatibility commitments** — Tools slot in Envelope,
  execution-mode flag at Setup (§3.5).
- **Atomic prompt template v2 form** — wraps the triple contract around the
  prompt body (§12).

### 1.2 What v2.0.1 does not cover

- **Re-debating direction.** v2.0 implements the spec; the spec implements
  the design document. Direction is settled. New direction goes through a
  fresh design cycle.
- **Standalone Library evolution.** The Lens Library catalog ships embedded
  in Appendix G (v0.10 at this release) for singleton-attachment use. The
  standalone file at `lens/PRISM_lens_library.md` (tag `prism-lens-v0.10`)
  remains authoritative for the Library's own evolution and for projects
  that explicitly pin to a newer Library version than the embedded copy.
- **Empirical calibration.** Several thresholds in v2.0 are rev. 1 draft
  estimates: M5 band thresholds (§5.1), Update session trigger (§7.5),
  probe iteration ceilings (§6.1). Calibration against real use is a
  post-release item (§16).
- **Multi-vendor Self-check empirical footing.** Verified on Claude
  Opus 4.6/4.7 and Sonnet 4.6 only. Behavior on Gemini, ChatGPT, Perplexity
  is report-worthy (§16).
- **Non-Claude orchestration.** v2.0's machinery uses Claude-specific
  affordances (`present_files`, `create_file`, `str_replace`,
  `ask_user_input`, `conversation_search`, Skill packaging). Non-Claude
  orchestration is graceful-degradation, not a design target (DD.§3.1).

### 1.3 Three-leg constraint `[structural | stable]`

v2.0 honours the constraint inherited from the design document (DD.§8.3):

- **Operator constraint.** Mobile-first; plain-chat substrate; manual
  artifact handling between sessions.
- **Substrate constraint.** Claude Opus 4.6/4.7 in orchestration; multi-
  vendor on the execution side.
- **Methodology constraint.** Structured audit-and-research with explicit
  scope-completeness and convergence discipline.

Mechanics that violate any leg do not earn their place in v2.0. Roadmap
adjacencies (§9 of DD: automated cross-vendor orchestration, plugin-equipped
execution, multi-vendor skill ecosystems) live in reserved structural slots
(`Tools:`, `execution_mode:`) but no machinery beyond the slot.

---
## 2. System overview

**Read this section first if you are encountering v2.0 mechanics for the
first time, and re-read it any time you need to locate a specific construct.**
This section is a map. Definitions live in the per-construct sections (§3–§14).

### 2.1 Construct list

PRISM v2.0 has the following constructs, grouped by category.

**Sessions** (§3.1)
- Orchestration session — Claude session with the framework attached
- Execution session — vendor session running a single dispatched prompt
- Update session — out-of-band, operator-gated, maintains Library currency
  (§7.5)

**Phases**
- P0.x — Setup (iterates against draft Prompt Strategy)
- P1+ — Execution (dispatched prompts run; convergence absorbs results)
- P0→P1 boundary — three-layer readiness clears (§6.2)

**Probes** (§6.3) — Setup-time grading constructs only
- P1 Coverage grading · P2 Adversarial Scope · P3 Decision Framing · P4
  Pre-mortem · P5 Falsifier · P6 Domain Reconnaissance · P7 User Voice

**Monitors** (§9) — orchestration-side checks
- M1 Missing Inputs · M2 Version Drift · M3 Sequence Violation · M4
  Ambiguous Ask · M5 Context Pressure · M6 Premise Shift · M7 Claim
  Conflict · M8 Stale Source · M9 Convergence Type Drift · M10 Rerun /
  Fix Required · M11 Layer 2 Readiness · M12 Result Completeness Check

**Top-level artifacts**
- Master (§3.3) · *What's next* (§3.4) · Lens Library (§7) · Migration
  handoff (§5.4) · Convergence delta (§4.3.1)

**Master sections** (state lives here)
- Decision brief · Stakeholder register · Claim inventory · Jurisdiction
  map · Prompt Strategy · Dispatch register · Findings · Rerun Register ·
  Learnings Register · Changelog · Open dispatches list · Active probes
  list · Open monitors list

**Execution contract** (the triple, §3.2)
- Envelope (inbound) · Self-check (substrate verification) · Output
  (outbound)

**Standing Principles** (§10)
- v2-new/extended: SP-1 ext, SP-12, SP-13, SP-14
- Carryforward: SP-2, SP-4, SP-5, SP-6, SP-7, SP-8 (narrowed), SP-9, SP-10
- Dissolved: SP-3

**Mechanisms**
- Vendor Selection (§3.6) · Vendor Triangulation (§4.3) · Bump atomicity
  (§9.1 spec / §11) · Telemetric framework (§5.1) · Point refresh (§7.4) ·
  Update session (§7.5) · Continuous-curation (§5.3) · Strategy stability
  (§6.5) · Three-layer readiness (§6.2) · Two-layer convergence · Triple
  contract

**Bands** — 🟢 Comfortable · 🟡 Getting warm · 🟠 Curate now · 🔴 Migrate

### 2.2 Visual map

```
┌─────────────────────────────────────────────────────────────────────┐
│ ORCHESTRATION SESSION (Claude; framework attached)                  │
│                                                                      │
│  ┌──────────────────┐    ┌──────────────────┐    ┌───────────────┐ │
│  │ Setup (P0.x)     │    │ Per-turn         │    │ Layer-2       │ │
│  │ ──────────────── │    │ ──────────────── │    │ ───────────── │ │
│  │ P1 Coverage      │    │ M1 Missing Inp.  │    │ Cold synth    │ │
│  │ P2 Adv. Scope    │    │ M2 Ver. Drift    │    │ M9 type drift │ │
│  │ P3 Decision Fr.  │    │ M3 Seq. Viol.    │    │ Falsifier     │ │
│  │ P4 Pre-mortem    │    │ M4 Ambig. Ask    │    │ check         │ │
│  │ P5 Falsifier     │    │ M5 Ctx. Press.   │    └───────────────┘ │
│  │ P6 Domain Recon  │    │ M11 L2 Ready.    │                      │
│  │ P7 User Voice    │    └──────────────────┘                      │
│  └──────────────────┘                                                │
│         │                                                             │
│         ▼                                                             │
│  Three-layer readiness (Structural · Lib coverage · Op ratification) │
│         │                                                             │
│         ▼                                                             │
│  Master version bump (P0→P1) ──── continuous Master + What's next   │
│                                    written every turn-close          │
│         │                                                             │
│         ▼                                                             │
│  ┌──────────────────────────────────────────────────────────┐       │
│  │ Vendor Selection (live web check at dispatch)            │       │
│  │  → produces Envelope                                      │       │
│  └──────────────────────────────────────────────────────────┘       │
│         │                                                             │
└─────────┼─────────────────────────────────────────────────────────────┘
          │ (operator dispatches)
          ▼
┌─────────────────────────────────────────────────────────────────────┐
│ EXECUTION SESSION (any vendor; framework NOT attached)              │
│                                                                      │
│  Envelope (inbound) ──► Self-check (substrate verify) ──► Task body │
│                                                                │     │
│                                                                ▼     │
│                                                         Output (.md) │
└────────────────────────────────────────────────────────────────┬─────┘
                                                                  │
                                                                  ▼
┌─────────────────────────────────────────────────────────────────────┐
│ ORCHESTRATION SESSION (continued; operator attaches Output)         │
│                                                                      │
│  Layer-1 convergence:                                                │
│    M6 Premise Shift                                                  │
│    M7 Claim Conflict      ──┐                                        │
│    M8 Stale Source         ├─► may chain to M10 (Rerun)             │
│    M12 Result Completeness ─┘                                        │
│                                                                      │
│    Vendor Triangulation (if equivalence dispatch, N≥2)               │
│       └─► Convergence delta written to Master                        │
│                                                                      │
│  Reconciliation (Output Vendor/config vs Envelope) ──► Dispatch reg  │
│                                                                      │
│  Master + What's next rewritten ──► band header (M5)                 │
│         │                                                             │
│         ▼                                                             │
│  At 🔴: Migration handoff produced; operator opens fresh session.     │
└─────────────────────────────────────────────────────────────────────┘

OUT-OF-BAND
┌─────────────────────────────────────────────────────────────────────┐
│ Update session (rare; operator-gated)                               │
│   Library file in → currency check → delta document → Library out   │
└─────────────────────────────────────────────────────────────────────┘
```

### 2.3 Construct cards

Per-construct lifecycle, reads, writes, triggers. Cross-refs to detail
sections.

**Sessions and phases**

| Construct | Lifecycle | Reads | Writes | Trigger | Detail |
|---|---|---|---|---|---|
| Orchestration session | Per session | All Master sections, Library, briefs | Master, *What's next* | Operator opens | §3.1 |
| Execution session | Per dispatch | Envelope.Attachments only | Output `.md` | Envelope dispatched | §3.1 |
| Update session | Out-of-band | Library file, web | New Library file | Operator declares | §7.5 |
| P0 Setup | Iterates per turn | Subject brief, Library | Setup artifacts, Prompt Strategy | First session | §6 |
| P1+ Execution | Per orchestration turn | Master, returned Outputs | Master findings | Operator dispatches | §6.5 |

**Probes** (Setup-only)

| Probe | Trigger | Reads | Writes | Detail |
|---|---|---|---|---|
| P1 Coverage grading | P0.x turn-close (iterates) | Library, draft strategy | Coverage map in Master | §6.3.1 |
| P2 Adversarial Scope | P0.x turn-close (iterates) | Library, draft strategy, domain context | Omission candidate list | §6.3.2 |
| P3 Decision Framing | First P0 turn (once) | Subject brief | Decision brief, Stakeholder register | §6.3.3 |
| P4 Pre-mortem | P0.x turn-close (iterates) | Draft strategy, Decision brief | Failure-mode list | §6.3.4 |
| P5 Falsifier | Late P0 (once) | Decision brief | Falsifiers section | §6.3.5 |
| P6 Domain Reconnaissance | Early P0.x (iterates) | Subject, web (live) | Jurisdiction map, authoritative-source citations | §6.3.6 |
| P7 User Voice | Early P0.x (iterates) | User-facing surfaces, web | User-signal list | §6.3.7 |

**Monitors** — orchestration-side; M12 (v2) is Result Completeness Check;
v1.x M12 Conversation Pressure retired into M5

| Monitor | Lifecycle | Reads | Writes | Trigger | Detail |
|---|---|---|---|---|---|
| M1 Missing Inputs | Per session-open + per turn | Session attachments, Output Attachment-warnings | M1 fire | Required attachment absent | §9.1.1 |
| M2 Version Drift | Per session-open | Master metadata, expected version | M2 fire | Master version ≠ expected | §9.1.2 |
| M3 Sequence Violation | Per turn (op declaration) | Prompt Strategy, op input | M3 fire | Step before prereq | §9.3.1 |
| M4 Ambiguous Ask | Per turn (op input) | Op turn content | M4 fire | Cannot confidently parse | §9.1.3 |
| M5 Context Pressure | Per turn-close | 7 telemetric signals | Band header | Every turn-close | §5.2 |
| M6 Premise Shift | Per Layer-1 ingestion | New finding, Setup artifacts | M6 fire | Premise invalidated | §9.2.1 |
| M7 Claim Conflict | Per Layer-1 ingestion | New finding, prior findings | M7 fire | Two findings incompatible | §9.2.2 |
| M8 Stale Source | Per Layer-1 ingestion | New finding's cited sources, web | M8 fire | Source invalidated | §9.2.3 |
| M9 Convergence Type Drift | Per Layer-1 + Layer-2 | Convergence step type | M9 fire | Wrong-posture convergence | §9.1.5 |
| M10 Rerun/Fix Required | Multi-source (chain or op) | Trigger source | Rerun Register | Rerun condition | §9.3.2 |
| M11 Layer 2 Readiness | Per turn-close | Dispatch register, Rerun reg, Open monitors | What's next candidate | Layer 2 conditions met | §9.3.3 |
| M12 Result Completeness | Per Layer-1 ingestion | New finding's domain coverage | M12 fire | Domain coverage gap inside finding | §9.2.4 |

**Artifacts** (state lives here; only orchestration writes Master)

| Artifact | Lifecycle | Reads | Writes | Detail |
|---|---|---|---|---|
| Master | Persistent + per-turn write | Orchestration + execution (selective) | Orchestration only | §3.3 |
| *What's next* | Per-turn rewrite | Orchestration + operator | Orchestration only | §3.4 |
| Lens Library | Persistent (read) | Orchestration | Update session only | §7 |
| Migration handoff | Per-🔴 (or 🟠 elective) | Orchestration | Orchestration | §5.4 |
| Convergence delta | Per Layer-1 batch | Orchestration | Orchestration | §4.3.1 |
| Dispatch register | Per dispatch + per return | Orchestration, *What's next*, M3, M10 | Orchestration | §4.8 |

**Mechanisms** (active behavioral routines)

| Mechanism | Lifecycle | Detail |
|---|---|---|
| Vendor Selection | Per dispatch | §3.6 |
| Vendor Triangulation | Per Layer-1 batch (equivalence mode, N≥2) | §4.3 |
| Bump atomicity | Per Master version increment | §11 |
| Telemetric framework | Per turn-close | §5.1 |
| Point refresh | Per Setup probe iteration | §7.4 |
| Continuous-curation | Per turn-close (band ≥🟡) | §5.3 |
| Strategy stability | Per Layer-1 trigger | §6.5 |
| Three-layer readiness | Per P0→P1 boundary | §6.2 |
| Triple contract | Per dispatch | §3.2 |

**Standing Principles** — persistent posture; not discrete fires (§10)

| SP | v2 status | Detail |
|---|---|---|
| SP-1 ext Canonicity | Extended in v2 | §10.1.1 |
| SP-2 Defer non-critical | Carryforward | §10.2.2 |
| SP-3 (dissolved) | — | §10.2 |
| SP-4 Monitors visible | Carryforward | §10.2.2 |
| SP-5 No heuristic guessing | Carryforward | §10.2.2 |
| SP-6 Rebuild at threshold | Carryforward | §10.2.2 |
| SP-7 File delivery mandatory | Carryforward | §10.2.2 |
| SP-8 Canonical authority (narrowed) | Carryforward (narrowed) | §10.2.1 |
| SP-9 Silence not consent | Carryforward | §10.2.2 |
| SP-10 Verify state before recommending | Carryforward as named principle | §10.1.4 |
| SP-12 Bounded-search disclosure | New in v2 | §10.1.2 |
| SP-13 Substrate declaration | New in v2 | §10.1.3 |
| SP-14 Filename discipline | New in v2 | §10.1.5 |

### 2.4 Lifecycle slots

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

Bands are M5's output; they drive curation and migration posture. Per-band
table in §5.6.

- 🟢 **Comfortable.** Silent. No intervention.
- 🟡 **Getting warm.** Curation observation in *What's next*. Migration
  available at next natural seam.
- 🟠 **Curate now.** Active curation. Migration strongly recommended at
  immediate next seam.
- 🔴 **Migrate.** Migration handoff produced; fresh session.

### 2.6 Cross-section quick-find

If you need to find:

- **A specific construct's full mechanics** → §2.3 construct card →
  cross-ref to detail.
- **How constructs flow in a real audit** → §15 worked example.
- **What changed from v1.10.4** → Appendix D v1.x → v2 surface drift.
- **Decision rationale on something** → Appendix C tag index → Spec.§
  reference for chosen alternative + rationale.
- **A template to paste** → Appendix E template compendium.
- **The full text of a Standing Principle** → Appendix F.

---
## 3. Architecture mechanics

v2.0's architecture is the operating skeleton: two session types, the triple
contract that lets them interoperate cleanly, two artifacts (Master and
*What's next*) that carry state across turns and sessions, forward-compat
slots for things v2.0 doesn't yet have machinery for, and Vendor Selection
as the live currency check at dispatch time.

### 3.1 Two session types `[structural | stable]`

**Orchestration session.** A Claude session with the framework attached.

- *Loaded artifacts at session open*: this framework file (or the PRISM v2
  Skill that loads it); the Master; the Lens Library
  (`PRISM_lens_library.md` v0.9); the Prompt Strategy (when separate from
  the Master); subject-brief documents.
- *Session-open verification*: SP-13 substrate self-check (§10.1.3) — Claude
  declares model identity and confirms it matches the declared orchestration
  target (Claude Opus 4.6 or 4.7). Halt and ask the operator on mismatch or
  cannot-determine.
- *Outputs*: Master updates, *What's next* artifacts, Envelopes for next
  dispatch, convergence findings, Monitor fires.
- *Closes by*: writing *What's next* to the Master and surfacing it for the
  operator. Operator hint emitted: `Save Master to cloud drive (E.5).`
- *Vendor*: Claude (Opus 4.6 / 4.7 verified at v2.0; other Claude models
  report-worthy per DD §3.5 beta posture).

**Execution session.** A vendor session running a single dispatched prompt.

- *Loaded artifacts*: only what the Envelope's `Attachments:` field names.
  Framework not attached.
- *Session-open verification*: PRISM Execution Self-check (§3.2.2) — vendor
  declares model identity and confirms match against the Envelope's
  `Vendor:` and `Vendor config:` fields. Halt and report on mismatch.
- *Outputs*: a single `.md` file wrapped in PRISM Execution Output signature
  (§3.2.3).
- *Closes by*: producing the file and instructing the operator on filename
  and next action (per Envelope's `Expected output:` and the Output's
  `Operator next:`).
- *Vendor*: per the Envelope's `Vendor:` field. Any LLM the strategy
  specified.

**Why the split.** Orchestration is the framework's home — Master state,
Monitor fires, Setup probes, convergence reasoning. Execution is purpose-
built single-shot work — one prompt, one file out, no framework overhead.
Crossing the boundary is the triple contract (§3.2). v1.x ran convergence
inside execution sessions under SP-3; v2 dissolved SP-3 because it was
incompatible with the split.

### 3.2 The triple contract `[structural | stable]`

Three blocks — Envelope (inbound), Self-check (between envelope and task
body), Output (outbound). All three are visually distinctive, self-contained,
and produced by orchestration's Vendor Selection step (§3.6) at dispatch
time. The contract is the load-bearing interface between sessions; it
survives mode changes (manual paste-chat today; automated dispatch later)
unchanged.

#### 3.2.1 PRISM Execution Envelope

```
━━━ PRISM EXECUTION ENVELOPE ━━━
Prompt ID:          [identifier — purpose/title]
Project:            [project name]
Master version:     [filename of Master at dispatch time]
Prompt digest:      [orchestration-generated short identifier; copy verbatim into Output]
Vendor:             [vendor] | multi-vendor
Dispatch shape:     equivalence | split | limitation-named
Dispatch rationale: [one positive-framing line per variant; see §4.2]
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
- `Vendor` — single vendor name (`Claude Opus 4.7`, `Gemini Pro Deep
  Research`, `Perplexity`, `ChatGPT o-series`) or the literal `multi-vendor`.
- `Dispatch shape` — see §4.1 for the three modes.
- `Dispatch rationale` — one positive-framing line per variant. See §4.2.
- `Vendor config` — vendor-specific configuration (e.g., `Deep Research ON,
  extended thinking ON`).
- `Session hygiene` — substrate setup the vendor session must satisfy.
- `Tools` — vendor tool slot. v2 default: `web search ON/OFF`. Reserved
  structural slot for future plugin/skill specification.
- `Attachments` — comma-separated filenames the operator must attach. Order
  is significant where the prompt body references attachments by position.
- `Expected output` — the filename the operator should download the produced
  file as. Naming convention per §11: `[project]_[promptID]_[vendor].md`.
- `Operator hints` — zero or more one-line cues. See §3.2.4.

#### 3.2.2 PRISM Execution Self-check

Operationalizes SP-13 (§10.1.3) inside the execution session. Sits between
the Envelope and the task body.

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
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Behavior contract.**

- The vendor session must self-identify before touching task content.
  Self-identification is best-effort honest — vendors that cannot introspect
  a field hedge on it rather than fabricate.
- Mismatch halts the task and emits a Self-check report. The report is the
  deliverable until the operator confirms.
- "Confirmation to proceed" is a positive operator action (a message in the
  conversation), not an inferred consent from continued attachment (SP-9).

**Multi-vendor empirical footing.** Verified on Claude Opus 4.6/4.7 and
Sonnet 4.6 at v2.0 release. Gemini, ChatGPT, Perplexity behavior under this
block is **report-worthy finding** per DD.§3.5 — operators report
divergences. See §16.

#### 3.2.3 PRISM Execution Output

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
  reconciliation (§4.7).
- `Schema version` — currently `output-v1`. Bumps when the Output block's
  structure changes; orchestration's Layer-1 convergence flags
  incompatibilities at ingestion.
- `Prompt digest` — short identifier orchestration generates for the exact
  dispatched prompt body and writes into the Envelope. Execution copies it
  verbatim from the Envelope into the Output. Orchestration verifies
  copy-through, not cryptographic computation by the execution model. This
  catches wrong-prompt / wrong-attachment delivery without depending on
  vendor chats to compute reliable hashes (which they can't, in general).
- `Operator next` — download filename + attachment instruction for the next
  orchestration turn.
- `Attachment warnings` — populated only when warranted. See §13 for
  emission rules and severity tags.

**Production discipline.** The execution session produces the file via the
vendor's file-creation surface (Claude `create_file`; ChatGPT Canvas;
Gemini's file generation). Where the vendor cannot produce a file, fallback
is delimited content rendering with explicit warning that paste fallback has
known clipboard-fidelity issues (DD.§4.1.1).

#### 3.2.4 Operator hints — emission discipline

Hints are optional one-line cues keyed to the upcoming action.

**Emission rules.**

- Fire only when a cue applies to *this* dispatch. Routine dispatches carry
  zero hints. Signal-to-noise discipline.
- One line per hint; pointer to §17 (mobile operator survival guide), not an
  inline essay.
- No hint that duplicates a Monitor fire.
- Substrate calibration attribution where non-obvious — `(Claude mobile,
  Samsung)`. Mismatched substrates self-diagnose rather than silently
  confuse.
- Hints surface in two places: in the Envelope's `Operator hints:` field
  when the next action is a dispatch; in the *What's next* artifact (§3.4)
  when the next action is not a dispatch (review, ratify, save-to-cloud).

The full operator hint catalog is in §13.

### 3.3 The Master `[structural | stable]`

The Master is the single canonical project state file. Operator workflow
treats it as the project — not the chat, not the session, not what
orchestration remembers.

**Filename convention** (per §11, SP-14):
`[project_name]_prism[version]_master_[phase-derived versioning].md`. E.g.,
`solace_audit_prism2.0_master_p2.3.md`.

**Lifecycle.**

- *Created* at Setup P0.1 (first orchestration turn).
- *Updated* at every orchestration turn-close, regardless of band state.
  Updates are append-mostly: the Changelog gains a line; relevant register
  sections gain entries. Continuous-state mechanic per §5.5.
- *Filename version bumps* at phase boundaries (P0→P1, P1→P2). Sub-version
  increments at convergence rounds within a phase (P2.1 → P2.2). Schema
  version increments tracked in the Master's metadata header. Bump
  atomicity rules in §11.
- *Single file by principle* — no parallel Masters. Multiple-Master state is
  itself a Monitor fire (M2 Version Drift, §9.1.2).
- *Authoritative copy* — operator's locally-attached Master at session open
  is authoritative for that session. Cloud-drive copies (§17 MO-5) are
  durable persistence, not authority.

**Required sections.**

- Metadata header: project name, current Master version, Schema version,
  last updated.
- Decision brief (Setup artifact, §6.4.1).
- Stakeholder register (Setup artifact, §6.4.2).
- Claim inventory (Setup artifact, §6.4.3).
- Jurisdiction map (Setup artifact, §6.4.4).
- Prompt Strategy — current ratified version.
- Dispatch register — table of recommended-vs-executed state per prompt
  (§4.8).
- Findings sections — per-prompt converged findings, with provenance.
- Open dispatches list — prompts not yet closed.
- Active probes list — Setup probes still iterating (P0 only).
- Open monitors list — M2/M3/M4/M6/M7/M8/M9/M10/M11/M12 fires not yet
  resolved.
- Rerun Register (§9.3.2) — overdue/scheduled/running/complete/cancelled.
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

*What's next* is the operator's single source of "what to do next." Not by
scrolling chat. Not by reading the Master in detail. Just *What's next*.

**Lifecycle.** Written at every orchestration turn-close. Replaces in-place;
old *What's next* is overwritten. Historical pointers live in the Master's
Changelog.

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
3. Open Rerun Register items overdue (M10 active).
4. M6 HIGH (Premise Shift) unresolved at convergence.
5. Adaptation pending operator approval.
6. Layer 2 readiness (M11) when conditions met *and* operator has not
   deferred.
7. Next canonical Setup probe iteration (when in P0).
8. Next canonical dispatched prompt (when in P1+ execution).
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
- **Execution mode flag at Setup.** Setup carries a session-level flag
  declaring execution mode. v2.0 default: `execution_mode:
  manual_plain_chat`. Reserved values for future modes:
  `execution_mode: agentic_orchestration`,
  `execution_mode: plugin_equipped`,
  `execution_mode: automated_cross_vendor`. Setup validates the value is
  one of the reserved set; unrecognized values halt Setup with an operator
  escalation.

### 3.6 Vendor Selection at dispatch `[methodological | review-if: vendor landscape changes]`

Vendor Selection runs every time orchestration is about to produce a
dispatch-ready Envelope. Not at Setup time; at dispatch time. The mechanic
operationalizes SP-10 (§10.1.4) at the moment a vendor recommendation
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
point refresh (§7.4), Update sessions (§7.5), and any future recommendation
surface.

---

## 4. Prompt-package engine

The prompt-package engine is the set of mechanics around how prompts are
shaped, dispatched, and reconciled. The triple contract (§3.2) is the
interface; this section is the dispatch logic that decides what to send,
how many vendors to send it to, how to read back what came in, and how to
handle failure.

### 4.1 Single-Envelope-with-spectrum shape `[structural | stable]`

A single Envelope shape across all dispatch shapes. The mode field tells
operator and vendor what kind of run this is.

`Dispatch shape:` carries one of three values: `equivalence`, `split`,
`limitation-named`.

**Mode semantics.**

- **`equivalence`** — dispatch the same prompt body to N vendors, expect
  comparable outputs. Orchestration's Vendor Triangulation fires at N≥2
  (§4.3).
  - `Vendor:` field reads `multi-vendor`.
  - A `Vendor list:` sub-field enumerates the vendors and configs:
    ```
    Vendor list:
      - Claude Opus 4.7 / standard
      - Gemini Pro Deep Research / Deep Research ON
      - Perplexity / Sonar Pro
    ```
  - `Dispatch rationale:` carries one positive-framing line per vendor
    (§4.2).
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
    (per §4.2 positive-framing rule). Not the access reason — the framework
    does not gate on operator vendor access (DD.§3.6).

### 4.2 Rationale discipline per dispatch variant `[methodological | stable]`

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

Vendor Triangulation is a Layer-1 convergence pass that fires when the
second return arrives in an `equivalence` dispatch. Re-fires as each
subsequent return arrives. Tracked via the Master's Dispatch register.

**Lives outside the probe taxonomy.** Operates against returned findings,
not draft strategy. Single-responsibility separation from Probe 2
Adversarial Scope (§6.3.2). Different surfaces (draft strategy vs returned
findings), different lifecycles (Setup-only vs per Layer-1 batch),
different output shapes (omission list vs agreement/divergence delta).

**Trigger.**

- N=1 return: ingested as a single finding, not triangulated. Master
  records `partial-equivalence: N/expected_N`.
- N=2: Vendor Triangulation fires. Convergence delta produced (§4.3.1).
- N=3+: Re-fires; convergence delta updates incrementally.
- N=expected_N: Delta finalizes; Vendor Triangulation closes for this
  prompt.

#### 4.3.1 Convergence delta document

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

Convergence proceeds with whatever returned. Failed dispatches are flagged
with named gaps; operator decides whether to re-dispatch.

**Failure handling.**

- Operator declares a dispatch failed via the close-loop mechanic (§4.9):
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

Default execution stance is "Claude alone is feasible." Multi-vendor or
non-Claude is invoked via explicit declaration in the Prompt Strategy. The
named-limitation escape hatch (§4.1 `limitation-named`) fires when Claude
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

Implicit. No separate `cost:` field. Cost is signaled by:

- *Dispatch shape*: `equivalence` mode N=3 implies ~3× the operator effort
  and vendor-cost of single dispatch.
- *Vendor selection*: Gemini Deep Research is more time-expensive than
  Claude default; Vendor Selection's recommendation bubble (§3.6) carries
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

The Output signature carries `Vendor:` and `Vendor config:` reflecting
executed state. Orchestration auto-reconciles against the Envelope's
recommended state at Layer-1 ingestion.

**Reconciliation states** (recorded in the Dispatch register):

- *Match* — executed Vendor/config equals recommended. Status: `returned`.
- *Substitution* — executed Vendor or config differs. Status:
  `substituted`. Both recommended and executed values logged.
- *Missing* — no Output ever returned. Status: `failed` or `skipped` (per
  close-loop §4.9).

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

Master gains a `Dispatch register` table that tracks recommended-vs-executed
state per prompt. Required Master section (§3.3).

**Schema.**

| Prompt ID | Recommended (Vendor / config) | Executed (Vendor / config) | Status | Convergence ref |
|---|---|---|---|---|
| P2.3 | Gemini Pro DR / DR ON | Claude Opus 4.7 / standard | substituted | layer1-p2.3 |
| P2.4 | Claude Opus 4.7 / standard | — | dispatched | — |
| P2.5 | multi-vendor / equivalence | partial (2 of 3) | partial | layer1-p2.5 |

**Status values** (closed set):

- `dispatched` — Envelope produced; no return yet.
- `scheduled` — operator declared deferral (§4.9).
- `returned` — single-vendor return absorbed; Match.
- `substituted` — return absorbed; Vendor or config differs from
  recommended.
- `partial` — multi-vendor (`equivalence`) dispatch with N < expected_N
  returns absorbed.
- `failed` — operator declared failed (§4.9); reason recorded.
- `skipped` — operator declared skipped (§4.9); rationale recorded.
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

Defined declaration set. Each declaration closes an open dispatch in a
defined way.

**Declarations and effects.**

- **`Done`** — operator attached the Output. Triggers Output reconciliation
  (§4.7). Dispatch register status updates per §4.8.
- **`Running later`** — dispatch deferred. Status: `scheduled`. Master keeps
  slot open. *What's next* surfaces it as a candidate at next turn-close
  (priority tier 8 per §3.4).
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
declaration, M4 (Ambiguous Ask, §9.1.4) fires and asks the operator to
clarify before updating Dispatch register. SP-9 lineage.

### 4.10 Substitution absorption `[structural | stable]`

Substitution is absorbed at convergence; no re-dispatch demanded. Mechanics
integrate with §4.7 reconciliation and §4.8 Dispatch register.

**Operating sequence.**

1. Output's `Vendor` field differs from Envelope's recommended `Vendor`.
2. §4.7 reconciliation detects substitution; logs in Dispatch register with
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

---

## 5. Context-pressure framework

The context-pressure framework is the always-on background mechanism that
keeps long-running orchestration sessions honest about their own
degradation. Seven signals, qualitative compounding, four bands. Asymmetric
bet: the cost of running it is small (some Master bookkeeping); the cost of
not running it is a session that produces silently-wrong work because
recall has frayed.

### 5.1 Telemetric framework — signal weighting and compounding `[methodological | review-if: substrate shifts]`

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
estimates. Real-use calibration is a post-release item (§16).

### 5.2 M5 — Context Pressure monitor `[structural | stable]`

Single Monitor (M5) absorbs the retired v1.x M12 (Conversation Pressure).
Fires at every orchestration turn-close.

**M5 spec.**

- **Trigger.** Every orchestration turn-close. M5 evaluates the seven
  signals (§5.1) and assigns a band.
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
    handoff (§5.4)."
- **Hysteresis** per §5.1.
- **Interaction with other Monitors.** M5 fires regardless of other
  Monitors. When M5 ≥ 🟠, M5's curation-now directive ranks at priority
  tier 1 in *What's next* (above other Monitor fires).

### 5.3 Continuous-curation posture `[methodological | stable]`

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
- **🔴** — curation has been overrun. Migration is the action (§5.4).

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

Defined handoff artifact. Produced by orchestration at 🔴 (mandatory) and
offered at 🟠 (operator-elective).

**Handoff format.**

```
━━━ PRISM SESSION HANDOFF ━━━
Project:                [name]
Master version:         [filename of attached Master]
Lens Library version:   [v0.9 | filename pinned]
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
    e.g., `solace_audit_prism2.0_master_p2.3_no_change.md`. The operator
    can defer cloud-save and attachment-swap on these emissions; the
    prior Master remains current. This addresses mobile churn cost
    without giving up the always-emit safety property.
  - Append-mostly when content does change: Changelog gains a line;
    relevant register sections gain entries; Dispatch register status
    updates per §4.8; findings sections absorb any newly-converged
    Layer-1 outputs.
  - Filename version bump only at phase boundaries or convergence-round
    increments (per §11 bump atomicity). The `_no_change` suffix is
    orthogonal to the version field — a no-change emission keeps the
    same version number as the prior content-bearing emission.
  - Operator must *download* the updated Master at session close when
    the emission is content-bearing (no `_no_change` suffix) to make it
    the authoritative canonical copy. (Manual step under v2.0.1
    plain-chat substrate.)
  - Cloud-drive save is the Operator hint emitted at every
    content-bearing turn-close: `Save Master to cloud drive (§17 MO-5).`

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

Migration posture keyed to band × seam.

| Band | Migration posture | Seam discipline |
|---|---|---|
| 🟢 | Available | At any natural seam; no urgency. Operator-elective. |
| 🟡 | Recommended | At the next natural seam; if no seam approaching, finish current sub-task to create one. |
| 🟠 | Strongly recommended | At the immediate next opportunity; framework actively closes current curation to reach a seam. |
| 🔴 | Correct action now | Framework produces handoff (§5.4); operator opens fresh session and attaches handoff + Master + Lens Library. |

**Operator override.** Operator can decline migration at any band.
Framework respects but flags continuing-at-band in *What's next*. At 🔴,
the per-turn flag escalates to a migration-overdue counter.

---

## 6. Setup mechanics

Setup is iterative refinement against the Lens Library. Not waterfall. The
P0→P1 boundary clears when three independent layers all read ready
simultaneously.

### 6.1 From waterfall to library-graded iterative refinement `[structural | stable]`

**Setup iteration loop.**

1. Operator provides initial subject brief.
2. Orchestration produces draft Prompt Strategy P0.1.
3. Probes 6, 7 iterate early in P0.1 (Domain Reconnaissance + User Voice);
   Probes 1, 2, 4 iterate per turn; Probes 3 and 5 run once.
4. Probe 1 (Coverage grading) outputs tri-state dispositions per Lens
   (§6.3.1).
5. Operator reviews probe outputs.
6. Orchestration produces P0.2 incorporating closures.
7. Repeat until §6.2 readiness clears.

**Iteration numbering** — P0.1, P0.2, …. No artificial cap. Floor: minimum
2 iterations. Soft ceiling: at 4 iterations without saturation, flag
*something structural may be wrong — operator intervention recommended*.

### 6.2 Three-layer readiness `[structural | stable]`

All three layers must clear before P0 → P1 boundary.

#### Layer 1 — Structural completeness

Every planned prompt has the following fields populated:

- Single objective (one-sentence statement).
- Output format (structured findings per §4.11).
- Dependency list (which prior prompts' outputs are inputs; can be empty).
- Attachment map (filenames per attachment).
- Enrichment decision (single-vendor / equivalence / split /
  limitation-named).
- Execution envelope (full Envelope per §3.2.1).

Verification: orchestration walks the strategy and confirms each prompt has
all six fields. Any missing field halts P0 → P1.

#### Layer 2 — Library coverage saturation

Every applicable Lens from the Lens Library v0.9 is either:

- Covered by at least one planned prompt (Probe 1 disposition:
  *fires-covered*), OR
- Explicitly marked out of scope with rationale (Probe 1 disposition:
  *doesn't-fire* with rationale captured, OR *fires-maybe* closed via
  *opt-out* per §6.3.1).

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
`solace_audit_prism2.0_master_p1.0.md`). Setup probes close. Strategy moves
to "presumed stable, revisable at convergence" per §6.5.

### 6.3 The seven probes

Probes operate against the draft Prompt Strategy at Setup. Vendor
Triangulation (§4.3) — convergence-time cross-vendor reconciliation —
lives outside the probe taxonomy because it operates against returned
findings, not draft strategy. Result Completeness Check (M12, §9.2.4) is
a convergence-time monitor. Single-responsibility discipline: probes are
Setup-time grading constructs only.

#### 6.3.1 Probe 1 — Coverage grading (iterates) `[structural | stable]`

Grade the draft strategy against the Lens Library v0.9. Universal lenses
(5) always evaluated. Domain lenses (18) evaluated where their `trigger:`
predicate is met by the subject.

**Per-lens disposition** (tri-state with maybe sub-state):

- **`fires-covered`** — lens applies, draft already covers it. Silent
  pass; recorded for audit trail.
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
decision). Empirical calibration deferred — see §16.

#### 6.3.2 Probe 2 — Adversarial Scope (iterates) `[structural | stable]`

Hunt for silent omissions and under-scoped treatments in the draft Prompt
Strategy. Library-driven (uses Library entries as starting prompts but
goes beyond catalog); informed by domain context.

**Lifecycle.** Setup-only. Iterates per P0.x turn-close. Does not fire at
Layer-1 convergence — cross-vendor finding triangulation is a separate
mechanism (Vendor Triangulation, §4.3) with its own trigger and output
shape.

**Multi-vendor recommendation.** Independent adversarial passes across
vendors; divergence between passes is signal about scope blind spots. Not
the same as cross-vendor finding reconciliation.

**Output.** List of silent-omission candidates the strategy did not
address. Operator reviews; orchestration converts surviving candidates
into Lens references or new prompt additions in the next iteration.

#### 6.3.3 Probe 3 — Decision Framing (once)

Does the strategy answer what the stakeholder actually needs to decide?

Outputs the Decision brief and Stakeholder register Setup artifacts
(§6.4.1, §6.4.2).

#### 6.3.4 Probe 4 — Pre-mortem (iterates)

Imagine execution completes. How would the finding fail to answer the
original question?

**Output.** A list of pre-mortem failure modes; each surviving mode either
becomes a new probe in the strategy or is dismissed with rationale.

#### 6.3.5 Probe 5 — Falsifier (once)

What findings would invalidate the thesis?

**Output.** Decision brief gains a Falsifiers section listing findings
that, if observed, would refute the thesis. These become explicit
success/failure criteria for Layer 2 synthesis.

#### 6.3.6 Probe 6 — Domain Reconnaissance (iterates early)

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

Outputs the Jurisdiction map Setup artifact (§6.4.4).

#### 6.3.7 Probe 7 — User Voice (iterates early) `[structural | stable]`

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
Triangulation extracted from rev. 1's Probe 2 and lives in §4.3, not in
the probe taxonomy.

### 6.4 Setup artifacts

Four instance-specific artifacts populated during Setup. Live in the
Master (§3.3 required sections).

#### 6.4.1 Decision brief

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

Populated by Probe 3 primarily.

```
## Stakeholder register

| Role | Stake | Decision power | Communication channel |
|---|---|---|---|
| [name] | [decision/outcome stake] | [yes/advisory/none] | [channel] |
| ... | ... | ... | ... |
```

#### 6.4.3 Claim inventory

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

**At P0 → P1 boundary.** Strategy moves to "presumed stable, revisable at
convergence."

**Convergence-time strategy revisions** trigger when Layer-1 convergence
produces:

- A premise invalidation (M6 Premise Shift fires HIGH).
- A newly-surfaced domain area (e.g., a regulatory regime not in the
  Jurisdiction map).
- A falsifier hit (one of the Decision brief's Falsifiers is observed).
- An assumption conflict between two findings (M7).

**Revision mechanic** (lighter than v1.x major-bump Adaptation).

1. Convergence finding triggers Monitor (M6 / M7) HIGH.
2. Orchestration drafts a revision: adds/modifies prompts, updates attach
   maps, updates Setup artifacts as needed.
3. Operator ratifies (per Layer 3 §6.2).
4. Master version increments (sub-version bump within phase, e.g., P2.2
   → P2.3).
5. Strategy continues with revised state.

**Attach map travels with each prompt.** When a prompt adapts, its attach
map adapts with it (§3.2.1).

---

## 7. Library integration

The Lens Library v0.10 is canonical at `lens/PRISM_lens_library.md`
(tag `prism-lens-v0.10`). The v0.10 catalog is also embedded in this
file as **Appendix G** for singleton-attachment use; that embedded copy
is the default Library source for orchestration. The standalone Library
file remains authoritative for the artifact's own evolution: Update
sessions (§7.5) produce new versions of the standalone file, and the
next PRISM minor version embeds the new content into Appendix G.
Operators on a newer standalone Library version pin to it explicitly
and override Appendix G (§7.1).

### 7.1 Library reference at Setup `[structural | stable]`

**Required Library source.** By default, orchestration uses the embedded
Lens Library v0.10 in Appendix G (this file). A standalone Lens Library
file (`lens/PRISM_lens_library.md`, tag `prism-lens-v0.10` or newer) is
attached only when the operator explicitly pins the project to a newer
standalone Library version than the embedded copy. When standalone is
attached, it overrides Appendix G for that session. Recommended: if a
standalone newer Library is used, live in the Claude Project alongside
the Master (see §8.1).

**Probe 1 grades against Library entries.** Mechanics in §6.3.1.

### 7.2 Lens schema — what orchestration consumes

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
  (§4.11).
- `specialist_type:` — open taxonomy. Used by judging LLM to promote
  relevant entries as specialist passes under Probe 1.
- `rubric_anchor:` — optional; version-pinned external spec where present.
  Two entries at v0.9 (LL-D-002 WCAG 2.2; LL-D-005 OWASP ASVS 5.0.0).
- `last_verified:` — populated on entries with `rubric_anchor:`.
  Maintenance signal per §7.4.
- `verification_basis:` — populated on entries with `last_verified:`;
  one of `{schema-introduction-only, independent-review}`. Gates §7.4
  freshness logic so a schema-introduction date is not silently treated
  as a performed currency check (v0.10).
- `informed_by:` — provenance only; not a runtime rubric.
- `failure_mode:` — used in operator-facing flag explanations.
- `minimum_scope_binding:` — what counts as "covered" for Probe 1
  disposition.

### 7.3 Specialist-pass promotion

The Library *is* the specialist enumeration. Each lens's `specialist_type:`
field names the practitioner role whose framing the lens channels.
Orchestration's Probe 1 grading promotes relevant entries as specialist
passes within the Prompt Strategy (e.g., "P3.4 — accessibility pass per
LL-D-002, specialist framing: WCAG-qualified accessibility auditor").

### 7.4 Currency maintenance — point refresh `[methodological | stable]`

Two-tier mechanism: point refresh (per-project, in Setup) + Update session
(standalone, rare, operator-gated, §7.5).

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
    accumulates toward an Update session (per §7.5).
- **Output.** Probe 1 output includes per-anchored-entry currency
  disposition.
- **Inline refresh format.** The refreshed citation appears in the Prompt
  Strategy with provenance:
  ```
  P3.4 — accessibility pass
  Specialist framing: WCAG-qualified accessibility auditor (LL-D-002)
  Anchor: WCAG 2.2 (October 2023) — verified current as of [date]
          via web search; PRISM Lens Library v0.10 last_verified
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

### 7.5 Currency maintenance — Update session `[methodological | stable]`

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

These two ideas were parked for v2 from the design-doc-level discussion
(DD §13.3): they earn their place but the framework treats them as
recommendations and graceful-degradation paths rather than hard machinery.

### 8.1 Claude Project as Setup recommendation `[vendor-dependent | review-if: orchestration vendor changes]`

Setup at P0.1 includes a recommendation to create a Claude Project as the
home for project state.

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
- `PRISM_lens_library.md` (v0.9 or pinned tag)
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
  cloud drive per §17 MO-5).

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
   evidence. Per SP-1: canonical artifacts are not regenerated without
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

All Monitors fire orchestration-side. Twelve Monitor slots specified;
v1.x M12 (Conversation Pressure) retired and absorbed into M5; the M12
slot reused in v2 for Result Completeness Check. Three presentation
groupings.

### 9.1 Standalone monitors (M1, M2, M4, M5, M9)

#### 9.1.1 M1 — Missing Inputs `[structural | stable]`

- **Trigger.** Every orchestration session-open and turn-close.
- **Detects.** Required attachments missing from current orchestration
  session; attachments declared in Envelopes but not present in returned
  Outputs (via §13 Attachment warnings).
- **Severity.** HIGH on missing canonical attachments (Master, Lens
  Library, Prompt Strategy if separate). MEDIUM on missing prompt-specific
  attachments. LOW on schema mismatches.
- **Resolution.** Halt until attachments provided; or operator confirms
  intentional absence.

#### 9.1.2 M2 — Version Drift `[structural | stable]`

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
  Optional: consult session history per §8.2.

**Why retained despite bump atomicity (§11).** Bump atomicity makes drift
unlikely *by construction* but not impossible. Residual failure modes:

- Operator attaches an old Master from cloud archive by mistake.
- OS-level filename collisions serve a stale file.
- Cross-device syncing serves a previous version.
- Multiple Masters from forked sessions (anti-pattern but not impossible).

#### 9.1.3 M4 — Ambiguous Ask `[methodological | stable]`

- **Trigger.** Every orchestration turn that processes operator input.
- **Detects.** Operator declaration that orchestration cannot confidently
  parse (close-loop §4.9 ambiguity; intent unclear; conflicting
  instructions).
- **Severity.** HIGH if the next action depends on the ambiguity. LOW if
  orchestration can proceed and clarify post-hoc.
- **Resolution.** Orchestration explicitly asks for clarification before
  proceeding. SP-9 lineage: silence not consent.
- **No execution mirror.** Execution sessions receive pre-resolved
  dispatched prompts; M4 is orchestration-only.

#### 9.1.4 M5 — Context Pressure

Spec per §5.2.

#### 9.1.5 M9 — Convergence Type Drift `[methodological | stable]`

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

Fire during Layer-1 integration of new findings into the Master. Can chain
to M10.

#### 9.2.1 M6 — Premise Shift `[structural | stable]`

- **Trigger.** Layer-1 convergence — new finding ingested.
- **Detects.** Finding invalidates a premise the strategy was built on.
  Premises documented in Decision brief, Stakeholder register, Claim
  inventory, Jurisdiction map.
- **Severity.** HIGH — strategy revision required (§6.5).
- **Resolution.** Strategy revision mechanic per §6.5. Chains to M10
  (Rerun) for prompts whose premise has shifted.
- **v1.x → v2 surface drift.** v1.x M6 read premises from prompt context
  sections. v2 M6 reads premises from Setup artifacts. Surface broadened;
  name unchanged because face value still describes the work.

#### 9.2.2 M7 — Claim Conflict `[structural | stable]`

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

#### 9.2.3 M8 — Stale Source `[structural | stable]`

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

**Scope distinction from §7.4 point refresh.** M8 looks at *evidence inside
the audit*. §7.4 looks at *framework anchors used to grade the audit's
scope*. Different artifacts, different lifecycles, different resolutions.

| Mechanism | Surface | Lifecycle | Resolution |
|---|---|---|---|
| **M8** | Cited evidence sources in returned findings | Per finding, at Layer-1 convergence | Re-dispatch with current sources |
| **§7.4 point-refresh** | Lens Library entry's `rubric_anchor:` / `informed_by:` | Per Setup probe iteration | Inline refresh in Prompt Strategy; advisory signal toward Update session |

#### 9.2.4 M12 — Result Completeness Check `[structural | stable]`

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

Feed the priority-ranked candidate list at each orchestration turn-close.

#### 9.3.1 M3 — Sequence Violation `[structural | stable]`

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

#### 9.3.2 M10 — Rerun / Fix Required `[structural | stable]`

- **Trigger.** Triggered by chain from M6 / M7 / M8 / M12 HIGH; or by
  operator declaration of `failed` (§4.9); or by Probe 5 falsifier hit; or
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
  priority tier 3 per §3.4.

#### 9.3.3 M11 — Layer 2 Readiness `[structural | stable]`

- **Trigger.** Every orchestration turn-close.
- **Detects.** Conditions for Layer 2 cold synthesis met: all Layer-1
  prompts closed; Rerun Register clear; convergence saturated; no
  unresolved M6 / M7 HIGH; operator has not deferred Layer 2.
- **Output.** Surfaces in *What's next* as a candidate at priority tier 6.
- **Resolution.** Operator decides at *What's next* moment whether to run
  Layer 2.

### 9.4 Monitor severity report format

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

Standing Principles are persistent posture, not discrete fires. They live
in the orchestration LLM's behavior at all times. Each principle has a
defined application surface; the principle travels even when specific
mechanics evolve.

### 10.1 Standing Principles introduced or extended in v2

#### 10.1.1 SP-1 extended — Canonicity preservation `[operator-scaffolding | stable]`

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

#### 10.1.2 SP-12 — Bounded-Search Disclosure `[operator-scaffolding | stable]`

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

#### 10.1.3 SP-13 — Substrate Declaration `[operator-scaffolding | stable]`

- PRISM-loaded sessions verify substrate against declared target before
  executing dependent work.
- If self-identification doesn't match declared target, or can't be
  determined, session halts and asks operator.
- Operationalized inside execution sessions via the Self-check block
  (§3.2.2).
- In orchestration sessions: operationalized as a session-open
  verification — orchestration self-identifies and confirms it matches
  the declared orchestration target (Claude Opus 4.6 or 4.7 at v2.0).

**Orchestration-side spec.**

```
[At every orchestration session-open:]
SP-13 verification:
  Self-identification: [model, vendor, mode]
  Declared target: [Claude Opus 4.6 or 4.7]
  Match: [yes / no / cannot-determine]
[If no or cannot-determine: halt; ask operator.]
```

#### 10.1.4 SP-10 — Verify state before recommending `[operator-scaffolding | stable]`

Carries forward from v1.10.4 as a named principle. The principle's
mechanics live primarily in Vendor Selection (§3.6) — but holding it as a
named SP keeps it portable: point refresh (§7.4), Update sessions (§7.5),
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

#### 10.1.5 SP-14 — Filename Discipline `[operator-scaffolding | stable]`

Extracted from v1.x SP-8 (which bundled two concerns under one number).
v2 splits SP-8 into Canonical Authority (the original SP-8) and Filename
Discipline (this new SP-14).

- Look-alike files produced by multi-vendor execution use the structured
  filename pattern: `[project]_[promptID]_[vendor].md` for Outputs,
  `[project_name]_prism[version]_master_[phase-versioning].md` for Masters,
  `PRISM_lens_library_[version].md` for Library files, dated handoffs for
  migrations.
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

Full filename-convention canonical reference table in §11.

### 10.2 v1.x Standing Principles — carryforward catalog

Per-SP disposition explicit:

| SP | v1.10.4 name | v2 disposition | Notes |
|---|---|---|---|
| SP-1 | Never reconstruct files from memory | Extended in v2 | Now covers *offers* to reconstruct. See §10.1.1 |
| SP-2 | Defer non-critical fixes to natural touchpoint | Carryforward | Direct; principle unchanged |
| SP-3 | Convergence is part of prompt delivery | **Dissolved** | Incompatible with orchestration/execution split |
| SP-4 | Every Monitor produces visible output | Carryforward | Direct; applies to v2 monitors at orchestration |
| SP-5 | No heuristic guessing on ambiguous input | Carryforward | Direct; pairs with SP-9 |
| SP-6 | Rebuild at threshold (build-method discipline) | Carryforward | Direct; applies to spec/framework builds |
| SP-7 | File delivery is mandatory | Carryforward | Direct; reinforced by triple contract's file-based Output |
| SP-8 | (a) Canonical authority + (b) Filename discipline | **Split** | (a) stays SP-8; (b) becomes SP-14 |
| SP-9 | Silence is never consent | Carryforward | Direct; applies to operator close-loop, ratification, ambiguity escalation |
| SP-10 | Verify state before recommending | Carryforward as named principle | Mechanics in Vendor Selection; principle stays SP-tier |
| SP-12 | Bounded-Search Disclosure | New in v2 | See §10.1.2 |
| SP-13 | Substrate Declaration | New in v2 | See §10.1.3 |
| SP-14 | Filename Discipline | New in v2 (extracted from SP-8) | See §10.1.5 |

#### 10.2.1 SP-8 narrowed — Canonical Authority `[operator-scaffolding | stable]`

After the v2 split, SP-8 carries one concern:

- The file delivered via `present_files` is canonical for that project
  state.
- Any edit made outside a Claude session (desktop editor, phone
  annotation, external LLM) must be flagged at the start of the next
  session so M2 (Version Drift) can reconcile.
- Filename discipline (the look-alike disambiguation pattern) extracted to
  SP-14 (§10.1.5).

#### 10.2.2 Carryforward SPs — application surfaces

The six pure-carryforward SPs (SP-2, SP-4, SP-5, SP-6, SP-7, SP-9) carry
forward from v1.10.4 verbatim in principle. Their v2 application surfaces:

- **SP-2 (Defer non-critical fixes to natural touchpoint).** Applies in
  orchestration's *What's next* ladder — non-critical issues queue against
  priority tiers, fix at next aligned step. M10 fires when no natural
  touchpoint exists.
- **SP-4 (Every Monitor produces visible output).** Applies to all M1–M12
  monitor fires in orchestration. Silent monitors are useless monitors.
- **SP-5 (No heuristic guessing on ambiguous input).** Applies wherever
  orchestration parses operator input. Pairs with M4 (Ambiguous Ask)
  firing.
- **SP-6 (Rebuild at threshold).** Applies to v2 framework builds (spec →
  PRISM_v2_0.md), Library Update sessions, large Master rewrites.
  Threshold ≤~8 sequential edits → str_replace; above → create_file
  rebuild.
- **SP-7 (File delivery is mandatory).** Applies to every orchestration
  session that updates Master, every execution session that produces
  Output, every Update session that produces a new Library file.
  Reinforced structurally by the triple contract's file-based Output
  (§3.2.3).
- **SP-9 (Silence is never consent).** Applies wherever operator decision
  is required: close-loop declarations, ratification, ambiguity
  escalation, migration override at 🔴, Project recommendation
  accept/decline. Active operator action required; no defaults-on-timeout.

Full text of every SP in Appendix F.

---

## 11. Filename conventions and bump atomicity `[structural | stable]`

Canonical reference table for every PRISM v2 artifact's filename pattern,
plus the atomic-bump routine that produces version increments.

### 11.1 Filename patterns

| Artifact | Pattern | Example |
|---|---|---|
| Master | `[project]_prism[major.minor]_master_[phase-versioning].md` | `solace_audit_prism2.0_master_p2.3.md` |
| Execution Output | `[project]_[promptID]_[vendor].md` | `solace_audit_p2.3_gemini.md` |
| Migration handoff | `[project]_handoff_[YYYY-MM-DD]_[seq].md` | `solace_audit_handoff_2026-04-25_01.md` |
| Lens Library file | `PRISM_lens_library_[version].md` | `PRISM_lens_library_v0_9.md` |
| Update session output | `PRISM_lens_library_[new-version].md` + delta document | `PRISM_lens_library_v0_9_1.md` |
| Subject brief | `[project]_brief.md` | `solace_audit_brief.md` |
| Prompt Strategy (when separate) | `[project]_prompt_strategy_[phase-versioning].md` | `solace_audit_prompt_strategy_p1.0.md` |

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

The atomic prompt template wraps the triple contract around the prompt
body. It's the unit operators paste into execution sessions.

### 12.1 Template shape `[structural | stable]`

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

- **No convergence checklists in the prompt body.** Convergence is
  orchestration-side per the triple-contract split. v1.x's per-prompt
  convergence checklists drop in v2 (SP-3 dissolution).
- **No vendor-specific machinery in the body.** Tool requests live in the
  Envelope's `Tools:` field; vendor-specific config in `Vendor config:`.
- **Attachments referenced by name and order.** When the body references
  `Attachment 1`, that maps to the first filename in the Envelope's
  `Attachments:` list.
- **Findings discipline per §4.11.** Numbered, attributable, evidence-
  classed, confidence-calibrated.

### 12.3 What v1.x's atomic template carried that v2 reshapes

- *Hygiene block* → folded into Envelope and Self-check (substrate
  verification is now structural, not prose discipline).
- *[UNVERIFIED] tagging* → restored as an explicit Verification status
  axis in the §4.11 finding structure (v2.0.1). Orthogonal to confidence;
  see §4.11 *Verification ≠ confidence*.
- *Discrepancy Check* → orchestration-side at Layer-1 (M7 Claim Conflict).
- *Live watch for preemptive scope-down* → orchestration-side via M5 +
  M6.
- *Convergence (Layer 1 — mandatory)* → orchestration-side; SP-3
  dissolved.

The body now carries only what a vendor session actually needs: context,
task, method, output shape. Everything else is in the Envelope or
orchestration-side.

---

## 13. Operator hint catalog `[methodological | stable]`

Hints are optional one-line cues keyed to the upcoming action. Emission
discipline per §3.2.4. The catalog below is the canonical reference; new
hints accrue here as patterns surface.

### 13.1 Cloud drive and persistence

- `Save output to cloud drive after download, before switching to the
  next vendor (see E.5).`
- `Save Master to cloud drive at session close (see E.5).`

### 13.2 Mobile platform cues

- `On Samsung, expect indexing delay on the downloaded file (E.1).`
- `If [vendor] mobile fails to download, retry in Firefox Desktop mode
  (E.2).`
- `On iOS, the download lands in Files → Downloads folder (vendor-
  specific).`

### 13.3 Session hygiene cues

- `Run [vendor] outside any project so it isn't distracted by project
  memory.`
- `Re-attach Master and Lens Library at session open.`
- `New session — paste handoff first, then attach Master and Library.`

### 13.4 Multi-vendor cues

- `Equivalence dispatch — N=3. Send to all three before attaching any
  return.`
- `Vendor [X] substituted at last dispatch — note this for triangulation
  weighting.`

### 13.5 Recovery cues

- `Master version mismatch — verify which file is current before
  attaching.`
- `Session history search may be needed — confirm scope before
  concluding.`

### 13.6 Attachment warnings

These are emission targets — the Output's `Attachment warnings:` field
(§3.2.3 footer) populates with severity-tagged lines:

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
  UNREADABLE: solace_brief.pdf (Deep Research subagent file-access)
```

**Orchestration response.** M1 fires HIGH on `MISSING:`, MEDIUM on
`UNREADABLE:` / `CORRUPTED:`, LOW on `SCHEMA_MISMATCH:`. *What's next*
surfaces re-dispatch with corrected attachment list as a candidate.

---

## 14. Missing-handoff recovery

What happens when the operator opens a fresh orchestration session
without a handoff (operator skipped the migration step at 🔴; handoff
was lost; mid-project session was opened cold)?

### 14.1 Recovery flow `[methodological | stable]`

1. **Session-open verification fires.** SP-13 substrate check passes;
   M1 detects no handoff attached.
2. **Orchestration searches for the canonical Master.** Per SP-1
   protocol:
   - Past-conversation search for the project name and likely Master
     filenames (`conversation_search`, bounded by current Project per
     §8.1; SP-12 disclosure on bound).
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
5. **No silent regeneration.** Per SP-1: orchestration does not
   reconstruct what's missing from memory. Surface what was located,
   surface what couldn't be located, ask operator how to proceed.
6. **If Master itself cannot be located.** Escalate per SP-1: name the
   consequences of regenerating from memory (authenticity loss, schema
   drift, silent contamination); ask operator whether to proceed with
   reconstruction (and document the reconstruction explicitly in the
   Master's Changelog), or whether to re-Setup.

### 14.2 Why this matters

The continuous-state mechanic (§5.5) is the front-line defense — every
turn-close writes the Master and *What's next*. The recovery flow is the
backstop when the front-line defense is bypassed (handoff lost, session
opened from outside the Project, cross-device churn). SP-1's discipline
makes the recovery flow safe rather than seductive: it's harder than
recreating from memory, and it should be — recreation is the failure
mode the discipline exists to prevent.

---

## 15. Worked example flow

This section walks a complete audit through v2.0's mechanics. Subject:
hypothetical career-coaching SaaS audit ("Atlas"). Sketch, not rubric;
illustrates how the constructs chain in real use.

```
Session 1 — Orchestration. Operator: "Begin PRISM v2 audit on
Atlas career coaching SaaS. Brief attached: atlas_brief.md."

[SP-13 substrate self-check fires: Claude Opus 4.7, match.]
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
  Probe 1 grades against Lens Library v0.9. Initial coverage map:
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

These items v2.0 does not fix because they require real-use signal.
Surfaces calibrate post-release on the dogfood run and operator
feedback channel.

1. **Probe iteration floors and ceilings.** Current: minimum 2, soft
   ceiling at 4. Calibrate against real Setup runs.
2. **Probe 1 *fires-maybe* operator-fatigue.** Volume of *maybes* per
   project; mitigation effectiveness of judging-LLM silent resolution.
3. **§7.4 point-refresh fatigue.** Frequency of `stale-refresh` per
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

These ride into the dogfood run as flagged items. Telemetry on each
feeds the v2.1 minor version.

---

## 17. Mobile operator survival guide

v2.0 is mobile-first. Mobile operators routinely encounter patterns —
both frictions and effective interaction moves — that desktop operators
either don't hit or don't need. This section catalogues two classes:
**vendor-client workarounds** (concrete responses to LLM-vendor
mobile-client limitations) and **operator interaction patterns** (ways
of asking and navigating that are more valuable on mobile than on
desktop). Living document: entries accumulate as patterns surface.

Entries here may be surfaced inline as **in-context operator hints** at
specific orchestration touchpoints — the Execution Envelope's
`Operator hints` field (§3.2.4) and the *What's next* artifact (§3.4) —
so an operator sees the relevant cue at the moment of acting rather
than from memory.

Each entry names the **Problem** or **Situation**, the **Workaround** or
**Pattern**, and **Why it works** (so an operator can extrapolate when
the exact case doesn't match).

### Vendor-client workarounds

#### E.1 — Samsung file explorer: LLM-downloaded files invisible until indexing catches up

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

#### E.2 — Broken file/clipboard operations in LLM mobile apps

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

#### E.3 — Artifact + handoff together: "present document with instructions"

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
Execution Envelope discipline (§3.2.1) — same instinct, different
altitude: bake operating context into the artifact.

#### E.4 — Session retrieval: "point me to the relevant session"

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

**Caveat — bounded-search disclosure (SP-12).** Past-conversations
search is scoped: if the operator is in a project, search is confined
to that project's chats; otherwise it covers non-project chats. If the
target session lives in a different scope, the search returns null.
Claude surfaces this bound rather than asserting a global null —
*"I didn't find it within this project's conversation scope; the
session may live in a different project or outside projects; confirm
before I conclude it doesn't exist."*

#### MO-5 — Persisting artifacts across device/session loss

*(v2.0.1: renamed from `E.5` to `MO-5` to disambiguate from Appendix E.5 — *What's next* template. Mobile-guide subsections are now MO-1 through MO-5; Appendix E template subsections remain E.1 through E.5.)*

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

---

## Appendix A — Glossary

Combines DD Appendix A and Spec Appendix A. Definitions live here;
mechanics live in the cross-referenced sections.

| Term | Definition |
|---|---|
| **Adversarial Scope Probe** | Setup-time probe (P2). Hunts silent omissions in draft strategy. Library-driven; multi-vendor recommended. §6.3.2. |
| **Anchor disposition** | Currency state per `rubric_anchor:` entry. States: `fresh`, `stale-refresh`, `stale-accumulating`. §7.4. |
| **Atomic prompt template** | Template that wraps the triple contract around a prompt body. The unit operators paste into execution sessions. §12. |
| **Band** | M5's output. Four states: 🟢 Comfortable, 🟡 Getting warm, 🟠 Curate now, 🔴 Migrate. §5.6. |
| **Bump atomicity** | The mechanic that ties Master version increments to defined triggers (phase transitions, convergence rounds, probe iterations, schema changes). §11. |
| **Claim Conflict** | M7's surface — two findings with incompatible claims on the same surface. v1.x called this Assumption Conflict. §9.2.2. |
| **Claim inventory** | Setup artifact. Table of claims the audit must adjudicate, with audit-pass mapping. §6.4.3. |
| **Continuous-curation** | Per-turn-close curation observation (band ≥ 🟡) or directive (band ≥ 🟠) in *What's next*. §5.3. |
| **Continuous-state mechanic** | Master + *What's next* written at every orchestration turn-close, regardless of band state. §5.5. |
| **Convergence delta** | Vendor Triangulation output document for an `equivalence` dispatch. §4.3.1. |
| **Decision brief** | Setup artifact. Captures the decision under test, decision-maker, deadline, cost-of-error, falsifiers. §6.4.1. |
| **Decision Framing Probe** | Setup-time probe (P3). Produces Decision brief + Stakeholder register. §6.3.3. |
| **Delta finalization** | When all expected vendor returns are in for an `equivalence` dispatch and Vendor Triangulation closes the convergence delta. §4.3. |
| **Dispatch rationale** | Envelope field carrying one positive-framing line per dispatch variant component. §4.2. |
| **Dispatch register** | Master section tracking recommended-vs-executed state per prompt. §4.8. |
| **Dispatch shape** | Envelope field carrying the dispatch structural shape: `equivalence`, `split`, or `limitation-named`. §4.1. |
| **Domain Reconnaissance Probe** | Setup-time probe (P6). Surveys domain practice + authoritative-source detection + Jurisdiction map. §6.3.6. |
| **Envelope** | The first block of the triple contract — inbound vendor instructions including dispatch metadata, attachments, and operator hints. §3.2.1. |
| **`equivalence` dispatch** | Same prompt body to N vendors; outputs comparable; triggers Vendor Triangulation at N≥2. §4.1. |
| **Execution session** | Vendor session running a single dispatched prompt. Framework not attached; loaded artifacts limited to Envelope's `Attachments:` field. §3.1. |
| **Falsifier** | A finding that, if observed, would refute the audit's thesis. Captured in the Decision brief. §6.3.5, §6.4.1. |
| **`fires-covered` / `fires-uncovered` / `doesn't-fire` / `fires-maybe`** | Probe 1's tri-state-with-maybe disposition per Lens. §6.3.1. |
| **Jurisdiction map** | Setup artifact. Per-jurisdiction listing of triggered regulatory regimes and their materiality. §6.4.4. |
| **Layer 1** | Per-prompt convergence — orchestration absorbs returned findings into the Master. Monitors M6/M7/M8/M12 fire here. |
| **Layer 2** | Cold synthesis across all Layer-1 findings to produce the audit's external deliverable. M9 fires here. M11 surfaces readiness. |
| **Lens Library** | The reference catalog of audit-scope lenses. Universal (5) + Domain (18). v0.9 release pinned at `prism-lens-v0.9`. §7. |
| **`limitation-named` dispatch** | Single-vendor dispatch with explicit `Not chosen:` rationale. §4.1. |
| **Master** | The single canonical project state file. Updated at every orchestration turn-close. §3.3. |
| **Migration handoff** | Defined artifact produced at 🔴 (mandatory) or 🟠 (optional) for fresh-session continuity. §5.4. |
| **Monitor** | Orchestration-side check that fires at a defined lifecycle slot. M1–M12 specified in §9. |
| **Natural seam** | A transition point where migration is low-cost. Defined set: convergence round complete, phase boundary, deliverable shipped, setup iteration complete. §5.3. |
| **Orchestration session** | Claude session with the framework attached. Master state, Monitor fires, Setup probes, convergence reasoning all live here. §3.1. |
| **Output** | The third block of the triple contract — outbound finding signature with executed-state metadata and operator-next instructions. §3.2.3. |
| **Point refresh** | Per-project, in-Setup currency check on Library `rubric_anchor:` entries. §7.4. |
| **Pre-mortem** | Setup-time probe (P4). Imagines execution complete; surfaces failure modes. §6.3.4. |
| **PRISM** | Prompts · Research · Iteration · Synthesis · Master. The framework. |
| **Probe** | Setup-time grading construct against the draft Prompt Strategy. Seven probes specified: P1–P7. §6.3. |
| **Prompt Strategy** | The plan of dispatched prompts produced by Setup. Lives in the Master. Iterates in P0; ratifies at P0→P1; revisable at convergence (§6.5). |
| **Result Completeness Check** | M12. Convergence-time monitor detecting within-domain coverage gaps in returned findings. §9.2.4. |
| **Saturation** | Two consecutive iterations produce no material change to coverage or strategy. §6.2. |
| **Self-check** | The middle block of the triple contract — substrate verification per SP-13. §3.2.2. |
| **Setup artifacts** | Four instance-specific artifacts populated during Setup: Decision brief, Stakeholder register, Claim inventory, Jurisdiction map. §6.4. |
| **`split` dispatch** | Prompt split into vendor-specific sub-prompts; synthesis happens orchestration-side. §4.1. |
| **Stakeholder register** | Setup artifact. Per-role listing of stake, decision power, communication channel. §6.4.2. |
| **Standing Principle (SP)** | Persistent posture; not a discrete fire. Twelve SPs in v2 (one dissolved, three new, eight carryforward). §10. |
| **Strategy stability** | At P0→P1 ratification, strategy is "presumed stable, revisable at convergence." §6.5. |
| **Substitution** | Output's Vendor field differs from Envelope's recommended Vendor. Absorbed at convergence; no automatic re-dispatch. §4.10. |
| **Three-layer readiness** | The P0→P1 boundary clears when Structural completeness, Library coverage saturation, and Operator ratification all clear. §6.2. |
| **Triple contract** | Envelope (inbound) + Self-check (substrate verify) + Output (outbound). The load-bearing interface between sessions. §3.2. |
| **Update session** | Standalone, rare, operator-gated session that maintains Library currency. §7.5. |
| **User Voice Probe** | Setup-time probe (P7). Imports real end-user signal. §6.3.7. |
| **Vendor config** | Envelope/Output field carrying vendor-specific configuration flags. §3.2.1. |
| **Vendor Selection** | Live web-search currency check at every dispatch; produces Envelope. §3.6. |
| **Vendor Triangulation** | Layer-1 convergence pass that fires at N≥2 for `equivalence` dispatches. §4.3. |
| ***What's next*** | Per-turn-close artifact. The operator's single source of "what to do next." §3.4. |

---

## Appendix B — Spec → v2.0 source mapping

How sections of the v2 specification (`PRISM_v2_spec_rev2.md`) map into
this operating document. Use this when reading rationale-level
discussion in the spec and wanting to find the operating instruction
here, or vice versa.

| Spec section | Topic | This file |
|---|---|---|
| Spec.§1 | Scope of spec | §1 |
| Spec.§2 | System overview | §2 |
| Spec.§3.1 | Two session types | §3.1 |
| Spec.§3.2 | Triple contract | §3.2 |
| Spec.§3.3 | Master | §3.3 |
| Spec.§3.4 | *What's next* | §3.4 |
| Spec.§3.5 | Forward-compatibility commitments | §3.5 |
| Spec.§3.6 | Vendor Selection | §3.6 |
| Spec.§4.1 | Single-Envelope-with-spectrum | §4.1 |
| Spec.§4.2 | Rationale discipline | §4.2 |
| Spec.§4.3 | Vendor Triangulation | §4.3 |
| Spec.§4.4 | Asymmetric returns | §4.4 |
| Spec.§4.5 | Claude-baseline | §4.5 |
| Spec.§4.6 | Cost signaling | §4.6 |
| Spec.§4.7 | Reconciliation | §4.7 |
| Spec.§4.8 | Dispatch register | §4.8 |
| Spec.§4.9 | Close-loop | §4.9 |
| Spec.§4.10 | Substitution absorption | §4.10 |
| Spec.§4.11 | Body convergence provisions | §4.11 |
| Spec.§5.1 | Telemetric framework | §5.1 |
| Spec.§5.2 | M5 + M12 consolidation | §5.2 |
| Spec.§5.3 | Continuous-curation | §5.3 |
| Spec.§5.4 | Migration handoff | §5.4 |
| Spec.§5.5 | Continuous-state mechanic | §5.5 |
| Spec.§5.6 | Migration matrix | §5.6 |
| Spec.§6.1–6.5 | Setup mechanics | §6.1–§6.5 |
| Spec.§7.1–7.5 | Library integration | §7.1–§7.5 |
| Spec.§8.1 | Claude Project recommendation | §8.1 |
| Spec.§8.2 | Session history | §8.2 |
| Spec.§9.1 | Bump atomicity / M2 | §11 + §9.1.2 |
| Spec.§9.2 | Attachment warnings | §13.6 |
| Spec.§9.3 | M8 vs §7.4 boundary | §9.2.3 |
| Spec.§10 | Worked example | §15 |
| Spec.§11 | Monitor specs | §9 |
| Spec.§12.1 | New / extended SPs | §10.1 |
| Spec.§12.2 | SP carryforward catalog | §10.2 |
| Spec.§13 | Resolved direction summary | (provenance — not reproduced) |
| Spec.§14 | Empirical items | §16 |
| Spec.§15 | Build residuals | §11, §12, §13, §14, App C |
| Spec.§16 | Flagged-items register | (provenance — see Spec) |
| Spec.§17 | Status | (provenance — see Spec) |
| Spec.App A | Terminology | App A |
| Spec.App B | Tag index | App C |
| Spec.App C | v1.x → v2 surface drift | App D |
| DD.App E | Mobile operator survival guide | §17 |

Provenance items (where this file does not reproduce content from spec):

- **Resolved direction summary tables** (Spec.§13). Provenance only —
  every direction listed there is implemented in the body of this file.
- **Flagged-items register** (Spec.§16). Alternatives considered for
  each design decision live in the spec; this file carries only the
  chosen alternative with its tag.
- **Status section** (Spec.§17). Build phase is past — this file is the
  build output.

---

## Appendix C — Decision tag index

Every decision in this document carries a two-axis tag. This appendix
indexes decisions by tag for easy review.

**Durability axis values:** `structural`, `methodological`,
`vendor-dependent`, `empirical`, `operator-scaffolding`.

**Review-trigger axis values:** `stable`, `review-if: <trigger>`,
`review-annually`.

### C.1 `[structural | stable]`

§1.1 (scope), §1.3 (three-leg constraint), §3.1 (two session types),
§3.2 (triple contract), §3.3 (Master), §3.4 (*What's next*), §3.5
(forward-compatibility commitments), §4.1 (single-Envelope-with-
spectrum), §4.3 (Vendor Triangulation), §4.4 (asymmetric returns), §4.7
(reconciliation), §4.8 (Dispatch register), §4.9 (close-loop), §4.10
(substitution absorption), §4.11 (prompt body convergence provisions),
§5.2 (M5), §5.4 (migration handoff format), §5.5 (continuous-state
mechanic), §5.6 (defensive migration), §6.2 (three-layer readiness),
§6.3.1 (Probe 1 Coverage grading), §6.3.2 (Probe 2 Adversarial Scope),
§6.3.7 (Probe 7 User Voice), §6.5 (strategy stability), §7.1 (Library
reference at Setup), §9.1.1 (M1 Missing Inputs), §9.1.2 (M2 Version
Drift), §9.2.1 (M6 Premise Shift), §9.2.2 (M7 Claim Conflict), §9.2.3
(M8 Stale Source), §9.2.4 (M12 Result Completeness Check), §9.3.1 (M3
Sequence Violation), §9.3.2 (M10 Rerun/Fix Required), §9.3.3 (M11 Layer
2 Readiness), §11 (filename conventions and bump atomicity), §12.1
(atomic prompt template).

### C.2 `[methodological | stable]`

§4.2 (rationale discipline), §4.6 (cost signaling), §6.1 (iterative
refinement), §7.4 (point refresh), §7.5 (Update session), §9.1.3 (M4
Ambiguous Ask), §9.1.5 (M9 Convergence Type Drift), §13 (operator hint
catalog), §14.1 (missing-handoff recovery flow).

### C.3 `[methodological | review-if: substrate shifts]`

§5.1 (telemetric framework — calibration thresholds empirical).

### C.4 `[methodological | review-if: vendor landscape changes]`

§3.6 (Vendor Selection routine).

### C.5 `[vendor-dependent | review-if: orchestration vendor changes]`

§8.1 (Claude Project recommendation), §8.2 (session history mechanism).

### C.6 `[vendor-dependent | review-if: vendor landscape changes]`

§4.5 (Claude-baseline + escape hatch list).

### C.7 `[operator-scaffolding | stable]`

§10.1.1 (SP-1 ext Canonicity), §10.1.2 (SP-12 Bounded-Search Disclosure),
§10.1.3 (SP-13 Substrate Declaration), §10.1.4 (SP-10 Verify state
before recommending), §10.1.5 (SP-14 Filename Discipline), §10.2.1
(SP-8 Canonical Authority — narrowed).

### C.8 `[empirical | review-annually]`

§16 (empirical calibration items — collectively; individual items
inherit calibration trigger).

**Tag count summary.**

| Axis 1 \ Axis 2 | stable | review-if | review-annually | Total |
|---|---|---|---|---|
| structural | 36 | 0 | 0 | 36 |
| methodological | 9 | 2 | 0 | 11 |
| vendor-dependent | 0 | 3 | 0 | 3 |
| operator-scaffolding | 6 | 0 | 0 | 6 |
| empirical | 0 | 0 | 1 | 1 |
| **Total** | **51** | **5** | **1** | **57** |

---

## Appendix D — v1.x → v2 surface drift

Construct-by-construct mapping for operators familiar with v1.10.4.
Direct carryforwards (🔁) and new constructs (🆕) marked; surface drift
items documented with the change.

### D.1 Sessions and lifecycle

| v2 construct | v1.10.4 counterpart | Disposition |
|---|---|---|
| Orchestration session | Setup + convergence sessions (PRISM.md attached) | v2 names the split that v1.x ran inconsistently |
| Execution session | Phase 1 specialist prompt session | Hardened contract via triple |
| Update session | — | 🆕 |
| Master | Starter | Renamed; functionally same |
| *What's next* | TRI-21 progress pointer (single ID) | Reshaped to full artifact |
| Lens Library | — | 🆕 — core v2 architecture |

### D.2 Probes

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
  (§3.6).

### D.3 Monitors

| v2 | v1.x | Disposition |
|---|---|---|
| M1 Missing Inputs | M1 Missing Inputs | 🔁 |
| M2 Version Drift | M2 Version Drift | 🔁 — surface narrowed to filename version |
| M3 Sequence Violation | M3 Sequence Violation | 🔁 |
| M4 Ambiguous Ask | M4 Ambiguous Ask | 🔁 |
| M5 Context Pressure | M5 Attachment Pressure + M12 Conversation Pressure | Merged into single telemetric monitor |
| M6 Premise Shift | M6 Premise Shift | 🔁 — surface broadened (premises now read from Setup artifacts) |
| M7 Claim Conflict | M7 Assumption Conflict | Renamed — v1.x had Assumption Register; v2 reads finding-vs-finding directly |
| M8 Stale Source | M8 Stale Source | 🔁 — surface narrowed (audit evidence only; framework-anchor staleness is point refresh §7.4) |
| M9 Convergence Type Drift | M9 Convergence Type Drift | 🔁 — surface broadened (also catches dispatch-mode treatment errors) |
| M10 Rerun/Fix | M10 Rerun/Fix | 🔁 |
| M11 Layer 2 Readiness | M11 Layer 2 Readiness | 🔁 |
| M12 Result Completeness Check | (slot was M12 Conversation Pressure — retired) | 🆕 in v2 (slot reused; v1.x M12 absorbed into M5) |

### D.4 Standing Principles

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
| SP-10 | SP-10 (Verify state before recommending) | 🔁 as named principle; mechanics live in Vendor Selection §3.6 |
| SP-12 | — | 🆕 Bounded-Search Disclosure |
| SP-13 | — | 🆕 Substrate Declaration |
| SP-14 | (extracted from SP-8) | 🆕 — Filename Discipline |

### D.5 Other constructs

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

### D.6 Nomenclature changes

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

All paste-ready blocks in one place.

### E.1 PRISM Execution Envelope

```
━━━ PRISM EXECUTION ENVELOPE ━━━
Prompt ID:          [identifier — purpose/title]
Project:            [project name]
Master version:     [filename of Master at dispatch time]
Prompt digest:      [orchestration-generated short identifier; copy verbatim into Output]
Vendor:             [vendor] | multi-vendor
Dispatch shape:     equivalence | split | limitation-named
Dispatch rationale: [one positive-framing line per variant]
Vendor config:      [vendor-specific config flags]
Session hygiene:    [fresh session, project attachment posture, web search on/off]
Tools:              [vendor tools requested; reserved slot for plugins/skills]
Attachments:        [filename, filename, ...]
Expected output:    [filename to download as]
Operator hints:     [zero or more one-line cues]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### E.2 PRISM Execution Self-check

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
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### E.3 PRISM Execution Output

```
━━━ PRISM EXECUTION OUTPUT ━━━
Prompt ID:        [identifier — purpose/title]
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

### E.4 Vendor Selection block

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

```
━━━ PRISM SESSION HANDOFF ━━━
Project:                [name]
Master version:         [filename of attached Master]
Lens Library version:   [v0.9 | filename pinned]
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

#### Decision brief

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

#### Stakeholder register

```
## Stakeholder register

| Role | Stake | Decision power | Communication channel |
|---|---|---|---|
| [name] | [decision/outcome stake] | [yes/advisory/none] | [channel] |
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

```
## Dispatch register

| Prompt ID | Recommended (Vendor / config) | Executed (Vendor / config) | Status | Convergence ref |
|---|---|---|---|---|
| P2.3 | Gemini Pro DR / DR ON | Claude Opus 4.7 / standard | substituted | layer1-p2.3 |
| P2.4 | Claude Opus 4.7 / standard | — | dispatched | — |
| P2.5 | multi-vendor / equivalence | partial (2 of 3) | partial | layer1-p2.5 |
```

### E.11 Rerun Register

```
## Rerun Register

| Prompt ID | Reason | Source Monitor | Status |
|---|---|---|---|
| P2.1 | M6 — premise shifted | M6 HIGH P2.4 ingestion | overdue |
```

---

## Appendix F — Standing Principles full text

Each Standing Principle stated in full, in canonical order.

### SP-1 (extended) — Canonicity preservation

`[operator-scaffolding | stable]`

Never silently reconstruct missing canonical files from memory. v2
extends this to cover *offers* to reconstruct: do not propose
regeneration as a routine option.

Order of operations when a canonical artifact is missing:

1. Locate the original — session history, file system, past chats.
2. If location fails, surface specific consequences: authenticity loss,
   schema drift, silent contamination.
3. Offer regeneration only as a documented last resort, with
   consequences named.

Never frame regeneration as "deterministic" or "low-cost" unless it
genuinely is. Cross-ref: §10.1.1, §14.

### SP-2 — Defer non-critical fixes to natural touchpoint

`[methodological | stable]` *(carryforward from v1.10.4)*

Non-critical issues queue against priority tiers in *What's next*; fix
at the next aligned step rather than mid-flight. M10 (Rerun) fires when
no natural touchpoint exists.

### SP-3 — DISSOLVED in v2

v1.10.4's SP-3 ("Convergence is part of prompt delivery") is
incompatible with v2's orchestration/execution split. Convergence moves
to orchestration; per-prompt convergence checklists drop from the
atomic prompt template (§12).

### SP-4 — Every Monitor produces visible output

`[methodological | stable]` *(carryforward)*

Silent monitors are useless monitors. Applies to all M1–M12 fires.
*What's next* surfaces every fire at appropriate severity.

### SP-5 — No heuristic guessing on ambiguous input

`[methodological | stable]` *(carryforward)*

Wherever orchestration parses operator input, ambiguity halts and
asks. Pairs with M4 (Ambiguous Ask) firing.

### SP-6 — Rebuild at threshold

`[methodological | stable]` *(carryforward)*

Build-method discipline. Threshold ≤~8 sequential edits → str_replace;
above → create_file rebuild via deterministic transformation script.
Applies to v2 framework builds, Library Update sessions, large Master
rewrites.

### SP-7 — File delivery is mandatory

`[methodological | stable]` *(carryforward)*

Every orchestration session that updates Master delivers a file. Every
execution session that produces Output delivers a file. Every Update
session that produces a new Library file delivers a file. Reinforced
structurally by the triple contract's file-based Output (§3.2.3).

### SP-8 (narrowed) — Canonical Authority

`[operator-scaffolding | stable]`

The file delivered via `present_files` is canonical for that project
state. Any edit made outside a Claude session must be flagged at the
start of the next session so M2 (Version Drift) can reconcile.

Filename discipline (the look-alike disambiguation pattern) extracted
to SP-14.

### SP-9 — Silence is never consent

`[methodological | stable]` *(carryforward)*

Wherever operator decision is required: close-loop declarations,
ratification, ambiguity escalation, migration override at 🔴, Project
recommendation accept/decline. Active operator action required;
no defaults-on-timeout.

### SP-10 — Verify state before recommending

`[operator-scaffolding | stable]` *(carryforward as named principle)*

When orchestration generates recommendations that depend on current
platform / vendor / model / best-practice state, verify before
recommending. Mechanics live in Vendor Selection (§3.6); principle
travels to point refresh (§7.4), Update sessions (§7.5), and any
future recommendation surface.

### SP-12 — Bounded-Search Disclosure

`[operator-scaffolding | stable]` *(new in v2)*

When orchestration answers on the basis of a bounded retrieval, the
default posture is to disclose the bound. "I found no evidence"
insufficient; "I found no evidence within [named scope]; confirm
before I proceed" is required. Cross-ref: §10.1.2.

### SP-13 — Substrate Declaration

`[operator-scaffolding | stable]` *(new in v2)*

PRISM-loaded sessions verify substrate against declared target before
executing dependent work. If self-identification doesn't match
declared target, or can't be determined, session halts and asks
operator. Operationalized inside execution sessions via the Self-check
block (§3.2.2); orchestration-side via session-open verification.
Cross-ref: §10.1.3.

### SP-14 — Filename Discipline

`[operator-scaffolding | stable]` *(new in v2; extracted from SP-8)*

Look-alike files produced by multi-vendor execution use the structured
filename pattern per §11. The em-dash separator stays cross-platform
safe. M1 (Missing Inputs) parses attached filenames against expected
patterns; mis-named files are flagged at session-open. Cross-ref:
§10.1.5, §11.

---

## Appendix G — Embedded Lens Library v0.10

The content below is an embedded, byte-for-byte copy of the canonical
`lens/PRISM_lens_library.md` v0.10 (tag `prism-lens-v0.10`) at the
time of this PRISM release. The standalone file remains authoritative
for the catalog's own evolution; this embedded copy is the **default
Library source** for orchestration so a single PRISM.md attachment is
sufficient (mobile-first singleton, per §7.1).

When PRISM and the embedded copy disagree (e.g., after the standalone
Library is bumped via an Update session, before the next PRISM minor
version embeds the new content), the standalone file is authoritative
on catalog content and PRISM.md's Appendix G is authoritative on
"what shipped with this PRISM version." Operators on the standalone
Library at a newer version pin to that version explicitly and attach
the standalone file alongside the Master (§7.1).

---

# PRISM Lens Library — v0.10 (pre-release)

**Version:** 0.10
**Release date:** 2026-04-25
**Status:** pre-release standalone artifact; awaiting real-world calibration before promotion to v1.0 stable
**Scope:** framework-neutral reference catalog; not a methodology, not a rubric, not framework-specific

---

## What this is

The PRISM Lens Library is a reference catalog of 23 audit-scope lenses. Each entry is a (material-question × evidence-class × specialist-type) triple that names a specific class of silent omission an audit can plausibly miss.

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
4. **Anchor currency.** Two entries carry version-pinned rubric anchors (LL-D-002 WCAG 2.2, LL-D-005 OWASP ASVS 5.0.0). At v0.10, both anchored entries carry `verification_basis: schema-introduction-only` to signal that `last_verified: 2026-04-24` reflects schema-introduction date, not an independently performed currency check. Run point refresh (per the adopting framework's Setup) before applying those lenses at the depth the anchor implies. The `verification_basis` field flips to `independent-review` after a real currency review is performed.
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
- `informed_by:` frameworks, standards, and practice traditions that inform the lens (indicative, not exhaustive; not a compliance claim)
- `failure_mode:` the silent omission this lens catches, in plain language
- `minimum_scope_binding:` the minimum scope commitment that counts as "covered" for this lens

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

## Domain lenses (18 entries across 6 packs)

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
  informed_by:
    - Porter five-forces and strategy literature
    - Jobs-to-be-Done (substitute analysis)
    - Competitive-intelligence practice
  failure_mode: >
    Audit overstates novelty or fit because no
    realistic comparator set — especially
    substitutes and do-nothing — was named; a
    buyer-side read surfaces the gap.
  minimum_scope_binding: >
    One pass names rivals, substitutes, and
    do-nothing; differentiation is stated in
    buyer-language and backed by evidence.

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

- **Total entries:** 23 (5 universal + 18 domain across 6 packs)
- **Rubric-anchored entries:** 2 (8.7%) — LL-D-002 (WCAG 2.2, October 2023), LL-D-005 (OWASP ASVS 5.0.0, May 2025)
- **`specialist_type:` population:** 23 / 23
- **`last_verified:` population on anchored entries:** 2 / 2 (all dated 2026-04-24)
- **`verification_basis:` population on anchored entries:** 2 / 2 (all `schema-introduction-only` at v0.10; flips to `independent-review` after real currency review)

## Version and status

**v0.10 pre-release.** Awaiting at least one real-world calibration application before promotion to v1.0 stable. Calibration may occur either as standalone use on a real audit or through a framework-integration (Phase B) effort against a committed target audit framework.

v0.10 is a schema-fidelity bump on top of v0.9: same 23 lenses, same content, same triggers. The change is the addition of `verification_basis:` on the two rubric-anchored entries, gating any adopting framework's freshness logic against silently treating schema-introduction dates as performed currency checks.

Feedback, patches, and field-observations welcome. Ongoing currency of rubric anchors is the responsibility of the adopting framework or engagement; v0.10 ships with anchors current as of 2026-04-24 (`schema-introduction-only` basis) and does not include an automated currency-update mechanism.

*End of PRISM Lens Library v0.10.*

---

## 18. Project, feedback, updates `[structural | stable]`

PRISM is an open framework. This file ships with enough information to
locate the project, check for newer versions, and feed observations back
to the maintainer.

### 18.1 Project identity

- **Repository.** `https://github.com/Ronkupper/PRISM`
- **Maintainer.** Ron Kuper ([@Ronkupper](https://github.com/Ronkupper))
- **Framework version.** v2.0.1 (this file)
- **Embedded Lens Library version.** v0.10 (Appendix G)
- **Release date.** 2026-04-25
- **Licensing.** Documentation under CC BY 4.0; any code under MIT;
  Code of Conduct under CC BY-SA 4.0. Full license texts in the repository.

### 18.2 Resource fetch convention

The framework and its companion artifacts are addressable on `main` of the
public repository under stable raw URLs. Orchestration sessions running on
substrates with web access can fetch these directly; mobile operators
without that capability can paste the URLs into a browser and download.

| Resource | Stable URL | Pinned URL |
|---|---|---|
| Framework (this file) | `https://raw.githubusercontent.com/Ronkupper/PRISM/main/PRISM.md` | `…/PRISM_v2_0_1.md` |
| Lens Library | `https://raw.githubusercontent.com/Ronkupper/PRISM/main/lens/PRISM_lens_library.md` | `…/lens/PRISM_lens_library_v0_10.md` |
| Framework version stamp | `https://raw.githubusercontent.com/Ronkupper/PRISM/main/VERSION` | — |
| Lens version stamp | `https://raw.githubusercontent.com/Ronkupper/PRISM/main/lens/VERSION` | — |
| Releases index | `https://github.com/Ronkupper/PRISM/releases` | — |
| Release at this version | — | `https://github.com/Ronkupper/PRISM/releases/tag/v2.0.1` |

The two `VERSION` endpoints exist as cheap currency checks: each is a
single-line file containing the current version on the corresponding
release track. Reading them does not require parsing the framework or
the Lens body. New resources added to the project follow the same path
pattern (a stable file on `main`, a `VERSION` stamp where versioned).

### 18.3 Currency check at session open `[methodological | stable]`

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
   `Framework v2.0.1 attached; v{published} available at {releases URL}.`
   `Lens v0.10 attached; v{published} available at {releases URL}.`
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

- **Bugs and concrete defects.** GitHub Issues on the public repository,
  using the issue templates under `.github/ISSUE_TEMPLATE/`.
- **Ideas, proposals, observations from real use.** GitHub Discussions
  on the public repository, *Ideas* category. Field observations from
  applying PRISM to real audits are particularly valuable: the framework
  ships with several rev. 1 draft thresholds (M5 bands, Update session
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

To cite PRISM in published work, see `CITATION.cff` in the repository.
A short attribution suitable for inline use:

> Kuper, R. (2026). *PRISM: A Framework for LLM Research and Audits*
> (v2.0.1). https://github.com/Ronkupper/PRISM

---

*End of PRISM v2.0.1 framework operating document.*
