<!-- PRISM v2.19.0 Skill bundle (on-demand reference). Lanes, roles, the PRISM UI, and Setup onboarding (Appendix I). Fetch when lanes / Desk / UI / onboarding work is in front of you.
     Generated from the assembled PRISM.md — edit PRISM.md, not this. -->

## Appendix I — Lanes, roles, PRISM UI, and Setup onboarding (reference)
<a id="appendix-lanes-roles-prism-ui"></a>

Reference-grade detail for the operating model
(§{section.lanes-roles-and-the-prism-ui}) and Setup onboarding
(§{section.setup-onboarding-and-mode-selection}). The rules are in those
sections; this appendix is the matrix, the UI rendering, the trajectory-view
reference, and the onboarding artifacts. In the Skill archive it is the
`reference/lanes-ui.md` bundle, fetched when lanes / Desk / UI / onboarding
work is in front of you.

### I.1 The role × context-tier matrix

Context-tier = PRISM-loaded *orchestration* vs clean *execution*. Role and
tier are independent axes — a convergence run is an orchestration-*class* role
run in a clean execution-*style* context.

| Role | Context-tier | Anchored to |
|---|---|---|
| Setup | orchestration | the seven probes (§{section.setup-mechanics}) |
| Planner/Steward (the PRISM Desk) | orchestration | the *What's next* pointer + the drain (§{section.cross-lane-inbox}) |
| Dispatch-builder | orchestration | Vendor Selection (§{section.vendor-selection-at-dispatch}) + the Envelope (§{section.prism-execution-envelope}) |
| Dispatch-consumer | orchestration | Layer-1 absorption + reconciliation + the Master write |
| Execution-run | execution | the self-contained dispatched prompt (§{section.two-session-types}); PRISM-unaware by design |
| Convergence-run | execution-*style*, orchestration-*class* | clean-session Vendor Triangulation (§{section.vendor-triangulation}) |
| Validation-run | execution | the Independent Validation Dispatch (§{section.independent-validation-dispatch}) — adversarial, deliverable-only, distinct-vendor |

The meta lane has its own roles (reflection / synthesis / worksheet-building).

### I.2 Isolation — inline, session, or sub-agent

A session that chooses to separate has three options: **inline** (when the
work is light), **a separate session** (for a durable handoff), or a
**clean-context sub-agent** (the default when the holding session is
contaminated — see §{section.roles-context-tier}). Sub-agent bounds: clean
context but same distribution (§{principle.SP-15}) — a converger or clean
reader, never a triangulation seat. Hand it return-paths + method only; it
reads returns from `outputs/` by path and writes back to `outputs/`; the
parent absorbs and writes canonical state.

### I.3 The PRISM UI — rendering detail

The three surfaces (STATE / HEALTH / ACTION) and the make-it-a-real-UI
discipline are in §{section.prism-ui}. Rendering specifics:

- **Consistency.** The visual language is stable round-to-round; mode is
  operator-selectable but the component schemas do not silently change between
  renders.
- **Colored status encoding** (operator-liked): complete · you-are-here ·
  pending · critical-path · decisive.
- **Code → real-name legend.** The view carries a legend translating pass
  codes (e.g. `A11`, `R1`, `T1`) to their real objectives, rendered from the
  live Master's Prompt Strategy and Dispatch register — not re-transcribed.

### I.4 The trajectory STATE view — two modes (operator-reviewed reference)

The STATE view has **two modes answering different questions**, shown **side
by side, each in its own form — not fused** into one diagram:

- **Dependency / critical-path map** (an "engagement map"): rounded-rectangle
  nodes top→bottom with explicit fork / join arrows; a dedicated critical-path
  + bottleneck callout; a status / role legend. Optimized to show
  **structure** — what gates what, what runs in parallel, where the bottleneck
  is. The decision-relevant view when the engagement is blocked on one external
  event.
- **Progress timeline**: a single vertical spine with one status dot per node
  (● complete · ◉ you are here · ○ pending), a nested sub-box for parallel
  legs, a dashed "not on this trajectory" aside. Optimized to show **sequence +
  status** — where am I, what's done. Cleaner at a glance; lower-information at
  a blocked / branching phase.

Operator inputs that shaped this: liked both renders and wants both (side by
side, not converged); liked the colored encoding; wants the code → name legend
on the view; wants the visual language stable round-to-round. The Builder owns
the final rendering; this records the reviewed inputs.

### I.5 Setup onboarding — the SI template and install cards

**The framework SI template** is a generic skeleton with native-construct
references + typed config slots, shipping with the SI version machinery baked
in (`SI version` + changelog). Filling it yields a complete lean SI with zero
boilerplate re-authoring.

- **Native-construct sections (one-line references):** persistence
  (`repo_backed`, §{section.repo-backed-mechanics}); resume protocol;
  commit-discipline + the cross-lane inbox (§{section.cross-lane-inbox}); lanes
  / roles / the Desk (§{section.lanes-roles-and-the-prism-ui}).
- **Per-subject slots (Setup fills):** subject + decision tracks; repo + work
  folder; surface registry (the two-project model on Cowork — orchestration +
  execution); credential location (PAT path) + redaction regime;
  engagement-specific standing directives, **embedded verbatim**.

**The project-create + install card** (one per surface; the operator-guide
schema, plain-language WHERE / WHAT / RESULT):

- **Create the project(s)** — two on Cowork (orchestration: SI installed,
  core-load enforced, hosts Desk + Meta; execution: SI-less, memory-off,
  organization-only, working folder separate from the orchestration mirror).
  Automatable vs guidance-only is surface-dependent — default guidance-only,
  automate where a surface allows.
- **Install the SI** — the full SI as a single wholesale-paste block ("Project
  instructions, not a chat; paste the WHOLE thing"); never a splice.
- **Drop the PAT** — guidance to place the credential in the per-surface
  location; guidance-only, never handled by the session.
- **Seed the repo** — the work-folder layout + first commit (or confirm the
  repo exists).
- **Re-issue on change** — any later SI change ships as a full replacement for
  wholesale paste on every surface; the resume-time version reconcile is the
  drift detector.

### I.6 Quick mode — the mini-Setup procedure

The shape and the kept / dropped split are in
§{section.setup-onboarding-and-mode-selection}. Concretely:

1. **Frame (≤ 2 lines):** audience + the decision this serves. If this cannot
   be stated, the task is under-specified — surface it, don't proceed on a
   guess (SP-9, §{principle.SP-9}).
2. **Lite lens pick:** name the handful of lenses that bear; note any
   deliberately out of scope (one line each). No coverage-saturation loop.
3. **Fan out** clean-context sub-agents per strand; assemble grounding facts.
4. **Apply the output gates** (SP-16 / SP-17 / SP-18) to the assembled
   deliverable.
5. **Deliver** one self-contained artifact (SP-20); no repo write-back. If it
   grows into a real engagement, graduate per
   §{section.setup-onboarding-and-mode-selection}.
