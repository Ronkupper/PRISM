---
name: prism
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
   triple contract, the prompt-package engine, context-pressure framework, Setup
   mechanics, Library-integration mechanics, Monitors M1–M12, Standing Principles,
   filename conventions, the atomic-prompt template, the operator-hint catalog, and
   missing-handoff recovery).
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

## On-demand bundles — fetch only when the task needs them

Read these with the file tool at the moment a task calls for them; they are not
resident until you open them.

- **`lens/PRISM_lens_library.md`** — the Lens Library v0.12 (canonical catalog).
  Fetch at Setup and whenever Probe 1 grades the strategy against lenses.
- **`reference/templates.md`** — paste-ready Setup and dispatch blocks (Envelope,
  Self-check, Output, Decision brief, Stakeholder register, Claim inventory,
  Jurisdiction map, Dispatch register). Fetch when producing one of these artifacts.
- **`reference/modes-and-surfaces.md`** — the Cowork capability surface and the
  `repo_backed` persistence mechanics. Fetch when a non-default orchestration surface
  or persistence value is in play.
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
