<!-- PRISM v2.20.1 Skill bundle (on-demand reference). Glossary (Appendix A). Reference.
     Generated from the assembled PRISM.md — edit PRISM.md, not this. -->

## Appendix A — Glossary
<a id="appendix-glossary"></a>

Combines DD Appendix A and Spec Appendix A. Definitions live here;
mechanics live in the cross-referenced sections.

| Term | Definition |
|---|---|
| **Adversarial Scope Probe** | Setup-time probe (§{probe.P2}). Hunts silent omissions in draft strategy. Library-driven; multi-vendor recommended. §{section.probe-2-adversarial-scope-iterates}. |
| **Anchor disposition** | Currency state per `rubric_anchor:` entry. States: `fresh`, `stale-refresh`, `stale-accumulating`. §{section.currency-maintenance-point-refresh}. |
| **Atomic prompt template** | Template that wraps the triple contract around a prompt body. The unit operators paste into execution sessions. §{section.atomic-prompt-template-v2-form}. |
| **Band** | M5's output. Four states: 🟢 Comfortable, 🟡 Getting warm, 🟠 Curate now, 🔴 Migrate. §{section.defensive-migration-at-natural-seams}. |
| **Bump atomicity** | The mechanic that ties Master version increments to defined triggers (phase transitions, convergence rounds, probe iterations, schema changes). §{section.filename-conventions-and-bump-atomicity}. |
| **Claim Conflict** | M7's surface — two findings with incompatible claims on the same surface. v1.x called this Assumption Conflict. §{section.m7-claim-conflict}. |
| **Claim inventory** | Setup artifact. Table of claims the audit must adjudicate, with audit-pass mapping. §{section.claim-inventory}. |
| **Continuous-curation** | Per-turn-close curation observation (band ≥ 🟡) or directive (band ≥ 🟠) in *What's next*. §{section.continuous-curation-posture}. |
| **Continuous-state mechanic** | Master + *What's next* written at every orchestration turn-close, regardless of band state. §{section.failsafe-recovery-continuous-state-mechanics}. |
| **Convergence delta** | Vendor Triangulation output document for an `equivalence` dispatch. §{section.convergence-delta-document}. |
| **Decision brief** | Setup artifact. Captures the decision under test, decision-maker, commissioner positioning, deadline, cost-of-error, falsifiers. §{section.decision-brief}. |
| **Decision Framing Probe** | Setup-time probe (§{probe.P3}). Produces Decision brief + Stakeholder register. §{section.probe-3-decision-framing-once}. |
| **Delta finalization** | When all expected vendor returns are in for an `equivalence` dispatch and Vendor Triangulation closes the convergence delta. §{section.vendor-triangulation}. |
| **Dispatch ID** | Envelope/Output field: a unique per-dispatch-instance identifier, paired with the Prompt digest and copied through, that reconciles a return to the exact dispatch that produced it. Distinct from Prompt ID (which names the pass). §{section.recommended-vs-executed-reconciliation}. |
| **Dispatch lifecycle** | The bounded five-stage dispatch round-trip — build → dispatch → execute → return/converge → reconcile — the dispatch-scoped sibling of the engagement lifecycle; subsumes the late-bound build, the operator/return cards, and the failure leg by reference. §{section.dispatch-lifecycle}. |
| **Dispatch rationale** | Envelope field carrying one positive-framing line per dispatch variant component. §{section.rationale-discipline-per-dispatch-variant}. |
| **Dispatch register** | Master section tracking recommended-vs-executed state per prompt. §{section.master-tracking-dispatch-register}. |
| **Dispatch shape** | Envelope field carrying the dispatch structural shape: `equivalence`, `split`, or `limitation-named`. §{section.single-envelope-with-spectrum-shape}. |
| **Domain Reconnaissance Probe** | Setup-time probe (§{probe.P6}). Surveys domain practice + authoritative-source detection + Jurisdiction map. §{section.probe-6-domain-reconnaissance-iterates-early}. |
| **Engagement closure** | The symmetric gate *out* of an engagement — a three-layer close sweep (object / lane-meta / operator) mirroring three-layer readiness; home of the orphan-sweep, reconcile-at-close, and deliverable polish. §{section.engagement-closure}. |
| **Engagement report** | The comprehensive final report — the engagement's deliverable of record, reflecting all the work, verdict-first and executive-scannable; a tight body + curated appendices. §{appendix.report-architecture}. |
| **Engagement workbook** | An interactive, operator-drivable cockpit companion to the report, delivered when the decision has a quantitative core: editable cells drive the decision gate live. §{appendix.report-architecture}. |
| **Envelope** | The first block of the triple contract — inbound vendor instructions including dispatch metadata, attachments, and operator hints (the PRISM PROMPT INTEGRITY transport anchor renders above it but is not a contract block, §{section.transport-integrity-bracket}). §{section.prism-execution-envelope}. |
| **`equivalence` dispatch** | Same prompt body to N vendors; outputs comparable; triggers Vendor Triangulation at N≥2. §{section.single-envelope-with-spectrum-shape}. |
| **Execution session** | Vendor session running a single dispatched prompt. Framework not attached; loaded artifacts limited to Envelope's `Attachments:` field. §{section.two-session-types}. |
| **Falsifier** | A finding that, if observed, would refute the audit's thesis. Captured in the Decision brief. §{section.probe-5-falsifier-once}, §{section.decision-brief}. |
| **`fires-covered` / `fires-uncovered` / `doesn't-fire` / `fires-maybe`** | Probe 1's tri-state-with-maybe disposition per Lens. §{section.probe-1-coverage-grading-iterates}. |
| **Follow-up** | An additive strategy revision when a *sound* prior run wants a new or expanded dimension: route the scope-addition to the next consuming pass or a new pass — do not augment-and-re-run the completed producer. Distinct from an M10 re-run (which redoes a *defective* run). §{section.strategy-stability}. |
| **Jurisdiction map** | Setup artifact. Per-jurisdiction listing of triggered regulatory regimes and their materiality. §{section.jurisdiction-map}. |
| **Lane** | A unit of parallel work — {a resume pointer, an append-only log, an inbox, one concern}. Object lane (the engagement) and meta lane (methodology). §{section.lanes}. |
| **Layer 1** | Per-prompt convergence — orchestration absorbs returned findings into the Master. Monitors M6/M7/M8/M12 fire here. |
| **Layer 2** | Cold synthesis across all Layer-1 findings to produce the audit's external deliverable. M9 fires here. M11 surfaces readiness. |
| **Lens Library** | The reference catalog of audit-scope lenses. Universal (5) + Domain (22). v0.16 release pinned at `prism-lens-v0.16`. §{section.library-integration}. |
| **`limitation-named` dispatch** | Single-vendor dispatch with explicit `Not chosen:` rationale. §{section.single-envelope-with-spectrum-shape}. |
| **Master** | The single canonical project state file. Updated at every orchestration turn-close. §{section.the-master}. |
| **Migration handoff** | Defined artifact produced at 🔴 (mandatory) or 🟠 (optional) for fresh-session continuity. §{section.migration-handoff}. |
| **Monitor** | Orchestration-side check that fires at a defined lifecycle slot. M1–M12 specified in §{section.monitor-specifications}. |
| **Natural seam** | A transition point where migration is low-cost. Defined set: convergence round complete, phase boundary, deliverable shipped, setup iteration complete. §{section.continuous-curation-posture}. |
| **Orchestration session** | Claude session with the framework attached. Master state, Monitor fires, Setup probes, convergence reasoning all live here. §{section.two-session-types}. |
| **OPEN_ITEMS inbox** | A lane's append-only, tier-1 cross-lane inbox; any session appends, the lane owner drains at its turn. Closes the pointer-clobber class. §{section.cross-lane-inbox}. |
| **Output** | The third block of the triple contract — outbound finding signature with executed-state metadata and operator-next instructions. §{section.prism-execution-output}. |
| **Point refresh** | Per-project, in-Setup currency check on Library `rubric_anchor:` entries. §{section.currency-maintenance-point-refresh}. |
| **Pre-mortem** | Setup-time probe (§{probe.P4}). Imagines execution complete; surfaces failure modes. §{section.probe-4-pre-mortem-iterates}. |
| **PRISM** | Prompts · Research · Iteration · Synthesis · Master. The framework. |
| **PRISM Desk** | The object lane's standing Planner/Steward lane — owns *What's next* and the drain, renders the PRISM UI; re-opened per round or periodically. §{section.prism-desk-and-prism-meta}. |
| **PRISM Meta** | The standing methodology lane (reflection / synthesis / worksheet-building), opened periodically. §{section.prism-desk-and-prism-meta}. |
| **PRISM UI** | The operator-facing View+Controller over the repo Model, rendered by the Desk; STATE / HEALTH / ACTION surfaces. §{section.prism-ui}. |
| **Probe** | Setup-time grading construct against the draft Prompt Strategy. Seven probes specified: P1–P7. §{section.the-seven-probes}. |
| **Prompt Strategy** | The plan of dispatched prompts produced by Setup. Lives in the Master. Iterates in P0; ratifies at P0→P1; revisable at convergence (§{section.strategy-stability}). |
| **Quick mode** | `SETUP_QUICKMODE` — a first-class light Setup shape (one ephemeral session, clean-context sub-agent fan-out) keeping the cheap rigor; graduates to a full engagement without losing work. §{section.setup-onboarding-and-mode-selection}. |
| **Reconcile-at-close** | A closure-gate codification sweep: at engagement close, diff the finished deliverable against its reference architecture in one pass and codify every craft element not yet codified (closes the applied≠codified pattern). §{section.engagement-closure}. |
| **Result Completeness Check** | M12. Convergence-time monitor detecting within-domain coverage gaps in returned findings. §{section.m12-result-completeness-check}. |
| **Saturation** | Two consecutive iterations produce no material change to coverage or strategy. §{section.three-layer-readiness}. |
| **Role × context-tier** | The flexible matrix a session occupies — role (Setup / Desk / dispatch-builder / -consumer / execution / convergence / validation) × tier (orchestration vs execution). §{section.roles-context-tier}. |
| **Self-check** | The middle block of the triple contract — the transport-integrity input-gate (step 0, §{section.transport-integrity-bracket}), substrate verification per §{principle.SP-13}, plus the output-side gates: the §{principle.SP-16} uninvited-frame audit (step 5) and the §{principle.SP-18} recompute gate (step 6). §{section.prism-execution-self-check}. |
| **Setup artifacts** | Four instance-specific artifacts populated during Setup: Decision brief, Stakeholder register, Claim inventory, Jurisdiction map. §{section.setup-artifacts}. |
| **`split` dispatch** | Prompt split into vendor-specific sub-prompts; synthesis happens orchestration-side. §{section.single-envelope-with-spectrum-shape}. |
| **Setup onboarding** | `SETUP_ONBOARDING` — the Setup-as-scaffolder flow that generates the per-engagement SI from a template and emits project-create / install cards; the two-project model. §{section.setup-onboarding-and-mode-selection}. |
| **Share archive** | The default external-share artifact — a self-contained, de-coded, `Index.html`-navigated archive of the engagement's work-product, redacted for share (the canonical repo untouched). §{appendix.external-share}. |
| **Stakeholder register** | Setup artifact. Per-role listing of stake, motivation, positioning/angle, decision power, and communication channel; the operator/commissioner is a mandatory row. §{section.stakeholder-register}. |
| **Standing Principle (SP)** | Persistent posture; not a discrete fire. See the full roster in §{section.standing-principles} and §{section.v1-x-standing-principles-carryforward-catalog}. |
| **Status-glyph legend** | The report's published ● / ◐ / ○ visual vocabulary for capability / coverage / severity, with Confidence and Verification as separate axes; introduced on first use and decoded in the glossary. §{appendix.report-architecture}. |
| **Strategy stability** | At P0→P1 ratification, strategy is "presumed stable, revisable at convergence." §{section.strategy-stability}. |
| **Substitution** | The filename-resolved executed vendor/config (§{principle.SP-14}) differs from the Envelope's recommended vendor/config; the Output `Vendor` field is advisory self-ID (§{section.recommended-vs-executed-reconciliation}). Absorbed at convergence; no automatic re-dispatch. §{section.substitution-absorption}. |
| **Three-layer readiness** | The P0→P1 boundary clears when Structural completeness, Library coverage saturation, and Operator ratification all clear. §{section.three-layer-readiness}. |
| **Transport-integrity bracket** | A top-of-paste PRISM PROMPT INTEGRITY anchor + a terminal END PRISM DISPATCHED PASTE sentinel wrapping any dispatched paste; Self-check Step 0 validates completeness by presence + Dispatch-ID match, so a truncated mid-stream copy is caught before work. Transport framing, not a contract block; excluded from the digest preimage. §{section.transport-integrity-bracket}. |
| **Triple contract** | Envelope (inbound) + Self-check (substrate verify) + Output (outbound). The load-bearing interface between sessions; the dispatched paste wraps it in a transport-integrity bracket (§{section.transport-integrity-bracket}), which is not a contract member. §{section.the-triple-contract}. |
| **Update session** | Standalone, rare, operator-gated session that maintains Library currency. §{section.currency-maintenance-update-session}. |
| **User Voice Probe** | Setup-time probe (§{probe.P7}). Imports real end-user signal. §{section.probe-7-user-voice-iterates-early}. |
| **Vendor config** | Envelope/Output field carrying vendor-specific configuration flags. §{section.prism-execution-envelope}. |
| **Vendor Selection** | Live web-search currency check at every dispatch; produces Envelope. §{section.vendor-selection-at-dispatch}. |
| **Vendor Triangulation** | Layer-1 convergence pass that fires at N≥2 for `equivalence` dispatches. §{section.vendor-triangulation}. |
| ***What's next*** | Per-turn-close artifact. The operator's single source of "what to do next." §{section.whats-next}. |

---
