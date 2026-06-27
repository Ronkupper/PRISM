<!-- PRISM v2.15.0 Skill bundle (on-demand reference). Mobile operator survival guide (section 17). Operator-facing reference.
     Generated from the assembled PRISM.md — edit PRISM.md, not this. -->

## 17. Mobile operator survival guide
<a id="section-mobile-operator-survival-guide"></a>

v2.0 is mobile-first. Mobile operators routinely encounter patterns —
both frictions and effective interaction moves — that desktop operators
either don't hit or don't need. This section catalogues two classes:
**vendor-client workarounds** (concrete responses to LLM-vendor
mobile-client limitations) and **operator interaction patterns** (ways
of asking and navigating that are more valuable on mobile than on
desktop). Living document: entries accumulate as patterns surface.

Entries here may be surfaced inline as **in-context operator hints** at
specific orchestration touchpoints — the Execution Envelope's
`Operator hints` field (§{section.operator-hints-emission-discipline}) and the *What's next* artifact (§{section.whats-next}) —
so an operator sees the relevant cue at the moment of acting rather
than from memory.

Each entry names the **Problem** or **Situation**, the **Workaround** or
**Pattern**, and **Why it works** (so an operator can extrapolate when
the exact case doesn't match).

### Vendor-client workarounds

#### MO-1 — Samsung file explorer: LLM-downloaded files invisible until indexing catches up

**Platform:** Android, Samsung devices (tested: Galaxy S25+).

**Problem.** Files downloaded from LLM mobile apps land in the Downloads
folder but do not appear in Samsung's built-in file manager immediately.
The system's indexing is delayed; a file you just downloaded may not be
visible to attach workflows for seconds to minutes. On the mobile-first
workflow (download output from one LLM, attach to orchestration
session), this stalls the loop.

**Workaround.** Install **MiX** (third-party Android file manager).
MiX sees new files immediately, independent of Samsung's indexing. It
also includes an HTML/Markdown reader ("HTML View") that renders `.md`
artifacts in place — useful for a quick sanity-check on an execution
output before attaching it to orchestration.

**Why it works.** MiX does its own directory scanning rather than
relying on the system indexing service. Same filesystem, different
reader; the file exists the moment the LLM app finishes writing it,
and MiX respects that.

#### MO-2 — Broken file/clipboard operations in LLM mobile apps

**Platform:** Android, varies by LLM vendor mobile app.

**Problem.** Some LLM mobile apps have incomplete implementations of
basic operations: copy-to-clipboard from rendered outputs, file
download of generated artifacts, attachment of certain file types. The
exact failures vary by vendor and change with app updates, but the
class of failure is consistent enough to plan around.

**Workaround.** Open the same vendor in **Firefox with Desktop Mode
enabled** on the mobile device. Desktop web rendering of the vendor's
site is typically more complete than the native mobile app for these
operations, and the actions that fail in-app usually succeed in the
desktop-rendered web version.

**Why it works.** Vendors' desktop web clients are generally more
mature and more uniformly implemented than their mobile apps; browser
rendering exposes the full web client regardless of the device's form
factor. Desktop Mode in Firefox spoofs the user-agent and viewport,
convincing the vendor's site to serve the full-featured client.

### Operator interaction patterns

#### MO-3 — Artifact + handoff together: "present document with instructions"

**Situation.** A session produces a deliverable that will feed into
another session's work (e.g., a walkthrough document that a fresh
session will react to; a setup strategy that a fresh session will
execute against). Requesting only the artifact leaves the operator to
reconstruct the handoff from memory later, which introduces drift and
loses precision about target model, session hygiene, attachment order,
scope boundaries, and so on.

**Pattern.** Ask for the artifact **and** the accompanying handoff
prompt in the same request. Example phrasing: *"Produce the walkthrough
document and an accompanying handoff prompt I can paste into a fresh
session."* Claude delivers both together; the handoff carries all the
context the next-session operator needs (which model, which mode, which
files to attach, what's in/out of scope), so there is no reconstruction
step later.

**Why it works.** Paired delivery creates self-contained packages that
travel together. The artifact is the deliverable; the handoff is the
operating context. Separating them is a mild form of session-forgetting
(the context is in the producing session's head; it has to be
reconstructed when the consumer session opens). Asking for both in one
shot eliminates the reconstruction step and leverages the producing
session's still-fresh context. This pattern pairs naturally with the
Execution Envelope discipline (§{section.prism-execution-envelope}) — same instinct, different
altitude: bake operating context into the artifact.

#### MO-4 — Session retrieval: "point me to the relevant session"

**Situation.** PRISM work routinely crosses sessions (artifact produced
in session A, used in session B). When an operator is in the wrong
session, or can't remember which session holds which artifact, mobile
manual navigation of the Claude chat list is slow — previews are
short, built-in search is limited, scrolling is tedious on a phone.

**Pattern.** Ask Claude directly: *"point me to the session where
[topic] happened"* or *"give me a clickable link to the [topic]
session."* Claude runs `conversation_search` on the topic, identifies
the referenced session, and returns a `https://claude.ai/chat/{uuid}`
URL. One tap to navigate.

**Why it works.** Claude has past-conversations search as a built-in
tool and can construct canonical session URLs from the UUIDs it
returns. Faster and more precise than mobile manual navigation. The
pattern also works as a disambiguation aid — if multiple sessions match
the topic, Claude can enumerate them with brief summaries before
committing to a link.

**Caveat — bounded-search disclosure (§{principle.SP-12}).** Past-conversations
search is scoped: if the operator is in a project, search is confined
to that project's chats; otherwise it covers non-project chats. If the
target session lives in a different scope, the search returns null.
Claude surfaces this bound rather than asserting a global null —
*"I didn't find it within this project's conversation scope; the
session may live in a different project or outside projects; confirm
before I conclude it doesn't exist."*

#### MO-5 — Persisting artifacts across device/session loss

*(v2.0.1: renamed from `E.5` to `MO-5` to disambiguate from Appendix E.5 — *What's next* template. v2.9.1 completed the rename: `E.1`–`E.4` → `MO-1`–`MO-4`. Mobile-guide subsections are now MO-1 through MO-5; Appendix E template subsections remain E.1 through E.5.)*

**Situation.** Mobile operators work primarily through vendor apps.
Execution outputs downloaded to the device live in local storage,
which is subject to events desktop operators rarely hit: device reset,
app storage clear, accidental delete, storage-quota cleanup, OS update
churn. Even absent those events, the mobile Downloads folder
accumulates cruft — overlapping versions, vendor-default filename
collisions, stale artifacts from prior sessions — that makes finding
the right file its own failure mode. An artifact that survives the
dispatch session can be gone, or effectively lost in the pile, by the
next orchestration turn if nothing external to the device holds a
structured copy. On a multi-session project, losing one converged
output is expensive; losing the Master is a project-reset event.

**Pattern.** Save execution outputs to a cloud drive (Google Drive,
Dropbox, OneDrive, or equivalent) immediately after download, before
switching to the next vendor or ending the session. Same move for the
Master at session close: cloud-save before dismissing the orchestration
session. Project-scoped folders on the cloud drive keep versions
separated and retrievable by name; superseded artifacts are archived
rather than deleted so the audit trail stays intact across the
project's lifetime. The local copy stays available for the immediate
next attach step; the cloud copy is the durable record.

**Why it works.** Cloud drives survive the device events local mobile
storage does not, and structured project folders give the operator a
navigable home rather than the flat Downloads-folder pile. On desktop
substrates this pattern is often redundant; on mobile it is
load-bearing, and the cost of the extra tap is negligible.

---
