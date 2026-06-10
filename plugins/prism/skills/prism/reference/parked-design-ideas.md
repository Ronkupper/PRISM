<!-- PRISM v2.14.0 Skill bundle (on-demand reference). Parked v2 design ideas (section 8). Reference.
     Generated from the assembled PRISM.md — edit PRISM.md, not this. -->

## 8. Parked v2 design ideas
<a id="section-parked-v2-design-ideas"></a>

These two ideas were parked for v2 from the design-doc-level discussion
(DD.§13.3): they earn their place but the framework treats them as
recommendations and graceful-degradation paths rather than hard machinery.

### 8.1 Claude Project as Setup recommendation `[vendor-dependent | review-if: orchestration vendor changes]`
<a id="section-claude-project-as-setup-recommendation"></a>

Setup at P0.1 includes a recommendation to create a Claude Project as the
home for project state.

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
- `PRISM_lens_library.md` (v0.15 or pinned tag)
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

### 8.2 Session history as validation/recovery `[vendor-dependent | review-if: orchestration vendor changes]`
<a id="section-session-history-as-validation-recovery"></a>

Session history (Claude's `conversation_search`) is consulted when state is
unexpected, ambiguous, or out-of-order. Results are advisory; SP-1 governs
canonicity.

**Triggers** (Monitors that consult session history):

- **M2 fires** (Version Drift) — Master version doesn't match expected.
  Consult session history for the last session that saved the expected
  version.
- **M3 fires** (Sequence Violation) — operator declared a step out of
  order. Consult session history for the canonical sequence in this
  project.
- **Master / *What's next* mismatch** — attached Master's version differs
  from what *What's next* predicted at last close. Consult session history
  for the closing turn that produced the mismatch.
- **Strategy-finding mismatch** — a finding references a prompt not in the
  Prompt Strategy. Consult session history for when the prompt was added
  or removed.
- **Attach-conversation disagreement** — attach map and conversation
  disagree about which file is canonical. Consult session history for the
  last canonical statement.

**Query construction.** Orchestration's `conversation_search` query is
derived from the ambiguity. Examples:

- M2: `"[Master version expected]" "[project name]"`
- M3: `"[prompt ID]" "[project name]"`
- Strategy-finding mismatch: `"[finding text]" "[project name]"`

Query length: 3–6 words distinctive content. No long passages.

**Results handling — advisory not authoritative.**

1. Orchestration reports what session history found:
   ```
   Session history check (per [Monitor or trigger]):
   Searched: "[query]"
   Scope: within [Project name | non-project conversations]
   Found: [N matches]
     - [session URL or descriptor] — [snippet]
     - ...
   ```
2. Orchestration does *not* silently update Master from session-history
   evidence. Per §{principle.SP-1}: canonical artifacts are not regenerated without
   operator confirmation.
3. Orchestration surfaces a recommendation: "Session history suggests
   [interpretation]. Update Master to reflect? [yes/no/clarify]"
4. Operator confirms; orchestration updates Master.

**Reconciliation when session history disagrees with attached Master.**
Both surfaced; named as discrepancy; escalated to operator.

- *Default posture*: attached Master is authoritative; session history is
  corroborating evidence.
- *Operator decides*: whether to update Master per session history, keep
  Master as-is, or open the older session and reconstruct.
- *SP-1 governance*: never silently regenerate canonical state from session
  history.

**SP-12 disclosure on every consult.**

```
Session history search note (SP-12):
Searched within [scope]. [N found / null]. The session may live in a
different scope I cannot see from here; confirm before concluding.
```

---
