---
description: Close a PRISM engagement — run the Engagement-closure gate (three-layer close sweep) and produce the deliverables: the plain-language report and, when the decision turns on numbers, the interactive workbook.
argument-hint: [master file or focus, optional]
disable-model-invocation: true
---

Close the active **PRISM** engagement — run the **Engagement-closure gate** and
hand over clean deliverables.

Optional Master pointer or closing focus (may be empty):

$ARGUMENTS

Then proceed:

1. **Locate the Master.** Use an attached Master, the one in this project/repo,
   or the pointer above. If none can be found, run the **SP-1 / missing-handoff
   recovery** protocol in `PRISM_core.md` — do **not** regenerate the Master from
   memory.
2. **Load the framework** if it is not already active: read `PRISM_core.md` (the
   Engagement-closure gate, §6.7, lives in the core).
3. **Run the closure gate — the three-layer close sweep.** Verify everything
   dispatched has **returned and converged**, open Monitors are cleared, and
   *What's next* holds no pending work. Run the reconcile-at-close checklist.
   **If the sweep finds unfinished work, halt and surface it** — do not close
   over a gap.
4. **Produce the deliverables.** Fetch `reference/report-architecture.md` and
   build the comprehensive **plain-language report** (the report skeleton + craft
   conventions); when the decision turns on numbers, add the **interactive
   workbook** cockpit so the audience can drive the model; apply the presentation
   house-style. For an external handoff, follow `reference/external-share.md`.
5. **Record closure** in the Master and write a terminal *What's next* that marks
   the engagement closed.

This command is a Claude-Skill convenience for the closure phase; it changes no
framework mechanic. Saying "close this engagement" in plain language is
equivalent, and is the portable form on every other vendor.
