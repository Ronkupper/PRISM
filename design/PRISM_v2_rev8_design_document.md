# PRISM v2 — Design Document

**Status:** Design document (direction and rationale). Specification to follow.
**Date:** April 2026 (rev. 8)
**Supersedes:** Working notes dated 2026-04-19 and rev. 3 (retained as provenance; see Appendix B); rev. 4 through rev. 7. Absorbs `PRISM_v2_walkthrough_converged_dispositions.md` and `PRISM_v2_rev4_ship_plan.md` — both retired as parallel artifacts; retained on cloud drive as historical provenance.
**Applies to:** v2 and later. Projects born under v1.10.4 remain on v1.10.4 (see §10).

**Capture discipline:** Decisions are captured in this document at their current fidelity as they accumulate; completeness of phrasing or implementation detail is not a prerequisite for capture. Refinement happens in subsequent revisions. This is the practice the rev. 5.x → rev. 6 sequence followed and the posture future revs should default to.

---

## Summary

PRISM v2 rebalances the framework from specification-heavy to principle-heavy. The working assumption changes: a capable modern LLM, given a clear problem frame, handles most of the analytical work that v1.x built explicit specification around. Specification continues to earn its place where it does something the LLM cannot do alone — countering session-forgetting, catching failure modes the LLM does not feel, and producing reproducible deliverables — but the overall footprint is lighter.

Three architectural moves define v2:

1. **Orchestration/execution split.** Sessions separate into *orchestration sessions* (plan, converge, decide, update state, with the framework attached) and *execution sessions* (run a dispatched prompt without the framework, return structured findings). This is not new machinery — v1.x already does this inconsistently (Deep Research dispatch, Layer 2 cold synthesis). v2 picks the separation consistently and names it.

2. **Library-graded setup.** Setup reshapes from a waterfall into an iterative refinement loop whose central activity is grading the draft strategy against a reference catalog — the **PRISM Lens Library** — and closing omissions until coverage saturates. The Library is core v2 architecture, not a downstream consumer.

3. **Forward-compatibility commitments.** v2's default execution substrate is plain chat tools operated by a human, with orchestration on Claude. The architecture preserves pluggability for future desktop-mode execution variants (agentic orchestration, plugin-equipped sessions, vendor skills ecosystems) without committing to build them inside v2.

**v2 is mobile-first.** The framework is shaped so a default-substrate operator can run it end-to-end from a phone — prompt composition, attachment workflows, convergence sessions, state updates. Desktop operators get everything mobile operators get plus whatever desktop-only affordances exist; nothing in PRISM is mobile-hostile. Some design choices (file-based contracts, minimal reliance on copy-paste, compact terminology, output-size discipline) are calibrated to mobile constraints. This is a positive design commitment, not an accommodation. Details in §3.4.

**v2 ships in beta posture.** Tested substrate at release: Android (Samsung Galaxy S25+) mobile and major desktop web browsers. iOS and other Android OEMs are untested. The beta label is honest tradeoff-naming, not disclaimer fog — the framework works as designed on tested substrates; divergences on untested substrates are *report-worthy findings*, not defects. Coverage expands as real-use data accumulates.

This document captures direction and rationale. The v2 specification is a separate, later deliverable.

---

## 1. Background

PRISM is a methodology for running rigorous multi-dimensional research and analysis — product audits, market research, competitive landscape, company analysis, due diligence, investment memos, regulatory-surface reviews, and similarly-shaped projects where one question is too large for one prompt and needs multiple specialist passes that add up to a coherent whole. The v1.x line (currently v1.10.4, public) codified the framework through extensive trial-and-error on real projects. It works. v2 is a rebalancing, not a replacement — the analytical vocabulary, the Learnings Register, the structured convergence model, and many other v1.x components continue into v2 in recognizable form.

### 1.1 Why v2

v1.x accumulated specification through a long series of patches driven by real projects. Each patch was justified at the time; in aggregate, the framework grew heavier than the underlying capability now requires, and one material blind spot surfaced that no single patch could address. Three realizations drove the rebalancing:

1. **Substrate recognition.** A capable modern LLM is a judgment-applying collaborator, not a deterministic tool. Methodology techniques borrowed from software engineering — long-tail edge-case hardening, rigid interface contracts, specification-as-enforcement — assume a deterministic substrate and produce diminishing or negative returns when applied to one that applies judgment at every step. Trying to "close edge cases" by specification can produce worse outcomes than a clear brief and trust.

2. **Specification ceiling.** Much of v1.x's specification was doing work the LLM would do unprompted given a clear problem frame. The remaining specification — the part that genuinely adds value — is narrower than v1.x's current footprint suggests.

3. **Scope integrity is the highest-leverage correction.** Quality in any multi-dimensional analysis is bounded by the scope it starts from. v1.x's Setup process had no mechanism to grade a draft scope against a reference of material questions, so silently missing lenses (regulatory surface, scientific validity of core efficacy claims, structured adversarial evaluation) could survive all the way to the final deliverable without surfacing. The PRISM Lens Library is v2's answer to this, promoted to core architecture.

4. **Substrate tolerance is both-edged.** LLMs absorb inaccuracy gracefully where deterministic tools would error out. The positive side — a clear frame produces good work from imperfect specification — is what v2's principle-heavy lightness relies on. The negative side — mismatched substrate, stale instructions, and incomplete inputs produce usable-looking outputs instead of halting — is what v2's hygiene stack (operator scaffolding as a distinct tag category, flag-don't-guess posture, SP-12, SP-13) exists to counter. One substrate property, two design consequences; v2 leans on it rather than fighting it.

---

## 2. Design principles

### 2.1 Principle-heavy, specification-light — but not specification-zero `[structural | stable]`

v2's default is that a clear problem frame plus a capable LLM produces high-quality work. Specification earns its place where it does something the LLM cannot do alone. Three positive categories are accepted:

- **Working memory.** Countering the LLM's session-forgetting, both within a session and across sessions. Examples: the Master (persistent state file), monitors that flag conditions the LLM would otherwise drift past.
- **Hygiene.** Catching failure modes the LLM does not feel. Examples: unverified-claim tagging, discrepancy checks, provenance discipline, falsifier probes, Library coverage grading.
- **Reproducibility.** The framework's promise to external stakeholders. Examples: structured deliverables, audit trails, semantic versioning.

A fourth, negative category — **ceremony carried over from earlier thinking** — does not earn its place. It is trimmed.

### 2.2 A second axis: is the specification shaped correctly? `[structural | stable]`

A specification element can earn its place in one of the three positive categories and still be in the wrong shape. v2 evaluates every specification element against both axes:

1. Does it earn a positive category?
2. Is it shaped for its substrate — orchestration (framework-attached, lower cognitive load; explicit gates work well) vs. execution (no framework, analytical pressure; heavy machinery degrades)?

Three possible outcomes for any v1.x element: survive as-is, survive but relocate/reshape, or dissolve.

### 2.3 Scaffolding for the LLM vs. scaffolding for the operator `[methodological | stable]`

A useful single-question filter, applied before the formal two-axis walk: *is this element scaffolding for the LLM, or scaffolding for the operator?*

- **Scaffolding for the operator** — helps maintain consistency across time, supports handoff to others, reduces cognitive load at high-pressure moments. These typically earn their place; the question becomes *minimum-sufficient*.
- **Scaffolding for the LLM** — added because the framework distrusts the LLM's default behaviour. These are often suspect under v2; a well-framed LLM typically performs the move unprompted.

### 2.4 Category-error avoidance `[structural | stable]`

Software engineering's long-tail hardening rhythm — define requirements, implement, harden through edge cases — assumes a deterministic substrate. v2 explicitly rejects applying this rhythm to LLM-mediated work. The framework's job is closer to facilitation than to programming: put the operator and the LLM in the right posture toward each other at each moment, and accept that posture, not specification completeness, is what determines quality.

This is not a nuance. It reframes what "done" looks like for the framework itself.

### 2.5 Standing Principles introduced or extended in v2

Most v1.x Standing Principles carry forward (see §7.1). Three are introduced or extended in v2:

**SP-1 extended — Canonicity preservation.** `[operator-scaffolding | stable]` v1.x's SP-1 forbade Claude from silently reconstructing missing files from memory. v2 extends this to cover *offers* to reconstruct. Canonical artifacts — prompts designed in a sequence, specs other artifacts were built against, files other work references — have authenticity that matters beyond their content. Regeneration from a spec or from memory produces a new artifact, not the original, even when the content looks equivalent; downstream work that consumed the original may be silently contaminated by substituting a similar-but-different replacement.

Order of operations when a canonical artifact is missing:

1. Locate the original — session history, file system, past chats.
2. If location fails, surface specific consequences of regeneration: authenticity loss, schema drift, silent contamination of downstream work that consumed the original.
3. Offer regeneration only as a documented last resort, with consequences named.

Never frame regeneration as "deterministic" or "low-cost" unless it genuinely is. Source: the PRISM Lens Library status-check session, April 2026, where an uncritical offer to regenerate missing canonical prompts was rightly refused by the operator.

**SP-12 — Bounded-Search Disclosure (new).** `[operator-scaffolding | stable]` When Claude answers on the basis of a bounded retrieval — any tool call with implicit scope (past-conversation search scoped to a project, file listing within a directory, web search with date/site filters, project knowledge lookup, etc.) — the default posture is to disclose the bound. "I found no evidence" is insufficient; "I found no evidence *within [named scope]*; confirm before I proceed" is the v2 default.

SP-12 is operator scaffolding. The scope disclosure gives the human — who knows what may live outside the bound — the chance to catch what the bounded view couldn't see. It closes a recurring failure mode where a bounded search's null result gets reported as a global null, and the operator (if tired, new, or distracted) acts on the false reading. Not a Monitor that fires discretely; a posture held at every retrieval.

**SP-13 — Substrate Declaration (new).** `[operator-scaffolding | stable]` When PRISM is loaded in a session with a declared target environment (model, vendor, mode), the session verifies what it's actually running on before executing dependent work. If self-identification doesn't match the declared target, or can't be determined, the session halts and asks the operator rather than silently proceeding.

SP-13 closes the wrong-substrate failure class: operator clicks the wrong model in the picker, the handoff is written for a different model, and the session proceeds on the substrate actually loaded. Substrate tolerance (§1.1 realization 4) means the session produces usable-looking output even on the wrong substrate, so the mismatch doesn't surface unless explicitly checked. Scope: SP-13 fires in PRISM-loaded sessions (orchestration sessions, execution sessions carrying the Self-check block per §4.1.1). Ad-hoc sessions without PRISM loaded are outside its reach and remain an operator-discipline question. Source: the rev. 5 tagging session where Sonnet 4.7 executed a task the handoff had specified for Opus 4.7 with Adaptive Thinking; a prompt-body pre-flight check fired cleanly on Sonnet 4.6 in subsequent verification testing (April 2026).

---

### 2.6 Face-value naming `[methodological | stable]`

Specification elements carry their semantic at face value. When implementation detail accumulates behind a name that wasn't designed for it, the element becomes over-loaded — what the name says it is and what the machinery actually does drift apart, and the framework starts shipping silent assumptions.

The walkthrough reactions session surfaced a clean example: SF1 was named *Multi-LLM enrichment*, but in practice gated three pieces of v1.x machinery — a Discovery pass at Setup, an Enrichment Scoping subsection, and a five-role catalog — none of which the name was authored for. Reading the flag at face value (*"a binary multi-LLM on/off"*) rather than at-loaded (*"the bundle of things SF1 happens to gate today"*) was load-bearing in the disposition: the face-value semantic had no concrete v2 gating left, which closed the dissolution argument cleanly.

The principle generalizes: read the name at face value first; if the machinery has drifted from what the name actually says, that drift is itself a finding, separate from whatever decision is being made about the element. Periodic face-value review during specification work surfaces the overload before it compounds.

---

### 2.7 Direction-of-record absorbs parallel state at fold-in seams `[methodological | stable]`

When a design or planning artifact spawns a downstream artifact (walkthrough → dispositions; design doc → ship plan; spec → build handoff), the downstream's converged outputs absorb back into the direction-of-record at every fold-in seam, and the source artifact retires as an active input. The alternative — keeping the source live as a parallel tracker — accumulates fragmentation: state spreads across multiple files, sessions must verify N attachments instead of one, divergence between source and absorbed copy becomes possible, and the framework's own anti-pattern ("multiple Masters per project") starts operating on the framework itself.

The discipline at every fold-in: identify which of the source's outputs are converged enough to absorb (most), absorb them into named sections of the direction-of-record at body-text fidelity, and mark the source as historical provenance — kept on cloud drive (Appendix E.5) for audit-trail integrity, not re-attached as an active input.

Worked example. The walkthrough reactions session produced converged dispositions and a ship plan tracking phase status. The rev. 7 fold-in absorbed Parts 1–4 and Part 6 of the dispositions but kept Parts 5 (design gaps) and 7 (deferrals) live as a parallel artifact, on the rationale that *"those feed the spec session, not the design doc."* The ship plan kept revving (rev. 1 → rev. 4) as a parallel tracker. The rationale was wrong: design gaps that feed the spec session are still v2 design state, and ship-plan phase tracking is still v2 status. Both belong inside the direction-of-record (§13 Open design gaps for spec, §12 Status and roadmap in this rev). Rev. 8 corrects the fragmentation and retires both source artifacts.

Failure mode this prevents: pre-flight attachment counts that fail because the count is non-unitary. The bad spec session of April 2026 attempted to verify a four-attachment list, missed one, rationalized the proceed, and produced a contaminated 1,485-line draft. Under unit-attachment discipline, the pre-flight collapses to *"is the direction-of-record attached, yes/no"* — a check that does not fail on bubble-rendering ambiguity or count-priming gaps.

Discipline statement: at every fold-in seam, the direction-of-record absorbs converged downstream state and the source retires. New artifacts retire on absorption, not on completion of their own work.

---

## 3. Operating model

### 3.1 Default substrate

v2's default execution substrate is **plain LLM chat tools**: prose input, prose output, attached documents, with the operator driving cross-vendor orchestration by hand. No code running in the background, no agentic automation. Alternative execution modes (desktop-mode, plugin-equipped, automated cross-vendor) are roadmap adjacencies, addressed in §9. `[vendor-dependent | review-if: substrate shifts]`

**Orchestration is Claude-specific.** `[vendor-dependent | review-if: orchestration vendor changes]` v2's orchestration session is designed for Claude — tested against Claude Opus 4.6 and 4.7 — and uses Claude-specific machinery (`present_files`, `create_file`, `str_replace`, `ask_user_input`, Skill packaging, past-conversation search). The *methodology* (atomic prompts, two-layer convergence, Monitors, Master-file state, Learnings Register) transfers to any capable LLM; the *machinery* does not. Non-Claude orchestration is a graceful-degradation path, not a design target.

**Execution is vendor-deliberate.** Execution sessions run on whichever vendor the Prompt Strategy names for the role. Typical assignments: `[vendor-dependent | review-if: vendor X changes Y]`
- **Claude** for most analytical work, red-teaming, cross-source convergence within a prompt.
- **Perplexity** for live-web breadth, recency-sensitive fact checking, competitive scan.
- **Gemini Pro Deep Research** for long-context deep-research passes with many sources.
- **ChatGPT o-series** for alternative reasoning style on adversarial or synthesis-heavy prompts.

The execution-session contract is vendor-agnostic; the dispatch is deliberate per prompt.

Under the default substrate:

- Every check fires because something in a prompt or an attachment told the LLM to fire it.
- Every state persists because the operator (or an LLM instructed to) wrote it into a file that is re-attached next session.
- **The substrate is the operator's attention itself.**

Consequence: operator discipline is irreducible at certain touchpoints — re-attaching state files, invoking the right templates, copying findings back. The framework's job is to minimize these touchpoints, make them obvious when they fire, and fail loudly when skipped.

### 3.2 Operator target

v2 is designed for a **motivated non-practitioner**: technical enough to follow instructions, motivated enough to actually read what they are handed, but without the pre-loaded discipline of a full-time methodologist. The framework carries what the operator does not — not everything, but the high-leverage cues at the moments they matter.

### 3.3 Version pinning

A PRISM project pins to the version it was born under. `[structural | stable]` Framework updates do not apply mid-project. This removes cross-version drift as a design concern and lets v2 ship without backward-compatibility obligations to v1.x projects.

### 3.4 Mobile-first `[structural | stable]`

v2 is mobile-first. The framework is shaped so a default-substrate operator can run it end-to-end from a phone — prompt composition, attachment workflows, convergence sessions, state updates. Desktop operators get everything mobile operators get plus whatever desktop-only affordances exist; nothing in PRISM is mobile-hostile. Some design choices (file-based contracts, minimal reliance on copy-paste, compact terminology, output-size discipline) are calibrated to mobile constraints. This is a positive design commitment, not an accommodation.

**Why mobile-first matters.** LLM vendors' mobile clients have consistently lagged their desktop counterparts in basic operations: clipboard fidelity, file download, attachment handling, copy-to-clipboard from rendered outputs. Mobile operators have to work harder to close these gaps. A mobile-first framework does some of that work in the operator's stead — both through design choices (§4.1.1's file-based contract as one example) and through documented workarounds (Appendix E).

**Accepted asymmetries.** v2 is comfortable with provisions that serve mobile without costing desktop. The inverse — provisions that serve desktop at mobile's expense — is what v2 avoids. Some v2 mechanisms may be redundant on desktop (e.g., file-based delivery on a substrate where clipboard works cleanly) without being costly; that's an acceptable tradeoff.

### 3.5 Beta posture `[empirical | review-annually]`

v2 ships in beta. The tested substrate covers core workflows but is not comprehensive.

**Tested at release.** Android (Samsung Galaxy S25+) Claude native mobile app; major desktop web browsers. LLM vendors other than Claude are tested as execution substrates per the Vendor Selection process (§4.5).

**Untested at release.** iOS mobile. Other Android OEMs. Orchestration on non-Claude vendors (by design — see §3.1).

**Posture toward divergence.** Operators on untested substrates should treat divergences from documented behavior as *report-worthy findings*, not as framework defects. Coverage expands as real-use data accumulates. The beta label is honest tradeoff-naming, not disclaimer fog — the framework works as designed on tested substrates.

---

### 3.6 Claude as prerequisite; design authority without access gating `[structural | stable]`

v2 has at-least-Claude as a framework prerequisite. Orchestration is Claude-specific by §3.1; the orchestration session is where v2's machinery — atomic prompt composition, Vendor Selection, *What's next*, Monitor firing, Setup probes, convergence — actually runs. Without Claude, an operator does not have the substrate v2 was designed against. Documenting this explicitly removes ambiguity from the contract.

Beyond the prerequisite, v2 takes a **design-authority-without-access-gating** posture. The framework designs the optimal path — including which vendor to dispatch each execution prompt to, in what mode, with what hygiene — and informs the operator. It does **not** condition its design on what vendors the operator might have access to. Access is the operator's information; design is the framework's. Asking for access state upstream of package generation is ceremony that confuses the contract.

Operationally: when Vendor Selection (§4.5) recommends *"Gemini Pro Deep Research, Deep Research mode ON, extended thinking ON"* for a given prompt, the framework writes that into the Execution Envelope. The operator without Gemini access reads the recommendation, runs Claude (or another available vendor) instead, and reports the substitution back via the Output return. The framework absorbs the substitution at convergence rather than re-dispatching or asking upstream. (Substitution-absorption mechanics are spec-session work; the principle is captured here.)

Two consequences:

- Setup never asks the operator to declare available vendors. The Prompt Strategy specifies what the analytical work needs; the operator runs what they can.
- Recommendations carry rationale at face value (per §2.6) — what each dispatch does, not what its substitutions lack. Positive framing keeps the asymmetry between framework-design and operator-access from contaminating the rationale.

The prerequisite is hard (no Claude → not a v2 substrate). The vendor-access posture is soft (any execution-vendor substitution is absorbed downstream, not gated upstream).

### 3.7 Context-pressure framework — telemetric, not arithmetic `[structural | stable]`

Context handling under v1.x was treated as arithmetic: declared budget × threshold percentage → monitor fire. v1.x's own Context Pressure Bands rationale acknowledged the fiction — *"LLMs are bad at estimating their own context usage; a specific count like '~142K tokens' looks precise but isn't."* The calibration chain is unreliable at every link: declared value is nominal not empirical, actual pressure is content- and task-variable, self-reporting is approximate, UX signals lag.

v2 replaces declared-budget arithmetic with a **telemetric framework**: the framework observes multiple weak signals continuously, compounds them into a strong read, surfaces qualitatively via bands, and fires protective machinery on band state rather than threshold percentages.

**Signal catalog (seven sources, compound read).** Volumetric: attached content size (estimable); conversation accumulation (estimable, monotonic in-session); reasoning accumulation (indirect, correlates with conversation shape). Behavioral: quality-degradation self-check (noisy but real; compounds with others); task-completion friction (edits not applying, broken cross-links, repeated questions about established state); platform UX signals (compaction events, warnings, response-time extension); operator-reported signals (live sensor; honest even when noisy).

**Bands.** Carrying forward from v1.10.4 as the reporting surface: 🟢 comfortable; 🟡 getting warm; 🟠 curate now; 🔴 migrate. Band assignment is judgment-applying rather than arithmetic — imprecise in a different way than numbers were, but honest about what the estimate is worth. Tier-agnostic by construction: 200K-budget sessions hit bands sooner, 1M-budget sessions hit them later, machinery response is identical. The framework never asks what tier the operator is on.

**Protective machinery fires on band state.**

- 🟢 *Comfortable.* No intervention. Advisory migration *available* at natural seams (convergence complete, phase boundary, major deliverable shipped).
- 🟡 *Getting warm.* Continuous-curation posture. Advisory migration *recommended* at the next natural seam.
- 🟠 *Curate now.* Active curation. Advisory migration *strongly recommended*; the framework actively finishes current curation so a seam arrives.
- 🔴 *Migrate.* Migration is the correct next action. The framework produces the handoff.

**Failsafe recovery as design posture.** Telemetric reads are imperfect. The answer is not chasing precision — it is making every pressure-related decision recoverable. Continuous-state infrastructure (Master continuously current, *What's next* always written, curation as continuous posture not fire-drill) means misreads are low-cost. Asymmetric bet: if the framework misreads, the operator loses nothing (migrate, fresh session inherits, work continues); if the framework reads correctly, the recovery infrastructure wasn't needed but wasn't costly either.

**Defensive migration at natural seams.** Migration is planning, not rescue. Advisory at 🟢 seams; recommended at 🟡; strongly recommended at 🟠; correct at 🔴. The continuous-Master + continuous-*What's next* infrastructure is what makes this a planning posture rather than a fire-drill — there is always a recoverable handoff state, regardless of which band the framework is currently reading.

This framework is what M5 (now absorbing the retired M12) fires against — see §7.2. Specification of signal-weighting, band-transition hysteresis, and operator-reported-signal capture mechanics is spec-session work (design-gap items 14–19 in the converged-dispositions artifact).

---

## 4. Architecture

### 4.1 Two session types

v2 splits sessions into two architecturally distinct types.

**Orchestration sessions.** The operator works with Claude, with the framework document attached. The full set of principles, specifications, and state is available. Orchestration sessions handle: setup, convergence across execution findings, adaptation, Layer 2 synthesis, the *What's next* decision at each turn's close, and all Monitor firing.

**Execution sessions.** A dispatched prompt runs on whichever LLM vendor the strategy specified. The framework document is **not** attached. The session has only what the prompt carries. Its job is pure analytical execution; it returns structured findings in a defined shape.

Continuity with v1.x: this is not a new architecture. v1.x already runs Deep Research as de facto execution (dispatch the prompt, collect outputs, bring them back for orchestration-side consolidation), and Layer 2 cold synthesis as de facto orchestration (full framework attached, all findings in hand). v2 picks the separation consistently and names it.

Reasons to make the split explicit:
- In v1.x's cases where convergence ran during execution (SP-3), it was working against a framework authored primarily for Claude while executing on an arbitrary vendor. Moving convergence to orchestration removes this silent liability.
- Orchestration sessions can batch across multiple execution outputs when dependencies allow. 1:1 session mapping was an artifact of v1.x architecture, not a requirement.
- The framework document does not need to travel to every vendor on every dispatch — a source of context pressure and vendor-portability friction in v1.x.

### 4.1.1 The execution-session contract

Execution sessions must receive instructions in a shape they can act on without orchestration-side framework context, and must return findings in a shape orchestration can read without re-interpretation. v2 codifies a triple contract: an **Execution Envelope** on the inbound side, an **Execution Self-check** between envelope and task body, and an **Execution Output** on the outbound side. `[structural | stable]` All three are visually distinctive, self-contained blocks embedded in the prompt and the output respectively. The Self-check operationalizes SP-13 (§2.5) inside the execution-session context.

#### Inbound: the PRISM Execution Envelope

Every dispatched execution prompt begins with a structured block naming the vendor, mode, tools, session hygiene, attachment manifest, and expected output filename. The operator reads it before dispatch and acts on it; the vendor session reads it at the top of the prompt and runs accordingly.

```
━━━ PRISM EXECUTION ENVELOPE ━━━
Prompt ID:          P2.3 — Regulatory Landscape
Project:            Solace Audit
Master version:     solace_audit_prism2.0_p2.2
Vendor:             Gemini Pro Deep Research
Mode:               Deep Research ON, extended thinking ON
Session hygiene:    fresh session, no project attached, web search ON
Attachments:        solace_brief.md, regulatory_context.md
Expected output:    solace_audit_p2.3_gemini.md
Operator hints:     Save output to cloud drive after download, before
                    switching to the next vendor (see E.5). On Samsung,
                    expect indexing delay on the downloaded file (E.1).
━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[atomic prompt body]
```

The Envelope serves three purposes:

- **Operator scaffolding at dispatch.** The operator knows which vendor, which mode, which tools, which session hygiene — no memory burden, no reconstructing instructions from a prior conversation. The "run Claude outside any project so it isn't distracted by project memory" sort of guidance lives in the Session hygiene field, not in the operator's head.
- **Vendor instructions at top of prompt.** The vendor session sees a standardized header it can parse, regardless of which vendor it is.
- **Dispatch-ready shape.** Vendor Selection (§4.5) produces the envelope; orchestration hands it to the operator as a ready-to-paste block.

**Operator hints (optional field).** The Envelope carries an optional `Operator hints` field for in-context cues keyed to the specific dispatch — pointers into Appendix E, artifact-survival moves, vendor-switch gotchas. Emission discipline: hints fire only when a cue applies to this dispatch (routine dispatches carry no hints, preserving signal-to-noise); one line per hint; pointer to the relevant Appendix E entry rather than an inline essay; no hint that duplicates a Monitor firing — the categories stay clean.

Hints are best-effort calibrated to the operator's environment (mobile vs. desktop, specific vendor client, tested substrates per §3.5). When the calibration target is non-obvious from context, hints carry a brief attribution — e.g., *"(Claude mobile, Samsung)"* — so an operator on a different substrate sees the mismatch rather than acting on a miscalibrated cue. Missing on an untested substrate is expected and benign under §3.5's beta posture; the attribution makes the miss self-diagnosing rather than silently confusing.

Secondary benefit: the field functions as a lightweight education surface. Operators new to multi-vendor LLM workflows encounter best-practice cues at the moment of application rather than in advance-of-need documentation they'd have no reason to read. This is a real part of why the feature earns its place — the same mechanism that surfaces a survival-guide cross-ref also carries operating knowledge forward to operators who haven't yet built it up themselves.

This names and generalizes work the Session hygiene field was already doing informally in v1.x and rev. 6.1 (*"run Claude outside any project..."* is itself a hint); v2 gives every such cue a consistent home and makes the practice discoverable. The appendix is the catalog; the Operator hints field is the just-in-time surfacing of whichever entries apply to *this* dispatch.

#### Pre-execution: the PRISM Execution Self-check

Between the Envelope and the task body, every dispatched prompt carries a Self-check block that operationalizes SP-13 (§2.5) inside the execution session. The session verifies the substrate it's actually running on against what the Envelope declared, before executing the task.

```
━━━ PRISM EXECUTION SELF-CHECK ━━━
Before doing the task:

1. State what model/vendor you are and what session state
   you can introspect (mode, thinking setting, tools enabled).
2. Compare to the Envelope's Vendor and Mode fields above.
3. If anything does not match, or if self-identification
   is incomplete, STOP. Report what you found and ask
   the operator whether to proceed, switch sessions, or
   abort. Do not proceed to the task silently.
4. Proceed only if (a) the substrate matches, or (b) the
   operator has explicitly confirmed to proceed despite
   mismatch.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

The Self-check serves the wrong-substrate failure class: handoff written for Opus 4.7 Adaptive dispatched to a Sonnet-no-Adaptive session, for example. Substrate tolerance (§1.1 realization 4) means the session would otherwise produce usable-looking output on the mismatched substrate — the Self-check forces the mismatch into the open.

Operator-empirical footing: verification testing (April 2026) confirmed Sonnet 4.6 honors the Self-check block cleanly — self-identifies, hedges on state it cannot confirm, halts on mismatch. Multi-vendor verification on Gemini, ChatGPT, and Perplexity is pending; the Self-check mechanic is calibrated to Claude-family adherence at rev. 6, and the `[empirical]` tag is honest about this.

Scope honesty: the Self-check fires inside PRISM-dispatched sessions that carry the block. Ad-hoc sessions without a PRISM envelope cannot be protected by a mechanism they don't load; that's a separate operator-discipline question, not an SP-13 or Self-check failure.

#### Outbound: the PRISM Execution Output

Every execution session ends with a post-outcomes production step: after the analytical work is done, the session produces an `.md` file with the findings wrapped in a matching PRISM Execution Output signature. The file is the deliverable; chat rendering is ephemeral.

```
━━━ PRISM EXECUTION OUTPUT ━━━
Prompt ID:       P2.3 — Regulatory Landscape
Project:         Solace Audit
Master version:  solace_audit_prism2.0_p2.2
Vendor:          Gemini Pro Deep Research
Mode:            Deep Research ON, extended thinking ON
Schema version:  output-v1
Date:            2026-04-24
Prompt hash:     a3f41d (first 6 chars)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[findings content]

━━━ END PRISM EXECUTION OUTPUT ━━━
Operator next:   Download this file as
                 solace_audit_p2.3_gemini.md.
                 Attach to orchestration session
                 as Layer-1 input for P2.3.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

The `Schema version` field is new in v2. It lets orchestration's Layer-1 convergence detect schema variance across vendor outputs — an issue surfaced by the PRISM Lens Library synthesis sessions, where different vendors produced structurally different entry shapes that would have gone unflagged without explicit versioning.

The production-step design moves three operator-burden tasks into the execution session:

- Content crafting and signature insertion happen inside the vendor session, while context is fresh and vendor tools (Claude's `create_file`, ChatGPT Canvas, Gemini's file generation) are available.
- Filename assignment follows the convention stated in the Envelope, removing naming drift.
- Operator workflow collapses to *download the file and attach it next*, rather than extract, reformat, save, and upload.

Vendor capability varies: Claude produces files cleanly; ChatGPT Canvas produces them reasonably; Gemini Deep Research has its own artifact surface; Perplexity's file-creation is limited. Where a vendor cannot produce a file, fall-back behaviour is to render the signed content between delimiters for operator copy — with explicit warning that this fallback path has the failure mode described below.

#### Why v2 delivers via file, not paste

Empirical testing (April 2026, three-vendor matrix: Gemini mobile, ChatGPT web, ChatGPT mobile) surfaced clipboard fidelity issues that made paste unsafe as a delivery path. Specifically: ChatGPT mobile silently stripped heading markers, code fences, and YAML fences while preserving raw text; YAML blocks still parsed but fence-dependent processors found zero blocks. Same vendor on the web client produced only cosmetic-quote deltas. Gemini mobile preserved bit-identical content.

One clean leg does not generalize. Clipboard fidelity is a cross-product of vendor × client × platform, not a property of the vendor alone, and the set of broken combinations can shift with any client update.

**v2's execution contract uses file-based delivery in response to what the testing surfaced.** `[empirical | review-if: vendor behavior changes]` This is not a framework limitation; it is baked-in learning from extensive testing. The production step (above) produces a file, not a rendering — the signature survives every sane export path because it lives inside the file the operator attaches. An integrity-check harness exists as a diagnostic for suspicious attachments or new-vendor pipeline validation, but it is not a gate on normal operation; if the operator has to run a harness before pasting, they should just attach.

On substrates where clipboard fidelity is not an issue (some desktop web workflows, for instance), the file-based contract is redundant rather than costly — the accepted asymmetry per §3.4. Mobile-first design choice that happens to be desktop-neutral.

#### Why the contract is load-bearing

Taken together, Envelope and Output resolve several v1.x failure modes:

- **Export survival.** The Output signature embeds identity in content; filename mangling during vendor export is no longer a state-loss event.
- **Cross-vendor state reconstruction.** Orchestration attaches signed outputs; the Master's state is rebuildable from its attachments rather than from cross-vendor conversation search.
- **Schema variance detection.** The `Schema version` field lets Layer-1 convergence flag incompatibilities at ingestion rather than discovering them during analysis.
- **Operator-extraction friction.** The 10-minute-per-vendor extraction pain of v1.x collapses to a download when the vendor supports file creation.
- **Clipboard-stripping class of failure.** Eliminated by construction — the contract never asks the operator to paste body content.

The paired Envelope/Output contract is part of the atomic prompt template (§7.1) and produced by Vendor Selection at dispatch (§4.5).

### 4.2 Shared state: the Master

State that must persist across sessions is written down. Orchestration sessions read and write it. Execution sessions read it only when a specific prompt needs extracted findings as evidence.

v2 names this file the **Master** — as in master record, the authoritative canonical version from which derivatives are cut. The filename convention is `[project_name]_prism[version]_master_[phase-derived versioning].md` (e.g., `solace_audit_prism2.0_master_p2.3.md`). The Master is a single file by principle; the plain-chat substrate (§3.1) makes file-based persistence the only available mechanism for cross-session continuity.

The Master does more than carry state. It is where **incremental convergence lands**: as execution findings arrive, orchestration's Layer 1 integration writes them into the Master's findings sections with provenance. This is what makes it possible for a later execution session to read one specific extracted finding as evidence without re-digesting the whole project. Converged state in the Master is the form execution sessions consume; raw outputs are the form they produce.

The Master scales with the project. A short dispatch sequence (three or four execution sessions, no convergence rounds, no Layer 2) keeps it lean — a few sections, a status table, a short Changelog. A 30-session audit with multiple convergence rounds and stakeholder deliverables builds out the full register stack. State infrastructure has costs as well as benefits; v2's default is *whatever persists, in the minimum shape that preserves it*, not *every register populated regardless of whether it earns its place*.

The v1.x Learnings Register carries forward inside the Master. It is the section that literally accumulates wisdom across projects — the living culture that survives every bake and grows richer each cycle. The sourdough analogy lives here cleanly: the Register is a starter culture for the framework itself.

### 4.3 *What's next* as a first-class artifact `[structural | stable]`

The closing act of every orchestration session computes and writes a *What's next* artifact. This resolves TRI-21 (raised in the v1.10 Claude QA review): v1.x's prompt-ID-as-progress-marker was a single implicit pointer, which produced different answers from different Claude sessions when state was messy (rerun overdue *and* M6 HIGH *and* Adaptation pending *and* next canonical step all live).

v2's *What's next* artifact carries:

- **Current state summary.** Active prompt (if any), open Rerun Register items, pending Adaptations, most recent Monitor fires.
- **Candidate list, priority-ranked.** Not a single pointer — every candidate next-action surfaced explicitly (Rerun Register overdue, M6 HIGH unresolved, Adaptation pending approval, next canonical step, Layer 2 readiness if M11 conditions met, etc.), ordered by a priority ladder.
- **Recommended next action with rationale.** Claude's pick plus why.
- **Escalation to operator on ties.** When multiple candidates are live and roughly equal priority, surface them and ask the operator (SP-9 compatible — silence is never consent).
- **Dispatch-ready payload.** If the next step is an execution prompt, the full atomic prompt with execution envelope and signature header ready to paste.
- **Operator hints, when applicable.** In-context cues keyed to the upcoming action — Appendix E cross-refs, artifact-survival moves, session-close moves. When the next action is an execution dispatch, hints ride inside the Envelope's `Operator hints` field (§4.1.1); when the next action is not a dispatch (review a convergence output, ratify a strategy, save Master to cloud before closing the session), hints surface on *What's next* directly. Same emission discipline as the Envelope field: fire only when a cue applies, one line each, Appendix E cross-ref when applicable, substrate calibration attributed where non-obvious, no duplication of Monitor output.

*What's next* is written at the close of each orchestration session and lives on the Master. It replaces the hygiene role that v1.x's GATE-1 was performing between prompts.

### 4.4 Forward-compatibility commitments `[structural | stable]`

v2's default execution substrate is plain chat (§3.1). The architecture is designed such that future execution modes plug in as *alternative runtime layers* above the same core contracts, without reworking what v2 builds now.

- **Execution-session contract is vendor-agnostic by design.** A dispatched prompt specifies what it needs and returns structured findings with the standard signature (§4.1.1). Automated orchestration — Cowork + Computer Use or any equivalent — can replace manual copy-paste dispatch without changing this contract.
- **The attach map includes a tools slot per execution session.** In v2's default mode, this slot specifies web search on/off and any recommended capabilities. The slot's existence is architectural, not just operational — it reserves the structured space where plugins, skills, or agentic tool-surfaces get named when desktop-mode extensions arrive.
- **Execution-mode is a first-class setup flag.** v2 defaults to *manual plain-chat mode*. The flag's existence reserves the namespace for future modes (desktop-mode with plugins, automated cross-vendor, etc.) rather than forcing them into a later architectural rewrite.

These commitments cost v2 very little now and prevent a later architectural forklift. See §9 for the roadmap items they support.

### 4.5 Vendor Selection at dispatch

Rather than a statically-maintained vendor-to-role mapping reference (which ages faster than the framework can patch it), v2 runs **Vendor Selection as an orchestration-time live step**. `[methodological | review-if: vendor landscape changes]` Whenever an execution prompt is about to be dispatched, the orchestration session runs a fresh check — current best practice, current vendor capabilities, current platform quirks — before finalizing the execution envelope.

The step has three parts:

**1. Prompt/context-engineering refresher.** Orchestration verifies current state on the specific decision — is Adaptive Thinking still behaving as expected on Opus? Is Perplexity still the right call for live-web breadth, or has a newer vendor taken that role? Are there known recent issues with Gemini Deep Research? This is SP-10 continuity from v1.9.1 — *verify current state before recommending* — applied at dispatch time, not left to stale training priors.

**2. Structured outcomes flow into the prompt strategy.** When the Vendor Selection check produces a specific, confident recommendation — *"Gemini Pro Deep Research, Deep Research mode ON, extended thinking ON"* — that configuration is embedded in the execution envelope and the signature header. The operator sees what was chosen and why. No decision required.

**3. Soft outcomes surface as a recommendation bubble.** When the check produces a judgment that shouldn't auto-apply — *"Vendor X is the usual choice but has had reliability issues this week; Vendor Y is a reasonable fallback if you have access"* — it appears as a non-blocking note attached to the prompt. Operator reads, agrees or overrides. This preserves the flag-don't-assume discipline (SP-5/SP-9 lineage) while not demanding operator decisions on settled questions.

Vendor Selection is a dedicated orchestration-layer step, not a background behavior. It has a visible output; the operator can see what was checked and what was decided.

---

## 5. Setup, reshaped

### 5.1 From waterfall to Library-graded iterative refinement

v1.x setup was a waterfall: complete Steps 1–N in sequence, secure operator approval at the end, route any later strategy change through a separate adaptation process. v2 replaces this with iterative refinement whose central activity is **grading the draft strategy against the PRISM Lens Library** (§6) and closing material omissions until coverage saturates.

Setup iterations are numbered **P0.1, P0.2, …** with no artificial cap. Each iteration produces a revised draft strategy; the probes in §5.3 surface what the revision missed.

### 5.2 Three-layer readiness

All three must clear before setup concludes:

1. **Structural completeness.** Every planned prompt has a single objective, output format, dependency list, attachment map, enrichment decision, and execution envelope. Mechanical; easy to verify.
2. **Library coverage saturation.** Every applicable lens from the Lens Library is either covered by at least one planned prompt, or explicitly and defensibly marked as out of scope with rationale. Saturation is signalled when two consecutive iterations produce no material change to coverage or strategy.
3. **Operator ratification.** The operator confirms the strategy matches intent.

### 5.3 The probe set (seven probes)

Seven probes run across setup iterations. Four iterate against the draft; three run once as readiness checks.

**Probe 1 — Coverage grading (iterates).** Grade the draft against the Lens Library's universal lenses plus any domain-triggered lenses. Library-driven. Disposition is tri-state, not binary:

- **Fires-covered.** The lens applies to this subject and the draft already covers it. Silent pass.
- **Fires-uncovered.** The lens applies and the draft does not cover it. Surfaces as a flag; closed by adding coverage to the next iteration.
- **Doesn't-fire.** The lens does not apply to this subject. Silent, with rationale captured so the non-applicability is traceable.
- **Fires-maybe.** Applicability or coverage is ambiguous — the lens might apply, or might already be covered implicitly, but the judging LLM cannot resolve it confidently. Two operator paths close a *maybe*:
  - **Dig-in.** The LLM does targeted research on the lens/subject intersection — web search, on-the-fly specialist framing synthesis — and produces an expanded lens framing or a scoped specialist pass to add to the strategy.
  - **Opt-out.** Documented exclusion with rationale.

Both dig-in and opt-out satisfy §5.2 readiness layer 2 (Library coverage saturation). A *maybe* left unresolved at readiness-check time is itself a flag.

*Failure mode to watch: operator-fatigue if too many maybes surface. Mitigation: the judging LLM resolves clear cases silently (covered or doesn't-fire with obvious rationale) and escalates only genuine ambiguity. Empirical calibration post-release — see §11.*

**Probe 2 — Adversarial (iterates).** Hunt for silent omissions and under-scoped treatments, informed by the Library and by domain context. Library-driven. Works well multi-vendor — divergence between independent adversarial passes is signal.

**Probe 3 — Stakeholder (once).** Does the strategy answer what the stakeholder actually needs to decide?

**Probe 4 — Pre-mortem (iterates).** Imagine execution completes. How would the finding fail to answer the original question?

**Probe 5 — Consolidation (once).** Overlapping prompts, prompts that should split or merge.

**Probe 6 — Falsifier (once).** What findings would invalidate the thesis?

**Probe 7 — Domain practitioner survey (iterates early).** What do practitioners, researchers, and serious analysts of this specific domain actually investigate? What lenses does the domain's own literature and practice treat as default? This probe imports domain-external signal that the Library (general catalog) cannot carry. It also asks whether an authoritative canonical source exists for the domain (§8.2) — if yes, the strategy brings it in as primary evidence. Multi-vendor is recommended; different vendors have different exposure to domain-specific literature.

Iteration floors and ceilings are tentative pending real-use calibration: minimum 2 iterations (a single pass cannot saturate); at 4, flag as *something structural may be wrong — operator intervention*. `[empirical | review-annually]`

### 5.4 Setup artifacts (instance-specific)

Setup produces more than a ratified strategy. It produces a set of **instance-specific artifacts** — populated from the project's brief and from the probe outputs, not drawn from the Lens Library — that downstream probes and the Library's lenses grade *against*. These are not material-question lenses; they are the project's own specifics rendered in structured form.

The core artifacts are:

- **Decision brief.** What the stakeholder actually needs to decide, in the stakeholder's own terms (populated primarily from Probe 3 output).
- **Stakeholder register.** Who else has a decision or outcome stake in the subject (populated primarily from Probe 3 output).
- **Claim inventory.** The specific claims the subject makes — efficacy, compliance, positioning — that the strategy will investigate.
- **Jurisdiction map.** Regulatory, geographic, and platform jurisdictions the subject operates within (populated primarily from Probe 7's domain-practitioner survey).

These artifacts are **relocated from what earlier revs treated as a Library tier** (the former "subject-template scaffolds"). The relocation recognizes that they are instance-specific outputs of Setup probes, not reusable catalog entries. The Library carries lenses (material questions that travel across projects); Setup carries artifacts (the specific answers this project's brief produces for those questions). Lenses grade the strategy's coverage; artifacts are part of what the strategy works on.

Artifacts are populated during Setup iteration — they accumulate as Probes 3 and 7 run — and stabilize alongside the strategy at the P0 → P1 boundary (§5.5). When convergence surfaces material change to the strategy, the artifacts may revise with it.

### 5.5 Strategy stability, not strategy freeze

At the P0 → P1 boundary, the strategy shifts from "iterating freely" to **presumed stable, revisable at convergence**. Execution proceeds (dispatched prompts start running); when orchestration convergence produces a finding that materially changes the strategy — a premise invalidation, a newly-surfaced domain area, a falsifier hit — the strategy adapts. This is lighter than v1.x's major-bump Adaptation ceremony and softer than a hard freeze.

The attach map travels with each prompt. When a prompt adapts at convergence, its attach map adapts with it.

---

## 6. The PRISM Lens Library

The PRISM Lens Library is core v2 architecture. It is the reference against which setup grades coverage (§5), and it is the mechanism by which v2 addresses scope-integrity failure — the highest-leverage quality lever for any audit or analysis project (§1.1).

### 6.1 What it is

**The Library is a reference catalog, not operational machinery.** Entries do not run at runtime; they sit in the catalog and are consulted when the judging LLM grades a draft strategy's coverage (§5.3, Probe 1). An entry that doesn't apply to a given subject costs nothing — it simply doesn't fire. This asymmetry matters for the inclusion bar: an entry earns its slot if it *could catch a silent omission on some real subject*, not if it *earns its slot against checklist fatigue* (which would be the bar for operational gates).

A catalog of material-question categories ("lenses") that any serious analysis of its subject type should address. Each entry carries:

- A **plain-English operational question** (e.g., "Who gets hurt if this ships?"), not an academic framework label. An operator reading the entry on a phone at scope-definition time grasps what the lens asks in one read.
- A **trigger rule** — always-on, detection predicate, or brief-derived. The trigger is a hint to the judging LLM about when the lens likely applies; applicability is decided under Probe 1 grading (including the tri-state disposition for ambiguous cases), not by deterministic predicate evaluation.
- An **evidence class** — observation, document, trace, probe, cross-check, expert interview, empirical test. Reproducible by a third party.
- A **specialist type** — the kind of practitioner whose framing the lens channels (e.g., *regulatory counsel*, *accessibility auditor*, *clinical reviewer*, *security researcher*). Open taxonomy, domain-appropriate term; entries use whatever label the domain's own practice uses. The Library itself is the specialist enumeration — the judging LLM promotes relevant entries as specialist passes under Probe 1 grading.
- An **optional anchor to a testable external specification** — populated only where the external spec mechanically grades the lens (e.g., WCAG success criteria, OWASP ASVS requirements). Rare; most entries have no such anchor. When populated, anchored entries carry a **`last_verified:`** field (date of the last check against the current version of the external spec) so that staleness of the anchor surfaces as a first-class maintenance signal rather than invisible drift.
- **Provenance** — external frameworks whose structural patterns informed the entry's design, cited at framework-name level only, not as runtime rubrics.
- A **specific failure-mode description** — what goes wrong concretely if the lens is silently missing from a scope.

**Lens = triple.** `[structural | stable]` A lens is the triple (material-question, evidence-class, specialist-type). The same subject surface can legitimately host multiple lenses when the triples differ — e.g., "data retention" viewed through a regulatory-counsel lens (evidence: statute/regulation citations), a security-researcher lens (evidence: trace of data flow and controls), and a consumer-rights-advocate lens (evidence: user-visible policy and surfaces) are three distinct lenses, not one. Partitioning the catalog by subject surface collapses research paths before the subject is even in view; the triple is what keeps the distinctions legible.

Entries are organized into two tiers: **universal lenses** (always applicable) and **domain-specific lenses** grouped into **domain packs** (fire when triggered by attributes of the subject). The earlier "subject-template scaffolds" tier dissolves — those artifacts relocate to Setup (§5.4) as instance-specific outputs of Probes 3 and 7, not catalog entries.

### 6.2 How it integrates into v2

The Library is the reference the setup phase (§5) grades against. Probes 1 (Coverage grading) and 2 (Adversarial) are Library-driven. Setup readiness cannot clear without Library coverage saturation.

### 6.3 Provenance discipline `[structural | stable]`

External frameworks (WCAG, ISO, OWASP, NIST, Cochrane, PRISMA, etc.) are cited as **provenance** — what informed the entry's design — not as runtime grading rubrics. Narrow exception for lenses with genuinely testable external specifications, which are anchored explicitly with version pin and access mode.

### 6.4 Framework-independence — emergent, not designed-for

v2 is the design target for the Library. Standalone usability by other frameworks is a **likely emergent property** of a well-shaped catalog — the fields (plain-English question, trigger, evidence class, specialist type, provenance, failure mode) are generic enough that other frameworks can consume entries without v2-specific machinery — but it is not designed-for and is not something the Library's structural decisions optimize for. Release notes frame the Library accordingly: produced for v2, shaped such that reuse elsewhere is plausible but unwarranted-by-design. If reuse materializes, that's a bonus; if it doesn't, nothing in the Library was compromised to pursue it.

This is a shift from rev. 6.4's posture, which framed framework-independence as an aspirational design property. Rev. 6.5's reframe recognizes that the Library's center of gravity is its fit to v2, and that framing reuse as aspirational set up a quiet tension between "shape for v2's needs" and "shape for generality." The emergent framing resolves the tension without forbidding the reuse case.

### 6.5 Production status

The PRISM Lens Library v0.9 shipped on 2026-04-24 — tagged `prism-lens-v0.9`, merged to `main`, public; canonical file at `lens/PRISM_lens_library.md`. The v2 ship dependency declared at rev. 6.5 is satisfied. Library refinement past v0.9 continues via the Update-session mechanic in §6.6. Original rev. 6.5 framing — *"v2's ship readiness is coupled to Library v0.9 availability"* — preserved here as historical posture; the dependency was real, and was met.

### 6.6 Currency maintenance `[methodological | stable]`

The Library's entries cite external frameworks (WCAG, ISO, OWASP, NIST, Cochrane, PRISMA, clinical guideline bodies, and others) as provenance (§6.3), and a narrow subset anchor to testable external specifications (§6.1). Both types of citation age. External frameworks revise — sometimes materially. Without a maintenance surface, staleness accumulates invisibly: a lens citing WCAG 2.1 after WCAG 3.0 has shipped, or anchored to a superseded OWASP ASVS version, still fires and still grades, but its grading reflects an older world than the subject does.

v2 handles this with a **two-tier mechanism**: lightweight per-project *point refresh* during Setup, and rare standalone *Update sessions* that revise the canonical Library file.

**Point refresh (per-project, in Setup).** The judging LLM extends its applicability reasoning (Probe 1) to include currency of each fired lens's `informed_by:` citations and `rubric_anchor` (where present). Three dispositions per lens:

- **Fresh-enough.** Citations are current or near-current; no action.
- **Stale-but-refresh-inline-in-prompt-strategy.** The cited version is outdated but the lens is still the right question; the per-project prompt strategy is updated inline to reference the current version of the framework. Canonical Library file is not modified.
- **Stale-and-pattern-accumulating.** The citation is outdated and this is the Nth time the judging LLM has noted it across projects — an advisory signal that the canonical Library entry should be revised, not just the per-project strategy.

Point refresh is cheap because it rides on reasoning the judging LLM is already doing for Probe 1. Its output is confined to the per-project prompt strategy; the canonical PRISM file is read-only from its perspective.

**Update session (standalone, rare, operator-gated).** A dedicated session whose contract is *PRISM file in → PRISM file out, nothing else persists*. The session:

- Queries current framework state via web search rather than relying on a hardcoded framework list inside the session prompt — self-referential correctness, the session's own staleness is avoided by the same mechanism it is checking for.
- Refreshes `informed_by:` citations and `rubric_anchor` versions where they've drifted; updates `last_verified:` fields.
- Preserves entry IDs and provenance across the refresh (downstream references to entry identity survive the Update).
- Is resilient to partial source-access failure: if one framework's current state can't be retrieved in-session, that entry is flagged and skipped rather than blocking the rest of the refresh.
- Does **not** do architectural drift. Schema changes, tier restructuring, and entry composition revisions are out of scope for an Update session and belong to separate Library-revision work. If the session notices a candidate architectural change, it flags it as an out-of-scope observation rather than fixing it inline.

Library versioning rides PRISM's own semantic version; an Update session's changes land inside PRISM's existing changelog as a bounded currency-refresh entry, not a separate Library changelog. Running an Update session is a deliberate operator action, not an automatic behaviour; the default posture is that the Library stays on its last ratified state until explicitly refreshed.

**Signal flow from point refresh to Update session.** The two tiers connect through an advisory signal. The judging LLM weighs:

- The count of *stale-but-refresh-inline* and *stale-and-pattern-accumulating* dispositions surfaced in recent projects.
- `rubric_anchor` version mismatches, weighted higher than `informed_by:` staleness — anchored specs grade mechanically, so anchor drift distorts grading more directly than provenance drift distorts framing.
- Time since the last Update session, weighed against the observed velocity of the cited frameworks.

These feed a single advisory output along the lines of *"consider running an Update session before the next project in this domain — WCAG and NIST CSF have both moved since the last refresh and several domain-pack lenses in this subject's space cite them."* The advisory is not blocking; the operator decides. Compatible with SP-9 (silence is never consent; the advisory is explicit rather than implicit) and SP-12 (the judgment is bounded by what the judging LLM has actually observed across the set of projects visible to it, and the bound is disclosable alongside the advisory).

*Rev. 6.5 posture: current-fidelity capture. The exact shape of point refresh's inline-update semantics and the Update session's source-access failure modes will clarify through real use; refinement expected in rev. 6.6+.*

---

## 7. Catalog: what carries forward, reshapes, or dissolves

The two-axis evaluation (§2.1–2.2) applied to v1.x's structural elements. Items flagged *open* are enumerated in §11 or delegated to the separate walkthrough artifact.

### 7.1 Carries forward

- **PRISM Lens Library** (new in v2 as core architecture) — the reference setup grades coverage against
- **Master** (the project state file; née Starter) — working memory; plain-chat substrate requires file-based persistence
- **Learnings Register** (lives inside the Master) — hygiene; cross-project pattern capture; the sourdough analogy belongs here
- **Standing Principles** (subset) — hygiene; some elements reshape (see §7.2)
- **Semantic versioning** — reproducibility
- **Structured final deliverables** — reproducibility for external stakeholders
- **Atomic prompt template** — hygiene; reshapes in v2 to carry the paired Execution Envelope (inbound) + Execution Output (outbound) contract (§4.1.1)
- **Multi-vendor triangulation** — hygiene; divergence between independent generations is signal

### 7.2 Relocates or reshapes

- **Monitors** — v1.x fired them inside execution sessions with mixed adherence (judgment monitors sat at ~55–65% because they fired under analytical pressure). v2 **relocates** all surviving monitors to orchestration, where they fire as explicit gates under lower cognitive load. `[empirical | review-if: substrate shifts]` Adherence should improve materially. The earlier "enforcement → posture cue" framing was over-rotated; explicit gates in orchestration work fine. Per-monitor dispositions, converged from the walkthrough reactions session (twelve handled, eleven survive, M12 retired):
  - **M1 — Missing Inputs.** Relocate to orchestration. Execution-side mirror via prompt-body instruction plus an optional `Attachment warnings` field in the Output signature.
  - **M2 — Version Drift.** Relocate to orchestration; **retained**. Real failure class (operator/environment mistakes); if v2's spec eventually specifies bump atomicity such that drift becomes impossible by construction, M2 quietly never fires — no cost. Spec session revisits.
  - **M3 — Sequence Violation.** Relocate to orchestration; feeds *What's next*.
  - **M4 — Ambiguous Ask.** Relocate to orchestration. No execution mirror — execution sessions receive pre-resolved dispatched prompts, not operator asks.
  - **M5 — Context Pressure (absorbs M12).** Relocate to orchestration; reshaped around the telemetric context-pressure framework (§3.7). Single monitor on compound volumetric + behavioral signal; band-state triggers; no declared-budget dependency.
  - **M6 — Premise Shift.** Relocate to orchestration; convergence-time.
  - **M7 — Assumption Conflict.** Relocate to orchestration; convergence-time.
  - **M8 — Stale Source.** Relocate to orchestration; convergence-time. Scope distinct from §6.6 point refresh: M8 catches stale *evidence in the audit*; §6.6 catches stale *framework anchors in the PRISM Lens Library*.
  - **M9 — Convergence Type Drift.** Relocate to orchestration; **retained**. Checks-and-balances on the LLM side, paralleling M1/M4 on the operator side. Neither side gets "well-framed, probably fine" benefit; the framework doesn't single-side its distrust.
  - **M10 — Rerun / Fix Required.** Relocate to orchestration; feeds *What's next*. Deferral-target logic operates on live strategy state rather than SF5 declaration (SF5 dissolved — see §7.3).
  - **M11 — Layer 2 Readiness.** Relocate to orchestration; feeds *What's next*. Operator decides at the *What's next* moment whether to run Layer 2, consistent with SF4 dissolution.
  - **M12 — Conversation Pressure.** **Retired.** Absorbed into M5's telemetric framework.

  Three presentation groupings (clarity, not mechanics): *What's next* inputs (M3, M10, M11) — state-detection monitors feeding the priority-ranked candidate list at each orchestration turn's close; convergence-time monitors (M6, M7, M8) — fire during Layer 1 integration of new findings into the Master, can chain to M10; standalone monitors (M1, M2, M4, M5, M9) — each serves a distinct failure class with no natural group. Triggers stay distinct within each group.

  *Framing — checks-and-balances on both sides.* The retained mix isn't accidental. M1 and M4 are checks on the operator side (catching missing inputs and ambiguous asks before they propagate); M9 is the matching check on the LLM side (catching convergence-type drift before it hides under "well-framed, probably fine"). Neither side gets the unconditional benefit of the doubt; the framework doesn't single-side its distrust. This is the principle that makes M2 and M9 retentions defensible even when their fire frequencies are expected to be low — the cost of a silent monitor that never has to fire is small; the cost of single-sided distrust is structural.
- **Adaptation** — v1.x's major-bump ceremony absorbs into two shapes: lightweight strategy revision at convergence (§5.5) plus the What's next escalation path (§4.3).
- **Gates** — GATE-1 folds into *What's next*; GATE-2 folds into M11's Layer-2 readiness trigger; GATE-0's work redistributes across session-start Monitor firing (M1, M2, M3, M4) and the What's next state summary.
- **Convergence (SP-3)** — moves from inside the prompt delivery session to orchestration. Per-prompt convergence checklists drop from the atomic prompt template.

### 7.3 Dissolves or demotes

- **SP-3 (convergence-in-prompt-session)** — incompatible with the orchestration/execution split.
- **Waterfall setup** — replaced by iterative refinement (§5).
- **"Setup ends at v0" versioning** — artifact of waterfall thinking.
- **All five Scope Flags (SF1–SF5)** — dissolve. Walkthrough proposed five → three; the session's inverse test (*"when would an operator actually disable this?"*) eliminated the remaining survivors. The unifying pattern: each declaration was carrying information v2's architecture already has, can compute live, or can observe directly. The Prompt Strategy carries project shape; the attach map carries per-prompt scope; *What's next* carries live state. Per-flag rationales: **SF1 (Multi-LLM enrichment)** — three pieces of v1.x machinery dissolve into v2 architecture independently (Discovery distributes across Probes 3, 7, and 1; Enrichment Scoping is replaced by Probe 1's tri-state grading; the five-role catalog becomes guidance, not machinery); the face-value semantic (§2.6) of "binary multi-LLM on/off" has no remaining gating. **SF2 (cross-prompt dependencies)** — mechanically visible from the strategy; M6's dormant-when-no-material is structural; misdeclaration was a live failure mode (`no` declared on a project that has dependencies → M6 silently disabled). **SF3 (external stakeholder deliverable)** — controls post-hoc rendering at Layer 2 time, from material §4.2 captures at constant discipline regardless of any flag; up-front declaration costs nothing to give up. **SF4 (Layer 2 cold synthesis)** — by the time Layer 2 is next-up, Layer 1 deliverables are already in hand; v2's Master-centric model with continuous Layer 1 integration makes the v1.x "mid-flight cost" argument a v1.x artifact. **SF5 (expected session count)** — static prediction about a length §5.5 explicitly lets adapt at convergence; *actively miscalibrated* M10 on the projects most likely to benefit from M10 firing cleanly.
- **Runtime Profile** — dissolves entirely. Replaced by the telemetric context-pressure framework (§3.7). v1.x's declared-budget arithmetic (declared budget × threshold percentage → monitor fire) was acknowledged as fiction in v1.10.4's own Context Pressure Bands rationale; the calibration chain is unreliable at every link (declared value nominal, actual pressure content-variable, self-reporting approximate, UX signals lag). v2 replaces it with a continuous-observation mechanism that compounds seven weak signals (volumetric: attached content size, conversation accumulation, reasoning accumulation; behavioral: quality-degradation self-check, task-completion friction, platform UX signals, operator-reported signals) into qualitative bands (🟢/🟡/🟠/🔴), with protective machinery firing on band state. Tier-agnostic by construction — 200K-budget sessions hit bands sooner, 1M-budget sessions hit them later, machinery response is identical. The non-default-host flag dissolves alongside (orchestration is Claude by §3.1; non-Claude orchestration is out of scope under §3.5's beta posture).
- **Subject-template tier (inside the Library)** — dissolves. Its work relocates to Setup (§5.4) as instance-specific artifacts produced by Probes 3 and 7. The Library carries reusable lenses across projects; Setup carries the specific-to-this-subject artifacts the lenses grade against. Collapsing the two was a category error the rev. 6.5 reframe corrects.

### 7.4 Walkthrough delegation — resolved

Resolved at rev. 7. The per-item walks for Scope Flags + Runtime Profile + Monitors converged through a walkthrough reactions session; converged dispositions are captured in `PRISM_v2_walkthrough_converged_dispositions.md`, which is the canonical output of this delegation and supersedes the walkthrough-proposals artifact for fold-in purposes. Outcomes folded into §7.2 (per-monitor dispositions, with framing on checks-and-balances) and §7.3 (Scope Flags + Runtime Profile dissolutions) above. Design-gap items raised during the session (Part 5 of the converged dispositions — nineteen items spanning the prompt-package engine and the context-pressure framework) feed the v2 specification, not this design document. Surfaced principles fold into the body text at §2.6, §3.6, and §3.7. The walkthrough proposals artifact is retained as provenance.

---

## 8. Scope boundaries

### 8.1 In scope

- Plain LLM chat-based tools (Claude for orchestration, any vendor for execution)
- Self-operated methodology (no external reviewer required)
- Mobile-friendly execution
- Multi-vendor triangulation as an operator-driven methodology
- Library-graded scope integrity

### 8.2 Out of scope (with narrow exceptions)

- **Hiring a domain expert to spot-check deliverables.**
- **Default-assumed automatic ground-truth validation.** Where an authoritative canonical data source *exists* for the subject (a regulated registry, a standards body with testable criteria, a curated research corpus, a benchmark dataset), PRISM should find it and use it — Probe 7 surfaces this. Where no such source exists (most consumer-product categories, most early-stage market analysis), the framework relies on the hygiene stack in §8.3 instead.

Desktop-mode execution variants (agentic orchestration, plugin-equipped sessions, automated cross-vendor dispatch, vendor skills ecosystems) are **not** out of scope in the same sense. v2 does not build them, but v2's architecture accommodates them as layered extensions. See §9.

### 8.3 The three-leg constraint

v2 operates under a structural constraint worth naming explicitly:

1. The operator is charting unfamiliar territory — that is why they are running the project.
2. LLMs produce the charting.
3. Neither the operator nor any single LLM has reliable domain ground truth *in the general case*.

Leg 3 is conditional. Where an authoritative source exists (§8.2), the framework brings it in. Where it doesn't, the hygiene stack compensates:

- Library coverage grading (reference-catalog check against material questions)
- Cross-vendor triangulation (divergence as signal)
- Falsifier probes (what would prove this wrong?)
- Provenance discipline (every claim traceable to its origin)
- Adversarial passes (separate session, clean slate, explicitly hunting for gaps)
- Calibration probes (the LLM rates its own confidence per claim, interpreted as relative signal)
- Pre-mortems

No single mechanism substitutes for domain expertise. Stacked, they materially reduce the risk of confident-but-wrong findings propagating into final deliverables.

---

## 9. Roadmap adjacencies

Three capability categories are not built into v2 but are treated as first-class roadmap items. v2's architecture is designed to accommodate them as layered extensions.

### 9.1 Automated cross-vendor orchestration

Desktop-mode tools (e.g., Cowork + Computer Use) driving authenticated web UIs of multiple LLM vendors automatically. v2 commits: vendor-agnostic execution contract (§4.4); execution-mode flag reserved at setup; convergence is already orchestration-side, so automation of dispatch doesn't touch convergence. v2 does not build the automation, test against current reliability curves, or pre-commit to a specific automation vendor. Gate for promotion: Cowork + Computer Use reliable enough to handle authenticated sessions across three or more vendors without frequent operator intervention.

### 9.2 Plugin-equipped execution sessions

Execution sessions that invoke specific plugins (Playwright, Chrome DevTools, Firecrawl, Figma, etc.). Plugins currently require a desktop-mode host. v2 commits: the attach map's tools slot is structural (§4.4); Vendor Selection (§4.5) extends naturally to plugin coverage as a signal. v2 does not curate plugin shortlists or maintain plugin-to-prompt pairings inside the framework. Gate for promotion: a desktop-mode variant exists, and specific plugin↔prompt pairings demonstrate material uplift on real work.

### 9.3 Multi-vendor skills/plugins ecosystems

Every major LLM vendor is building a skill/plugin ecosystem (Claude Plugins, Perplexity Skills, OpenAI GPTs, Gemini Gems). v2 commits: Vendor Selection (§4.5) can incorporate skill coverage as a signal; multi-vendor triangulation treats different ecosystems as epistemic diversity. v2 does not survey ecosystems, recommend specific pairings, or privilege one ecosystem. Gate for promotion: Vendor Selection's live check accumulates enough signal to make materially better recommendations informed by skill coverage.

---

## 10. Relationship to v1.x

### 10.1 Version pinning

Projects born under v1.10.4 pin to v1.10.4 for their lifetime. v2 does not apply to them, and v1.10.4 is not asked to adopt v2 mechanics mid-project.

### 10.2 Parallel-track — v2 supersedes v1.x

**Decision:** v2 supersedes v1.x as it stabilizes. v1.10.4 is the terminal v1.x release by default.

**Exception retained by the operator:** a v1.11 courtesy patch may ship ahead of v2 stabilization if the operator chooses — on the order of the already-completed triage — to protect the public-repo first-impression window (the GitHub repo is live as of April 2026). No commitment; the call is made when the timing becomes clearer.

---

## 11. Open questions

Named honestly rather than quietly assumed:

1. **Phase-ID vs. prompt-ID naming.** Decided: Phase IDs are P.x for filename versioning (grouped under phase); prompt IDs are short unique identifier + purpose/title, unrelated to phase. Closed.
2. **Strategy stability loosening.** Decided in §5.5: presumption of stability, revisable at convergence. Strategy freeze softens to strategy stability. Closed.
3. **Probe set composition.** Seven probes as of rev. 3. Iteration floors and ceilings need real-use data. Open.
4. **Scope Flags per-item walk.** Closed via walkthrough reactions session (rev. 7 fold-in). All five dissolve; per-flag rationale captured in §7.3 and the converged-dispositions artifact.
5. **Runtime Profile simplification.** Closed via walkthrough reactions session (rev. 7 fold-in). Dissolves entirely; replaced by the telemetric context-pressure framework in §3.7. Captured in §7.3 and the converged-dispositions artifact.
6. **Monitor-by-Monitor walk.** Closed via walkthrough reactions session (rev. 7 fold-in). Eleven monitors relocate to orchestration; M12 retired (absorbed into M5's reshape around the telemetric framework); M2 and M9 retained on checks-and-balances reasoning rather than as quiet-retirement candidates. Per-monitor dispositions captured in §7.2 and the converged-dispositions artifact.
7. **Multi-LLM coordination under the split.** Addressed via the paired Execution Envelope + Output contract (§4.1.1) which carries vendor+mode+schema-version+caveats across the split. Empirical testing (April 2026) confirmed paste as an unsupported input path; file-based delivery is mandatory. Sufficient for first-cut; real-use may surface additional needs.
8. **Master file leanness.** Addressed in §4.2: the Master scales with project complexity; lean workflows get a lean Master. Closed for direction; specific register populations per project-type are a specification-level concern.
9. **Design-alternatives evaluation methodology.** Worked out in a separate session before v2 specification begins. Prompt text provided separately. Open.
10. **Posture-cuing operationalization.** Largely absorbed by the Monitor relocation in §7.2. The residual question — can any element that has to live inside execution operate via posture-cuing rather than explicit instruction — is small enough to defer to real-use observation.
11. **Library-coupled ship timing.** v2 ship readiness was coupled to PRISM Lens Library v0.9 availability (§6.5). Library v0.9 shipped on 2026-04-24 (tagged `prism-lens-v0.9`, public repo); the dependency is satisfied. Closed.
12. **Library-architecture uniqueness.** Surfaced in the rev. 6.5 consultation: is the two-tier (universal + domain) catalog shape uniquely right, or one of several viable shapes? Closed: acknowledged as conventional rather than derived — the shape is a reasonable choice, not a forced conclusion. Release notes will document the choice as conventional so that future revisions can revisit it without treating the existing shape as load-bearing.
13. **Specialist-pass mechanism.** Surfaced in the rev. 6.5 consultation: how do specialist passes (regulatory, security, accessibility, etc.) get enumerated and dispatched? Closed: the Library itself is the specialist enumeration — each lens carries a `specialist_type` (§6.1), and the judging LLM promotes relevant entries as specialist passes under Probe 1 grading. No separate specialist catalog is needed.
14. **Point-refresh operator-fatigue calibration.** Open. The tri-state Probe 1 disposition and the point-refresh pass (§6.6) both surface potential noise to the operator. How often *fires-maybe* and *stale-but-refresh-inline* fire per project in practice — and whether that volume stays in the signal range or drifts into noise — is empirical and can only be calibrated post-release against real projects. Revisit after a handful of v2 audits.
15. **Learnings-accretion path for domain-practitioner-surfaced lenses.** Open. Probe 7 (domain-practitioner survey) can surface lenses that are materially important for the specific subject but are not in the catalog. Where do those lenses go? Options include: (a) the Learnings Register inside the Master (per-project only, no propagation), (b) a staging area feeding future Update-session decisions about whether to promote to the canonical Library, (c) something else. Resolution belongs to post-ship real-use observation, not upfront design.

---

## 12. Status and roadmap

Absorbs ship plan rev. 4 (April 2026) — phase status, decisions register, and tracked-items lists. The ship plan retires as a parallel artifact per §2.7.

### 12.1 Critical path to v2.0

Four phases. Status as of April 2026.

**Phase 1 — Walkthrough reactions → rev. 7. ✅ Complete.** Walkthrough reactions session converged the per-item Scope Flags + Runtime Profile + Monitors dispositions; rev. 7 fold-in absorbed converged dispositions and surfaced principles. Rev. 8 absorbs the remaining un-folded outputs and retires the dispositions and ship plan artifacts per §2.7.

**Phase 2 — PRISM Lens Library v0.9. ✅ Complete.** Shipped to git on 2026-04-24, tagged `prism-lens-v0.9`, file at `lens/PRISM_lens_library.md`.

**Phase 3 — Specification. 🟢 Next up.** Inputs: rev. 8 design document (this artifact) + Library v0.9. Output: first-draft v2 specification (`PRISM_v2_spec_rev1_draft.md`) covering rev. 8 §4 / §5 / §6 mechanics, §13 Open design gaps for spec, and §14 Spec-session deferrals. Design-alternatives methodology prework deliberately skipped per §11 item 9.

**Phase 4 — Build. 📋 Tracked.** Build PRISM v2.0 from spec; full rebuild not patched (per §10.1); SP-6 deterministic build method. Followed by an integration dogfood run on a small real project to surface multi-vendor Self-check empirical gap (only Claude-family verified at rev. 7), telemetric framework calibration on real signals, and *What's next* behavior under messy state.

**Phase 5 — Release. 📋 Tracked.** v2.0 release notes (operator-facing, distinct from Appendix B); RELEASING.md updates for Library cross-repo pinning if needed; CONTRIBUTING.md updates for v2-specific contribution surface; signed commit; tag `v2.0.0`; PAT-driven push.

### 12.2 Decisions register

**D1 — Retrospective SIT harness disposition. 🟡 Pending operator call.** Pre-execution SIT function architecturally absorbed by Library coverage saturation (§5.2 #2). Post-execution declared-vs-executed retrospective audit not represented in v2. Options: (a) ship as v2 appendix; (b) park for post-v2.0 *(recommended)*; (c) retire. Not blocking v2.0 ship.

**D2 — v1.11 courtesy patch ship/skip. 🟡 Pending operator call.** §10.2 leaves operator's call. Repo public with v1.10.4; first-impression window partially spent. Options: (a) ship v1.11 as patch; (b) skip; v1.10.4 terminal v1.x *(recommended)*. Not blocking v2.0 ship.

**D3 — When do parked v2 ideas surface. ✅ Resolved.** Three parked ideas. Idea #1 (Claude Project as Setup recommendation) and Idea #2 (session history as validation/recovery mechanism) incorporated into spec scope — see §13.3. Idea #3 (two-axis tag taxonomy) shipped in rev. 6.5 Appendix C.

**D4 — Sequencing preference. ✅ Resolved.** Walkthrough-first vs. Library-first — both done.

**D5 — Working-artifact durability strategy. 🟡 Pending operator action.** Design-phase working artifacts live in `/mnt/user-data/outputs/`. Options: (a) upload to project knowledge for auto-attach durability *(recommended)*; (b) push to repo as design-phase provenance trail; (c) re-attach explicitly each session. Increasingly load-bearing as session count grows; rev. 8's §2.7 discipline reduces but does not eliminate the surface (the direction-of-record is still re-attached each session). Recommendation aligns with parked idea #1 (§13.3) — Claude Project absorbs the friction.

**D6 — Design-alternatives methodology prework. ✅ Resolved by skip.** Operator decision to skip the prework session and let the spec session pick alternatives directly. Closes §11 item 9. Spec-session handoff carries forward the instruction that picks be made and alternatives-considered captured in a flagged-items register.

### 12.3 Operator-facing artifact strategy

v2 ship readiness depends on canonical artifacts being unambiguous. The discipline:

- **Direction-of-record:** this design document, then v2 specification, then PRISM v2.0 itself. One file at any moment is "the source"; downstream artifacts retire on absorption (§2.7).
- **Production artifacts at ship:** `PRISM_v2_0.md` (canonical) + `PRISM_v2_0_0.md` (versioned copy) + `lens/PRISM_lens_library.md` (already shipped at v0.9). Release notes and updated contributing/releasing docs round out the v2.0 release surface.
- **Historical provenance:** working notes, dispositions artifact, ship plans rev. 1–4 — retained on cloud drive (Appendix E.5), not re-attached as active inputs. Accessible via session search if needed.

### 12.4 v1.11 — operator's call

§10.2 retains the option of a v1.11 courtesy patch ahead of v2 stabilization. No commitment; D2 disposition above.

---

## 13. Open design gaps for spec

Seventeen items the spec session resolves. Folded from `PRISM_v2_walkthrough_converged_dispositions.md` Part 5 (items 7 and 8 already body-text in §3.6 and §2.6 respectively) plus parked design ideas D3 #1 and D3 #2 (incorporated into spec scope per ship plan rev. 4). The spec session picks design alternatives where multiple exist, captures alternatives-considered in a flagged-items register, and produces `PRISM_v2_spec_rev1_draft.md`.

### 13.1 Prompt-package engine (items 1–6, 9–13)

Surfaced during the SF1 → prompt-package-engine investigation. The architecture in §4 supports these mechanics; the spec names and shapes them.

1. **Single-Envelope-with-spectrum shape.** Dispatch spectrum carried in one Envelope (equivalence / split / limitation-named) rather than binary two-Envelope shape.
2. **Rationale discipline per dispatch variant.** Positive framing (what it does, not what it lacks); one line each; mobile-legible.
3. **Multi-vendor convergence mechanics.** Probe 2 fires at N≥2; re-runs as returns arrive.
4. **Asymmetric parallel return handling.** Graceful degradation when one of N parallel dispatches fails.
5. **Claude-baseline feasibility with named-limitation escape hatch.** For prompt shapes where Claude alone is genuinely insufficient.
6. **Cost signaling.** Implicit in rationale and dispatch shape; no separate field.
7. *(Folded into rev. 7 §3.6 — Claude prerequisite.)*
8. *(Folded into rev. 7 §2.6 — face-value naming.)*
9. **Prompt body convergence provisions.** Baked in at composition; vendor-neutral; any-subset-executable.
10. **Recommended-vs-executed reconciliation mechanic.** On Output return.
11. **Substitution absorption.** Operator ran Claude instead of Gemini — accept and adjust at convergence; no re-dispatch demand. Principle in §3.6; mechanics deferred to spec.
12. **Master tracking field.** Recommended-vs-executed state per prompt.
13. **Operator-declaration close-loop mechanic.** "Done" / "running later" / "skipping" — each closes an open dispatch.

### 13.2 Context-pressure framework (items 14–19)

Surfaced during the Runtime Profile investigation. The framework in §3.7 names the architecture; the spec shapes the mechanics.

14. **Telemetric framework full spec.** Signal weighting and compounding rules across the seven sources catalogued in §3.7.
15. **M5 + M12 consolidation full spec.** Single context-pressure monitor reshaped around the telemetric framework.
16. **Continuous-curation posture — operationalization.** Earlier and lighter than v1.x's threshold-based intervention.
17. **Migration-as-planning-not-rescue — handoff format at 🔴.** Concrete handoff format produced when the framework reaches the migrate band.
18. **Failsafe recovery as design posture — Master/*What's next* continuous-state mechanics.** What "always written" actually means in spec terms.
19. **Defensive migration at natural seams — band-state migration spec.** Advisory at 🟢 / recommended at 🟡 / strongly recommended at 🟠 / correct at 🔴.

### 13.3 Parked v2 design ideas (D3 closure)

Two ideas previously parked, now incorporated into spec scope per D3 (§12.2). Both are Claude-specific (rely on Claude's Project structure and past-conversation search), consistent with §3.1's `[vendor-dependent | review-if: orchestration vendor changes]` tag on orchestration. Spec carries this provenance forward in the relevant decision tags.

**Idea #1 — Claude Project as Setup recommendation.** v2 Setup recommends the operator create a Claude Project as the home for project state. Benefits: project-knowledge auto-attach absorbs the D5-class re-attach friction; session-history search becomes bounded to the project, which interacts cleanly with SP-12 bounded-search disclosure. Spec covers: when in Setup the recommendation surfaces, what the operator is told about what to put in the Project, how the Master fits into the Project structure, fallback when the operator declines or cannot create a Project (graceful degradation, not refusal to proceed).

**Idea #2 — Session history as validation/recovery mechanism.** When state is unexpected, ambiguous, or out-of-order — Master version does not match what *What's next* predicted; a finding references a prompt that does not appear in the strategy; the attach map and the conversation disagree about which file is canonical — session history (Claude's past-conversation search) is consulted to reconstruct or validate. Likely the practical TRI-21 state-pointer answer in real use. Spec covers: which Monitor (or *What's next* state-summary path) triggers the consult, what it queries, how the result is reconciled into Master state, the SP-12 bounded-search disclosure posture for what session history could and could not see (project-scoped vs. global), and reconciliation when session history disagrees with the attached Master.

---

## 14. Spec-session deferrals

Three items consciously not resolved at rev. 7/rev. 8; spec session handles. Folded from dispositions Part 7.

1. **M2's fate pending bump-atomicity specification.** M2 retained for v2.0 (§7.2). If v2's spec specifies bump atomicity such that drift becomes impossible by construction, M2 quietly never fires. Spec produces the bump-atomicity spec, then revisits M2.
2. **Output signature `Attachment warnings` field placement.** Small mechanic; lives naturally in §4.1.1's Output block. Exact field ordering and syntax is spec-session detail.
3. **M8 vs. §6.6 point-refresh scope separation.** Distinction clear conceptually (M8 catches stale evidence in the audit; §6.6 catches stale framework anchors in the Library). Needs clean specification so neither mechanism crowds the other out.

Open empirical items from §11 (items 14, 15) ride into spec as flagged post-release items, not specified upfront.

---

## Appendix A — Terminology

| Term | Definition |
|---|---|
| **Orchestration session** | A Claude session with the framework attached; handles planning, convergence, deciding, and state updates. |
| **Execution session** | A dispatched analytical session on any vendor, without the framework attached; receives instructions via the Execution Envelope and returns structured findings via the Execution Output. |
| **Master** | The single-file state document carried across sessions (née Starter in v1.x). Filename convention: `[project_name]_prism[version]_master_[phase-derived versioning].md`. |
| **PRISM Execution Envelope** | Inbound signature: a structured header block at the top of every dispatched execution prompt, carrying prompt ID, project, Master version, vendor, mode, session hygiene, attachment manifest, expected output filename, and optional operator hints. |
| **PRISM Execution Output** | Outbound signature: a structured header/footer block wrapping the findings in the `.md` file produced at the end of every execution session. Carries prompt ID, project, Master version, vendor, mode, schema version, date, prompt hash, and download instructions. Produced as a file, not as pasted content. |
| **What's next** | Artifact written at the close of each orchestration session: state summary, priority-ranked candidate list, recommendation, operator escalation on ties, dispatch-ready payload, and operator hints where applicable. |
| **Operator hint (in-context)** | Optional one-line cue emitted by orchestration at a specific touchpoint (Execution Envelope's `Operator hints` field, §4.1.1; *What's next* artifact, §4.3) to surface a time-sensitive operational move for the operator — an Appendix E cross-ref, an artifact-survival step, a vendor-switch gotcha. Emitted only when a cue applies to the specific action; routine turns carry no hints. Best-effort calibrated to the operator's environment, with calibration target attributed where non-obvious so a substrate mismatch is self-diagnosing. |
| **Vendor Selection** | Orchestration-time live step, run at dispatch, that verifies current vendor/mode/best-practice state and outputs structured choices + a recommendation bubble. |
| **Saturation** | Readiness condition: two consecutive setup iterations produce no material change to coverage or strategy. |
| **Earn its place** | The filter applied to every specification element in v2 — category × shape. |
| **PRISM Lens Library** | The reference catalog of material-question categories. Core v2 architecture. Often shortened to "Library" in subsequent references within the same section. |
| **Lens** | One entry in the Library. |
| **Provenance discipline** | External frameworks cited as what informed a lens's design, not as runtime rubrics. |
| **Motivated non-practitioner** | v2's operator target. |
| **Execution mode** | Setup-level flag identifying how execution sessions are dispatched. v2 default: `manual plain-chat`. |
| **Roadmap adjacency** | A capability v2 does not build but explicitly accommodates via architectural commitments. |

---

## Appendix B — Provenance and revision history

This document consolidates and supersedes two sets of working notes dated 2026-04-19 (a first design session and a same-day addendum). The notes used internal shorthand; this document translates their conclusions into terminology accessible to external readers.

**Rev. 1 → Rev. 2 changes:**
- Lens Library promoted from deferred integration to core v2 architecture.
- Desktop-mode variants / plugins / vendor skills promoted from out-of-scope to roadmap adjacencies.

**Rev. 2 → Rev. 3 changes:**
- Subject scope broadened from "consumer-facing digital products" to the full range of multi-dimensional research and analysis projects PRISM supports.
- Orchestration made explicitly Claude-specific; execution vendor examples sharpened (Perplexity, Gemini, ChatGPT, Claude).
- Project State File renamed to **Master**; sourdough analogy relocated to the Learnings Register where it fits cleanly.
- §4.1.1 added: **PRISM Execution Output signature** as load-bearing element of the execution-session contract, with export-survival rationale.
- §4.3 *What's next* revised from pointer to priority-ranked candidate list (TRI-21 fix).
- §4.5 added: **Vendor Selection at dispatch** as an orchestration-time live step with structured outcomes + recommendation bubble split.
- §5.3 gains **Probe 7 — Domain practitioner survey** (seven probes total).
- §5.4 (now §5.5 after the rev. 6.5 renumbering) softens from "strategy freeze" to "strategy stability, revisable at convergence."
- §7.2 Monitors reframed as **relocation** to orchestration, not enforcement→posture-cue reshape.
- §8.2 adds the authoritative-source narrow exception.
- §10.2 softened from "ship v1.11 first" to operator's call, no commitment.
- Continuity framing added: the orchestration/execution split is not new architecture; v2 formalizes what v1.x already does inconsistently.

**Rev. 3 → Rev. 4 changes** (driven by the Lens Library status-check case study and the paste-integrity empirical test):
- §2.5 added: **Standing Principles introduced or extended in v2** — SP-1 extended (Canonicity preservation) and SP-12 (Bounded-Search Disclosure). Sources: the Lens Library status-check session where an uncritical regeneration offer was rightly refused; the same session's bounded-conversation-search misreporting.
- §4.1.1 restructured as the paired **Execution Envelope (inbound) + Execution Output (outbound) contract**. Envelope block added to cover vendor-environment and session-hygiene instructions (e.g., "fresh session, no project attached"). Output signature gains a `Schema version` field, and its production moves into the execution session as a post-outcomes `.md`-file production step — the deliverable is a file, not a chat rendering. Paste is declared an unsupported input path, with empirical footing cited (three-vendor matrix, April 2026; ChatGPT-mobile fence-stripping is the load-bearing finding).
- §4.2 gains the Master-proportionality statement: lean projects keep a lean Master; register populations scale with complexity.
- §7.1 Atomic prompt template line updated to reference the paired contract.
- Appendix A terminology: added **PRISM Execution Envelope**; updated **PRISM Execution Output** to reflect file-based delivery.
- Open questions #7 and #8 closed by the §4.1.1 restructure and the §4.2 proportionality addition.
- Next steps and §7.4 updated to target rev. 5 as the walkthrough fold-in destination.

**Rev. 4 → Rev. 5 changes** (decision tagging pass):
- 15 decision tags applied across 16 sites (15 definite tags + 1 open flag). Two axes: Durability (`[structural]`, `[methodological]`, `[vendor-dependent]`, `[empirical]`) and Review trigger (`[review-if: ...]`, `[review-annually]`, `[stable]`).
- One open-flag item: §2.5 SP-12 Bounded-Search Disclosure — durability axis ambiguous (`[methodological]` vs. `[vendor-dependent]`); operator disposition required before tagging.
- Appendix C added: Tag Index by category for fast lookup.
- No changes to design decisions; tagging pass plus Appendix C index addition.

**Rev. 5 → Rev. 5.1 changes** (tagging-pass cleanup):
- SP-1 extended (§2.5) tagged `[operator-scaffolding | stable]` (missed in rev. 5).
- §4.3 *What's next* tagged `[structural | stable]` (missed in rev. 5).
- SP-12 (§2.5) disposition resolved: `[operator-scaffolding | stable]`; open-flag marker removed. SP-12 body text tightened: dropped the Claude-tool-name framing, demoted `conversation_search` to one example in a general list, named the principle explicitly as operator scaffolding. No change to the underlying principle.
- `[operator-scaffolding]` added as a fifth option on the durability axis. The handoff's "two axes, committed" constraint held — this expands options within an axis, not adds an axis — but the taxonomy grew, which is worth naming. Motivation: the scaffolding distinction is already load-bearing in §2.3; the tagging system is now aligned with what the framework already says it cares about.
- Appendix C: new `[operator-scaffolding | stable]` section added; Open Flags section removed (SP-12 resolved); tag counts updated.
- Rev. 4 → Rev. 5 change-log wording corrected: "No changes to design decisions; tagging pass plus Appendix C index addition" (prior wording said "no content changes," which Appendix C itself falsified).
- No changes to design decisions; tagging cleanup only.

**Rev. 5.1 → Rev. 5.2 changes** (terminology note):
- Added a note for future tagging passes: if a section holding ambiguous-tag dispositions reappears in a later rev, rename it (e.g., "Ambiguous tags" or "Unresolved dispositions") to avoid overload with the framework's other flag-shaped mechanisms (Monitor flags, Scope Flags). The rev. 5 "Open flags" label collided with those.
- No other changes.

**Rev. 5.2 → Rev. 5.3 changes** (filename convention captured):
- Appendix D added: filename conventions for design-phase working artifacts. Formalizes the version-after-name pattern adopted during rev. 5.2 delivery to keep version identity visible before mobile filename truncation.
- No changes to design decisions; convention capture only.

**Rev. 5.3 → Rev. 6 changes** (consolidated content additions — first minor bump since rev. 4):
- **§1.1 gains a fourth realization** — *substrate tolerance is both-edged*. Names the property (LLMs absorb inaccuracy gracefully) that unifies v2's principle-heavy lightness on the positive side and the operator-scaffolding hygiene stack on the negative side.
- **§2.5 adds SP-13 — Substrate Declaration** (`[operator-scaffolding | stable]`). Closes the wrong-substrate failure class: PRISM-loaded sessions verify their actual substrate against the declared target before executing dependent work. Sourced from the rev. 5 tagging session where Sonnet 4.7 executed work the handoff had specified for Opus 4.7 Adaptive; verification testing (April 2026) confirmed the pre-flight mechanic fires cleanly on Sonnet 4.6. Multi-vendor verification pending.
- **§4.1.1 restructured from paired contract to triple contract** — Envelope + Self-check + Output. The Self-check block operationalizes SP-13 inside execution sessions. Structural tag on the contract covers all three elements.
- **§4.1.1 paste-not-supported rewording.** Reframed from "paste is not a supported input path in v2" (which read as a framework-imposed restriction) to "v2's execution contract uses file-based delivery in response to what the testing surfaced." Makes the empirical origin explicit; names the design choice as mobile-first with accepted desktop-neutrality rather than restriction.
- **§3.4 Mobile-first added** (`[structural | stable]`). Promotes mobile-first from operational reality (v1.x) to named design commitment. Desktop fully supported as a superset.
- **§3.5 Beta posture added** (`[empirical | review-annually]`). Honest release positioning: tested substrate at release is Android (Samsung Galaxy S25+) mobile and major desktop web browsers; iOS and other Android OEMs untested; divergences on untested substrates are report-worthy findings, not defects.
- **Summary gains two paragraphs** — one for mobile-first, one for beta posture, both with pointers to the §3.4 / §3.5 detail.
- **Capture-discipline note added** at the top of the document, below metadata: *decisions are captured at current fidelity; completeness of phrasing or implementation detail is not a prerequisite for capture*. Codifies the rev. 5.x → rev. 6 practice.
- **Appendix E added — Mobile operator survival guide.** Platform-indexed catalog of known friction points and concrete workarounds for mobile operators. Initial entries: Samsung file-explorer indexing delay → MiX file manager; broken mobile-app functionality → Firefox Desktop mode. Living document.
- **Appendix C updated.** Three new tagged entries (§3.4, §3.5, SP-13). Tag count: 21 definite tags across 21 sites.
- Absolute-language audit performed; existing absolutes are contract-internal or principle-internal, not substrate-contingent claims. No sweep edits needed beyond the paste-not-supported rewording.
- Version bump: rev. 5.x patch family closed; rev. 6 as first minor-bumped content rev since rev. 4. The walkthrough fold-in originally queued for rev. 6 slides to rev. 7+.

**Rev. 6 → Rev. 6.1 changes** (survival guide accumulation):
- **Appendix E reshaped** to cover two classes of pattern, not one: *vendor-client workarounds* (original scope) and *operator interaction patterns* (new scope). Intro rewritten; structural subsection dividers added.
- **E.3 added — Artifact + handoff together ("present document with instructions").** When producing an artifact that will feed a subsequent session's work, ask for artifact + accompanying handoff prompt in one request. Avoids reconstruction drift on context the producing session still has fresh.
- **E.4 added — Session retrieval ("point me to the relevant session").** When work crosses sessions and the operator is in the wrong one (or can't locate a prior artifact), ask Claude for a clickable link via `conversation_search`. Includes SP-12 bounded-search caveat about project-scoped search.
- E.3 placeholder ("Space for future entries") removed; its content folded into the appendix intro as framing.
- No other changes. Rev. 7 remains reserved for walkthrough fold-in.

**Rev. 6.1 → Rev. 6.2 changes** (in-context operator hints):
- **§4.1.1 Execution Envelope gains an optional `Operator hints` field.** Names and generalizes work the Session hygiene field was already doing informally — one-line cues at dispatch, keyed to the specific action, with Appendix E cross-refs where applicable. Emission discipline included to preserve signal-to-noise: hints fire only when a cue applies, one line each, cross-ref not essay, no duplication of Monitor output. Example envelope updated to show hint use.
- **§4.3 *What's next* gains an Operator hints bullet.** When the next action is a dispatch, hints ride inside the Envelope. When the next action is not a dispatch (review, ratify, save-to-cloud before session close), hints surface on *What's next* directly. Same emission discipline either way.
- **Appendix A adds Operator hint (in-context).** Updates PRISM Execution Envelope and *What's next* entries to list the new field.
- **Appendix E gains E.5 — Persisting artifacts across device/session loss.** Operator interaction pattern: save execution outputs (and the Master) to cloud drive immediately after download / at session close. Exactly the kind of hard-won mobile operator knowledge the survival guide exists to catalog.
- **Appendix E intro adds the cross-reference pointer.** Names the just-in-time surfacing relationship between Envelope/*What's next* hints and this appendix, so an operator seeing `E.1` or `E.5` in an Envelope understands where the reference lands.
- No new tags; the additions extend already-tagged mechanisms (Envelope is `[structural | stable]`, *What's next* is `[structural | stable]`). Tag count unchanged at 21.
- Rev. 7 remains reserved for walkthrough fold-in.

**Rev. 6.2 → Rev. 6.3 changes** (operator-hint refinements from immediate-post-rev-6.2 notes):
- **§4.1.1 Operator hints paragraph extended with substrate calibration.** Hints are best-effort calibrated to the operator's environment (mobile vs. desktop, vendor client, tested substrates per §3.5); where the calibration target is non-obvious, hints carry a brief attribution — e.g., *"(Claude mobile, Samsung)"* — so a substrate mismatch is self-diagnosing rather than silently confusing. Missing on an untested substrate is expected and benign under §3.5's beta posture. Matching clause added to the §4.3 *What's next* bullet and the Appendix A Operator hint term.
- **§4.1.1 Operator hints paragraph gains an education-surface framing sentence.** Captures the secondary benefit: operators new to multi-vendor LLM workflows encounter best-practice cues at the moment of application rather than in advance-of-need documentation they'd have no reason to read. Part of why the feature earns its place. Design-doc capture of the framing; downstream marketing artifacts (README, landing page, positioning) can lift or rework as appropriate.
- **Appendix E.5 extended with Downloads-folder-clutter beat.** Situation paragraph adds the mobile Downloads folder's accumulation of overlapping versions, vendor-default filename collisions, and stale artifacts as a failure mode in its own right, separate from device-event loss. Why-it-works paragraph extends the cloud-drive rationale to cover navigability (structured project folders) alongside durability (survives device events).
- No new tags; extensions ride on existing Envelope and *What's next* tags. Tag count unchanged at 21.
- Rev. 7 remains reserved for walkthrough fold-in.

**Rev. 6.3 → Rev. 6.4 changes** (E.5 archival-discipline refinement):
- **Appendix E.5 Pattern paragraph extended with an archival clause.** Project-scoped folders keep versions separated; superseded artifacts are archived rather than deleted so the audit trail stays intact across the project's lifetime. Captures at principle level the Archive/ pattern observed in the maintainer's own Drive layout without prescribing a specific folder taxonomy (which would be altitude-mismatched for the rest of the appendix and brittle against operators whose scope differs from the maintainer's).
- Deliberate non-change: considered and declined adding a concrete ASCII folder-layout reference to Appendix E. Reasoning: (a) altitude mismatch with the Situation/Pattern/Why-it-works shape of other entries; (b) the maintainer's tree is tuned to multi-version maintenance, public-repo shipping, and active design work that most operators won't share; (c) durability risk — specific folder names (SIT Scope Test Harness/, V1/, V2/) age within months; (d) the principle is already carried at the right altitude by the Pattern paragraph. Concrete layout examples, if wanted later, belong in repo docs or the Skill file as *"how the maintainer runs it"*, not in the canonical design.
- No new tags. Tag count unchanged at 21.
- Rev. 7 remains reserved for walkthrough fold-in.

**Rev. 6.4 → Rev. 6.5 changes** (Lens Library consultation fold-in — the Library as reference catalog, not operational machinery):
- **Reframe underpinning the rev.** A reference catalog is not operational machinery. Entries cost nothing at runtime when they don't fire. This unlocks a tri-state Probe 1 disposition, relocates subject-template scaffolds from the Library to Setup, formalizes `specialist_type` as a first-class schema field, and surfaces currency of `informed_by:` / `rubric_anchor` as a real maintenance surface rather than an invisible drift source. The changes below flow from this single reframe.
- **§5.3 Probe 1 rewritten from binary to tri-state disposition.** Dispositions are *fires-covered* (silent pass), *fires-uncovered* (flag), *doesn't-fire* (silent, rationale captured), and *fires-maybe* (ambiguous — closed by either a *dig-in* targeted-research path or an *opt-out* documented-exclusion path). Both dig-in and opt-out satisfy §5.2 readiness layer 2. Failure-mode note included: operator-fatigue if too many *maybes* surface; mitigation is that the judging LLM resolves clear cases silently and escalates only genuine ambiguity. Empirical calibration deferred to post-release observation (new §11 item 14).
- **§5.4 added — Setup artifacts (instance-specific).** New subsection capturing the decision brief, stakeholder register, claim inventory, and jurisdiction map as Setup outputs populated primarily by Probes 3 and 7. Relocated from what earlier revs treated as a Library tier: these are instance-specific artifacts the Library's lenses grade against, not catalog entries that travel across projects. Old §5.4 (Strategy stability) renumbered to §5.5; cross-references in §7.2 and §11 item 2 updated; the rev. 2 → rev. 3 changelog entry gained a parenthetical pointer to avoid reader confusion.
- **§6.1 opening paragraph added — "The Library is a reference catalog, not operational machinery."** Names the inclusion bar asymmetry explicitly: an entry earns its slot if it could catch a silent omission on some real subject, not if it earns its slot against checklist fatigue.
- **§6.1 schema extended.** Added `specialist_type` (open taxonomy, domain-appropriate term — the Library itself is the specialist enumeration; judging LLM promotes relevant entries as specialist passes under Probe 1 grading). Added `last_verified:` per `rubric_anchor` (date of last check against the external spec's current version) so anchor staleness surfaces as a first-class signal.
- **§6.1 "Lens = triple" principle named explicitly.** `[structural | stable]` A lens is the triple (material-question, evidence-class, specialist-type). The same subject surface can legitimately host multiple lenses when triples differ. Partitioning by subject surface collapses research paths before the subject is in view; the triple keeps distinctions legible.
- **§6.1 trigger-rule language softened.** Dropped "mechanical, not judgment"; triggers are hints to the judging LLM about likely applicability, with actual applicability decided under Probe 1 grading (including the tri-state disposition). The judging-LLM-centered phrasing replaces the earlier deterministic-predicate phrasing.
- **§6.1 tier structure collapsed from three to two.** Universal + domain. Subject-template tier dissolves (work relocates to §5.4); §7.3 gains a matching dissolve entry.
- **§6.4 reframed from aspirational to emergent.** v2 is the design target for the Library; standalone usability is a likely emergent property of a well-shaped catalog but not designed-for. Release notes frame accordingly. This resolves a quiet tension between "shape for v2's needs" and "shape for generality" that the aspirational framing had introduced.
- **§6.6 added — Currency maintenance.** `[methodological | stable]` Two-tier mechanism. *Point refresh* (per-project, in Setup) extends Probe 1 to citation currency with three dispositions (fresh-enough / stale-but-refresh-inline-in-prompt-strategy / stale-and-pattern-accumulating); canonical PRISM file not modified. *Update session* (standalone, rare, operator-gated) has a PRISM-file-in → PRISM-file-out contract, queries current framework state via web search (self-referential correctness), preserves entry IDs and provenance, is resilient to partial source-access failure, and does not do architectural drift (schema/tier/composition changes are out-of-scope and flagged rather than fixed inline). Library versioning rides PRISM's own; changelog lives inside PRISM's existing changelog. Signal flow from point refresh to Update session is advisory (not blocking): count of refreshes, `rubric_anchor` version mismatches weighted higher than `informed_by:` staleness, time-since-last-Update vs. framework velocity. Rev-posture note in the subsection: exact shape of inline-update semantics and source-access failure modes will clarify through real use; refinement expected in rev. 6.6+.
- **§7.3 gains a dissolve entry — Subject-template tier (inside the Library).** Its work relocates to Setup (§5.4) as instance-specific artifacts produced by Probes 3 and 7. Category-error correction: the Library carries reusable lenses across projects; Setup carries the specific-to-this-subject artifacts lenses grade against.
- **§11 housekeeping.** Two items closed on arrival: (12) Library-architecture uniqueness — acknowledged as conventional rather than derived; release notes document the choice; (13) Specialist-pass mechanism — resolved by the Library-is-the-specialist-enumeration framing and the `specialist_type` schema field. Two items opened: (14) Point-refresh operator-fatigue calibration — empirical, post-release observation; (15) Learnings-accretion path for domain-practitioner-surfaced lenses absent from the catalog — resolution belongs to post-ship observation, not upfront design.
- **Appendix C updated.** Two new tag sites: §6.1 "Lens = triple" tagged `[structural | stable]`; §6.6 Currency maintenance tagged `[methodological | stable]`. Tag count: 23 across 23 sites (was 21 across 21). No axis additions.
- **Rev posture: current-fidelity capture.** Ship rev 6.5 with current language; refine in rev 6.6+ as the shape of point refresh and Update session clarifies through real use. This is the rev. 5.x → rev. 6 practice continued (see capture-discipline note at the top of the document).
- Rev. 7 remains reserved for walkthrough fold-in.

**Rev. 6.5 → Rev. 7 changes** (walkthrough fold-in):
- **§7.2 Monitors bullet rewritten** with per-monitor dispositions from the walkthrough reactions session. Twelve handled, eleven survive (all relocate to orchestration); M12 retired into M5's reshape around the new telemetric context-pressure framework (§3.7). M2 and M9 retained on checks-and-balances reasoning. Three presentation groupings named: *What's next* inputs (M3, M10, M11); convergence-time monitors (M6, M7, M8); standalone monitors (M1, M2, M4, M5, M9). Closing paragraph added on checks-and-balances framing (Part 4 principle 6 from the converged dispositions).
- **§7.3 rewritten — all five Scope Flags dissolve.** Walkthrough proposed five → three; the session's inverse test (*"when would an operator actually disable this?"*) eliminated the remaining survivors. The unifying pattern is named: each declaration was carrying information v2's architecture already has, can compute live, or can observe directly. Per-flag rationales (SF1 through SF5) consolidated into a single bullet.
- **§7.3 Runtime Profile entry rewritten — dissolves entirely.** Replaced by the new telemetric context-pressure framework (§3.7). The earlier "five → one-and-a-half" framing is retired. Non-default-host flag dissolves alongside (orchestration is Claude by §3.1; non-Claude orchestration is out of scope under §3.5's beta posture).
- **§7.4 marked resolved.** Walkthrough delegation closed; converged dispositions captured in `PRISM_v2_walkthrough_converged_dispositions.md`, which is the canonical output and supersedes the proposals artifact for fold-in purposes.
- **§11 housekeeping.** Items 4 (Scope Flags per-item walk), 5 (Runtime Profile simplification), and 6 (Monitor-by-Monitor walk) closed via walkthrough resolution. Item 11 (Library-coupled ship timing) closed via Library v0.9 ship. Items 14 and 15 stay open as post-release empirical, per the dispositions artifact.
- **§12 items 1, 3, 4 updated.** Item 1 reflects walkthrough complete (was: "converged dispositions fold into rev. 5"). Item 3 starts the spec session from rev. 7 (was: rev. 5) and points at the design-gap list. Item 4 reflects PRISM Lens Library v0.9 shipped status.
- **§6.5 Production status freshened** to record Library v0.9 ship (capture-discipline; original rev-6.5 dependency framing preserved as historical posture). End-of-document line updated to rev. 7.
- **PRISM Lens Library naming update applied** per ship plan rev. 2 Appendix B. Full name "PRISM Lens Library" used on first reference per top-level section across §Summary, §1.1, §2.5, §4.1.1, §5.1, §6 (heading + body), §7.1, §11 item 11, §12 item 4, and Appendix A terminology; subsequent references continue to use "Lens Library" or "Library" per the existing §6 convention. Historical changelog entries in Appendix B left in their period-of-record wording. Labeling update only; no semantic change.
- **§2.6 added — Face-value naming** `[methodological | stable]`. Specification elements carry their semantic at face value; when implementation detail accumulates behind a name that wasn't designed for it, the element is over-loaded. SF1 ("Multi-LLM enrichment" gating three pieces of v1.x machinery) is the worked example. Source: walkthrough converged dispositions Part 4 principle 1.
- **§3.6 added — Claude as prerequisite; design authority without access gating** `[structural | stable]`. Two paired moves: (a) at-least-Claude is a framework prerequisite (orchestration is Claude-specific by §3.1; explicit declaration removes contract ambiguity); (b) the framework designs the optimal path and informs the operator, without conditioning design on operator vendor access. Substitution-absorption mechanics deferred to spec session. Source: walkthrough converged dispositions Part 4 principle 2 + Part 5 design-gap item 7.
- **§3.7 added — Context-pressure framework, telemetric not arithmetic** `[structural | stable]`. Replaces the dissolved Runtime Profile. Compound seven-signal observation (volumetric: attached content, conversation accumulation, reasoning accumulation; behavioral: quality self-check, task friction, platform UX, operator-reported); qualitative bands (🟢/🟡/🟠/🔴); protective machinery fires on band state. Failsafe-recovery posture and defensive-migration-at-natural-seams included as subsections under the §3.7 structural tag. Tier-agnostic by construction. M5 (now absorbing the retired M12) fires against this framework. Specification of signal-weighting, hysteresis, and capture mechanics deferred to spec session (design-gap items 14–19). Source: walkthrough converged dispositions Part 2 + Part 4 principles 4, 5 + Part 5 design-gap items 14–19.
- **Appendix C tag index updated.** Three new tag sites — §2.6 (`[methodological | stable]`), §3.6 (`[structural | stable]`), §3.7 (`[structural | stable]`). Tag count: 26 across 26 sites (was 23 across 23). No axis additions; existing categories absorb the new sites cleanly. Failsafe-recovery folded into §3.7's section tag rather than tagged separately, matching the handoff's "23 to ~26" estimate. Checks-and-balances framing in §7.2 is body text; no new tag (Part 4 principle 6 is captured in body, not a separate tag site).
- Rev posture: current-fidelity capture continues per the top-of-document discipline. The telemetric framework's signal-weighting and the substitution-absorption mechanics will sharpen through spec-session work and real use; refinement expected in rev. 7.x or at specification time.
- Walkthrough fold-in complete; spec-session work next per §12 step 3.

The working notes remain available as provenance. The walkthrough reactions session converged the per-item Scope Flags and Monitors dispositions into `PRISM_v2_walkthrough_converged_dispositions.md`, which is the canonical output and supersedes the walkthrough-proposals artifact for fold-in purposes; the per-item outcomes are folded into §7 above.

**Rev. 7 → Rev. 8 changes** (parallel-state absorption; direction-of-record consolidation):

The driving discipline failure. Rev. 7 absorbed the agreed parts of the walkthrough dispositions (Parts 1–4, 6) but kept Parts 5 (17 design gaps) and 7 (3 deferrals) live as a parallel artifact, with the rationale *"those feed the spec session, not the design doc."* In parallel, the ship plan kept revving (rev. 1 → rev. 4) as a separate tracker rather than collapsing into the design doc as a status section. The accumulation went unnoticed until a spec session pre-flight failed because the count of named-required attachments was non-unitary (four instead of one), and the same counting ambiguity that produced the bad-session failure was structural in the artifact set itself. Rev. 8 corrects the fragmentation, retires both source artifacts, and adds §2.7 as the named principle.

Body-text changes:

- **§2.7 added — Direction-of-record absorbs parallel state at fold-in seams** `[methodological | stable]`. Methodological principle: when a downstream artifact converges, its outputs absorb back into the direction-of-record at body-text fidelity, and the source retires as an active input. The alternative (parallel trackers) accumulates fragmentation. Worked example: the rev. 6.5 → rev. 7 fold-in itself, where Parts 5 and 7 of the dispositions and the rev. 4 ship plan should have absorbed at rev. 7 and did not. Failure-mode capture: pre-flight attachment counts that fail because the count is non-unitary; the bad April 2026 spec session is named explicitly. Source: this fold-in session, April 2026.
- **§12 replaced — Status and roadmap.** Was "Next steps" (five line items). Replaced with four-subsection Status and roadmap absorbing ship plan rev. 4 §1 (status), §2 (critical path, four phases), §3 (decisions register D1–D6), §4 (tracked items lists). §12.3 added — Operator-facing artifact strategy — stating the direction-of-record discipline plus the production-artifact set at ship.
- **§13 added — Open design gaps for spec.** Absorbs `PRISM_v2_walkthrough_converged_dispositions.md` Part 5 (seventeen un-folded items: prompt-package engine items 1–6, 9–13; context-pressure framework items 14–19). Items 7 and 8 already body-text in rev. 7 (§3.6, §2.6 respectively); §13.1 references those as folded. §13.3 incorporates parked v2 design ideas #1 (Claude Project as Setup recommendation) and #2 (session history as validation/recovery mechanism) per D3 closure in ship plan rev. 4.
- **§14 added — Spec-session deferrals.** Absorbs dispositions Part 7 (three items: M2's bump-atomicity dependency, Output signature `Attachment warnings` field placement, M8 vs. §6.6 point-refresh scope separation).
- **Title/front matter:** date and rev marker bumped to rev. 8; Supersedes line names rev. 7 plus the two retired source artifacts (dispositions, ship plan rev. 4) explicitly.
- **Appendix C tag count:** §2.7 adds one site (`[methodological | stable]`). Tag count: 27 across 27 sites (was 26).
- **End-of-document rev marker** updated.

Source artifacts retired and replaced:
- `PRISM_v2_walkthrough_converged_dispositions.md` — Parts 1–4, 6 already absorbed at rev. 7; Parts 5, 7 absorbed at rev. 8 (§13, §14). Retired as parallel artifact; retained on cloud drive (Appendix E.5) as historical provenance.
- `PRISM_v2_rev4_ship_plan.md` — fully absorbed into §12. Retired as parallel artifact; retained on cloud drive.

Rebuild-discipline note (per dispositions Part 4 principle 3 — "Inverse test for Setup declarations"): for any Setup-time declaration, test whether a legitimate operator scenario benefits from it. The walkthrough's load-bearing application of this principle dissolved four of five Scope Flags. Captured here per the principle's own placement guidance (rebuild-discipline practice, not body-text principle).

Rev posture: current-fidelity capture continues. The §2.7 principle generalizes from one observed failure; expect refinement (or a body-text move to a different §2.x slot) as more fold-ins surface fragmentation patterns or absence-of-fragmentation cases that warrant a sharper distinction.

---

*End of v2 design document rev. 8. Direction-of-record consolidated; specification session next per §12.1 Phase 3.*

---

## Appendix C — Tag Index

All tagged decisions, organized by category. Format: `[durability | review-trigger]`. Inline tags in the document body use the same format; this index collates them for fast lookup and cross-referencing.

Tag count: 27 definite tags across 27 sites. No open flags.

Durability axis options: `[structural]`, `[methodological]`, `[vendor-dependent]`, `[empirical]`, `[operator-scaffolding]`. Review trigger options: `[review-if: ...]`, `[review-annually]`, `[stable]`.

---

### `[structural | stable]`

Architectural invariants. Change only via deliberate version bump with documented rationale.

| Section | Decision |
|---|---|
| §2.1 | Earn-its-place framework — three positive specification categories (working memory, hygiene, reproducibility) plus one negative (ceremony) |
| §2.2 | Two-axis shape test — every spec element evaluated against both category and substrate fit |
| §2.4 | Category-error rejection — software engineering's long-tail hardening rhythm explicitly rejected for LLM substrate |
| §3.3 | Version pinning — projects pin to the version they were born under; no mid-project framework updates |
| §3.4 | Mobile-first — design commitment: framework shaped so a default-substrate operator can run end-to-end from a phone; desktop fully supported as a superset |
| §4.1.1 | Execution Envelope + Output paired contract — the load-bearing execution-session boundary |
| §4.3 | *What's next* as a first-class artifact — state summary + priority-ranked candidate list + recommendation + operator escalation + dispatch-ready payload, replacing v1.x's implicit prompt-ID-as-progress-marker (resolves TRI-21) |
| §4.4 | Forward-compatibility commitments — vendor-agnostic contract, tools slot, execution-mode flag |
| §6.1 | Lens = triple — a lens is the triple (material-question, evidence-class, specialist-type); the same subject surface can host multiple lenses when triples differ |
| §6.3 | Provenance discipline — external frameworks cited as `informed_by:` provenance, not runtime rubrics |
| §3.6 | Claude as prerequisite + design authority without access gating — at-least-Claude is a framework prerequisite; the framework designs the optimal path and informs the operator without conditioning on operator vendor access |
| §3.7 | Context-pressure framework — telemetric, not arithmetic; seven-signal compound observation feeding qualitative bands (🟢/🟡/🟠/🔴); protective machinery fires on band state; failsafe recovery and defensive migration as design postures; tier-agnostic by construction |

---

### `[methodological | stable]`

Principles about how work gets done. Survive substrate changes; unlikely to require revision.

| Section | Decision |
|---|---|
| §2.3 | Scaffolding filter — primary question before formal two-axis walk: is this element for the operator or for the LLM? |
| §6.6 | Currency maintenance — two-tier mechanism: per-project point refresh (in Setup) updates the prompt strategy inline without modifying the canonical Library; rare operator-gated Update sessions refresh `informed_by:` and `rubric_anchor` in the canonical Library under a PRISM-file-in/PRISM-file-out contract; signal flow from point refresh to Update is advisory, not blocking |
| §2.6 | Face-value naming — specification elements carry their semantic at face value; over-loading (machinery accumulating behind a name not designed for it) is itself a finding when surfaced |
| §2.7 | Direction-of-record absorbs parallel state at fold-in seams — when downstream artifacts converge, their outputs absorb back into the direction-of-record at body-text fidelity and source artifacts retire; alternative (parallel trackers) accumulates fragmentation and breaks unitary attachment-count discipline |

---

### `[methodological | review-if: vendor landscape changes]`

Process design whose value is contingent on current vendor volatility. If the vendor landscape stabilizes (capabilities become predictable and well-documented), the live-check overhead should be re-evaluated.

| Section | Decision |
|---|---|
| §4.5 | Vendor Selection as orchestration-time live step rather than static role mapping |

---

### `[vendor-dependent | review-if: substrate shifts]`

Calibrated to the current plain-chat substrate. If the default execution substrate changes (agentic orchestration, automated dispatch, plugin-equipped sessions), revisit.

| Section | Decision |
|---|---|
| §3.1 | Plain LLM chat tools as default execution substrate |

---

### `[vendor-dependent | review-if: orchestration vendor changes]`

Explicitly Claude-specific. If orchestration migrates to a different primary vendor, everything under this tag needs re-evaluation against that vendor's machinery.

| Section | Decision |
|---|---|
| §3.1 | Orchestration session designed for Claude (tools: `present_files`, `create_file`, `str_replace`, Skill packaging, past-conversation search) |

---

### `[vendor-dependent | review-if: vendor X changes Y]`

Volatile by design. Vendor capability assignments are expected to drift; treat this as a live configuration, not a durable specification.

| Section | Decision |
|---|---|
| §3.1 | Vendor role assignments: Claude (analytical), Perplexity (live-web breadth), Gemini Pro Deep Research (long-context), ChatGPT o-series (adversarial/synthesis) |

---

### `[empirical | review-if: vendor behavior changes]`

Decided on the basis of a specific test (three-vendor matrix, April 2026). If a vendor updates its clipboard or file-handling behavior, re-run the test before updating the policy.

| Section | Decision |
|---|---|
| §4.1.1 | Paste is not a supported input path — file-based delivery mandatory; empirical footing: ChatGPT mobile stripped fence structure while preserving raw text |

---

### `[empirical | review-if: substrate shifts]`

Decided on the basis of observed adherence data. If the substrate changes (e.g., execution sessions gain more framework context, or orchestration moves off Claude), re-evaluate whether the relocation decision still applies.

| Section | Decision |
|---|---|
| §7.2 | Monitors relocated from execution to orchestration — empirical basis: ~55–65% judgment-monitor adherence in execution sessions under analytical pressure |

---

### `[empirical | review-annually]`

No specific change trigger yet. Calibration values are tentative; check against real-use data on a regular cadence. Update tag to `[review-if: ...]` once a specific trigger is identified.

| Section | Decision |
|---|---|
| §3.5 | Beta posture — tested substrate at release is Android (S25+) mobile and major desktop browsers; iOS and other Android OEMs untested; divergences on untested substrates are report-worthy findings, not defects |
| §5.3 | Probe iteration floors and ceilings — minimum 2 iterations; flag at 4 as structural problem |

---

### `[operator-scaffolding | stable]`

Principles whose primary purpose is to cue the human operator — to surface a bound, a missing artifact, or a posture the operator needs at a specific moment. Distinct from methodological (principles about how work gets done in general) because the review question is different: *does the human still need this cue?*, not *is this principle still sound?* §2.3 of the design treats the scaffolding-for-the-operator vs. scaffolding-for-the-LLM distinction as a primary filter; this tag surfaces it in the index.

| Section | Decision |
|---|---|
| §2.5 | SP-1 extended — Canonicity preservation: locate the original before regenerating; surface consequences of regeneration (authenticity loss, schema drift, silent contamination) rather than offering regeneration as low-cost. |
| §2.5 | SP-12 — Bounded-Search Disclosure: when answering from a bounded retrieval, disclose the bound. Gives the human the chance to catch what the bounded view couldn't see. |
| §2.5 | SP-13 — Substrate Declaration: when PRISM is loaded with a declared target environment (model, vendor, mode), the session verifies what it's actually running on before executing dependent work; halts on mismatch rather than silently proceeding. Operationalized inside execution sessions by the Execution Self-check block (§4.1.1). |

---

*End of Appendix C.*

---

## Appendix D — Filename conventions for design-phase artifacts

Design-phase working files — this document, design notes, walkthroughs, handoff specs, rev iterations — follow a naming pattern that keeps the framework version and rev number visible before mobile filename-preview truncation:

`[artifact-name]_v[framework-version]_rev[X.Y]_[descriptor].md`

Example: `PRISM_v2_rev5_3_design_document.md`.

Rationale: mobile clients truncate filenames in file cards and attach previews. Putting framework version and rev number immediately after the artifact name keeps the version identity legible even when the descriptor is cut. Rev. 5.2 originally shipped as `PRISM_v2_design_document_rev5_2.md`; the `rev5_2` portion was truncated in mobile file-card rendering, making version-checking harder at a glance. The convention adopted mid-session fixes this prospectively.

Applies to: design documents, design notes, working drafts, handoff specs, and other session-to-session working artifacts for v2's design process. Does not apply to project Master files (which follow their own convention — see §4.2) or to production PRISM skill files (which follow the canonical skill naming).

---

*End of Appendix D.*

---

## Appendix E — Mobile operator survival guide

v2 is mobile-first (§3.4). Mobile operators routinely encounter patterns — both frictions and effective interaction moves — that desktop operators either don't hit or don't need. This appendix catalogues two classes: **vendor-client workarounds** (concrete responses to LLM-vendor mobile-client limitations) and **operator interaction patterns** (ways of asking and navigating that are more valuable on mobile than on desktop). Living document: entries accumulate as patterns surface. The intent is honest accumulation, not release comprehensiveness — this matches v2's beta posture (§3.5). Report-worthy findings on untested substrates surface through the same channel.

Entries in this appendix may be surfaced inline as **in-context operator hints** at specific orchestration touchpoints — the Execution Envelope's `Operator hints` field (§4.1.1) and the *What's next* artifact (§4.3) — so an operator sees the relevant cue at the moment of acting rather than from memory of having read the appendix. The appendix is the catalog; inline hints are the just-in-time surfacing of whichever entries apply to the specific action.

Each entry names the **Problem** or **Situation**, the **Workaround** or **Pattern**, and **Why it works** (so an operator can extrapolate when the exact case doesn't match).

---

### Vendor-client workarounds

### E.1 — Samsung file explorer: LLM-downloaded files invisible until indexing catches up

**Platform:** Android, Samsung devices (tested: Galaxy S25+).

**Problem.** Files downloaded from LLM mobile apps land in the Downloads folder but do not appear in Samsung's built-in file manager immediately. The system's indexing is delayed; a file you just downloaded may not be visible to attach workflows for seconds to minutes. On the mobile-first workflow (download output from one LLM, attach to orchestration session), this stalls the loop.

**Workaround.** Install **MiX** (third-party Android file manager). MiX sees new files immediately, independent of Samsung's indexing. It also includes an HTML/Markdown reader ("HTML View") that renders `.md` artifacts in place — useful for a quick sanity-check on an execution output before attaching it to orchestration.

**Why it works.** MiX does its own directory scanning rather than relying on the system indexing service. Same filesystem, different reader; the file exists the moment the LLM app finishes writing it, and MiX respects that.

### E.2 — Broken file/clipboard operations in LLM mobile apps

**Platform:** Android, varies by LLM vendor mobile app.

**Problem.** Some LLM mobile apps have incomplete implementations of basic operations: copy-to-clipboard from rendered outputs, file download of generated artifacts, attachment of certain file types. The exact failures vary by vendor and change with app updates, but the class of failure is consistent enough to plan around. Tested, broken examples at rev. 6 release include ChatGPT mobile's clipboard fidelity on fenced content (§4.1.1) and inconsistent download behavior across vendors.

**Workaround.** Open the same vendor in **Firefox with Desktop Mode enabled** on the mobile device. Desktop web rendering of the vendor's site is typically more complete than the native mobile app for these operations, and the actions that fail in-app usually succeed in the desktop-rendered web version. Costs some UX friction (smaller tap targets, scrolling) but unblocks otherwise-impossible mobile workflows.

**Why it works.** Vendors' desktop web clients are generally more mature and more uniformly implemented than their mobile apps; browser rendering exposes the full web client regardless of the device's form factor. Desktop Mode in Firefox spoofs the user-agent and viewport, convincing the vendor's site to serve the full-featured client.

---

### Operator interaction patterns

### E.3 — Artifact + handoff together: "present document with instructions"

**Situation.** A session produces a deliverable that will feed into another session's work (e.g., a walkthrough document that a fresh session will react to; a setup strategy that a fresh session will execute against). Requesting only the artifact leaves the operator to reconstruct the handoff from memory later, which introduces drift and loses precision about target model, session hygiene, attachment order, scope boundaries, and so on.

**Pattern.** Ask for the artifact **and** the accompanying handoff prompt in the same request. Example phrasing: *"Produce the walkthrough document and an accompanying handoff prompt I can paste into a fresh session."* Claude delivers both together; the handoff carries all the context the next-session operator needs (which model, which mode, which files to attach, what's in/out of scope), so there is no reconstruction step later.

**Why it works.** Paired delivery creates self-contained packages that travel together. The artifact is the deliverable; the handoff is the operating context. Separating them is a mild form of session-forgetting (the context is in the producing session's head; it has to be reconstructed when the consumer session opens). Asking for both in one shot eliminates the reconstruction step and leverages the producing session's still-fresh context. This pattern pairs naturally with the Execution Envelope discipline (§4.1.1) — same instinct, different altitude: bake operating context into the artifact.

### E.4 — Session retrieval: "point me to the relevant session"

**Situation.** PRISM work routinely crosses sessions (artifact produced in session A, used in session B). When an operator is in the wrong session, or can't remember which session holds which artifact, mobile manual navigation of the Claude chat list is slow — previews are short, built-in search is limited, scrolling is tedious on a phone.

**Pattern.** Ask Claude directly: *"point me to the session where [topic] happened"* or *"give me a clickable link to the [topic] session."* Claude runs `conversation_search` on the topic, identifies the referenced session, and returns a `https://claude.ai/chat/{uuid}` URL. One tap to navigate. Works when you don't remember the session title but do remember the topic.

**Why it works.** Claude has past-conversations search as a built-in tool and can construct canonical session URLs from the UUIDs it returns. Faster and more precise than mobile manual navigation. The pattern also works as a disambiguation aid — if multiple sessions match the topic, Claude can enumerate them with brief summaries before committing to a link.

**Caveat — bounded-search disclosure (SP-12).** Past-conversations search is scoped: if the operator is in a project, search is confined to that project's chats; otherwise it covers non-project chats. If the target session lives in a different scope, the search returns null. Claude surfaces this bound rather than asserting a global null — *"I didn't find it within this project's conversation scope; the session may live in a different project or outside projects; confirm before I conclude it doesn't exist."* The operator can then redirect the search (move out of the project, switch projects) or surface the session manually.

### E.5 — Persisting artifacts across device/session loss

**Situation.** Mobile operators work primarily through vendor apps. Execution outputs downloaded to the device live in local storage, which is subject to events desktop operators rarely hit: device reset, app storage clear, accidental delete, storage-quota cleanup, OS update churn. Even absent those events, the mobile Downloads folder accumulates cruft — overlapping versions, vendor-default filename collisions, stale artifacts from prior sessions — that makes finding the right file its own failure mode, harder than on a desktop where file-manager workflows are more mature. An artifact that survives the dispatch session can be gone, or effectively lost in the pile, by the next orchestration turn if nothing external to the device holds a structured copy. On a multi-session project, losing one converged output is expensive; losing the Master is a project-reset event.

**Pattern.** Save execution outputs to a cloud drive (Google Drive, Dropbox, OneDrive, or equivalent) immediately after download, before switching to the next vendor or ending the session. Same move for the Master at session close: cloud-save before dismissing the orchestration session. Project-scoped folders on the cloud drive keep versions separated and retrievable by name; superseded artifacts are archived rather than deleted so the audit trail stays intact across the project's lifetime. The local copy stays available for the immediate next attach step; the cloud copy is the durable record. Works well as an inline Operator hint in the Execution Envelope — *"Save output to cloud drive after download, before switching to the next vendor (see E.5)"* — surfaced at exactly the moment the artifact exists and is most at risk.

**Why it works.** Cloud drives survive the device events local mobile storage does not, and structured project folders give the operator a navigable home rather than the flat Downloads-folder pile — the artifact becomes retrievable from any replacement device, from desktop, and from any session where the operator needs to re-attach it. On desktop substrates this pattern is often redundant (the local filesystem is already backed up and file-manager workflows are more usable); on mobile it is load-bearing, and the cost of the extra tap is negligible. Fits the mobile-first substrate (§3.4): the framework does not assume a durable or navigable local filesystem the way desktop-centric workflows implicitly do, and the cloud-drive step closes that gap without imposing a cost on desktop operators who already have persistent, organized local storage.

---

*End of Appendix E.*
