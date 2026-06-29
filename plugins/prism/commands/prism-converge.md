---
description: Converge dispatch returns into the Master — transport-integrity check (Dispatch ID), Layer-1 absorption + reconciliation, write the convergence delta and refresh What's next.
argument-hint: "[returns file or paste, optional]"
disable-model-invocation: true
---

Converge the returns from a dispatched pass back into the **PRISM** Master — the
**return leg** of the dispatch round-trip (the dispatch-consumer role).

The returns to absorb (a pasted vendor output, a file path, or empty to use what
is attached / in the project):

$ARGUMENTS

Then proceed:

1. **Load the framework** if it is not already active: read `PRISM_core.md`
   (naming PRISM also auto-triggers the `prism` Skill, which loads the same
   core). Fetch `reference/dispatch-conventions.md` — the convergence-side
   bundle.
2. **Locate the Master and the Dispatch register.** Identify *which* dispatch
   these returns answer; if it is ambiguous or no register entry matches, surface
   that and ask rather than guessing.
3. **Run the transport-integrity check (Step 0) before absorbing anything.**
   Confirm the `━━━ END PRISM DISPATCHED PASTE — <Dispatch ID> ━━━` sentinel is
   present and that its **Dispatch ID** matches the register entry. **Halt** on a
   missing sentinel, a Dispatch-ID mismatch, or a truncated return — a
   mis-pasted or wrong-pass return must never be silently absorbed.
4. **Absorb and reconcile (Layer-1).** Fold the returns into the Master's
   findings with provenance; run the convergence Monitors that bear — **M8**
   (Stale Source), **M9** (Convergence Type Drift), **M10** (Rerun) — and surface
   any **M7** (Source Conflict) rather than silently resolving it.
5. **Write canonical state.** Append the **convergence delta** to the Master,
   mark the dispatch *returned* in the register, and **rewrite *What's next*** so
   the next session resumes from the updated plan.

If the returns look incomplete, contaminated, or off-pass, stop and surface it —
do not absorb partial or suspect output into the Master.

This command is a Claude-Skill convenience for the convergence return-leg; it
changes no framework mechanic. Saying "converge these returns" in plain language
is equivalent, and is the portable form on every other vendor. It is the return
sibling of `/prism-whats-next` (which stages the *outgoing* dispatch).
