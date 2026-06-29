<!-- PRISM v2.20.2 Skill bundle (on-demand reference). Corpus-access dispatch (section 4.13) — the investigation-posture Envelope for a targeted lookup against an external reference corpus, brought back caveat-attached. Fetch when the dispatch-builder classifies a pass as corpus-access.
     Generated from the assembled PRISM.md — edit PRISM.md, not this. -->

### 4.13 Corpus-access dispatch `[structural | review-if: corpus-access Phase 3 lands]`
<a id="section-corpus-access-dispatch"></a>

During a live engagement, a material question is sometimes best answered by an
*external reference corpus* — a startup-idea database, a pitch-deck library, a
funding-record service — rather than by a vendor reasoning from its own training.
Corpus-access dispatch is the **investigation-posture** Envelope that performs a
targeted lookup against such a source, scoped to the engagement's actual
question, and brings the result back caveat-attached. The corpus stays external
and is queried on demand; nothing is mined into the framework or a lens.

It is *investigation*, not execution: no prompt body is distributed across vendors
and there is no triangulation question, so the Envelope carries
`Posture: investigation` (§{section.prism-execution-envelope}, the Execution
Envelope) and none of the triangulation fields. That absence is what keeps a
retrieval step from masquerading as a judgment step.

**The Envelope.**

```
━━━ PRISM CORPUS-ACCESS ENVELOPE ━━━
Prompt ID:        [identifier — purpose/title]
Dispatch ID:      [unique per dispatch instance; copy verbatim]
Project:          [project name]
Master version:   [filename at dispatch]
Prompt digest:    [orchestration-generated; copy verbatim]
Posture:          investigation        ← no Dispatch shape exists
Source:           [named corpus]
Corpus kind:      narrative | structured-record
Source access:    open-web | operator-authenticated   ← routes the path
Driver:           vendor-executed | cowork-mcp | manual
Fan:              none | coverage (N)   ← coverage only; never equivalence
Tools:            web search ON [, Playwright]         ← vendor-executed path
Question:         [engagement question, scoped, self-contained]
Extract:          [exactly what to pull; fields / form]
Return form:      [finding structure]
Archive:          requested | none      ← screenshots / downloads / exports
Source framing:   [mandatory bias caveat — e.g. survivor bias]
Temporal frame:   [mandatory recency / coverage-window constraint]
Return handling:  [recall-merge; agreement = retrieval-consistency note]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Corpus-access fields.**

- `Source` — the named corpus (e.g. a startup-idea database, a funding-record
  service).
- `Corpus kind` — `narrative` (read/search corpora returning prose findings or
  artifact patterns) or `structured-record` (queryable databases returning
  records — funding rounds, comparable transactions). The kind conditions
  `Extract`, `Return form`, and `Temporal frame`; it is not a fork into two
  capabilities.
- `Source access` — `open-web` or `operator-authenticated`. Routes the lookup
  path (below).
- `Driver` — `vendor-executed | cowork-mcp | manual`. The locus that performs the
  retrieval (below).
- `Fan` — `none` or `coverage (N)`. A coverage fan retrieves the same material
  across N vendors for recall; it is **never** equivalence dispatch and never
  triangulates (see *Coverage fan*).
- `Tools` — on the vendor-executed path, the vendor tools the lookup requests
  (`web search ON`, optionally `Playwright`); rides the reserved `Tools:` slot
  (§{section.prism-execution-envelope}, the Execution Envelope).
- `Question` — the engagement question, scoped and **self-contained**
  (§{section.atomic-prompt-self-containment}, atomic-prompt self-containment): no
  bare PRISM shorthand, since the executing locus may not share PRISM context.
- `Extract` — exactly what to pull: fields/records for the structured-record
  kind, the prose finding or pattern for the narrative kind.
- `Return form` — the structure the finding comes back in (tabular for records,
  prose for narrative).
- `Archive` — `requested` or `none`. `requested` triggers the mandatory Exhibits
  manifest on return (§{section.prism-execution-output}, the Execution Output).
- `Source framing` *(mandatory)* — the bias caveat the source carries (e.g.
  survivor bias in a startup-idea corpus). Mandatory because a finding stripped of
  it is a silent-omission failure.
- `Temporal frame` *(mandatory)* — the recency / coverage-window constraint.
  Narrative corpora *age* (era-conditional vs durable: "is this stale?");
  structured-record databases are continuously updated ("what historical depth —
  does it cover my era?"). Same field, different question per kind.
- `Return handling` — how the return routes: recall-merge for a coverage fan,
  with agreement recorded as a retrieval-consistency note — never the Vendor
  Triangulation delta (§{section.vendor-triangulation}, Vendor Triangulation).

**Lookup-path `Driver` — a capability-local enum, distinct from the Axis-2
execution driver.** The corpus-access `Driver` answers a different question than
the Axis-2 execution-driver enum
(§{section.orchestration-driver-and-persistence-axes}, the orchestration / driver
/ persistence axes). Axis-2 (`manual | auto_drive`) governs *who moves the
Envelope into the execution vendor's chat* — the paste-driver. Corpus-access
`Driver` governs *what locus performs the retrieval against the source*. The two
compose orthogonally rather than collapsing: a `vendor-executed` lookup still
reaches the vendor via the paste-driver (Axis-2 `manual` today, `auto_drive`
later), so it is not a third Axis-2 value. The enum is therefore capability-local,
not an Axis-2 extension:

- `manual` — the operator runs the lookup in their own authenticated browser and
  pastes the result back. The universal fallback; coincides with Axis-2 `manual`
  (the operator does the legwork). Not surface-gated.
- `vendor-executed` — the lookup is dispatched to an execution vendor that
  performs it with its own **web search**, escalating to **Playwright**
  (vendor-side browser automation in its code-execution sandbox) when retrieval
  needs live page interaction. Rides the `Tools:` slot; orthogonal to the
  paste-driver. **Open-web only.** Not surface-gated.
- `cowork-mcp` — PRISM drives the Chrome MCP under the `cowork` surface
  (§{section.cowork-surface-capabilities}, the Cowork capability surface) to
  operate the source directly, including the operator's own authenticated session
  for paywalled sources. App-under-test-shaped, **not** `auto_drive`'s per-vendor
  machinery. `cowork`-gated; reserved for Phase 3.

**Path routing (by `Source access`).**

| Source access | Default path | Fallbacks | Barred |
|---|---|---|---|
| open-web | vendor-executed | cowork-mcp, manual | — |
| operator-authenticated | cowork-mcp | manual | vendor-executed |

The credential boundary is hard: a vendor-executed lookup is **open-web only**,
because authenticating a paywall would mean handing the operator's seat
credentials to an execution vendor, which is never done. Whether a given vendor
honors a `Playwright` request, and whether captured binaries return across the
dispatch boundary, is vendor-empirical — the same class as the Self-check
substrate-declaration items (§{section.prism-execution-self-check}, the Execution
Self-check): the Envelope *requests* the tool, the Self-check *confirms* what the
vendor actually has, and the rationale names the fallback. Because the
corpus-access paste is itself a dispatched paste carrying a Dispatch ID and
digest, it is wrapped by the same transport-integrity bracket
(§{section.transport-integrity-bracket}); the executing locus runs Self-check
Step 0 before the lookup.

**Coverage fan.** Fanning a lookup across N vendors looks like equivalence
dispatch, but posture decides routing, not vendor count. In a coverage fan the N
vendors each *retrieve* the same material — different web-search indexes surface
different sources — so for *retrieved* facts multiplicity buys **recall**, not
judgment. Agreement across the fan is a **retrieval-consistency** signal ("this
fact is robustly findable") recorded as a note, never promoted to convergence.
The marker is `Fan: coverage (N)`, structurally distinct from
`Dispatch shape: equivalence`, so Vendor Triangulation cannot fire on a
retrieval-only fan (§{section.vendor-triangulation}, Vendor Triangulation). (A
fan whose loci *infer* over the material is the different case — its
disagreements are triangulation-grade, the `inferred` side of the finding-basis
axis, §{section.prompt-body-convergence-provisions}.) If the engagement then wants multi-vendor *judgment on* the
retrieved material, that is a *separate* `equivalence` dispatch with the retrieved
corpus as its attachment — epistemic posture, routed to Vendor Triangulation
normally.

**Self-containment is bidirectional here**
(§{section.atomic-prompt-self-containment}, atomic-prompt self-containment): the
`Question` goes out self-contained, and the `Return` must come back
caveat-attached — a bare fact stripped of its framing and recency caveat is itself
the silent-omission failure.

**Storage.** A corpus-access return is durable engagement state. Corpus-access
emits the bundle; the persistence axis (§{section.repo-backed-mechanics},
repo-backed mechanics) decides where it lives. Its archive value is fullest under
`repo_backed`, where exhibits survive across sessions and surfaces to reach the
eventual report; under `ephemeral` it degrades to the local or Cowork folder. Not
a hard dependency — a reason to recommend `repo_backed` whenever corpus-access is
in play.

**Lens-anchored auto-trigger.** Phase 1 waits to be told ("look this up in
[source]"); the lens-anchored auto-trigger lets orchestration recognize, on its
own, that a material question warrants a corpus lookup, and *propose* one. The
trigger is anchored to a lens: a lens carrying a `recommended_sources:` entry —
the Lens Library field that binds framework-curated external sources to the lens's
material question (§{section.library-integration}, the Library-integration surface
that bundles the Lens Library) — is, by virtue of that field,
trigger-capable.

*Recognition is the only automatic step.* Orchestration recognizes, on its own,
the conjunction of three conditions: **(i)** the lens is *in play* — it has fired
and its disposition is live; **(ii)** the engagement is actively working that
lens's `material_question:` (a prompt is being shaped against it, or a finding is
being sought for it); and **(iii)** a recommended source's `answers:` binding
matches that question. Nothing beyond this recognition becomes automatic.

*Dispatch stays advisory and operator-ratified.* Recognition produces a
**candidate dispatch, not a dispatch.** Orchestration shapes the
investigation-posture Envelope — every corpus-access field auto-populated from the
matched source record (below) — and surfaces it as a ready-to-ratify proposal,
e.g.: *"The LL-D-008 lens ('Compared to what?', the competitive-substitution lens)
is in play and your substitution question matches its recommended corpus,
ideas.rip. Here is a shaped corpus-access dispatch. Ratify to run, edit, or
skip."* The shaped Envelope is investigation posture, so it routes to a
recall-merge and never the Vendor Triangulation delta
(§{section.vendor-triangulation}, the convergence machinery — a coverage fan
retrieves, it does not triangulate). The operator ratifies, edits, or declines.
**Silence does nothing.**

*Squaring with SP-9.* The autonomy is in the recognition, never the dispatch.
SP-9 (§{principle.SP-9}, the "silence is never consent" Standing Principle)
forbids treating an absent objection as license to act; an auto-*dispatching*
trigger would spend operator resources — vendor calls, time, possibly
authenticated-session access — on inferred consent, violating it directly. An
advisory trigger requires the same explicit ratification SP-9 demands everywhere
else, reusing the framework's existing propose-then-ratify spine: the Layer-3
operator-ratification posture at the P0→P1 boundary
(§{section.three-layer-readiness}, the three-layer-readiness gate, whose Layer 3
parses for an explicit "ratify / approved / go" and treats silence as
non-ratification). No new consent model is introduced. Phase 1 is
operator-initiated ("look this up"); the auto-trigger is
orchestration-initiated-but-operator-ratified ("you'll want to look this up —
shall I?"). It moves the *initiative* to orchestration while leaving *authority*
with the operator.

**Auto-populate — closing the Phase 1 hand-written loop.** When the trigger fires,
the Envelope's corpus-access fields populate from the matched source record rather
than being hand-written each dispatch:

| Source record field | Envelope field | Effect |
|---|---|---|
| `source` | `Source` | identity |
| `kind` | `Corpus kind` | conditions Extract / Return form / Temporal frame |
| `access` | `Source access` | routes the `Driver` via the path-routing table above |
| `framing` | `Source framing` *(mandatory)* | bias caveat travels by default |
| `recency` | `Temporal frame` *(mandatory)* | recency / era posture travels by default |

This closes a loop Phase 1 left open. Phase 1 made `Source framing` and `Temporal
frame` mandatory on the Envelope but hand-written each time; the auto-trigger makes
them populate from recorded metadata, so the caveat is structurally impossible to
silently omit — the operator may still edit, but the default is caveat-attached.
It is the outbound half of the bidirectional self-containment point above
(§{section.atomic-prompt-self-containment}, atomic-prompt self-containment): the
`Question` already goes out self-contained, and now the *outbound caveat* travels
automatically too, so the bare-fact silent-omission failure is prevented at the
source rather than relying on hand-entry. This is also why the source record's
`framing:` and `recency:` are mandatory in the lens schema — a blank there would
become a blank in a *mandatory* Envelope field.

**Where a surfaced candidate lives, and the noise guard.** A surfaced-but-
unratified candidate is *What's next* material (§{section.whats-next}, the
*What's next* artifact — the open-loop surface that lists open options and asks the
operator, on the SP-9 "silence is never consent" lineage), **not** a
Dispatch-register entry (§{section.master-tracking-dispatch-register}, the
Dispatch register, which records actually-dispatched prompts). This keeps the
register clean and reuses the existing open-loop machinery rather than inventing a
parallel log. The candidate surfaces under *What's next*'s advisory, non-blocking
candidates, in this shape:

```
Corpus-access candidate (advisory):
  Lens:              [LL-code + name] — in play
  Material question: [the question being worked]
  Source:            [matched corpus]  (answers: [the matched binding])
  Shaped Envelope:   [investigation-posture Envelope, auto-populated]
  Disposition:       awaiting ratification | declined (turn [n])
```

A material-question-level trigger can fire often, and over-surfacing is its own
failure — the operator tunes out, which is silent omission in reverse. The noise
guard: **surface a candidate once per `{lens, source, material-question}` per
engagement; record a decline; re-surface only on a material change to the
question.** The re-surface predicate reuses the saturation test the framework
already applies to Library coverage at the P0→P1 boundary
(§{section.three-layer-readiness}, the three-layer-readiness gate — its Layer 2
reaches saturation when two consecutive iterations produce no material change to
coverage or strategy): a *material change* here is a shift in the question's
framing, scope, or the finding sought, enough that a prior decline no longer
settles it; a re-worded restatement of the same question does not re-surface. No
new bound is introduced.

**Phase status.** Phase 1 (the v2.6.0 release) made the `manual` and
`vendor-executed` paths operational under manual invocation ("look this up in
[source]" → orchestration shapes a self-contained investigation-posture Envelope →
the operator or an execution vendor runs it → the result returns caveat-attached,
with an Exhibits bundle where capturable). Phase 2 (this release) adds the
lens-anchored auto-trigger above: orchestration recognizes the need itself and
surfaces an operator-ratified candidate, rather than waiting to be told. The
`cowork-mcp` path remains defined-but-reserved (Phase 3, gated on the Cowork
substrate maturing), exactly as the `auto_drive` execution driver is reserved.

**Passive pre-fill of self-report.** When a pass depends on a subject's
*self-report* — a founder questionnaire, a management interview, a data-room
claim set — and especially when it is gated on a person returning, pre-fill
what is externally knowable *before* the self-report arrives. Run passive
external detection (the Chrome-MCP / authenticated-browse surface,
§{section.cowork-surface-capabilities}, plus public records — DNS,
certificate-transparency, IP-WHOIS, app-store listings) and pre-answer the
items observation can reach. This turns gate-blocked waiting into
subject-independent, de-risking progress, and one detection pass feeds many.
It is a **browse/retrieval** job: name the browse capability per the
retrieval-shape step (§{section.vendor-selection-at-dispatch}); do **not**
route it to a synthesis/Deep-Research mode, which silently fails to fetch. Tag
every pre-filled item by provenance — `[OBS]` observed first-hand, `[INF]`
inferred from observed signals, `[ask]` not passively knowable
(§{section.prompt-body-convergence-provisions}, the finding-basis axis). The
self-report is then **triangulated against this independent baseline** when it
arrives (the external check pre-positioned over the claim — §{principle.SP-21};
the detection is investigation-posture single-source, §{principle.SP-15}, never
a triangulation seat). **Passive-only by default** on a trust-relationship
subject: honor the questionnaire's own promise — no scanning, no
ID/parameter manipulation (IDOR), no auth-bypass / rate-limit / upload /
state-changing actions; read key *names*, never token *values*. Active tests
require explicit operator authorization and are marked `[not tested — out of
passive scope → ask or authorized test]`. The paste-ready detection template
and per-vendor browse recipes are in §{appendix.vendor-parsing-observations}
(vendor parsing observations).
