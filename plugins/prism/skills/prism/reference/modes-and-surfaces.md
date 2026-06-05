<!-- PRISM v2.9.1 Skill bundle (on-demand reference). Cowork capability surface + repo_backed mechanics (sections 3.5.2-3.5.3). Fetch when a non-default orchestration surface or persistence value is in play.
     Generated from the assembled PRISM.md — edit PRISM.md, not this. -->

#### 3.5.2 Cowork surface capabilities
<a id="section-cowork-surface-capabilities"></a>

Under `orchestration_surface: cowork`, Computer Use and the Chrome MCP (the
Claude Chrome Extension) are exposed as a substrate. Its uses are
deliberately an **open set** — documented as a capability surface rather
than a fixed enum, so a new use does not force a schema change. The
closed-enum discipline governs axis *values*; this capability surface is
intentionally open. Known uses today:

- **Auto-drive execution** — drive other vendors' execution apps (the
  Axis-2 `auto_drive` value).
- **App-under-test** — when the work's scope includes auditing a web (or
  other) application, Computer Use / Chrome MCP operate the target itself.
  This is the audit *subject*, distinct from driving execution.
- **Isolated-context execution of the Claude seat** — in a cross-vendor
  equivalence run, the Claude seat can execute in a Cowork sub-agent with
  its own context window rather than inline. This shifts only the
  context-isolation axis, not epistemic posture — triangulation asymmetry
  stays carried by the vendor set — so it is SP-15-clean
  (§{section.sp-15-triangulation-integrity}). It depends on atomic-prompt
  self-containment (§{section.atomic-prompt-self-containment}): a
  fresh-context sub-agent carries none of the orchestrator's assumptions,
  so bare shorthand misreads exactly as it would across vendors.
- **Subagent investigation** — bounded investigation work
  (candidate-credibility checks, single-source extraction, methodology
  lookups, pre-dispatch scoping). Investigation posture only, never a
  triangulation substitute.
- **Future uses** — any later capability that benefits from or depends on
  these primitives lands here without a schema change.

Every sub-agent use lands on the context-isolation axis, never the
epistemic-posture axis — consistent with SP-15
(§{section.sp-15-triangulation-integrity}).

**Posture, now a first-class Envelope field.** The investigation-vs-epistemic
distinction described in this surface as prose is, as of the corpus-access
capability, carried structurally as the Envelope's `Posture:` field
(§{section.prism-execution-envelope}, the Execution Envelope). Corpus-access
(§{section.corpus-access-dispatch}, the external-reference-corpus lookup) is the
first investigation use to earn its own first-class Envelope, which is what forced
the distinction up from prose into the schema. Its `cowork-mcp` lookup path —
PRISM driving the Chrome MCP to operate a source directly, including the
operator's authenticated session — lands in this open capability set (Phase 3,
reserved) and is App-under-test-shaped, not the `auto_drive` per-vendor
machinery.

#### 3.5.3 `repo_backed` mechanics
<a id="section-repo-backed-mechanics"></a>

`persistence: repo_backed` makes a GitHub repo the durable home for an
engagement's state. It earns its place even on a single surface: in a plain
`single_chat` or `projects` session, the repo is where the Master
(§{section.the-master}) and *What's next* (§{section.whats-next}) survive
across chats that would otherwise lose them to scrollback. The cross-surface
payoff — switching between, say, a Cowork session and a mobile Project and
having each pick up exactly where the last left off — is an *additional*
benefit repo-residence unlocks, not the baseline justification. The axis is
orthogonal to the orchestration surface by construction
(§{section.orchestration-driver-and-persistence-axes}).

**Setup flow.** When `repo_backed` is selected at Setup, orchestration:

1. **Asks the operator for a repo and a scoped PAT.** A GitHub repository (new
   or existing) to hold the engagement, and a Personal Access Token the
   orchestration session uses to read and write it. PAT hygiene is
   operator-side and is spelled out below — this is the operator's own
   credential for their own repo, distinct from any maintainer credential.
2. **Creates a work folder** for this engagement in the repo (e.g.
   `prism/<engagement-slug>/`) — the canonical home for every artifact the
   engagement produces.
3. **Writes an engagement SI file** into that folder codifying the repo
   workflow (skeleton below), so any session that loads it operates the
   engagement identically regardless of surface.
4. **Asks the operator to configure that SI in a Project** — one per surface
   the operator intends to use (e.g. a desktop Cowork Project and a mobile
   Project both pointing at the same repo).
5. **Saves the engagement's whole state to the repo** — everything the work
   touches, inputs in and outputs out. The set is illustrative, not closed:
   operator-supplied **Inputs** (the subject brief and any reference material),
   the Master, Envelopes, handoffs, execution Outputs, and the *What's next*
   artifact, which becomes **repo-resident** (§{section.whats-next}): same
   artifact, same per-turn-close lifecycle, written to a fixed path in the work
   folder rather than living only in chat.
6. **Lets the operator switch surfaces freely.** Each surface reads the
   repo-resident *What's next* on resume and continues from it. The repo is
   the shared state; the surface is interchangeable.

**Committer model.** The orchestration session commits artifacts directly
using the operator-supplied PAT — the operator delegates the GitHub mechanics
the same way *What's next* spares them from scrolling chat. An operator who
prefers not to place a PAT in a Project can instead run
**operator-as-committer**: orchestration produces each artifact as a file and
the operator commits it by hand. This is the conservative fallback; it
reintroduces the manual round-trip `repo_backed` exists to remove, so it is
not the default.

**Operator inputs.** Anything the operator supplies to the engagement — the
subject brief, reference documents, spreadsheets, decks, and information given
in a chat prompt — is captured to the work folder, at Setup or any time after.
Information pasted into chat is written to a file rather than left in
scrollback; otherwise it is exactly the cross-surface state a different surface
could not pick up, which is the loss `repo_backed` exists to prevent.

**Execution returns.** Execution Outputs — the reports a vendor produces from a
dispatched Envelope, in whatever form they come back (Markdown, a Word or PDF
document, pasted text) — persist the same way as every other artifact. Under
the manual execution driver (§{section.orchestration-driver-and-persistence-axes},
the only built driver), the operator attaches the returned Output to the
orchestration session as it already does in the normal lifecycle, and
orchestration commits it to the work folder; this works today under the
Claude-as-committer model with no extra machinery. A future git-enabled
execution session that commits its own returns directly is a possible later
direction — lower priority, not built — the persistence-side parallel to the
reserved `auto_drive` execution driver. Either way the returns land in the same
work folder as the operator's Inputs, the Master, Envelopes, handoffs, and
*What's next*.

**Operator PAT hygiene.** The PAT is the operator's credential for the
operator's repo. The discipline below mirrors token handling PRISM's own
maintenance has used reliably; it is guidance for the operator's setup, not a
prescription of any particular maintainer flow:

- **Minimum scope.** A fine-grained PAT scoped to the single engagement repo
  only (never account-wide), granting Contents read/write and Metadata read —
  nothing further unless the engagement specifically needs it.
- **Storage.** Held in the Project's credential surface (its files), never
  pasted into chat, never committed to the repo, never echoed into an
  artifact. Treat it as a password.
- **Injection and strip.** When the session pushes, the PAT is embedded in the
  remote URL for the push only and stripped from the remote immediately after.
  It is never written to a tracked file.
- **Rotation.** Give the token an expiry (90 days is a reasonable default),
  track that date, and regenerate before it lapses. Avoid no-expiry tokens.

**Engagement SI skeleton.** The file written in step 3 is the per-engagement
operating document. Its sections:

1. **Purpose & repo model** — what this engagement is; the repo; the
   work-folder path.
2. **Source of truth** — the repo is canonical; the repo-resident *What's
   next* is the single state pointer.
3. **Surface registry** — which surfaces are configured and any per-surface
   setup notes. A single entry in the baseline single-surface case; one row
   per surface when the operator runs more than one.
4. **Persistence workflow** — fetch-on-resume, write-on-turn-close; the
   *What's next* read/write path and protocol; artifact placement rules within
   the work folder.
5. **PAT & credential hygiene** — the operator-side rules above.
6. **Commit discipline** — commit author and message conventions; signing
   left to the operator (their repo); the committer model in force.
7. **Redaction note** *(conditional)* — heavier if the operator's repo is
   public, lighter if private.
8. **Resume protocol** — the literal session-start instruction: fetch *What's
   next* from its path, read it, proceed.

The value and contract for `repo_backed` are fixed in
§{section.orchestration-driver-and-persistence-axes}; this subsection is the
mechanics that realize them. The triple contract
(§{section.the-triple-contract}) is untouched: `repo_backed` changes only
where durable state lives, never how the Envelope/Self-check/Output interface
works.
