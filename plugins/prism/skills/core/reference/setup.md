<!-- PRISM v2.21.0 Skill bundle (on-demand reference). Setup mechanics (sections 6.1-6.6, 7.1, 7.3-7.4, 8.1) — three-layer readiness, the seven probes (P1–P7), Setup-artifact procedures, strategy stability, onboarding; Library-reference-at-Setup; the Scope-Integrity Test and specialist-pass promotion; the Claude-Project-as-Setup recommendation. Fetch at a Setup session.
     Generated from the assembled PRISM.md — edit PRISM.md, not this. -->

## 6. Setup mechanics
<a id="section-setup-mechanics"></a>

Setup is iterative refinement against the Lens Library. Not waterfall. The
P0→P1 boundary clears when three independent layers all read ready
simultaneously.

### 6.1 From waterfall to library-graded iterative refinement `[structural | stable]`
<a id="section-from-waterfall-to-library-graded-iterative-refinement"></a>

**Setup iteration loop.**

1. Operator provides initial subject brief.
2. Orchestration produces draft Prompt Strategy P0.1.
3. Probes 6, 7 iterate early in P0.1 (Domain Reconnaissance + User Voice);
   Probes 1, 2, 4 iterate per turn; Probes 3 and 5 run once.
4. Probe 1 (Coverage grading) outputs tri-state dispositions per Lens
   (§{section.probe-1-coverage-grading-iterates}).
5. Operator reviews probe outputs.
6. Orchestration produces P0.2 incorporating closures.
7. Repeat until §{section.three-layer-readiness} readiness clears.

**Iteration numbering** — P0.1, P0.2, …. No artificial cap. Floor: minimum
2 iterations. Soft ceiling: at 4 iterations without saturation, flag
*something structural may be wrong — operator intervention recommended*.

### 6.2 Three-layer readiness `[structural | stable]`
<a id="section-three-layer-readiness"></a>

All three layers must clear before P0 → P1 boundary.

#### Layer 1 — Structural completeness

Every planned prompt has a complete pass **spec** — **not** a frozen Envelope.
The Envelope is *rendered just-in-time at dispatch* (the dispatch lifecycle's
Build stage, §{section.dispatch-lifecycle}); requiring a populated Envelope here
would force a Setup-time render to be replayed stale on a long engagement, the
opposite of late binding. The spec is the durable, Setup-graded,
convergence-revisable (§{section.strategy-stability}) contract; it carries:

- Single objective (one-sentence statement).
- Output format (structured findings per §{section.prompt-body-convergence-provisions}).
- Dependency list (which prior prompts' outputs are inputs; can be empty).
- Attachment map (filenames per attachment).
- Enrichment decision (single-vendor / equivalence / split /
  limitation-named).
- Success criteria + the applicable conventions and lenses — what "done" means
  and what binds. This is the **anchor** the just-in-time Envelope render must
  preserve (objective + lens-coverage + success-criteria), so a late-bound
  rebuild refreshes the *rendering* without re-scoping the Setup grading.

Verification: orchestration walks the strategy and confirms each prompt has a
complete spec across these six fields. Any missing field halts P0 → P1. The
Envelope itself is not required to clear this gate — it is built at dispatch
from the live Master and current conventions (§{section.prism-execution-envelope}),
anchored to this spec, with the decisive caveats carried forward explicitly so
the fresh Dispatch-builder loses nothing the Desk knew.

#### Layer 2 — Library coverage saturation

Every applicable Lens from the Lens Library v0.16 is either:

- Covered by at least one planned prompt (Probe 1 disposition:
  *fires-covered*), OR
- Explicitly marked out of scope with rationale (Probe 1 disposition:
  *doesn't-fire* with rationale captured, OR *fires-maybe* closed via
  *opt-out* per §{section.probe-1-coverage-grading-iterates}).

**Saturation signal.** Two consecutive iterations produce no material
change to coverage or strategy.

**Material change criteria.**

- New Lens added to coverage map (P0.x → P0.x+1).
- Existing Lens disposition changes from *fires-uncovered* to
  *fires-covered* (or *opt-out*).
- New planned prompt added or merged.
- Prompt's Vendor or Vendor config changed.

If two consecutive iterations show none of the above, saturation reached.

#### Layer 3 — Operator ratification

Operator confirms the strategy matches intent. Free-form confirmation;
orchestration parses for explicit ratification ("ratify", "approved", "go",
"looks good — proceed"). SP-9 lineage: silence is not ratification.

**Ratification triggers P0 → P1.** Master filename bumps to P1 (e.g.,
`acme_audit_prism2.0_master_p1.0.md`). Setup probes close. Strategy moves
to "presumed stable, revisable at convergence" per §{section.strategy-stability}.

### 6.3 The seven probes
<a id="section-the-seven-probes"></a>

Probes operate against the draft Prompt Strategy at Setup. Vendor
Triangulation (§{section.vendor-triangulation}) — convergence-time cross-vendor reconciliation —
lives outside the probe taxonomy because it operates against returned
findings, not draft strategy. Result Completeness Check (§{monitor.M12}, §{section.m12-result-completeness-check}) is
a convergence-time monitor. Single-responsibility discipline: probes are
Setup-time grading constructs only.

#### 6.3.1 Probe 1 — Coverage grading (iterates) `[structural | stable | ✅]`
<a id="section-probe-1-coverage-grading-iterates"></a>

Grade the draft strategy against the Lens Library v0.16. Universal lenses
(5) always evaluated. Domain lenses (18) evaluated where their `trigger:`
predicate is met by the subject.

**Per-lens disposition** (tri-state with maybe sub-state):

- **`fires-covered`** — lens applies, draft already covers it, and the
  Scope-Integrity Test passes (see below). Silent pass; recorded for
  audit trail.
- **`fires-uncovered`** — lens applies, draft does not cover it. Surfaces
  as a flag; closed by adding coverage in next iteration.
- **`doesn't-fire`** — trigger predicate not met; rationale captured (one
  line).
- **`fires-maybe`** — applicability or coverage ambiguous.
  - **`fires-maybe — dig-in`** — judging LLM does targeted research on the
    lens-subject intersection. Produces an expanded lens framing or a
    scoped specialist pass to add to the strategy. Closes by becoming
    *fires-covered* in next iteration.
  - **`fires-maybe — opt-out`** — documented exclusion with rationale.
    Closes by becoming a recorded out-of-scope decision.

**Scope-Integrity Test — the `fires-covered` gate.** A lens cannot be
marked `fires-covered` on assertion alone. Before the disposition is
recorded, restate the lens's own `minimum_scope_binding:` as a yes/no
falsifier — *every clause satisfied with evidence, or any clause unmet?* —
and answer it in context. A clause-by-clause pass is required; any unmet or
undocumented clause forces `fires-uncovered` (or a documented
`fires-maybe — opt-out`) instead. A lens carrying a `scope_integrity_probe:`
field uses that sharpened falsifier in place of the generic restatement.
This inline self-check is the always-on floor of the Scope-Integrity Test;
its rigor ladder and home are specified in §{section.scope-integrity-test-sit}.

**Disposition output format** (per turn-close in P0):

```
━━━ PROBE 1 — COVERAGE GRADING ━━━
Iteration: P0.x
Universal lenses (5):
  LL-U-001 Who gets hurt?           — fires-covered (P2.1)
  LL-U-002 What's the thesis?       — fires-covered (decision brief)
  LL-U-003 What would refute?       — fires-uncovered (FLAG)
  LL-U-004 Who acts on this?        — fires-covered (decision brief)
  LL-U-005 What laws touch this?    — fires-maybe → dig-in
Domain lenses (triggered):
  LL-D-002 Can anyone use?          — fires-covered (P3.4 a11y pass)
  LL-D-005 Can attackers get in?    — fires-uncovered (FLAG)
  LL-D-011 Is data handled lawfully? — fires-maybe → opt-out
                                       (rationale: subject is read-only
                                       informational service; no PII)
  ...
Domain lenses (not triggered):
  LL-D-016 Is the ledger safe?      — doesn't-fire (no custody/payments)
  ...
Saturation flag: not-yet (3 changes from P0.2)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Operator-fatigue mitigation.** Judging LLM resolves clear cases silently
(covered or doesn't-fire with obvious rationale). Escalates to operator
only on genuine ambiguity (*fires-maybe* requiring dig-in vs. opt-out
decision). Empirical calibration deferred — see §{section.empirical-calibration-items}.

#### 6.3.2 Probe 2 — Adversarial Scope (iterates) `[structural | stable | ✅]`
<a id="section-probe-2-adversarial-scope-iterates"></a>

Hunt for silent omissions and under-scoped treatments in the draft Prompt
Strategy. Library-driven (uses Library entries as starting prompts but
goes beyond catalog); informed by domain context.

**Lifecycle.** Setup-only. Iterates per P0.x turn-close. Does not fire at
Layer-1 convergence — cross-vendor finding triangulation is a separate
mechanism (Vendor Triangulation, §{section.vendor-triangulation}) with its own trigger and output
shape.

**Multi-vendor recommendation.** Independent adversarial passes across
vendors; divergence between passes is signal about scope blind spots. Not
the same as cross-vendor finding reconciliation.

**Output.** List of silent-omission candidates the strategy did not
address. Operator reviews; orchestration converts surviving candidates
into Lens references or new prompt additions in the next iteration.

#### 6.3.3 Probe 3 — Decision Framing (once) `[structural | stable | ✅]`
<a id="section-probe-3-decision-framing-once"></a>

Does the strategy answer what the stakeholder actually needs to decide?

**Operator-positioning question (new in v2.15.0).** Who commissioned this and
why? What is their relationship to the subject and to the decision? What angle
or conflict does that create, and how should the brief be framed to be true to
it? Answer positively (§{principle.SP-16}) — state what each stakeholder *is*
and the conflict it creates, never a denial of what they are not. Every
stakeholder *and the operator/commissioner* is captured with role, motivation,
and positioning/angle.

Outputs the Decision brief and Stakeholder register Setup artifacts
(§{section.decision-brief}, §{section.stakeholder-register}).

#### 6.3.4 Probe 4 — Pre-mortem (iterates) `[structural | stable | ✅]`
<a id="section-probe-4-pre-mortem-iterates"></a>

Imagine execution completes. How would the finding fail to answer the
original question?

**Output.** A list of pre-mortem failure modes; each surviving mode either
becomes a new probe in the strategy or is dismissed with rationale.

#### 6.3.5 Probe 5 — Falsifier (once) `[structural | stable | ✅]`
<a id="section-probe-5-falsifier-once"></a>

What findings would invalidate the thesis?

**Output.** Decision brief gains a Falsifiers section listing findings
that, if observed, would refute the thesis. These become explicit
success/failure criteria for Layer 2 synthesis.

#### 6.3.6 Probe 6 — Domain Reconnaissance (iterates early) `[structural | stable | ✅]`
<a id="section-probe-6-domain-reconnaissance-iterates-early"></a>

What do practitioners, researchers, and serious analysts of this domain
actually investigate? What lenses does the domain's own literature treat
as default?

**Imports domain-external signal that the Library cannot carry.**

Asks whether an authoritative canonical source exists for the domain:

- Regulated registry?
- Standards body with testable criteria?
- Curated research corpus?
- Benchmark dataset?

If yes: strategy brings it in as primary evidence; Probe 6 outputs a
citation.

**Multi-vendor recommended.** Different vendors have different exposure to
domain-specific literature.

Outputs the Jurisdiction map Setup artifact (§{section.jurisdiction-map}).

#### 6.3.7 Probe 7 — User Voice (iterates early) `[structural | stable | ✅]`
<a id="section-probe-7-user-voice-iterates-early"></a>

Imports real end-user / customer / affected-user perspectives into Setup.
Mines actual user signal from forums, reviews, support tickets, public
commentary, social platforms — whatever surfaces are available for the
subject's user base.

**Why a probe.** Strategies built only on the project brief plus Library
lenses risk being shaped by what the framework *expects* users to care
about rather than what they actually do. User Voice surfaces friction
points, pain patterns, and lived-experience signal the brief misses.

**Lifecycle.** Setup-only. Iterates early in P0 alongside Probe 6 (Domain
Reconnaissance) — both import external signal before the strategy hardens.

**Multi-vendor recommended.** Different vendors have different exposure to
user-generated content (Perplexity is strong on live web; Claude on
synthesis from quoted text; Gemini on long-context corpus).

**Output.** A list of user-surfaced concerns, friction points, and
reality-checks that feed the strategy. Surviving items either become new
prompts, become flagged-for-coverage Library lenses, or refine the
Decision brief's stakeholder section.

**v1.x lineage.** v1.x had User Voice as a Phase 2 enrichment role
("mine real user perspectives — reality check"). v2 promotes it to Setup
probe so user signal informs strategy *before* execution rather than
enriching findings *after*.

#### 6.3.8 Probe ordering — recommended sequence
<a id="section-probe-ordering-recommended-sequence"></a>

P0.1: Probe 6 (Domain Reconnaissance — establishes domain context); Probe
7 (User Voice — imports user signal); Probe 1 (initial coverage); Probe 3
(Decision Framing).
P0.2: Probe 4 (pre-mortem); Probe 1 (re-grade); Probe 2 (adversarial
scope).
P0.3: Probe 1 (re-grade for saturation); Probe 5 (falsifier).
P0.4+: Probes 1, 2, 4, 6, 7 iterate as needed until saturation.

Order is a default; operator may re-sequence per project shape.

**Probe taxonomy notes.** P5 Consolidation (rev. 1 of the spec) dissolved —
structural overlap-spotting is judgment work the LLM does inside Probe 1
and Probe 2 grading rather than a checkbox-shaped standalone probe.
Aligns with v2's principle-heavy / specification-light philosophy. Vendor
Triangulation extracted from rev. 1's Probe 2 and lives in §{section.vendor-triangulation}, not in
the probe taxonomy.

### 6.4 Setup artifacts
<a id="section-setup-artifacts"></a>

Four instance-specific artifacts populated during Setup. Live in the
Master (§{section.the-master} required sections).

#### 6.4.1 Decision brief
<a id="section-decision-brief"></a>

Populated by Probe 3 primarily; refined by Probe 5 (Falsifiers section).

**Commissioner positioning is an explicit premise (new in v2.15.0).** The
verified operator/commissioner positioning — role, motivation, and
angle/conflict relative to the subject and the decision — is recorded as a
Decision-brief premise, stated positively (§{principle.SP-16}). M6
(§{monitor.M6}) then guards the right premise: a finding that contradicts the
pinned positioning fires M6 correctly, but the frame is correct from P0, so M6
is a backstop, not the primary catch.

```
## Decision brief

Subject:           [name]
Decision under test: [one sentence]
Decision-maker:    [name or role]
Commissioner positioning: [operator/commissioner role, motivation, angle/conflict — stated positively]
Deadline:          [date or trigger]
Cost of error:    
  - False positive: [cost]
  - False negative: [cost]
Stakes / blast radius: [one paragraph]
Falsifiers:        [list — findings that would refute the thesis]
```

**Quantitative core → an interactive workbook (new in v2.18.0).** When the
decision under test has a quantitative, operator-tunable core (unit economics, a
threshold / corner case, a returns or break-even model), the finding may be
delivered **also** as a live operator-drivable **workbook** — editable assumption
cells driving the brief's decision gate in real time, color-coded — so the
decision-maker explores the verdict against their own numbers. The report
*states* the finding; the workbook lets them *drive* it. Trigger (one per
engagement, on the central quantitative gate) and the cockpit pattern
(editable-cells-only + live gate + opens-at-the-report's-case + §{principle.SP-18}
tie-back) are in §{appendix.report-architecture}.

#### 6.4.2 Stakeholder register
<a id="section-stakeholder-register"></a>

Populated by Probe 3 primarily. Every stakeholder is pinned, and the
**operator/commissioner is a mandatory row — never omitted** (they hold a
stake, a motivation, and an angle that shapes the brief). Motivation and
Positioning/angle are mandatory for the decision-maker and the operator, and
stated positively (§{principle.SP-16}) — what the stakeholder *is* and the
conflict it creates, never a denial of what they are not.

```
## Stakeholder register

| Role | Stake | Motivation | Positioning/angle | Decision power | Communication channel |
|---|---|---|---|---|---|
| [operator/commissioner] | [decision/outcome stake] | [why they want this engagement / this outcome] | [advisor / investor / competitor / partner / regulator / arms-length / advocacy; + any conflict] | [yes/advisory/none] | [channel] |
| [name] | [decision/outcome stake] | [motivation] | [positioning/angle; + any conflict] | [yes/advisory/none] | [channel] |
| ... | ... | ... | ... | ... | ... |
```

#### 6.4.3 Claim inventory
<a id="section-claim-inventory"></a>

Populated by Setup orchestration as it parses subject brief; refined by
Probe 6 (Domain Reconnaissance).

```
## Claim inventory

| Claim type | Specific claim | Source | Audit pass(es) |
|---|---|---|---|
| Efficacy | [...] | [where claim is made] | P2.x |
| Compliance | [...] | [...] | P3.x |
| Positioning | [...] | [...] | P4.x |
| ... | ... | ... | ... |
```

#### 6.4.4 Jurisdiction map
<a id="section-jurisdiction-map"></a>

Populated by Probe 6 (Domain Reconnaissance) primarily.

```
## Jurisdiction map

| Jurisdiction | Triggered regimes | Material to scope? | Pass(es) |
|---|---|---|---|
| US (federal) | FTC, ADA | yes | P3.1 |
| EU | GDPR, EU AI Act | yes | P3.2 |
| US-CA | CCPA/CPRA | yes | P3.1 |
| ... | ... | ... | ... |
```

### 6.5 Strategy stability `[structural | stable]`
<a id="section-strategy-stability"></a>

**At P0 → P1 boundary.** Strategy moves to "presumed stable, revisable at
convergence."

**Strategy revisions** trigger from two sources. *Convergence-time
revisions* trigger when Layer-1 convergence produces:

- A premise invalidation (§{monitor.M6} Premise Shift fires HIGH).
- A newly-surfaced domain area (e.g., a regulatory regime not in the
  Jurisdiction map).
- A falsifier hit (one of the Decision brief's Falsifiers is observed).
- An assumption conflict between two findings (§{monitor.M7}).

*Operator-initiated revisions* trigger independently of convergence:

- **Operator-initiated scope expansion** — the operator adds new prompts or a
  new pass to the strategy (e.g., extending coverage to an additional subject
  area or comparison set), with no premise break, conflict, or falsifier in
  play. It reuses the same draft → ratify → version-bump spine below; the
  revision mechanic does not require a convergence event to fire.

**Follow-up vs M10 re-run.** A *Follow-up* and an §{monitor.M10} re-run
(§{section.m10-rerun-fix-required}) are different operations and must not be
conflated:

- **M10 re-run** — the prior run was *defective or incomplete*; redo that same
  dispatch with corrections. Logged in the Rerun Register
  (§{section.m10-rerun-fix-required}).
- **Follow-up** — the prior run was *sound*, but a new or expanded dimension is
  now wanted. Do **not** augment-and-re-run the completed producer; route the
  scope-addition to the next consuming pass (the natural carrier) or a new
  dedicated pass, as an operator-initiated revision above. The strategy
  progresses additively per results.

Verify live engagement state before advising on either (§{principle.SP-10},
verify-before-recommend, applied to engagement state — not only vendor
currency).

**Revision mechanic** (lighter than v1.x major-bump Adaptation).

1. A revision trigger fires — a convergence-time trigger (above: a premise
   invalidation or assumption conflict via §{monitor.M6} / M7 HIGH, a falsifier
   hit, or a newly-surfaced domain area), or an operator-initiated scope
   expansion.
2. Orchestration drafts a revision: adds/modifies prompts, updates attach
   maps, updates Setup artifacts as needed.
3. Operator ratifies (per Layer 3 §{section.three-layer-readiness}).
4. Master version increments (sub-version bump within phase, e.g., P2.2
   → P2.3).
5. Strategy continues with revised state.

**Attach map travels with each prompt.** When a prompt adapts, its attach
map adapts with it (§{section.prism-execution-envelope}).

**Setup-artifact re-audit (new in v2.15.0).** A Setup premise that is
*mis-scoped at the root* — wrong actor, wrong decision-maker, wrong audience,
wrong frame — and that no returned finding happens to contradict is invisible
to §{monitor.M6} and to every other monitor: nothing re-questions the Setup
artifacts against accumulating reality. Re-audit them proactively at the
P0 → P1 boundary and again before the report is assembled: re-pose the Decision
brief's and Stakeholder register's actor / decision-maker / commissioner
positioning / audience / frame as a falsifier against the evidence gathered
since Setup ("is the named decision-maker still right? whose decision is this
actually? is the commissioner positioning still true?"). A mis-scope found here
is corrected via the revision mechanic above, restated positively
(§{principle.SP-16}) — correct the actor/frame, never plant a denial. This is
the premise-side complement to the P5 falsifier
(§{section.probe-5-falsifier-once}, which tests the *thesis*); M6 stays the
finding-driven backstop.

### 6.6 Setup onboarding and mode selection `[structural | stable]`
<a id="section-setup-onboarding-and-mode-selection"></a>

Setup is the workspace **scaffolder**: the operator should run the system
without learning lanes and roles (§{section.lanes-roles-and-the-prism-ui}).
Two completions of that scaffolding role land here — the onboarding flow
(which generates the engagement's SI and stands up its project(s)) and the
mode offer (full engagement vs quick brief). Reference-grade detail — the SI
template, the project-create / install cards, and the quick-mode procedure —
is in Appendix I (§{appendix.lanes-roles-prism-ui}); this section is the rule.

**Mode offer (first thing Setup does).** Setup offers **full engagement vs
quick brief** at the very top. The mode is **operator-selected**, not
auto-detected — auto-detection risks mis-classifying a real engagement as a
brief.

#### Full-engagement onboarding (Setup-as-scaffolder)

For a full engagement, Setup runs once at engagement creation: **gather →
generate → ratify → commit → emit cards.**

1. **Gather** the per-subject config — mostly already collected by the probes
   that build the Decision brief and Stakeholder register
   (§{section.setup-artifacts}): subject +
   decision tracks; repo + work folder (the `repo_backed` locus); the surface
   registry; credential location + redaction regime; any engagement-specific
   standing directives.
2. **Generate the SI draft** by instantiating the framework **SI template** —
   framework-native sections collapse to one-line references (persistence,
   resume, commit-discipline, the cross-lane inbox, lanes / roles per the
   framework); per-subject sections are filled from the gathered config.
   Engagement-specific standing directives are **embedded verbatim** (memory
   does not cross projects; the SI is the only cross-project carrier).
3. **Operator ratification — a hard gate (SP-9, §{principle.SP-9}).** Setup
   presents the draft SI to ratify or edit before install: **auto-draft, not
   auto-install** — generated so the operator never hand-writes boilerplate,
   ratified so a bespoke SI is still possible. Silence is not ratification.
4. **Commit the SI to the repo** as the canonical copy from day one (the
   resume-time reconcile then catches later drift).
5. **Emit the project-create + install card(s)** — one per surface, in the
   "open a session, paste this" family, naming WHERE / WHAT / RESULT in plain
   language. The SI installs as a **full wholesale paste, never a splice**
   (manual splice-edits are risky; re-issue on change is always a full
   replacement). The PAT is **guidance-only** — placed by the operator, never
   handled by the session.

**Two-project model (on Cowork).** A full engagement runs as **two
projects**: an **orchestration project** (the SI installed, core-load
enforced; it hosts the standing PRISM Desk and PRISM Meta lanes) and an
**execution project** (**SI-less, memory off, organization-only**) so the
ephemeral, PRISM-unaware vendor-execution runs have a home and their returns
land somewhere. Memory-off and a working folder kept separate from the
orchestration mirror are **recommended, not merely allowed** — they preserve
the execution run's clean-context independence (the
§{section.independent-validation-dispatch} premise: a shared SI or memory would
let run N inherit run N-1's framing). This graduates the
Claude-Project-at-Setup recommendation
(§{section.claude-project-as-setup-recommendation}) to active. The SI's
repo-canonical sync and opener machinery are framework-native from here, not
engagement-local interim.

#### Quick mode (`SETUP_QUICKMODE`)

A first-class **proportionality** option — the light end of the lean-Master
principle — for a task that wants *some* rigor but not the full apparatus (a
meeting brief, a quick analysis). Without it, the activation cost is paid in
full or the rigor is skipped entirely.

**Shape:** one Cowork session, `ephemeral` persistence, with **clean-context
sub-agent fan-out** for the work (one sub-agent per research / extraction /
drafting strand, returning only grounding facts;
§{section.lanes-roles-and-the-prism-ui}).

**Dropped (the heavy machinery):** `repo_backed` persistence; Master
accumulation and bump atomicity; multi-vendor equivalence dispatch and Vendor
Triangulation; multi-session handoff; the full seven-probe Setup and
three-layer readiness.

**Kept (the cheap, load-bearing rigor):** a **mini decision-brief** (two
lines — the audience and the decision it serves); a **lite Probe-1** (name the
handful of lenses that actually bear, plus any deliberately out of scope; no
coverage-saturation loop); and the **output-discipline gates on the
deliverable** — SP-16 (§{principle.SP-16}), SP-17 (§{principle.SP-17}), SP-18
(§{principle.SP-18}) — which are exactly the part that protects a brief from
being confidently wrong or mis-framed. The deliverable is self-contained
(SP-20, §{principle.SP-20}).

**Sub-agents need no envelope.** The triple contract exists for cross-vendor /
cross-session boundaries that quick mode does not cross; fan-out delegation is
free-form internal.

**Graduation (the load-bearing line).** When a quick brief turns out to be a
real engagement, it is promoted **without losing work**: the quick-mode output
**seeds a `repo_backed` Master** — the mini decision-brief becomes the Decision
brief, the lite lens pick seeds the Prompt Strategy, and the deliverable
becomes the first finding — and full Setup continues from there.

### 7.1 Library reference at Setup `[structural | stable]`
<a id="section-library-reference-at-setup"></a>

**Required Library source.** By default, orchestration fetches the bundled
Lens Library v0.16 (`lens/PRISM_lens_library.md`, tag `prism-lens-v0.16`)
on demand. A newer standalone Library version is used only when the
operator explicitly pins the project to it, overriding the bundled copy
for that session. Recommended: if a newer Library is used, live in the
Claude Project alongside the Master (see §{section.claude-project-as-setup-recommendation}).

**Probe 1 grades against Library entries.** Mechanics in §{section.probe-1-coverage-grading-iterates}.

### 7.3 Scope-Integrity Test (SIT) `[structural | stable]`
<a id="section-scope-integrity-test-sit"></a>

A lens's `minimum_scope_binding:` *states* what coverage requires; it does not
*enforce* it. Probe 1 (§{section.probe-1-coverage-grading-iterates}) can mark a
lens `fires-covered` on the strength of an enumeration that looks complete but
quietly scoped the question too narrowly. The **Scope-Integrity Test (SIT)** is
the enforcement layer: a coverage-time falsifier gate that the binding was
actually satisfied, not waved through. PRISM is an orchestration layer, not
running code, so SIT is a prompt-level adversarial question that gates coverage —
not a test runner.

**The failure it prevents.** The cleanest case is the category-vs-audience
substitution trap that §{lens.LL-D-008} "Compared to what?" already names in its
`failure_mode:`. A competitor scan scoped by *product category* — rather than by
*audience and job* — can converge on a confident "this is unique" finding while a
same-audience substitute in a different form factor (a hardware device, a manual
workflow, a do-nothing default) goes unnamed. Enumeration depth does not catch
this; more passes inside the wrong scope only harden the wrong boundary. The miss
is structural, so the check is structural — applied at the moment coverage is
claimed.

**Mechanism — a rigor ladder.** SIT runs at one of three rigor levels; the
operator escalates by stakes.

1. **Inline self-check (the floor — always on).** Before Probe 1 records
   `fires-covered`, the orchestrator restates the lens's `minimum_scope_binding:`
   as a yes/no falsifier and answers it in context: *has every clause been
   satisfied with evidence, or is any clause unmet?* Coverage is invalid without a
   structured falsifier-response. This is a **floor, not triangulation**: the same
   agent that did the enumeration is certifying its own work — the
   single-distribution trap SP-15 (Triangulation integrity,
   §{section.sp-15-triangulation-integrity}) warns about. Naming that limit
   honestly is part of the mechanism.
2. **Fresh-context probe (independent, single-vendor).** Dispatch the falsifier to
   a context that did *not* perform the enumeration. A fresh context catches what
   self-certification cannot, but it shares the orchestrator's training
   distribution, so it is the *minimum* independent rigor, not full triangulation.
3. **Cross-vendor probe (independent, cross-distribution).** Dispatch the falsifier
   to a different vendor. Distinct priors and failure modes make this **full SP-15
   triangulation** (§{section.sp-15-triangulation-integrity}) — the strongest
   level.

Levels 2 and 3 are operator-invokable today in a single chat: dispatch the probe
as its own prompt to a fresh context or a second vendor. A future `auto_drive`
execution driver (§{section.orchestration-driver-and-persistence-axes}) would only
*automate* that dispatch; it is not a prerequisite, and the SIT path carries no
`auto_drive` dependency.

**Home — lens-anchored, at coverage time.** SIT lives where coverage is marked:
the Probe 1 disposition gate (§{section.probe-1-coverage-grading-iterates}). It is
**not** a Monitor (those scan continuously) and **not** a Standing Principle (those
are posture). SIT is mechanical and condition-triggered — it fires exactly when a
lens is about to be marked covered — so it is anchored to the lens and the grading
step, not to the always-on machinery.

**Scope — a generic gate for all 27 lenses, plus optional sharpened probes.**

- **Generic gate (day one, every lens).** The falsifier is the lens's own
  `minimum_scope_binding:`, restated as the yes/no challenge above. Free,
  full-scope, runs immediately.
- **Sharpened per-lens probe (`scope_integrity_probe:`).** A lens may carry a
  `scope_integrity_probe:` field (§{section.lens-schema-what-orchestration-consumes})
  — a falsifier sharpened to that lens's known failure. When present it
  **overrides** the generic restatement for that lens. Additive: lenses without it
  use the generic gate.
- **First probe ships on §{lens.LL-D-008} "Compared to what?".** The one lens with
  a ground-truth worked miss carries the first hand-authored probe; its
  `scope_integrity_probe:` requires naming a cross-form-factor audience-job
  substitute the comparator set omits, or documenting its absence with rationale.
  The other 22 ride the generic gate. Sharpened probes accrete over time: a lens
  earns one when a live engagement surfaces a miss the generic gate let through.

### 7.4 Specialist-pass promotion
<a id="section-specialist-pass-promotion"></a>

The Library *is* the specialist enumeration. Each lens's `specialist_type:`
field names the practitioner role whose framing the lens channels.
Orchestration's Probe 1 grading promotes relevant entries as specialist
passes within the Prompt Strategy (e.g., "P3.4 — accessibility pass per
LL-D-002 "Can anyone use?", specialist framing: WCAG-qualified accessibility auditor").

### 8.1 Claude Project as Setup recommendation `[vendor-dependent | review-if: orchestration vendor changes]`
<a id="section-claude-project-as-setup-recommendation"></a>

Setup at P0.1 includes a recommendation to create a Claude Project as the
home for project state.

**Graduated under SETUP_ONBOARDING (v2.16.0).** This recommendation is now
active rather than parked: an engagement runs as the two-project model
(orchestration + execution) that Setup onboarding stands up — see
§{section.setup-onboarding-and-mode-selection}.

**Recommendation surfacing — when.**

- At P0.1, before the first probe iteration runs.
- *What's next* surfaces it as the first operator action:
  ```
  Setup recommendation: Create a Claude Project named "[subject] audit"
  (or per your naming convention). Reasons:
    - Project knowledge auto-attaches Master, Lens Library, and brief
      documents to every session you open inside the Project.
    - Past-conversation search becomes bounded to the Project, which
      pairs cleanly with SP-12 bounded-search disclosure.
    - Reduces re-attach friction across multi-session work.
  Proceed without a Project? [yes/no]
  ```

**Project contents at Setup completion** (recommended):

- `[project]_prism2.0_master_p0.1.md` (Master, current version)
- `PRISM_lens_library.md` (v0.16 or pinned tag)
- `[project]_brief.md` (subject brief)
- `[project]_prompt_strategy_p0.1.md` (current Prompt Strategy, optional —
  Master can carry this)
- Any subject-supplied reference documents

**Master in the Project** — operator workflow:

- Each orchestration session updates the Master.
- At session close, operator downloads the updated Master to the device.
- Operator uploads the new version to project knowledge (replacing or
  adding).
- Old version retained in project knowledge as audit trail (or archived to
  cloud drive per §{section.mobile-operator-survival-guide} MO-5).

This is a manual sync step under v2.0's plain-chat substrate. Auto-sync is
a roadmap adjacency.

**Fallback (operator declines or cannot create a Project).**

- Setup proceeds. P0.1 continues without Project.
- Every subsequent *What's next* emits an Operator hint: `Re-attach Master
  and Lens Library at session open.`
- The Project recommendation does not re-surface unless operator asks;
  framework respects the decline.

**SP-12 bounded-search disclosure interaction.** When a Project is in
place, Claude's `conversation_search` is bounded to the Project. SP-12
disclosure language adjusts:

> *"Searched within the [project name] Project. [Result]. The session may
> live outside this Project; confirm before I conclude."*

When no Project is in place, search covers non-project conversations.
SP-12 disclosure language:

> *"Searched outside any Project's scope. [Result]. The session may live
> inside a Project I cannot see from here; confirm before I conclude."*
