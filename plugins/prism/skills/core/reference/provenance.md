<!-- PRISM v2.17.0 Skill bundle (on-demand reference). Spec→v2 source mapping, decision tag index, v1.x→v2 surface drift (Appendices B–D). Reference.
     Generated from the assembled PRISM.md — edit PRISM.md, not this. -->

## Appendix B — Spec → v2.0 source mapping
<a id="appendix-spec-v2-0-source-mapping"></a>

How sections of the v2 specification (`PRISM_v2_spec_rev2.md`) map into
this operating document. Use this when reading rationale-level
discussion in the spec and wanting to find the operating instruction
here, or vice versa.

| Spec section | Topic | This file |
|---|---|---|
| Spec.§{section.scope} | Scope of spec | §{section.scope} |
| Spec.§{section.system-overview} | System overview | §{section.system-overview} |
| Spec.§{section.two-session-types} | Two session types | §{section.two-session-types} |
| Spec.§{section.the-triple-contract} | Triple contract | §{section.the-triple-contract} |
| Spec.§{section.the-master} | Master | §{section.the-master} |
| Spec.§{section.whats-next} | *What's next* | §{section.whats-next} |
| Spec.§{section.forward-compatibility-commitments} | Forward-compatibility commitments | §{section.forward-compatibility-commitments} |
| Spec.§{section.vendor-selection-at-dispatch} | Vendor Selection | §{section.vendor-selection-at-dispatch} |
| Spec.§{section.single-envelope-with-spectrum-shape} | Single-Envelope-with-spectrum | §{section.single-envelope-with-spectrum-shape} |
| Spec.§{section.rationale-discipline-per-dispatch-variant} | Rationale discipline | §{section.rationale-discipline-per-dispatch-variant} |
| Spec.§{section.vendor-triangulation} | Vendor Triangulation | §{section.vendor-triangulation} |
| Spec.§{section.asymmetric-parallel-return-handling} | Asymmetric returns | §{section.asymmetric-parallel-return-handling} |
| Spec.§{section.claude-baseline-feasibility-with-named-limitation-escape-hatch} | Claude-baseline | §{section.claude-baseline-feasibility-with-named-limitation-escape-hatch} |
| Spec.§{section.cost-signaling} | Cost signaling | §{section.cost-signaling} |
| Spec.§{section.recommended-vs-executed-reconciliation} | Reconciliation | §{section.recommended-vs-executed-reconciliation} |
| Spec.§{section.master-tracking-dispatch-register} | Dispatch register | §{section.master-tracking-dispatch-register} |
| Spec.§{section.operator-declaration-close-loop} | Close-loop | §{section.operator-declaration-close-loop} |
| Spec.§{section.substitution-absorption} | Substitution absorption | §{section.substitution-absorption} |
| Spec.§{section.prompt-body-convergence-provisions} | Body convergence provisions | §{section.prompt-body-convergence-provisions} |
| Spec.§{section.telemetric-framework-signal-weighting-and-compounding} | Telemetric framework | §{section.telemetric-framework-signal-weighting-and-compounding} |
| Spec.§{section.m5-context-pressure-monitor} | M5 + M12 consolidation | §{section.m5-context-pressure-monitor} |
| Spec.§{section.continuous-curation-posture} | Continuous-curation | §{section.continuous-curation-posture} |
| Spec.§{section.migration-handoff} | Migration handoff | §{section.migration-handoff} |
| Spec.§{section.failsafe-recovery-continuous-state-mechanics} | Continuous-state mechanic | §{section.failsafe-recovery-continuous-state-mechanics} |
| Spec.§{section.defensive-migration-at-natural-seams} | Migration matrix | §{section.defensive-migration-at-natural-seams} |
| Spec.§{section.from-waterfall-to-library-graded-iterative-refinement}–6.5 | Setup mechanics | §{section.from-waterfall-to-library-graded-iterative-refinement}–§{section.strategy-stability} |
| Spec.§{section.library-reference-at-setup}–7.5 | Library integration | §{section.library-reference-at-setup}–§{section.currency-maintenance-update-session} |
| Spec.§{section.claude-project-as-setup-recommendation} | Claude Project recommendation | §{section.claude-project-as-setup-recommendation} |
| Spec.§{section.session-history-as-validation-recovery} | Session history | §{section.session-history-as-validation-recovery} |
| Spec.§{section.standalone-monitors-m1-m2-m4-m5-m9} | Bump atomicity / M2 | §{section.filename-conventions-and-bump-atomicity} + §{section.m2-version-drift} |
| Spec.§{section.convergence-time-monitors-m6-m7-m8-m12} | Attachment warnings | §{section.attachment-warnings} |
| Spec.§{section.whats-next-input-monitors-m3-m10-m11} | M8 vs §{section.currency-maintenance-point-refresh} boundary | §{section.m8-stale-source} |
| Spec.§{section.standing-principles} | Worked example | §{section.worked-example-flow} |
| Spec.§{section.filename-conventions-and-bump-atomicity} | Monitor specs | §{section.monitor-specifications} |
| Spec.§{section.template-shape} | New / extended SPs | §{section.standing-principles-introduced-or-extended-in-v2} |
| Spec.§{section.composition-rules} | SP carryforward catalog | §{section.v1-x-standing-principles-carryforward-catalog} |
| Spec.§{section.operator-hint-catalog} | Resolved direction summary | (provenance — not reproduced) |
| Spec.§{section.missing-handoff-recovery} | Empirical items | §{section.empirical-calibration-items} |
| Spec.§{section.worked-example-flow} | Build residuals | §{section.filename-conventions-and-bump-atomicity}, §{section.atomic-prompt-template-v2-form}, §{section.operator-hint-catalog}, §{section.missing-handoff-recovery}, App C |
| Spec.§{section.empirical-calibration-items} | Flagged-items register | (provenance — see Spec) |
| Spec.§{section.mobile-operator-survival-guide} | Status | (provenance — see Spec) |
| Spec.App A | Terminology | App A |
| Spec.App B | Tag index | App C |
| Spec.App C | v1.x → v2 surface drift | App D |
| DD.App E | Mobile operator survival guide | §{section.mobile-operator-survival-guide} |

Provenance items (where this file does not reproduce content from spec):

- **Resolved direction summary tables** (Spec.§{section.operator-hint-catalog}). Provenance only —
  every direction listed there is implemented in the body of this file.
- **Flagged-items register** (Spec.§{section.empirical-calibration-items}). Alternatives considered for
  each design decision live in the spec; this file carries only the
  chosen alternative with its tag.
- **Status section** (Spec.§{section.mobile-operator-survival-guide}). Build phase is past — this file is the
  build output.

---

## Appendix C — Decision tag index
<a id="appendix-decision-tag-index"></a>

Every decision in this document carries a two-axis tag. This appendix
indexes decisions by tag for easy review.

**Durability axis values:** `structural`, `methodological`,
`vendor-dependent`, `empirical`, `operator-scaffolding`.

**Review-trigger axis values:** `stable`, `review-if: <trigger>`,
`review-annually`.

### C.1 `[structural | stable]`
<a id="appendix-structural-stable"></a>

§{section.what-v2-8-0-covers} (scope), §{section.three-leg-constraint} (three-leg constraint), §{section.two-session-types} (two session types),
§{section.the-triple-contract} (triple contract), §{section.the-master} (Master), §{section.whats-next} (*What's next*), §{section.forward-compatibility-commitments}
(forward-compatibility commitments), §{section.single-envelope-with-spectrum-shape} (single-Envelope-with-
spectrum), §{section.vendor-triangulation} (Vendor Triangulation), §{section.asymmetric-parallel-return-handling} (asymmetric returns), §{section.recommended-vs-executed-reconciliation}
(reconciliation), §{section.master-tracking-dispatch-register} (Dispatch register), §{section.operator-declaration-close-loop} (close-loop), §{section.substitution-absorption}
(substitution absorption), §{section.prompt-body-convergence-provisions} (prompt body convergence provisions),
§{section.m5-context-pressure-monitor} (§{monitor.M5}), §{section.migration-handoff} (migration handoff format), §{section.failsafe-recovery-continuous-state-mechanics} (continuous-state
mechanic), §{section.defensive-migration-at-natural-seams} (defensive migration), §{section.three-layer-readiness} (three-layer readiness),
§{section.probe-1-coverage-grading-iterates} (Probe 1 Coverage grading), §{section.probe-2-adversarial-scope-iterates} (Probe 2 Adversarial Scope),
§{section.probe-7-user-voice-iterates-early} (Probe 7 User Voice), §{section.strategy-stability} (strategy stability), §{section.library-reference-at-setup} (Library
reference at Setup), §{section.m1-missing-inputs} (§{monitor.M1} Missing Inputs), §{section.m2-version-drift} (§{monitor.M2} Version
Drift), §{section.m6-premise-shift} (§{monitor.M6} Premise Shift), §{section.m7-claim-conflict} (§{monitor.M7} Claim Conflict), §{section.m8-stale-source}
(§{monitor.M8} Stale Source), §{section.m12-result-completeness-check} (§{monitor.M12} Result Completeness Check), §{section.m3-sequence-violation} (§{monitor.M3}
Sequence Violation), §{section.m10-rerun-fix-required} (§{monitor.M10} Rerun/Fix Required), §{section.m11-layer-2-readiness} (§{monitor.M11} Layer
2 Readiness), §{section.filename-conventions-and-bump-atomicity} (filename conventions and bump atomicity), §{section.template-shape}
(atomic prompt template), §{section.project-feedback-updates} (project, feedback, updates), §{section.project-identity}
(project identity), §{section.resource-fetch-convention} (resource fetch convention), §{section.feedback-and-contribution} (feedback
and contribution), §{section.citation} (citation), §{section.lanes-roles-and-the-prism-ui} (lanes,
roles, and the PRISM UI), §{section.cross-lane-inbox} (cross-lane OPEN_ITEMS
inbox), §{section.prism-desk-and-prism-meta} (PRISM Desk and PRISM Meta),
§{section.prism-ui} (PRISM UI), §{section.bundle-load-integrity} (bundle-load
integrity), §{section.setup-onboarding-and-mode-selection} (Setup onboarding
and mode selection), §{section.dispatch-lifecycle} (dispatch lifecycle), §{section.transport-integrity-bracket} (transport-integrity bracket).

### C.2 `[methodological | stable]`
<a id="appendix-methodological-stable"></a>

§{section.rationale-discipline-per-dispatch-variant} (rationale discipline), §{section.cost-signaling} (cost signaling), §{section.from-waterfall-to-library-graded-iterative-refinement} (iterative
refinement), §{section.currency-maintenance-point-refresh} (point refresh), §{section.currency-maintenance-update-session} (Update session), §{section.m4-ambiguous-ask} (§{monitor.M4}
Ambiguous Ask), §{section.m9-convergence-type-drift} (§{monitor.M9} Convergence Type Drift), §{section.operator-hint-catalog} (operator hint
catalog), §{section.recovery-flow} (missing-handoff recovery flow), §{section.currency-check-at-session-open} (currency check
at session open), §{section.sp-16-the-elephant-rule} (§{principle.SP-16} The
Elephant Rule — uninvited-frame discipline), §{section.sp-17-plain-words-first}
(§{principle.SP-17} Plain words first), §{section.sp-18-it-must-recompute}
(§{principle.SP-18} It must recompute), §{section.sp-19-claims-carry-their-basis}
(§{principle.SP-19} Claims carry their basis), §{section.sp-20-editions-stand-alone}
(§{principle.SP-20} Editions stand alone), §{section.sp-21-trust-structure-self-report-advisory}
(§{principle.SP-21} Trust structure, self-report advisory),
§{section.sp-22-surface-translation} (§{principle.SP-22} Surface translation),
§{section.independent-validation-dispatch}
(Independent Validation Dispatch).

### C.3 `[methodological | review-if: substrate shifts]`
<a id="appendix-methodological-review-if-substrate-shifts"></a>

§{section.telemetric-framework-signal-weighting-and-compounding} (telemetric framework — calibration thresholds empirical).

### C.4 `[methodological | review-if: vendor landscape changes]`
<a id="appendix-methodological-review-if-vendor-landscape-changes"></a>

§{section.vendor-selection-at-dispatch} (Vendor Selection routine).

### C.5 `[vendor-dependent | review-if: orchestration vendor changes]`
<a id="appendix-vendor-dependent-review-if-orchestration-vendor-changes"></a>

§{section.claude-project-as-setup-recommendation} (Claude Project recommendation), §{section.session-history-as-validation-recovery} (session history mechanism).

### C.6 `[vendor-dependent | review-if: vendor landscape changes]`
<a id="appendix-vendor-dependent-review-if-vendor-landscape-changes"></a>

§{section.claude-baseline-feasibility-with-named-limitation-escape-hatch} (Claude-baseline + escape hatch list).

### C.7 `[operator-scaffolding | stable]`
<a id="appendix-operator-scaffolding-stable"></a>

§{section.sp-1-extended-canonicity-preservation} (§{principle.SP-1} ext Canonicity), §{section.sp-12-bounded-search-disclosure} (§{principle.SP-12} Bounded-Search Disclosure),
§{section.sp-13-substrate-declaration} (§{principle.SP-13} Substrate Declaration), §{section.sp-10-verify-state-before-recommending} (§{principle.SP-10} Verify state
before recommending), §{section.sp-14-filename-discipline} (§{principle.SP-14} Filename Discipline), §{section.sp-8-narrowed-canonical-authority}
(§{principle.SP-8} Canonical Authority — narrowed).

### C.8 `[empirical | review-annually]`
<a id="appendix-empirical-review-annually"></a>

§{section.empirical-calibration-items} (empirical calibration items — collectively; individual items
inherit calibration trigger).

### C.9 `[methodological | review-if: release-sweep | recommended]`
<a id="appendix-methodological-review-if-release-sweep-recommended"></a>

§{appendix.vendor-parsing-observations} (Appendix H preamble — vendor parsing
observations: empirical, observation-driven; the preamble's maintenance
protocol carries the tag, the table rows are data).

**Tag count summary.**

The strength axis (`required` default; `recommended` / `optional` non-default)
and polarity glyphs (✅ / ⚠️ / 🚫) are introduced in v2.1.0 per the
frontmatter `normativity` block; only non-default strength values appear as
tokens in tags. The summary below indexes by the original two-axis pair
(durability × review-trigger); rows whose listed entries include non-default
strength are noted parenthetically.

| Axis 1 \ Axis 2 | stable | review-if | review-annually | Total |
|---|---|---|---|---|
| structural | 43 | 0 | 0 | 43 |
| methodological | 12 | 3 (1 with `recommended`) | 0 | 15 |
| vendor-dependent | 0 | 3 | 0 | 3 |
| operator-scaffolding | 6 | 0 | 0 | 6 |
| empirical | 0 | 0 | 1 | 1 |
| **Total** | **61** | **6** | **1** | **68** |

---

## Appendix D — v1.x → v2 surface drift
<a id="appendix-v1-x-v2-surface-drift"></a>

Construct-by-construct mapping for operators familiar with v1.10.4.
Direct carryforwards (🔁) and new constructs (🆕) marked; surface drift
items documented with the change.

### D.1 Sessions and lifecycle
<a id="appendix-sessions-and-lifecycle"></a>

| v2 construct | v1.10.4 counterpart | Disposition |
|---|---|---|
| Orchestration session | Setup + convergence sessions (PRISM.md attached) | v2 names the split that v1.x ran inconsistently |
| Execution session | Phase 1 specialist prompt session | Hardened contract via triple |
| Update session | — | 🆕 |
| Master | Starter | Renamed; functionally same |
| *What's next* | TRI-21 progress pointer (single ID) | Reshaped to full artifact |
| Lens Library | — | 🆕 — core v2 architecture |

### D.2 Probes
<a id="appendix-probes"></a>

| v2 probe | v1.x counterpart | Notes |
|---|---|---|
| P1 Coverage grading | — | 🆕 Library-driven |
| P2 Adversarial Scope | Red Team (Phase 2 enrichment) — partial | Reshape — Red Team operated post-finding; P2 operates pre-execution |
| P3 Decision Framing | Implicit in Setup brief | Made explicit; full output is Decision brief + Stakeholder register |
| P4 Pre-mortem | — | 🆕 |
| P5 Falsifier | Red Team (in spirit) | Falsifier is at Setup; Red Team was post-finding |
| P6 Domain Reconnaissance | Discovery (Setup-phase enrichment) | Direct counterpart; covers practice survey + authoritative-source check + Jurisdiction map |
| P7 User Voice | User Voice (Phase 2 enrichment role) | Promoted from Phase 2 enrichment to Setup probe — informs strategy *before* execution |

**v1.x roles not migrating as probes:**

- **Coverage** (Phase 2 enrichment, "find what a specific prompt missed
  within its domain") → became **M12 Result Completeness Check**
  (convergence-time monitor).
- **Fact Check** (Phase 2 enrichment) → absorbed into M8 Stale Source +
  Layer-1 reconciliation.
- **Deep Research** (Phase 2 enrichment) → Vendor Selection mode field
  (§{section.vendor-selection-at-dispatch}).

### D.3 Monitors
<a id="appendix-monitors"></a>

| v2 | v1.x | Disposition |
|---|---|---|
| M1 Missing Inputs | M1 Missing Inputs | 🔁 |
| M2 Version Drift | M2 Version Drift | 🔁 — surface narrowed to filename version |
| M3 Sequence Violation | M3 Sequence Violation | 🔁 |
| M4 Ambiguous Ask | M4 Ambiguous Ask | 🔁 |
| M5 Context Pressure | M5 Attachment Pressure + M12 Conversation Pressure | Merged into single telemetric monitor |
| M6 Premise Shift | M6 Premise Shift | 🔁 — surface broadened (premises now read from Setup artifacts) |
| M7 Claim Conflict | M7 Assumption Conflict | Renamed — v1.x had Assumption Register; v2 reads finding-vs-finding directly |
| M8 Stale Source | M8 Stale Source | 🔁 — surface narrowed (audit evidence only; framework-anchor staleness is point refresh §{section.currency-maintenance-point-refresh}) |
| M9 Convergence Type Drift | M9 Convergence Type Drift | 🔁 — surface broadened (also catches dispatch-mode treatment errors) |
| M10 Rerun/Fix | M10 Rerun/Fix | 🔁 |
| M11 Layer 2 Readiness | M11 Layer 2 Readiness | 🔁 |
| M12 Result Completeness Check | (slot was M12 Conversation Pressure — retired) | 🆕 in v2 (slot reused; v1.x M12 absorbed into M5) |

### D.4 Standing Principles
<a id="appendix-standing-principles"></a>

| v2 SP | v1.x | Disposition |
|---|---|---|
| SP-1 ext | SP-1 (Never reconstruct from memory) | Extended in v2 — covers *offers* to reconstruct |
| SP-2 | SP-2 (Defer non-critical fixes) | 🔁 |
| (none) | SP-3 (Convergence in prompt session) | Dissolved — incompatible with orchestration/execution split |
| SP-4 | SP-4 (Monitors visible) | 🔁 |
| SP-5 | SP-5 (No heuristic guessing) | 🔁 |
| SP-6 | SP-6 (Rebuild at threshold) | 🔁 |
| SP-7 | SP-7 (File delivery mandatory) | 🔁 |
| SP-8 narrowed | SP-8 (Canonical authority + filename disambig) | Split — (a) stays SP-8; (b) becomes SP-14 |
| SP-9 | SP-9 (Silence is never consent) | 🔁 |
| SP-10 | SP-10 (Verify state before recommending) | 🔁 as named principle; mechanics live in Vendor Selection §{section.vendor-selection-at-dispatch} |
| SP-12 | — | 🆕 Bounded-Search Disclosure |
| SP-13 | — | 🆕 Substrate Declaration |
| SP-14 | (extracted from SP-8) | 🆕 — Filename Discipline |

### D.5 Other constructs
<a id="appendix-other-constructs"></a>

| v2 | v1.x | Disposition |
|---|---|---|
| Triple contract (Envelope/Self-check/Output) | Atomic prompt template + Execution notes | Reshape; Self-check is new |
| Vendor Selection | Execution notes (per-prompt prose at Setup, SP-10) | Reshape from Setup-prose to dispatch-time live step |
| Vendor Triangulation | (no v1.x mechanism for this) | 🆕 |
| Bands (🟢🟡🟠🔴) | Context Pressure Bands | 🔁 |
| Two-layer convergence | Two-layer convergence | 🔁 |
| Setup artifacts | Implicit in Setup brief | Made explicit and structured |
| Scope Flags | Scope Flags (5: SF1-SF5) | All dissolved |
| Runtime Profile | Runtime Profile | Dissolved into telemetric framework |
| GATE-0 / GATE-1 / GATE-2 | Gates | Folded into Monitors + What's next + M11 |
| Adaptations | Adaptations | Lighter — strategy-stability with revisable-at-convergence + Master version bump |
| Discrepancy Check | Discrepancy Check (prompt-template mechanic) | Absorbed into M7 Claim Conflict + Layer-1 reconciliation |

### D.6 Nomenclature changes
<a id="appendix-nomenclature-changes"></a>

| Concept | v1.x | v2 |
|---|---|---|
| Project state file | Starter | Master |
| Progress pointer | (single ID, TRI-21) | *What's next* artifact |
| Inbound prompt header | (informal Execution notes) | Execution Envelope |
| Outbound finding signature | (informal — extracted by user) | Execution Output (file with structured signature) |
| Multi-vendor reconciliation | Discrepancy Check + Fact Check | Vendor Triangulation |
| Within-prompt scope check | Coverage role | M12 Result Completeness Check |
| Domain external signal import | Discovery role | P6 Domain Reconnaissance |
| User signal import | User Voice role | P7 User Voice |
| Filename look-alike defense | SP-8 (b) | SP-14 |
| Recommendation freshness check | SP-10 (in Setup execution notes) | SP-10 + Vendor Selection live check |

---
