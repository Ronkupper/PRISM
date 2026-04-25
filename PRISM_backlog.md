# PRISM Backlog

**Version:** 7
**Maintained by:** Ron Kuper + Claude
**Purpose:** Capture ideas, proposals, and deferred items for future PRISM versions. Separate from PRISM.md because backlog items are proposals, not in-force rules — keeping them out of PRISM.md preserves the "everything in PRISM.md is canonical" property.

---

## How to use this file

Attach this file to planning/workshop sessions where PRISM evolution is being discussed. Do not attach it to regular PRISM project sessions — it's not canonical and would add noise.

When an item promotes to a version, move it from **Accepted for next version** into PRISM.md's Version History, and delete it from this file (or move to **Shipped** with the version number, if a record of the backlog lineage is useful).

When an item is declined, move it to **Declined** with rationale — prevents re-litigating the same idea across cycles.

---

## Structure

- **Active proposals** — being workshopped, no decision yet
- **Accepted for next version** — committed to a specific version, not yet built
- **Deferred** — considered, held for later with rationale
- **Declined** — considered, rejected with rationale
- **Shipped** — optional historical record of which backlog items made it into which version

---

## Active proposals

### Contribution channel for cross-vendor adaptations

**Triggered by:** v1.10.1's compatibility notice. The user-facing invitation ("ask your LLM of choice to adapt the Claude-specific machinery... we'd love to get your upgrade. Share what you built, tell us what broke, send patches back.") promises a destination that doesn't yet exist.

**The gap:** A non-Claude user who takes the invitation seriously and produces a working GPT or Gemini port has nowhere obvious to send it. "PRISM grows through the projects that feed it" is vibes-accurate but infrastructure-absent. Before the first real contribution lands and asks "where do I send this?", PRISM should have a channel ready.

**Options to consider (not decided):**
- **GitHub repo (public)** with CONTRIBUTING.md and issue/PR templates — the expected pattern for open-source, but adds maintenance overhead (watching issues, triaging PRs, responding to questions)
- **Dedicated email address** — lowest overhead, but contributions are private by default; hard to surface them to future users who'd benefit
- **Gist registry** — a single index Gist pointing to community-published adaptations, each hosted wherever the contributor prefers. Lightweight on the maintainer side, handles the read-side well
- **Discord / community space** — social and responsive, but conversations fragment over time; no durable record without extra curation

**Urgency:** Not blocking. v1.10.1 shipped with the invitation and is usable as-is. Becomes time-sensitive when the first actual contribution arrives with nowhere to go — answering "thanks, can you send it to... uh..." would be a worse experience than having said nothing at all in the invitation.

**Likely resolution:** a future version (v1.10.2 patch or v1.11 minor, depending on whether the channel itself requires any framework-side changes) adds a **Contributing** subsection to PRISM.md pointing to the chosen channel. The invitation text in the v1.10.1 compatibility notice stays as-is; it just gains a concrete pointer. Also worth: a section in the Starter's README template for projects to optionally credit community adaptations they used.

**User commitment:** "I would like to do that at some point near future" — v1.10.1 build session, Apr 2026.

---

### Cowork + Computer Use for framework execution

**Triggered by:** User note, Apr 2026. Cowork (Anthropic's desktop file/task automation tool) with Computer Use enabled could automate the multi-vendor orchestration PRISM currently runs manually.

**The idea:** Multi-LLM triangulation (Claude / ChatGPT / Gemini / Perplexity) is hand-driven today — open each vendor's interface, paste prompts, collect outputs, hand-off to Convergence. Cowork with Computer Use could in principle drive the browser-based vendors, run prompts in sequence, collect outputs into files, and stage a consolidated set for the synthesis steps. Folds the mechanical cross-vendor work into a single orchestrating session.

**What to investigate:**
- Whether Cowork + Computer Use handles authenticated web UIs (ChatGPT / Gemini / Perplexity logins, session persistence, file uploads per vendor) reliably enough for a full run, or degrades on the edge cases.
- How this interacts with SP-5 / SP-9 ("flag, don't assume" / "silence is never consent"). Computer Use makes many micro-decisions; the framework has to decide which surface for operator approval vs. run autonomously. Default should be aggressive surfacing until reliability is established.
- Whether automated orchestration preserves the epistemic value of multi-vendor triangulation. Different vendors have different failure modes — those still surface regardless of who types the prompts, so probably yes, but the operator's real-time judgment calls ("that Gemini output went off-rails, re-run") need a place to land in the automated flow.
- Augments the mobile-first workflow with a desktop-mode execution path. If Cowork + Computer Use works reliably, both modes are first-class: mobile-mode retains its advantages (portability, low ceremony, the thinking/doing separation that mobile friction naturally enforces), desktop-mode gains automation of the mechanical cross-vendor work. Neither is the "real" way to run PRISM; the operator picks per project based on what the project needs.

**Open questions:**
- New Execution Mode flag at Setup (alongside the LLM access flag from v1.9), or a separate build path?
- Does this compose with PRISM's existing handoff-artifact pattern (thinking/doing separation), or is the temptation to run everything in one agentic session going to collapse the gap that separation exists to preserve?

**Urgency:** Not blocking. Exploratory — depends on Cowork's actual capabilities as they mature, and on Computer Use reliability curves generally.

---

### Claude Plugins integration (native)

**Triggered by:** User note, Apr 2026. Anthropic maintains an official plugin directory ([claude.com/plugins](https://claude.com/plugins)) bundling MCPs, skills, and tools for Claude Code and Cowork. PRISM currently doesn't reference any of them.

**The idea:** Several plugins in the directory pair directly with PRISM audit work. Naming the right plugin in a prompt's execution envelope could produce higher-quality intermediate artifacts than generic prompting. Exemplar categories and named plugins from the current directory:
- **Market / competitive research** — ZoomInfo (company & contact enrichment, AI-ranked lookalikes), Nimble Web Data (web crawl + structured extraction)
- **Live product inspection** — Playwright, Chrome DevTools (drive the audit subject, capture screens, inspect network)
- **Data ingestion** — Firecrawl (convert product surface to LLM-ready data), Data plugin (SQL / dataset exploration, Cowork-native)
- **Design surface** — Figma (access design files), Frontend Design (produce UI recommendation artifacts)
- **PRISM maintenance** — framework iteration, not audit execution — Skill Creator, CLAUDE.md Management, Superpowers

**Hard platform gate:** Plugins run in Claude Code or Cowork, not in stock claude.ai (mobile or web). Plugin integration is therefore unavailable in PRISM's default mobile-first execution mode. Couples tightly to the Cowork + Computer Use proposal above — any execution mode that exposes Claude Plugins is a desktop-mode variant by definition.

**What to investigate:**
- Which specific plugins clear a usefulness threshold for PRISM (shortlist, not blanket endorsement). The actual audit workload determines the shortlist, not the feature list.
- **"Need to look them up each time?"** — the directory is browsable but large (80+ plugins already) and still growing. Any PRISM reference would be a curated shortlist of plugin↔prompt pairings, not the whole catalog, and would age faster than the framework itself. Probably lives as a separate reference alongside PRISM.md — same ageing argument as the vendor-to-role mapping in v1.9.
- Interaction with SP-5 / SP-9 — plugins that take external actions (Firecrawl crawls, Playwright clicks, ZoomInfo lookups consuming credit) need consent surfaces. Same pattern as Computer Use; likely resolvable with the same machinery.

**Open questions:**
- Does meaningful plugin uplift promote the Cowork + Computer Use proposal from "exploratory" to "recommended for projects where plugin advantage is material"?
- Is there a "PRISM Plugin" worth building eventually — a single bundle shipping PRISM as a Skill plus a curated set of companion plugins? Out of scope for 2026 but worth flagging.

**Urgency:** Not blocking. Gated on Cowork proposal resolution — no point investing in plugin shortlists if the execution-mode decision lands against desktop variants.

---

### Multi-vendor skills/plugins ecosystems

**Triggered by:** User note, Apr 2026. Perplexity ships its own Skills library (e.g., `marketing-competitive-analysis`, under its computer-use surface). Claude Plugins are not a Claude-specific anomaly — they're one instance of a broader pattern where every major vendor is building a skill/plugin ecosystem. PRISM's role-based vendor recommendations (v1.9) should account for this.

**The idea:** Vendor skill coverage is now a first-class signal of vendor fit for specific prompt roles. "Use Perplexity for competitive analysis" becomes stronger when Perplexity literally ships a `marketing-competitive-analysis` Skill — the vendor has invested in that capability surface deliberately, not just incidentally. Multi-vendor triangulation gets richer, not redundant: different vendors bring different skill libraries, which means different blind spots and different strengths surface in the same audit. Epistemically additive.

**What to investigate:**
- Survey scope: which vendors currently ship named skill/plugin libraries (Claude and Perplexity confirmed; OpenAI GPTs, Gemini Gems likely analogous but mechanically different). Which PRISM prompt roles have strong skill coverage from at least one vendor? Which don't?
- **Platform gate consistency:** Claude Plugins require Cowork / Code. Perplexity Skills appear to live in their computer-use context. The pattern across vendors seems to be that skill/plugin ecosystems are gated on agentic/desktop surfaces, not chat-default surfaces. Worth confirming — if general, it generalises the Cowork coupling to "any desktop-mode execution variant, for any vendor," not just Claude.
- **Vendor-to-role mapping reference:** v1.9 established that this mapping lives outside PRISM.md because it ages fast. Skill-coverage columns (per-vendor skill library, named skills relevant to PRISM roles) are a natural addition to that reference. Doesn't touch PRISM.md.

**Open questions:**
- Does skill coverage get weight alongside raw model capability in the vendor-for-role recommendation? Probably yes, but needs explicit framing — capability ∧ skill coverage, not either alone.
- When a vendor is recommended for a role because of its skill coverage, does PRISM recommend *using* that vendor's specific skill, or treat skill availability as a signal that the vendor has strong latent capability even when invoked in chat-default mode? First is more leveraged, second is more flexible. Likely depends on whether the operator is in a desktop execution variant (gate from the entry above).

**Urgency:** Not blocking. Low-cost research — a vendor survey session cataloguing current skill libraries and mapping them to PRISM prompt roles produces the v1.9 mapping reference's next revision without needing framework changes.

---

### Repo-backed PRISM mode (operator GitHub flow)

**Triggered by:** User note, Apr 25, 2026. Adoption of the PRISM-GitHub Workflow v1 in PRISM's own development project (paired `PRISM` public + `PRISM-workshop` private repos, fetch-on-demand reads, signed commits as durable artifact handoff) produced substantial flow improvement over the previous download-attach-reattach cycle. User declared the new flow non-negotiable for future PRISM projects ("can't go back to download-attach"). The infrastructure that PRISM dogfoods on itself should be promotable to a first-class operator mode, not just internal scaffolding.

**The idea:** A new execution mode where the operator backs their PRISM project with a GitHub repo (or paired repos) instead of relying on Claude.ai project knowledge + per-session attachments. Credentials (PAT + SSH signing key) live in project files; durable artifacts (probes, handoffs, Setup outputs, evidence captures, learnings, audit findings) commit to the repo at session boundaries; subsequent sessions fetch from the repo on demand rather than re-attaching files. Replaces the download-attach-reattach cycle that currently moves artifacts between sessions with a commit-fetch cycle that's automatic, diffable, and recoverable.

**Why this is structural, not cosmetic:**
- **Solves cross-session handoff at the right layer.** The current model treats Claude.ai project knowledge as the artifact store, which puts upload/download friction on every session boundary. Repo-backed mode treats the repo as the artifact store, with sessions as ephemeral views.
- **Pairs naturally with PRISM's session discipline.** Thinking/doing separation already produces clean session boundaries; signed commits at those boundaries are first-class evidence of what each session shipped.
- **Built-in version history and recoverability.** Audit artifacts diff cleanly across revisions. Project deletion / model migration / context pressure no longer threaten durable state.
- **Generalises beyond Claude.** Public-repo reads work from any vendor's session (ChatGPT, Gemini, Perplexity); only writes need authenticated Claude. Aligns with PRISM's multi-vendor methodology rather than fighting it.

**What to investigate:**
- **Artifact scope.** Which artifact classes belong in the repo (Setup outputs, probes, handoffs, evidence, learnings, findings) vs. stay session-local (scratch, exploratory thinking, single-turn outputs)? Default heuristic: anything a future session would re-attach today belongs in the repo; anything purely intra-session does not.
- **Repo topology.** Single repo (private, all artifacts) vs. paired (private working + public deliverable, mirroring PRISM's own dev model). Paired makes sense when there's a publishable audit deliverable; single is right for sensitive subjects with no public artifact. Decision rule needs explicit framing.
- **Onboarding cost.** PAT + SSH signing key + git config is a real friction barrier for non-technical operators. Options to lower it: a setup script that walks the operator through PAT creation and key generation; a stripped-down "read-only" variant where the operator's repo is public and Claude only writes via PR; explicit acceptance that repo-backed mode self-selects for technical operators and chat-default mode remains the friction-free path.
- **Multi-vendor symmetry.** Claude with bash + filesystem + project files writes back natively. ChatGPT, Gemini, and Perplexity sessions can fetch from public repos but lack credentialed write-back. Asymmetry probably acceptable given existing role split (Claude as build/synthesis, others as parallel input/critique), but worth naming so operators know what to expect.
- **PAT/key lifecycle.** Project-side credentials rotate. The framework needs a recurring lifecycle nudge (PAT expiration warning, signing-key rotation prompt) — already learned in the PRISM dev project, generalisable.

**Open questions:**
- **Required, recommended, or optional?** Probably optional + recommended for multi-session projects, given onboarding cost. Required would cut off non-technical operators; required-after-N-sessions is a possible middle ground.
- **Default repo template.** What does a fresh PRISM project repo ship with? A direct mirror of `PRISM-workshop`'s structure (`design/`, `handoffs/`, `synthesis/`, `protocols/`, `notes/`, `archive/`) probably overshoots for an audit project; a slimmer audit-specific layout (`probes/`, `handoffs/`, `evidence/`, `findings/`, `learnings.md`) likely fits better. Worth a v0 spec.
- **Interaction with existing Scope Flags.** New orthogonal flag (Execution Mode: chat-default / repo-backed)? Or a sub-option under the LLM access flag? Probably orthogonal — repo-backed mode is independent of multi-vendor access.
- **Setup automation.** Does PRISM ship a Setup-time prompt sequence that, given a repo URL and credentials, scaffolds the layout, drops in canonical placement docs, and configures git? Or does it stop at "here's the recommended structure, set it up yourself"? First is much more leveraged but more to maintain.

**Composition with existing backlog:**
- **Cowork + Computer Use:** Composes well — desktop-mode execution with repo-backed artifacts is the most leveraged combination. Repo-backed mode can ship independent of Cowork, but Cowork without repo-backed mode would re-introduce the artifact-handoff problem this entry exists to solve.
- **Contribution channel for cross-vendor adaptations:** Repo-backed mode produces natural cross-vendor adaptation artifacts (each operator's repo is itself a worked example). Channel design should account for this.

**Urgency:** Not blocking for v2.0 operators today; current download-attach mode works. Becomes higher priority before the user's next PRISM project starts — already a stated requirement for that project.

**User commitment:** "I want to introduce a PRISM mode to support it first-class. As an operator I'd like my next PRISM project to use this flow. Can't go back to download-attach." — Apr 25, 2026.

---

## Accepted for v1.9

### ask_user_input UX integration

**Proposed mechanism:** Use the `ask_user_input` tool (where available) for decision points that have clean discrete options. Specifically:
- **Setup Scope Flags** — one bundled multi-question call covering the five flags, with "Keep all defaults" as a single-option shortcut for users who want to proceed quickly
- **Enrichment Scoping** — per-prompt approve/decline/defer choices
- **M10 classification** — rerun / injected prompt / standalone fix
- **Adaptation confirmation** — approve / modify / reject

**Not used for:**
- GATE-0 pass/fail output (informational, no decision)
- Monitor triggers that log rather than decide (M2, M7, M8)
- Free-text clarifications (SP-5 territory — "stop and ask" is rarely two or three clean options)

**Fallback:** When `ask_user_input` is unavailable (API contexts, non-tool-enabled sessions), Claude falls back to prose ask — the current behaviour. Codified via new SP-9.

**No timer.** Explicitly rejected. A timer that auto-picks the default would make *silence* a decision, which inverts PRISM's core "flag, don't assume" ethos (SP-5, full-decline flag rule). SP-9 generalises this stance.

**Decisions made in workshop session:**
- Binary is fine; "Keep all defaults" shortcut for Scope Flags is the most common path
- Prose fallback, not feature-required

---

### LLM access Scope Flag + execution envelope

**Proposed mechanism:** Two linked additions.

**1. New Scope Flag: LLM access**
- Options: `claude-only` / `multi-vendor`
- Default: `claude-only` (conservative — PRISM is a Claude skill, Claude is always available)
- When `multi-vendor`, user declares which vendors/tiers they have access to at Setup. Per-project declaration (not persisted across projects) — access churns and a 10-second tap at Setup is honest about current state.
- Consistency check: if enrichment flag is `full` or `minimal` but LLM access flag is `claude-only`, flag the mismatch (same pattern as full-decline flag rule).

**2. Execution envelope on the attach map**
- New columns on the attach map (not a separate table — keeps it in one place, mobile scroll is acceptable): Web Search (y/n), Deep Research mode (y/n), Recommended vendor (role-based, not hardcoded)
- Adaptive Thinking: recommended on at Setup as a one-time flag, not per-prompt. Claude doesn't override per-prompt because the model itself is deciding per-turn when Adaptive Thinking is on.

**Role-based vendor recommendation:** The framework describes *roles* ("use a vendor with strong multi-document synthesis for DR"), not named vendors. Vendor-to-role mapping is a separate, shorter-lived reference (either a project-level note or a user-level default table) that ages without forcing PRISM.md to age with it.

**Fallback language when best vendor is unavailable:** "Recommended: [best vendor]. Not in your access set — falling back to [alternative]. Caveat: [what's lost in the swap]." Same flag-don't-assume ethos.

**Claude as default:** Stated explicitly in the framework — when no vendor recommendation is given, Claude is assumed.

**Decisions made in workshop session:**
- Binary for access flag (claude-only / multi-vendor)
- Execution envelope as new columns on attach map, not separate table
- Role-based recommendations, not named-vendor hardcoding
- Adaptive Thinking as Setup-level recommendation only; no per-prompt thinking-depth matrix (platform is already deciding per-turn, framework recommendation would be redundant or wrong)
- Vendor access declaration is per-project, not user-level persisted

---

### SP-9: Silence is never consent

**Proposed mechanism:** New Standing Principle generalising the no-timer rationale and codifying the `ask_user_input`/prose-fallback behaviour.

**Text:** When a decision requires the user's input, Claude stops and asks — either via `ask_user_input` (when available) or via prose question (fallback). Silence, timeouts, and assumed-default auto-advance are never valid substitutes. This applies to Scope Flags, Enrichment Scoping, M10 classification, Adaptation confirmation, and any future decision point added to the framework.

**Rationale for SP status (not just a behavioural note):** The principle generalises beyond ask_user_input — it's a framework-wide stance that applies everywhere an ambiguous input or decision surfaces. SP-5 already says "no heuristic guessing"; SP-9 extends that to cover tool-mediated interaction patterns. Adding an SP is the appropriate signal that this is a load-bearing default, not an implementation detail.

---

## Deferred

*(none currently)*

---

## Declined

### Timer on ask_user_input with auto-advance to default

**Proposed:** In workshop, user initially suggested a timer with high-confidence defaults auto-advancing on timeout.

**Declined because:** Inverts PRISM's core ethos. SP-5 ("no heuristic guessing on ambiguous input"), the full-decline flag rule, and the general stance of "flag, don't assume" all require explicit user input on decisions. A timer makes silence a decision — the user not tapping becomes the user consenting to the default. PRISM's "Keep all defaults" shortcut solves the same convenience problem (one tap for the common path) without conceding the principle.

Codified as SP-9 in v1.9.

---

### Named-vendor recommendations in PRISM.md

**Proposed:** Embed specific vendor recommendations in the framework file ("use Gemini Pro for Deep Research, Perplexity for Fact Check").

**Declined because:** Vendor strengths drift on a 6-12 month timescale; the framework file is meant to outlive specific vendor capabilities. Named-vendor recommendations would force frequent patch bumps just to stay current, and would be wrong more often than right.

**Resolution:** Role-based recommendations in PRISM.md ("use a vendor with strong multi-document synthesis for DR"), with vendor-to-role mapping kept as a separate, shorter-lived reference. Adopted in v1.9.

---

### Per-prompt thinking-depth matrix

**Proposed:** A matrix in PRISM.md specifying which prompts benefit from extended thinking ("Red Team → extended thinking; Layer 2 → extended thinking + Deep Research").

**Declined because:** Claude.ai now exposes Adaptive Thinking as a platform-level flag that decides per-turn whether to think deeply. A framework-level matrix would be redundant at best, wrong at worst — the model itself is making the same decision with more information than the framework has.

**Resolution:** Adaptive Thinking recommended on at Setup as a single flag. No per-prompt thinking-depth column in the execution envelope. Adopted in v1.9.

---

## Shipped

*(moved here when v1.9 is built and the backlog items ship — structure reserved for future use)*

---

*End of backlog.*
