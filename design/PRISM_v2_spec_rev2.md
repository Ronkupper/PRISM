# PRISM v2 — Specification

**Status:** Specification rev. 2. Mechanics for v2.0 build.
**Date:** April 2026 (rev. 2)
**Supersedes:** PRISM_v2_spec_rev1_draft.md (rev. 1, April 2026), retained as historical provenance.
**Inputs:** `PRISM_v2_rev8_design_document.md` (direction-of-record); `PRISM_lens_library.md` v0.9 (canonical at `lens/PRISM_lens_library.md` in the public repo, tag `prism-lens-v0.9`).
**Applies to:** v2.0 and later. Projects under v1.10.4 remain on v1.10.4 (design doc §11).

**Capture discipline.** Per the rev. 8 design-doc top-of-file note: decisions captured at current fidelity; refinement expected in subsequent revisions. This rev. 1 draft picks design alternatives directly (per D6 closure) and captures alternatives-considered in §16 flagged-items register. Items left under-specified are flagged, not papered over.

**Citation convention.** Section references prefixed `DD.` point to the rev. 8 design document (e.g., `DD.§4.1.1`); references prefixed `LL.` point to the Lens Library v0.9 (e.g., `LL.LL-U-001`). Internal references use bare section numbers.

---

## 1. Scope of this specification

### 1.1 What this spec covers

- **Architecture mechanics** (DD.§4): triple contract (Envelope + Self-check + Output), Master, *What's next*, forward-compatibility commitments, Vendor Selection.
- **Setup mechanics** (DD.§5): iterative refinement, three-layer readiness, seven probes, Setup artifacts, strategy stability.
- **Library integration mechanics** (DD.§6): how the Library plugs into Setup; currency maintenance (point refresh, Update session). The catalog itself is `lens/PRISM_lens_library.md` v0.9 — not duplicated here.
- **17 design gaps** (DD.§13.1, DD.§13.2): prompt-package engine + context-pressure framework. Rev. 2 separates rev. 1's Probe 2 into Adversarial Scope (Setup) + Vendor Triangulation (Layer-1).
- **2 parked v2 design ideas** (DD.§13.3): Claude Project as Setup recommendation; session history as validation/recovery.
- **3 spec-session deferrals** (DD.§14): M2 fate, Attachment warnings field, M8 vs. DD.§6.6 scope.
- **Monitor specifications** (DD.§7.2): M1–M11 mechanics in orchestration.
- **Standing Principles** introduced or extended in v2 (DD.§2.5).

### 1.2 What this spec does not cover

- **Re-stating principle-level direction.** This spec assumes the design document. It implements; it does not re-debate.
- **The Library catalog.** The catalog is its own canonical artifact. v0.9 ships pinned at `prism-lens-v0.9`.
- **Build artifacts.** `PRISM_v2_0.md` and `PRISM_v2_0_0.md` (DD.§12.3) are produced from this spec in Phase 4.
- **Release notes.** Operator-facing release notes are a Phase 5 artifact.
- **Empirical-only items.** Probe-iteration calibration (DD.§5.3 floors/ceilings), point-refresh fatigue (DD.§11 item 14), domain-practitioner lens accretion (DD.§11 item 15), multi-vendor Self-check verification (DD.§4.1.1 footing). Flagged as post-release calibration items in §16.

### 1.3 Tag conventions

Decisions in this spec carry the same two-axis tag system as the design document (durability axis × review-trigger axis). New tags are introduced where a decision in this spec needs one; tags are not duplicated when a decision merely implements an already-tagged direction.

---

## 2. System overview

**Read this first.** Map of every PRISM v2 construct, what it touches, and when it fires. Use this section to locate any construct's full mechanics in §3–§12. §10 traces the constructs through a worked audit example.

This section is descriptive — it points; it does not define. Definitions live in the per-construct sections.

### 2.1 Construct list

PRISM v2 has the following constructs, grouped by category:

**Sessions** (§3.1)
- Orchestration session — Claude session with framework attached
- Execution session — vendor session running a single dispatched prompt
- Update session — out-of-band, operator-gated, maintains Library currency

**Phases**
- P0.x — Setup (iterates against draft Prompt Strategy)
- P1+ — Execution (dispatched prompts run; convergence absorbs results)
- P0→P1 boundary — three-layer readiness clears (§6.2)

**Probes** (§6.3) — Setup-time grading constructs
- P1 Coverage grading · P2 Adversarial Scope · P3 Decision Framing · P4 Pre-mortem · P5 Falsifier · P6 Domain Reconnaissance · P7 User Voice

**Monitors** (§11) — orchestration-side checks
- M1 Missing Inputs · M2 Version Drift · M3 Sequence Violation · M4 Ambiguous Ask · M5 Context Pressure · M6 Premise Shift · M7 Claim Conflict · M8 Stale Source · M9 Convergence Type Drift · M10 Rerun/Fix · M11 Layer 2 Readiness · M12 Result Completeness Check

**Top-level artifacts**
- Master (§3.3) · *What's next* (§3.4) · Lens Library · Migration handoff (§5.4) · Convergence delta (§4.3.1)

**Master sections** (state lives here)
- Decision brief · Stakeholder register · Claim inventory · Jurisdiction map · Prompt Strategy · Dispatch register · Findings · Rerun Register · Learnings Register · Changelog · Open dispatches/monitors/probes lists

**Execution contract** (triple, §3.2)
- Envelope (inbound) · Self-check (substrate verification) · Output (outbound)

**Standing Principles** (§12)
- v2-new/extended: SP-1 ext, SP-12, SP-13, SP-14
- Carryforward: SP-2, SP-4, SP-5, SP-6, SP-7, SP-8 (narrowed), SP-9, SP-10
- Dissolved: SP-3

**Mechanisms**
- Vendor Selection (§3.6) · Vendor Triangulation (§4.3) · Bump atomicity (§9.1) · Telemetric framework (§5.1) · Point refresh (§7.4) · Update session (§7.5) · Continuous-curation (§5.3) · Strategy stability (§6.5) · Three-layer readiness (§6.2) · Two-layer convergence · Triple contract

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

Per-construct lifecycle / reads / writes / triggers. Cross-refs to detail sections.

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
| P3 Decision Framing | First P0 turn (once) | Subject brief | Decision brief, Stakeholder reg | §6.3.3 |
| P4 Pre-mortem | P0.x turn-close (iterates) | Draft strategy, Decision brief | Failure-mode list | §6.3.4 |
| P5 Falsifier | Late P0 (once) | Decision brief | Falsifiers section | §6.3.5 |
| P6 Domain Reconnaissance | Early P0.x (iterates) | Subject, web (live) | Jurisdiction map, authoritative-source citations | §6.3.6 |
| P7 User Voice | Early P0.x (iterates) | User-facing surfaces, web | User-signal list | §6.3.7 |

**Monitors** — orchestration-side; M12 (rev. 2) replaces v1.x M12 (Conversation Pressure, retired)

| Monitor | Lifecycle | Reads | Writes | Trigger | Detail |
|---|---|---|---|---|---|
| M1 Missing Inputs | Per session-open + per turn | Session attachments, Output Attachment-warnings | M1 fire | Required attachment absent | §11.1.1 |
| M2 Version Drift | Per session-open | Master metadata, expected version | M2 fire | Master version ≠ expected | §11.1.2 |
| M3 Sequence Violation | Per turn (op declaration) | Prompt Strategy, op input | M3 fire | Step before prereq | §11.3.1 |
| M4 Ambiguous Ask | Per turn (op input) | Op turn content | M4 fire | Cannot confidently parse | §11.1.3 |
| M5 Context Pressure | Per turn-close | 7 telemetric signals | Band header | Every turn-close | §5.2 |
| M6 Premise Shift | Per Layer-1 ingestion | New finding, Setup artifacts | M6 fire | Premise invalidated | §11.2.1 |
| M7 Claim Conflict | Per Layer-1 ingestion | New finding, prior findings | M7 fire | Two findings incompatible | §11.2.2 |
| M8 Stale Source | Per Layer-1 ingestion | New finding's cited sources, web | M8 fire | Source invalidated | §11.2.3 |
| M9 Convergence Type Drift | Per Layer-1 + Layer-2 | Convergence step type | M9 fire | Wrong-posture convergence | §11.1.5 |
| M10 Rerun/Fix Required | Multi-source (chain or op) | Trigger source | Rerun Register | Rerun condition | §11.3.2 |
| M11 Layer 2 Readiness | Per turn-close | Dispatch register, Rerun reg, Open monitors | What's next candidate | Layer 2 conditions met | §11.3.3 |
| M12 Result Completeness | Per Layer-1 ingestion | New finding's domain coverage | M12 fire | Domain coverage gap inside finding | §11.2.4 |

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
| Bump atomicity | Per Master version increment | §9.1 |
| Telemetric framework | Per turn-close | §5.1 |
| Point refresh | Per Setup probe iteration | §7.4 |
| Continuous-curation | Per turn-close (band ≥🟡) | §5.3 |
| Strategy stability | Per Layer-1 trigger | §6.5 |
| Three-layer readiness | Per P0→P1 boundary | §6.2 |
| Triple contract | Per dispatch | §3.2 |

**Standing Principles** — persistent posture; not discrete fires

| SP | v2 status | Detail |
|---|---|---|
| SP-1 ext Canonicity | Extended in v2 | §12.1.1 |
| SP-2 Defer non-critical | Carryforward | §12.2.2 |
| SP-3 (dissolved) | — | §12.2 |
| SP-4 Monitors visible | Carryforward | §12.2.2 |
| SP-5 No heuristic guessing | Carryforward | §12.2.2 |
| SP-6 Rebuild at threshold | Carryforward | §12.2.2 |
| SP-7 File delivery mandatory | Carryforward | §12.2.2 |
| SP-8 Canonical authority (narrowed) | Carryforward (narrowed) | §12.2.1 |
| SP-9 Silence not consent | Carryforward | §12.2.2 |
| SP-10 Verify state before recommending | Carryforward as named principle | §12.1.4 |
| SP-12 Bounded-search disclosure | New in v2 | §12.1.2 |
| SP-13 Substrate declaration | New in v2 | §12.1.3 |
| SP-14 Filename discipline | New in rev. 2 | §12.1.5 |

### 2.4 Lifecycle slots

Every construct fires in exactly one lifecycle slot. (Probe 2 in rev. 1 fired in two — the rev. 2 split resolves that.)

| Slot | What fires here |
|---|---|
| Setup-only | All probes (P1–P7) |
| Per session-open | M1 (also fires per-turn), M2 |
| Per orchestration turn | M3, M4, M5, M11, *What's next* write, Master append |
| Per dispatch | Envelope production, Self-check execution, Output return, Vendor Selection |
| Per Layer-1 ingestion | M6, M7, M8, M12, Vendor Triangulation (if applicable), reconciliation |
| Per Layer-2 synthesis | M9 (also Layer-1) |
| Out-of-band | Update session, point refresh (in-Setup) |
| 🔴 band | Migration handoff |
| Persistent posture | All Standing Principles |

### 2.5 Band legend

Bands are M5's output; they drive curation and migration posture. Per-band table in §5.6.

- 🟢 **Comfortable.** Silent. No intervention.
- 🟡 **Getting warm.** Curation observation in *What's next*. Migration available at next natural seam.
- 🟠 **Curate now.** Active curation. Migration strongly recommended at immediate next seam.
- 🔴 **Migrate.** Migration handoff produced; fresh session.

### 2.6 Cross-section quick-find

If you need to find:

- **A specific construct's full mechanics** → §2.3 construct card → cross-ref to detail
- **How constructs flow in a real audit** → §10 worked example
- **Why a rev. 1 construct was renamed or restructured** → §16 flagged-items register
- **What changed from v1.10.4** → Appendix C v1.x → v2 surface drift table
- **Decision rationale on something** → DD.§ reference inside the relevant spec section header

---


## 3. Architecture mechanics (DD.§4)

### 3.1 Two session types — operating spec

**Orchestration session.** A Claude session with the framework attached.

- *Loaded artifacts at session open*: the framework file (PRISM v2.0 Skill or attached `.md`); the Master; the Lens Library; the Prompt Strategy; subject-brief documents.
- *Outputs*: Master updates, *What's next* artifacts, Envelopes for next dispatch, convergence findings, Monitor fires.
- *Closes by*: writing *What's next* to the Master and surfacing it for the operator.
- *Vendor*: Claude (Opus 4.6/4.7 verified at rev. 1 draft; other Claude models report-worthy per DD.§3.5 beta posture).

**Execution session.** A vendor session running a single dispatched prompt.

- *Loaded artifacts*: only what the Envelope's `Attachments:` field names. Framework not attached.
- *Outputs*: a single `.md` file wrapped in PRISM Execution Output signature.
- *Closes by*: producing the file and instructing the operator on filename and next action (per Envelope's `Expected output:` and the Output's `Operator next:`).
- *Vendor*: per the Envelope's `Vendor:` field. Any LLM the strategy specified.

### 3.2 The triple contract (DD.§4.1.1)

Three blocks — Envelope (inbound), Self-check (between envelope and task body), Output (outbound). All three are visually distinctive, self-contained, and produced by orchestration's Vendor Selection step (§3.6) at dispatch time. `[structural | stable]`

#### 3.2.1 PRISM Execution Envelope — full schema

```
━━━ PRISM EXECUTION ENVELOPE ━━━
Prompt ID:          [identifier — purpose/title]
Project:            [project name]
Master version:     [filename of Master at dispatch time]
Vendor:             [vendor] | multi-vendor
Dispatch shape:     equivalence | split | limitation-named
Dispatch rationale: [one positive-framing line per variant; see §4.1]
Vendor config:      [vendor-specific config flags]
Session hygiene:    [fresh session, project attachment posture, web search on/off]
Tools:              [vendor tools requested; reserved slot for plugins/skills]
Attachments:        [filename, filename, ...]
Expected output:    [filename to download as]
Operator hints:     [zero or more one-line cues; see §3.2.4]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Field semantics.**

- `Prompt ID` — short unique identifier + purpose/title, unrelated to phase. Per DD.§11 item 1.
- `Master version` — the filename of the Master that was current when this Envelope was produced. Used for reconciliation if state drifts.
- `Vendor` — single vendor name (`Claude Opus 4.7`, `Gemini Pro Deep Research`, `Perplexity`, `ChatGPT o-series`) or the literal `multi-vendor`.
- `Dispatch shape` — see §4.1 for the three modes.
- `Dispatch rationale` — one positive-framing line per variant. See §4.2.
- `Vendor config` — vendor-specific configuration (e.g., `Deep Research ON, extended thinking ON`).
- `Session hygiene` — substrate setup the vendor session must satisfy.
- `Tools` — vendor tool slot. v2 default: `web search ON/OFF`. Reserved structural slot for future plugin/skill specification (DD.§4.4).
- `Attachments` — comma-separated filenames the operator must attach. Order is significant where the prompt body references attachments by position.
- `Expected output` — the filename the operator should download the produced file as. Naming convention: `[project]_[promptID]_[vendor].md`.
- `Operator hints` — zero or more one-line cues. See §3.2.4.

#### 3.2.2 PRISM Execution Self-check — full schema

The Self-check operationalizes SP-13 (§6.4) inside the execution session. It sits between the Envelope and the task body.

```
━━━ PRISM EXECUTION SELF-CHECK ━━━
Before doing the task:

1. State what model/vendor you are and what session
   state you can introspect (mode, thinking setting,
   tools enabled).
2. Compare to the Envelope's Vendor and Mode fields
   above.
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

- Session must self-identify before touching task content. Self-identification is best-effort honest — vendors that cannot introspect a field hedge on it rather than fabricate.
- Mismatch halts the task and emits a Self-check report. The report is the deliverable until the operator confirms.
- "Confirmation to proceed" is a positive operator action (a message in the conversation), not an inferred consent from continued attachment.

**Multi-vendor empirical footing.** Verified on Claude Opus 4.6/4.7 and Sonnet 4.6 at rev. 1 draft. Gemini, ChatGPT, Perplexity behavior under this block is **report-worthy finding** per DD.§3.5 — operators should report divergences. Flagged in §16.

#### 3.2.3 PRISM Execution Output — full schema

Every execution session produces a `.md` file whose contents are wrapped in this signature.

```
━━━ PRISM EXECUTION OUTPUT ━━━
Prompt ID:        [identifier — purpose/title]
Project:          [project name]
Master version:   [from Envelope]
Vendor:           [vendor that actually executed; see §4.10]
Vendor config:    [config actually applied at execution]
Schema version:   output-v1
Date:             [YYYY-MM-DD]
Prompt hash:      [first 6 chars of hash of the prompt body]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[findings content]

━━━ END PRISM EXECUTION OUTPUT ━━━
Operator next:        [download instruction; attach instruction]
Attachment warnings:  [optional; one line per warning; see §12.2]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Field semantics.**

- `Vendor` and `Mode` reflect *executed* state, not *recommended* state. This is the field orchestration reads for recommended-vs-executed reconciliation (§4.7).
- `Schema version` — currently `output-v1`. Bumps when the Output block's structure changes; orchestration's Layer-1 convergence flags incompatibilities at ingestion (DD.§4.1.1 *Why the contract is load-bearing*).
- `Prompt hash` — first 6 hex chars of SHA-256 of the prompt body (excluding signature blocks). Lets orchestration verify that the file came from the prompt orchestration thinks it did.
- `Operator next` — download filename + attachment instruction for the next orchestration turn.
- `Attachment warnings` — populated only when warranted. See §12.2 for trigger conditions.

**Production discipline.** The execution session produces the file via the vendor's file-creation surface (Claude `create_file`; ChatGPT Canvas; Gemini's file generation). Where the vendor cannot produce a file, fallback is delimited content rendering with explicit warning that paste fallback has known clipboard-fidelity issues (DD.§4.1.1 *Why v2 delivers via file*).

#### 3.2.4 Operator hints — emission discipline

Hints are optional one-line cues keyed to the upcoming action.

**Emission rules.**

- Fire only when a cue applies to *this* dispatch. Routine dispatches carry zero hints.
- One line per hint; pointer to Appendix E (DD's mobile operator survival guide), not an inline essay.
- No hint that duplicates a Monitor fire.
- Substrate calibration attribution where non-obvious — `(Claude mobile, Samsung)`. Mismatched substrates self-diagnose rather than silently confuse.
- Hints surface in two places: in the Envelope's `Operator hints:` field when the next action is a dispatch; in the *What's next* artifact (§3.4) when the next action is not a dispatch (review, ratify, save-to-cloud).

**Catalog of hint types** (rev. 1 draft; expandable):

- `Save output to cloud drive after download, before switching to the next vendor (see E.5).`
- `On Samsung, expect indexing delay on the downloaded file (E.1).`
- `If Gemini mobile fails to download, retry in Firefox Desktop mode (E.2).`
- `Run [vendor] outside any project so it isn't distracted by project memory.`
- `Re-attach Master and Lens Library at session open.`
- Project-specific cues from the operator's documented preferences (post-release).

### 3.3 The Master — full mechanics

**Filename convention.** `[project_name]_prism[version]_master_[phase-derived versioning].md`. E.g., `solace_audit_prism2.0_master_p2.3.md`.

**Lifecycle.**

- *Created* at Setup P0.1 (first orchestration turn).
- *Updated* at every orchestration turn-close, regardless of band state. Updates are append-mostly (Changelog gains a line; relevant register sections gain entries). Continuous-state mechanic per §5.5.
- *Filename version bumps* at phase boundaries (P0→P1, P1→P2). Sub-version increments at convergence rounds within a phase (P2.1 → P2.2). Schema version increments tracked in the Master's metadata header.
- *Single file by principle* — no parallel Masters. Multiple-Master state is itself a Monitor fire (M2 Version Drift).
- *Authoritative copy* — operator's locally-attached Master at session open is authoritative for that session. Cloud-drive copies (Appendix E.5 from DD) are durable persistence, not authority.

**Required sections.**

- Metadata header: project name, current Master version, Schema version, last updated.
- Decision brief (DD.§5.4 Setup artifact).
- Stakeholder register (DD.§5.4 Setup artifact).
- Claim inventory (DD.§5.4 Setup artifact).
- Jurisdiction map (DD.§5.4 Setup artifact).
- Prompt Strategy — current ratified version.
- Dispatch register — table of recommended-vs-executed state per prompt (§4.8).
- Findings sections — per-prompt converged findings, with provenance.
- Open dispatches list — prompts not yet closed.
- Active probes list — Setup probes still iterating.
- Open monitors list — M2/M3/M4/M6/M7/M8/M9/M10/M11 fires not yet resolved.
- Learnings Register — cross-project pattern accumulator (DD.§4.2).
- Changelog.

**Optional sections** (populated when applicable to the project):

- Falsifier probe outputs (Probe 5).
- Layer-2 synthesis (when Layer 2 has run).
- External-stakeholder deliverable drafts (when applicable).

**Proportionality** (DD.§4.2). Lean projects keep a lean Master — small dispatch sequences need only a subset of the required sections (metadata, decision brief, dispatch register, findings, Changelog). Spec inclusion of optional sections is operator-discretion at Setup; default is *include sections that earn their place*. Empirical calibration post-release.

**Tag.** `[structural | stable]`

### 3.4 *What's next* — full mechanics

**Lifecycle.** Written at every orchestration turn-close. Replaces in-place; old *What's next* is overwritten. Historical pointers live in the Master's Changelog. `[structural | stable]`

**Required content** (per DD.§4.3):

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

**Candidate ranking ladder** (priority order, ties surfaced for operator):

1. 🔴 context-pressure migration handoff (when band = 🔴).
2. M2/M3/M4 fires (operator-side checks-and-balances) unresolved.
3. Open Rerun Register items overdue (M10 active).
4. M6 HIGH (Premise Shift) unresolved at convergence.
5. Adaptation pending operator approval.
6. Layer 2 readiness (M11) when conditions met *and* operator has not deferred.
7. Next canonical Setup probe iteration (when in P0).
8. Next canonical dispatched prompt (when in P1+ execution).
9. Convergence-round consolidation (Layer 1 batch when ≥2 returns are in).
10. Curation and migration at natural seam (when band ≥ 🟡).

**Tie-handling.** When two or more candidates are within the same priority tier, *What's next* surfaces all of them and asks the operator. SP-9 lineage: silence is never consent.

**Operator escalation format** (when ties surface):
```
Multiple candidates at priority [tier]:
  - A: [candidate] — [rationale]
  - B: [candidate] — [rationale]
Operator pick required before proceeding.
```

### 3.5 Forward-compatibility commitments — spec form (DD.§4.4)

- **Vendor-agnostic execution contract** — the Envelope/Self-check/Output triple is vendor-agnostic by construction. Future automated dispatch plugs in by replacing the operator with an automation layer; contract unchanged.
- **Tools slot in Envelope** — the `Tools:` field is a structural reservation. v2 defaults to `web search ON/OFF`. Future desktop-mode extensions use this slot for plugin/skill enumeration (e.g., `Tools: web search ON, Playwright, Firecrawl`). Spec adds no machinery for this beyond the slot.
- **Execution mode flag at Setup** — Setup carries a session-level flag declaring execution mode. v2 default: `execution_mode: manual_plain_chat`. Reserved values for future modes: `execution_mode: agentic_orchestration`, `execution_mode: plugin_equipped`, `execution_mode: automated_cross_vendor`. Setup validates the value is one of the reserved set; unrecognized values halt Setup with an operator escalation.

These commitments cost the v2 build essentially nothing now and prevent later architectural rework.

### 3.6 Vendor Selection at dispatch (DD.§4.5) — spec

**When it runs.** Every time orchestration is about to produce a dispatch-ready Envelope. Not at Setup time; at dispatch time.

**Three-step routine.**

1. **Refresh.** Orchestration runs a web-search-based currency check on the specific decision: is the recommended vendor still the right call for this prompt shape? Are there known issues this week? Has a newer vendor capability changed the calculus? Output: a 2–4 line refresh note with citations.
2. **Structured outcomes.** Where refresh produces a confident specific recommendation, the configuration is written into the Envelope (`Vendor:`, `Mode:`, `Tools:`). No operator decision required.
3. **Soft outcomes — recommendation bubble.** Where refresh produces a judgment call (vendor X usually but has had issues; vendor Y is a fallback), the soft outcome surfaces as a non-blocking note attached to the Envelope. Operator reads, agrees or overrides via reply.

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

This block is visible in the orchestration session but does not travel into the execution session. The Envelope (without the Vendor Selection block) is what the operator pastes.

**Tag.** `[methodological | review-if: vendor landscape changes]`

---

## 4. Prompt-package engine (DD.§13.1, items 1–6, 9–13)

The architecture in DD.§4 supports the prompt-package engine; this section names and shapes the mechanics.

### 4.1 Single-Envelope-with-spectrum shape (DD.§13.1 item 1) `[structural | stable]`

**Decision.** Single Envelope with a `Dispatch shape:` field carrying one of three values: `equivalence`, `split`, `limitation-named`.

**Mode semantics.**

- **`equivalence`** — dispatch the same prompt body to N vendors, expect comparable outputs. Orchestration's Vendor Triangulation fires at N≥2 (§4.3).
  - `Vendor:` field reads `multi-vendor`.
  - A `Vendor list:` sub-field enumerates the vendors and modes:
    ```
    Vendor list:
      - Claude Opus 4.7 / standard
      - Gemini Pro Deep Research / Deep Research ON
      - Perplexity / Sonar Pro
    ```
  - `Dispatch rationale:` carries one positive-framing line per vendor (§4.2).
  - The operator dispatches to each vendor sequentially or in parallel; each return carries its own Output signature. Orchestration tracks N expected returns.

- **`split`** — split the prompt into vendor-specific sub-prompts; each vendor gets a piece. Synthesis happens orchestration-side.
  - `Vendor:` field reads `multi-vendor (split)`.
  - The Envelope contains nested sub-Envelopes, one per piece, each with its own `Vendor`, `Vendor config`, `Attachments`, `Expected output`.
  - Parent declares synthesis approach: how the pieces compose (sequential dependency, parallel + merge, hierarchical).

- **`limitation-named`** — single vendor; explicit acknowledgment of what is intentionally not chosen and why.
  - `Vendor:` field reads the single vendor.
  - `Dispatch rationale:` includes a `Not chosen:` line naming the alternative considered and the reason for not choosing it. Positive framing per §4.2 — what this dispatch *does*, not deficit framing.

**Operator-legible benefit.** A single Envelope shape across all dispatch shapes. The mode field tells operator and vendor what kind of run this is.

**Alternatives considered.** Captured in §16.

### 4.2 Rationale discipline per dispatch variant (DD.§13.1 item 2) `[methodological | stable]`

**Decision.** `Dispatch rationale:` field holds one positive-framing line per dispatch variant component. Mobile-legible. No deficit framing.

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
    Not chosen: Claude — context window insufficient for this prompt's source base
  ```

**Discipline rules.**

- Each line ≤ 80 characters where possible (mobile legibility).
- Verb-first, value-first phrasing.
- "Not chosen" lines explain the analytical reason, not the access reason (per DD.§3.6 design-authority-without-access-gating).

### 4.3 Vendor Triangulation (DD.§13.1 item 3) `[structural | stable]`

**Decision.** Vendor Triangulation is a Layer-1 convergence pass that fires when the second return arrives in an `equivalence` dispatch. Re-fires as each subsequent return arrives. Tracked via the Master's Dispatch register. Lives outside the probe taxonomy because it operates against returned findings, not draft strategy — single-responsibility separation from Probe 2 Adversarial Scope (§6.3.2).

**Why a separate construct from Probe 2.** Rev. 1 conflated two jobs under "Probe 2": Setup-time strategy adversarial grading + convergence-time cross-vendor finding reconciliation. Different surfaces (draft strategy vs. returned findings), different lifecycles (Setup-only vs. per Layer-1 batch), different output shapes (omission list vs. agreement/divergence delta). Rev. 2 separates them: Probe 2 Adversarial Scope is Setup-only; Vendor Triangulation is convergence-only.

**Trigger.**

- N=1 return: ingested as a single finding, not triangulated. Master records `partial-equivalence: N/expected_N`.
- N=2: Vendor Triangulation fires. Convergence delta produced (§4.3.1).
- N=3+: Re-fires; convergence delta updates incrementally.
- N=expected_N: Delta finalizes; Vendor Triangulation closes for this prompt.

**Convergence delta document** (§4.3.1).

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

**Iterative re-firing.** Each new return triggers a re-run of the delta. Old delta is replaced; the Changelog records the iteration.

**Delta finalization.** When all expected returns are in *and* no new return is expected, the delta finalizes. The Master's findings section absorbs the final delta.

### 4.4 Asymmetric parallel return handling (DD.§13.1 item 4) `[structural | stable]`

**Decision.** Convergence proceeds with whatever returned. Failed dispatches are flagged with named gaps; operator decides whether to re-dispatch.

**Failure handling.**

- Operator declares a dispatch failed via the close-loop mechanic (§4.9): "P2.3 Gemini failed — Deep Research timed out."
- Master's Dispatch register status: `failed: [reason]`.
- Vendor Triangulation proceeds with available returns. Convergence delta notes the dimension that's missing-due-to-failure:
  ```
  Vendor coverage gap: Gemini failed (timeout); Claude + Perplexity converged.
  Long-context many-source synthesis dimension is absent from this delta.
  ```
- *What's next* surfaces re-dispatch as a candidate at next turn-close, ranked by whether the gap materially affects the finding.

**No automatic retry.** Re-dispatch is an operator decision, surfaced as a candidate. Per DD.§3.6 — design-authority-without-access-gating — the framework does not assume the operator can retry on the same vendor.

### 4.5 Claude-baseline feasibility with named-limitation escape hatch (DD.§13.1 item 5) `[structural | stable]`

**Decision.** Default execution stance is "Claude alone is feasible." Multi-vendor or non-Claude is invoked via explicit declaration in the Prompt Strategy. The named-limitation escape hatch (§4.1 `limitation-named`) fires when Claude is genuinely insufficient for the prompt shape.

**When non-Claude default escapes apply** (rev. 1 draft list — Vendor Selection refreshes per dispatch):

- *Live-web breadth* — Perplexity (Sonar/Sonar Pro). Claude's web search exists but is shallower for breadth-recency tasks.
- *Long-context many-source synthesis* — Gemini Pro Deep Research. When source base materially exceeds Claude's context window.
- *Adversarial-style alternative reasoning* — ChatGPT o-series. When the strategy benefits from a structurally different reasoning posture for red-teaming.

**When multi-vendor (`equivalence`) is invoked.**

- Strategy declares it explicitly per prompt.
- Vendor Triangulation is the analytical goal.
- Or operator strategy preference for a specific prompt class.

**Default behavior absent declaration.** Single-vendor Claude dispatch.

**Tag.** `[vendor-dependent | review-if: vendor landscape changes]`

### 4.6 Cost signaling (DD.§13.1 item 6) `[methodological | stable]`

**Decision.** Implicit. No separate `cost:` field. Cost is signaled by:

- *Dispatch shape*: `equivalence` mode N=3 implies ~3× the operator effort and vendor-cost of single dispatch.
- *Vendor selection*: Gemini Deep Research is more time-expensive than Claude default; Vendor Selection's recommendation bubble (§3.6) carries this implicitly via mode rationale.
- *Mode rationale lines*: positive framing + named alternatives carry enough information for the operator to understand the cost tradeoff without an explicit field.

**Why no explicit field.**

- A `cost_estimate:` field would either be inaccurate (vendor pricing changes faster than the framework) or operator-specific (subscription tiers vary). Both fail the contract-minimum test.
- DD.§3.6 access-not-gating posture: cost is operator's information; framework's job is design.

**Operator override.** If operator wants explicit cost framing in *What's next*, they can ask for it; orchestration produces it on-demand. Not a default field in the Envelope.

### 4.7 Recommended-vs-executed reconciliation (DD.§13.1 item 10) `[structural | stable]`

**Decision.** The Output signature carries `Vendor:` and `Mode:` reflecting executed state. Orchestration auto-reconciles against the Envelope's recommended state at Layer-1 ingestion.

**Reconciliation states** (recorded in the Dispatch register):

- *Match* — executed Vendor/config equals recommended. Status: `returned`.
- *Substitution* — executed Vendor or config differs. Status: `substituted`. Both recommended and executed values logged.
- *Missing* — no Output ever returned. Status: `failed` or `skipped` (per close-loop §4.9).

**Reconciliation algorithm** (orchestration-side, at Layer-1 ingestion):

```
1. Read Output signature fields: Executed Vendor, Executed Mode, Schema version,
   Prompt hash.
2. Look up Dispatch register entry for Prompt ID.
3. Verify Schema version compatible.
4. Verify Prompt hash matches expected.
   - If mismatch: flag as "wrong prompt" — operator escalation.
5. Compare Executed Vendor/config to Recommended Vendor/config.
   - If match: status = returned.
   - If differs: status = substituted; log both.
6. Ingest findings into Master's findings section with provenance:
   "P2.3 — executed on [Executed Vendor / Mode]; recommended was
    [Recommended]; absorbed without re-dispatch."
7. Vendor Triangulation (if equivalence mode) updates with this return.
```

### 4.8 Master tracking field — Dispatch register (DD.§13.1 item 12) `[structural | stable]`

**Decision.** Master gains a `Dispatch register` table that tracks recommended-vs-executed state per prompt. Required section per §3.3.

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
- `substituted` — return absorbed; Vendor or Mode differs from recommended.
- `partial` — multi-vendor (`equivalence`) dispatch with N < expected_N returns absorbed.
- `failed` — operator declared failed (§4.9); reason recorded.
- `skipped` — operator declared skipped (§4.9); rationale recorded.
- `closed` — all expected returns received and convergence finalized.

**Status transitions** (machine-readable for orchestration's *What's next* logic):

```
dispatched → returned | substituted | partial | failed | skipped | scheduled
scheduled → returned | substituted | partial | failed | skipped
returned → closed
substituted → closed
partial → returned | substituted | partial | closed (when expected_N met or operator declares closed)
failed → dispatched (re-dispatch) | skipped | closed
skipped → closed
```

### 4.9 Operator-declaration close-loop mechanic (DD.§13.1 item 13) `[structural | stable]`

**Decision.** Defined declaration set. Each declaration closes an open dispatch in a defined way.

**Declarations and effects.**

- **`Done`** — operator attached the Output. Triggers Output reconciliation (§4.7). Dispatch register status updates per §4.8.
- **`Running later`** — dispatch deferred. Status: `scheduled`. Master keeps slot open. *What's next* surfaces it as a candidate at next turn-close (priority tier 8 per §3.4).
- **`Skipping`** — dispatch abandoned. Status: `skipped`. Operator provides rationale (one line). Convergence absorbs the gap.
- **`Failed: [reason]`** — dispatch attempted but failed (vendor error, timeout, format failure). Status: `failed`. *What's next* surfaces re-dispatch as a candidate.
- **`Substituted: [vendor]`** — operator preempts auto-detection by declaring upfront. Status: `substituted`. Operator attaches the Output produced by the substitute vendor.

**Declaration syntax.** Free-form prose; orchestration parses for the declaration keywords. Examples that orchestration recognizes:

- `P2.3 done` / `P2.3 — done, attached`
- `P2.3 running later` / `Will run P2.3 tomorrow`
- `P2.3 skipping — out of scope after P2.2 finding`
- `P2.3 failed — Gemini Deep Research timed out twice`
- `P2.3 substituted — ran on Claude instead, attaching now`

**Ambiguous declarations.** If orchestration cannot confidently parse the declaration, M4 (Ambiguous Ask, §11.1.4) fires and asks the operator to clarify before updating Dispatch register.

### 4.10 Substitution absorption (DD.§13.1 item 11) `[structural | stable]`

**Decision.** Substitution is absorbed at convergence; no re-dispatch demanded. Mechanics integrate with §4.7 reconciliation and §4.8 Dispatch register.

**Operating sequence.**

1. Output's `Vendor` field differs from Envelope's recommended `Vendor`.
2. §4.7 reconciliation detects substitution; logs in Dispatch register with Status `substituted`.
3. Layer 1 convergence ingests the output as-is. Findings absorb into Master with provenance noting the substitution: *"P2.3 — executed on Claude (substituted from Gemini Pro DR recommendation); finding absorbed."*
4. If the prompt was `equivalence` mode, Vendor Triangulation delta notes the diversity collapse:
   ```
   Triangulation note: P2.5 was specified as equivalence/3-vendor.
   Returns received: 2 Claude (one substituted from Gemini), 1 Perplexity.
   Vendor-diversity dimension is reduced; cross-vendor convergence is
   weaker than designed.
   ```
5. *What's next* surfaces the diversity-collapse as a soft note. Operator decides whether the collapse materially affects confidence and whether to re-dispatch on the original recommended vendor.

**No automatic re-dispatch.** Per DD.§3.6 — substitution is an operator-access reality the framework absorbs, not a defect the framework demands be cured.

### 4.11 Prompt body convergence provisions (DD.§13.1 item 9) `[structural | stable]`

**Decision.** Composition rules for the prompt body that make convergence orchestration-side robust to partial returns.

**Composition rules.**

1. **Discrete attributable findings.** Each finding is self-contained: claim + evidence + provenance, in one paragraph or bullet. No finding depends on a prior finding having been received.
2. **Numbered/IDed sections.** Returns are sectioned (`Finding 1`, `Finding 2`, ...). Orchestration can ingest any subset by ID without re-issuing the prompt.
3. **No cross-section dependency.** A return that includes Findings 1, 2, 4 (skipping 3) is valid and ingestable; orchestration absorbs what's there and notes the gap.
4. **Vendor-neutral phrasing.** No Claude-specific tool references in the body. Tool requests live in the Envelope's `Tools:` field.
5. **Evidence-class explicit.** Each finding names its evidence class (per LL schema field `evidence_class`): document, trace, probe, empirical-test, expert-interview, cross-check.
6. **Confidence calibration.** Each finding self-rates confidence on a 3-point scale (low/medium/high). Calibration is *relative signal*, not ground truth — used for triangulation weighting in Vendor Triangulation.

**Required output structure** (the prompt body specifies this):

```
## Findings

### Finding 1 — [short title]
- Claim: [...]
- Evidence: [...]
- Provenance: [source, citation, date]
- Evidence class: [document | trace | probe | empirical-test | expert-interview | cross-check]
- Confidence: [low | medium | high]
- Notes: [optional]

### Finding 2 — ...
```

**Adaptable.** Where the prompt's analytical shape requires a different finding structure, the prompt body specifies the alternative explicitly. Default is the structure above.

---

## 5. Context-pressure framework (DD.§13.2, items 14–19)

Spec for the architecture named in DD.§3.7. This section operationalizes the seven-signal telemetric framework, M5 (consolidating M12), continuous-curation posture, migration handoff, failsafe recovery, and band-state migration.

### 5.1 Telemetric framework — signal weighting and compounding (DD.§13.2 item 14) `[structural | stable]`

**Decision.** Qualitative compounding: each signal evaluated as *quiet*, *active*, or *strong* per turn-close; band state computed from compounded signals via rules below. Behavioral signals weight higher than volumetric.

**Per-signal evaluation criteria** (rev. 1 draft — calibration via real use):

#### Volumetric signals (weak-signal: alone they don't move bands)

1. **Attached content size** — total `.md` file content attached to the orchestration session.
   - quiet: < 50KB
   - active: 50–200KB
   - strong: > 200KB

2. **Conversation accumulation** — turn count + estimated message length in the orchestration session.
   - quiet: < 20 turns AND short-medium messages
   - active: 20–40 turns OR sustained long messages
   - strong: > 40 turns OR sustained very-long messages

3. **Reasoning accumulation** — extended thinking blocks accumulated in-session (proxy: explicit reasoning sections in turn-bodies, multi-step monitor cascades).
   - quiet: minimal reasoning per turn
   - active: sustained reasoning per turn, multi-monitor cascades visible
   - strong: every turn carries deep reasoning, monitor cascades dominate

#### Behavioral signals (strong-signal: one alone can move bands)

4. **Quality-degradation self-check** — orchestration LLM's self-rating of its current cognitive sharpness (orchestration explicitly checks itself at turn-close).
   - quiet: "feels sharp; recall and synthesis intact"
   - active: "noticing some lag on cross-section recall; minor"
   - strong: "context-recall failing; producing inconsistent answers across turns"

5. **Task-completion friction** — observed friction in performing routine moves.
   - quiet: edits applying cleanly, cross-links intact, no repeated-ask pattern
   - active: occasional edit-not-applying, occasional re-ask of established state
   - strong: frequent edit failures, repeated requests to re-state established state, broken cross-references

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

**Hysteresis** — bands de-escalate only after two consecutive turn-closes show lower signal. Prevents flicker. Escalation is immediate.

**Tag.** `[methodological | review-if: substrate shifts]` — calibration thresholds are empirical.

### 5.2 M5 + M12 consolidation full spec (DD.§13.2 item 15) `[structural | stable]`

**Decision.** Single Monitor (M5 — Context Pressure) absorbs the retired M12. Fires at every orchestration turn-close.

**M5 spec.**

- **Trigger.** Every orchestration turn-close. M5 evaluates the seven signals (§5.1) and assigns a band.
- **Output.** Band assignment as a header field on *What's next*:
  ```
  Context band: 🟡 — getting warm
  Driver(s): conversation-accumulation active; quality-self-check active
  ```
- **Fire emission discipline.**
  - 🟢: silent (no fire line; just header).
  - 🟡: advisory line — "Migration available at next natural seam."
  - 🟠: active line — "Curate now. Next natural seam: [seam]. Migration strongly recommended."
  - 🔴: handoff line — "Migration is the correct next action. Producing handoff (§5.4)."
- **Hysteresis** per §5.1.
- **Interaction with other Monitors.** M5 fires regardless of other Monitors. When M5 ≥ 🟠, M5's curation-now directive ranks at priority tier 1 in *What's next* (above other Monitor fires).

### 5.3 Continuous-curation posture operationalization (DD.§13.2 item 16) `[methodological | stable]`

**Decision.** From band 🟡 onward, every orchestration turn-close ends with a one-line curation observation in *What's next*.

**Per-band curation behavior.**

- **🟢** — no curation note. No intervention.
- **🟡** — curation observation line:
  ```
  Curation: [what could be deprioritized in this session;
   what canonical state is worth migrating to fresh session if seam approaches]
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

- Convergence round complete (Layer-1 batch absorbed; Vendor Triangulation delta finalized).
- Phase boundary (P0→P1, P1→P2, etc.).
- Deliverable shipped (Layer 2 synthesis emitted).
- Setup iteration complete (P0.x finalized).

**Curation operations** (what orchestration deprioritizes or compacts):

- Verbose reasoning chains → terse conclusions.
- Multi-paragraph state summaries → bullet summaries.
- Tangential probe outputs → archived in Master, not re-summarized.
- Speculative What-if exploration → deferred to a fresh session.

### 5.4 Migration-as-planning-not-rescue handoff format (DD.§13.2 item 17) `[structural | stable]`

**Decision.** Defined handoff artifact with required sections. Produced by orchestration at 🔴 (mandatory) and offered at 🟠 (operator-elective).

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

- Produced at 🔴 automatically as the closing act of the orchestration session.
- Offered at 🟠 in *What's next* as a candidate next action: "Migrate now to fresh session — produce handoff?"
- Available at 🟢/🟡 on operator request.
- The handoff *plus* the current Master *plus* the Lens Library are the three artifacts the new session opens with attached. Together: complete context restoration.

**Handoff vs. Master.** The Master is canonical project state; the handoff is migration context. The handoff is short (≤ 1 page) and points into the Master for detail. New session reads the handoff first to orient, then works with the Master as canonical reference.

### 5.5 Failsafe recovery — Master/*What's next* continuous-state mechanics (DD.§13.2 item 18) `[structural | stable]`

**Decision.** "Always written" defined mechanically: Master and *What's next* are written at every orchestration turn-close, regardless of band state, regardless of whether the operator asks for them. Misreads of context band cost essentially nothing because state is always recoverable.

**Mechanics.**

- **Master update at every orchestration turn-close.**
  - Append-mostly: Changelog gains a line; relevant register sections gain entries; Dispatch register status updates per §4.8; findings sections absorb any newly-converged Layer-1 outputs.
  - Filename version bump only at phase boundaries or convergence-round increments (per §3.3).
  - Operator must *download* the updated Master at session close to make it the authoritative canonical copy. (Manual step under v2 plain-chat substrate; auto-sync is a roadmap adjacency.)
  - Cloud-drive save is the Operator hint emitted at every turn-close: `Save Master to cloud drive (E.5).`

- ***What's next* rewrite at every orchestration turn-close.**
  - Replaces in place; no history kept (Changelog carries the historical pointer).
  - Always reflects the current state, not a future or planned state.
  - Operator reads *What's next* as the sole source of "what to do next" — not by scrolling chat, not by reading the Master in detail.

**Consequence — asymmetric bet** (DD.§3.7).

- If the framework misreads band: operator migrates → fresh session attaches Master + handoff + Lens Library → work continues, no loss.
- If the framework reads correctly: the recovery infrastructure wasn't needed but wasn't costly either (writing the Master + *What's next* is part of the orchestration turn anyway).
- If the operator declines to migrate at 🔴: operator-discretion override (the framework cannot force migration); the framework continues but flags continuing-at-🔴 in *What's next* and increments a turn-counter that escalates the migration recommendation.

### 5.6 Defensive migration at natural seams — band-state migration spec (DD.§13.2 item 19) `[structural | stable]`

**Decision.** Migration posture keyed to band × seam. Spec table:

| Band | Migration posture | Seam discipline |
|---|---|---|
| 🟢 | Available | At any natural seam; no urgency. Operator-elective. |
| 🟡 | Recommended | At the next natural seam; if no seam approaching, finish current sub-task to create one. |
| 🟠 | Strongly recommended | At the immediate next opportunity; framework actively closes current curation to reach a seam. |
| 🔴 | Correct action now | Framework produces handoff (§5.4); operator opens fresh session and attaches handoff + Master + Lens Library. |

**Natural seams** (defined per §5.3): convergence round complete; phase boundary; deliverable shipped; setup iteration complete.

**Operator override.** Operator can decline migration at any band. Framework respects but flags continuing-at-band in *What's next*. At 🔴, the per-turn flag escalates to a migration-overdue counter.

**Tag.** `[structural | stable]`

---

## 6. Setup mechanics (DD.§5)

### 6.1 From waterfall to library-graded iterative refinement — operating spec

**Setup iteration loop.**

1. Operator provides initial subject brief.
2. Orchestration produces draft Prompt Strategy P0.1.
3. Probes 6, 7 iterate early in P0.1 (Domain Reconnaissance + User Voice); Probes 1, 2, 4 iterate per turn; Probes 3 and 5 run once.
4. Probe 1 (Coverage grading) outputs tri-state dispositions per Lens (§6.3.1).
5. Operator reviews probe outputs.
6. Orchestration produces P0.2 incorporating closures.
7. Repeat until §6.2 readiness clears.

**Iteration numbering** — P0.1, P0.2, …. No artificial cap. Floor: minimum 2 iterations. Soft ceiling: at 4 iterations without saturation, flag *something structural may be wrong — operator intervention recommended*.

### 6.2 Three-layer readiness — operating spec

All three layers must clear before P0 → P1 boundary.

#### Layer 1 — Structural completeness

Every planned prompt has the following fields populated:

- Single objective (one-sentence statement).
- Output format (structured findings per §4.11).
- Dependency list (which prior prompts' outputs are inputs; can be empty).
- Attachment map (filenames per attachment).
- Enrichment decision (single-vendor / equivalence / split / limitation-named).
- Execution envelope (full Envelope per §3.2.1).

Verification: orchestration walks the strategy and confirms each prompt has all six fields. Any missing field halts P0 → P1.

#### Layer 2 — Library coverage saturation

Every applicable Lens from the Lens Library v0.9 is either:

- Covered by at least one planned prompt (Probe 1 disposition: *fires-covered*), OR
- Explicitly marked out of scope with rationale (Probe 1 disposition: *doesn't-fire* with rationale captured, OR *fires-maybe* closed via *opt-out* per §6.3.1).

**Saturation signal.** Two consecutive iterations produce no material change to coverage or strategy.

**Material change criteria** (rev. 1 draft):

- New Lens added to coverage map (P0.x → P0.x+1).
- Existing Lens disposition changes from *fires-uncovered* to *fires-covered* (or *opt-out*).
- New planned prompt added or merged.
- Prompt's Vendor or Mode changed.

If two consecutive iterations show none of the above, saturation reached.

#### Layer 3 — Operator ratification

Operator confirms the strategy matches intent. Free-form confirmation; orchestration parses for explicit ratification ("ratify", "approved", "go", "looks good — proceed").

**Ratification triggers P0 → P1.** Master filename bumps to P1 (e.g., `solace_audit_prism2.0_master_p1.0.md`). Setup probes close. Strategy moves to "presumed stable, revisable at convergence" per §6.5.

### 6.3 The seven probes — operating spec

Probes operate against the draft Prompt Strategy at Setup. Vendor Triangulation (§4.3) — convergence-time cross-vendor reconciliation — lives outside the probe taxonomy because it operates against returned findings, not draft strategy. Result Completeness Check (M12, §11.2.4) is a convergence-time monitor with its own mechanism. Single-responsibility discipline: probes are Setup-time grading constructs only.

#### 6.3.1 Probe 1 — Coverage grading (iterates)

**What it does.** Grade the draft strategy against the Lens Library v0.9. Universal lenses (5) always evaluated. Domain lenses (18) evaluated where their `trigger:` predicate is met by the subject.

**Per-lens disposition** (tri-state with maybe sub-state):

- **`fires-covered`** — lens applies, draft already covers it. Silent pass; recorded for audit trail.
- **`fires-uncovered`** — lens applies, draft does not cover it. Surfaces as a flag; closed by adding coverage in next iteration.
- **`doesn't-fire`** — trigger predicate not met; rationale captured (one line).
- **`fires-maybe`** — applicability or coverage ambiguous.
  - **`fires-maybe — dig-in`** — judging LLM does targeted research on the lens-subject intersection. Produces an expanded lens framing or a scoped specialist pass to add to the strategy. Closes by becoming *fires-covered* in next iteration.
  - **`fires-maybe — opt-out`** — documented exclusion with rationale. Closes by becoming a recorded out-of-scope decision.

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

**Operator-fatigue mitigation.** Judging LLM resolves clear cases silently (covered or doesn't-fire with obvious rationale). Escalates to operator only on genuine ambiguity (*fires-maybe* requiring dig-in vs. opt-out decision). Empirical calibration deferred per DD.§11 item 14 — flagged in §16.

#### 6.3.2 Probe 2 — Adversarial Scope (iterates)

**What it does.** Hunt for silent omissions and under-scoped treatments in the draft Prompt Strategy. Library-driven (uses Library entries as starting prompts but goes beyond catalog); informed by domain context.

**Lifecycle.** Setup-only. Iterates per P0.x turn-close. Does not fire at Layer-1 convergence — cross-vendor finding triangulation is a separate mechanism (Vendor Triangulation, §4.3) with its own trigger and output shape.

**Multi-vendor recommendation.** Independent adversarial passes across vendors; divergence between passes is signal about scope blind spots. Not the same as cross-vendor finding reconciliation.

**Output.** List of silent-omission candidates the strategy did not address. Operator reviews; orchestration converts surviving candidates into Lens references or new prompt additions in the next iteration.

#### 6.3.3 Probe 3 — Decision Framing (once)

**What it does.** Does the strategy answer what the stakeholder actually needs to decide?

**Outputs the Decision brief and Stakeholder register Setup artifacts** (§6.4).

#### 6.3.4 Probe 4 — Pre-mortem (iterates)

**What it does.** Imagine execution completes. How would the finding fail to answer the original question?

**Output.** A list of pre-mortem failure modes; each surviving mode either becomes a new probe in the strategy or is dismissed with rationale.

#### 6.3.5 Probe 5 — Falsifier (once)

**What it does.** What findings would invalidate the thesis?

**Output.** Decision brief gains a Falsifiers section listing findings that, if observed, would refute the thesis. These become explicit success/failure criteria for Layer 2 synthesis.

#### 6.3.6 Probe 6 — Domain Reconnaissance (iterates early)

**What it does.** What do practitioners, researchers, and serious analysts of this domain actually investigate? What lenses does the domain's own literature treat as default?

**Imports domain-external signal that the Library cannot carry.**

**Asks whether an authoritative canonical source exists for the domain** (DD.§8.2):

- Regulated registry?
- Standards body with testable criteria?
- Curated research corpus?
- Benchmark dataset?

If yes: strategy brings it in as primary evidence; Probe 6 outputs a citation.

**Multi-vendor recommended.** Different vendors have different exposure to domain-specific literature.

**Outputs the Jurisdiction map Setup artifact** (§6.4).

#### 6.3.7 Probe 7 — User Voice (iterates early)

**What it does.** Imports real end-user / customer / affected-user perspectives into Setup. Mines actual user signal from forums, reviews, support tickets, public commentary, social platforms — whatever surfaces are available for the subject's user base.

**Why a probe.** Strategies built only on the project brief plus Library lenses risk being shaped by what the framework *expects* users to care about rather than what they actually do. User Voice surfaces friction points, pain patterns, and lived-experience signal the brief misses.

**Lifecycle.** Setup-only. Iterates early in P0 alongside Probe 6 (Domain Reconnaissance) — both import external signal before the strategy hardens.

**Multi-vendor recommended.** Different vendors have different exposure to user-generated content (Perplexity is strong on live web; Claude on synthesis from quoted text; Gemini on long-context corpus).

**Output.** A list of user-surfaced concerns, friction points, and reality-checks that feed the strategy. Surviving items either become new prompts, become flagged-for-coverage Library lenses, or refine the Decision brief's stakeholder section.

**Carries forward from v1.x.** v1.x had User Voice as a Phase 2 enrichment role ("mine real user perspectives — reality check"). v2 promotes it to Setup probe so user signal informs strategy *before* execution rather than enriching findings *after*.

#### 6.3.8 Probe ordering — recommended sequence

P0.1: Probe 6 (Domain Reconnaissance — establishes domain context); Probe 7 (User Voice — imports user signal); Probe 1 (initial coverage); Probe 3 (Decision Framing).
P0.2: Probe 4 (pre-mortem); Probe 1 (re-grade); Probe 2 (adversarial scope).
P0.3: Probe 1 (re-grade for saturation); Probe 5 (falsifier).
P0.4+: Probes 1, 2, 4, 6, 7 iterate as needed until saturation.

Order is a default; operator may re-sequence per project shape.

**Probe taxonomy after rev. 2 changes.** P5 Consolidation (rev. 1) dissolved — structural overlap-spotting is judgment work the LLM does inside Probe 1 and Probe 2 grading rather than a checkbox-shaped standalone probe. Aligns with v2's principle-heavy / specification-light philosophy. Vendor Triangulation extracted from rev. 1's Probe 2 and lives in §4.3, not in the probe taxonomy.

### 6.4 Setup artifacts (DD.§5.4) — operating spec

Four instance-specific artifacts populated during Setup. Live in the Master (§3.3 required sections).

#### 6.4.1 Decision brief

**Populated by Probe 3** primarily; refined by Probe 5 (Falsifiers section).

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

**Populated by Probe 3** primarily.

```
## Stakeholder register

| Role | Stake | Decision power | Communication channel |
|---|---|---|---|
| [name] | [decision/outcome stake] | [yes/advisory/none] | [channel] |
| ... | ... | ... | ... |
```

#### 6.4.3 Claim inventory

**Populated by Setup orchestration** as it parses subject brief; refined by Probe 6 (Domain Reconnaissance).

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

**Populated by Probe 6 (Domain Reconnaissance)** primarily.

```
## Jurisdiction map

| Jurisdiction | Triggered regimes | Material to scope? | Pass(es) |
|---|---|---|---|
| US (federal) | FTC, ADA | yes | P3.1 |
| EU | GDPR, EU AI Act | yes | P3.2 |
| US-CA | CCPA/CPRA | yes | P3.1 |
| ... | ... | ... | ... |
```

### 6.5 Strategy stability — operating spec (DD.§5.5)

**At P0 → P1 boundary.** Strategy moves to "presumed stable, revisable at convergence."

**Convergence-time strategy revisions** trigger when Layer-1 convergence produces:

- A premise invalidation (M6 Premise Shift fires HIGH).
- A newly-surfaced domain area (e.g., a regulatory regime not in the Jurisdiction map).
- A falsifier hit (one of the Decision brief's Falsifiers is observed).
- An assumption conflict between two findings (M7).

**Revision mechanic** (lighter than v1.x major-bump Adaptation).

1. Convergence finding triggers Monitor (M6/M7) HIGH.
2. Orchestration drafts a revision: adds/modifies prompts, updates attach maps, updates Setup artifacts as needed.
3. Operator ratifies (per Layer 3 §6.2).
4. Master version increments (sub-version bump within phase, e.g., P2.2 → P2.3).
5. Strategy continues with revised state.

**Attach map travels with each prompt.** When a prompt adapts, its attach map adapts with it (§3.2.1).

---

## 7. Library integration (DD.§6) — operating spec

The Lens Library v0.9 (`lens/PRISM_lens_library.md`, tag `prism-lens-v0.9`) is the canonical catalog. This section specifies how it integrates with PRISM v2 mechanics. The catalog itself is not duplicated.

### 7.1 Library reference at Setup

**Required attachment.** Lens Library v0.9 is attached to every orchestration session (alongside the Master). Recommended: live in the Claude Project alongside the Master (see §8.1).

**Probe 1 grades against Library entries.** Spec mechanics in §6.3.1.

### 7.2 Lens schema — what orchestration consumes

Per LL.§Schema:

- `id:` — identifier orchestration uses to reference the lens.
- `name:` — short colloquial title for human-legible operator output.
- `material_question:` — the question Probe 1 grades the strategy against.
- `tier:` — universal | domain. Universal always-evaluated; domain evaluated when trigger predicate met.
- `trigger:` — predicate the judging LLM evaluates against the subject for domain lenses.
- `evidence_class:` — one of {document, trace, probe, empirical-test, expert-interview, cross-check}. Used in finding output structure (§4.11).
- `specialist_type:` — open taxonomy. Used by judging LLM to promote relevant entries as specialist passes under Probe 1.
- `rubric_anchor:` — optional; version-pinned external spec where present. Two entries at v0.9 (LL-D-002 WCAG 2.2; LL-D-005 OWASP ASVS 5.0.0).
- `last_verified:` — populated on entries with `rubric_anchor:`. Maintenance signal per §7.4.
- `informed_by:` — provenance only; not a runtime rubric.
- `failure_mode:` — used in operator-facing flag explanations.
- `minimum_scope_binding:` — what counts as "covered" for Probe 1 disposition.

### 7.3 Specialist-pass promotion

Per LL design — the Library *is* the specialist enumeration. Each lens's `specialist_type:` field names the practitioner role whose framing the lens channels. Orchestration's Probe 1 grading promotes relevant entries as specialist passes within the Prompt Strategy (e.g., "P3.4 — accessibility pass per LL-D-002, specialist framing: WCAG-qualified accessibility auditor").

### 7.4 Currency maintenance — point refresh (DD.§6.6) `[methodological | stable]`

**Decision.** Two-tier mechanism per DD.§6.6 — point refresh (per-project, in Setup) + Update session (standalone, rare, operator-gated). Spec for both below.

**Point refresh.**

- **Trigger.** Probe 1 evaluation extends to citation currency. For each lens with `rubric_anchor:` set:
  - If `last_verified:` is within 6 months: disposition includes `fresh`. No flag.
  - If `last_verified:` is 6–12 months old: disposition includes `stale-refresh`. Orchestration runs a web-search currency check and refreshes the citation in the Prompt Strategy (the canonical Library file is *not* modified).
  - If `last_verified:` is > 12 months old: disposition includes `stale-accumulating`. Same inline refresh, but advisory signal accumulates toward an Update session (per §7.5).
- **Output.** Probe 1 output includes per-anchored-entry currency disposition.
- **Inline refresh format.** The refreshed citation appears in the Prompt Strategy with provenance:
  ```
  P3.4 — accessibility pass
  Specialist framing: WCAG-qualified accessibility auditor (LL-D-002)
  Anchor: WCAG 2.2 (October 2023) — verified current as of [date]
          via web search; PRISM Lens Library v0.9 last_verified
          2026-04-24 still current.
  ```
  If the web-search currency check finds a newer version (e.g., WCAG 3.0 published):
  ```
  Anchor: WCAG 2.2 (October 2023). Note: WCAG 3.0 published [date];
          considered for use; chose WCAG 2.2 because [rationale —
          subject's commitment, regulatory pin, etc.] OR
          updating to 3.0 because [rationale].
  ```
- **No silent modification of Library.** Library file is read-only at point-refresh time.

**Tag.** `[methodological | stable]`

### 7.5 Currency maintenance — Update session (DD.§6.6) `[methodological | stable]`

**Decision.** Standalone session, rarely run, operator-gated. PRISM-file-in / PRISM-file-out contract.

**When.**

- Triggered by point-refresh advisory signal accumulation (count of `stale-accumulating` over time + count of `informed_by:` framework changes seen across sessions).
- Operator decision; framework recommends in *What's next* when signal exceeds threshold (rev. 1 draft threshold: 3 stale-pattern accumulations across 6+ months).
- Operator can also run on demand at any time.

**Mechanic.**

1. Operator opens fresh orchestration session.
2. Attaches: PRISM v2 framework, current Lens Library, possibly other reference frameworks pertinent to anchor checks.
3. Operator declares: `Run Update session against Lens Library [version].`
4. Orchestration's Update routine:
   - Walks each entry with `rubric_anchor:`. Web-searches current state of the external spec. Records currency.
   - Walks each entry's `informed_by:` list. Web-searches major framework updates since `last_verified:`. Records changes.
   - Produces a delta document: per-entry currency status, recommended `last_verified:` date updates, recommended citation text updates.
   - Does *not* modify entry IDs, schema, tier composition, or `informed_by:` provenance lineage. Architectural changes are flagged, not made inline.
5. Operator reviews delta document.
6. Orchestration applies approved deltas to a new Library file (e.g., `PRISM_lens_library_v0_9_1.md`).
7. Operator reviews, ratifies, and ships the new Library.

**Resilient to partial source-access failure.** When a web-search currency check fails (gated source, paywall, expired URL), Update routine records `currency-check-failed` for that anchor and proceeds. Operator decides whether to escalate.

**Library versioning rides PRISM's own.** Library version increments are minor patches (v0.9 → v0.9.1) unless schema changes (in which case major-bump and architectural review).

**Library changelog lives inside Library file.** Update session appends to it.

**Not architectural drift.** Schema/tier/composition changes are out-of-scope for Update sessions and produce flag-don't-fix outputs. Architectural changes go through a fresh Library design cycle, not an Update session.

---

## 8. Parked v2 design ideas (DD.§13.3)

### 8.1 Claude Project as Setup recommendation (DD.§13.3 Idea #1) `[vendor-dependent | review-if: orchestration vendor changes]`

**Decision.** Setup at P0.1 includes a recommendation to create a Claude Project as the home for project state.

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
- `[project]_prompt_strategy_p0.1.md` (current Prompt Strategy, optional — Master can carry this)
- Any subject-supplied reference documents

**Master in the Project** — operator workflow:

- Each orchestration session updates the Master.
- At session close, operator downloads the updated Master to the device.
- Operator uploads the new version to project knowledge (replacing or adding).
- Old version retained in project knowledge as audit trail (or archived to cloud drive per Appendix E.5).

This is a manual sync step under v2's plain-chat substrate. Auto-sync is a roadmap adjacency.

**Fallback (operator declines or cannot create a Project).**

- Setup proceeds. P0.1 continues without Project.
- Every subsequent *What's next* emits an Operator hint: `Re-attach Master and Lens Library at session open.`
- The Project recommendation does not re-surface unless operator asks; framework respects the decline.

**SP-12 bounded-search disclosure interaction.** When a Project is in place, Claude's `conversation_search` is bounded to the Project. SP-12 disclosure language adjusts:
> *"Searched within the [project name] Project. [Result]. The session may live outside this Project; confirm before I conclude."*

When no Project is in place, search covers non-project conversations. SP-12 disclosure language:
> *"Searched outside any Project's scope. [Result]. The session may live inside a Project I cannot see from here; confirm before I conclude."*

### 8.2 Session history as validation/recovery mechanism (DD.§13.3 Idea #2) `[vendor-dependent | review-if: orchestration vendor changes]`

**Decision.** Session history (Claude's `conversation_search`) is consulted when state is unexpected, ambiguous, or out-of-order. Results are advisory; SP-1 governs canonicity.

**Triggers** (Monitors that consult session history):

- **M2 fires** (Version Drift) — Master version doesn't match expected. Consult session history for the last session that saved the expected version.
- **M3 fires** (Sequence Violation) — operator declared a step out of order. Consult session history for the canonical sequence in this project.
- **Master/What's next mismatch** — attached Master's version differs from what *What's next* predicted at last close. Consult session history for the closing turn that produced the mismatch.
- **Strategy-finding mismatch** — a finding references a prompt not in the Prompt Strategy. Consult session history for when the prompt was added or removed.
- **Attach-conversation disagreement** — attach map and conversation disagree about which file is canonical. Consult session history for the last canonical statement.

**Query construction.** Orchestration's `conversation_search` query is derived from the ambiguity. Examples:

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
2. Orchestration does *not* silently update Master from session-history evidence. Per SP-1: canonical artifacts are not regenerated without operator confirmation.
3. Orchestration surfaces a recommendation: "Session history suggests [interpretation]. Update Master to reflect? [yes/no/clarify]"
4. Operator confirms; orchestration updates Master.

**Reconciliation when session history disagrees with attached Master.** Both surfaced; named as discrepancy; escalated to operator.

- *Default posture*: attached Master is authoritative; session history is corroborating evidence.
- *Operator decides*: whether to update Master per session history, keep Master as-is, or open the older session and reconstruct.
- *SP-1 governance*: never silently regenerate canonical state from session history.

**SP-12 disclosure on every consult.**

```
Session history search note (SP-12):
Searched within [scope]. [N found / null]. The session may live in a
different scope I cannot see from here; confirm before concluding.
```

---

## 9. Resolved spec-session deferrals (DD.§14)

### 9.1 M2's fate pending bump-atomicity specification (DD.§14 item 1)

**Bump atomicity spec.**

Master version bumps are mechanically tied to:

- **Phase transitions** (P0→P1, P1→P2, etc.) — major filename version advances:
  `solace_audit_prism2.0_master_p0.4.md` → `solace_audit_prism2.0_master_p1.0.md`
- **Convergence rounds within a phase** — sub-version increments:
  `…_master_p2.1.md` → `…_master_p2.2.md`
- **Setup probe iterations** — sub-version increments within P0:
  `…_master_p0.1.md` → `…_master_p0.2.md`
- **Schema version changes** — Schema version field in Master metadata header increments. Filename does *not* bump on schema-only changes; the metadata field tracks it.

**Atomic bump routine** (orchestration-side, at every turn-close):

1. Compute the new Master filename per the bump rule above.
2. Produce the updated Master content.
3. Write a Changelog entry: `[date] | [old version] → [new version] | [trigger: phase transition / convergence round / probe iteration / state update]`
4. Emit *What's next* with the new Master version embedded.
5. Operator hint: `Download as [new filename]; attach next session.`

**M2 disposition post-bump-atomicity.**

**Decision: M2 retained.** Bump atomicity makes drift very unlikely *by construction* but not impossible. Residual failure modes:

- Operator attaches an old Master from cloud archive by mistake.
- OS-level filename collisions serve a stale file.
- Cross-device syncing serves a previous version.
- Multiple Masters from forked sessions (anti-pattern but not impossible).

**M2 spec.**

- **Trigger.** Every orchestration session-open. Compares attached Master's metadata header to expected.
- **Compare against.** The version *What's next* predicted at last close (orchestration sees its own prior closing turn via session history if available; else operator declaration).
- **Fire conditions.**
  - Attached Master version < expected: HIGH (older than expected; rollback risk).
  - Attached Master version > expected: HIGH (newer than expected; ghost session ran in between).
  - Schema version mismatch: HIGH.
  - Attached Master == expected: silent pass.
- **Resolution.** M2 HIGH halts orchestration until operator clarifies. Optional: consult session history per §8.2.

**Per §8.2 of DD design doc** — checks-and-balances framing supports M2 retention. Silent monitor that rarely fires has small cost.

**Tag.** `[structural | stable]`

### 9.2 Output signature `Attachment warnings` field placement (DD.§14 item 2)

**Decision.** Field lives in the Output block's footer area, after `Operator next:`. Optional — fires only when warranted.

**Field syntax** (already shown in §3.2.3):

```
━━━ END PRISM EXECUTION OUTPUT ━━━
Operator next:           [download instruction; attach instruction]
Attachment warnings:     [optional; one line per warning]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Trigger conditions** (when to populate):

- Vendor session received an attachment but couldn't read it. Example: Deep Research subagent file-access bug; format unsupported on this vendor.
- Attachment was expected per Envelope's `Attachments:` field but absent (vendor session detects this before task execution).
- Attachment was present but corrupted, truncated, or apparently mis-delivered.
- Attachment was readable but content didn't match expected schema (for structured attachments like prior Outputs).

**Format.**

- One line per warning.
- Severity tag at the start: `MISSING:`, `UNREADABLE:`, `CORRUPTED:`, `SCHEMA_MISMATCH:`.
- Filename + brief reason.
- Example:
  ```
  Attachment warnings:
    MISSING: regulatory_context.md (declared in Envelope but not attached)
    UNREADABLE: solace_brief.pdf (Deep Research subagent file-access)
  ```

**Orchestration behavior on Attachment warnings.**

- M1 (Missing Inputs) fires HIGH on `MISSING:` warnings.
- M1 fires MEDIUM on `UNREADABLE:` / `CORRUPTED:` warnings.
- M1 fires LOW on `SCHEMA_MISMATCH:` (informational).
- *What's next* surfaces re-dispatch with corrected attachment list as a candidate.

This is the M1 execution-side mirror per DD.§7.2. M1 itself fires orchestration-side; the warning field is the execution-side input that lets M1 detect issues that the operator's perspective alone couldn't catch.

**Tag.** `[structural | stable]`

### 9.3 M8 vs. DD.§6.6 point-refresh scope separation (DD.§14 item 3)

**Decision.** Clean specification with separate sections; neither mechanism crowds the other.

#### 9.3.1 M8 scope — stale evidence in the audit being conducted

**M8 (Stale Source) spec.**

- **Trigger.** Layer-1 convergence — orchestration ingesting findings from execution sessions.
- **Detects.** A returned finding cites a source (document, study, regulation, vendor product) dated before some material event affecting its validity for the current audit.
- **Material event examples.**
  - Cited regulation has been amended/repealed since source date.
  - Cited study has been superseded by a published replication or correction.
  - Cited vendor product has been retired/end-of-lifed.
  - Cited statistic comes from a dataset that has been corrected.
- **Detection mechanic.** Orchestration runs a focused web search on cited source(s) at convergence time. If the search surfaces a material event invalidating the source, M8 fires.
- **Severity.**
  - HIGH: source is invalidated; finding's claim no longer supported.
  - MEDIUM: source is dated but still substantively current; finding's claim weakened, not invalid.
  - LOW: source is dated but the field hasn't moved; informational.
- **Resolution.** HIGH M8 fires trigger re-dispatch of the prompt with current sources as required attachments. MEDIUM/LOW recorded in Master's findings sections as confidence caveats.

**Scope.** M8 looks at *evidence inside the audit*. Each finding's cited sources are the surface.

#### 9.3.2 DD.§6.6 point-refresh scope — stale framework anchors in the Lens Library

**Spec per §7.4** above.

**Scope.** DD.§6.6 looks at *framework anchors used to grade the audit's scope*. The Lens Library's `rubric_anchor:` and `informed_by:` fields are the surface.

#### 9.3.3 Boundary statement

| Mechanism | Surface | Lifecycle | Resolution |
|---|---|---|---|
| **M8** | Cited evidence sources in returned findings | Per finding, at Layer-1 convergence | Re-dispatch with current sources |
| **DD.§6.6 point-refresh** | Lens Library entry's `rubric_anchor:` / `informed_by:` | Per Setup probe iteration | Inline refresh in Prompt Strategy; advisory signal toward Update session |

Different artifacts, different lifecycles, different resolutions. Spec keeps them in separate sections. Neither's machinery crowds the other.

**Tag.** `[structural | stable]`

---

## 10. Setup, dispatch, and convergence — example flow

Worked example to illustrate the full mechanics. Subject: hypothetical career-coaching SaaS audit.

```
Session 1 — Orchestration. Operator: "Begin PRISM v2 audit on
Atlas career coaching SaaS. Brief attached: atlas_brief.md."

[Setup recommendation surfaces (§8.1):]
  "Recommend creating Claude Project 'Atlas Audit'. [...]
   Proceed without? [yes/no]"
[Operator: yes, create.]

[P0.1 — Probes 6, 7, 1, 3 fire.]
  Probe 6 (Domain Reconnaissance) surveys career-coaching domain practice. Surfaces: ICF
    competencies; CLAS multicultural standards; APA ethics for
    coaching adjacent to therapy. Outputs Jurisdiction map (§6.4.4):
    US (federal) FTC + state UPL rules; EU AI Act for any algorithmic
    matching.
  Probe 1 grades against Lens Library v0.9. Initial coverage map:
    LL-U-001..005 — three covered, two uncovered. Domain triggers:
    Pack 1 (using product), Pack 4 (proving results), Pack 5 (laws).
    Pack 2 partial, Pack 6 doesn't-fire.
  Probe 3 produces Decision brief: "Should sponsor invest
    additional capital in Atlas?" Stakeholder register: founders,
    investors, current users, prospective users, regulator.
[Master P0.1 written. What's next emits: P0.2 with probe iteration.]

[P0.2 — Probes 4, 1, 2 fire. Saturation not yet reached.]
[P0.3 — Probes 1 (re-grade), 5 (falsifier) fire. Coverage saturates. Layer 1 clears.]
[P0.4 — Operator ratifies. P0 → P1.]
[Master bumps from p0.4 to p1.0.]

Session 2 — Orchestration. Operator: "Continue Atlas. Master attached."

[M2 fires silent (version match).]
[Vendor Selection runs for P2.1 — efficacy claim review.]
  Refresh: confirms Claude analytical depth fits; multi-vendor not
    needed at this prompt; adversarial-style alternative not material.
  Recommended: Claude Opus 4.7 / standard. Dispatch rationale: analytical
    claim adjudication.
[Envelope produced. What's next emits dispatch-ready payload.]
[Operator dispatches Claude. Output returned. Reconciliation: match.]
[Layer-1 convergence ingests. Master findings section P2.1 populated.]

[P2.2 — efficacy evidence base. Vendor Selection recommends:
  multi-vendor (equivalence) — Claude + Gemini Pro DR + Perplexity.
  Rationale: source breadth (Perplexity), long-context synthesis
  (Gemini), analytical depth (Claude).]
[Operator dispatches all three. Two return; Perplexity fails.]
[§4.4 graceful degradation: Vendor Triangulation fires at N=2; delta
 notes the live-web breadth dimension is missing.]
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

This is a sketch, not a rubric. It illustrates how the mechanics chain in real use.

---

## 11. Monitor specifications (DD.§7.2)

All Monitors fire orchestration-side. Eleven Monitors specified; M12 retired (absorbed into M5 §5.2). Three presentation groupings per DD.§7.2.

### 11.1 Standalone monitors (M1, M2, M4, M5, M9)

#### 11.1.1 M1 — Missing Inputs `[structural | stable]`

- **Trigger.** Every orchestration session-open and turn-close.
- **Detects.** Required attachments missing from current orchestration session; attachments declared in Envelopes but not present in returned Outputs (via §9.2 Attachment warnings).
- **Severity.** HIGH on missing canonical attachments (Master, Lens Library, Prompt Strategy if separate). MEDIUM on missing prompt-specific attachments. LOW on schema mismatches.
- **Resolution.** Halt until attachments provided; or operator confirms intentional absence.

#### 11.1.2 M2 — Version Drift

Spec per §9.1.

#### 11.1.3 M4 — Ambiguous Ask `[methodological | stable]`

- **Trigger.** Every orchestration turn that processes operator input.
- **Detects.** Operator declaration that orchestration cannot confidently parse (close-loop §4.9 ambiguity; intent unclear; conflicting instructions).
- **Severity.** HIGH if the next action depends on the ambiguity. LOW if orchestration can proceed and clarify post-hoc.
- **Resolution.** Orchestration explicitly asks for clarification before proceeding. SP-9 lineage: silence not consent.
- **No execution mirror.** Execution sessions receive pre-resolved dispatched prompts; M4 orchestration-only.

#### 11.1.4 M5 — Context Pressure

Spec per §5.2.

#### 11.1.5 M9 — Convergence Type Drift `[methodological | stable]`

- **Trigger.** Layer-1 convergence and Layer-2 synthesis steps.
- **Detects.** Convergence treating findings as if they were a different convergence type than declared (e.g., treating multi-vendor `equivalence` as a `split`-style synthesis; treating a single-vendor return as if it had been triangulated).
- **Severity.** MEDIUM (analytical posture wrong but recoverable). HIGH if the wrong posture has materially affected a finding's claim.
- **Resolution.** Re-run convergence with correct posture; updates findings sections.
- **Why retained.** Per DD.§7.2 — checks-and-balances on the LLM side (M1/M4 check operator side; M9 checks LLM side). Neither side gets unconditional benefit of the doubt.

### 11.2 Convergence-time monitors (M6, M7, M8, M12)

Fire during Layer-1 integration of new findings into the Master. Can chain to M10.

#### 11.2.1 M6 — Premise Shift `[structural | stable]`

- **Trigger.** Layer-1 convergence — new finding ingested.
- **Detects.** Finding invalidates a premise the strategy was built on. Premises documented in Decision brief, Stakeholder register, Claim inventory, Jurisdiction map.
- **Severity.** HIGH — strategy revision required (§6.5).
- **Resolution.** Strategy revision mechanic per §6.5. Chains to M10 (Rerun) for prompts whose premise has shifted.
- **v1.x → v2 surface drift.** v1.x M6 read premises from prompt context sections. v2 M6 reads premises from Setup artifacts (Decision brief / Stakeholder register / Claim inventory / Jurisdiction map). Surface broadened; name unchanged because face value still describes the work.

#### 11.2.2 M7 — Claim Conflict `[structural | stable]`

- **Trigger.** Layer-1 convergence — new finding ingested.
- **Detects.** Two findings make incompatible claims on the same surface.
- **Severity.** HIGH if the conflict materially affects a falsifier or decision-brief item; MEDIUM otherwise.
- **Resolution.** Orchestration surfaces the conflict; operator decides whether to (a) re-dispatch one or both prompts, (b) accept the conflict and document, (c) escalate to a tie-breaker pass. May chain to M10.
- **v1.x → v2 rename.** v1.x called this "Assumption Conflict" because v1.x had an Assumption Register that M7 read against. v2 has no Assumption Register; M7 reads finding-vs-finding directly. Renamed to **Claim Conflict** in rev. 2 to match the actual surface.

#### 11.2.3 M8 — Stale Source

Spec per §9.3.1.

#### 11.2.4 M12 — Result Completeness Check `[structural | stable]`

- **Trigger.** Layer-1 convergence — new finding ingested.
- **Detects.** Returned findings within a single prompt's declared domain leave domain-relevant surfaces unaddressed. Concrete: a P3.4 accessibility pass produces findings on WCAG criteria 1-3 but does not touch keyboard navigation, cognitive load, motor disabilities, or color independence — surfaces inside the pass's stated domain.
- **Distinct from.** M6 (premise invalidated), M7 (claim vs claim), M8 (cited evidence stale), P1 Coverage grading (strategy-level coverage against Library), Vendor Triangulation (cross-vendor agreement). M12 asks: *did this finding cover its own declared domain?*
- **Severity.** HIGH if uncovered surfaces are material to the finding's claim. MEDIUM if uncovered surfaces are adjacent. LOW if uncovered surfaces are tangential.
- **Resolution.** HIGH chains to M10 (rerun with expanded scope). MEDIUM/LOW recorded in Master findings sections as scope caveats. Operator decides re-dispatch or accept-with-caveat.
- **v1.x lineage.** v1.x had **Coverage** as a Phase 2 enrichment role: *"Find what a specific prompt's narrower analysis missed within its domain."* Same job, relocated from per-prompt enrichment to convergence-time monitor. Run on multi-vendor: divergence between independent passes is signal about within-domain blind spots.
- **Numbering note.** v1.x M12 was Conversation Pressure (retired in v2; absorbed into M5's telemetric framework). The M12 slot is reused in v2 for Result Completeness Check. v1.x → v2 mapping table (§15.x) makes the change explicit.

### 11.3 *What's next* input monitors (M3, M10, M11)

Feed the priority-ranked candidate list at each orchestration turn-close.

#### 11.3.1 M3 — Sequence Violation `[structural | stable]`

- **Trigger.** Operator declaration or strategy state.
- **Detects.** A canonical sequence step has been performed before its prerequisite; a step has been skipped.
- **Severity.** HIGH if the skipped step is on the critical path; MEDIUM otherwise.
- **Output.** Surfaces in *What's next* candidate list at appropriate priority tier.
- **Resolution.** Operator decides: backfill the skipped step, declare it intentionally skipped, or accept the out-of-order sequence with documented rationale.

#### 11.3.2 M10 — Rerun / Fix Required `[structural | stable]`

- **Trigger.** Triggered by chain from M6/M7/M8 HIGH; or by operator declaration of `failed` (§4.9); or by Probe 5 falsifier hit; or by Layer-2 synthesis revealing a Layer-1 gap.
- **Detects.** A previously-completed prompt needs to be rerun (with corrections) or a prompt's output needs explicit fix.
- **Output.** Rerun Register entry in Master:
  ```
  ## Rerun Register
  | Prompt ID | Reason | Source Monitor | Status |
  |---|---|---|---|
  | P2.1 | M6 — premise shifted | M6 HIGH P2.4 ingestion | overdue |
  | ... | ... | ... | ... |
  ```
- **Status values.** `overdue` | `scheduled` | `running` | `complete` | `cancelled`.
- **Surfaces in What's next.** Overdue Rerun Register items rank at priority tier 3 per §3.4.
- **Deferral-target on live state.** Per DD.§7.2 — M10 logic operates on live strategy state, not on a static SF5 declaration. SF5 dissolved per DD.§7.3.

#### 11.3.3 M11 — Layer 2 Readiness `[structural | stable]`

- **Trigger.** Every orchestration turn-close.
- **Detects.** Conditions for Layer 2 cold synthesis met: all Layer-1 prompts closed; Rerun Register clear; convergence saturated; no unresolved M6/M7 HIGH; operator has not deferred Layer 2.
- **Output.** Surfaces in *What's next* as a candidate at priority tier 6.
- **Resolution.** Operator decides at *What's next* moment whether to run Layer 2. Consistent with SF4 dissolution per DD.§7.3.

### 11.4 Monitor severity report format

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

MEDIUM and LOW Monitor fires surface in compressed form on *What's next* state summary line.

---

## 12. Standing Principles in v2

### 12.1 Standing Principles introduced or extended in v2

#### 12.1.1 SP-1 extended — Canonicity preservation `[operator-scaffolding | stable]`

Spec per DD.§2.5:

- v1.x's SP-1 forbade silently reconstructing missing files from memory.
- v2 extends to cover *offers* to reconstruct.
- Order of operations when a canonical artifact is missing:
  1. Locate the original — session history, file system, past chats.
  2. If location fails, surface specific consequences: authenticity loss, schema drift, silent contamination.
  3. Offer regeneration only as a documented last resort, with consequences named.
- Never frame regeneration as "deterministic" or "low-cost" unless it genuinely is.

#### 12.1.2 SP-12 — Bounded-Search Disclosure `[operator-scaffolding | stable]`

Spec per DD.§2.5:

- When orchestration answers on the basis of a bounded retrieval, the default posture is to disclose the bound.
- "I found no evidence" insufficient; "I found no evidence within [named scope]; confirm before I proceed" is required.
- Applies to: past-conversation search, file listing, web search with date/site filters, project knowledge lookup, any retrieval with implicit scope.
- Not a Monitor that fires discretely; a posture held at every retrieval.

**Spec form** (rev. 1 draft phrasing template):

```
[Result]. SP-12 disclosure: Searched within [explicit scope].
[N matches | null]. The target may live outside this scope;
confirm before I conclude.
```

#### 12.1.3 SP-13 — Substrate Declaration `[operator-scaffolding | stable]`

Spec per DD.§2.5 + §3.2.2 (Self-check operationalization):

- PRISM-loaded sessions verify substrate against declared target before executing dependent work.
- If self-identification doesn't match declared target, or can't be determined, session halts and asks operator.
- Operationalized inside execution sessions via the Self-check block (§3.2.2).
- In orchestration sessions: operationalized as a session-open verification — orchestration self-identifies and confirms it matches the declared orchestration target (Claude Opus 4.6 or 4.7 at v2.0).

**Orchestration-side spec.**

```
[At every orchestration session-open:]
SP-13 verification:
  Self-identification: [model, vendor, mode]
  Declared target: [Claude Opus 4.6 or 4.7]
  Match: [yes / no / cannot-determine]
[If no or cannot-determine: halt; ask operator.]
```

#### 12.1.4 SP-10 — Verify state before recommending `[operator-scaffolding | stable]`

Carries forward from v1.10.4 as a named principle in v2. The principle's mechanics live primarily in Vendor Selection (§3.6) — but holding it as a named SP keeps it portable: point refresh (§7.4), Update sessions (§7.5), and any future recommendation surface inherit the discipline rather than re-deriving it.

- When orchestration generates recommendations that depend on current platform / vendor / model / best-practice state, verify before recommending.
- Training knowledge is reliably out of date for fast-moving domains.
- Verification pattern: targeted web search at recommendation-generation moments.
- Calibrated output: search result is *input* to recommendation, not substitution; reconcile with operator observations and remaining uncertainty.
- Graceful degradation when verification fails: frame as best-effort, name the staleness risk.
- Budget discipline: verification searches return substantial context; only trigger on fast-moving state, not on stable defaults.

#### 12.1.5 SP-14 — Filename Discipline `[operator-scaffolding | stable]`

Extracted from v1.x SP-8 (which bundled two concerns under one number). Rev. 2 splits SP-8 into Canonical Authority (the original SP-8) and Filename Discipline (this new SP-14).

- Look-alike files produced by multi-vendor execution use the structured filename pattern: `[project]_[promptID]_[vendor].md` for Outputs, `[project_name]_prism[version]_master_[phase-versioning].md` for Masters, `PRISM_lens_library_[version].md` for Library files, dated handoffs for migrations.
- The em-dash (` — `) separator stays cross-platform safe (pipe is illegal on Windows, shell-active on Unix).
- M1 (Missing Inputs) parses attached filenames against expected patterns; mis-named files are flagged at session-open.
- "Wrong-file-that-looks-similar" is a specific failure mode v2 creates by design (multi-vendor equivalence dispatches produce N similarly-named outputs); the naming convention is the defense.

**Surface in v2** (narrower than v1.x; principle still earns its place):
- Equivalence-mode Outputs (one file per vendor for the same prompt)
- Master versions across phases accumulating in cloud drive
- Migration handoffs (one per migration, dated)
- Update-session Library output versions

### 12.2 v1.x Standing Principles — carryforward catalog

Per-SP disposition explicit (closes rev. 1 build-residual #1):

| SP | v1.10.4 name | v2 disposition | Notes |
|---|---|---|---|
| SP-1 | Never reconstruct files from memory | Extended in v2 | Now covers *offers* to reconstruct. See §12.1.1 |
| SP-2 | Defer non-critical fixes to natural touchpoint | Carryforward | Direct; principle unchanged |
| SP-3 | Convergence is part of prompt delivery | **Dissolved** | Incompatible with orchestration/execution split (DD.§7.3) |
| SP-4 | Every Monitor produces visible output | Carryforward | Direct; applies to v2 monitors at orchestration |
| SP-5 | No heuristic guessing on ambiguous input | Carryforward | Direct; pairs with SP-9 |
| SP-6 | Rebuild at threshold (build-method discipline) | Carryforward | Direct; applies to spec/framework builds |
| SP-7 | File delivery is mandatory | Carryforward | Direct; reinforced by triple contract's file-based Output |
| SP-8 | (a) Canonical authority + (b) Filename discipline | **Split in rev. 2** | (a) stays SP-8; (b) becomes SP-14 |
| SP-9 | Silence is never consent | Carryforward | Direct; applies to operator close-loop, ratification, ambiguity escalation |
| SP-10 | Verify state before recommending | Carryforward as named principle | See §12.1.4. Mechanics live in Vendor Selection; principle stays SP-tier |
| SP-12 | Bounded-Search Disclosure | New in v2 | See §12.1.2 |
| SP-13 | Substrate Declaration | New in v2 | See §12.1.3 |
| SP-14 | Filename Discipline | New in rev. 2 (extracted from SP-8) | See §12.1.5 |

#### 12.2.1 SP-8 narrowed — Canonical Authority `[operator-scaffolding | stable]`

After the rev. 2 split, SP-8 carries one concern:

- The file delivered via `present_files` is canonical for that project state.
- Any edit made outside a Claude session (desktop editor, phone annotation, external LLM) must be flagged at the start of the next session so M2 (Version Drift) can reconcile.
- Filename discipline (the look-alike disambiguation pattern) extracted to SP-14.

#### 12.2.2 Carryforward SPs — body text

The six pure-carryforward SPs (SP-2, SP-4, SP-5, SP-6, SP-7, SP-9) carry forward from v1.10.4 verbatim in principle. Their v2 application surfaces are:

- **SP-2 (Defer non-critical fixes to natural touchpoint).** Applies in orchestration's What's next ladder — non-critical issues queue against priority tiers, fix at next aligned step. M10 fires when no natural touchpoint exists.
- **SP-4 (Every Monitor produces visible output).** Applies to all M1–M12 monitor fires in orchestration. Silent monitors are useless monitors.
- **SP-5 (No heuristic guessing on ambiguous input).** Applies wherever orchestration parses operator input. Pairs with M4 (Ambiguous Ask) firing.
- **SP-6 (Rebuild at threshold).** Applies to v2 framework builds (spec → PRISM_v2_0.md), Library Update sessions, large Master rewrites. Threshold ≤~8 sequential edits → str_replace; above → create_file rebuild.
- **SP-7 (File delivery is mandatory).** Applies to every orchestration session that updates Master, every execution session that produces Output, every Update session that produces a new Library file. Reinforced structurally by the triple contract's file-based Output (§3.2.3).
- **SP-9 (Silence is never consent).** Applies wherever operator decision is required: close-loop declarations, ratification, ambiguity escalation, migration override at 🔴, Project recommendation accept/decline. Active operator action required; no defaults-on-timeout.

---

## 13. Resolved direction summary

| DD reference | Item | This spec section | Decision summary |
|---|---|---|---|
| DD.§4.1.1 | Triple contract | §3.2 | Envelope + Self-check + Output, full schemas |
| DD.§4.2 | Master | §3.3 | Lifecycle, sections, proportionality |
| DD.§4.3 | What's next | §3.4 | Continuous; priority ladder |
| DD.§4.4 | Forward-compat | §3.5 | Tools slot, execution_mode flag |
| DD.§4.5 | Vendor Selection | §3.6 | Three-step routine, output block |
| DD.§5 | Setup | §6 | Iteration, three-layer readiness, seven probes, artifacts, stability |
| DD.§6 | Library integration | §7 | Integration points; v0.9 catalog by reference |
| DD.§13.1 item 1 | Single Envelope, dispatch spectrum | §4.1 | equivalence \| split \| limitation-named |
| DD.§13.1 item 2 | Rationale discipline | §4.2 | Per-mode templates |
| DD.§13.1 item 3 | Multi-vendor convergence | §4.3 | Vendor Triangulation (extracted from Probe 2); fires at N≥2; re-fires |
| DD.§13.1 item 4 | Asymmetric returns | §4.4 | Graceful degradation; no auto-retry |
| DD.§13.1 item 5 | Claude-baseline | §4.5 | Default; declared escapes |
| DD.§13.1 item 6 | Cost signaling | §4.6 | Implicit; no field |
| DD.§13.1 item 9 | Body convergence provisions | §4.11 | Composition rules |
| DD.§13.1 item 10 | Reconciliation | §4.7 | Auto-detect via Output fields |
| DD.§13.1 item 11 | Substitution absorption | §4.10 | At convergence; no re-dispatch demand |
| DD.§13.1 item 12 | Master tracking | §4.8 | Dispatch register schema |
| DD.§13.1 item 13 | Close-loop | §4.9 | Defined declaration set |
| DD.§13.2 item 14 | Telemetric framework | §5.1 | Seven signals, qualitative compounding |
| DD.§13.2 item 15 | M5 + M12 consolidation | §5.2 | Single M5; band-state output |
| DD.§13.2 item 16 | Continuous curation | §5.3 | Per-band behavior |
| DD.§13.2 item 17 | Migration handoff | §5.4 | Defined artifact format |
| DD.§13.2 item 18 | Failsafe recovery | §5.5 | Continuous-state mechanics |
| DD.§13.2 item 19 | Defensive migration | §5.6 | Band × seam table |
| DD.§13.3 Idea #1 | Claude Project | §8.1 | Setup recommendation; fallback |
| DD.§13.3 Idea #2 | Session history | §8.2 | Trigger set; advisory; SP-1/SP-12 |
| DD.§14 item 1 | M2 fate | §9.1 | Bump atomicity spec; M2 retained |
| DD.§14 item 2 | Attachment warnings | §9.2 | Output footer; trigger conditions |
| DD.§14 item 3 | M8 vs DD.§6.6 | §9.3 | Boundary table; separate sections |
| Rev. 2 audit | Probe 2 decoupled | §4.3 + §6.3.2 | Vendor Triangulation extracted; Adversarial Scope is Setup-only |
| Rev. 2 audit | P5 Consolidation dissolved | §6.3 | Structural overlap-spotting folds into P1/P2 LLM judgment |
| Rev. 2 audit | P7 User Voice added | §6.3.7 | Mines real user signal at Setup; v1.x role promoted from enrichment to probe |
| Rev. 2 audit | M12 Result Completeness Check added | §11.2.4 | Convergence-time monitor; v1.x Coverage role lineage |
| Rev. 2 audit | SP-8 split | §12.1.5 + §12.2.1 | SP-8 Canonical Authority (narrowed); SP-14 Filename Discipline (new) |
| Rev. 2 audit | SP-10 retained as named principle | §12.1.4 | Mechanics in Vendor Selection; principle stays SP-tier |
| Rev. 2 audit | M7 renamed Claim Conflict | §11.2.2 | v1.x had Assumption Register; v2 doesn't |
| Rev. 2 audit | Envelope/Output field renames | §3.2 | Mode → Vendor config; Dispatch mode → Dispatch shape; Mode rationale → Dispatch rationale |
| Rev. 2 audit | System overview added | §2 | Construct cards + visual map + lifecycle slots |
| Rev. 2 audit | v1.x SP carryforward catalog | §12.2 | Per-SP disposition explicit; closes rev. 1 build-residual #1 |
| Rev. 2 audit | v1.x → v2 surface drift documented | Appendix C | Per-construct comparison |

---

## 14. Open empirical items (post-release calibration)

Items the v2.0 spec does not fix because they require real-use signal. From DD.§11 and inherited:

1. **Probe iteration floors and ceilings** (DD.§11 item 3). Current: minimum 2, soft ceiling at 4. Calibrate against real Setup runs.
2. **Probe 1 *fires-maybe* operator-fatigue** (DD.§11 item 14). Volume of *maybes* per project; mitigation effectiveness of judging-LLM silent resolution.
3. **DD.§6.6 point-refresh fatigue** (DD.§11 item 14). Frequency of `stale-refresh` per project; threshold for advisory accumulation toward Update session.
4. **Probe 7 lens accretion path** (DD.§11 item 15). Lenses surfaced by domain-practitioner survey that aren't in the catalog. Where do they go: per-project Learnings Register, staging area for Update-session promotion, or other?
5. **Multi-vendor Self-check verification** (DD.§4.1.1 footing). Verify Self-check block adherence on Gemini, ChatGPT, Perplexity. Currently Claude-family verified only.
6. **M5 band thresholds** (§5.1). Volumetric thresholds (50KB / 200KB; 20 / 40 turns; etc.) are rev. 1 draft estimates. Calibrate against real sessions.
7. **Update session trigger threshold** (§7.5). Rev. 1 draft: 3 stale-pattern accumulations across 6+ months. Calibrate against real maintenance cadence.

These ride into the build (Phase 4) and the dogfood run (Phase 4 follow-up per DD.§12.1) as flagged items.

---

## 15. Build-time residual items

Items the build (Phase 4) consumes alongside this spec:

1. **Complete v1.x SP carryforward catalog.** Enumerate all v1.10.4 Standing Principles; note carryforward / reshape / dissolve disposition for each. Spec only covers SP-1 ext, SP-12, SP-13, and SP-3 dissolution explicitly.
2. **Atomic prompt template — full v2 form.** DD.§7.1 references the carrying forward of the atomic prompt template "reshapes in v2 to carry the paired Execution Envelope (inbound) + Execution Output (outbound) contract." This spec specifies the contract. The template integration (the prompt-body wrapper that embeds the contract) is build-time work.
3. **Filename-convention canonicalization.** Master, Output, handoff, and Update-session-output filename conventions all specified in this spec, but a single canonical reference table in PRISM_v2_0.md is build-time work.
4. **Decision tag application.** This spec carries tags on new decisions; build applies the same tagging convention to every decision in PRISM_v2_0.md. Appendix C of v2.0 holds the tag index per the v1.x convention.
5. **Migration recovery from missing handoff.** When the operator opens a fresh session without a handoff (operator skipped the migration step at 🔴, or handoff was lost), what does the framework do? Rev. 1 draft: orchestration runs SP-1 protocol — locate Master via past-conversation search; if Master found, attach and proceed; if not, walk SP-1 escalation. This is implicit in §12.1.1 + §8.2 but not called out as a named recovery flow. Build elaborates if needed.
6. **Operator hint catalog expansion.** §3.2.4 carries a rev. 1 draft list. Build canonicalizes.

---

## 16. Flagged-items register — alternatives considered (per D6 closure)

This register captures alternatives considered for each spec decision, the alternative chosen, and the rationale. Per DD.§11 item 9 / D6 closure, design alternatives are picked directly in this spec session; this register is the audit trail.

### 16.1 Prompt-package engine

#### Item — Single-Envelope-with-spectrum shape (§4.1)

- **Alt A** *(chosen)*: Single Envelope with `Dispatch shape:` field carrying `equivalence | split | limitation-named`.
- **Alt B**: Separate Envelope template per dispatch mode (three distinct headers).
- **Alt C**: Free-form rationale field with no taxonomy.
- **Rationale for A**: Cleanest, most legible, easiest to spec. Operator sees one Envelope shape across all dispatches; the mode field is the discriminator. Alt B fragments the contract (three things to learn, three things to maintain). Alt C abandons the structural promise of the Envelope (orchestration cannot reliably parse free-form mode rationale into a dispatch-shape decision).
- **Review trigger**: revisit if real-use surfaces a fourth mode that can't be expressed as a sub-variant of the three.

#### Item — Multi-vendor convergence firing rule (§4.3)

- **Alt A**: Wait for all N before firing convergence (completeness-first).
- **Alt B** *(chosen)*: Re-run convergence as each new return arrives (incremental, more responsive). Vendor Triangulation fires at N≥2; re-fires on every subsequent return.
- **Alt C**: Fire after first 2, re-run on 3rd+.
- **Rationale for B**: Per DD.§13.1 item 3 explicit guidance ("fires at N≥2; re-runs as returns arrive"). Operator gets analytical signal earlier; partial-return reality (some vendors will fail or be slow) is absorbed gracefully.
- **Cost of B**: Convergence delta document churns (replaced on each return). Acceptable per the continuous-state mechanic — Master holds the latest, Changelog tracks history.

#### Item — Asymmetric parallel return handling (§4.4)

- **Alt A**: Block convergence until all N return; require operator to chase failed dispatches.
- **Alt B** *(chosen)*: Convergence proceeds with whatever returned; failures flagged with named gap.
- **Alt C**: Auto-retry failed dispatches.
- **Rationale for B**: DD.§3.6 — design-authority-without-access-gating. Failures are absorbed, not retried-on-demand. Alt A creates blockage on operator's vendor access (against DD.§3.6). Alt C requires the framework to know the operator has retry budget on the failed vendor (it doesn't).
- **Review trigger**: real-use surfacing of frequent multi-vendor partial-failure patterns → revisit whether soft-retry (operator-elective, framework-suggested) earns its place.

#### Item — Claude-baseline default (§4.5)

- **Alt A**: Always require multi-vendor for X categories (mechanical rule).
- **Alt B** *(chosen)*: Claude-baseline default; multi-vendor for declared categories; escape hatch for "Claude-cannot-do-this" cases.
- **Alt C**: Operator-driven only (no framework guidance).
- **Rationale for B**: Honest about capability. Most prompts fit Claude. The escape hatch names the genuine analytical reason (live-web breadth → Perplexity; long-context → Gemini). Alt A would over-spec; Alt C would under-spec.

#### Item — Cost signaling (§4.6)

- **Alt A**: Explicit `cost_estimate:` field in Envelope.
- **Alt B** *(chosen)*: Implicit via dispatch shape + rationale; no separate field.
- **Alt C**: Operator-only concern; no framework presence.
- **Rationale for B**: Per DD.§13.1 item 6 explicit guidance. Cost is operator-specific (subscription tiers vary) and changes faster than the framework can patch. Field would be inaccurate or operator-specific. Implicit signaling via dispatch shape carries enough for the operator without false precision.

#### Item — Reconciliation mechanic (§4.7)

- **Alt A**: Operator manually reconciles after each return.
- **Alt B** *(chosen)*: Output signature carries Vendor/Mode; orchestration auto-reconciles against Envelope.
- **Alt C**: No reconciliation; trust operator narration.
- **Rationale for B**: The Output already carries the data; using it for reconciliation is free. Alt A puts unnecessary operator burden; Alt C abandons the contract's structural promise.

#### Item — Substitution absorption (§4.10)

- **Alt A**: Re-dispatch on substitution.
- **Alt B** *(chosen)*: Absorb at convergence; no re-dispatch.
- **Alt C**: Block convergence until original-vendor execution.
- **Rationale for B**: DD.§3.6 design-authority-without-access-gating. Substitution is operator-access reality; framework absorbs gracefully. Alt A and C both penalize the operator for vendor-access mismatch the framework caused by recommending a vendor the operator may not have.

#### Item — Master tracking field (§4.8)

- **Alt A**: Single status field per prompt.
- **Alt B** *(chosen)*: Structured Dispatch register table with recommended-vs-executed columns.
- **Alt C**: Embedded in convergence findings, not separate.
- **Rationale for B**: Status alone insufficient — operator and orchestration both need to see "what was recommended, what actually ran" for traceability. Alt C buries dispatch state inside findings; less retrievable.

#### Item — Close-loop declarations (§4.9)

- **Alt A**: Operator narrates freely; orchestration interprets.
- **Alt B** *(chosen)*: Defined declaration set with explicit semantics.
- **Alt C**: Auto-close after timeout.
- **Rationale for B**: Defined set allows orchestration to update Dispatch register reliably. Alt A's interpretation introduces ambiguity (M4 fires more often). Alt C — what timeout? A long prompt may legitimately take days.

### 16.2 Context-pressure framework

#### Item — Signal compounding rule (§5.1)

- **Alt A**: Weighted sum to numeric score → band by threshold.
- **Alt B** *(chosen)*: Qualitative compound read; behavioral signals weight higher than volumetric.
- **Alt C**: Single-strongest-signal rule (one signal sufficient).
- **Rationale for B**: Per DD.§3.7 — *"telemetric framework: observes multiple weak signals continuously, compounds them into a strong read."* Alt A revives the arithmetic illusion v2 explicitly rejects (DD.§3.7 — *"calibration chain is unreliable at every link"*). Alt C is too brittle; one false signal moves bands.
- **Cost of B**: Calibration is empirical, will need real-use feedback to refine thresholds. Captured in §14.

#### Item — M5 + M12 consolidation (§5.2)

- **Alt A**: M5 fires on volumetric only; new M12.x for behavioral.
- **Alt B** *(chosen)*: Single M5 absorbs both, fires on band-state changes.
- **Alt C**: No monitor; band state is structural.
- **Rationale for B**: Per DD.§7.2 — M12 retired into M5's reshape. Single monitor is simpler; band state captures everything M5 + M12 separately did.

#### Item — Continuous-curation trigger (§5.3)

- **Alt A**: Curation event-triggered (fire on 🟠).
- **Alt B** *(chosen)*: Curation continuous from 🟡.
- **Alt C**: Curation operator-only.
- **Rationale for B**: Per DD.§13.2 item 16 — *"continuous-curation posture — earlier and lighter."* Earlier curation prevents the fire-drill posture at 🟠/🔴.

#### Item — Migration handoff format (§5.4)

- **Alt A**: Handoff is an ad-hoc Master snapshot.
- **Alt B** *(chosen)*: Defined handoff artifact with required sections.
- **Alt C**: Handoff is regenerated *What's next* + Master attachment.
- **Rationale for B**: Defined artifact is reproducible; the new session knows exactly what to expect. Alt A loses portability; Alt C duplicates *What's next* without adding the migration-context fields (reason for migration, operator state).

#### Item — Continuous-state mechanic (§5.5)

- **Alt A**: Master + What's next written on demand.
- **Alt B** *(chosen)*: Master + What's next written at every orchestration turn-close, regardless of band.
- **Alt C**: Written only at phase boundaries.
- **Rationale for B**: Per DD.§3.7 — *"misreads are low-cost"* requires continuous state. Alt A and C leave windows where misread → loss. Alt B's cost (writing every turn) is small.

#### Item — Migration band × seam matrix (§5.6)

- **Alt A**: Migration only at 🔴.
- **Alt B** *(chosen)*: Migration spec keyed to band × seam.
- **Alt C**: Operator-driven migration only.
- **Rationale for B**: Per DD.§3.7 — *"defensive migration at natural seams."* Alt A is reactive (DD.§3.7 — *"migration is planning, not rescue"*); Alt C abandons framework guidance.

### 16.3 Parked v2 design ideas

#### Item — Claude Project recommendation (§8.1)

- **Alt A**: Mandatory (Setup halts if Project not created).
- **Alt B** *(chosen)*: Recommended with graceful degradation fallback.
- **Alt C**: Optional silent (offered once if at all).
- **Rationale for B**: Per DD.§13.3 — *"fallback when the operator declines or cannot create a Project (graceful degradation, not refusal to proceed)."* Alt A creates an access-gating posture (DD.§3.6 violation if operator can't create a Project). Alt C under-uses an obvious leverage point.

#### Item — Session history triggers (§8.2)

- **Alt A**: Always consult session history at every turn-close.
- **Alt B** *(chosen)*: Consult on Monitor-fire triggers (M2, M3) + named ambiguity conditions.
- **Alt C**: Operator-request only.
- **Rationale for B**: Targeted consultation balances signal vs. cost. Alt A is noisy and SP-12 disclosure overhead is high. Alt C misses the failure modes Idea #2 was designed to catch.

### 16.4 Resolved deferrals

#### Item — M2 disposition post-bump-atomicity (§9.1)

- **Alt A**: Retire M2 (drift impossible by construction).
- **Alt B** *(chosen)*: Keep M2 as low-cost safeguard for residual cases.
- **Alt C**: Convert M2 to an SP.
- **Rationale for B**: Per DD.§7.2 — *"if v2's spec eventually specifies bump atomicity such that drift becomes impossible by construction, M2 quietly never fires — no cost."* Bump atomicity makes drift unlikely but not impossible (operator attaches old Master from cloud archive; cross-device sync delivers stale file). M2 retained at low cost; checks-and-balances framing (DD.§7.2) supports retention.

#### Item — Attachment warnings field placement (§9.2)

- **Alt A** *(chosen)*: Output footer area, after Operator next.
- **Alt B**: Output header area, alongside Vendor/Mode.
- **Alt C**: Separate Attachment-warnings block adjacent to Output.
- **Rationale for A**: Footer keeps the Output content the visual focus; warnings are a footnote, not a header. Alt B confuses execution metadata with operational notes. Alt C creates two blocks where one suffices.

#### Item — M8 vs. DD.§6.6 boundary (§9.3)

- **Alt A**: Single mechanism covering both.
- **Alt B** *(chosen)*: Two separate mechanisms with explicit boundary.
- **Alt C**: Crowd one out (e.g., DD.§6.6 absorbs M8).
- **Rationale for B**: Per DD.§14 item 3 — *"distinction clear conceptually."* The two surfaces (audit evidence vs. framework anchor) have different lifecycles, different resolutions. Combining them obscures the analytical distinction.

### 16.5 Architecture-level decisions

#### Item — Triple contract structure (§3.2)

- **Alt A** *(chosen)*: Three blocks (Envelope, Self-check, Output).
- **Alt B**: Two blocks (Envelope absorbs Self-check inline).
- **Alt C**: Four blocks (split Envelope into vendor-config + content-prompt-frame).
- **Rationale for A**: Per DD.§4.1.1 explicit structure. Self-check has its own concern (substrate verification per SP-13) that's separable from envelope (vendor + dispatch context) and output (return shape). Alt B couples concerns that have different lifecycles (Self-check fires once per session; Envelope is the dispatch-time artifact). Alt C over-decomposes.

#### Item — What's next priority ladder (§3.4)

- **Alt A**: Static priority ladder (the 10-tier list).
- **Alt B** *(chosen)*: Static priority ladder with operator-tie escalation.
- **Alt C**: Dynamic ladder reordered per project.
- **Rationale for B**: Per DD.§4.3 — *"escalation to operator on ties."* Static ladder is predictable; ties surface to operator (SP-9 lineage). Alt C is over-flexible; project shapes don't usually need ladder reordering.

### 16.6 Rev. 2 alternatives — audit-driven decisions

#### Item — Probe 2 decoupling (§4.3 + §6.3.2)

- **Alt A**: Keep Probe 2 as single construct firing in two contexts (rev. 1 status).
- **Alt B** *(chosen)*: Decouple into Adversarial Scope Probe (Setup-only, §6.3.2) + Vendor Triangulation (Layer-1 only, §4.3, outside probe taxonomy).
- **Alt C**: Keep both jobs but rename to a unifying name (e.g., "Adversarial Convergence").
- **Rationale for B**: Single-responsibility violation. Different surfaces (draft strategy vs returned findings), different lifecycles (Setup vs Layer-1), different output shapes (omission list vs convergence delta). Alt A perpetuates the violation; Alt C papers over it with naming.

#### Item — P5 Consolidation status (§6.3)

- **Alt A**: Keep P5 Consolidation as standalone probe.
- **Alt B** *(chosen)*: Dissolve. Structural overlap-spotting is judgment work LLM does inside P1/P2 grading.
- **Alt C**: Fold into Layer-2 readiness check.
- **Rationale for B**: v2 philosophy is principle-heavy / specification-light. Standalone P5 is checkbox-shaped — explicitly enumerating overlap-detection as its own probe contradicts the LLM-judgment posture. Alt C blurs Setup-time vs Layer-2 boundary.

#### Item — User Voice placement (§6.3.7)

- **Alt A**: Drop User Voice (v1.x role) entirely.
- **Alt B** *(chosen)*: Promote to Setup probe — imports user signal *before* strategy hardens.
- **Alt C**: Add as universal Library lens.
- **Alt D**: Add as Layer-1 enrichment role.
- **Rationale for B**: User Voice is not a coverage check (Alt C); it's external-signal import that shapes the strategy. Belongs alongside P6 Domain Reconnaissance — both bring outside signal in early. Alt D would replicate v1.x's enrichment posture, which v2's principle-heavy philosophy moves away from.

#### Item — Result Completeness Check placement (§11.2.4)

- **Alt A**: Add as new probe (Setup-time).
- **Alt B** *(chosen)*: Add as convergence-time monitor (M12) — distinct from M6/M7/M8 by detection focus.
- **Alt C**: Fold into Vendor Triangulation.
- **Rationale for B**: The check operates on *single-prompt* findings (within-domain coverage), not on *multi-vendor* findings. Different surface from Vendor Triangulation. Setup-time placement (Alt A) doesn't fit — the check needs returned findings, not draft strategy.

#### Item — M12 numbering (§11.2.4)

- **Alt A** *(chosen)*: Reuse M12 slot. v1.x M12 was Conversation Pressure (retired in v2; absorbed into M5). Slot is free.
- **Alt B**: Use M13 to preserve M12's retired marker.
- **Rationale for A**: Clean numbering with no gap. v1.x → v2 mapping table makes the slot reuse explicit; no operational ambiguity in v2 sessions.

#### Item — SP-8 split (§12.1.5 + §12.2.1)

- **Alt A**: Keep SP-8 carrying both concerns (canonical authority + filename discipline).
- **Alt B** *(chosen)*: Split SP-8 (narrowed to Canonical Authority) + new SP-14 Filename Discipline.
- **Alt C**: Absorb filename discipline into spec's filename-convention reference table (no SP).
- **Rationale for B**: Two distinct concerns. Filename discipline is operator-scaffolding-tier (defends against the wrong-similar-file failure mode v2 creates by design); deserves SP framing. Alt C loses the scaffolding posture.

#### Item — SP-10 status (§12.1.4)

- **Alt A**: Keep SP-10 only as Vendor Selection mechanics; remove from SP catalog.
- **Alt B** *(chosen)*: Retain as named principle. Vendor Selection is one application; point refresh and Update sessions are others; future surfaces inherit cleanly.
- **Rationale for B**: Principles travel; mechanics don't. Naming SP-10 explicitly preserves portability.

#### Item — M7 rename Claim Conflict (§11.2.2)

- **Alt A**: Keep "Assumption Conflict" name; document the v1.x-vs-v2 surface drift.
- **Alt B** *(chosen)*: Rename "Claim Conflict" — match the actual v2 surface (finding-vs-finding, no Assumption Register).
- **Rationale for B**: Face-value naming (DD.§2.6). v2 has no Assumption Register; calling the monitor "Assumption Conflict" perpetuates v1.x semantic.

#### Item — Field naming inside contracts (§3.2)

- **Alt A**: Keep "Mode / Dispatch mode / Mode rationale" (rev. 1 names).
- **Alt B** *(chosen)*: Rename to "Vendor config / Dispatch shape / Dispatch rationale" — three distinct names for three distinct concerns.
- **Rationale for B**: Three uses of "Mode" in the Envelope schema collide. Reader cannot tell at face value which field carries which concept. Rename resolves at low cost (rev 2 is operator-internal).

#### Item — System overview placement (§2)

- **Alt A**: Place at front of spec as new §2 (renumber §2-§16 → §3-§17).
- **Alt B**: Place as Appendix C at back.
- **Alt C**: Place as §1.4 inside Scope.
- **Alt A chosen**. Reader orientation belongs at the entry point. Renumbering cost (cross-ref updates) is one-pass and clean. Alt B less prominent; Alt C overloads §1.

### 16.7 Carried items needing build-time decisions

The following decisions are flagged for build-time treatment (not made in this rev):

- v1.x SP carryforward catalog complete enumeration (§15 item 1).
- Atomic prompt template v2 form (§15 item 2).
- Filename-convention canonical reference table (§15 item 3).
- Decision tag application across all of v2.0 (§15 item 4).
- Missing-handoff recovery flow named explicitly (§15 item 5).
- Operator hint catalog expansion (§15 item 6).

---

## 17. Status

**Rev. 2.** Folds in audit findings from `PRISM_v2_spec_rev1_audits.md` (April 2026). Major changes from rev. 1: Probe 2 decoupled into Adversarial Scope (Setup) + Vendor Triangulation (Layer-1, outside probe taxonomy); P5 Consolidation dissolved; P7 User Voice added; M7 renamed Claim Conflict; M12 reused for Result Completeness Check (v1.x M12 was retired); SP-8 split into Canonical Authority (narrowed) + SP-14 Filename Discipline; SP-10 retained as named principle; Envelope/Output field renames (Mode → Vendor config; Dispatch mode → Dispatch shape; Mode rationale → Dispatch rationale); System overview added as §2; v1.x SP carryforward catalog completed; v1.x → v2 surface drift documented (Appendix C). Capture discipline per DD: decisions captured at current fidelity.

**Phase position** (per DD.§12.1): Phase 3 — Specification. Output is input to Phase 4 — Build.

**Next steps** (per DD.§12.1):

1. Operator review of rev. 2.
2. Build (Phase 4): construct `PRISM_v2_0.md` from this spec + Lens Library v0.9. Full rebuild not patched (DD.§10.1); SP-6 deterministic build method.
3. Integration dogfood run on a small real project (Phase 4 follow-up). Surfaces:
   - Multi-vendor Self-check empirical gap.
   - M5 telemetric framework calibration on real signals.
   - *What's next* behavior under messy state.
   - User Voice probe effectiveness in real Setup runs.
   - M12 Result Completeness Check sensitivity.
4. Release (Phase 5): release notes, RELEASING.md updates, CONTRIBUTING.md updates, signed commit, tag `v2.0.0`, PAT-driven push.

---

## Appendix A — Terminology updates beyond DD Appendix A

This spec introduces the following terminology not in DD Appendix A:

| Term | Definition |
|---|---|
| **Adversarial Scope Probe** | Setup-time probe (P2). Hunts silent omissions in draft strategy. Library-driven; multi-vendor recommended. Spec §6.3.2. |
| **Vendor Triangulation** | Layer-1 convergence pass. Triangulates findings across N vendor returns from an `equivalence` dispatch. Lives outside the probe taxonomy. Fires at N≥2; re-fires per return. Spec §4.3. |
| **Result Completeness Check** | Convergence-time monitor (M12). Detects within-domain coverage gaps in returned findings. v1.x lineage: Coverage role. Spec §11.2.4. |
| **User Voice Probe** | Setup-time probe (P7). Imports real end-user signal. v1.x lineage: User Voice (Phase 2 enrichment). Spec §6.3.7. |
| **Domain Reconnaissance Probe** | Setup-time probe (P6). Surveys domain practice + authoritative-source detection + Jurisdiction map. v1.x lineage: Discovery role. Spec §6.3.6. |
| **Decision Framing Probe** | Setup-time probe (P3). Produces Decision brief + Stakeholder register. Renamed from rev. 1's "Stakeholder Probe" to capture full output. Spec §6.3.3. |
| **Dispatch register** | Master section tracking recommended-vs-executed state per prompt. Schema in §4.8. |
| **Convergence delta** | Vendor Triangulation output document for an `equivalence` dispatch. Schema in §4.3.1. |
| **Probe 1 disposition** | Tri-state grade per Lens against the strategy. States: `fires-covered`, `fires-uncovered`, `doesn't-fire`, `fires-maybe (dig-in / opt-out)`. |
| **Anchor disposition** | Currency state per `rubric_anchor:` entry. States: `fresh`, `stale-refresh`, `stale-accumulating`. |
| **Saturation** | Per DD Appendix A. Two consecutive iterations produce no material change to coverage or strategy. Material change criteria in §6.2. |
| **Delta finalization** | When all expected vendor returns are in for an `equivalence` dispatch and Vendor Triangulation closes the convergence delta. Replaces rev. 1's overloaded "convergence saturation" term. §4.3. |
| **Natural seam** | A transition point where migration is low-cost. Defined set: convergence round complete, phase boundary, deliverable shipped, setup iteration complete (§5.3). |
| **Bump atomicity** | The mechanic that ties Master version increments to defined triggers (phase transitions, convergence rounds, probe iterations, schema changes). Spec in §9.1. |
| **Migration handoff** | Defined artifact produced at 🔴 (mandatory) or 🟠 (optional) for fresh-session continuity. Schema in §5.4. |
| **Continuous-state mechanic** | Master + *What's next* written at every orchestration turn-close, regardless of band state. §5.5. |
| **Vendor Selection block** | Orchestration-visible output of the Vendor Selection routine; not embedded in the Envelope sent to vendor. Schema in §3.6. |
| **Update session** | Standalone, rare, operator-gated session that maintains Library currency. Spec in §7.5. |
| **Point refresh** | Per-project, in-Setup currency check on Library `rubric_anchor:` entries. Spec in §7.4. |
| **Dispatch shape** | Envelope field carrying the dispatch structural shape: `equivalence`, `split`, or `limitation-named`. Renamed from rev. 1's "Dispatch mode" to avoid collision with `Vendor config` (vendor-specific config flags). |
| **Vendor config** | Envelope/Output field carrying vendor-specific configuration flags (e.g., `Deep Research ON, extended thinking ON`). Renamed from rev. 1's "Mode". |
| **Dispatch rationale** | Envelope field carrying one positive-framing line per dispatch variant component. Renamed from rev. 1's "Mode rationale". |

---

## Appendix B — Spec-level decision tag index

Per the v1.x convention. Tags applied to decisions in this spec:

### B.1 `[structural | stable]`

§3.2 (triple contract); §3.3 (Master); §3.4 (*What's next*); §3.5 (forward-compat); §4.1 (single-Envelope spectrum); §4.3 (Vendor Triangulation); §4.4 (asymmetric returns); §4.7 (reconciliation); §4.8 (Dispatch register); §4.9 (close-loop); §4.10 (substitution absorption); §4.11 (body convergence provisions); §5.1 (telemetric framework — note: methodological in axis 1; structural here covers spec form); §5.2 (M5); §5.4 (handoff format); §5.5 (continuous-state); §5.6 (migration matrix); §6.3.2 (Adversarial Scope Probe); §6.3.7 (User Voice Probe); §9.1 (M2); §9.2 (Attachment warnings); §9.3 (M8 vs DD.§6.6); §11.1.1 (M1); §11.2.1 (M6); §11.2.2 (M7 Claim Conflict); §11.2.4 (M12 Result Completeness Check); §11.3.1 (M3); §11.3.2 (M10); §11.3.3 (M11).

### B.2 `[methodological | stable]`

§4.2 (Dispatch rationale discipline); §4.6 (cost signaling); §7.4 (point refresh); §7.5 (Update session); §11.1.3 (M4); §11.1.5 (M9).

### B.3 `[methodological | review-if: substrate shifts]`

§5.1 (telemetric framework — calibration thresholds empirical); §5.2 (M5 — band thresholds empirical).

### B.4 `[methodological | review-if: vendor landscape changes]`

§3.6 (Vendor Selection routine).

### B.5 `[vendor-dependent | review-if: orchestration vendor changes]`

§8.1 (Claude Project recommendation); §8.2 (session history mechanism).

### B.6 `[vendor-dependent | review-if: vendor landscape changes]`

§4.5 (Claude-baseline + escape hatch list).

### B.7 `[operator-scaffolding | stable]`

§12.1.1 (SP-1 ext); §12.1.2 (SP-12); §12.1.3 (SP-13); §12.1.4 (SP-10 named principle); §12.1.5 (SP-14 Filename Discipline); §12.2.1 (SP-8 Canonical Authority — narrowed).

**Tag count:** 36 across 36 decision sites. (Build-phase will tag remaining decisions across v2.0.)

---

## Appendix C — v1.x → v2 surface drift

Construct-by-construct mapping for operators familiar with v1.10.4. Direct carryforwards (🔁) and new constructs (🆕) marked; surface drift items documented with the change.

### C.1 Sessions and lifecycle

| v2 construct | v1.10.4 counterpart | Disposition |
|---|---|---|
| Orchestration session | Setup + convergence sessions (PRISM.md attached) | v2 names the split that v1.x ran inconsistently |
| Execution session | Phase 1 specialist prompt session | Hardened contract via triple |
| Update session | — | 🆕 |
| Master | Starter | Renamed; functionally same |
| *What's next* | TRI-21 progress pointer (single ID) | Reshaped to full artifact |
| Lens Library | — | 🆕 — core v2 architecture |

### C.2 Probes

| v2 probe | v1.x counterpart | Notes |
|---|---|---|
| P1 Coverage grading | — | 🆕 Library-driven |
| P2 Adversarial Scope | Red Team (Phase 2 enrichment) — partial | Reshape — Red Team operated post-finding; P2 operates pre-execution |
| P3 Decision Framing | Implicit in Setup brief | Made explicit; renamed in rev. 2 from "Stakeholder" to capture full output (Decision brief + Stakeholder register) |
| P4 Pre-mortem | — | 🆕 |
| P5 Falsifier | Red Team (in spirit) | Falsifier is at Setup; Red Team was post-finding |
| P6 Domain Reconnaissance | Discovery (Setup-phase enrichment) | Direct counterpart; renamed in rev. 2 to cover practice survey + authoritative-source check + Jurisdiction map |
| P7 User Voice | User Voice (Phase 2 enrichment role) | Promoted from Phase 2 enrichment to Setup probe — informs strategy *before* execution |

**v1.x roles not migrating as probes:**
- **Coverage** (Phase 2 enrichment, "find what a specific prompt missed within its domain") → became **M12 Result Completeness Check** (convergence-time monitor)
- **Fact Check** (Phase 2 enrichment) → absorbed into M8 Stale Source + Layer-1 reconciliation
- **Deep Research** (Phase 2 enrichment) → Vendor Selection mode field (§3.6)

### C.3 Monitors

| v2 | v1.x | Disposition |
|---|---|---|
| M1 Missing Inputs | M1 Missing Inputs | 🔁 |
| M2 Version Drift | M2 Version Drift | 🔁 — surface narrowed to filename version (v1.x also caught Changelog-vs-header mismatches; that surface absorbed by bump atomicity §9.1) |
| M3 Sequence Violation | M3 Sequence Violation | 🔁 |
| M4 Ambiguous Ask | M4 Ambiguous Ask | 🔁 |
| M5 Context Pressure | M5 Attachment Pressure + M12 Conversation Pressure | Merged into single telemetric monitor |
| M6 Premise Shift | M6 Premise Shift | 🔁 — surface broadened (premises now read from Setup artifacts: Decision brief / Stakeholder register / Claim inventory / Jurisdiction map; v1.x read prompt context sections) |
| M7 Claim Conflict | M7 Assumption Conflict | Renamed in rev. 2 — v1.x had Assumption Register; v2 reads finding-vs-finding directly |
| M8 Stale Source | M8 Stale Source | 🔁 — surface narrowed (audit evidence only; framework-anchor staleness is point refresh §7.4) |
| M9 Convergence Type Drift | M9 Convergence Type Drift | 🔁 — surface broadened (also catches dispatch-mode treatment errors: equivalence treated as split, etc.) |
| M10 Rerun/Fix | M10 Rerun/Fix | 🔁 |
| M11 Layer 2 Readiness | M11 Layer 2 Readiness | 🔁 |
| M12 Result Completeness Check | (slot was M12 Conversation Pressure — retired) | 🆕 in v2 (slot reused; v1.x M12 absorbed into M5) |

### C.4 Standing Principles

| v2 SP | v1.x | Disposition |
|---|---|---|
| SP-1 ext | SP-1 (Never reconstruct from memory) | Extended in v2 — covers *offers* to reconstruct |
| SP-2 | SP-2 (Defer non-critical fixes) | 🔁 |
| (none) | SP-3 (Convergence in prompt session) | Dissolved — incompatible with orchestration/execution split |
| SP-4 | SP-4 (Monitors visible) | 🔁 |
| SP-5 | SP-5 (No heuristic guessing) | 🔁 |
| SP-6 | SP-6 (Rebuild at threshold) | 🔁 |
| SP-7 | SP-7 (File delivery mandatory) | 🔁 |
| SP-8 narrowed | SP-8 (Canonical authority + filename disambig) | Split in rev. 2 — (a) stays SP-8; (b) becomes SP-14 |
| SP-9 | SP-9 (Silence is never consent) | 🔁 |
| SP-10 | SP-10 (Verify state before recommending) | 🔁 as named principle; mechanics live in Vendor Selection §3.6 |
| SP-12 | — | 🆕 Bounded-Search Disclosure |
| SP-13 | — | 🆕 Substrate Declaration |
| SP-14 | (extracted from SP-8) | 🆕 in rev. 2 — Filename Discipline |

### C.5 Other constructs

| v2 | v1.x | Disposition |
|---|---|---|
| Triple contract (Envelope/Self-check/Output) | Atomic prompt template + Execution notes | Reshape; Self-check is new |
| Vendor Selection | Execution notes (per-prompt prose at Setup, SP-10) | Reshape from Setup-prose to dispatch-time live step |
| Vendor Triangulation | (no v1.x mechanism for this — Layer-1 reconciliation was claim-by-claim) | 🆕 — extracted from rev. 1's Probe 2 |
| Bands (🟢🟡🟠🔴) | Context Pressure Bands | 🔁 |
| Two-layer convergence | Two-layer convergence | 🔁 |
| Setup artifacts (Decision brief / Stakeholder reg / Claim inv / Jurisdiction map) | Implicit in Setup brief | Made explicit and structured |
| Scope Flags | Scope Flags (5: SF1-SF5) | All dissolved per DD.§7.3 |
| Runtime Profile | Runtime Profile | Dissolved into telemetric framework |
| GATE-0 / GATE-1 / GATE-2 | Gates | Folded into Monitors + What's next + M11 |
| Adaptations | Adaptations | Lighter — strategy-stability with revisable-at-convergence + Master version bump |
| Discrepancy Check | Discrepancy Check (prompt-template mechanic) | Absorbed into M7 Claim Conflict + Layer-1 reconciliation |

### C.6 Nomenclature changes

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

*End of PRISM v2 specification rev. 2.*
