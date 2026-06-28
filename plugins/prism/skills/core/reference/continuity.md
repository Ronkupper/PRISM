<!-- PRISM v2.20.0 Skill bundle (on-demand reference). Continuity reference (sections 5.4-5.6 + 14) — migration handoff format, failsafe-recovery mechanics, defensive migration at natural seams, and cold-open missing-handoff recovery. Fetch at a resume / context-seam, or when M5 reads 🟠/🔴.
     Generated from the assembled PRISM.md — edit PRISM.md, not this. -->

### 5.4 Migration handoff `[structural | stable]`
<a id="section-migration-handoff"></a>

Defined handoff artifact. Produced by orchestration at 🔴 (mandatory) and
offered at 🟠 (operator-elective).

**Handoff format.**

```
━━━ PRISM SESSION HANDOFF ━━━
Project:                [name]
Master version:         [filename of attached Master]
Lens Library version:   [v0.16 | filename pinned]
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

Operator state:         [optional operator note —
                         "I'm at lunch; resume with P2.5 tomorrow"]

Next session opens with:
  Attach: Master, Lens Library, this handoff.
  Read: this handoff first, then proceed per "What's next."
━━━ END SESSION HANDOFF ━━━
```

**Production discipline.**

- Produced at 🔴 automatically as the closing act of the orchestration
  session.
- Offered at 🟠 in *What's next* as a candidate next action: "Migrate now
  to fresh session — produce handoff?"
- Available at 🟢 / 🟡 on operator request.
- The handoff *plus* the current Master *plus* the Lens Library are the
  three artifacts the new session opens with attached. Together: complete
  context restoration.

**Handoff vs. Master.** The Master is canonical project state; the handoff
is migration context. The handoff is short (≤ 1 page) and points into the
Master for detail. New session reads the handoff first to orient, then
works with the Master as canonical reference.

### 5.5 Failsafe recovery — continuous-state mechanics `[structural | stable]`
<a id="section-failsafe-recovery-continuous-state-mechanics"></a>

"Always written" defined mechanically: Master and *What's next* are written
at every orchestration turn-close, regardless of band state, regardless of
whether the operator asks for them. Misreads of context band cost
essentially nothing because state is always recoverable.

**Mechanics.**

- **Master update at every orchestration turn-close.**
  - Always emitted at turn-close, regardless of whether material state
    changed. Continuous-state safety property (operator never picks the
    wrong Master because the latest is always the most recent emission)
    is preserved.
  - **No-state-change marker (v2.0.1).** When no material Master state
    changed during the turn (no Dispatch register change, no findings
    ingestion, no probe disposition change, no monitor state change, no
    strategy change, no new Changelog entry), the emitted filename
    carries the `_no_change` suffix immediately before the extension —
    e.g., `acme_audit_prism2.0_master_p2.3_no_change.md`. The operator
    can defer cloud-save and attachment-swap on these emissions; the
    prior Master remains current. This addresses mobile churn cost
    without giving up the always-emit safety property.
  - Append-mostly when content does change: Changelog gains a line;
    relevant register sections gain entries; Dispatch register status
    updates per §{section.master-tracking-dispatch-register}; findings sections absorb any newly-converged
    Layer-1 outputs.
  - Filename version bump only at phase boundaries or convergence-round
    increments (per §{section.filename-conventions-and-bump-atomicity} bump atomicity). The `_no_change` suffix is
    orthogonal to the version field — a no-change emission keeps the
    same version number as the prior content-bearing emission.
  - Operator must *download* the updated Master at session close when
    the emission is content-bearing (no `_no_change` suffix) to make it
    the authoritative canonical copy. (Manual step under v2.0.1
    plain-chat substrate.)
  - Cloud-drive save is the Operator hint emitted at every
    content-bearing turn-close: `Save Master to cloud drive (§{section.mobile-operator-survival-guide} MO-5).`

- ***What's next* rewrite at every orchestration turn-close.**
  - Replaces in place; no history kept (Changelog carries the historical
    pointer).
  - Always reflects the current state, not a future or planned state.
  - Operator reads *What's next* as the sole source of "what to do next" —
    not by scrolling chat, not by reading the Master in detail.

- **Inbox drain at every orchestration turn-close (repo_backed lanes).**
  The lane owner reads its `OPEN_ITEMS` inbox alongside *What's next*, folds
  each non-terminal item into the Strategy / next-action / register, and
  appends a `drained` disposition line (§{section.cross-lane-inbox}). The drain
  is a turn-close peer of the Master and *What's next* writes, and part of
  resume. An un-drained inbox at turn-close is a turn-close self-check surfaced
  on the resume line and via SP-4 emission — not a separate Monitor (it does
  not warrant a numbered slot).

**Consequence — asymmetric bet.**

- If the framework misreads band: operator migrates → fresh session
  attaches Master + handoff + Lens Library → work continues, no loss.
- If the framework reads correctly: the recovery infrastructure wasn't
  needed but wasn't costly either (writing the Master + *What's next* is
  part of the orchestration turn anyway).
- If the operator declines to migrate at 🔴: operator-discretion override
  (the framework cannot force migration); the framework continues but
  flags continuing-at-🔴 in *What's next* and increments a turn-counter
  that escalates the migration recommendation.

### 5.6 Defensive migration at natural seams `[structural | stable]`
<a id="section-defensive-migration-at-natural-seams"></a>

Migration posture keyed to band × seam.

| Band | Migration posture | Seam discipline |
|---|---|---|
| 🟢 | Available | At any natural seam; no urgency. Operator-elective. |
| 🟡 | Recommended | At the next natural seam; if no seam approaching, finish current sub-task to create one. |
| 🟠 | Strongly recommended | At the immediate next opportunity; framework actively closes current curation to reach a seam. |
| 🔴 | Correct action now | Framework produces handoff (§{section.migration-handoff}); operator opens fresh session and attaches handoff + Master + Lens Library. |

**Operator override.** Operator can decline migration at any band.
Framework respects but flags continuing-at-band in *What's next*. At 🔴,
the per-turn flag escalates to a migration-overdue counter.

---

## 14. Missing-handoff recovery
<a id="section-missing-handoff-recovery"></a>

What happens when the operator opens a fresh orchestration session
without a handoff (operator skipped the migration step at 🔴; handoff
was lost; mid-project session was opened cold)?

### 14.1 Recovery flow `[methodological | stable]`
<a id="section-recovery-flow"></a>

1. **Session-open verification fires.** SP-13 substrate check passes;
   M1 detects no handoff attached.
2. **Orchestration searches for the canonical Master.** Per §{principle.SP-1}
   protocol:
   - Past-conversation search for the project name and likely Master
     filenames (`conversation_search`, bounded by current Project per
     §{section.claude-project-as-setup-recommendation}; SP-12 disclosure on bound).
   - If a past session is identified that produced a Master version,
     surface the session URL and the Master filename to operator.
3. **Operator attaches the located Master.** Orchestration runs M2
   (Version Drift) verification against operator's expected version
   (operator-declared on resume).
4. **Orchestration reconstructs `What's next` from the Master.** The
   Master's Open dispatches list, Active probes list, Open monitors list,
   and Rerun Register together carry sufficient state to reproduce a
   *What's next*. Decision brief / Stakeholder register / Claim inventory
   / Jurisdiction map carry the Setup artifacts.
5. **No silent regeneration.** Per §{principle.SP-1}: orchestration does not
   reconstruct what's missing from memory. Surface what was located,
   surface what couldn't be located, ask operator how to proceed.
6. **If Master itself cannot be located.** Escalate per §{principle.SP-1}: name the
   consequences of regenerating from memory (authenticity loss, schema
   drift, silent contamination); ask operator whether to proceed with
   reconstruction (and document the reconstruction explicitly in the
   Master's Changelog), or whether to re-Setup.

### 14.2 Why this matters
<a id="section-why-this-matters"></a>

The continuous-state mechanic (§{section.failsafe-recovery-continuous-state-mechanics}) is the front-line defense — every
turn-close writes the Master and *What's next*. The recovery flow is the
backstop when the front-line defense is bypassed (handoff lost, session
opened from outside the Project, cross-device churn). SP-1's discipline
makes the recovery flow safe rather than seductive: it's harder than
recreating from memory, and it should be — recreation is the failure
mode the discipline exists to prevent.

---
