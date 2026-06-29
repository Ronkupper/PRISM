---
description: Start a PRISM audit or research engagement for a subject — activates PRISM and begins Setup (probes P1–P7). The lifecycle entry point.
argument-hint: "[subject]"
disable-model-invocation: true
---

Activate **PRISM** and begin a new engagement for the following subject — the
entry point of the **Setup → rounds → Closure** lifecycle:

$ARGUMENTS

Then proceed:

1. **Load the framework.** Read the PRISM Skill's core (`PRISM_core.md`) in full —
   the operating model and architecture, the Execution Envelope / Self-check /
   Output triple contract, Setup mechanics, Monitors M1–M12, and Standing
   Principles. (Naming PRISM also triggers the `prism` Skill, which loads the same
   core; either path is fine.)
2. **Run the SP-13 substrate self-check.** Declare your model identity and confirm
   you are Claude, Opus-class / flagship tier (a capability floor — version-agnostic,
   latest by default). Halt and ask the operator on mismatch or cannot-determine.
3. **Run M1 (Missing Inputs) and M2 (Version Drift)** against any attached Master,
   Lens Library, or Prompt Strategy. Halt at HIGH severity on a missing required
   artifact or a version mismatch.
4. **Begin Setup** — the seven probes P1–P7 — for the subject above: grade the
   draft Prompt Strategy against the Lens Library toward three-layer readiness at
   the P0→P1 boundary, then proceed per the *What's next* artifact.

If the subject above is empty, ask the operator for the audit or research subject
before starting Setup. If a Master for an existing engagement is attached, surface
this subject against its *What's next* and let the operator choose rather than
silently restarting Setup.

This command is a Claude-Skill convenience for invoking and seeding PRISM; it
changes no framework mechanic. The plain-language invocation ("Run a PRISM audit
on …") is equivalent and is the portable form on every other vendor. Once an
engagement is running, resume it with `/prism-whats-next`, fold returns back with
`/prism-converge`, view the trajectory with `/prism-status`, and finish with
`/prism-close`.
