---
description: How to use PRISM — a 30-second orientation and the one action to begin.
argument-hint: "[topic, optional]"
disable-model-invocation: true
---

Answer the operator's "how do I use PRISM / where do I start" question with a
**30-second orientation** — never a framework dump, never the full Setup entry.
This is the intended front door (the core's front-door behavior). Render the
four lines below, then offer to begin:

**What PRISM is.** A structured, multi-session, multi-vendor LLM-orchestrated
audit and research framework. It keeps state, scope, evidence, dispatch,
convergence, and validation coherent across sessions and vendors.

**You don't need to read it all.** A lean always-loaded core pulls reference
bundles on demand — load the core, fetch a bundle only when the work needs it.

**The one action to begin.** `/prism-start [subject]`, or just say "Run a PRISM
audit (or brief) on [subject]." That activates PRISM and starts Setup.

**Pick the heaviness.** A **quick brief** (rigor kept, machinery dropped) or a
**full audit** (the complete probe → dispatch → converge → close lifecycle). You
can start light and graduate to the full machinery later.

Then **offer to begin**: ask for the subject and hand off to `/prism-start` — do
not duplicate Setup here.

**If a topic argument is supplied** ($ARGUMENTS), point to the matching surface
instead of rendering the full orientation:

- *install / start / setup* → `/prism-start [subject]` (begins Setup, probes P1–P7).
- *resume / next / where was I* → `/prism-whats-next` (the PRISM Desk — resume + next action).
- *converge / returns / a dispatch came back* → `/prism-converge` (fold a return back in).
- *status / trajectory* → `/prism-status` (the engagement STATE view).
- *close / finish* → `/prism-close` (the engagement-closure gate).
- *methodology / meta* → `/prism-meta` (the methodology lane).

This command renders orientation only; it changes no framework mechanic and never
dumps the framework. Once the operator names a subject, `/prism-start` does the
real work.
