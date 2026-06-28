<!-- PRISM v2.20.1 Skill bundle (on-demand reference). Dispatch conventions reference — the promoted §A–H convention set, the promotion map, the canonical execution-paste model, and the digest-preimage pin (Appendix J). Fetch when building or converging a dispatch.
     Generated from the assembled PRISM.md — edit PRISM.md, not this. -->

## Appendix J — Dispatch conventions (reference)
<a id="appendix-dispatch-conventions"></a>

Reference-grade detail behind the dispatch lifecycle
(§{section.dispatch-lifecycle}). The lifecycle's *rules* live in the core
sections; this appendix is the battle-tested recipe set the stages draw on,
plus the **promotion map** that records where each convention's rule landed —
so a working, field-proven convention set does not orphan as the framework
absorbs it. Entries are practice distilled from live dispatch rounds; consult
it when building or converging a dispatch.

### J.1 Promotion map — convention → framework home

Each item is **REFERENCE** (already core — cite it), **PROMOTE** (battle-tested
local practice lifted into the framework), or **PROMOTE-OR-DECIDE** (a
divergence sanctioned as an option or kept documented). Where a convention's
local practice and core diverged, the verdict follows the dispatch-lifecycle
source.

| Conv | Item | Disposition → framework home |
|---|---|---|
| A.1 | Single-arm self-contained paste (vendor unaware it is 1 of N) | PROMOTE → §{section.atomic-prompt-self-containment} — strip the orchestration machinery; arm-count is orchestration-side |
| A.2 | Inline small + available; attach large / not-yet-produced | PROMOTE → §{section.atomic-prompt-self-containment} composition guidance |
| A.3 | 3-way pre-flight: INPUT halts · SUBSTRATE declares · ANALYSIS proceeds | REFERENCE/PROMOTE → the Self-check (§{section.prism-execution-self-check}); the completeness limb of INPUT is operationalized as the **Step 0** transport-integrity check (§{section.transport-integrity-bracket}); "only INPUT may halt" preserved |
| A.3a | Transport-integrity bracket — truncation guard (top anchor + terminal sentinel) | PROMOTE → §{section.transport-integrity-bracket} (Self-check Step 0; template §{appendix.prism-prompt-integrity}) |
| A.4 | Lean delimited output signature beats prose | REFERENCE → the delimited Output signature (§{section.prism-execution-output}) is already the standard (empirical: ━━━ got 4/4 vendor adherence, prose 2/5) |
| A.5 | Per-seat mode + live currency at dispatch | REFERENCE → §{section.vendor-selection-at-dispatch} |
| A.6 | No bare PRISM shorthand in the paste | REFERENCE → §{section.atomic-prompt-self-containment} |
| A.7 | Per-vendor download / export recipes | PROMOTE → §{appendix.vendor-parsing-observations} |
| B.8 / B.8a | Converge in a dedicated clean session / clean-context sub-agent | REFERENCE → §{section.roles-context-tier} (seam-③); converger only, never a triangulation seat (§{principle.SP-15}) |
| B.9 | Adversarial review = Independent Validation Dispatch | REFERENCE → §{section.independent-validation-dispatch}; sharpened to "distinct from all N producers" (§{principle.SP-15}) |
| C.11 | Plain words to the operator | REFERENCE → §{principle.SP-17} |
| C.12 | Repo / write discipline (rebase-on-tail, commit-only-own, identity-before-commit) | engagement SI + the cross-lane inbox (§{section.cross-lane-inbox}); the repo mechanics are maintainer-protocol, not framework body |
| D.13–15 | Paste-as-own-file · fixed-schema operator card · in-paste guardrails | PROMOTE → the Stage-2 dispatch card (§{appendix.outbound-dispatch-card}) within the dispatch lifecycle (§{section.dispatch-lifecycle}) |
| E | Canonical execution-paste model (bookended ━━━ blocks) | REFERENCE → the reference paste shape, an instantiation of the atomic template (§{section.template-shape}); J.2 below |
| F.16–19 | Recon: probe-spine + one explore-agent; retrieved-vs-inferred; recon output discipline; agentic-browser driver class | PROMOTE → §{section.prompt-body-convergence-provisions} (finding basis) + §{section.vendor-selection-at-dispatch} (driver class) + §{appendix.vendor-parsing-observations} |
| G.20–22 | Match dispatch mode to retrieval shape; capture-then-attach; capability-null ≠ substantive-null | PROMOTE → §{section.vendor-selection-at-dispatch} retrieval-shape step |
| H.23–25 | Passive pre-fill of self-report; provenance tags; passive-only ethics | PROMOTE → §{section.corpus-access-dispatch} (passive pre-fill) + §{appendix.vendor-parsing-observations} (template) |

### J.2 Canonical execution-paste model (reference shape)

The reference shape for the execution unit a Stage-3 dispatch sends: **two lean
delimited `━━━` blocks bookending the task body**, all inside one fenced block,
themselves wrapped by the transport-integrity bracket
(§{section.transport-integrity-bracket}) — the `PRISM PROMPT INTEGRITY` anchor
above and the terminal sentinel below, transport framing rather than contract
blocks — with the operator dispatch card (§{appendix.outbound-dispatch-card})
rendered above the whole paste. It is an instantiation of the atomic template
(§{section.template-shape}), not a replacement: it restores the delimited
*inbound* structure (the Self-check, §{section.prism-execution-self-check}) that
a prose pre-flight loses, and keeps the delimited *outbound* signature (the
Output, §{section.prism-execution-output}).

- **Inbound — Self-check (§{appendix.prism-execution-self-check}).** Carries the
  3-way pre-flight: **INPUT** check is the *only* place the vendor may halt —
  completeness is the terminal-sentinel presence + Dispatch-ID match (Self-check
  Step 0, §{section.transport-integrity-bracket}); are named files present +
  readable?; **SUBSTRATE**
  declares mode + best-effort model and proceeds; **ANALYSIS** proceeds on
  defaults, recording any under "could not verify," never asking the operator.
- **Body.** Self-contained context (inline small + available priors, attach
  large / not-yet-produced), task, method (recompute — do not trust —
  arithmetic), output structure (the finding shape,
  §{section.prompt-body-convergence-provisions}), success criteria.
- **Outbound — Output signature (§{appendix.prism-execution-output}).** The
  vendor wraps its findings in the `━━━ PRISM EXECUTION OUTPUT ━━━` block and
  copies the `Dispatch ID` and `Prompt digest`/`Reference` lines verbatim.

Use `━━━` heavy-line delimiters, never triple-backtick fences, for the paste's
internal blocks — they are fence-safe, so the whole paste survives inside one
outer fenced block when rendered to the operator.

### J.3 Digest preimage — pin for re-stage reproducibility

The copy-through digest (§{section.prism-execution-output}) is only reproducible
on a **re-stage** if its preimage is pinned exactly: the byte scope is the
content between the paste fences, with the Envelope's (and Output's) `Reference:`
/ `Prompt digest:` line set to the sentinel `sha256:PENDING`, the
transport-integrity bracket (§{section.transport-integrity-bracket}) — the
`PRISM PROMPT INTEGRITY` anchor block in full and the terminal
`━━━ END PRISM DISPATCHED PASTE` sentinel — **excluded** from the byte scope as
transport framing, and **no trailing-newline normalization**. (The bracket is
*excluded*, not normalized — its own `Prompt digest:` line is display-only and
never enters the preimage; this differs from the `Reference:` line, which is
*included-with-value-blanked*.)
An unpinned preimage stays deterministic and consistent *within* a session, but
a later session that wants to re-stage the same dispatch and preserve the
original digest cannot reproduce it — the field catch behind this rule. The
digest pairs with the **Dispatch ID**
(§{section.recommended-vs-executed-reconciliation}): the digest verifies body
integrity, the Dispatch ID identifies the dispatch instance; together with the
operator-set filename they are the reconciliation triple.
