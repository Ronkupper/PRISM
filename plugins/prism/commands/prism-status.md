---
description: Render the PRISM engagement state from verified repo state — the dependency / critical-path map and the progress timeline, side by side, with the code→name legend.
argument-hint: [map | timeline | both, optional]
disable-model-invocation: true
---

Render the **PRISM** engagement's current state — the Desk's **STATE view**,
built from verified repo state, never from memory.

Optional view selector (`map`, `timeline`, or empty for both):

$ARGUMENTS

Then proceed:

1. **Load the framework** if it is not already active: read `PRISM_core.md`, then
   fetch `reference/lanes-ui.md` (the PRISM UI and trajectory-view reference).
2. **Re-sync canonical state (the HEALTH view).** Work from a fresh `pull --rebase`
   of the live tail; confirm HEAD matches the mirror and the *What's next* pointer
   is present. If the repo is unreachable, degrade to the attached Master and say so.
3. **Render the STATE view — two modes, side by side, each in its own form (not
   fused):**
   - a **dependency / critical-path map** — what gates what, what runs in
     parallel, where the bottleneck is, with the critical-path callout; and
   - a **progress timeline** — where am I, what's done (● complete · ◉ you are
     here · ○ pending).
   Use the stable visual language, the colored status encoding, and a **code → real-name
   legend** translating pass codes (`A11`, `R1`, …) to their objectives — rendered
   from the live Master's Prompt Strategy and Dispatch register, not re-transcribed.
4. **Close with the one next action** (the ACTION line) so the view hands off
   cleanly to `/prism-whats-next`.

This command is a Claude-Skill convenience for summoning the state view on demand;
it changes no framework mechanic. Asking "show the trajectory / where are we" in
plain language is equivalent, and is the portable form on every other vendor.
