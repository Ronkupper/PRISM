<!-- PRISM v2.20.0 Skill bundle (on-demand reference). Parked v2 design ideas (section 8). Reference.
     Generated from the assembled PRISM.md — edit PRISM.md, not this. -->

## 8. Parked v2 design ideas
<a id="section-parked-v2-design-ideas"></a>

These two ideas were parked for v2 from the design-doc-level discussion
(DD.§13.3): they earn their place but the framework treats them as
recommendations and graceful-degradation paths rather than hard machinery.

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
