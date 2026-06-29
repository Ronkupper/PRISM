---
description: Resume a PRISM engagement — the PRISM Desk. Re-sync from the repo, show where you are and the one next action, and stage the next dispatch as a paste-ready Envelope.
argument-hint: "[master file or focus, optional]"
disable-model-invocation: true
---

Resume the active **PRISM** engagement from its continuous state — this is the
**PRISM Desk**, your single pane of glass between sessions.

Optional Master pointer or focus note (may be empty):

$ARGUMENTS

Then proceed:

1. **Locate the Master.** Use an attached Master, the one in this project/repo
   (or repo-backed `What's next`), or the path/pointer above. If no Master can be
   found, run the **SP-1 / missing-handoff recovery** protocol in `PRISM_core.md` —
   do **not** regenerate the Master from memory.
2. **Load the framework** if it is not already active: read `PRISM_core.md` (naming
   PRISM also auto-triggers the `prism` Skill, which loads the same core).
3. **Run the SP-13 substrate self-check**, then **M1 (Missing Inputs)** and
   **M2 (Version Drift)** against the Master and its declared attachments. Halt at
   HIGH severity on a missing required artifact or a version mismatch.
4. **Read the Master's *What's next* artifact and proceed** from the predicted next
   action. If a focus was supplied above, weigh it against *What's next* and let the
   operator choose when they diverge rather than silently overriding the plan.
5. **Stage the next step as a card.** When the next action is a dispatch, render it
   as a **paste-ready Execution Envelope** (the ACTION surface) with its Dispatch ID;
   otherwise name the next move plainly. On request, render the **STATE view**
   (`/prism-status`) instead.
6. If *What's next* is missing or stale, surface that and ask the operator rather
   than guessing the next action.

This command is a Claude-Skill convenience for resuming PRISM; it changes no
framework mechanic. Asking "What's next?" in plain language is equivalent, and is
the portable form on every other vendor. Its siblings cover the rest of the loop:
`/prism-converge` (fold returns back), `/prism-status` (the trajectory view), and
`/prism-close` (finish the engagement).
