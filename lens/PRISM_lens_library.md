# PRISM Lens Library — v0.16 (pre-release)

**Version:** 0.16
**Release date:** 2026-06-28
**Status:** pre-release standalone artifact; awaiting real-world calibration before promotion to v1.0 stable
**Scope:** framework-neutral reference catalog; not a methodology, not a rubric, not framework-specific

---

## What this is

The PRISM Lens Library is a reference catalog of 27 audit-scope lenses. Each entry is a (material-question × evidence-class × specialist-type) triple that names a specific class of silent omission an audit can plausibly miss.

The Library is used as a coverage map at scope-definition time. For a given audit subject, an auditor evaluates every lens against the subject:

- **Universal lenses** (LL-U-*) fire always-on, on every engagement.
- **Domain lenses** (LL-D-*) fire when their `trigger:` predicate is met by the subject.

Each fire is tri-state:

- **fires-covered** — the lens's concern is already addressed by a planned scope pass.
- **fires-uncovered** — the lens's concern applies but no scope pass addresses it. Flag for inclusion.
- **fires-maybe** — the lens's concern applies at the edge. Operator judgment warranted, informed by subject detail.
- **doesn't-fire** — the trigger predicate is not met; no action.

The gap between fired-lenses and covered-lenses is the silent-omission risk.

## What this is not

- Not a methodology. It does not describe how to run an audit, what order to work in, or how to weight findings.
- Not framework-specific. Integration into any particular audit framework is a separate effort.
- Not self-updating. Version-pinned rubric anchors require human-verified currency checks before depth use.
- Not a completeness guarantee. It catches known silent-omission categories, not unknown-unknowns.
- Not a substitute for specialist competence. A lens flags that a specialist pass should be in scope; it does not ensure the pass is executed well.

## Known limitations

1. **Weak-brief blind spot.** If a subject brief understates facts so that domain predicates fail to fire (a hidden jurisdiction, an undersold efficacy claim, an unreported custody function), the triggering lens stays silent. The Library relies on honest brief population.
2. **Execution-quality blind spot.** A specialist pass included in scope but executed incompetently still checks the box. The Library catches scope-level omissions only.
3. **Novel-subject blind spot.** Subjects whose failure modes don't match any covered category may slip past the catalog entirely.
4. **Anchor currency.** Two entries carry version-pinned rubric anchors (LL-D-002 WCAG 2.2, LL-D-005 OWASP ASVS 5.0.0). At v0.10, both anchored entries carry `verification_basis: schema-introduction-only` to signal that `last_verified: 2026-04-24` reflects schema-introduction date, not an independently performed currency check. Run point refresh (per the adopting framework's Setup) before applying those lenses at the depth the anchor implies. The `verification_basis` field flips to `independent-review` after a real currency review is performed.
5. **Pack structure is a convention.** Lenses are grouped into six domain packs as a readability aid. The assignment rule is primary-failure-surface dictates placement; cross-pack concerns are handled via other lenses' triggers. Packs are not orthogonal by construction.

---

## Schema

Every entry uses the following fields:

- `id:` stable identifier of the form LL-{U|D}-NNN
- `name:` short question (the lens's colloquial title)
- `material_question:` the audit-scope question this lens forces scope to answer
- `tier:` universal | domain
- `trigger:` `always-on` (universal) or a predicate (domain)
- `evidence_class:` document | trace | probe | empirical-test | expert-interview | cross-check
- `specialist_type:` the specialist role the lens's pass would typically require (open taxonomy)
- `rubric_anchor:` optional — a version-pinned external rubric the lens recommends binding to
- `last_verified:` populated on entries carrying `rubric_anchor:`
- `verification_basis:` populated on entries carrying `last_verified:`; one of `{schema-introduction-only, independent-review}`. Gates freshness logic in adopting frameworks: a `schema-introduction-only` basis must not be treated as fresh on the strength of date alone
- `recommended_sources:` optional — a framework-curated list of external reference sources this lens recommends consulting, each bound to the lens's material question. Populated only on lenses with a high-signal source; absent on the rest (like `rubric_anchor:`). Each source record carries:
  - `source:` the named corpus or reference
  - `kind:` one of `{narrative, structured-record}`
  - `access:` one of `{open-web, operator-authenticated}`
  - `framing:` MANDATORY — the bias or handling caveat that must travel with any use of the source
  - `recency:` MANDATORY — the source-scoped era/recency posture (how the source's currency bears on its use; distinct from any lens-level findings-recency)
  - `answers:` the lens material-question(s) this source helps address
- `informed_by:` frameworks, standards, and practice traditions that inform the lens (indicative, not exhaustive; not a compliance claim)
- `failure_mode:` the silent omission this lens catches, in plain language
- `minimum_scope_binding:` the minimum scope commitment that counts as "covered" for this lens
- `scope_integrity_probe:` optional — a sharpened, lens-specific falsifier an adopting framework can pose at coverage time to test whether `minimum_scope_binding:` was genuinely satisfied rather than asserted. When present it overrides any generic scope-completeness challenge the adopting framework derives from `minimum_scope_binding:`; populated only on lenses with a ground-truth worked miss, absent on the rest (like `rubric_anchor:`). Backward-compatible: entries without it remain valid.

---

## Universal lenses (5 entries)

```yaml
- id: LL-U-001
  name: Who gets hurt?
  material_question: >
    Which people, groups, or roles bear material
    downside if this subject ships, continues, or
    is acted on as currently framed — including
    parties outside the buying audience?
  tier: universal
  trigger: always-on
  evidence_class: cross-check
  specialist_type: engagement lead / stakeholder analyst
  rubric_anchor: ~
  informed_by:
    - ISO 31000:2018 (stakeholder concept)
    - OECD Regulatory Impact Analysis (counterfactual harm)
    - IIA Standards (materiality)
  failure_mode: >
    Audit recommends ship, continue, or invest
    without naming who absorbs the downside or
    where harm lands unevenly; harmed parties
    surface post-launch.
  minimum_scope_binding: >
    At least one pass enumerates affected
    stakeholders and names at least one whose
    interests cut against the main thesis.

- id: LL-U-002
  name: What's the thesis?
  material_question: >
    What specific claim, decision, or defense is
    the audit testing — stated clearly enough
    that a finding could refute it?
  tier: universal
  trigger: always-on
  evidence_class: document
  specialist_type: engagement lead / audit methodologist
  rubric_anchor: ~
  informed_by:
    - PICO / PICOT (answerable-question structure)
    - PCAOB AS 2101 / ISA 300 (audit planning)
    - IIA Standards (engagement objectives)
  failure_mode: >
    Scope produces findings that cannot be refuted
    because the thesis was never stated; audit
    becomes a tour of the subject rather than a
    test of a proposition.
  minimum_scope_binding: >
    Scope names the thesis or decision under test
    in one sentence, and lists the evidence
    classes that would falsify it.

- id: LL-U-003
  name: What would refute?
  material_question: >
    What plausible observation, rival explanation,
    or contrary evidence would make the current
    thesis materially weaker or false, and where
    would that evidence be found?
  tier: universal
  trigger: always-on
  evidence_class: cross-check
  specialist_type: engagement lead / audit methodologist
  rubric_anchor: ~
  informed_by:
    - Cochrane RoB 2 (risk-of-bias structure)
    - GRADE (certainty-of-evidence tiers)
    - PCAOB / ISA audit-risk model
  failure_mode: >
    Audit becomes confirmatory and collects only
    evidence that agrees with the draft view;
    replication or second opinion trivially
    overturns it.
  minimum_scope_binding: >
    Scope names at least one disconfirming path
    and where that path would be checked.

- id: LL-U-004
  name: Who acts on this?
  material_question: >
    Who is the audit output written for, and what
    decision does it feed? Shape, depth, and tone
    should follow from that decision and its stakes.
  tier: universal
  trigger: always-on
  evidence_class: document
  specialist_type: engagement lead / audit communications
  rubric_anchor: ~
  informed_by:
    - IIA Standards (engagement communication)
    - PCAOB AS 1301 (communication with audit committees)
    - Decision-analysis tradition
  failure_mode: >
    Audit is technically correct but operationally
    useless because its depth, vocabulary, or
    framing does not match the decision it was
    supposed to serve.
  minimum_scope_binding: >
    Scope names the decision-maker, the decision,
    the deadline, and the cost of getting it wrong
    in each direction.

- id: LL-U-005
  name: What laws touch this?
  material_question: >
    Which legal, regulatory, or supervisory regimes
    plausibly apply to this subject, and does any
    rise to material depth requiring a specialist
    pass?
  tier: universal
  trigger: always-on
  evidence_class: document
  specialist_type: regulatory counsel (screening) / compliance analyst
  rubric_anchor: ~
  informed_by:
    - OECD Regulatory Impact Analysis (regulatory surface)
    - IIA Standards (compliance scope)
    - General compliance-audit tradition
  failure_mode: >
    Audit ships without having asked whether any
    law applies; material regulatory surface
    (privacy, advertising, discrimination,
    sector-specific) is discovered by a regulator,
    not the audit.
  minimum_scope_binding: >
    A regulatory screening pass is present in
    scope, naming plausibly applicable regimes and
    marking each as "material, specialist pass
    required" or "screened, immaterial" with reason.
```

---

## Domain lenses (22 entries across 6 packs)

### Pack 1 — Using the product

**Trigger:** `predicate: end users directly interact with a UI, workflow, or content experience`

```yaml
- id: LL-D-001
  name: Can they finish?
  material_question: >
    Can a target user move from entry to intended
    outcome without confusion, dead ends, or
    avoidable abandonment?
  tier: domain
  trigger: >
    predicate: end users must complete a sequence
    of actions to realize the subject's value
  evidence_class: empirical-test
  specialist_type: UX researcher / usability analyst
  rubric_anchor: ~
  informed_by:
    - Nielsen's 10 Usability Heuristics
    - ISO 9241-11 (usability definition)
  failure_mode: >
    Scope reviews features but misses a broken
    critical path that blocks conversion or task
    completion; production telemetry surfaces the
    failure, not the audit.
  minimum_scope_binding: >
    One pass maps at least one critical journey
    end to end and either tests it with
    representative users or reviews telemetry
    against success criteria.

- id: LL-D-002
  name: Can anyone use?
  material_question: >
    Can users with sensory, motor, cognitive,
    language, or assistive-technology constraints
    actually operate this product for its intended
    task?
  tier: domain
  trigger: >
    predicate: subject has a user interface
    intended for broad or public user populations
  evidence_class: probe
  specialist_type: accessibility auditor (WCAG-qualified)
  rubric_anchor: >
    WCAG 2.2 (October 2023); access mode:
    conformance audit combining automated scanning
    and manual assistive-technology testing
  last_verified: 2026-04-24
  verification_basis: schema-introduction-only
  informed_by:
    - WCAG 2.2
    - ARIA Authoring Practices
    - EN 301 549 (EU ICT accessibility)
  failure_mode: >
    Product launches excluding a meaningful
    fraction of users and exposes the sponsor to
    disability-discrimination liability.
  minimum_scope_binding: >
    An accessibility pass is present, names a
    target conformance level with version pin,
    and includes both automated and manual
    testing.

- id: LL-D-003
  name: Is guidance sound?
  material_question: >
    Where the product delivers expert content,
    advice, or recommendations, is that content
    accurate, current, and fit for the audience's
    stakes?
  tier: domain
  trigger: >
    predicate: subject provides instructional,
    advisory, editorial, or evaluative content
    that could materially shape user action
  evidence_class: expert-interview
  specialist_type: domain subject-matter expert (e.g., clinician, CFP, career counselor, as matched to content domain)
  rubric_anchor: ~
  informed_by:
    - GRADE
    - EEF toolkit (evidence of effect)
    - Cochrane (where clinical overlap)
    - Editorial-standards tradition
  failure_mode: >
    Polished experience passes as quality while
    the underlying guidance is wrong, outdated, or
    mis-scoped; users act on it at their cost.
  minimum_scope_binding: >
    One pass samples high-impact guidance against
    independent references or qualified
    subject-matter reviewers, with a sampling
    plan and accuracy criteria.

- id: LL-D-019
  name: Who said otherwise?
  material_question: >
    Does every uninvited frame in the document
    under review — a negation, a defensive
    intensifier, or a temporal hedge — answer
    a live alternative the reader demonstrably
    brings, rather than planting a doubt or
    trajectory nobody raised?
  tier: domain
  trigger: >
    predicate: subject is or includes a prose
    deliverable — report, pitch, marketing or
    position copy, expository document — whose
    framing shapes reader belief or action
  evidence_class: document
  specialist_type: communications editor / framing reviewer
  rubric_anchor: ~
  informed_by:
    - Lakoff, "Don't Think of an Elephant!" (frame activation by negation)
    - Misinformation-correction research (negation reinforces familiarity)
    - Plain-language editorial tradition
  failure_mode: >
    Scope reviews the document's claims but
    never audits its framing devices;
    uncalled-for denials plant the frames
    they deny, defensive intensifiers
    ("real", "actual", "truly") imply doubts
    nobody raised, and temporal hedges ("for
    now", "currently") concede adverse
    trajectories the evidence never put on
    the table.
  minimum_scope_binding: >
    One pass enumerates every negation ("not
    Y", "X, not Y", "rather than Y", "no Y"),
    defensive intensifier ("real", "actual",
    "genuine", "truly", "clearly"), and
    temporal hedge ("for now", "today",
    "currently") in the deliverable and tags
    each as called-for (naming the live
    alternative it answers) or uncalled-for
    (flagged for positive, informative
    rewrite). Where the positive verb already
    bounds the claim ("shrink", "slow",
    "narrow"), a trailing denial of the
    unbounded case is uncalled-for by
    default; inside a section whose explicit
    job is worst-case assessment, the extreme
    is a called question. Headings, titles,
    and opening sentences audited first.

- id: LL-D-020
  name: Help or ammunition?
  material_question: >
    Read sentence by sentence as the named
    audience — analyst, quant, banker, per the
    document's audience line — does every
    sentence make sense, read clearly, and
    land as positive or at least defensible
    for the subject, rather than handing a
    hostile expert ammunition?
  tier: domain
  trigger: >
    predicate: subject is or includes a prose
    deliverable addressed to a named expert
    audience whose reading affects the
    subject's interests
  evidence_class: document
  specialist_type: named-audience expert reviewer (hostile-but-fair posture)
  rubric_anchor: ~
  informed_by:
    - Hostile-review / red-team editorial practice
    - Equity-research and credit-memo review conventions
    - Plain-language editorial tradition
  failure_mode: >
    The deliverable is reviewed for accuracy
    but never read as its audience reads it;
    a sentence that is true and clear still
    hands a hostile-but-fair expert
    ammunition — an implied arithmetic that
    computes against the subject, a framing a
    quant reads as evasion — and the audit
    passes what the audience punishes.
  minimum_scope_binding: >
    One pass reads every sentence through
    three lenses in order: (1) does it make
    sense; (2) is it clear, preferring the
    plain word over compressed jargon;
    (3) read as the named audience, is it
    problematic or positive for the subject —
    recomputing any arithmetic the sentence
    implies and asking what a hostile-but-
    fair expert does with it. Findings route
    to rewrite, with the triggering lens
    named.

- id: LL-D-021
  name: Does a stranger follow?
  material_question: >
    Can a zero-context reader resolve every
    referent in the document — every quoted
    figure attributed, every acronym defined
    at first use, every premise the logic
    depends on stated on the page — without
    access to anything the author knows but
    the page omits?
  tier: domain
  trigger: >
    predicate: subject is or includes a prose
    deliverable intended to travel beyond its
    authors, reaching readers who arrive
    without the production context
  evidence_class: document
  specialist_type: cold reader / new-to-file editor
  rubric_anchor: ~
  informed_by:
    - Technical-writing review practice (cold-read pass)
    - Curse-of-knowledge research (Camerer et al.; Heath & Heath framing)
    - Plain-language editorial tradition
  failure_mode: >
    Everyone who reviews the document already
    knows the context, so nobody notices the
    often-quoted figure quoted nowhere, the
    acronym never defined, or the unstated
    premise an entire calculation silently
    assumes — a report whose export-limit
    arithmetic depended on the company's home
    jurisdiction, stated nowhere — until a
    real stranger reads it.
  minimum_scope_binding: >
    One pass reads the deliverable as a
    zero-context stranger: every third-party
    claim attributed (quoted where, by whom),
    every acronym defined at first use,
    insider jargon expanded, and every
    premise the document's logic depends on
    stated on the page. Headings and opening
    sentences audited first; unresolved
    referents and unstated premises route to
    rewrite.

- id: LL-D-022
  name: Does this respect the reader?
  material_question: >
    Does every sentence earn its place — would
    the reader lose something real if it were
    cut — or is the deliverable padded with
    filler that spends the reader's attention
    and returns nothing: empty preambles, the
    prompt restated back, contentless
    transitions, and qualifiers that hedge
    without informing?
  tier: domain
  trigger: >
    predicate: subject is or includes a prose
    deliverable — report, pitch, marketing or
    position copy, expository document — whose
    length the reader must spend attention on
  evidence_class: document
  specialist_type: line editor / substantive editor (reader-advocate posture)
  rubric_anchor: ~
  informed_by:
    - Strunk & White and Zinsser editorial tradition ("omit needless words"; clutter)
    - Plain-language editorial tradition
    - Generated-text review practice (boilerplate and filler detection)
  failure_mode: >
    The deliverable is reviewed for accuracy but
    never for whether it respects the reader's
    time. Empty openers ("in today's
    landscape"), the brief restated as if new,
    contentless transitions, and qualifier-
    padding each survive because each is
    individually harmless — and the reader, half
    of whose attention bought nothing, reads the
    author (or the tool that drafted it) as not
    having cared enough to cut.
  minimum_scope_binding: >
    One pass reads every paragraph asking what
    the reader loses if it is removed: each
    empty preamble, restated prompt, contentless
    transition, redundant restatement, and
    content-free hedge is flagged to cut or
    justify. Openings and each section's first
    paragraph are audited first, where filler
    concentrates; substance is preserved while
    length is never defended for its own sake.
```

### Pack 2 — Running the system

**Trigger:** `predicate: software, data processing, or model behavior materially affects delivery or outputs`

```yaml
- id: LL-D-004
  name: Will it hold up?
  material_question: >
    Under realistic load, failure, and maintenance
    conditions, will the system keep producing
    the intended result?
  tier: domain
  trigger: >
    predicate: backend services, integrations, or
    model/runtime behavior materially affect user
    outcome
  evidence_class: trace
  specialist_type: SRE / reliability engineer
  rubric_anchor: ~
  informed_by:
    - ISO/IEC 25010:2011 (software quality)
    - Google SRE principles (reliability, error budgets)
    - NIST CSF 2.0 (identify/protect structure)
  failure_mode: >
    Audit signs off on a demoable system that
    degrades under production reliability,
    performance, or maintenance pressure;
    scaling failures later attributed to market.
  minimum_scope_binding: >
    One pass inspects architecture, failure
    handling, performance, and maintainability
    under realistic conditions.

- id: LL-D-005
  name: Can attackers get in?
  material_question: >
    Could a reasonably capable attacker or abusive
    user compromise accounts, data, or core
    functions through the application as shipped?
  tier: domain
  trigger: >
    predicate: subject stores accounts, user data,
    money, or privileged actions, or is publicly
    deployed with attacker-reachable surface
  evidence_class: probe
  specialist_type: AppSec engineer / penetration tester
  rubric_anchor: >
    OWASP ASVS 5.0.0 (May 2025); access mode:
    requirements-based verification plus focused
    security testing at appropriate level
  last_verified: 2026-04-24
  verification_basis: schema-introduction-only
  informed_by:
    - OWASP ASVS 5.0.0
    - OWASP Top 10
    - NIST SSDF 1.1
    - MITRE ATT&CK (adversary behavior model)
  failure_mode: >
    Audit misses exploitable weaknesses in auth,
    session handling, input processing, or data
    exposure; first external researcher or
    attacker finds what the audit would have.
  minimum_scope_binding: >
    One pass verifies core security controls or
    maps them to an equivalent security
    verification scheme at a stated level.

- id: LL-D-006
  name: How would it fail?
  material_question: >
    How can the system's outputs be manipulated,
    misled, abused, or weaponized under
    adversarial, edge-case, or misuse conditions?
  tier: domain
  trigger: >
    predicate: subject produces personalized,
    ranked, model-mediated, or otherwise gameable
    outputs with real user consequences
  evidence_class: probe
  specialist_type: red team / adversarial-ML specialist
  rubric_anchor: ~
  informed_by:
    - MITRE ATLAS (adversarial ML)
    - NIST AI RMF 1.0
    - NIST AI 600-1 (generative AI risk profile)
    - FAIR (threat-scenario quantification)
  failure_mode: >
    Harmful edge-case behavior, leakage, or abuse
    pathways stay invisible until live users
    discover them; abuse scenarios never
    structured before launch.
  minimum_scope_binding: >
    One pass runs structured misuse, edge-case,
    or adversarial scenarios against high-stakes
    outputs and documents the threat model.

- id: LL-D-007
  name: What relies on others?
  material_question: >
    Which third-party APIs, external libraries,
    data feeds, or upstream dependencies must
    remain available and trustworthy for the
    subject's core loop to function?
  tier: domain
  trigger: >
    predicate: subject's core functionality
    depends on external APIs, data feeds, or
    third-party libraries that the sponsor does
    not control
  evidence_class: trace
  specialist_type: supply-chain / third-party risk analyst
  rubric_anchor: ~
  informed_by:
    - NIST CSF 2.0 (supply-chain function)
    - NIST SP 800-161 (supply-chain risk)
  failure_mode: >
    Audit exhaustively tests first-party code but
    misses that the core loop breaks when a
    single external API degrades, changes terms,
    or goes down.
  minimum_scope_binding: >
    One pass inventories external dependencies,
    identifies the critical path through them,
    and names at least one failure scenario with
    mitigation.

- id: LL-D-015
  name: Can you see it?
  material_question: >
    Can operators see what the system is doing in
    production well enough to detect problems,
    diagnose incidents, and support scale-up —
    and is that visibility matched to the system's
    maturity and blast radius?
  tier: domain
  trigger: >
    predicate: subject runs production services
    whose behavior, latency, error rate, or
    output quality must be monitored for
    operational or business continuity
  evidence_class: trace
  specialist_type: SRE / platform engineer
  rubric_anchor: ~
  informed_by:
    - Google SRE principles (observability, SLIs/SLOs)
    - OpenTelemetry (instrumentation patterns)
    - ISO/IEC 25010:2011 (operability)
  failure_mode: >
    Product runs but nobody can tell whether it
    is working; incidents surface via user
    reports rather than internal detection, and
    scale-up proceeds blind.
  minimum_scope_binding: >
    One pass inspects observability stance —
    logs, metrics, and traces coverage of
    critical paths; alerting on user-visible
    symptoms; and SLO/SLI maturity against the
    system's current stage.

- id: LL-D-016
  name: Is the ledger safe?
  material_question: >
    Where the subject holds user funds, settles
    payments, or records balances, are the
    ledger, reconciliation, and anti-fraud
    controls rigorous enough to prevent loss,
    theft, or silent corruption?
  tier: domain
  trigger: >
    predicate: subject custodies user funds,
    operates a digital wallet, processes
    payments directly, or records financial
    balances that users rely on
  evidence_class: trace
  specialist_type: financial-systems auditor / ledger engineer / SOC 1 reviewer
  rubric_anchor: ~
  informed_by:
    - SOC 1 (ICFR-relevant controls)
    - PCI DSS (where card data in scope)
    - Double-entry accounting and reconciliation practice
  failure_mode: >
    Ledger quietly drifts from reality; users
    lose funds to fraud, reconciliation errors,
    or adversarial manipulation of balance state
    because no one verified custodial controls
    end-to-end.
  minimum_scope_binding: >
    One pass inspects ledger integrity,
    reconciliation cadence, anti-fraud controls,
    and custody/segregation of user funds; at
    least one end-to-end transaction trace is
    verified.
```

### Pack 3 — Getting chosen

**Trigger:** `predicate: subject competes for adoption, revenue, budget, or strategic attention`

```yaml
- id: LL-D-008
  name: Compared to what?
  material_question: >
    Against the user's realistic alternatives —
    including substitutes and do-nothing — where
    is this materially better, worse, or merely
    different?
  tier: domain
  trigger: >
    predicate: users or buyers have realistic
    substitute products, workflows, or
    status-quo options
  evidence_class: cross-check
  specialist_type: competitive analyst / market researcher
  rubric_anchor: ~
  recommended_sources:
    - source: ideas.rip
      kind: narrative
      access: open-web
      framing: >
        Founder-selection bias; retrospective failure
        narratives optimized for teaching. Funded ≠
        correct — a documented startup is a survivor of
        the funding filter, not a validated answer.
      recency: >
        Era-conditional: capital-climate and
        category-maturity details age; substitution
        patterns are more durable. Weight recent cases
        for current priors.
      answers: >
        Substitute and do-nothing enumeration for an
        audience-job pair: what realistic alternatives
        a comparable subject was measured against.
    - source: Failory
      kind: narrative
      access: open-web
      framing: >
        Founder-interview and post-mortem corpus;
        failure-selection plus interview-subject
        self-presentation bias. Funded ≠ correct, and a
        founder's own account — of who they lost to, or
        why the money ran out — is a claim, not a finding.
      recency: >
        Era-conditional: competitive sets, capital
        climate, and cost structures in any case age; the
        substitution and failure dynamics they reveal are
        more durable. Weight recent cases for current priors.
      answers: >
        Substitute and lost-to enumeration from the
        loser's side: which realistic alternatives a
        comparable subject was actually displaced by.
    - source: pitch-deck libraries
      kind: narrative
      access: open-web
      framing: >
        Survivor bias — how a category presents itself
        to investors, not ground truth. Funded ≠
        correct. Premium tiers are paywalled; the
        free corpus is browsable; open libraries
        include bestpitchdeck.com.
      recency: >
        Era-conditional: deck conventions evolve with
        capital climate and category maturity. Match
        the library era to the question's era.
      answers: >
        "Compared to what?" framing patterns — how
        comparable subjects name their competitive set
        and differentiate against substitutes.
    - source: CB Insights / PitchBook / Tracxn
      kind: structured-record
      access: operator-authenticated
      framing: >
        Coverage gaps by region, stage, and era;
        stealth rounds absent and bootstrapped
        companies under-represented. Classification
        quality is platform-decided. Funding ≠
        business signal. Access via employer or
        library subscriptions; do not gatekeep on a
        free-only basis.
      recency: >
        Continuously updated, so the question is not
        "is this stale?" but "what historical depth
        does it carry, and does it cover my era?"
      answers: >
        Competitor and comparable-population selection:
        which firms constitute the realistic
        alternative set for the audience-job pair.
    - source: Start-Up Nation Central — Finder
      kind: structured-record
      access: open-web
      framing: >
        Deep, continuously-updated structured source for
        the Israeli tech ecosystem (startups, investors,
        multinationals, funding and M&A activity). Not a
        merely-regional record: in sectors where Israel
        leads — cybersecurity above all, and deep-tech
        broadly — its companies are global category
        innovators and disproportionately M&A targets
        (predominantly of U.S. acquirers), so the Israeli
        comparable, competitor, and acquirer set is
        materially relevant even for a non-Israeli subject
        in those sectors. Bias is depth-by-ecosystem:
        deepest on Israel-linked firms — pair with a
        global platform for full breadth. Free public tier
        plus deeper authenticated data; classification is
        platform-decided.
      recency: >
        Continuously updated with real-time company,
        funding, and M&A data, so the question is coverage
        scope, not staleness: deepest current coverage of
        the Israeli ecosystem and its global acquirer links.
      answers: >
        Comparable, competitor, and likely-acquirer
        enumeration: which firms make up the realistic
        alternative set, at a depth global platforms miss
        in Israel-led categories such as cybersecurity.
  informed_by:
    - Porter five-forces and strategy literature
    - Jobs-to-be-Done (substitute analysis)
    - Competitive-intelligence practice
  failure_mode: >
    Audit overstates novelty or fit because no
    realistic comparator set — especially
    substitutes and do-nothing — was named; a
    buyer-side read surfaces the gap. Common
    drift: category-bounded rival enumeration
    is mistaken for substitute analysis.
    Substitutes are defined by the audience and
    the job — not by product category — so a
    hardware device, a different workflow, or a
    do-nothing default can each be a substitute
    if it serves the same audience-job pair.
  minimum_scope_binding: >
    One pass names the audience and the job
    first, then names rivals, substitutes, and
    do-nothing as alternatives for that
    audience-job pair (substitutes defined by
    the job, not the product category);
    differentiation is stated in buyer-language
    and backed by evidence.
  scope_integrity_probe: >
    The named comparator set claims to cover
    this audience-job pair's realistic
    alternatives. Name at least one substitute
    that serves the same audience and the same
    job through a different form factor — a
    hardware device, a manual workflow, an
    adjacent-category product, or a do-nothing
    default — that the set omits. Pass only if
    either (a) at least one such audience-job
    substitute is named and incorporated, or
    (b) its absence is documented with explicit
    rationale for why no cross-form-factor
    substitute serves this audience-job pair.

- id: LL-D-009
  name: Does it pay back?
  material_question: >
    Can the subject sustain itself financially or
    operationally without assuming unreal
    conversion, retention, cost, or staffing
    behavior?
  tier: domain
  trigger: >
    predicate: audit must judge commercial
    viability, unit economics, or sustainability
    of the operating model
  evidence_class: document
  specialist_type: unit-economics analyst / FP&A
  rubric_anchor: ~
  recommended_sources:
    - source: ideas.rip
      kind: narrative
      access: open-web
      framing: >
        Founder-selection bias; retrospective failure
        narratives optimized for teaching. Funded ≠
        correct — a documented startup is a survivor of
        the funding filter, not a validated answer.
      recency: >
        Era-conditional: capital-climate and
        category-maturity details age; substitution
        patterns are more durable. Weight recent cases
        for current priors.
      answers: >
        Demand-validation and willingness-to-pay priors:
        whether comparable subjects found a market that
        actually paid, and where demand assumptions
        broke down.
    - source: Failory
      kind: narrative
      access: open-web
      framing: >
        Founder-interview and post-mortem corpus;
        failure-selection plus interview-subject
        self-presentation bias. Funded ≠ correct, and a
        founder's own account — of who they lost to, or
        why the money ran out — is a claim, not a finding.
      recency: >
        Era-conditional: competitive sets, capital
        climate, and cost structures in any case age; the
        substitution and failure dynamics they reveal are
        more durable. Weight recent cases for current priors.
      answers: >
        Willingness-to-pay and burn post-mortems: where
        revenue, retention, or cost assumptions broke for
        comparable subjects, and how the runway ran out.
    - source: pitch-deck libraries
      kind: narrative
      access: open-web
      framing: >
        Survivor bias — how a category presents itself
        to investors, not ground truth. Funded ≠
        correct. Premium tiers are paywalled; the
        free corpus is browsable; open libraries
        include bestpitchdeck.com.
      recency: >
        Era-conditional: deck conventions evolve with
        capital climate and category maturity. Match
        the library era to the question's era.
      answers: >
        TAM/SAM/SOM construction patterns and
        demand-claim conventions: how comparable
        subjects sized their market and framed the
        revenue opportunity.
    - source: CB Insights / PitchBook / Tracxn
      kind: structured-record
      access: operator-authenticated
      framing: >
        Coverage gaps by region, stage, and era;
        stealth rounds absent and bootstrapped
        companies under-represented. Classification
        quality is platform-decided. Funding ≠
        business signal. Access via employer or
        library subscriptions; do not gatekeep on a
        free-only basis.
      recency: >
        Continuously updated, so the question is not
        "is this stale?" but "what historical depth
        does it carry, and does it cover my era?"
      answers: >
        Comparable transactions, valuations, and
        funding history as a market-sizing and
        commercial-viability cross-check.
    - source: Start-Up Nation Central — Finder
      kind: structured-record
      access: open-web
      framing: >
        Deep, continuously-updated structured source for
        the Israeli tech ecosystem, strongest on funding
        rounds, valuations, and M&A / exit activity.
        Israeli tech — cybersecurity especially — is a
        world leader in acquisitions, predominantly by
        U.S. companies, so its exit and transaction record
        is a globally material payback and market-sizing
        cross-check in those categories, not a regional
        footnote. Bias is depth-by-ecosystem (deepest on
        Israel-linked firms); funding ≠ business signal.
        Free public tier plus deeper authenticated data.
      recency: >
        Continuously updated with real-time funding and
        M&A data, so the question is coverage scope, not
        staleness: current depth on the Israeli ecosystem's
        rounds and exits.
      answers: >
        Comparable transactions, valuations, and exit /
        acquisition outcomes as a market-sizing and
        commercial-viability cross-check, with particular
        depth on Israel-led categories such as cybersecurity.
  informed_by:
    - SaaS unit-economics literature (CAC, LTV, payback)
    - OECD RIA (counterfactual analysis)
    - Valuation and forecast-audit practice
  failure_mode: >
    Audit recommends continuation or scaling on
    economics that fail outside optimistic
    assumptions; cash runs out before
    product-market fit.
  minimum_scope_binding: >
    One pass tests revenue, cost, conversion,
    retention, or staffing assumptions with
    sensitivity analysis on the two or three
    assumptions that dominate the outcome.
```

### Pack 4 — Proving results

**Trigger:** `predicate: subject makes causal, quantitative, comparative, or efficacy claims that could change behavior`

```yaml
- id: LL-D-010
  name: What's the evidence?
  material_question: >
    For each quantified efficacy or outcome claim,
    do the study design, sample, comparator,
    measurement, and reproducibility survive
    independent appraisal?
  tier: domain
  trigger: >
    predicate: subject or sponsor makes a measured
    outcome claim that could change buyer, user,
    regulator, or investor behavior
  evidence_class: cross-check
  specialist_type: evidence-synthesis methodologist / study-design reviewer
  rubric_anchor: ~
  informed_by:
    - Cochrane RoB 2 (risk of bias)
    - GRADE (certainty of evidence)
    - CONSORT (trial reporting)
    - PRISMA 2020 (synthesis reporting)
    - SPIRIT 2013 (study design)
  failure_mode: >
    Marketing claim is supported by a small,
    non-comparative, non-replicated internal
    study; the claim collapses on first external
    challenge because the audit never tested the
    underlying evidence.
  minimum_scope_binding: >
    One pass grades the strongest supporting
    evidence on design, sample, comparator,
    measurement, and reproducibility, then states
    the resulting confidence level.

- id: LL-D-017
  name: Is it clinically valid?
  material_question: >
    Where the subject makes a clinical,
    diagnostic, therapeutic, or physiological
    claim, does the evidence meet the clinical
    and regulatory standards for the relevant
    medical-device class and jurisdiction?
  tier: domain
  trigger: >
    predicate: subject performs a diagnostic,
    therapeutic, or physiological function, is
    marketed for medical use, or would plausibly
    meet the definition of a medical device
    under FDA, EU MDR, or comparable regime
  evidence_class: cross-check
  specialist_type: clinical regulatory reviewer / clinical biostatistician / medical device consultant
  rubric_anchor: ~
  informed_by:
    - ICH-GCP (clinical trial conduct)
    - FDA guidance on software as a medical device (SaMD)
    - IMDRF SaMD risk categorization
    - EU MDR (medical device regulation)
    - IEC 62304 (medical device software lifecycle)
  failure_mode: >
    Product makes a clinical claim supported by
    evidence that passes a general scientific-
    validity bar but fails the clinical-regulatory
    bar; regulator intervention, adverse events,
    or recall follow launch, and patients bear
    the downside.
  minimum_scope_binding: >
    One pass classifies the subject under the
    applicable medical-device regime, grades the
    clinical evidence against the required
    standard for that class, and verifies
    regulatory-submission adequacy.
```

### Pack 5 — Laws and rights

**Trigger:** `predicate: subject touches regulated data, advertising claims, automated decisions affecting users, employment, education, health, minors, or cross-border operations`

```yaml
- id: LL-D-011
  name: Is data handled lawfully?
  material_question: >
    Is each category of personal data collected,
    processed, stored, and shared on a defensible
    lawful basis, with consent patterns,
    retention, minimisation, and subject rights
    actually implemented?
  tier: domain
  trigger: >
    predicate: subject processes personal data,
    or special-category data such as health,
    disability, children's, biometric, financial,
    or employment data
  evidence_class: document
  specialist_type: DPO / privacy counsel
  rubric_anchor: ~
  informed_by:
    - GDPR / UK GDPR (lawful basis, rights)
    - ISO 27701 (privacy information management)
    - NIST Privacy Framework
    - CCPA / CPRA (US state privacy patterns)
  failure_mode: >
    Product is built on a consent or legal-basis
    pattern that fails scrutiny; regulator action,
    fines, or forced retooling follow launch, and
    the audit never examined it.
  minimum_scope_binding: >
    One pass covers lawful basis per data
    category, consent patterns, retention,
    cross-border transfer, and subject-rights
    implementation.

- id: LL-D-012
  name: Who does it disadvantage?
  material_question: >
    Does the subject's automated output, pricing,
    routing, or recommendation systematically
    disadvantage a group along a protected
    characteristic or legitimate interest?
  tier: domain
  trigger: >
    predicate: subject makes automated decisions,
    recommendations, prices, or routes that
    materially affect users
  evidence_class: empirical-test
  specialist_type: algorithmic-fairness analyst / civil-rights counsel
  rubric_anchor: ~
  informed_by:
    - NIST AI Risk Management Framework 1.0
    - EU AI Act (high-risk system framing)
    - US EEOC guidance on automated employment decisions
    - UK Equality Act 2010
    - ISO/IEC 24027 (AI bias)
  failure_mode: >
    Automated output produces disparate outcomes
    along age, gender, disability, or other
    protected lines; first external audit,
    journalist, or regulator surfaces the pattern.
  minimum_scope_binding: >
    One pass names the decision surface, the
    protected characteristics analysed, the
    metric used, and the thresholds for concern.

- id: LL-D-013
  name: Which rules apply where?
  material_question: >
    For each jurisdiction the subject operates in,
    which rules govern data residency, consumer
    protection, advertising substantiation,
    employment, and sector-specific regulation —
    and do the operational choices reflect them?
  tier: domain
  trigger: >
    predicate: subject operates across two or
    more regulatory jurisdictions, or markets
    quantified/comparative claims in any
    regulated jurisdiction
  evidence_class: document
  specialist_type: jurisdictional regulatory counsel / substantiation counsel
  rubric_anchor: ~
  informed_by:
    - GDPR / UK GDPR / CCPA-CPRA comparative practice
    - FTC advertising substantiation (US)
    - UK CAP / BCAP Codes, ASA precedent
    - EU Unfair Commercial Practices Directive
    - OECD cross-border data transfer guidance
  failure_mode: >
    Product applies its home-jurisdiction defaults
    abroad and violates a local rule no one
    examined — data residency, tax registration,
    local consent pattern, local advertising
    prohibition, or substantiation standard.
  minimum_scope_binding: >
    One pass names each live jurisdiction and
    the regimes triggered, including at least
    one requirement that materially cuts against
    current design or claim.

- id: LL-D-018
  name: Are kids protected?
  material_question: >
    Where minors use, are exposed to, or have
    data collected by the subject, are
    age-appropriate design, grooming-risk
    controls, parental-consent patterns, and
    child-specific safety features adequate —
    beyond the baseline privacy lawful basis?
  tier: domain
  trigger: >
    predicate: subject is likely to be accessed
    by minors, markets to minors, collects data
    from minors, or hosts content or interaction
    patterns where adult-minor contact or
    child-targeted harm is plausible
  evidence_class: cross-check
  specialist_type: child-safety specialist / age-appropriate-design (AADC) consultant
  rubric_anchor: ~
  informed_by:
    - UK ICO Age Appropriate Design Code
    - COPPA (US)
    - GDPR Article 8 (children's consent)
    - 5Rights Foundation design principles
  failure_mode: >
    Audit clears privacy and fairness gates but
    misses grooming risk, age-inappropriate
    monetization patterns, or absence of
    parental-consent flows; harm lands on
    children and draws regulatory and media
    response the sponsor cannot survive.
  minimum_scope_binding: >
    One pass evaluates age-appropriate design
    against applicable code(s), inspects
    grooming-risk surfaces (adult-minor contact
    channels, private messaging, user-generated
    content), and verifies parental-consent and
    age-verification patterns where required.
```

### Pack 6 — Physical context

**Trigger:** `predicate: device, sensor, location, bandwidth, or real-world environment materially changes behavior or risk`

```yaml
- id: LL-D-014
  name: Does context matter?
  material_question: >
    Do device, browser, network, location, or
    real-world use conditions materially change
    safety, usability, or performance?
  tier: domain
  trigger: >
    predicate: outcome quality or risk changes
    materially by device, browser, network,
    location, or physical environment
  evidence_class: probe
  specialist_type: field-conditions QA / real-world-testing analyst
  rubric_anchor: ~
  informed_by:
    - ISO/IEC 25010:2011 (context of use)
  failure_mode: >
    Audit signs off on desktop or lab behavior
    that breaks in the conditions where the
    subject is actually used.
  minimum_scope_binding: >
    One pass tests representative environments
    or explicitly justifies why context
    variation is immaterial.
```

---

## Summary counts

- **Total entries:** 27 (5 universal + 22 domain across 6 packs)
- **Rubric-anchored entries:** 2 (7.4%) — LL-D-002 (WCAG 2.2, October 2023), LL-D-005 (OWASP ASVS 5.0.0, May 2025)
- **`recommended_sources:`-bearing entries:** 2 (7.4%) — LL-D-008 ("Compared to what?"), LL-D-009 ("Does it pay back?")
- **`scope_integrity_probe:`-bearing entries:** 1 (3.7%) — LL-D-008 ("Compared to what?")
- **`specialist_type:` population:** 27 / 27
- **`last_verified:` population on anchored entries:** 2 / 2 (all dated 2026-04-24)
- **`verification_basis:` population on anchored entries:** 2 / 2 (all `schema-introduction-only` at v0.10; flips to `independent-review` after real currency review)

## Version and status

**v0.16 pre-release.** Awaiting at least one real-world calibration application before promotion to v1.0 stable. Calibration may occur either as standalone use on a real audit or through a framework-integration (Phase B) effort against a committed target audit framework.

v0.16 is an additive catalog bump on top of v0.15: one new domain lens plus a recommended-sources curation pass, no schema change. It adds LL-D-022 ("Does this respect the reader?") to Pack 1 — a reader-respect pass that flags filler which spends the reader's attention and returns nothing (empty preambles, the prompt restated back, contentless transitions, content-free hedges), completing the document-review family alongside LL-D-019/020/021. It also expands the `recommended_sources:` on the two source-bearing lenses: LL-D-008 ("Compared to what?") and LL-D-009 ("Does it pay back?") each gain Failory (a founder-interview and post-mortem corpus) and Start-Up Nation Central — Finder (a deep structured source for the Israeli tech ecosystem, globally material in Israel-led categories such as cybersecurity), and the existing pitch-deck-libraries source now names bestpitchdeck.com among its open examples. Each new source carries the mandatory `framing:` and `recency:` caveats; no schema change and no existing lens behavior changes beyond the two expanded source lists. Total entries 26 → 27 (5 universal + 22 domain).

v0.15 is an additive catalog bump on top of v0.14: two new domain lenses and one amended lens, no schema change. It broadens LL-D-019 ("Who said otherwise?") from negations alone to the full uninvited-frame family — negations, defensive intensifiers ("real", "actual", "truly"), and temporal hedges ("for now", "currently") — with a fast path for self-bounding verbs (a verb like "shrink" already bounds the claim, so a trailing denial of the unbounded case is uncalled-for by default) and an exception for sections whose explicit job is worst-case assessment, where the extreme is a called question. It adds LL-D-020 ("Help or ammunition?"), a per-sentence triple audit that reads a deliverable as its named expert audience reads it — sense, clarity, and effect for the subject, recomputing any implied arithmetic under a hostile-but-fair posture — and LL-D-021 ("Does a stranger follow?"), a cold-reader pass requiring every referent to resolve on the page: third-party claims attributed, acronyms defined at first use, and the premises the document's logic depends on stated rather than assumed. Both new lenses carry the standard fields only, and existing lenses beyond LL-D-019 are untouched. Total entries 24 → 26 (5 universal + 21 domain).

v0.14 is an additive catalog bump on top of v0.13: one new domain lens, no schema change. It adds LL-D-019 ("Who said otherwise?") to Pack 1 — a document-review lens that audits negation targeting in prose deliverables. Every negation must answer a live alternative the reader demonstrably brings (a common prior, a named risk, or an inference the document's own content invites); a denial of a belief nobody holds plants the very frame it denies, reads as defensive, and implies a critic nobody heard from. The lens carries the standard fields only — no rubric anchor, no recommended sources, no scope-integrity probe at introduction — and existing lenses are untouched, so v0.14 introduces no behavior change for them. Total entries 23 → 24 (5 universal + 19 domain).

v0.13 is an additive schema bump on top of v0.12: same 23 lenses, same triggers. It adds the optional `scope_integrity_probe:` field, which carries a sharpened, lens-specific falsifier an adopting framework poses at coverage time to test whether `minimum_scope_binding:` was genuinely satisfied rather than waved through. The field is populated on one lens (LL-D-008 "Compared to what?", whose category-vs-audience substitution trap has a ground-truth worked miss) and absent on the rest. Like `recommended_sources:`, it is optional and backward-compatible: entries without it remain valid and fall back to the generic scope-completeness challenge derived from `minimum_scope_binding:`, so v0.13 introduces no behavior change for existing lenses.

v0.12 is an additive schema bump on top of v0.11: same 23 lenses, same triggers. It adds the optional `recommended_sources:` field, which attaches a framework-curated list of external reference sources — each with a mandatory `framing:` and `recency:` caveat — to the lens's material question. The field is populated on two high-yield lenses (LL-D-008 "Compared to what?" and LL-D-009 "Does it pay back?") and absent on the rest. Like `rubric_anchor:`, it is optional and backward-compatible: entries without it remain valid, so v0.12 introduces no behavior change for existing lenses.

v0.11 is a lens-binding refinement on top of v0.10: same 23 lenses, no schema change. It sharpens LL-D-008 ("Compared to what?") to name the category-vs-audience substitution trap in `failure_mode`, and tightens `minimum_scope_binding` to require naming the audience and job before enumerating comparators — substitutes defined by the job, not the product category. The refinement is posture-facilitation, motivated by a real audit that reached a false-uniqueness finding after enumerating category-bounded rivals while an audience-defined substitute went unnamed.

v0.10 is a schema-fidelity bump on top of v0.9: same 23 lenses, same content, same triggers. The change is the addition of `verification_basis:` on the two rubric-anchored entries, gating any adopting framework's freshness logic against silently treating schema-introduction dates as performed currency checks.

Feedback, patches, and field-observations welcome. Ongoing currency of rubric anchors is the responsibility of the adopting framework or engagement; v0.16 ships with anchors current as of 2026-04-24 (`schema-introduction-only` basis) and does not include an automated currency-update mechanism.

*End of PRISM Lens Library v0.16.*
