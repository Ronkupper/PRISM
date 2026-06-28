---
description: Resume the PRISM Meta lane (methodology / contributor work) — pull canonical repo state, adopt the session number, drain the meta inbox, and continue from the meta resume-pointer.
argument-hint: [meta pointer or focus, optional]
disable-model-invocation: true
---

Resume the **PRISM Meta** lane (the methodology lane — reflection, synthesis,
worksheet-building) from its continuous repo state.

Optional meta pointer or focus note (may be empty):

$ARGUMENTS

Then proceed:

1. **Pull canonical repo state.** The Meta lane is `repo_backed` — work from a
   fresh clone or `pull --rebase` of the live tail, never a stale checkout
   (commit-only-your-own-files; see `PRISM_core.md` §3.7.3). If the repo is not
   reachable, degrade to the pointer/handoff the operator supplies above.
2. **Load the framework** if it is not already active: read `PRISM_core.md`
   (naming PRISM also auto-triggers the `prism` Skill, which loads the same
   core).
3. **Adopt the session identity.** Read the meta resume-pointer (the latest
   meta handoff / meta *What's next*) and adopt the `Meta-<N>` number it
   assigns — do not self-grab a number. Announce it ("Meta-N, resuming from
   ML-…").
4. **Drain the meta inbox.** Read `OPEN_ITEMS_meta.md`; fold each non-terminal
   `cross-lane` / open item into the meta-log (promote any candidate-ML to a
   real `ML-N` from the live tail), then append a `drained` disposition line.
   Draining is append-only — never edit a prior item in place.
5. **Run the SP-13 substrate self-check** and emit your **M5 self-band** (this
   standing session's own context band, read against `Meta-N`). Hand off
   proactively at a seam if your self-band warrants.
6. **Proceed** from the meta pointer (or the focus above, weighed against it);
   honor lane boundaries — append to the meta-log and update the meta pointer;
   route object-lane items to the object lane's inbox rather than acting on
   them here.

This command is a Claude-Skill convenience for entering the Meta lane; it
changes no framework mechanic. It is the **contributor / methodology** command —
the sibling of the engagement commands (`/prism-start`, `/prism-whats-next`,
`/prism-converge`, `/prism-status`, `/prism-close`), serving the lane that
develops the methodology itself rather than running an audit. The plain-language
form ("resume the PRISM meta lane") is equivalent and is the portable form on
every other vendor.
