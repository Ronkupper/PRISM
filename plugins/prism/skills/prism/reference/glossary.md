<!-- PRISM v2.11.1 Skill bundle (on-demand reference). Glossary (Appendix A). Reference.
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
| **Decision brief** | Setup artifact. Captures the decision under test, decision-maker, deadline, cost-of-error, falsifiers. §{section.decision-brief}. |
| **Decision Framing Probe** | Setup-time probe (§{probe.P3}). Produces Decision brief + Stakeholder register. §{section.probe-3-decision-framing-once}. |
| **Delta finalization** | When all expected vendor returns are in for an `equivalence` dispatch and Vendor Triangulation closes the convergence delta. §{section.vendor-triangulation}. |
| **Dispatch rationale** | Envelope field carrying one positive-framing line per dispatch variant component. §{section.rationale-discipline-per-dispatch-variant}. |
| **Dispatch register** | Master section tracking recommended-vs-executed state per prompt. §{section.master-tracking-dispatch-register}. |
| **Dispatch shape** | Envelope field carrying the dispatch structural shape: `equivalence`, `split`, or `limitation-named`. §{section.single-envelope-with-spectrum-shape}. |
| **Domain Reconnaissance Probe** | Setup-time probe (§{probe.P6}). Surveys domain practice + authoritative-source detection + Jurisdiction map. §{section.probe-6-domain-reconnaissance-iterates-early}. |
| **Envelope** | The first block of the triple contract — inbound vendor instructions including dispatch metadata, attachments, and operator hints. §{section.prism-execution-envelope}. |
| **`equivalence` dispatch** | Same prompt body to N vendors; outputs comparable; triggers Vendor Triangulation at N≥2. §{section.single-envelope-with-spectrum-shape}. |
| **Execution session** | Vendor session running a single dispatched prompt. Framework not attached; loaded artifacts limited to Envelope's `Attachments:` field. §{section.two-session-types}. |
| **Falsifier** | A finding that, if observed, would refute the audit's thesis. Captured in the Decision brief. §{section.probe-5-falsifier-once}, §{section.decision-brief}. |
| **`fires-covered` / `fires-uncovered` / `doesn't-fire` / `fires-maybe`** | Probe 1's tri-state-with-maybe disposition per Lens. §{section.probe-1-coverage-grading-iterates}. |
| **Jurisdiction map** | Setup artifact. Per-jurisdiction listing of triggered regulatory regimes and their materiality. §{section.jurisdiction-map}. |
| **Layer 1** | Per-prompt convergence — orchestration absorbs returned findings into the Master. Monitors M6/M7/M8/M12 fire here. |
| **Layer 2** | Cold synthesis across all Layer-1 findings to produce the audit's external deliverable. M9 fires here. M11 surfaces readiness. |
| **Lens Library** | The reference catalog of audit-scope lenses. Universal (5) + Domain (18). v0.13 release pinned at `prism-lens-v0.13`. §{section.library-integration}. |
| **`limitation-named` dispatch** | Single-vendor dispatch with explicit `Not chosen:` rationale. §{section.single-envelope-with-spectrum-shape}. |
| **Master** | The single canonical project state file. Updated at every orchestration turn-close. §{section.the-master}. |
| **Migration handoff** | Defined artifact produced at 🔴 (mandatory) or 🟠 (optional) for fresh-session continuity. §{section.migration-handoff}. |
| **Monitor** | Orchestration-side check that fires at a defined lifecycle slot. M1–M12 specified in §{section.monitor-specifications}. |
| **Natural seam** | A transition point where migration is low-cost. Defined set: convergence round complete, phase boundary, deliverable shipped, setup iteration complete. §{section.continuous-curation-posture}. |
| **Orchestration session** | Claude session with the framework attached. Master state, Monitor fires, Setup probes, convergence reasoning all live here. §{section.two-session-types}. |
| **Output** | The third block of the triple contract — outbound finding signature with executed-state metadata and operator-next instructions. §{section.prism-execution-output}. |
| **Point refresh** | Per-project, in-Setup currency check on Library `rubric_anchor:` entries. §{section.currency-maintenance-point-refresh}. |
| **Pre-mortem** | Setup-time probe (§{probe.P4}). Imagines execution complete; surfaces failure modes. §{section.probe-4-pre-mortem-iterates}. |
| **PRISM** | Prompts · Research · Iteration · Synthesis · Master. The framework. |
| **Probe** | Setup-time grading construct against the draft Prompt Strategy. Seven probes specified: P1–P7. §{section.the-seven-probes}. |
| **Prompt Strategy** | The plan of dispatched prompts produced by Setup. Lives in the Master. Iterates in P0; ratifies at P0→P1; revisable at convergence (§{section.strategy-stability}). |
| **Result Completeness Check** | M12. Convergence-time monitor detecting within-domain coverage gaps in returned findings. §{section.m12-result-completeness-check}. |
| **Saturation** | Two consecutive iterations produce no material change to coverage or strategy. §{section.three-layer-readiness}. |
| **Self-check** | The middle block of the triple contract — substrate verification per §{principle.SP-13}. §{section.prism-execution-self-check}. |
| **Setup artifacts** | Four instance-specific artifacts populated during Setup: Decision brief, Stakeholder register, Claim inventory, Jurisdiction map. §{section.setup-artifacts}. |
| **`split` dispatch** | Prompt split into vendor-specific sub-prompts; synthesis happens orchestration-side. §{section.single-envelope-with-spectrum-shape}. |
| **Stakeholder register** | Setup artifact. Per-role listing of stake, decision power, communication channel. §{section.stakeholder-register}. |
| **Standing Principle (SP)** | Persistent posture; not a discrete fire. Twelve SPs in v2 (one dissolved, three new, eight carryforward). §{section.standing-principles}. |
| **Strategy stability** | At P0→P1 ratification, strategy is "presumed stable, revisable at convergence." §{section.strategy-stability}. |
| **Substitution** | Output's Vendor field differs from Envelope's recommended Vendor. Absorbed at convergence; no automatic re-dispatch. §{section.substitution-absorption}. |
| **Three-layer readiness** | The P0→P1 boundary clears when Structural completeness, Library coverage saturation, and Operator ratification all clear. §{section.three-layer-readiness}. |
| **Triple contract** | Envelope (inbound) + Self-check (substrate verify) + Output (outbound). The load-bearing interface between sessions. §{section.the-triple-contract}. |
| **Update session** | Standalone, rare, operator-gated session that maintains Library currency. §{section.currency-maintenance-update-session}. |
| **User Voice Probe** | Setup-time probe (§{probe.P7}). Imports real end-user signal. §{section.probe-7-user-voice-iterates-early}. |
| **Vendor config** | Envelope/Output field carrying vendor-specific configuration flags. §{section.prism-execution-envelope}. |
| **Vendor Selection** | Live web-search currency check at every dispatch; produces Envelope. §{section.vendor-selection-at-dispatch}. |
| **Vendor Triangulation** | Layer-1 convergence pass that fires at N≥2 for `equivalence` dispatches. §{section.vendor-triangulation}. |
| ***What's next*** | Per-turn-close artifact. The operator's single source of "what to do next." §{section.whats-next}. |

---
