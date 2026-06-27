<!-- PRISM v2.15.0 Skill bundle (on-demand reference). Templates compendium — paste-ready blocks (Appendix E). Fetch when producing a Setup/dispatch artifact.
     Generated from the assembled PRISM.md — edit PRISM.md, not this. -->

## Appendix E — Templates compendium
<a id="appendix-templates-compendium"></a>

All paste-ready blocks in one place.

### E.1 PRISM Execution Envelope
<a id="appendix-prism-execution-envelope"></a>

```
━━━ PRISM EXECUTION ENVELOPE ━━━
Prompt ID:          [identifier — purpose/title]
Project:            [project name]
Master version:     [filename of Master at dispatch time]
Prompt digest:      [orchestration-generated at dispatch; copy verbatim; never recomputed]
Posture:            epistemic | investigation
Vendor:             [vendor] | multi-vendor          ← epistemic posture
Dispatch shape:     equivalence | split | limitation-named   ← epistemic posture
Dispatch rationale: [one positive-framing line per variant]   ← epistemic posture
Vendor config:      [vendor-specific config flags]
Session hygiene:    [fresh session, project attachment posture, web search on/off]
Tools:              [vendor tools requested; reserved slot for plugins/skills]
Attachments:        [filename, filename, ...]
Expected output:    [filename to download as]
Operator hints:     [zero or more one-line cues]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### E.2 PRISM Execution Self-check
<a id="appendix-prism-execution-self-check"></a>

```
━━━ PRISM EXECUTION SELF-CHECK ━━━
Before doing the task:

1. State what model/vendor you are and what session
   state you can introspect (mode, thinking setting,
   tools enabled).
2. Compare to the Envelope's Vendor and Vendor config
   fields above.
3. If anything does not match, or if self-identification
   is incomplete, STOP. Report what you found and ask
   the operator whether to proceed, switch sessions,
   or abort. Do not proceed to the task silently.
4. Proceed only if (a) the substrate matches, or
   (b) the operator has explicitly confirmed to proceed
   despite mismatch.
5. Before emitting the Output: enumerate every
   negation ("not Y", "X, not Y", "rather than
   Y", "no Y"), defensive intensifier ("real",
   "actual", "truly"), and temporal hedge ("for
   now", "currently") in the findings content;
   tag each called-for (naming the live
   alternative it answers) or uncalled-for
   (rewrite positively before release). A
   self-bounding verb ("shrink", "slow",
   "narrow") makes a trailing denial of the
   unbounded case uncalled-for by default; a
   worst-case section makes the extreme a
   called question. Headings and opening
   sentences first (SP-16, the Elephant Rule).
6. Before emitting the Output: recompute every
   stated quantitative relationship from the
   document's own numbers; re-count every
   enumeration intro against its list; verify
   repeated structures as a set; re-read every
   sourced claim against its source — same
   noun, same metric. Exact match or rewrite;
   never round silently (SP-18, It must
   recompute).
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### E.3 PRISM Execution Output
<a id="appendix-prism-execution-output"></a>

```
━━━ PRISM EXECUTION OUTPUT ━━━
Prompt ID:        [identifier — purpose/title]
Project:          [project name]
Master version:   [from Envelope]
Vendor:           [vendor that actually executed]
Vendor config:    [config actually applied at execution]
Schema version:   output-v1
Date:             [YYYY-MM-DD]
Prompt digest:    [copied verbatim from Envelope]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[findings content]

━━━ END PRISM EXECUTION OUTPUT ━━━
Operator next:        [download instruction; attach instruction]
Attachment warnings:  [optional; one line per warning]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Exhibits manifest** — appended inside the findings content on a corpus-access
bundle return when `Archive: requested` (§{section.prism-execution-output}, the
Execution Output):

```
━━━ EXHIBITS ━━━
[filename] · [source] · [capture date]
   query answered: [the scoped question this artifact substantiates]
   caveat:         [the applicable framing + temporal caveat]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### E.4 Vendor Selection block
<a id="appendix-vendor-selection-block"></a>

```
━━━ VENDOR SELECTION ━━━
Prompt ID:           [...]
Refresh check:       [2-4 lines, what was checked, what was found]
Recommended:         [Vendor / Vendor config / Tools]
Rationale:           [1-2 lines, positive framing]
Soft notes:          [optional; concerns or alternatives the operator should know]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### E.5 *What's next*
<a id="appendix-whats-next"></a>

```
━━━ WHAT'S NEXT ━━━
Master version:        [current Master filename]
Context band:          🟢 | 🟡 | 🟠 | 🔴

Current state summary:
  Active prompt(s):    [prompt IDs in flight]
  Open dispatches:     [prompts in dispatch register, status != closed]
  Pending Adaptations: [list]
  Recent Monitor fires: [last 3 turn-closes' Monitor fires]
  Active probes:       [Setup probes still iterating, if in P0]

Candidate next actions (priority-ranked):
  1. [candidate] — [rationale, 1 line]
  2. [candidate] — [rationale]
  ...

Recommended next action:
  [pick from candidates] — [why]

Operator hints:        [zero or more]

Dispatch-ready payload (if applicable):
  [full Envelope + Self-check + prompt body, ready to paste]
━━━ END WHAT'S NEXT ━━━
```

### E.6 Vendor Triangulation delta
<a id="appendix-vendor-triangulation-delta"></a>

```
━━━ VENDOR TRIANGULATION DELTA ━━━
Prompt ID:           [identifier]
Returns received:    N/expected_N
Vendors converged:   [list]

Agreement claims:    [findings agreed across all vendors]
Divergent claims:    [findings where vendors disagree; per-vendor citation]
Vendor-unique:       [findings only one vendor surfaced; per-vendor citation]
Method-significant:  [where divergence reflects vendor methodology, not subject content]

Operator action:     [recommended next step — accept, dig, or escalate]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### E.7 Migration handoff
<a id="appendix-migration-handoff"></a>

```
━━━ PRISM SESSION HANDOFF ━━━
Project:                [name]
Master version:         [filename of attached Master]
Lens Library version:   [v0.15 | filename pinned]
Producing session:      [orchestration session URL or descriptor, if known]
Reason for migration:   [band-state, named driver(s)]
Migration timestamp:    [YYYY-MM-DD]

Current state summary:
  Active prompt(s):     [...]
  Open dispatches:      [from Dispatch register]
  Pending Adaptations:  [...]
  Active probes:        [Setup probes still iterating]

Open monitors:          [unresolved fires by Monitor ID]

What's next (current):
  [the current What's next artifact, pasted in full]

Operator state:         [optional operator note]

Next session opens with:
  Attach: Master, Lens Library, this handoff.
  Read: this handoff first, then proceed per "What's next."
━━━ END SESSION HANDOFF ━━━
```

### E.8 Probe 1 Coverage grading output
<a id="appendix-probe-1-coverage-grading-output"></a>

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

### E.9 Setup artifacts (Master sections)
<a id="appendix-setup-artifacts-master-sections"></a>

#### Decision brief

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

#### Stakeholder register

```
## Stakeholder register

| Role | Stake | Motivation | Positioning/angle | Decision power | Communication channel |
|---|---|---|---|---|---|
| [operator/commissioner] | [decision/outcome stake] | [why they want this engagement / this outcome] | [advisor / investor / competitor / partner / regulator / arms-length / advocacy; + any conflict] | [yes/advisory/none] | [channel] |
| [name] | [decision/outcome stake] | [motivation] | [positioning/angle; + any conflict] | [yes/advisory/none] | [channel] |
| ... | ... | ... | ... | ... | ... |
```

#### Claim inventory

```
## Claim inventory

| Claim type | Specific claim | Source | Audit pass(es) |
|---|---|---|---|
| Efficacy | [...] | [where claim is made] | P2.x |
| Compliance | [...] | [...] | P3.x |
| Positioning | [...] | [...] | P4.x |
```

#### Jurisdiction map

```
## Jurisdiction map

| Jurisdiction | Triggered regimes | Material to scope? | Pass(es) |
|---|---|---|---|
| US (federal) | FTC, ADA | yes | P3.1 |
| EU | GDPR, EU AI Act | yes | P3.2 |
| US-CA | CCPA/CPRA | yes | P3.1 |
```

### E.10 Dispatch register
<a id="appendix-dispatch-register"></a>

```
## Dispatch register

| Prompt ID | Recommended (Vendor / config) | Executed (Vendor / config) | Status | Convergence ref |
|---|---|---|---|---|
| P2.3 | Gemini Pro DR / DR ON | Claude Opus 4.7 / standard | substituted | layer1-p2.3 |
| P2.4 | Claude Opus 4.7 / standard | — | dispatched | — |
| P2.5 | multi-vendor / equivalence | partial (2 of 3) | partial | layer1-p2.5 |
```

### E.11 Rerun Register
<a id="appendix-rerun-register"></a>

```
## Rerun Register

| Prompt ID | Reason | Source Monitor | Status |
|---|---|---|---|
| P2.1 | M6 — premise shifted | M6 HIGH P2.4 ingestion | overdue |
```

### E.12 Corpus-access Envelope
<a id="appendix-corpus-access-envelope"></a>

```
━━━ PRISM CORPUS-ACCESS ENVELOPE ━━━
Prompt ID:        [identifier — purpose/title]
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

### E.13 Validation Dispatch Envelope
<a id="appendix-validation-dispatch-envelope"></a>

```
━━━ PRISM VALIDATION DISPATCH ENVELOPE ━━━
Prompt ID:        [identifier — purpose/title]
Project:          [project name]
Master version:   [filename at dispatch]
Prompt digest:    [orchestration-generated; copy verbatim]
Posture:          epistemic
Dispatch shape:   limitation-named     ← never a triangulation seat
Not chosen:       [producing vendor/session] — the producing thread
                  cannot validate its own framing
Vendor:           [single vendor; fresh session mandatory]
Vendor config:    [vendor-specific flags; web search OFF unless
                  validation scope includes source-checking]
Tools:            [minimal — only what validation requires]
Attachments:      [deliverable(s); cross-consistency materials when
                  in scope]
Excluded context: author rationale, structure notes, known-weak-spots
                  list (the independence rule)
Validation axes:  logic | defensibility | internal consistency |
                  consistency against attached materials |
                  readability | quality
Lens kit:         LL-D-019, LL-D-020, LL-D-021 + SP-18-style
                  recompute sweep
Return form:      severity-tagged findings list, routed to the
                  producing thread
Expected output:  [filename to download as]
Operator hints:   [zero or more one-line cues]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---
