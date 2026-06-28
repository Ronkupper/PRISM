---
name: core
description: >-
  PRISM — a structured, multi-session, multi-vendor LLM-orchestrated audit and
  research framework (orchestration on Claude, Opus-class). Trigger when the user
  invokes PRISM by name or by a recognizable PRISM construct: PRISM / PRISM audit /
  begin a PRISM audit; a Master file or any filename matching *_master_p*.md; Prompt
  Strategy; the Lens Library; Vendor Selection or Vendor Triangulation; Setup probes
  P1–P7; Monitors M1–M12; Standing Principles SP-*; the Execution Envelope /
  Self-check / Output triple contract; Dispatch register or Dispatch shape
  (equivalence / split / limitation-named); the "What's next" artifact; context
  bands 🟢🟡🟠🔴; migration handoff; the P0/P1 boundary; three-layer readiness;
  Update sessions or point refresh; or Setup artifacts (Decision brief / Stakeholder
  register / Claim inventory / Jurisdiction map). Also trigger when the user attaches
  a Master or Lens Library file. Do NOT trigger for generic audit, research, or
  prompt-engineering work that does not invoke PRISM by name or construct, nor for
  v1.x-only terms (Starter, GATE-0/1/2, Scope Flags, Runtime Profile) — v2 supersedes
  them.
---

# PRISM framework loader

This Skill loads PRISM — the canonical operating framework for structured,
multi-session, multi-vendor LLM-orchestrated audit and research. The framework is
decomposed into a lean always-loaded **core** plus **on-demand bundles**; load the
core first, fetch a bundle only when the work in front of you needs it.

## When triggered

1. **Read `PRISM_core.md` in full** before acting — it is the operating core
   (operating model and architecture, the Execution Envelope / Self-check / Output
   triple contract, the prompt-package engine, the context-pressure framework
   including the M5 bands and the in-core recovery floor, the §7.2 lens schema,
   Monitors M1–M12, Standing Principles, filename conventions, the atomic-prompt
   template, the operator-hint catalog, the engagement-closure gate, and the
   phase → bundle manifest). Phase-scoped mechanics (Setup, currency, continuity,
   corpus-access) are on-demand bundles — see step 5.
2. **Run the SP-13 substrate self-check** (Standing Principle SP-13, in the core's
   section 10.1.3): declare your model identity and confirm you are **Claude, Opus-class /
   flagship tier** (a capability floor — version-agnostic, latest by default). Halt
   and ask the operator on mismatch or cannot-determine.
3. **Run M1 (Missing Inputs)** and **M2 (Version Drift)**: verify the canonical
   attachments are present (Master, subject brief, and a Prompt Strategy if separate)
   and that the Master version matches what the last *What's next* predicted. Halt at
   HIGH severity on a missing required artifact or a version mismatch.
4. **Proceed per the Master's *What's next* artifact**, or per the operator's
   declared next action.
5. **Load the phase bundle for the role you occupy.** The core is lean; phase-,
   seam-, and condition-scoped mechanics are fetched on demand per the core's
   **phase → bundle manifest** (section 3.7.6). Run the visible self-check and
   fetch:
   - **Setup / P0** (no Master yet, or the operator initiates an engagement) →
     `reference/setup.md` (probes, three-layer readiness, Setup-artifact procedures).
   - **Update session / the session-open currency check** → `reference/currency.md`.
   - **Resume with a missing or abnormal handoff, or M5 band 🟠/🔴** →
     `reference/continuity.md` (the in-core recovery floor stays resident; the full
     migration / recovery procedure is in the bundle).
   - **A pass classified corpus-access** → `reference/corpus-access.md`.
   Each gutted area carries a fail-loud in-core stub — operating without the
   required bundle is detectable, not a silent gap.

## On-demand bundles — fetch only when the task needs them

Read these with the file tool at the moment a task calls for them; they are not
resident until you open them.

- **`lens/PRISM_lens_library.md`** — the Lens Library v0.15 (canonical catalog).
  Fetch at Setup and whenever Probe 1 grades the strategy against lenses.
- **`reference/templates.md`** — paste-ready Setup and dispatch blocks (Envelope,
  Self-check, Output, Decision brief, Stakeholder register, Claim inventory,
  Jurisdiction map, Dispatch register). Fetch when producing one of these artifacts.
- **`reference/setup.md`** — the Setup-phase mechanics: three-layer readiness, the
  seven probes (P1–P7), Setup-artifact procedures, strategy stability, onboarding,
  Library-reference-at-Setup, the Scope-Integrity Test, specialist-pass promotion,
  and the Claude-Project-as-Setup recommendation. Fetch at a Setup session / the P0
  boundary.
- **`reference/currency.md`** — point-refresh, the Update session, and the
  session-open currency check. Fetch for an Update session or when the
  currency-check-at-open fires.
- **`reference/continuity.md`** — the migration handoff format, failsafe recovery,
  defensive migration at natural seams, and cold-open missing-handoff recovery.
  Fetch at a resume / context-seam, or when M5 reads 🟠/🔴.
- **`reference/corpus-access.md`** — the corpus-access dispatch (the
  investigation-posture Envelope for a targeted external-corpus lookup). Fetch when
  the dispatch-builder classifies a pass as corpus-access.
- **`reference/modes-and-surfaces.md`** — the Cowork capability surface and the
  `repo_backed` persistence mechanics. Fetch when a non-default orchestration surface
  or persistence value is in play.
- **`reference/lanes-ui.md`** — the lanes / roles model, the PRISM Desk and PRISM
  Meta standing lanes, the PRISM UI, and Setup onboarding. Fetch when lanes / Desk /
  UI / onboarding work is in front of you.
- **`reference/dispatch-conventions.md`** — the promoted dispatch convention set
  (§A–H), the promotion map, the canonical execution-paste model, and the
  digest-preimage pin. Fetch when building or converging a dispatch.
- **`reference/report-architecture.md`** — the comprehensive final report skeleton
  + craft conventions, the interactive workbook cockpit pattern, the presentation
  house-style, and the reconcile-at-close checklist. Fetch when building or closing
  an engagement deliverable.
- **`reference/external-share.md`** — one-repo-per-engagement, the de-coded share
  archive, share modes, the image-redaction procedure, and the
  read-the-repo-not-the-mirror canonical-source block. Fetch when preparing an
  external handoff.
- **`reference/provenance.md`** — spec→v2 source mapping, the decision-tag index, and
  the v1.x→v2 surface drift. Fetch when tracing a decision's rationale or origin.
- **`reference/glossary.md`** — the glossary. Fetch on an unfamiliar term.
- **`reference/worked-example.md`** — a worked example flow and the empirical
  calibration items. Fetch to see constructs flow in a real audit.
- **`reference/mobile-operator-guide.md`** — the mobile-operator survival guide.
- **`reference/vendor-parsing.md`** — vendor parsing observations.
- **`reference/parked-design-ideas.md`** — parked v2 design ideas (reference only).

## Operating discipline

- Treat the core as authoritative. When the operator's request and the framework
  conflict, surface the conflict and ask — do not silently override the framework.
- Honour Standing Principles persistently. SP-9 in particular: silence is never
  consent. SP-1: never silently regenerate canonical artifacts.
- Write the Master and *What's next* at every orchestration turn-close, regardless of
  context band.
- Emit operator hints only when a cue applies to the specific dispatch — routine
  turns carry no hints.

## What this Skill does NOT do

- Does not regenerate a missing Master from memory — it runs the SP-1 /
  missing-handoff recovery protocol.
- Does not silently substitute v1.10.4 mechanics — v2 supersedes v1.x; v1.10.4
  projects stay on v1.10.4.
- Does not bypass operator ratification at the P0→P1 boundary.
- Does not auto-retry a failed dispatch — it surfaces re-dispatch as a candidate and
  the operator decides.
