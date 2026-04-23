---
name: prism
description: "Use this skill whenever the user is working on a multi-prompt research or audit project using the PRISM framework. Triggers: mentions of PRISM, Starter file (e.g., *_starter_v*.md), any *_starter_v*.md or *_audit_master*.md file, product audit work, competitive landscape research with multi-LLM triangulation, convergence of multiple LLM outputs, references to running 'P3.2' or similar numbered prompts, red team prompts, fact-check prompts, Prompt Strategy, canonical steps, Rerun Register, requests to run a specialist prompt in a research project. Also triggers when a file matching *_starter_v*.md or *_prompts_v*.md is attached. This skill contains the full PRISM method: Monitors, Gates, Standing Principles, two-layer convergence, Version Management, project folder structure, prompt templates, and learnings register. Read it in full at the start of any PRISM session before doing any work."
---

# PRISM
#### *Prompts · Research · Iteration · Synthesis · Master*
**A Framework for LLM Research and Audits**

**Version:** 1.10.4
**Maintained by:** Ron Kuper + Claude
**Origin:** Distilled from real-world competitive research and product audit projects (2026).

---

## WHAT PRISM IS

Serious research doesn't fit in one prompt. The moment a question spans multiple angles — competitive, technical, financial, strategic — a single LLM session either answers everything shallowly or produces a long, unfocused mass that's hard to trust. Splitting the work across prompts helps, but then the outputs drift out of sync, sources contradict each other, context budgets blow up mid-session, and by session three nobody remembers what the original thesis was.

PRISM is a method that keeps that work coherent — across prompts, across sessions, and across the context limits of any single chat.

- It's built for **multi-prompt research** where one question is too big for one prompt and you need specialist passes that add up to a whole.
- It's about **managing research across sessions** — the project outlives any one chat, with state, decisions, and findings carried forward intact.
- It's **context-disciplined** (or context-engineered) — session scope, working-set size, and context pressure are watched and managed by the framework, so the LLM operates inside its effective limits instead of past them.
- It's a **methodology and a helper** — Monitors, Gates, Standing Principles, a two-layer convergence model, and codified learnings from real projects. It carries project state across sessions, tracks loose ends, and handles the bookkeeping. At any point, in any session, "What's next?" is a valid question — PRISM is designed to recover state reliably and tell you what comes next.
- It's **self-driving at Setup** — the user brings the subject and the goal; PRISM produces the Prompt Strategy, applying prompt-engineering and context-engineering best practices the user doesn't need to know. The user reviews and approves; they don't have to author.
- It's **"foolproof" per prompt** — each prompt in the Strategy arrives as a complete execution package with best-effort guidance: the prompt text, attachments needed, which LLM to run it on (e.g., Claude, Perplexity, Gemini Deep Research), which mode to use, and any platform-specific guidance. The user pastes, attaches, and runs; they don't decide where, how, with what files, or with what settings.
- It's aimed at **output quality** — structure, explicit assumptions, cross-checking, and a cold final synthesis exist to make the deliverable something you can trust, not just something that's done.
- It's **scoped to the project** — Scope Flags at Setup match the framework's machinery to what the work actually requires. Full scope is the default; lighter work opts out of specific machinery.

Concretely: PRISM splits a research or audit problem into independent specialist prompts, each running in its own session, and converges their outputs into a single living document called the **Starter**. The Starter grows as findings arrive, carries project state across sessions, and survives the session-level memory gaps that normally force research to restart. A final cold synthesis pass resolves the full picture with all inputs on the table.

What makes PRISM different from ad-hoc multi-prompt work:

- **Nothing is reconstructed from memory.** Every prompt is self-contained, every finding is written down, every decision is logged. Sessions are disposable; the Starter is not.
- **State survives sessions.** The Starter is designed to be handed to a fresh session and resumed without context loss.
- **Drift is caught early.** Monitors and Gates watch for version drift, premise shifts, missing inputs, and unscheduled reruns before they compound into rework.
- **The plan is explicit — and PRISM writes it.** A Prompt Strategy is produced at Setup by Claude, applying decomposition, atomic prompt design, and context-engineering best practices. The user reviews and approves before work begins. Major version numbers track progress through the Prompt Strategy (not edit count); minor versions absorb the flexibility within each phase — reruns, fixes, enrichment passes, and any drill-down the project needs. The Starter's version at a glance tells you where the project is in its plan.
- **Multi-LLM when the prompt calls for it.** PRISM specifies per-prompt which LLM vendor to use and in which mode (e.g., standard chat, Deep Research, web-enabled). Because prompts are atomic and self-contained, the same question can also be run across different LLMs when cross-validation matters — outputs are compared in the Starter. The user doesn't decide whether, where, or how; the Strategy does.

PRISM lives as a single file. Attach it to any session, or install it as a Claude Skill, and Claude runs the framework.

### The backronym

**P**rompts · **R**esearch · **I**teration · **S**ynthesis · **M**aster — the five movements, roughly in order.

### Companion artifact

The **Starter** is the living master file that grows with each feeding. Named `{project}_starter_v{N}.md`. Single file, always — no splitting.

> **Footnote on naming.** Hu et al. (USC, March 2026) published a technique also called "PRISM" (Persona Routing via Intent-based Self-Modeling). Separate technique, same acronym, same domain. Any references to "the USC PRISM paper" or "Hu et al. 2026" in this framework refer to the persona-prompting research cited in Learning #29 — not to a rival framework or a different version of this one.

---

## WHEN TO USE PRISM

- Product audits (competitive, technical, UX, content, strategy)
- Competitive landscape research
- Market sizing with multiple sources cross-checked
- Investment due diligence
- Any research problem where a single prompt would either be too shallow or too long to trust

## WHEN NOT TO USE PRISM

- Simple factual lookups
- Single-session analysis that fits in one prompt
- Creative work (writing, design) where divergent specialist passes don't add value

---

## GLOSSARY

*Quick-reference definitions for terms that carry specific meaning in PRISM.*

- **Starter** — the single living markdown file that carries all project state. Like its namesake, it grows with each feeding. Named `{project}_starter_v{N}.md`.
- **Atomic prompt** — a prompt that is fully self-contained: carries its own context, instructions, output format, and attachments. Can be handed to a fresh session on any LLM and executed without requiring memory of prior sessions or cross-references to other prompts. The "atomic" unit of PRISM work.
- **Specialist lens** — the principle that each prompt answers one focused question (or one narrow domain) well, rather than trying to cover many angles shallowly. A research project's breadth comes from *running many specialist prompts*, not from one prompt trying to be comprehensive.
- **Canonical step** — a planned forward-motion item in the Prompt Strategy. Drives major version bumps.
- **Non-canonical work** — reruns, fixes, bookkeeping. Drives minor version bumps (even when it adds findings).
- **Layer 1 (Integration)** — incremental, additive merge of new data into the Starter after each source arrives.
- **Layer 2 (Synthesis)** — cold, holistic pass with all inputs on the table. Resolves conflicts, rewrites interpretation, produces the final deliverable.
- **Prompt Strategy** — the articulated plan for which prompts run, in what order, with what dependencies. Produced at Setup, approved before work begins.
- **Scope Flags** — five orthogonal toggles declared at Setup that determine which framework machinery is active for this project. Defaults to full scope.
- **Discovery** — Setup-phase enrichment role. Maps the problem space before the Prompt Strategy is finalised. Can reshape the strategy itself.
- **Coverage** — prompt-phase enrichment role. Finds what a specific prompt's narrower analysis missed within its defined domain. Replaces v1.6's "Scouting" in the prompt-phase context.
- **Delivery Folder** — the project root folder, optimised for stakeholder legibility. Contains the deliverable, Appendices, and `_PRISM/`.
- **Adaptation** — a structural change to the canonical plan mid-project. Major version bump.
- **[UNVERIFIED]** — inline tag on any claim sourced from a single LLM without primary-source verification.
- **[NULL RESULT]** — explicit marker that a prompt investigated a dimension and found nothing material. Informative; silence is ambiguous.
- **[MATERIAL]** — changelog tag on minor-version entries that carry substantive findings (not just housekeeping).
- **GATE-2** — formal readiness check before Layer 2 cold synthesis. Verifies all canonical steps complete, Rerun Register clear, M6 flags assessed.
- **M5 (Attachment Pressure)** — monitor for the attached working set (Starter + LLM outputs + uploads). Threshold ~30% of effective context budget (~300K on 1M context, ~60K on 200K).
- **M12 (Conversation Pressure)** — monitor for accumulated conversation in the current session (turns, outputs, reasoning). Threshold ~50% of effective context budget (~500K on 1M, ~100K on 200K). Combined with M5 via a ~70%-of-effective-context guideline.
- **Context Pressure Bands** — shared reporting convention (🟢 Comfortable / 🟡 Getting warm / 🟠 Curate now / 🔴 Migrate) used by GATE-0, M5, and M12 for reporting combined context usage. Bands exist because LLM token self-estimation is imprecise; qualitative bands are honest about what the estimate is worth. Thresholds are calibration points, not cliffs.
- **SP-9 (Silence is never consent)** — Standing Principle requiring explicit user input on decisions. Silence, timeouts, and auto-advance-on-default are never valid substitutes.
- **SP-10 (Verify current state before recommending)** — Standing Principle requiring web-search verification at recommendation-generation moments for platform/vendor/best-practice state. Output framed as best-effort; user observation weighted where it contradicts training-era knowledge.
- **ask_user_input** — mobile-first tool for presenting tappable multi-choice questions. Used at Scope Flags, Enrichment Scoping, M10 classification, Adaptation confirmation. Falls back to prose per SP-9.
- **Execution notes** — prose guidance written by Claude at Setup for each prompt in the Strategy, covering thinking depth, Web Search, Deep Research mode, and vendor recommendations. Best-effort per SP-10. Lives as a single column on the attach map alongside required attachments.
- **Output Quality Check (OQC)** — six-signal check for thinkless output, split across two locations: live watch during the prompt run (signal #6 preemptive scope-down) and convergence-time check for all six signals. Single-signal trigger for #6; two-signal trigger for #1-5.
- **Runtime Profile** — Setup-time declaration of the host environment's capabilities: host type, effective context budget, file ops availability, conversation history search availability, delivery mechanism. Drives percentage-based threshold calibration and graceful behavior across surfaces.
- **Attachment Discipline** — the framework's explicit convention for when PRISM.md is needed (framework-running sessions: Setup, convergence, Adaptations, bookkeeping, "What's next?") vs. when it isn't (Phase 1 specialist prompt sessions — atomic prompts are self-contained by design).

---

## HOW TO USE THIS FILE

> **A note on LLM compatibility.** PRISM is designed for Claude. The *methodology* — atomic prompts, two-layer convergence, Monitors, Gates, the Learnings Register — transfers to any capable LLM. The *machinery* doesn't: `present_files`, `create_file`, `str_replace`, `conversation_search`, `ask_user_input`, and Claude Skills are Claude-specific, and PRISM.md is written as operating instructions *to Claude*. If running on another vendor, declare `Host = other` in the Runtime Profile at Setup; the graceful-degradation path handles the substitution, but expect manual work for file ops and session continuity.
>
> *To the LLM reading this file:* if you are not Claude (claude.ai, Claude Code, or the Anthropic API), surface this notice to the user at the start of the first session, before any other work. Don't skip on the assumption the user has read the file — they likely haven't.
>
> *To the user running PRISM on another LLM:* ask your LLM of choice to adapt the Claude-specific machinery to its environment — most of the tool calls above have equivalents on other platforms; some need prose workarounds. If your LLM produces a working port for GPT, Gemini, Mistral, or whatever you're running, we'd love to get your upgrade. Share what you built, tell us what broke, send patches back. PRISM grows through the projects that feed it, and cross-vendor adaptations are exactly the kind of contribution that makes the framework better for everyone. 🙂

Attach this file at the start of any PRISM session, or install it as a Claude Skill so it loads automatically. Claude reads it and treats it as the operating manual — no setup, no preamble needed.

To start a new project — or to resume one at any point — attach the file and send:

> What's next?

That's it, every time. Whether you're starting fresh, coming back after a break, or just finished a prompt and don't remember what's next — "What's next?" works. Claude runs GATE-0, reads the Starter, and tells you where the project is and what to do. You never need to remember where you left off.

You don't have to read any of what follows — PRISM is designed to guide you through it. The rest of this file is the operating manual Claude uses; it's here for reference, not as a prerequisite.

The order of sections is the order work happens:

1. **Session Start** — GATE-0 verification before any work begins
2. **Setup** — Scope Flags, Discovery, Enrichment Scoping, Prompt Strategy, new Starter
3. **Phase 1: Specialist Prompts** — running canonical steps
4. **Phase 2: Enrichment** — Coverage, Fact Check, Deep Research, Red Team, User Voice (scoped per project)
5. **Phase 3: Layer 1 Convergence** — incremental integration after each source
6. **GATE-2** — formal readiness check before Layer 2
7. **Phase 4: Layer 2 Convergence** — cold synthesis with all inputs in
8. **Monitors** — proactive checks running throughout
9. **Adaptations** — the flex mechanism
10. **Project Folder Structure** — Delivery Folder, Appendices, `_PRISM/`
11. **Learnings Register** — what we've learned so far

---

## ATTACHMENT DISCIPLINE

PRISM.md is roughly 45K tokens (v1.10, on current Claude tokenization). On a 1M-token context budget that's ~4-5% of context just for the framework file; on a 200K-token context it's over 20%. Overhead matters, and where PRISM.md needs to be attached is explicit by design.

**PRISM.md is needed for:**
- Setup sessions (drafting Prompt Strategy, running Discovery if scoped, writing atomic prompt texts, verifying per SP-10)
- Convergence sessions (Layer 1 integration after each source, Layer 2 cold synthesis)
- Adaptation sessions (any structural change to the canonical plan)
- Bookkeeping sessions (Monitor triggers, Rerun Register scheduling, process updates)
- "What's next?" sessions where Claude is running the framework for you

**PRISM.md is NOT needed for:**
- Phase 1 specialist prompt sessions — the user copies the atomic prompt text out of the Starter into a fresh conversation, attaches only the files in the attach map, and runs. The prompt is atomic and self-contained by design; it carries its own context, its own output format, its own convergence checklist. The fresh session running the prompt doesn't need PRISM.md because the prompt has already been shaped by PRISM.md at Setup.

**This is deliberate.** The framework overhead concentrates where it matters least for raw context budget — framework-running sessions have less competition from research content. Research sessions (where findings, LLM outputs, and attachments compete for context) stay unburdened by the framework file itself. The atomic prompt principle isn't just about session independence; it's also about context economy.

**Attach PRISM.md** when you're going to ask Claude to *run the framework*. Don't attach it when you're going to ask Claude to *run a prompt that PRISM has shaped*. The distinction is in the Status Tracker — convergence and framework-level work use PRISM.md; executing a canonical prompt uses the prompt text plus attach-map items.

---

## CORE CONCEPTS

### The Starter file

One markdown file per project. Named `{project}_starter_v{N}.md`. **Single file always — never split.** Holds:
- Prompt Strategy (the articulated plan, with Scope Flags and attach map)
- Status Tracker (canonical step progress, with Delivery Filename column)
- Rerun Register (live fix task list)
- Assumption Register
- Findings (one section per canonical step)
- Enrichment Findings (if scoped)
- Sources
- Final Synthesis (populated at Layer 2)
- Changelog (narrative form — substantive entries per version)
- Action Log (process-health events from Monitors and Adaptations)
- Prompts (atomic prompt texts for each canonical step)

### Atomic prompts

Every prompt is self-contained:
- Carries its own product context
- Carries its own technical/process notes (not "see master file")
- Specifies its own output format
- Contains its own convergence checklist

This means prompts can be run in a fresh session, across different LLMs, without losing state. It also means prompt premises need to be updated when findings shift them — handled by Monitor **M6**.

### The Prompt Strategy

The **Prompt Strategy** is the articulated plan for a PRISM project — the thoughtful, carefully laid-out scheme of what prompts will run, in what order, with what dependencies, producing what outputs. It's produced during SETUP as Claude's primary deliverable and approved by the user before any work begins.

It lives as a top-level section in the Starter, near the top. It defines what counts as **canonical** (the planned main path) for this project. It changes only through **Adaptations** — structural modifications like injecting a new prompt or adjusting the run order. Each Adaptation drives a major version bump because it changes the canonical plan.

The Prompt Strategy answers: why these prompts? In what sequence? What depends on what? What comes out of each? How will multi-LLM outputs be collected? What attachments does each prompt need? Which enrichments were scoped per prompt (and which declined)? When it changes, why?

### Prompt numbering

**Integer IDs for peer prompts:** P1, P2, P3, P4... Each is an independent specialist lens in the Prompt Strategy.

**Decimal IDs for nested enrichment:** When a prompt gains multi-LLM enrichment mid-project (or is scoped with it from the start), sub-prompts use decimal notation: P3.1 (Coverage), P3.2 (Fact Check), P3.3 (Deep Research). The original prompt stays as P3. Decimal indicates "enriches P3's domain."

**Role lives in the name, not the ID.** Enrichment roles (a guidance catalog, not a required vocabulary):
- **Discovery** — Setup-phase role. Maps the problem space *before* the Prompt Strategy is finalised. Runs once, on 3-4 LLMs. Not numbered as P#.x — runs at project level, feeds the Prompt Strategy itself.
- **Coverage** — prompt-phase role (formerly "Scouting"). Finds what a specific prompt's narrower analysis missed within its defined domain. Run on 3-4 LLMs. Divergence is the signal.
- **Fact Check** — cross-platform verification of specific claims. Run on 2 LLMs. Convergence is the signal.
- **Deep Research** — extended research on a specific dimension. Run on 1-2 LLMs.
- **Red Team** — adversarial stress test of the thesis. Run on 1 LLM.
- **User Voice** — mine real user perspectives. Run on 1 LLM.

**Atomic = one prompt text.** Running the same prompt on 4 LLMs is parallelism *within* a prompt, not four separate prompts.

### Canonical steps

A **canonical step** is a planned forward-motion item in the main path laid out by the Prompt Strategy. Canonical includes:
- Specialist prompts (P1, P2, P3...)
- Enrichment sub-prompts (P3.1, P3.2, P3.3...)
- Layer 2 cold synthesis
- New prompts promoted into the plan via Adaptation

**Non-canonical work** includes:
- Reruns of prior canonical steps (tracked in Rerun Register)
- Injected fixes that don't become promoted prompts
- Standalone fix sessions
- Monitor-triggered bookkeeping updates
- Process tweaks, corrections, formatting fixes

The canonical / non-canonical distinction drives version bumps directly: **canonical progress = major bump. Non-canonical work = minor bump**, even when it adds findings. See **VERSION MANAGEMENT** for the full rules.

### The Rerun Register

Separate from the Action Log (historical event log), the **Rerun Register** is a live task list of rerun and fix work that needs to be done but can't be deferred per SP-2. Each entry tracks:
- Target (which canonical step needs rerun, or what gap needs a new prompt)
- Classification (rerun / injected prompt / standalone fix)
- Rationale (why — the finding or failure that triggered it)
- Scope (what changes from the original)
- Target session (when it'll happen)
- Status (⬜ scheduled / 🔄 in progress / ✅ complete / 🚫 cancelled)

Entries are created by Monitor **M10** and closed when the work completes. The Rerun Register is checked as part of GATE-0 at every session start — scheduled reruns don't get forgotten.

### Layer 1 and Layer 2 convergence

**Layer 1 — Integration (incremental, after each source):**
- Purpose: merge new data into the Starter
- Scope: *additive and corrective only* — new entries, corrected facts, updated tables, added sources
- "Corrected facts" means **uncontested factual errors only** — if two sources disagree, that's a conflict for Layer 2, not a correction for Layer 1
- Does NOT: rewrite interpretation, resolve conflicts, synthesise themes, update recommendations, touch the executive summary
- Produces: major version bump when the source is a canonical step (per VERSION MANAGEMENT)

**Layer 2 — Synthesis (cold, after all sources are in):**
- Purpose: step back and look at the whole
- Scope: everything above the facts layer — conflict resolution, premise re-examination, interpretation updates, executive summary
- Requires: all planned canonical steps complete, no new inputs expected
- Runs in a **fresh conversation** to avoid anchoring on the working draft
- Produces: major version bump (final synthesis — often the definitive version of the project), substantive Changelog entry

Getting these confused is a common failure mode. Monitor **M9** catches Layer 1 work that's sneaking interpretation in, or Layer 2 work that's still trying to add new sources.

### Monitors

Proactive checks with explicit triggers. They fire throughout the session, not just at fixed points. Every Monitor that triggers produces visible output — if Claude doesn't print it, it didn't happen. See the full list in the **Monitors** section below.

### Gates

Mandatory checks at specific moments. **GATE-0** runs at session start. **GATE-1** runs between canonical steps. **GATE-2** runs before Layer 2 cold synthesis. More may be added as we learn.

### Adaptations

The framework flexes. Adding a new prompt mid-project, injecting a multi-LLM enrichment layer, reshuffling the run order, adding a new dimension — all allowed, all documented. Adaptations change the canonical plan and are major-bump events. See the **Adaptations** section.

---

## STANDING PRINCIPLES

*These apply at all times, in every session, regardless of phase. They're not checks — they're defaults Claude must never violate.*

### SP-1: Never reconstruct files from memory

If a needed file (Starter, LLM output, prior deliverable) is not in the current context, **stop and ask the user to upload it by exact filename**. Do not rebuild from memory, even with strong recall. Even "I remember most of it" is a failure mode — subtle content drifts silently and the diff/verify cycle costs more than the upload.

This applies especially at session start, but also mid-session if a reference becomes needed. The moment Claude catches itself thinking "I'll just reconstruct this," it's already wrong.

### SP-2: Defer non-critical fixes to the next natural touchpoint

When a canonical step produces a minor issue (wrong detail captured, imprecise measurement, missing peripheral content), do not burn a standalone session fixing it. Instead:
- Flag the issue in the Action Log
- Assign the fix to whichever upcoming canonical step naturally overlaps the affected area
- Proceed with current work

**Valid deferral requires all three:**
- A natural touchpoint exists within the remaining canonical sequence
- The issue doesn't block downstream work
- The fix fits into the future step's scope without expanding it

**If any requirement fails → Monitor M10 fires.** The issue gets scheduled explicitly in the Rerun Register as a rerun, injected prompt, or standalone fix session. Nothing falls through the cracks.

Example: a P1 walkthrough captured wrong content on one walkthrough step due to fast JS navigation. The issue fit into a later prompt's scope, which was already scheduled to cover that area. Deferral was valid — fix happened inside the later prompt, zero extra sessions.

### SP-3: Convergence is part of prompt delivery, never a separate step

When a specialist prompt completes, Claude updates the Starter in the same session — paste findings, merge Assumption Register, update Status Tracker, bump version, deliver new file. Leaving convergence to the user or "for later" is the exact manual, error-prone step PRISM is designed to eliminate. Learned the hard way on an earlier project — convergence left for a later session drifted, and the resulting diff-and-verify cost more than doing it inline would have.

### SP-4: Every Monitor that triggers produces visible output

Silent monitors are useless monitors. Discrete-trigger monitors (M1–M10) print their labeled output block on fire. Condition monitors (M11) print when conditions are met. Advisory monitors (M12) print when thresholds are crossed. If Claude doesn't print, the user has no way to know it ran — and therefore no way to trust it did.

### SP-5: No heuristic guessing on ambiguous input

If GATE-0 or any Monitor flags ambiguity, stop and ask. Do not proceed with "best interpretation." Do not reconstruct intent. The cost of one extra question is always lower than the cost of wrong work.

### SP-6: Rebuild at threshold

When producing a new Starter version (or any file update):
- **≤~8 sequential edits** → use `str_replace` for surgical edits
- **>~8 sequential edits, renumbering cascades, or structural changes across the file** → use `create_file` to rebuild the entire new version from scratch

**Why:** Sequential `str_replace` edits hold the full file state in working memory between calls. Each edit requires Claude to re-anchor on current file content, track what's already been changed, and plan what's left. By the time a file has accumulated ~8+ sequential surgical edits, working memory is loaded with file structure, new content, remaining edit plan, and the task context — that's where slowdowns and near-stalls happen.

**Threshold calibration:** the ~8 figure is set on the cautious side of an observed 8–12 variance in sequential-edit stall onset. Err toward the lower bound — staying safely inside the stall zone beats discovering it at edit #11.

**`create_file` is one tool call.** No cascading state. No string-match failures. No renumbering hell. The old version is right there for reference, so drop-risk is low.

**Source:** Learned from a past convergence session — 15 sequential edits across ~600 lines, slowdown and near-stall at edit #12.

### SP-7: File delivery is mandatory

Every session that produces or modifies a file must: copy it to `/mnt/user-data/outputs/` with the correct versioned filename, then call `present_files`. This is a closing action, not an optional post-QA step. If Claude does not deliver the file, the session's work is inaccessible to the user. No exceptions — applies to prompt sessions, convergence sessions, bookkeeping sessions, and Adaptation sessions alike.

### SP-8: The delivered file is canonical; look-alike files are disambiguated by name

The file Claude delivers via `present_files` is the canonical file for that project state. Any edit made outside a Claude session (desktop editor, phone annotation, external LLM) must be flagged at the start of the next session so GATE-0 can reconcile.

Conversely: PRISM enrichment naturally produces look-alike files (DR1/DR2 from different LLMs, FC outputs from multiple platforms). These must carry role and source in predictable filename order:

```
[LLM] — [Prompt ID] — [Description]
```

Examples:
```
Claude DR — P3.1 — Competitive Coverage
Gemini DR — P3.2 — Fact Check Results
```

The em-dash (` — `) is deliberate: the pipe character (`|`) is illegal in Windows filenames and shell-active on Unix, both of which create portability problems when projects are downloaded, scripted over, or moved between machines. Em-dash is filesystem-safe everywhere and visually unambiguous.

GATE-0 parses attached filenames against the attach map and flags any that don't match the expected pattern. Human error in picking "the wrong file that looks similar" is a specific failure mode PRISM creates by design — the naming convention is the defense.

### SP-9: Silence is never consent

When a decision requires the user's input, Claude stops and asks. Silence, timeouts, and auto-advance-on-default are never valid substitutes for an answer. The user not responding is not the user consenting.

This generalises across the framework:
- **Setup Scope Flags** — the user actively taps "Keep all defaults" or adjusts specific flags. The absence of a response is not "keep defaults."
- **Enrichment Scoping** — the user actively approves or declines each proposed enrichment. Omission is not acceptance.
- **M10 classification** — the user confirms rerun / injected prompt / standalone fix. Claude does not auto-classify.
- **Adaptation confirmation** — the user approves the Adaptation before it executes. Silence is not a go-ahead.

**Mechanism:** Where the `ask_user_input` tool is available (mobile chat interface), use it for clean discrete choices — two to four tappable options per question, with defaults pre-selected where applicable. Where `ask_user_input` is unavailable (API contexts, non-tool-enabled sessions, or the tool isn't surfaced), fall back to a prose question. Either mechanism requires an actual response before proceeding.

**No timers.** A timer that auto-picks the default on timeout would make silence a decision, which inverts the principle. "Keep all defaults" is available as a single-option shortcut in interfaces that support it — the user still taps. The convenience of one-tap consent is preserved without conceding that silence ever means yes.

**Why this is an SP, not a behavioural note:** The principle generalises beyond any specific tool. SP-5 ("no heuristic guessing on ambiguous input") established that Claude doesn't interpret; SP-9 extends that to tool-mediated interaction patterns, where the temptation is structural rather than interpretive. Together, SP-5 and SP-9 close the two main failure modes: guessing when the input was ambiguous, and proceeding when the input was absent.

### SP-10: Verify current state before recommending

When Claude generates recommendations that depend on current platform, vendor, model, or prompt-engineering best-practice state, Claude verifies before recommending. Training knowledge is reliably out of date for fast-moving domains: vendor capabilities drift on a 3-6 month cycle, platform flags (Adaptive Thinking, Deep Research modes, effort levels) change behaviour across model releases, and best-practice conventions evolve.

**Verification pattern:** one or two targeted web searches at recommendation-generation moments — Setup (execution notes, vendor recommendations), Adaptations that change recommendations, mid-flight recommendation triggers. Include UI/interface queries when the user runs prompts in a specific chat interface, not just API/capability queries.

**Calibrated output:** the search result is input to a recommendation, not a substitution for it. Claude reconciles search findings with the user's own observations (especially observations of a specific interface's current controls), with the prompt's requirements, and with remaining uncertainty. Recommendations are framed as **best-effort** with explicit uncertainty callouts where search didn't resolve the question.

**User observation weighting:** when the user reports platform behaviour that contradicts training-era knowledge, weight the user's observation. They are looking at the current state of the tool; Claude is not. A single search may not resolve what a glance at the UI does.

**Graceful degradation:** when verification yields nothing useful — search fails, domain is too niche, the platform is too new for coverage — the recommendation degrades gracefully rather than fabricating confidence. Frame as: *"Based on training-era knowledge (may be stale). Verify against your own experience."*

**Budget discipline.** Each verification search returns substantial context (~15-25K tokens). Over a Prompt Strategy with 5-6 prompts, unbounded per-prompt verification can consume 100-300K tokens at Setup — where Claude needs most headroom for strategy drafting. Trigger verification only when the recommendation touches fast-moving state: naming a specific vendor, naming a specific platform flag (Adaptive Thinking, Deep Research, effort levels), naming a specific best-practice convention. Generic recommendations (default Claude settings, attach map entries, standard specialist prompts) don't trigger verification. For projects where most prompts have platform-specific recommendations, a single broad orientation search at Setup can amortise cost across the Strategy rather than running per-prompt searches.

**Pairs with Output Quality Check:** SP-10 is pre-flight (verify state before generating recommendations). The Output Quality Check is post-flight (verify output quality after the prompt runs). Together they close the loop — informed recommendations, then quality-checked results.

---

## VERSION MANAGEMENT

*Non-negotiable. Every Starter change bumps a version and produces a new filename. No overwrites, ever.*

### Scope of these rules

**Everything in this section applies to the Starter file only.** Canonical / non-canonical, major = whole number, minor = decimal, `[MATERIAL]` tag, download tracking — all Starter-scoped. The Starter's versioning is a **plan-progress signal**: a glance at the version number tells you where the project is along its planned path.

**PRISM itself uses standard semantic versioning (MAJOR.MINOR.PATCH — e.g., v1.7.3).** The two schemes look similar at a glance but mean different things:

| Scheme | Used by | Format | Meaning |
|--------|---------|--------|---------|
| Plan-progress | Starter | `vN` / `vN.M` | Major = canonical step, Minor = anything else |
| Semver | PRISM (this file) | `vX.Y.Z` | MAJOR = breaking/structural, MINOR = additive, PATCH = corrections |

For PRISM semver specifically:
- **MAJOR** bump when framework behaviour changes in a way that existing Starters can't be read or run under without modification (e.g., a Scope Flag becomes required, a Standing Principle is retired, a Phase is restructured).
- **MINOR** bump when machinery is added in a backward-compatible way (new Monitor, new SP, new optional feature, new prompt template).
- **PATCH** bump for corrections, clarifications, naming hygiene, and bugfixes that don't change behaviour.

**Why this is stated up front:** the Starter's canonical/non-canonical logic is load-bearing for projects, but a reader absorbing it fresh can easily mis-apply it to PRISM's own version history (which looks like the same scheme but isn't). The rules below are Starter-scoped — PRISM's own Version History table at the end of this file follows semver.

### Why this matters

The user often works from a phone. Downloaded files live with the exact filename they were given. If two changes produce the same filename, the phone silently holds a stale copy. The only defense is: **every change = new filename = version bump**.

### The canonical distinction

The rule is simple once the canonical distinction is clear:

**Major version** (whole number: v1, v2, v3...) = a **canonical step** has advanced the project along its planned main path.
**Minor version** (decimal: v3.1, v3.2, v3.3...) = anything else, even if new findings were added.

Canonical steps are the planned forward motion laid out in the Prompt Strategy. Everything else — reruns, fixes, bookkeeping, process tweaks, Monitor-triggered updates — is non-canonical and drives a minor bump regardless of what content it adds.

### The [MATERIAL] tag

Minor versions that carry substantive findings (not just housekeeping) are tagged `[MATERIAL]` in the changelog. This lets a cold reader distinguish "minor with teeth" from "minor housekeeping" without the version number changing its meaning.

```
v3.1 [MATERIAL] — P1 rerun: corrected market sizing from $6.5B to $3.8B...
v3.2 — Typo fix in P2 findings header
```

The version number stays plan-bound (progress signal). The changelog carries the content signal.

### What drives a Major bump

- A specialist prompt completing with Layer 1 integration (e.g., P3 converges → v3)
- An enrichment source integrated via Layer 1 (e.g., P3.1 Coverage integrated)
- A Layer 2 cold synthesis (often the definitive final bump)
- An Adaptation that changes the canonical plan (new prompt injected and promoted, run order changed, enrichment layer added, Scope Flag upgraded mid-flight)

### What drives a Minor bump

- A rerun that corrects prior findings (new findings, but not canonical forward motion — it's a fix). Tag `[MATERIAL]` in changelog.
- An injected side work that wasn't canonical in the original plan (until formally promoted via Adaptation)
- Monitor-triggered bookkeeping (logging an M6 flag, noting an M8 stale source, scheduling work in the Rerun Register)
- Process updates to the Starter (new Monitor, tightened rule, clarified prompt)
- Corrections without new canonical findings
- Formatting fixes
- Any edit that isn't canonical progress

**The litmus test:** Does this change represent the project moving forward along its planned path? → Major. Does it represent anything else — even if it adds content? → Minor (tag `[MATERIAL]` if substantive).

**Minor resets to 0 when the next major version is created.** v3.2 → v4 (not v3.2 → v4.0). Clean whole numbers are the canonical baseline.

### Download tracking rule

Every change — no matter how small — produces a new filename with an incremented version. Never overwrite. Always bump. The filename is the version record.

### Example sequence

```
Starter created                          → {project}_starter_v0.md
P1 converges (canonical)                 → {project}_starter_v1.md   (major)
Typo fix in P1 findings                  → {project}_starter_v1.1.md (minor)
P2 converges (canonical)                 → {project}_starter_v2.md   (major, minor resets)
M6 flags premise shift on P1             → {project}_starter_v2.1.md (minor — bookkeeping)
P1 prompt refreshed per M6               → {project}_starter_v2.2.md (minor)
M10: P1 rerun scheduled in Register      → {project}_starter_v2.3.md (minor — scheduling)
P3 converges (canonical)                 → {project}_starter_v3.md   (major)
P1 rerun executes, findings updated      → {project}_starter_v3.1.md (minor [MATERIAL])
P3.1 Coverage enrichment integrated      → {project}_starter_v4.md   (major — canonical)
P3.2 Fact Check enrichment integrated    → {project}_starter_v5.md   (major — canonical)
P4 converges (canonical)                 → {project}_starter_v6.md   (major)
Adaptation: P4.1 enrichment promoted  → {project}_starter_v7.md   (major — canonical plan changed)
P5 converges (canonical)                 → {project}_starter_v8.md   (major)
Layer 2 cold synthesis (canonical)       → {project}_starter_v9.md   (major — final synthesis)
```

### Header discipline

Every Starter's header version must match its latest Changelog entry. Monitor M2 catches drift between them. If header says v5 but the latest Changelog entry is v4, stop and resolve before any further work.

---

## GATE-0: SESSION START VERIFICATION

**Runs at the start of every PRISM session, before any other work. No exceptions.**

Claude runs these checks in order and produces visible output:

### Checks

1. **Task identification.** What does the user want to do in this session? If unclear or ambiguous, stop and ask.
2. **File presence.** Are all expected inputs attached?
   - Starter file present? (always expected unless this is project setup)
   - Required attachments for this prompt present? (check the attach map in the Prompt Strategy)
   - Predecessor outputs present? (if this task depends on prior prompt outputs that aren't in the Starter yet — e.g., LLM outputs for convergence)
   - Filenames match the `[LLM] — [Prompt ID] — [Description]` convention (SP-8) for enrichment outputs?
3. **Version coherence.** Does the Starter's header version match its latest Changelog entry? Does the header's PRISM version match what's expected for this project (i.e., the framework version this project was initialised under, unless an explicit PRISM upgrade has been logged)?
4. **Sequence validity.** Does the requested task make sense given the current state? (e.g., "run P5" when P4 is still ⬜ NOT STARTED → stop)
5. **Prompt freshness.** If the task is to run a specific prompt, are there any open M6 flags on that prompt? If yes, the prompt may need refreshing before execution — flag and ask.
6. **Rerun Register scan.** Any scheduled reruns in the Register? Does the current session align with one of them? Overdue reruns get flagged with age (see output format).
7. **Ambiguity scan.** Does the task reference anything with more than one valid interpretation? (e.g., "run Prompt 4" when two versions of Prompt 4 exist → stop)
8. **Conversation history cross-reference.** Search recent conversations in this project to verify: is the attached Starter the latest version delivered? Was any work produced in a prior session that hasn't been incorporated? One targeted conversation search, not a deep dive — goal is to catch "grabbed wrong file from Downloads," which is common enough and costly enough to be worth 30 seconds per session. Time-boxed.
9. **Context pressure.** Estimate the combined token load of attached files + accumulated conversation against the effective context budget declared in the Runtime Profile. Report as a Context Pressure Band (🟢 Comfortable / 🟡 Getting warm / 🟠 Curate now / 🔴 Migrate) with per-dimension breakdown and percentage-of-effective-context. No action needed unless 🟠 or 🔴 — in which case M5 (if attachments-heavy) or M12 (if conversation-heavy, or combined 🔴) fires with its own action.
10. **Prompt content readiness.** For each canonical step in the Status Tracker, does the Starter's Prompts section contain the atomic prompt text? Missing prompt text means the prompt hasn't been written yet — this will block session startup for that prompt. Flag any missing.
11. **Execution notes coverage.** If this session involves running or preparing to run a canonical prompt (end-of-Setup handoff, "What's next?" session pointing to a prompt run, or an Adaptation that produces a new prompt), verify the Execution notes for that prompt cover the four required topics (thinking/reasoning depth, web search, Deep Research mode, vendor). If any topic is missing, surface it in the GATE-0 output — either the notes need updating via Adaptation, or proceed with the default for the missing topic and note in the session. Not a blocker. For convergence, bookkeeping, or other session types that don't involve imminent prompt execution, this check is n/a.

### Output format

Always print one of these at the start of the session:

**Pass:**
```
✅ GATE-0 passed
- Task: [what I understand you want to do]
- Files: [list of attached files with versions; SP-8 naming validated for enrichment files]
- History check: [matches last session / discrepancy noted]
- State: [current project state — e.g., "Starter v6, P1-P4 complete, P5 next"]
- PRISM version: v[X.Y.Z] (matches project header)
- Prompt freshness: [any M6 flags on the target prompt, or "clean"]
- Rerun Register: [scheduled items relevant to this session, or "none pending"]
- Overdue reruns: [none / list with age — e.g., "RR2 overdue by 3 days"]
- Prompt content: [all canonical prompts have text / missing: P#, P#]
- Execution notes: [covers all 4 topics / missing: topic-X — default assumed / n/a — not a prompt-handoff session]
- Context: [🟢 Comfortable / 🟡 Getting warm / 🟠 Curate now / 🔴 Migrate] (~[N]K attachments + ~[M]K conversation, ~[P]% of effective context). [Action note if any.]
- Proceeding.
```

**Fail:**
```
⚠️ GATE-0: discrepancy found
- [list of specific discrepancies]
- Cannot proceed until resolved.
- Please: [specific ask — upload file, clarify task, etc.]
```

**Overdue reruns rule:** overdue reruns warn but don't block, unless the current session IS the scheduled session (in which case they enter the task list and the status moves to 🔄 in progress).

**No heuristic guessing.** If something is missing or ambiguous, stop and ask. Do not assume. Do not reconstruct from memory. Do not "proceed with best interpretation."

### The "pressed send too fast" case

GATE-0 is designed specifically to catch the case where the user presses send before attaching everything or before fully specifying the task. The default assumption is: *they're moving fast, they might have missed something*. A missing file is almost never a deliberate choice — it's almost always an oversight. Flag it and ask.

---

## GATE-1: BETWEEN-PROMPTS SCAN

*Runs after a canonical step completes and Layer 1 integration is done, before accepting the next task. Two minutes, not a deep review. Goal: catch gross errors early. Detailed reconciliation is Layer 2's job.*

### Checks

1. **Layer scope respected?** The new findings section should not have rewritten interpretation of other sections or touched the executive summary. Monitor M9 catches this structurally; GATE-1 confirms it explicitly.
2. **Assumption Register populated?** The prompt should have added entries for every quantitative claim or external benchmark. If the prompt produced numbers but the register is empty, flag it as a quality issue.
3. **Discrepancy Check performed?** The prompt's findings should either confirm prior findings or explicitly state divergence in a dedicated "Discrepancy Check" subsection at the end of its findings. Silence means the check was skipped — flag it.
4. **[UNVERIFIED] tagging applied?** Any LLM-sourced claim without primary verification should be tagged inline. A prompt with zero [UNVERIFIED] tags on LLM-heavy work is suspicious.
5. **Monitor triggers logged?** Did any M6 (premise shift), M7 (assumption conflict), or M10 (rerun required) fire? If yes, Action Log and/or Rerun Register entries should exist. Check.
6. **Deferrable issues captured?** Per SP-2, minor issues should be flagged with a target touchpoint within the remaining canonical sequence. If no valid target exists, M10 should have fired. Check.
7. **Status Tracker updated?** The completed step should be marked ✅ with the output filename and Delivery Filename recorded.
8. **Version bump correct?** Major bump (canonical progress), new filename, delivered via `present_files` per SP-7.

### Backtrace audit (final GATE-1 step)

Before declaring GATE-1 passed, Claude re-scans the session work:

| Check | Question |
|-------|----------|
| SP-1 | Did I reconstruct anything from memory instead of asking for a file? |
| SP-3 | Did I converge in this session, or leave it for the user? |
| SP-6 | Did I use create_file when I should have (>~8 edits)? |
| SP-7 | Am I about to deliver via present_files? |
| Version | Is the bump correct (major for canonical, minor otherwise)? |
| Header sync | Does the Starter header version match the latest Changelog entry? |
| Changelog | Is the entry narrative with substance, not a one-liner? |
| [MATERIAL] | If minor with findings, did I tag it? |
| M6/M7 | Should M6 or M7 have fired? Quick scan: do my top 3 findings conflict with any Assumption Register entry or shift any prior prompt's premise? |
| OQC | Was the Output Quality Check performed? Any signals fire? If yes, logged in Changelog with action taken? |

If any item fails → fix before delivery. Log the catch in the GATE-1 output. The Header sync check catches mid-session drift (Claude bumps the header, forgets the Changelog) before delivery — not at next session's GATE-0 after the fact.

### Output format

**Pass:**
```
✅ GATE-1: [Prompt ID] integration clean
- Layer scope: respected
- Assumption Register: [N] new entries
- Discrepancy Check: [summary — confirmations / divergences flagged]
- [UNVERIFIED] tags: [count, if relevant]
- Monitor triggers: [list or "none"]
- Deferred items: [list with targets, or "none"]
- Rerun Register: [new entries, or "no changes"]
- Status Tracker: updated
- Version: v[X] → v[Y] (major) — header and Changelog in sync
- Ready for next task.
```

**Fail:**
```
⚠️ GATE-1: issues found in [Prompt ID] integration
- [specific issues]
- Please resolve before proceeding to next prompt.
```

### Session closeout role

If the user isn't running the next prompt immediately, GATE-1 output doubles as the session closeout summary. They can glance at it in the next session (or on their phone later) and pick up exactly where they left off. The pass block becomes the "state of the project" snapshot.

### Non-prompt session closeout

For sessions that don't run a canonical prompt (Adaptations, bookkeeping, process updates, extended discussion), GATE-1 doesn't formally apply. Instead, run a lightweight closeout before ending:

```
Session closeout:
- SP-7: file delivered? [yes/no/no file produced]
- Version: correct? [bump type and number]
- Changelog: narrative entry added? [yes/n/a]
- State: [where the project stands now]
- Next: [what the user should do next]
```

---

## SETUP: SPAWNING A NEW STARTER

*When starting a new PRISM project. Skip if the project already exists.*

### Inputs needed from the user

Before any work begins, Claude confirms:
- Project name (short, used for filenames)
- Subject (what's being researched/audited)
- Stakeholder (who the final output is for — affects tone)
- Scope (which dimensions, which prompts)
- Constraints (timeline, access, sensitivities)
- Deliverables (final report? teaching material? reusable methodology?)
- Domain glossary (3-6 acronyms or terms a cold reader of the README would need)
- Runtime Profile (defaults to Claude Skill / 1M context / full file ops / history search / present_files — adjust if running on a different host, smaller context plan, or different delivery mechanism)

If anything is unclear, Claude asks before building.

### Scope Flags (default: full scope)

The Prompt Strategy declares what machinery is in-scope for this project. Flags default to full coverage — PRISM is designed for breadth-and-depth work, and full scope is the right starting point for any new or uncertain project. Downgrade only when the user explicitly opts out.

| Flag | Options | Default |
|------|---------|---------|
| Multi-LLM enrichment | full / minimal / none | full |
| Cross-prompt dependencies | yes / no | yes |
| External stakeholder deliverable | yes / no | yes |
| Layer 2 cold synthesis | yes / no | yes |
| Expected session count | <3 / 3-10 / 10+ | 3-10 |

**Multi-LLM enrichment options:**
- **full** — Discovery at Setup + Coverage/FC/DR/RT/UV as applicable per prompt
- **minimal** — Discovery at Setup + Coverage and Fact Check only (the cheap, high-value pair)
- **none** — specialist prompts only, no enrichment

**Flag-to-machinery mapping:**
- Multi-LLM enrichment = none → Phase 2 machinery dormant, no enrichment naming convention needed, no Discovery run, no Enrichment Scoping at Setup
- Cross-prompt dependencies = no → M6 dormant (no prior-prompt premises to shift). M7 stays active — Assumption Register conflicts can still arise between independent prompts citing the same benchmark with different values.
- External stakeholder = no → Delivery Folder / Appendices / README optional
- Layer 2 = no → M11/GATE-2 dormant, Layer-2-specific fresh-session migration protocol dormant. M12 stays active — conversation pressure degrades synthesis quality in any long session, not just pre-Layer-2.
- Session count < 3 → M10's deferral-target check is stricter: a valid SP-2 deferral target must exist in the current session or the immediately next one; otherwise the issue is scheduled explicitly in the Rerun Register or fixed in-session. (Short projects rarely have later touchpoints to absorb deferred work, so the deferral window shrinks accordingly.)

Setup prints the flag block with defaults selected and uses `ask_user_input` (where available) to gather the user's choices. The primary path is a single "Keep all defaults" tap for users who want the full framework without adjusting anything — one interaction for the most common case. Users adjusting flags see each flag as a tappable option with its default pre-selected. When `ask_user_input` isn't available, Claude falls back to a prose question per SP-9. A first-time user who doesn't know what to answer keeps defaults and gets the full framework. An experienced user can downgrade specific flags for simpler work.

A project's Scope Flags can be upgraded mid-flight via Adaptation (major bump). Downgrade is not supported once the machinery is active — dormant is fine, removing mid-project is not.

The approved Scope Flags are recorded in the Prompt Strategy section of the Starter so post-hoc readers can see what was active.

### Runtime Profile (declared at Setup)

PRISM's behavior has dependencies on the host environment — file operations, conversation history search, context window size, delivery mechanism. These have default values assumed by the framework (Claude Skill on claude.ai, ~1M-token context on Opus 4.7, `create_file` / `str_replace` / `present_files` available, conversation history search available), but explicit declaration at Setup enables graceful behavior on other hosts and lets percentage-based thresholds calibrate correctly.

| Field | Options | Default |
|-------|---------|---------|
| Host | Claude Skill / claude.ai chat / Claude Code / API / other | Claude Skill |
| Effective context budget | 200K / 500K / 1M / other (specify) | 1M |
| File ops available | yes / no | yes |
| Conversation history search | available / unavailable | available |
| Delivery mechanism | present_files / manual file link / export / other | present_files |

**Setup prints the Runtime Profile alongside Scope Flags.** Defaults are pre-selected; user taps "Keep defaults" or adjusts per SP-9. Most claude.ai / Claude Skill users keep defaults; API-driven workflows or smaller-context plans declare accordingly.

**What the profile drives:**

- **Effective context budget** → percentage-based M5/M12 thresholds calibrate to the declared budget (see Monitors section). A 200K-context project's ~30%-of-context threshold is ~60K, not ~300K.
- **File ops available = no** → SP-6 and SP-7 adapt: delivery via path/link rather than `present_files`; text-based output instead of file creation.
- **Conversation history search = unavailable** → GATE-0's history cross-reference check (v1.7 addition) falls back to asking the user: "Is the attached Starter the latest version delivered?"
- **Delivery mechanism ≠ present_files** → SP-7 adapts; outputs are surfaced via the declared mechanism.

**The profile is recorded in the Starter's Prompt Strategy section** (next to Scope Flags) so post-hoc readers can see what host the project ran under. A project can change Runtime Profile mid-flight via Adaptation if the user switches surfaces (rare but possible — e.g., escalating from mobile chat to desktop for a complex convergence session).

**Graceful degradation for unknown hosts:** if the user declares "other" without further specification, Claude asks clarifying questions about the four other fields and proceeds based on the answers. No field is allowed to be unknown at Setup — SP-9 applies.

### Discovery (Setup-phase enrichment)

*Active when Multi-LLM enrichment = full or minimal.*

Before the Prompt Strategy is finalised, Claude proposes a **Discovery** pass. Discovery runs once, across 3-4 LLMs in parallel, at the project level — not as a P#.x sub-prompt of any specialist.

**Purpose:** map the problem space. What dimensions should a rigorous audit/research project in this subject examine? What blind spots, regulatory considerations, ethical issues, technical risks, or stakeholder segments might a generalist framework miss? What would a senior practitioner in this domain look for that isn't yet in the proposed scope?

**Discovery prompt pattern:**
```
Given this subject [describe] and these stakeholder goals [describe], what
dimensions should a rigorous audit/research project examine? What blind
spots, regulatory considerations, ethical issues, technical risks, or
stakeholder segments might a generalist framework miss? What would a senior
practitioner in this domain look for?

Return: a list of dimensions, risks, and considerations with brief rationale
for each. Prioritise what a generic framework is likely to miss over what
any competent plan would already cover.
```

**Output:** a list of dimensions, risks, and considerations that the user reviews with Claude and folds into the Prompt Strategy before approval. Discovery findings can reshape the Prompt Strategy — add prompts, change scope boundaries, surface a required specialist lens that wasn't in the initial brief.

**Version impact:** if Discovery runs before v0, the Starter is created with a Discovery-informed Prompt Strategy (no bump needed — Discovery is pre-v0). If Discovery runs mid-project as an Adaptation, it's a major bump because it changes the canonical plan.

### The Prompt Strategy is the setup deliverable

After Scope Flags are agreed and Discovery (if scoped) has run, Claude drafts **the Prompt Strategy** based on the user's brief, the Discovery output, and the approved flags — then proposes it for approval. The Prompt Strategy is the contract between the user and Claude for how the project will run. It contains:

- **Scope Flags** — the five flags and their approved settings for this project
- **Scope rationale** — why these prompts, why this scope, what the audit/research is trying to answer (informed by Discovery if run)
- **Canonical sequence** — the planned prompts in order, with brief descriptions (defines what's canonical for this project)
- **Dependencies** — which prompt needs which predecessor
- **Run order** — optimal sequence with parallelization notes (what can run simultaneously)
- **Expected outputs** — per prompt (findings format, deliverables)
- **Attach map + execution notes** — per prompt, which files must be attached beyond the Starter (e.g., "P2 requires P1 walkthrough docx") and a short `Execution notes` block capturing how to run the prompt (thinking depth, web search, Deep Research mode, vendor recommendations if multi-vendor). Claude writes the execution notes at Setup per SP-10, framed as best-effort based on current understanding of vendor capabilities. The user reads and applies when running the prompt. Checked by GATE-0.
- **Enrichment Scoping** — per prompt, which enrichments were proposed and which were approved or declined (see next subsection)
- **Collection method** — if enrichment is scoped, how multi-LLM outputs get gathered
- **Strategy Revision Log** — changes over the course of the project, via Adaptations (empty at start)

The user reviews and approves (or adjusts) before Claude writes the individual atomic prompts into the Starter. Without an approved Prompt Strategy, no work begins.

### Execution notes (best-effort runtime guidance)

For each prompt in the Strategy, Claude writes a short `Execution notes` block alongside the attach list — prose guidance on how to run the prompt effectively. This is best-effort based on Claude's current understanding of vendor capabilities and prompt-engineering practice, verified per SP-10 at Setup.

The execution notes must cover all four topics, per prompt:
- **Thinking / reasoning depth** — what mode to use and why. Interface-specific where relevant (Claude.ai UI toggle state, Claude Code /effort level, API thinking config, equivalent on other vendors).
- **Web Search** — on/off and why.
- **Deep Research mode** — on/off and why. See "Routing to Deep Research vs. regular" below.
- **Vendor recommendations** — if the prompt genuinely benefits from a specific vendor capability (strong citation fidelity, multi-source synthesis, adversarial reasoning), Claude names vendor options in preferred→fallback order for single-LLM prompts, or as an independent set for multi-LLM prompts (Coverage, Fact Check, Discovery). When no vendor-specific recommendation applies, default is Claude.

Default coverage is fine for prompts where the defaults apply (e.g., "Claude, Adaptive Thinking on, no web search, no Deep Research"), but all four topics must be addressed explicitly even when each is the default. GATE-0 verifies coverage at prompt-run session start (see GATE-0 check #11).

**Two output shapes** — single-LLM prompts rank vendors; multi-LLM prompts specify a set:

*Single-LLM shape (specialist, Deep Research, Red Team, User Voice):*
```
Thinking / reasoning depth: High.
  Claude.ai UI (Opus 4.7): Toggle "Adaptive thinking" ON for this prompt.
    ⚠️ Adaptive may occasionally skip thinking on prompts it judges
    simple; if output feels shallow for a Red Team or Layer 2 pass,
    flip OFF and re-run as a cross-check.
  Claude Code: /effort max
  API: thinking: {type: "adaptive"}, effort: "max"
  Other vendors: enable deepest reasoning mode available.

Web Search: On (for market-state claims; off for pure analysis).
Deep Research: On (needs multi-source synthesis).

Vendor options (preferred → fallback):
1. Claude Opus 4.7 with max effort — strongest adversarial reasoning
2. GPT-5 Pro or equivalent with extended thinking equivalent
3. Gemini Pro with Deep Thinking
```

*Multi-LLM shape (Coverage, Fact Check, Discovery — same prompt run on 2-4 different vendors):*
```
Thinking / reasoning depth: High across all runs.
Web Search: On.
Deep Research: [on/off as applies to role].

Run on 2-3 vendors with independent indexes. Suggested set (pick any two or three):
- Claude Opus 4.7 with web search — strong reasoning, broad index
- Perplexity Pro — citation-first, real-time web
- Gemini Pro — independent index, strong on long-tail sources

Convergence signal: if sources return the same verdict on a claim, confidence is high.
Divergence: Layer 2 resolves.
```

**Routing to Deep Research vs. regular:**

Not every prompt benefits from Deep Research mode. It's a web-search-then-synthesize engine that earns its keep when external sourcing genuinely adds value — current platform features, recent literature, evolving market state, multi-source convergence. When the task is synthesis or structuring of stable, well-trained domain knowledge (taxonomies, prerequisite chains, classical classifications), routing through Deep Research actively degrades output: the model spiders tangential pages, loses coherence, and produces worse results than direct generation. "Like asking someone to Google the alphabet."

Decision guide for setting the Deep Research field in execution notes:

- **Regular chat wins when** the subject is stable, well-trained knowledge; the task is synthesis or structuring rather than sourcing; Deep Research would primarily add citations rather than new facts.
- **Deep Research wins when** the task genuinely requires external sourcing (current platform features, recent literature, evolving market data); the answer depends on things the model wasn't trained on; multi-source convergence is the point.
- **Regular-with-web-search wins in the middle** — when some external verification helps but full multi-source synthesis is overkill. Fact-checking specific claims, confirming a date, pulling a recent quote.

If a proposed prompt has mixed needs — stable-knowledge synthesis for one sub-task, external sourcing for another — the right move is usually splitting the prompt and routing each sub-task to the right mode, not applying one mode to the whole. Claude evaluates each prompt in the Strategy for routing fit at Setup. See Learning #40.

**Why not framework-enforced vendor matching:** vendor capabilities drift on a 3-6 month cycle; hardcoding specific recommendations in the framework would age badly. The execution notes are prose output from Claude at Setup, verified per SP-10. The framework describes the shape; the content is generated per project.

**Claude as default.** When no role-specific recommendation applies, Claude is the recommended vendor. Default for a Claude skill; removes ambiguity for prompts where vendor choice doesn't move the needle.

### Enrichment Scoping (mandatory when enrichment flag is full or minimal)

*Reminder: multi-LLM enrichment assumes you have access to at least two LLM vendors. If you only have Claude, the enrichment pattern degrades — "different vendor" passes become "same vendor with different settings" which is a weaker convergence signal. Consider `none` enrichment, or accept the degraded pattern deliberately.*

Claude reviews each proposed prompt against these triggers and proposes enrichment explicitly. The triggers Claude may propose depend on the enrichment flag:

**Under `full`:**
- Accuracy heavy in single-LLM claims? → Coverage or Fact Check recommended
- Depends on market/competitive data that changes frequently? → Deep Research recommended
- Conclusion needs to survive adversarial scrutiny? → Red Team recommended
- Touches user behavior, sentiment, or lived experience? → User Voice recommended

**Under `minimal`:**
- Accuracy heavy in single-LLM claims? → Coverage or Fact Check recommended

Deep Research, Red Team, and User Voice are not proposed under `minimal`. If one becomes necessary mid-project, the user requests an Adaptation that upgrades the enrichment flag to `full` (major bump per VERSION MANAGEMENT → Scope Flag upgrades). Minimal keeps enrichment cheap and high-signal (Discovery at Setup + Coverage + FC); projects that need adversarial stress or user-research go full.

The user approves or declines each proposed enrichment. **Declining is valid; omission is not.** Per SP-9, Claude uses `ask_user_input` (where available) to present each proposed enrichment as a tappable choice (approve / decline / defer to later) rather than asking for a prose response per prompt. Falls back to prose ask where the tool isn't available.

**Full-decline flag:** If the Multi-LLM enrichment Scope Flag is set to `full` or `minimal` but every proposed enrichment on every prompt is declined, Claude flags the inconsistency before finalising the Prompt Strategy: *"Enrichment flag is set to [full/minimal] but no enrichments were approved. Options: (a) update the flag to `none` to match the scope in force, or (b) keep the flag and proceed — this is recorded as a deliberate choice. Which?"* Stop and ask — do not proceed on a heuristic guess. Per PRISM's general stance, flagging beats assuming; unwanted silent content (or in this case, a silent scope-flag mismatch) is exactly what flagging prevents.

The Prompt Strategy records which enrichments were proposed and which were declined, so post-hoc readers can see the decision.

This converts enrichment from "opt-in because someone remembered" to "opt-out after considering each prompt." Closes the failure mode observed in a recent comparison of a PRISM project against its pre-PRISM equivalent: enrichment framed as optional → enrichment not run → significant structural downgrade. See Learning #30.

### Setup session context management

Setup is a reasoning-heavy session. Scope Flags + Runtime Profile declarations, Discovery (if scoped — 3-4 LLM outputs to synthesize), Prompt Strategy drafting, Enrichment Scoping approvals, SP-10 verifications for Execution notes, and writing all the atomic prompt texts can accumulate significant context especially on smaller-context hosts. The ~45K-token PRISM.md is already attached. Context budget can get tight.

**M12 applies to Setup sessions.** If accumulated context approaches the 🟠 Curate now band during Setup, save the partial Prompt Strategy to the Starter (whatever fields are complete), bump to v0.1 as a non-canonical checkpoint, hand off to a fresh session per the M12 migration protocol, and resume.

**Resumable Setup stages:**

1. Scope Flags + Runtime Profile + Discovery (if scoped) → save and can resume
2. Prompt Strategy outline (canonical sequence, dependencies, run order) → save and can resume
3. Execution notes with SP-10 verifications → save and can resume (verifications done to date stay valid)
4. Atomic prompt texts written into the Starter → save and can resume
5. Enrichment Scoping approvals → requires user input anyway; a natural session boundary

GATE-0 in the fresh session identifies the resumable stage from the Starter's current state (v0.1 vs. v0.2 vs. etc., and which sections are populated vs. empty) and continues from there. Setup ends at v0 when all stages complete and the user approves the final Prompt Strategy.

**This is a fail-safe, not a default.** Most projects' Setup fits in one session. The migration pattern activates only when context-heavy operations (large Discovery, many SP-10 verifications, complex Prompt Strategy) push against the band.

### What Claude produces

**1. The Starter file** — placed in `/mnt/user-data/outputs/{project}_starter_v0.md`, containing:

1. **Header** — project name, PRISM version, Starter version, date, subject, stakeholder
2. **Prompt Strategy** — the approved articulated plan (with Scope Flags, Runtime Profile, and Enrichment Scoping)
3. **Status Tracker** — empty rows tracking progress against the canonical sequence, including Delivery Filename column
4. **Rerun Register** — empty, populated by M10 triggers
5. **Assumption Register** — empty, ready for entries
6. **Findings** — one empty section per canonical step
7. **Enrichment Findings** — empty section, used only if enrichment is scoped
8. **Sources** — empty, grows with work
9. **Final Synthesis** — empty placeholder, populated at Layer 2
10. **Changelog** — one entry (narrative form): "v0 — Starter created, Prompt Strategy approved. [Scope Flags summary. Runtime Profile summary. Discovery summary if run. Enrichment Scoping summary.]"
11. **Action Log** — empty, populated by Monitor triggers and Adaptations
12. **Prompts** — one section per canonical step, with the atomic prompt text (tailored to this project) ready to copy-paste

**2. The README** (if External stakeholder deliverable = yes) — placed in the Delivery Folder root (see PROJECT FOLDER STRUCTURE). Boilerplate template populated from the Prompt Strategy: folder contents, PRISM methodology description, audit lenses with file mappings, and domain glossary from the user's input.

### Scope decision

Claude proposes a scope based on the user's inputs and (if run) Discovery outputs, but does not decide unilaterally. Typical dimensions for a product audit: Walkthrough, UX, Content, Competitive, Technical, Strategy. For a competitive research project: Market Sizing, Pricing & Packaging, Go-to-Market, Competitive Landscape, Regulatory, Team & Org. Note that Red Team, Fact Check, Coverage, Deep Research, and User Voice are **enrichment roles** (Phase 2), not primary specialist dimensions — they enrich findings from a specialist prompt rather than standing alone as the prompt's core lens. Claude picks specialist dimensions from the domain and proposes a run order within the Prompt Strategy, then applies enrichment roles per prompt via Enrichment Scoping. The user approves or adjusts before the file is finalised.

---

## PROMPT DESIGN PRINCIPLES

Every specialist prompt must satisfy these rules. Claude checks against these when writing or reviewing a prompt.

1. **Atomic** — runs in a fresh session with no memory. All context carried in the prompt body.
2. **Self-contained** — no "see the master file" for critical context. Paste relevant findings inline if needed.
3. **Specialist lens, not identity** — opens by framing the analysis through a domain-specific lens: "Analyze through the lens of competitive intelligence" — not "You are a competitive intelligence analyst." The lens shapes vocabulary, reasoning structure, and output format without activating instruction-following behaviors that degrade factual accuracy. Research (Wharton 2025, USC/Hu et al. 2026) shows expert persona prompts do not reliably improve factual accuracy on knowledge benchmarks and can degrade it. Personas help writing quality and tone — but those benefits come from *behavioral instructions* ("write with authority, lead with conclusions"), not identity claims. Describe the output, not the author.
4. **Single primary question** — one focused objective, not a laundry list.
5. **Specified output format** — structured output (sections, tables, register entries) so convergence is mechanical.
6. **Assumption Register instruction** — every quantitative claim or external benchmark must be logged.
7. **Discrepancy Check instruction** — before finalising, compare top claims against any prior findings. State divergences in a dedicated "Discrepancy Check" subsection at the end of findings. Format: `| Claim | This prompt's finding | Prior finding (source) | Verdict |`. Do not silently override or conform. **If this is the first prompt and no prior findings exist**, state this explicitly ("No prior findings exist — Discrepancy Check not applicable") rather than fabricating prior entries to fill the table.
8. **Convergence checklist** — Layer 1 integration steps spelled out at the end of the prompt.
9. **[UNVERIFIED] tagging** — any claim sourced from a single LLM without primary-source verification must be tagged inline.
10. **Null-result handling.** If a prompt investigates a dimension and finds nothing material, state it explicitly: `[NULL RESULT — investigated X, no material findings. Reasoning: ...]`. Silence in a findings section is ambiguous; explicit null result is informative. Especially valuable for Red Team and Fact Check prompts where "nothing found" is a confidence-increasing outcome.

### Prompt template

```
Analyze [PROJECT_NAME] through the lens of [SPECIALIST DOMAIN].

## Context
[Product/subject description in 2-4 sentences]
[Any critical prior findings this prompt depends on — pasted inline, not referenced]

## Your Task
[Single primary objective]

## Method
[Specific methods, frameworks, or research approaches to use]

## Output Format
[Exact structure expected — sections, tables, etc.]

## Writing Standard
Lead with conclusions. Defend every claim with evidence.
Use precise language — "increased 18%" not "substantially increased."
Tag uncertainty with [UNVERIFIED] inline; do not hedge with weasel words.
State what you don't know as clearly as what you do.
If a dimension you investigated yielded nothing material, say so explicitly
with [NULL RESULT — ...]. Silence is ambiguous.

## Assumption Register
For every quantitative claim, external benchmark, or sourced fact, log it:
| ID | Claim | Value | Source | Date | Confidence | Prompt | Conflicts |
Fill as you work. The Date column records the source's publication date
(YYYY-MM minimum, YYYY-MM-DD if known) so Monitor M8 can evaluate recency.
The Prompt column is populated at convergence with the prompt ID that
produced the row. These rows get merged into the master Assumption Register
at convergence.

## [UNVERIFIED] Tagging
Any claim you're making from a single LLM source without primary verification
→ tag it inline with [UNVERIFIED]. Do not hide uncertainty.

## Discrepancy Check
Before finalising: compare your top 3-5 quantitative claims and strategic
conclusions against prior findings in the Starter. Report in a dedicated
subsection:

| Claim | This prompt's finding | Prior finding (source) | Verdict |
|-------|----------------------|----------------------|---------|
| [claim] | [your number/conclusion] | [prior number/conclusion (P#)] | Confirms / Diverges — [brief reason] |

If your numbers or conclusions diverge, DEFEND your position. Do not silently
override. Do not silently conform. The divergence is the signal — Layer 2
convergence resolves it.

**If this is the first prompt and there are no prior findings to compare
against**, skip the table and state explicitly: *"No prior findings exist —
Discrepancy Check not applicable for this prompt."* Do not fabricate prior
entries to fill the format.

## Live watch for preemptive scope-down

While running this prompt, watch for the LLM declaring inability to complete the work before substantial work has been attempted — especially if the complaint is coupled with a "start a fresh session" recommendation rather than scope-clarification questions. This is a thinkless-output signal (see Output Quality Check signal #6 in the Convergence checklist below).

Tells:
- Budget-complaint appears in the first 1-3 turns of a session
- Complaint cites specific items already consumed (tool discovery, INDEX read) but doesn't attempt the actual work before declaring it won't fit
- Complaint proposes deferral rather than compression or prioritisation
- Complaint persists or re-surfaces even after the user confirms context is fine

If this pattern appears:
- Correct the assessment and re-issue if context is genuinely fine
- Restart cleanly with a new session if context is genuinely constrained
- Do not accept deferral as the default path

Distinction from legitimate wrap-up: genuine budget awareness comes late in a session after visible work, proposes compression or prioritisation, and responds to user correction. Preemptive scope-down comes early, proposes deferral, and may persist after correction.

## Convergence (Layer 1 — mandatory)
After producing findings, before updating the Starter:
0. **Monitor pre-scan:** Compare your top 3 findings against the Assumption
   Register — any conflicts? (M7) Check if your findings shift any premise
   stated in other prompts' context sections. (M6) Fire monitors if triggered.

0a. **Output Quality Check (pre-convergence):** Before integrating these findings, check six signals:

   1. **Reasoning visibly occurred.** On Claude.ai, the thinking indicator was visible. On API, the thinking block is present and non-trivial. On other vendors, equivalent reasoning markers are present. Absent reasoning trace on a complex specialist prompt is a red flag.
   2. **Sources cited or [UNVERIFIED] tags present** on LLM-heavy claims. Zero [UNVERIFIED] tags on LLM-heavy work is suspicious.
   3. **Output engages specific project context**, not template-with-nouns-substituted. Shallow output often reads as the generic structure for that kind of analysis with project-specific nouns swapped in.
   4. **[NULL RESULT] entries present** where investigations yielded nothing. For Red Team and Fact Check especially, total absence of null results despite the prompt instruction is suspicious.
   5. **Length and depth match prompt complexity.** A 200-word Red Team on a high-stakes market-sizing claim is too thin; a 50-word Fact Check per claim with no sourcing is too thin.
   6. **Preemptive scope-down did NOT occur during the run.** Cross-reference: was this handled live per the "Live watch" section above? If yes, note the intervention in the Changelog. If no (and the behaviour occurred but wasn't corrected), this is the strongest signal and warrants re-run.

   **Thresholds:**
   - **Signal #6 alone** → single-signal trigger. Correct & re-issue, or restart cleanly. Do not integrate deferral-path output.
   - **Two or more of signals #1-5** → re-run with deepest-reasoning mode available, cross-check results, integrate the better pass.
   - **One of #1-5 alone** → note in Changelog, flag for Layer 2 scrutiny, proceed.

   Log the OQC result in the Changelog entry: *"OQC: clean"* or *"OQC: signal #N fired, [action taken]"*.

Then update:
1. Paste findings into the corresponding section of the Starter
2. Merge your Assumption Register rows into the master register (populate the
   Prompt column with this prompt's ID)
3. Update the Status Tracker (mark ✅, record Delivery Filename if standalone
   artifact produced)
4. Add a narrative Changelog entry (major version bump — canonical step
   completing)
5. Save updated Starter to /mnt/user-data/outputs/ with new filename (per
   SP-6, use create_file if >~8 edits needed)
6. Call present_files (per SP-7)
Do NOT: rewrite interpretation of other sections, resolve conflicts with
other findings, rewrite the executive summary, or touch Layer 2 territory.
That's for cold synthesis later.
```

---

## PHASE 1: RUNNING SPECIALIST PROMPTS

Each canonical prompt runs in its own session. The user copies the prompt text from the Starter, opens a new Claude conversation, attaches the Starter (and any required files per the attach map), and pastes the prompt.

Between prompts, Claude runs Monitors:
- **M6** — does this finding invalidate any prompt's premise? If yes, flag prompt for refresh.
- **M7** — does this finding conflict with an existing Assumption Register entry? If yes, log for Layer 2.
- **M10** — does this finding reveal an issue that requires rerun or fix but has no natural deferral target? If yes, schedule in Rerun Register.

The user does a 2-minute scan between prompts to catch anything obviously wrong. Detailed reconciliation is Layer 2's job. GATE-1 formalises this scan.

---

## PHASE 2: ENRICHMENT

*Active when Multi-LLM enrichment flag is "full" or "minimal." Each enrichment was scoped per prompt at Setup via Enrichment Scoping; prompts for which every enrichment was declined will have no Phase 2 sub-prompts.*

### Enrichment roles (guidance catalog)

| Role | Phase | Purpose | LLMs | Value signal |
|------|-------|---------|------|-------------|
| **Discovery** | Setup | Map the problem space before the Prompt Strategy is finalised (project-level) | 3-4 (same prompt) | Divergence → dimensions the generic framework missed |
| **Coverage** | Prompt | Find what a specific prompt's narrower analysis missed within its domain | 3-4 (same prompt) | Divergence → blind spots in that prompt's scope |
| **Fact Check** | Prompt | Verify high-risk claims | 2 (same prompt) | Convergence → confidence |
| **Deep Research** | Prompt | Deepen what we know | 1-2 | Richer data |
| **Red Team** | Prompt | Break the thesis | 1 | Adversarial pressure |
| **User Voice** | Prompt | Mine real user perspectives | 1 | Reality check |

Each prompt-phase enrichment sub-prompt is canonical once scoped into the Prompt Strategy, numbered as a decimal under its parent (P3.1, P3.2, etc.). Discovery is not numbered as P#.x — it runs at project level, before the Prompt Strategy is finalised.

### Coverage prompt pattern

```
Given this prompt's findings on [domain], what did it miss? Named entities it
didn't include, angles it didn't examine, counter-evidence it didn't address.

For each gap you identify, state:
- What's missing (specific entity, angle, or piece of evidence)
- Why it's material to the prompt's stated objective
- What the missing content suggests about the finding's robustness
```

Output feeds back into the parent prompt's findings section via Layer 1.

### Run order

Coverage first (unknowns feed Deep Research). Fact Check independent. Deep Research after Coverage. Red Team after the core thesis has emerged. User Voice any time. Discovery runs at Setup, not in Phase 2.

### Collection method

The user appends each LLM output to one running document with separators:
```
=== [ROLE]-[N] [LLM NAME] ===
```

Before uploading for Layer 1 integration, the user checks: does the separator count match the number of LLM runs? Catches truncated pastes.

### Red Team prompt pattern

```
Your associate has produced the attached analysis. Your job is to BREAK it before [the stakeholder audience] sees it. Find every weakness, unstated assumption, and analytical gap.

For each [major claim / use case / recommendation]:
- Find a counter-argument
- Identify what would have to be true for the claim to fail
- Find the single assumption that, if false, collapses the whole case

Be adversarial. The [audience] will be. If the analysis survives your scrutiny, it's ready. If it doesn't, we need to know now.

If you genuinely find no material weakness on a claim after rigorous attack,
say so with [NULL RESULT — attacked X along Y axes, no material weakness
found]. A clean red team result is an output, not an absence.
```

### Fact Check prompt pattern

```
Verify or refute each claim below with cited sources. For each: state Confirmed / Partially Confirmed / Refuted / Unable to Verify. Source URL required for every verdict.

1. [Specific claim with numbers, dates, names]
2. [Another specific claim]
...

If you cannot find any contradicting evidence after genuine search, state
[NULL RESULT — searched X, no contradicting evidence found] rather than
leaving the claim unmarked.
```

Run the same FC prompt on 2 LLMs. Value is in convergence — if both agree, confidence is high. If they disagree, Layer 2 resolves.

---

## PHASE 3: LAYER 1 CONVERGENCE (Incremental Integration)

*Runs after each new source arrives. Stays strictly additive.*

### Scope

Layer 1 ONLY:
- Add new findings to their Starter sections
- Merge Assumption Register rows
- Add new sources
- Update status tracker
- Correct **uncontested** factual errors — errors where no source disagrees (if sources conflict, that's Layer 2 territory, not a Layer 1 correction)
- Log action items for Layer 2 (flagged conflicts, divergences, premise shifts)
- Fire Monitors (especially M6, M7, M10)

Layer 1 does NOT:
- Rewrite interpretations
- Resolve conflicts between sources
- Update the executive summary
- Change strategic recommendations
- Touch the final synthesis

### Fact Check reconciliation

Fact Check enrichment results produce specific, mechanical updates to prior claims. These are *corrective* (safe for Layer 1), not *interpretive* (which would be Layer 2).

When integrating a Fact Check output (P#.x), process each verdict:

- **Confirmed** — strip the `[UNVERIFIED]` tag from the claim inline in findings. Upgrade the Assumption Register confidence from 🟡 single-source to 🟢 multi-source verified. Add the FC source to the Register's Source column (append, don't replace).
- **Partially confirmed** — keep the `[UNVERIFIED]` tag with a qualifier (e.g., `[UNVERIFIED — partially confirmed by FC, caveat: ...]`). Confidence stays 🟡. Note the caveat in the Register.
- **Refuted** — strike through the claim in findings (`~~claim~~`), add a note with the correcting finding, and trigger **M7** (assumption conflict). The struck-through version stays in place for audit trail; the correcting claim is added as a new Register entry. Layer 2 resolves any downstream interpretations that depended on the refuted claim.
- **Unable to verify** — the `[UNVERIFIED]` tag remains. Note the FC attempt in the Register's Source column (e.g., "P3.2 attempted, could not verify"). Confidence stays 🟡 or moves to 🔴 if FC found partial contradicting signal. This is a `[NULL RESULT]` on the FC side — log it explicitly.

These mutations are safe for Layer 1 because they don't change *interpretation* — they update the confidence tier and tag status based on new verification evidence. The underlying claim's meaning is not re-framed; its epistemic status is sharpened.

### Output

**Major version bump** if this is a canonical step completing (e.g., P3 converges, P3.1 enrichment source integrated). **Minor version bump** if this is a rerun, fix, or non-canonical work that happens to add findings (tag `[MATERIAL]` in changelog). See VERSION MANAGEMENT for the full rules.

Narrative changelog entry describing what was integrated. Action Log entries for any Monitor triggers. Rerun Register updated if M10 fired.

### Monitor M9 check

After Layer 1 work, Claude verifies: did I stay in Layer 1 territory? If interpretation sneaked in, back out and flag for Layer 2.

### SP-6 check

If Layer 1 integration requires >~8 sequential edits (common for enrichment convergence work), use `create_file` to rebuild the new version rather than accumulating `str_replace` edits.

---

## GATE-2: LAYER 2 READINESS

*Formal readiness check before cold synthesis. Triggered by M11 (all canonical steps complete, Rerun Register clear). Can also be invoked manually by the user.*

GATE-2 has two parts: the **hard Gate** on verifiable conditions, and the **Quality Report** that flags informational issues for Layer 2 to acknowledge. The hard Gate is what blocks Layer 2. The Quality Report is not a gate — it feeds Layer 2's work.

### Hard Gate checks

1. **Status Tracker complete?** All canonical steps show ✅.
2. **Rerun Register clear?** All entries ✅ complete or 🚫 cancelled. Any open entries must be explicitly deferred or resolved before proceeding.
3. **Open M6 flags assessed?** For each open M6 (premise shift on a prompt whose findings are already converged):
   - **Severity: LOW** — the shifted premise was peripheral to the prompt's core findings. Findings stand. Log for Layer 2 awareness.
   - **Severity: HIGH** — the shifted premise directly undermines a key finding or recommendation. Findings may need revision before Layer 2 can trust them. → Recommend M10 (rerun with corrected premise) before proceeding. HIGH flags block the hard Gate.
4. **Open M7 conflicts catalogued?** List all unresolved assumption conflicts. These are Layer 2's job to resolve — not a blocker, but the list must be visible.
5. **Starter version confirmed?** Current version number, date, and a check that no work has been done outside the Starter (e.g., in a side conversation) that hasn't been integrated. Any external edits flagged per SP-8.
6. **Cool-down (fresh session check).**
   - Confirm Layer 2 will run in a new conversation with only the Starter attached.
   - If continuing in the same conversation: ⚠️ anchoring risk — synthesis may echo current-session reasoning rather than examine it.

   No hours. No sleep advice. Pure technical check. The researcher-facing side of cool-down (recency bias, anchoring on prior drafts) is covered in the Layer 2 introduction — see "Notes for the researcher at Layer 2" in Phase 4.

### Quality Report (informational — feeds Layer 2)

Runs as part of GATE-2 but does not block. Layer 2 acknowledges each flagged item in its synthesis rather than requiring resolution before Layer 2 starts.

- **Findings coverage:** does every canonical step have a populated findings section? [all ✅ / gaps in: P#]
- **Assumption Register:** entries present for every prompt that produced quantitative claims? [complete / sparse in: P#]
- **Discrepancy Checks:** does every findings section include a Discrepancy Check subsection? [all present / missing in: P#]
- **[UNVERIFIED] density:** any prompt with zero [UNVERIFIED] tags on LLM-heavy work? [normal / suspicious in: P#]

**Disposition:**
- Layer 2 acknowledges each flagged item in its synthesis.
- If any gap is severe enough to actually block synthesis (e.g., an entire findings section empty), back out to M10 before proceeding — but that's a judgment call the synthesiser makes, not a hard Gate.

This separates "readiness to attempt Layer 2" (the real gate) from "quality of the inputs" (the sanity check).

### Output format

**Pass:**
```
✅ GATE-2 passed — ready for Layer 2
- Status Tracker: all canonical steps ✅
- Rerun Register: clear
- Open M6 flags: [none / list with severity — all LOW]
- Open M7 conflicts: [count — Layer 2 will resolve]
- Starter: v[N], [date]
- Cool-down: fresh session confirmed (or: ⚠️ same-session — anchoring risk)
- Attach instructions: fresh conversation, Starter only

Quality Report (informational — feeds Layer 2):
- Findings coverage: [all ✅ / gaps in: P#]
- Assumption Register: [complete / sparse in: P#]
- Discrepancy Checks: [all present / missing in: P#]
- [UNVERIFIED] density: [normal / suspicious in: P#]

→ Layer 2 acknowledges each flagged item in its synthesis.
→ If any gap blocks synthesis, back out to M10 before proceeding.

Proceeding to Layer 2.
```

**Fail:**
```
⚠️ GATE-2: not ready for Layer 2
- [specific blockers — e.g., "M6 HIGH on P2: recommendation #3 undermined by P3.1 findings"]
- Recommended action: [resolve blockers, then re-run GATE-2]
```

---

## PHASE 4: LAYER 2 CONVERGENCE (Cold Synthesis)

*Runs once, after all planned canonical steps are in. Ideally in a fresh conversation to reduce anchoring.*

### Pre-requisites

- **GATE-2 hard Gate passed** (all six checks)
- Fresh conversation with only the Starter attached (cool-down technical check)

### Notes for the researcher at Layer 2

Cold synthesis works best when you come to it without an active mental model of the conclusions. Three patterns quietly undermine Layer 2:

- **Recency bias** — the most recent prompt's framing tends to dominate synthesis. Re-read earlier prompts' findings before Layer 2, not just the latest.
- **Anchoring on the draft executive summary** — if an ES already exists (even a rough one), it shapes what you notice. Layer 2 rewrites the ES; don't let the old one pre-frame the new one.
- **Confirmation comfort** — if synthesis feels like it "clicks" quickly, that's often a sign it's echoing what you already thought, not discovering what the evidence actually says.

These are informational. The framework doesn't enforce them — they're context for the person running the project, not behavioral mandates on Claude.

### Cold convergence setup

The user opens a **fresh conversation**, attaches the final-state Starter, and pastes the Layer 2 prompt. The fresh conversation is deliberate — it prevents anchoring on the working session's accumulated reasoning.

### Layer 2 prompt template

```
Perform cold synthesis on a PRISM project through the lens of holistic research reconciliation. The attached Starter contains complete findings from all canonical specialist prompts and enrichment layers. This is a fresh session — you have no prior context and no attachment to earlier reasoning.

## Your Task

### 1. Read the full Starter
Read every findings section, the Assumption Register, the Rerun Register, the Action Log, and the Changelog. Form an independent picture before reading any summary or recommendations. Read earlier prompts' findings with the same care as the most recent ones — recency bias is real.

### 2. Premise Check (mandatory)
Go back to each prompt in the Starter. Ask: are its stated premises and assumed facts still consistent with what all other sources have found? List any prompts whose premises have shifted and describe how.

### 3. Conflict Resolution
Review the Action Log and Assumption Register for flagged conflicts. For each:
- State what each source concluded
- State what evidence supports each position
- Make a call and defend it

### 4. Quality Report Acknowledgment
If GATE-2's Quality Report flagged gaps (coverage, Assumption Register sparseness, missing Discrepancy Checks, suspicious [UNVERIFIED] density), acknowledge each one. State whether the gap materially affects the synthesis and, if so, how you're working around it.

### 5. Big Picture Synthesis
What patterns emerge when you look at all sources at once? What does one source agree with another on? What's only visible when you see everything together?

**Preserve [NULL RESULT] entries as findings.** A prompt that explicitly hunted for something and didn't find it is not an absence of content — it's a verified absence, and in some cases (clean Red Team, unable-to-refute Fact Check, Coverage with no material gaps) it's among the most valuable outputs the project produced. Standard summarisation tends to drop "things that didn't happen"; do not do this. If a major risk, competitor feature, or analytical weakness was explicitly investigated and not found, surface it in the deliverable. A clean adversarial pass increases confidence in the thesis; dropping it silently removes that signal.

### 6. Final Deliverable
Produce the final report structure appropriate for the stakeholder. For a product audit: executive summary, dimension sections, prioritised recommendations, risks, gaps. For research: executive summary, findings by dimension, conclusions, open questions.

**Writing standard:** Write with authority. Lead with conclusions. Defend every claim with a specific finding. Be direct about uncertainty — state what's known, what's inferred, and what's missing. No hedging language where evidence is strong; no false confidence where evidence is thin.

### 7. Quality Checks
- Does every recommendation tie to a specific finding?
- Are all quantitative claims sourced or tagged [UNVERIFIED]?
- Have all conflicts been addressed?
- Are [NULL RESULT] entries preserved as findings (not dropped as absences)?
- Is the executive summary honest about what's certain and what's not?

### 8. Layer 2 Convergence
1. Replace/update relevant sections of the Starter with synthesised content (per SP-6, use create_file — Layer 2 almost always needs a full rebuild)
2. Update the executive summary
3. Update prioritised recommendations
4. Add a substantive narrative Changelog entry (major version bump — canonical Layer 2 step)
5. Produce the final report as a separate deliverable file (stakeholder-friendly name, no P# prefix)
6. Copy both to /mnt/user-data/outputs/
7. Call present_files (per SP-7)
```

### Output

- Starter: major version bump, synthesis integrated
- Final Report: standalone deliverable (separate file, stakeholder-friendly name)
- Both placed in `/mnt/user-data/outputs/` and delivered via `present_files`

---

## MONITORS

*Automatic checks running throughout the session. Every trigger produces visible output. Every action gets an Action Log entry.*

### Monitor Sweep (compact checklist)

*Run this sweep at fixed moments: after convergence (before GATE-1), before Layer 2 (GATE-2), and at session closeout. The full narrative definitions below are reference — the sweep is what Claude actually executes.*

| # | Check | When |
|---|-------|------|
| M1 | All expected files attached? | Session start (GATE-0) |
| M2 | Header version = latest changelog? | Session start (GATE-0) |
| M3 | Prerequisites met for this task? | Session start (GATE-0) |
| M6 | Do new findings shift any prior prompt's premise? | After convergence |
| M7 | Do new findings conflict with Assumption Register? | After convergence |
| M9 | Did I stay in the correct layer (L1 vs L2)? | After convergence |
| M10 | Any issues with no natural deferral target? | After convergence |
| M12 | Conversation pressure — is accumulated session > ~50% of effective context? | Ongoing |
| M5+M12 | Combined: attachments + conversation > ~70% of effective context? | Ongoing |

*M4 (ambiguous ask), M5 (attachment pressure — single-dimension check, fires on its own trigger; note the combined M5+M12 check is part of the sweep), M8 (stale source), M11 (Layer 2 readiness) fire on their own triggers and aren't part of the routine sweep.*

### Context Pressure Bands

*Shared reporting convention used by GATE-0, M5, and M12. The bands exist because LLMs are bad at estimating their own context usage — a specific token count ("~142K") looks precise but isn't. Bands are honest about what the estimate is worth.*

| Band | Combined working set (% of effective context) | Absolute (1M context) | Absolute (200K context) | Action |
|------|-----------------------------------------------|----------------------|-------------------------|--------|
| 🟢 **Comfortable** | <20% | <200K | <40K | None. Proceed normally. |
| 🟡 **Getting warm** | 20-40% | 200-400K | 40-80K | Mention in output. No action needed; just awareness. |
| 🟠 **Curate now** | 40-70% | 400-700K | 80-140K | Prune integrated raw sources (M5 territory). If conversation-heavy and synthesis is degrading, consider migration (M12 territory). |
| 🔴 **Migrate** | >70% | >700K | >140K | Close current session per M12 protocol. Context rot is real at this level. |

*Thresholds are percentage-based against the effective context budget declared in the Runtime Profile. Absolute columns shown for 1M (default) and 200K (common paid-plan context) as reference. If Runtime Profile declares 500K context, halve the 1M column figures.*

Report format: `Context: 🟡 Getting warm (~[N]K attachments + ~[M]K conversation). [Action note if any.]`

Bands are approximate — the thresholds are calibration points, not cliffs. A specific token count can still be reported as a breakdown, but the band is what drives decisions. If attachments alone cross M5's ~30%-of-effective-context trigger, M5 fires regardless of band (it has its own action: curation). If conversation alone crosses M12's ~50%-of-effective-context trigger, M12 fires regardless of band (migration protocol). The band is the combined headline.

### Full Monitor Definitions

### M1 — Missing Inputs
**Trigger:** Expected file is not attached.
**Action:** STOP. Print "🔍 M1 triggered: [file] expected but not attached. Please upload before I proceed." Log: waiting on the user.
**Linked principle:** SP-1 (never reconstruct files from memory). If tempted to rebuild from recall, M1 is triggering silently — make it visible.

### M2 — Version Drift
**Trigger:** Starter header version ≠ latest Changelog entry, OR a version rule from **VERSION MANAGEMENT** has been violated (e.g., minor bump used where major was required, or vice versa).
**Action:** STOP. Print "🔍 M2 triggered: [specific discrepancy]. Please clarify before proceeding." Log: resolved with the user's answer.

### M3 — Sequence Violation
**Trigger:** Requested task depends on a prior task that's still ⬜ or 🔄.
**Action:** STOP. Print "🔍 M3 triggered: [task] depends on [predecessor] which is not complete. Options: (a) run predecessor first, (b) skip dependency and proceed anyway, (c) I misunderstood — please clarify." Log: decision.

### M4 — Ambiguous Ask
**Trigger:** The user's request has more than one valid interpretation given current state.
**Action:** STOP. Print "🔍 M4 triggered: your request could mean [A] or [B]. Which?" Log: clarification.

### M5 — Attachment Pressure
**Trigger:** The total attached working set (Starter + LLM outputs + uploads + skill files) is estimated to exceed **~30% of the effective context budget** declared in the Runtime Profile (~300K on 1M context, ~60K on 200K context).
**Action:** Do not stop work, but propose a curation pass. Print "🔍 M5 triggered: attachments estimated at [N]K tokens (~[P]% of effective context; Context band: 🟠 Curate now or 🔴 Migrate). Recommending curation: [specific suggestions — e.g., 'P3.1 raw outputs already integrated at v5, safe to drop from working set'; 'P1 walkthrough docx not needed for this task']. Proceed with current set, or prune first?"

**Note:** M5 is a curation trigger, not a file-split trigger. The Starter is always a single file. When attachments grow large, the response is to prune raw sources that have already been integrated, drop attachments not needed for the current task, and verify that only relevant material is in context. The ~30% threshold is approximate — context rot is real but gradual, and curation matters more than hitting an exact number.

**Combined with M12:** M5 and M12 measure different dimensions of the same effective context budget. A project can approach the limit through their combination without tripping either individually. See M12 for the combined threshold.

### M6 — Premise Shift
**Trigger:** A new finding invalidates a stated fact or assumption in an existing prompt's context section.
**Action:** Print the trigger AND a severity assessment:

```
🔍 M6 triggered: [prompt P-X] contains a premise that has shifted.
Old: [quote from prompt context]
New evidence: [finding from P-Y]
Flagging prompt for refresh.

Severity assessment:
- P-X findings converged: [yes at v[N] / no — not yet run]
- If already converged → Impact on existing findings:
  [LOW — shifted premise was peripheral to P-X's core analysis]
  OR [HIGH — P-X recommendation/finding [specific item] is directly
  undermined. Existing findings may need revision.]
- If HIGH → recommend M10 (rerun P-X with corrected premise)
- If LOW → log for Layer 2 reconciliation, no rerun needed
```

Add to Action Log. If findings already converged and severity is HIGH, chain to M10. GATE-2 re-checks all open M6 flags before Layer 2 proceeds.

### M7 — Assumption Conflict
**Trigger:** New finding contradicts an existing Assumption Register entry.
**Action:** Print "🔍 M7 triggered: new finding [X] conflicts with Assumption Register entry A[N] ([original claim]). Flagging for Layer 2 resolution. Both kept in register with conflict marker." Do NOT resolve in Layer 1. Log.

### M8 — Stale Source
**Trigger:** A cited source is >12 months old for a topic where recency matters (market data, pricing, org status, personnel).
**Action:** Print "🔍 M8 triggered: source [X] is [N] months old. Recency-sensitive claim. Suggest refresh via [method]." Log as advisory — the user decides.

### M9 — Convergence Type Drift
**Trigger:** Layer 1 work is sneaking interpretation in, OR Layer 2 work is still trying to add new sources.
**Action:** Print "🔍 M9 triggered: this work is [interpretation in L1 / new sourcing in L2]. Backing out and flagging for correct layer." Log the event and the correction.

### M10 — Rerun / Fix Required
**Trigger:** A rerun or fix is required but SP-2's deferral rules don't apply. Specifically:
- An issue exists but no natural touchpoint within the remaining canonical sequence
- A canonical step's output is flawed and needs to run again
- A new prompt needs to be injected mid-plan to fill a discovered gap
- A minor issue is high-priority and can't wait for deferral
- A GATE-1 check failed AND the fix cannot happen within the current session (requires new prompt run, access to external data, or async work). In-session fixes for GATE-1 failures are handled by GATE-1's Fail path, not by M10.

**Action:** Print "🔍 M10 triggered: [issue]. Classification: [rerun / injected prompt / standalone fix]. Proposed handling: [plan with target session]." Then use `ask_user_input` (where available) to present the classification as a tappable choice (rerun / injected prompt / standalone fix / cancel). Per SP-9, silence is not a confirmation — Claude waits for the user's response before logging. Falls back to prose ask where the tool isn't available.

Once confirmed:
1. Log entry in **Rerun Register** with target, classification, rationale, scope, target session, status
2. Update **Status Tracker** if a canonical step moves to ⚠️ NEEDS RERUN or 🔁 RERUN SCHEDULED
3. If classification is "injected prompt" and it's being promoted to canonical → trigger **Adaptation Checklist** (this is a canonical plan change → major bump). If kept as non-canonical fix → minor bump.
4. Log in Action Log

**Linked:** SP-2 (deferral), Rerun Register (tracking), Adaptation Checklist (if promoting to canonical).

### M11 — Layer 2 Readiness (triggers GATE-2)
**Trigger:** All canonical steps show ✅ in the Status Tracker AND the Rerun Register has no open entries (all ✅ or 🚫).
**Action:** Print "🔍 M11 triggered: all canonical steps complete, Rerun Register clear. Initiating GATE-2 readiness check." Then run GATE-2 checks (see GATE-2 section). Log: decision.

**Note:** M11 is a condition monitor — it detects a state rather than firing on a discrete event. GATE-2 is the formal verification. M11 prints when the conditions are met; the user can also request GATE-2 manually at any time.

### M12 — Conversation Pressure
**Trigger:** The current conversation is estimated to exceed **~50% of the effective context budget** (~500K on 1M, ~100K on 200K) accumulated in conversation history, tool outputs, and reasoning, OR Claude self-assesses quality degradation (slower reasoning, hazier references, less precise edits, missed cross-references, weak pattern-finding).

**Action:** Print "🔍 M12 triggered: session is long (~[N] turns, estimated [X]K tokens accumulated, ~[P]% of effective context; Context band: 🟠 Curate now or 🔴 Migrate). Synthesis quality may be degrading. Recommend: save current state (SP-7), note next task, start fresh session with Starter attached. GATE-0 will pick up cleanly."

**Combined M5 + M12 guideline:** If attachments (M5 dimension) + conversation (M12 dimension) together exceed ~70% of the effective context budget, recommend a fresh session regardless of whether either individual threshold has tripped. The context budget is shared — either one can quietly consume it, and the combined total is what determines whether the session still has headroom.

**Migration protocol:**
1. Complete and deliver any in-progress work (SP-7)
2. GATE-1 closeout if a prompt just completed, otherwise print a state summary
3. The user starts a new conversation, attaches the latest Starter
4. GATE-0 in the new session picks up where this one left off

**Note:** PRISM is already designed for session boundaries — every prompt runs in its own session. M12 formalises the signal for sessions that aren't single-prompt (e.g., multi-step convergence work, extended discussion, process updates that accumulate turns).

### Adding new Monitors

As we discover new failure modes, add them to this list with the same Trigger / Action / Log format. Adding a Monitor is an additive change → **MINOR** bump per PRISM semver (see VERSION MANAGEMENT → Scope of these rules).

---

## ADAPTATIONS

*The framework flexes. New prompts, new LLMs, new enrichment layers can be injected mid-project. This section defines how.*

### What counts as an Adaptation

- Adding a new prompt mid-project (new dimension discovered) — if promoted to canonical
- Injecting a new enrichment layer (e.g., adding multi-LLM to a single-LLM project, or running a mid-flight Discovery pass)
- Changing the run order
- Dropping a planned prompt
- Bringing in a new LLM source unplanned
- Upgrading a Scope Flag mid-flight (e.g., enrichment minimal → full)
- Any structural change to the canonical plan

Adaptations change the Prompt Strategy and are **canonical** changes — they drive a major version bump and get logged in the Strategy Revision Log inside the Prompt Strategy section.

### Adaptation Checklist

When the user proposes an Adaptation (or Claude detects one is needed via M10 with "injected prompt" classification):

1. **Scope check.** What is being added/changed/dropped? State precisely.
2. **Rationale.** Why now? What triggered this?
3. **Predecessor impact.** Does the Adaptation invalidate any prior prompt's output? Any Assumption Register entries? (If yes → M6/M7 territory, flag accordingly.)
4. **Run order.** Where does the new element fit? Before what? After what?
5. **Layer implications.** Is this happening mid-Layer-1 or post-Layer-1? If post-L1, the Adaptation is a significant event — document it clearly and consider whether Layer 2 should be re-scoped.
6. **Documentation.** Log in Action Log with full rationale. Update Strategy Revision Log. Update Status Tracker. Update Changelog. Update README if audit lenses changed.
7. **Confirmation.** Claude summarises the Adaptation and asks the user to confirm before executing.

### Output format for Adaptations

```
🔄 Adaptation proposed:
- Change: [what]
- Rationale: [why]
- Impact: [what shifts]
- Run order update: [new sequence]
- Strategy Revision Log entry: [drafted]
- Action Log entry: [drafted]
- Version bump: major (canonical plan changed)
Proceed?
```

Per SP-9, Claude uses `ask_user_input` (where available) to present the confirmation as a tappable choice (approve / modify / reject). Modifying opens the conversation for the user to describe the adjustment; rejecting aborts the Adaptation. Silence is not a go-ahead. Falls back to prose ask where the tool isn't available.

### Manual Revert (not a formal Adaptation type)

If a convergence goes wrong — LLM hallucinated during Layer 1 integration, the wrong file was attached and integrated, a finding was based on a source that was later retracted — the user can revert to a prior Starter version without re-running the framework.

Procedure:

1. **Identify the target version.** The last-known-good Starter lives in `_PRISM/Archive/` (per PROJECT FOLDER STRUCTURE). Pick the version to revert to.
2. **Attach that Archive file** at the start of a session.
3. **Claude bumps the version forward**, not backward — SP-8's filename discipline still applies. If the current state is v8 and reverting to v6-state content, the new file is v9 (not v6 or v6.1). The version number is a filename uniqueness guarantee, not a state identifier.
4. **Changelog entry is narrative and tagged `[MATERIAL]`** — something like: *"v9 [MATERIAL] — Reverted Starter content to v6 state. Rationale: v7's P4 integration was based on a hallucinated source (FC P4.2 later confirmed the citation was fabricated). v7 and v8 content discarded. The work done in v7–v8 is lost; affected prompts (P4) will need to re-run. Rerun Register updated."*
5. **Rerun Register** gets entries for any canonical work from the discarded versions that needs redoing.
6. **Assumption Register and Action Log** keep their entries from the discarded period — they're historical record, not state. This means the Register may briefly contain rows whose source claims no longer appear in findings; that's intentional audit trail.
7. **Status Tracker** reverts to the state from the target version, with any prompts that now need re-running marked ⚠️ NEEDS RERUN.

This is a manual pattern, not a formal Adaptation type or a new Monitor. The filename discipline from SP-8 (forward-rolling versions) and the Archive/ convention from PROJECT FOLDER STRUCTURE do the structural work; the Changelog entry and Rerun Register do the auditability work. No new machinery required.

If reverts start happening frequently on a project, that itself is a signal — M6 premise shifts or M7 conflicts should have caught the upstream problem earlier. Worth asking why they didn't.

---

## WHICH LOG GETS WHAT

*Four log-like structures exist. Here's which one records what.*

| Event | Changelog | Action Log | Rerun Register | Strategy Revision Log |
|-------|-----------|------------|----------------|----------------------|
| Canonical step converges | ✅ narrative entry | — | — | — |
| Non-canonical work (rerun, fix) | ✅ narrative entry | — | ✅ status → complete | — |
| Monitor trigger | — | ✅ trigger + action | ✅ if M10 | — |
| Adaptation | ✅ narrative entry | ✅ full rationale | ✅ if rerun involved | ✅ what changed + why |
| Process tweak | ✅ brief entry | — | — | — |
| Deferral logged (SP-2) | — | ✅ issue + target | — | — |
| Deferral escalated to M10 | — | ✅ escalation | ✅ new entry | — |

**Changelog** = file state changes (what changed in this version). Narrative form per entry.
**Action Log** = process-health events (what happened during work). Timestamped.
**Rerun Register** = live task list (what still needs doing). Cleared when done.
**Strategy Revision Log** = canonical plan changes only (how the plan evolved). Inside the Prompt Strategy section.

---

## PROJECT FOLDER STRUCTURE

*Convention, not a Gate-checked rule. Recommended for every PRISM project with External stakeholder deliverable = yes.*

### Delivery Folder (project root)

The project root is the **Delivery Folder** — optimised for stakeholder legibility. An uninitiated observer should be able to open this folder and immediately understand what they're looking at.

```
{Project Name} — {Date}/
├── {Project} Final Audit.md              ← THE deliverable
├── Appendices/
│   ├── {Project} Product Walkthrough.docx   ← standalone canonical artifacts
│   ├── {Project} UX & Design Findings.md
│   └── Research/                            ← raw LLM outputs, flat
│       ├── Claude DR — P3.1 — ...
│       ├── Gemini DR — P3.1 — ...
│       ├── Gemini DR — P3.2 — ...
│       └── Perplexity DR — P3.2 — ...
├── README.md                              ← orientation + PRISM description
└── _PRISM/
    ├── {project}_starter_v{latest}.md     ← current Starter
    └── Archive/                           ← superseded Starters
```

### Rules

- **Root holds only:** the final deliverable, Appendices/, README.md, and _PRISM/. Nothing else.
- **No P# prefixes in root or Appendices.** Stakeholder-friendly names only. The Status Tracker's `Delivery Filename` column is the authoritative P# → file index.
- **Appendices/** holds standalone canonical artifacts (component reports, walkthrough docs) and Research/ (raw LLM outputs, flat — role carried in filename per SP-8).
- **Research/ filenames** follow `[LLM] — [P#.x] — [Description]` pattern per SP-8. All flat, no sub-subfolders.
- **_PRISM/** holds the current Starter and Archive/. Internal working state — stakeholders can ignore it.
- **Archive/** holds superseded Starter versions. Move-on-supersede: when a new major Starter version is created, the previous one moves to Archive/ in the same action.
- **README.md** is a boilerplate orientation doc generated at Setup from the Prompt Strategy. Contains: folder contents map, PRISM methodology description, audit lenses with file mappings, and domain glossary. Stateless and regenerable — rebuild from the Prompt Strategy at any Adaptation.

### Dual-output prompts

Some prompts produce both a standalone artifact (e.g., P1 walkthrough docx) AND Starter findings. The Status Tracker records both:

| # | Prompt | Status | Delivery Filename | Starter Section |
|---|--------|--------|-------------------|-----------------|
| P1 | Product Walkthrough | ✅ | `{Project} Product Walkthrough.docx` | § P1 Findings |

The standalone artifact goes in Appendices/. The findings section stays in the Starter. Both are first-class outputs.

---

## STARTER FILE STRUCTURE

```markdown
# {PROJECT_NAME} — {SUBJECT}
**PRISM v{X.Y.Z} | Starter v{N} | {DATE}**
**Stakeholder:** {WHO}
**Status:** {one-line state}

---

## PROMPT STRATEGY

### Scope Flags
| Flag | Setting |
|------|---------|
| Multi-LLM enrichment | full / minimal / none |
| Cross-prompt dependencies | yes / no |
| External stakeholder deliverable | yes / no |
| Layer 2 cold synthesis | yes / no |
| Expected session count | <3 / 3-10 / 10+ |

### Runtime Profile
| Field | Setting |
|-------|---------|
| Host | Claude Skill / claude.ai chat / Claude Code / API / other |
| Effective context budget | 200K / 500K / 1M / other |
| File ops available | yes / no |
| Conversation history search | available / unavailable |
| Delivery mechanism | present_files / manual file link / export / other |

### Scope rationale
[Why these prompts, why this scope, what this project is trying to answer. Note any Discovery findings that shaped the plan.]

### Canonical sequence
- **P1** — [name]: [brief description]
- **P2** — [name]: [brief description]
- **P3** — [name]: [brief description]
  - P3.1 — [role] ([LLMs])
  - P3.2 — [role] ([LLMs])
- **Layer 2** — cold synthesis

### Dependencies
[What needs what — e.g., "P5 depends on P1-P4 findings"]

### Run order
[Optimised sequence with parallelization notes — e.g., "P1 → (P2 + P3 parallel) → P4 → P5"]

### Attach map + execution notes
| Prompt | Required attachments | Execution notes (best-effort) |
|--------|---------------------|-------------------------------|
| P2 | P1 walkthrough docx | *[prose block — thinking depth, web search, DR mode, vendor options; see Execution notes guidance in Setup]* |
| P3 | — | *[prose block]* |
| P3.2 | — | *[prose block — multi-LLM shape for FC]* |
| P4 | P1 walkthrough docx | *[prose block]* |
| P5 | — (all deps in Starter) | *[prose block]* |
| Layer 2 | — (Starter only) | *[prose block — highest reasoning, no web search, no DR]* |

*Execution notes are written at Setup by Claude and are best-effort based on current vendor capabilities. Update via Adaptation if notes materially change (e.g., a prompt's mode routing changes after early findings).*

### Expected outputs
[Per prompt: findings format, standalone deliverables if any]

### Enrichment Scoping
| Prompt | Enrichment proposed | Approved | Declined | Rationale |
|--------|---------------------|----------|----------|-----------|
| P1 | Coverage, FC | Coverage | FC | [why declined] |
| P3 | Coverage, DR, FC | All | — | — |
| P4 | RT | RT | — | — |

*Records what was proposed at Setup and what the user approved or declined per prompt. Declining is valid; omission is not.*

### Collection method
[If enrichment is scoped: how multi-LLM outputs get gathered, separator convention, single-file upload pattern]

### Strategy Revision Log
| Date | Version | Change | Rationale |
|------|---------|--------|-----------|

---

## STATUS TRACKER

| # | Prompt | Role / Lens | Status | Delivery Filename | Starter Section | Notes |
|---|--------|-------------|--------|-------------------|-----------------|-------|
| P1 | ... | ... | ⬜ | | § P1 Findings | ... |
| ... | | | | | | |

**Legend:** ⬜ NOT STARTED | 🔄 IN PROGRESS | ✅ COMPLETE | ⚠️ NEEDS RERUN | 🔁 RERUN SCHEDULED | 🚫 DROPPED

---

## RERUN REGISTER

| ID | Target | Classification | Rationale | Scope | Target Session | Status |
|----|--------|----------------|-----------|-------|----------------|--------|

**Classification:** rerun / injected prompt / standalone fix
**Status:** ⬜ scheduled | 🔄 in progress | ✅ complete | 🚫 cancelled

*Populated by Monitor M10 triggers. Closed when work completes. Checked at GATE-0 every session.*

---

## ASSUMPTION REGISTER

| ID | Claim | Value | Source | Date | Confidence | Prompt | Conflicts |
|----|-------|-------|--------|------|------------|--------|-----------|

**Confidence:** 🟢 multi-source verified | 🟡 single-source | 🔴 estimated

*The Date column records the source's publication date (YYYY-MM minimum) so Monitor M8 can evaluate recency. The Prompt column is populated at convergence with the prompt ID that produced the row. Complements [UNVERIFIED] inline tags. The Register provides a queryable table view of all quantitative claims; inline tags provide at-a-glance visibility in the findings text. Both are maintained — the Register for structured lookup, the tags for reading flow.*

---

## FINDINGS

### P1 — [Name]
[Populated when prompt completes]

#### Discrepancy Check
| Claim | This prompt's finding | Prior finding (source) | Verdict |
[Populated by the prompt's Discrepancy Check instruction]

### P2 — [Name]
[...]

---

## ENRICHMENT FINDINGS
*(If enrichment is scoped)*

### Discovery (Setup)
*Project-level problem-space mapping. Populated at Setup if Discovery was run.*

### P3.1 — [Role]
### P3.2 — [Role]
### P3.3 — [Role]

---

## SOURCES

[Numbered list, grouped by prompt and layer]

---

## FINAL SYNTHESIS
*(Populated at Layer 2 convergence)*

### Executive Summary
### Key Findings
### Recommendations
### Risks
### Gaps

---

## CHANGELOG

*Narrative form. One entry per version. Substantive enough to understand what changed without reading the diff.*

| Date | Version | Entry |
|------|---------|-------|
| {date} | v0 | Starter created, Prompt Strategy approved. [Scope Flags summary. Discovery summary if run. Enrichment Scoping summary.] |

*Minor versions carrying substantive findings are tagged [MATERIAL].*

---

## ACTION LOG

| Date | Monitor / Event | Trigger | Action |
|------|----------------|---------|--------|
| | | | |

*Captures process-health events (Monitor triggers, Adaptations, clarifications). Separate from Changelog (file state changes) and Rerun Register (live task list). Cross-reference by version.*

---

## PROMPTS

### P1 — [Name]
```
[Full atomic prompt text]
```

### P2 — [Name]
```
[Full atomic prompt text]
```

...
```

---

## LEARNINGS REGISTER

*Carried forward across projects. The starter gets smarter with each bake.*

**Status legend:**
- 🟢 **Active** — currently in force
- 🟡 **Qualified** — superseded in part, still partly relevant
- 🔴 **Superseded** — fully replaced by newer learning

### Lineage: Source Projects → PRISM

| Learning | Source | Became in PRISM | Status |
|----------|--------|----------------|--------|
| Never reconstruct from memory | Past audit project | SP-1 | 🟢 Active |
| Defer non-critical reruns | Past audit project | SP-2 | 🟢 Active |
| Versioning (major/minor) | Past audit project | VERSION MANAGEMENT | 🟢 Active |
| Convergence is part of delivery | Past audit project | SP-3 | 🟢 Active |
| Prompts must be self-contained | Past audit project | Prompt Design Principle #1-2 | 🟢 Active |
| Sequential edit stall at ~8-12 edits | Past convergence session | SP-6 | 🟢 Active |
| Multi-LLM triangulation works | Past research project | Phase 2, enrichment roles | 🟢 Active |
| Discrepancy Check catches divergence | Past audit project (method) | Prompt Design Principle #7 | 🟢 Active |
| [UNVERIFIED] inline tagging | Past research project (method) | Prompt Design Principle #9 | 🟢 Active |
| Premise changes propagate | Past research project (method) | Monitor M6 | 🟢 Active |
| Changelog discipline at every bump | Past research project (process) | VERSION MANAGEMENT | 🟢 Active |
| Browser batching for timeouts | Past audit project | Project-specific (not in PRISM) | 🟢 Active |
| Simulation stall at a known threshold | Past audit project | Project-specific (not in PRISM) | 🟢 Active |
| Three-doc splits wrong for mobile | Past audit project (process) | Single-file principle | 🟢 Active |
| Skill file for method, Starter for state | Past audit project (method) | Architecture (PRISM.md vs Starter) | 🟢 Active |
| Simulation tools may not match production | Past audit project (quality) | Learnings Register (quality) | 🟢 Active |
| Touch target measurement context matters | Past audit project (quality) | Learnings Register (quality) | 🟢 Active |

### Early Research Project (Mar-Apr 2026)

**Method:**
1. Multi-LLM triangulation works. Different LLMs have different indexes and biases — disagreement is the signal, not the problem. **Status: 🟢 Active**
2. Incremental integration (Layer 1) is safe. Big-bang final synthesis (Layer 2) is where real insight happens. **Status: 🟢 Active**
3. Red team as a distinct prompt role produces adversarial pressure that stress-tests the thesis. Essential for high-stakes work. **Status: 🟢 Active**
4. Fact check as a distinct prompt role catches the embarrassing errors before they reach the stakeholder. **Status: 🟢 Active**
5. `[UNVERIFIED]` inline tagging is better than a separate confidence table for claims that are LLM-sourced without primary attribution. **Status: 🟢 Active**
6. Premise changes propagate: when new findings shift what a prior prompt assumed, the prompt itself needs to be updated, not just the findings. **Status: 🟢 Active**
7. File splits happen organically when one file gets unwieldy. Don't split preemptively; split when bloat is real. *(v1.3 update: replaced with single-file principle and M5 curation trigger.)* **Status: 🔴 Superseded**

**Process:**
8. Running LLM work on a phone while Claude desktop does compute-intensive work parallelises the critical path. **Status: 🟢 Active**
9. Separators between pasted LLM outputs (`=== LAYER-N NAME ===`) let Claude reliably distinguish sources in convergence. **Status: 🟢 Active**
10. Changelog discipline at every version bump prevents drift and makes sessions pick up cleanly. **Status: 🟢 Active**
11. **Sequential `str_replace` edits stall around ~8-12 edits on large files.** v3→v4 convergence required 15 sequential edits; working memory loaded with file structure, all findings, remaining edits, and task context caused slowdown and near-stall. Codified as SP-6: rebuild via `create_file` when >~8 edits needed. Threshold set at the cautious end of the 8-12 variance. **Status: 🟢 Active**

### Early Audit Project (Apr 2026)

**Method:**
12. Specialist prompts need a Discrepancy Check built in — state divergence from prior findings, don't silently override or conform. Divergence is signal for Layer 2. **Status: 🟢 Active**
13. Quantitative claims must be defended, not just asserted. "I'm saying X because Y, but industry benchmark is Z" is better than just "X." **Status: 🟢 Active**
14. User voice research is cheap and catches assumptions that pure competitive analysis misses. Should be standard as an enrichment layer. **Status: 🟢 Active**
15. A Skill-level file is the right home for methodology. A Starter is the right home for project state. Keep them separate. **Status: 🟢 Active**

**Process:**
16. Three-document splits are wrong for mobile workflows. Two-file maximum. *(v1.3 update: single file always. No splitting.)* **Status: 🟡 Qualified** *(the anti-split principle is in force; the "two-file" wording was superseded by single-file in v1.3.)*
17. Convergence is Claude's job, not the user's. Update the Starter in the same session as the prompt runs. No handoffs. **Status: 🟢 Active**
18. Versioning by filename prevents stale copies on mobile. Every change = new filename. **Status: 🟢 Active**
19. Browser automation gotchas (scroll containers, SPA routing, timeouts) belong in a per-project technical notes section, not in the PRISM skill itself. Skill stays method-level. **Status: 🟢 Active**

**Quality:**
20. Simulation/test tools may not match production behavior. Caveat findings accordingly. **Status: 🟢 Active**
21. Touch target measurements from dev tools aren't transferable to user-facing pages. Measure in the right place. **Status: 🟢 Active**

### From PRISM v1.3 Audit (Apr 2026)

**Architecture:**
22. Single-file Starter always. On a 1M-token context (Opus 4.7 / Opus 4.6 / Sonnet 4.6 on API, Enterprise plans), file-splitting for size is unnecessary — the largest observed Starter (~2300 lines, ~55K tokens) used <6% of context. On smaller contexts (200K on most paid chat plans, 500K on some Enterprise surfaces), the headroom shrinks proportionally but single-file remains the right pattern because the binding constraint is sequential edit stalls (SP-6), not file size. Runtime Profile at Setup declares the effective context; Percentage-based M5/M12 thresholds adapt. **Status: 🟡 Qualified** *(v1.10: the "current Claude models" blanket language was over-broad; tightened to specific surfaces with percentage-based threshold adaptation.)*
23. Assumption Register and [UNVERIFIED] tags serve complementary purposes: Register for structured lookup, tags for reading flow. Keep both and observe whether the Register earns its keep. **Status: 🟢 Active**
24. Folder structure is a stakeholder presentation layer, not just file organisation. Delivery Folder root holds only deliverables; `_PRISM/` holds working state; Appendices bridges the two with component reports and raw research. **Status: 🟢 Active**
25. README at project root orients uninitiated stakeholders and carries PRISM methodology description. Stateless and regenerable from the Prompt Strategy. **Status: 🟢 Active**
26. Plan-centric versioning (major = canonical progress) is more useful as a glance-progress signal than content-centric versioning. The `[MATERIAL]` changelog tag compensates for substantive minor bumps. **Status: 🟢 Active**
27. Enrichment sub-prompts use decimal numbering (P3.1, P3.2) with role in the name, not the ID. The SC/FC/DR/RT/UV vocabulary is a guidance catalog, not a naming convention. **Status: 🟡 Qualified** *(v1.7: "SC" retired as a role name — split into Discovery and Coverage. Decimal-numbering principle remains; vocabulary catalog updated.)*
28. Framework adherence is ~70% blended. Judgment-dependent monitors (M6, M7) are the weakest link at 55-65%. Mitigations: embed monitor checks into the convergence checklist (check happens at the right moment), add backtrace audit to Gates (retrospective catch), and provide a compact Monitor Sweep table (scannable in one pass). PRISM-lite (~40% of framework at ~90% adherence) is a viable profile for simpler projects. **Status: 🟡 Qualified** *(v1.7: PRISM-lite binary retired in favour of Scope Flags — see Learning #32. Adherence estimates and mitigation strategies remain in force.)*
29. Expert persona prompts ("You are a...") degrade factual accuracy on knowledge benchmarks (Wharton 2025, USC/Hu et al. 2026) while improving writing tone and structure. The accuracy cost comes from identity assignment; the writing benefit comes from behavioral instruction. These are separable. PRISM uses lens framing ("Analyze through the lens of X") for accuracy-sensitive specialist prompts, and explicit writing instructions ("Write with authority, lead with conclusions") for the Layer 2 deliverable. Describe the output, not the author. **Status: 🟢 Active**

### From PRISM v1.7 Build (Apr 2026)

30. **Optional enrichment gets skipped.** A comparison of a v1.6 PRISM project against its pre-PRISM equivalent found that the PRISM run produced zero enrichment passes, while the pre-PRISM run produced ~11 enrichment passes (Scouting ×4, Fact Check ×2, Deep Research ×2, User Voice, Usage Intelligence, Audit Blind Spot Scouting ×3). Root cause: v1.6 framed Phase 2 as "Optional," which under session pressure → skipped by default. v1.7 converts enrichment scoping to a mandatory Setup step with opt-out per prompt. **Status: 🟢 Active**

31. **Scouting has two distinct functions that v1.6 conflated.** (a) Discovery of problem space — what dimensions to examine, what blind spots exist at the project level. Runs at Setup, can reshape Prompt Strategy. (b) Coverage within a prompt — what a specific analysis missed in its known domain. Runs after a specialist prompt, enriches findings. v1.7 splits these into named roles (Discovery / Coverage) with different phases, outputs, and convergence paths. Source: on a pre-PRISM project, a late-stage scouting pass explicitly did Discovery work — surfacing regulatory, ethical, and validity dimensions that weren't in the original prompt set. **Status: 🟢 Active**

32. **PRISM-lite as a binary "light vs full" toggle hides too much.** v1.5's PRISM-lite collapsed ~10 independent framework capabilities into one switch, forcing an all-or-nothing choice that didn't match real project shape (e.g., short project *with* stakeholder deliverable, or long project *without* enrichment). v1.7 replaces the binary with five orthogonal Scope Flags — enrichment, dependencies, stakeholder, Layer 2, session count — each defaulting to full coverage. Downgrade only on explicit opt-out. The old "light vs full" framing is retired. **Status: 🟢 Active**

### From PRISM v1.7.5 External Review (Apr 2026)

33. **A structured external-LLM QA pass catches schema bugs self-review misses.** v1.7.5 was triggered by a Gemini Pro Deep Thinking review of v1.7.1 that surfaced nine acted-on items — six schema bugs (including SP-8's illegal-on-Windows pipe delimiter, the Assumption Register column header mismatch claimed reconciled in v1.7, and the Action Log's dual-tracking `Status` column) plus three operational edge cases (M8's mechanical non-functionality without source dates, qualitative "lighter touch" language under pressure, P1's hallucinated-prior-findings risk). Several of these were items the author reviewed during v1.7's build and missed; self-review from inside the build is a known blind spot. Practice that seems to work: after a major bump stabilises, run the previous version through a strong external LLM (Gemini Pro Deep Thinking, GPT-5 Pro, Claude Opus with extended thinking) with the prompt "QA audit this framework — find schema bugs, contradictions, and operational edge cases," then triage the review with the author. The v1.7.1-era review found the bugs v1.7 had introduced; running review against the prior version rather than the current one also protects against review-bias from recent edits. Not formalised into framework machinery — it's an author-level practice, not a runtime rule — but worth repeating after any substantial version bump. **Status: 🟢 Active**

### From PRISM v1.8 Build (Apr 2026)

34. **Split response to external review across patch and minor bumps by change type, not by batch.** The Gemini v1.7.1 review surfaced 14 items spanning schema bugs, edge cases, and behavioural additions. The first instinct was to take the acted-on items as a batch and release them together. Doing it by change-type instead produced cleaner releases: v1.7.5 absorbed all nine corrections/clarifications/schema fixes as a patch (no behavioural change, fits the PATCH semver definition), v1.8 absorbed the four behavioural additions as a minor (extends behaviour, fits MINOR). The test is the semver rule codified in v1.7.3: does this change framework behaviour? Corrections say no → PATCH. Additions say yes → MINOR. Batching by review cycle obscures that test. Splitting by change type also keeps each release small enough to review cleanly — v1.7.5 was 13 edits in distinct sections, v1.8 was 7 edits plus Version History and learnings. A combined release would have been 20+ edits, well past SP-6's threshold, and would have mixed "fix the typo" with "add new behaviour to Layer 1" in one Changelog. Principle: a single review produces multiple release candidates classified by semver level, not one release that happens to include everything. **Status: 🟢 Active**

35. **When a multi-edit build exhausts tool budget mid-session, the handoff pattern is the framework's own M12 migration.** The v1.7.5+v1.8 build ran back-to-back in a single session, hit the tool-use limit partway through v1.8, and had to resume in a new turn within the same session using the `/home/claude/` working copy as the baseline (since it persists within a session). This worked because: (1) the file was produced via `present_files` at the v1.7.5 delivery point, giving a recoverable artifact, (2) the `/home/claude/` working copy survived between turns, so the v1.8 edits didn't need to be re-applied from memory, and (3) the remaining work was well-defined at handoff — Version History entry, learnings, verification, delivery — not a design question. If the session had been terminated rather than just turn-limited, attaching v1.7.5 to a fresh session and providing the v1.8 edit spec as a handoff document would have been the equivalent recovery. The framework's M12 migration protocol is the right model for this: save state (SP-7), note next task, resume on attached file. Not new machinery; just confirmation that the existing pattern covers this case. **Status: 🟢 Active**

### From PRISM v1.9 Build (Apr 2026)

*v1.9 shipped briefly and was superseded by v1.9.1 before meaningful use — most of its vendor machinery was walked back. Learnings #36-38 here survive the walk-back because they capture understanding that remains true regardless of whether the specific machinery was kept. Text is reconstructed from v1.9 themes as preserved in the v1.9.1 handoff and the PRISM backlog; the underlying decisions stand even where the encoding was rolled back.*

36. **Silence is never consent — the temptation is structural, not interpretive.** During the v1.9 workshop on `ask_user_input` integration, an initial proposal included a timer with high-confidence defaults that would auto-advance on timeout. On inspection, this inverts SP-5's core stance: if silence auto-resolves to the default, the user's non-response has been interpreted as consent — which is exactly what "no heuristic guessing on ambiguous input" forbids. The temptation toward timers is structural (tool-mediated interfaces naturally suggest them) rather than interpretive (a human reader of a prose question doesn't feel pressure to "resolve" silence). SP-5 handled interpretive guessing; SP-9 generalises the stance to tool-mediated decisions. Mechanism: `ask_user_input` with pre-selected defaults and a "Keep all defaults" shortcut preserves the convenience of one-tap consent without conceding the principle. The user still taps. Codified as SP-9 in v1.9; kept unchanged in v1.9.1. **Status: 🟢 Active**

37. **Role-based vendor recommendations age better than named-vendor recommendations — and prose guidance ages better than framework machinery.** Vendor capabilities drift on a 3-6 month cycle. Embedding named recommendations in the framework file ("use Gemini Pro for Deep Research, Perplexity for Fact Check") would force frequent patch bumps just to stay current, and the recommendations would be wrong more often than right between bumps. v1.9's initial response was to describe roles in the framework ("use a vendor with strong multi-document synthesis for DR") and keep vendor-to-role mapping as a separate, shorter-lived artifact. v1.9.1 went further: the mapping itself is prose output generated by Claude at Setup per SP-10, not encoded as framework machinery at all. The framework describes the shape of the recommendation (single-LLM preferred→fallback vs. multi-LLM independent set) and defers the content to Claude-at-runtime. Principle: any content that ages on a faster cycle than the framework itself should live outside the framework. **Status: 🟢 Active**

38. **Defer to platform-level flags where the platform is already making a finer-grained decision with better information.** v1.9 considered a per-prompt thinking-depth matrix ("Red Team → extended thinking; Layer 2 → extended thinking + Deep Research; specialist → standard"). During workshop, Claude.ai's Adaptive Thinking surfaced as the counterargument: the platform already decides per-turn whether to think deeply, using the current prompt's actual content — which is strictly more information than a framework-level matrix could encode. A per-prompt matrix in the framework would be redundant at best (saying the same thing the platform already says) and wrong at worst (overriding the platform's per-turn judgement with a per-prompt-type generalisation). v1.9 accordingly recommended Adaptive Thinking on at Setup as a single platform-level flag rather than encoding a thinking-depth matrix. v1.9.1 further refined this via dogfooding SP-10 (see Learning #42): platform flags themselves drift across model releases, and recommendations about them need SP-10's verification pattern. Principle: the framework recommends at the coarsest level the recommendation is reliable at; it doesn't try to out-think the platform where the platform has finer-grained signal. **Status: 🟢 Active**

### From PRISM v1.9.1 Build (Apr 2026)

39. **Deterministic Python transformation scripts for mid-size, non-cascading builds.** When a version bump requires ~15-25 edits across distinct sections of a large file, and the edits don't cascade (each sits in its own section, touches no shared state), a Python transformation script run over the prior version via `bash_tool` is the right build method. Three tool calls total regardless of edit count (write script, run script, deliver output). Preserves formatting that `create_file` full rebuilds can drop; deterministic and reviewable as a single artifact; survives session interruption via `/home/claude/` persistence. Above ~25 edits or for cascading rewrites, `create_file` full rebuild is still correct (SP-6). Below ~6 edits, `str_replace` is still faster. The sweet spot v1.7.1 and v1.9 occupied — 15-25 discrete, non-cascading edits — is where this pattern is clearly best. Codified here after being used successfully across three consecutive builds (v1.7.1, v1.9, v1.9.1). **Status: 🟢 Active**

40. **Deep Research routing: mode should match task, not span the whole prompt.** Deep Research is a web-search-then-synthesize engine. It earns its keep when external sourcing genuinely adds value — comparing current platform features, surveying recent literature, pulling data from evolving market/product state, or when multi-source convergence is the point. When the task is synthesis or structuring of stable, well-trained domain knowledge (taxonomies, prerequisite chains, classical classifications, established difficulty tiers), routing through Deep Research actively degrades output: the model spiders tangential pages, loses coherence, exhausts context, and produces worse results than direct generation would. "Like asking someone to Google the alphabet." The fix isn't splitting big prompts into smaller ones — it's routing each sub-task to the right mode. Source: music theory platform project, seven proposed Deep Research prompts analysed and re-routed. Prompt 1 split into 1A (taxonomy + prerequisites + levels → regular) and 1B (methodology comparison + misconceptions → deep research). Prompt 6 split three ways with only platform analysis staying DR. The principle informs Prompt Strategy drafting at Setup — Claude evaluates routing fit per proposed prompt and splits where sub-tasks have different routing needs. The Deep Research field in execution notes is the concrete surface. **Status: 🟢 Active**

41. **Preemptive scope-down as a cross-platform thinkless-output signal.** Observed on Opus 4.6 Extended (April 2026) with the specific pattern: user sends a simple continuation command ("Ssa next"), Claude performs tool discovery and status reads, then before attempting any actual work declares "I'm running low on context budget in this session" and recommends starting a fresh session. The complaint persists even after the user confirms context is fine. This is distinct from legitimate budget awareness (which comes late in a session after visible work, proposes compression rather than deferral, and responds to user correction). The pattern is cross-platform — equivalent behaviours exist on other vendors under different surface forms (fast-mode deflection, "this is a big task, want me to split it?" framings, premature task_budget-style wrap-up). PRISM addresses it via the Output Quality Check (signal #6) with two application points: live watch during the run (in the prompt template) and convergence-time verification (in the convergence checklist). Single-signal trigger — unlike content-level signals (unsourced claims, template output, etc.) where two or more must fire, preemptive scope-down alone warrants re-run. Source: user screenshots of the behaviour; Anthropic community reports of related Opus 4.6/4.7 quality issues (HN thread on 4.7 launch, GitHub issue #46727 on Opus 4.6 Max 20x). **Status: 🟢 Active**

42. **Dogfooding SP-10 during the v1.9.1 design session revealed the verification pattern needs to be reconcilable, not deferential.** SP-10 was initially framed as "verify before recommending." During design, Claude ran a web search to verify its understanding of Adaptive Thinking on Opus 4.7; search returned API-heavy results that didn't cleanly answer the UI-specific question the user had raised. User provided a direct screenshot of the Claude.ai UI that resolved the ambiguity. Lesson: (a) search finds API/developer docs much more readily than end-user UI docs, so the verification pattern must include both; (b) the user's direct observation of the interface often beats Claude's best search, so SP-10 explicitly weights user observation where it contradicts training-era knowledge; (c) "verify before recommending" doesn't mean "defer to what's found" — the search result is input to a calibrated recommendation, not a substitute for reasoning; (d) where verification yields ambiguous or interface-dependent answers, expose the ambiguity in the recommendation rather than hiding it behind a single confident choice. SP-10's final wording reflects all four points. **Status: 🟢 Active**

43. **External review catches what internal review cannot, across release cycles.** Second instance of Learning #33's pattern: external reviews (Claude Pro review and ChatGPT Pro review, both of v1.7.1) surfaced Scope Flag internal contradictions (minimal/full enrichment trigger mismatch, M7 over-disabling, M12 over-disabling) that had shipped silently through v1.7.2, v1.7.3, v1.7.4, v1.7.5, v1.8, v1.9, and v1.9.1 — seven releases across several weeks of internal review and dogfooding. The pattern is robust: strong external LLM review against a specific version (not the latest) catches self-review blind spots created during that version's build. Practice worth institutionalising: after every minor or major release stabilises, run the *previous stable version* through an external LLM with a structured QA prompt. Separately, this cycle also demonstrates the **prose-vs-structure tension resolution** on Execution notes: v1.7.1 promised execution packaging without structural fields (gap); v1.9 over-delivered with a three-column machinery (too rigid for fluid domain); v1.9.1 walked back to prose column (right direction but loose); v1.10 added minimum-content requirement to prose (settling point). The four-iteration sequence is the cost of not seeing the middle path on the first or second try. Generalisable: when a framework promise tensions against structural specificity, the answer is often required-content-in-prose rather than either extreme. **Status: 🟢 Active**

44. **Markdown table integrity — verify post-edit.** Markdown tables are sensitive to at least two distinct content patterns that silently break rendering, and both have shipped through multiple PRISM releases before being caught. **(a) Blank lines inside the table.** A blank line anywhere inside a markdown table silently terminates the table; rows after the blank render as plain text. The failure mode is silent (no error, no warning, content is preserved) and renderer-dependent (some desktop renderers tolerate it, mobile ones don't). PRISM's Version History hit this at v1.8's build: a row insertion produced a blank line between the v1.7.5 and v1.8 rows, breaking the table. The break shipped silently through v1.8, v1.9, v1.9.1, v1.10, and v1.10.1 — five releases — before a user viewing v1.10.1 on Claude.ai mobile caught it. **(b) Unescaped pipe characters inside backtick code spans inside table cells.** Pipes are the column delimiter in markdown tables. When a cell contains a code span that itself contains a literal *unescaped* pipe, different parsers behave very differently — some miscount columns, others hit unexpected parse states. The observed failure modes on a single file across three renderers: Claude.ai web rendered the row but squeezed into a single narrow column (garbled); a standalone markdown viewer app silently dropped the entire table (no error); the Claude mobile app crashed the file view on open (hard fail). PRISM hit this at v1.10.2's build: the v1.10.2 row documented the blank-line bug using code-span examples containing literal unescaped pipes. **Escaped pipes** (using backslash: `\` followed by the pipe character) inside code spans inside cells work across renderers — historical Version History entries have used this construct safely (v1.7's row documenting the older filename convention is an example). The crash-prone combination is specifically the unescaped form. **Mitigation against recurrence:** after any edit that touches a table (adds rows, edits cells, reorders rows), scan every table in the file for both failure modes before delivering. A small awk pass catches blank lines — walk the file tracking whether the current line is inside a table (entered by the header row, exited on any non-table line), and flag any blank line encountered while inside. A second Python pass catches unescaped-pipe-in-code-span-in-cell — for each table row, find all backtick-delimited spans and check whether any contain a pipe character not preceded by a backslash. Both checks are cheap; both catch silent, renderer-dependent failure modes that regular review misses. Adopting them as default build-verification steps closes the gap. Also worth: when describing markdown syntax inside a markdown file, prefer prose descriptions over literal code-span examples whenever the example would contain table-hostile characters — prose is more robust than relying on escape characters to survive all renderers. Source: v1.10.2 patch session (blank-line mode), v1.10.3 patch session (unescaped-pipe mode), Apr 2026. **Status: 🟢 Active**

45. **Tables with many long cells are fragile across renderers — use headings for release-notes-style content.** Markdown tables work well for compact tabular data (short cells, regular structure). They work poorly for release-notes-style content where each row is really a long-form narrative — 2KB to 7KB of prose with nested formatting. Each such cell becomes a deeply-nested DOM subtree; when many accumulate (PRISM hit the ceiling at around 19 rows), mobile renderers in particular can exceed memory or complexity limits and crash on file open. The failure pattern is cumulative and environment-dependent: desktop renderers cope (possibly with visual glitches), standalone viewers may silently drop the table, mobile apps may hard-crash. The failure passes desktop review and only surfaces on mobile use, which makes it easy to ship through multiple releases. **Rule:** for content that grows unboundedly (changelogs, release notes, long issue logs, anything where each entry is a long-form narrative), prefer heading-based format over tables. Each entry becomes an H3 or H4 with tag and date inline and body as a paragraph. Benefits: no cell-complexity ceiling, per-entry anchors for navigation, easier to edit without stressing table alignment. Tradeoff: slightly less scannable for very short entries, rarely relevant for release notes. Tables remain correct for true tabular data (short regular cells: Scope Flags, Monitor Sweep, Context Pressure Bands). Source: v1.10.2 and v1.10.3 mobile-crash pattern, v1.10.4 restructuring, Apr 2026. **Status: 🟢 Active**

### From Future Projects

*Each project feeds the culture.*

[Add learnings here with project name and date as they emerge.]

---

## ADAPTATION NOTES — OTHER USE CASES

PRISM generalises beyond product audits. Worked examples:

**Competitive landscape research** (SP pattern):
- Skip product walkthrough prompts
- Heavy enrichment layer with Coverage/Fact Check/Deep Research/Red Team
- Discovery at Setup to surface non-obvious competitor segments and market definitions
- Final deliverable is an internal brief, not a stakeholder report

**Technical due diligence:**
- Heavy Technical prompt
- Red Team prompt focuses on engineering risk
- Discovery at Setup to surface regulatory and compliance dimensions
- Final deliverable is a DD memo with risk register

**Market entry analysis:**
- Competitive + market sizing + regulatory prompts
- Heavy enrichment on market data
- Discovery at Setup to surface jurisdiction-specific blind spots
- Final deliverable is a go/no-go recommendation

**Investment memo:**
- Competitive + strategy + team + financials prompts
- Red team as mandatory
- Fact check as mandatory
- Discovery at Setup to surface industry-specific diligence dimensions
- Final deliverable is an IC-ready memo

**Core pattern that transfers:**
1. Declare Scope Flags
2. Run Discovery if enrichment is scoped
3. Identify dimensions (Discovery-informed)
4. Draft the Prompt Strategy (the plan) with per-prompt Enrichment Scoping
5. Write atomic specialist prompt per dimension
6. Run independently, in parallel where possible
7. Layer 1 integrate as sources arrive
8. Layer 2 cold synthesis with everything on the table
9. Produce stakeholder-appropriate final deliverable in the Delivery Folder

---

## FRAMEWORK LIMITATIONS

*Honest calibration. PRISM is aspirational in places. These numbers are estimates from v1.4 analysis, to be refined through real projects.*

### Adherence estimates

- **Gates, Standing Principles, version management:** ~85-90%. Structural and procedural — hard to accidentally skip.
- **Reactive monitors (M1-M4):** ~85%. Fire at natural checkpoints.
- **Judgment monitors (M5-M9):** ~55-65%. Require interrupting in-progress reasoning to cross-reference. Silent failure is the common mode. The Monitor Sweep, GATE-1's backtrace audit, and GATE-2's Quality Report mitigate this.
- **Complex monitors (M10-M12):** ~50-60%. Multi-step evaluation that fights Claude's bias toward continuing.
- **Qualitative standards (changelog depth, [MATERIAL] tags, Discrepancy Check tables):** ~50-65%. Easy to simplify under pressure.

**Blended: ~70% adherence to the full framework in any given session.** The user spot-checks the critical 30%. GATE-1's backtrace audit (per-prompt) and GATE-2's Quality Report (project-level) catch what monitors miss. First 2-3 projects are calibration — track what fires vs what should have and evolve the triggers.

The 70% that works is already a massive improvement over no framework. GATE-0 alone catches "pressed send too fast." SP-1 alone catches "reconstructed from memory." SP-3 alone prevents "convergence left to the user." SP-7 alone ensures files are delivered. Those four at ~90% adherence are worth the entire framework's overhead.

### The false-rigor risk

At 70% adherence, 30% is silently not happening. The framework creates an expectation of completeness that actual adherence doesn't match. The gap between perceived and actual coverage is more dangerous than having no framework — because without one, the user stays vigilant. **Antidote:** assume monitors are advisory, not reliable. The user is the real M6.

### Scope Flags (retired: PRISM-lite)

*v1.5 introduced a "PRISM-lite" binary profile (light vs full). v1.7 retires it in favour of orthogonal Scope Flags — see Setup.*

The old binary forced an all-or-nothing choice across ~10 independent framework capabilities, which didn't match real project shape (short project *with* stakeholder deliverable; long project *without* enrichment; etc.). Scope Flags let the user declare five axes independently at Setup: Multi-LLM enrichment, Cross-prompt dependencies, External stakeholder deliverable, Layer 2 cold synthesis, Expected session count. Each flag activates or deactivates specific framework machinery, and all default to full coverage.

A project can upgrade flags mid-flight via Adaptation (major bump). Downgrades are not supported once machinery is active — dormant is fine, removing mid-project is not.

See Learning #32 for the rationale behind the change.

---

## PRISM VERSION HISTORY

*PRISM uses standard semantic versioning (MAJOR.MINOR.PATCH). See VERSION MANAGEMENT → Scope of these rules. The Starter's own versioning is a different scheme — see the same section.*

### v1.0 — 2026-04-10

Initial framework. Distilled from real-world competitive research and product audit projects. GATE-0, Monitors M1-M9, two-layer convergence, Adaptations, Learnings register.

### v1.1 — 2026-04-10

Added VERSION MANAGEMENT with full major/minor rules and download tracking discipline. Added STANDING PRINCIPLES (SP-1 through SP-5). Added GATE-1. Fixed version-bump semantics in Layer 1 convergence. Enhanced M1 and M2.

### v1.2 — 2026-04-10

Introduced "canonical steps" as core concept. Added Prompt Strategy as named artifact. Added Rerun Register and Monitor M10. Refined SP-2 with deferral rules + M10 escalation. Added SP-6 (rebuild at threshold). Rewrote VERSION MANAGEMENT with canonical framing.

### v1.3 — 2026-04-10

**Cold audit pass (Layer 2 on the framework itself).** Single-file principle: retired prompts-file splitting and companion file concept entirely. Replaced M5 (file bloat → working set curation at ~300K tokens). Added M11 (Layer 2 readiness trigger). Added SP-7 (file delivery mandatory). Added GLOSSARY. Added PROJECT FOLDER STRUCTURE (Delivery Folder, Appendices, _PRISM/, README). Added WHICH LOG GETS WHAT map. Introduced decimal prompt numbering (P3.1, P3.2) for nested enrichment; demoted SC/FC/DR/RT/UV from ID convention to role-guidance catalog. Added attach map to Prompt Strategy. Added Delivery Filename column to Status Tracker. Added Discrepancy Check output format (table). Upgraded Changelog to narrative form with [MATERIAL] tag for substantive minor bumps. Added GATE-0 prompt freshness check (M6 flags). Tightened Layer 1 corrective scope to uncontested errors only. Relaxed SP-2 (removed fabricated 2-3 step window; now "next natural touchpoint, else M10"). Updated SP-6 threshold unit from "5 sections" to "~8 sequential edits." Added Learnings Register lineage table. Added learnings #22-27 from the v1.3 audit. Context window analysis: 1M tokens on current Claude models makes splitting unnecessary for any observed project size. v1.3 built via create_file per SP-6 (full rebuild — every section touched).

### v1.4 — 2026-04-10

**Engineering hardening.** Added **GATE-2** (Layer 2 readiness) as formal Gate with pass/fail output, absorbing the pre-requisites previously inline in Phase 4. M11 reframed as the trigger that proposes GATE-2. Added **M12** (Context Pressure) — fires when accumulated session tokens degrade synthesis quality (~500K threshold), recommends migration to fresh session with protocol. Enhanced **M6** with severity assessment for already-converged findings: LOW (peripheral, defer to Layer 2) vs HIGH (key finding undermined, chain to M10 for rerun). GATE-2 re-checks all open M6 flags with severity before Layer 2 proceeds. Enhanced **GATE-0** with conversation-history cross-reference (catches wrong-file-from-Downloads) and working-set budget estimate in output. Added GATE-2 and M12 to GLOSSARY. Updated Gates concept, SP-4 range, HOW TO READ ordering. v1.4 built via str_replace (11 targeted edits — at SP-6 threshold but each independent and non-cascading).

### v1.5 — 2026-04-10

**Adherence hardening.** Added **backtrace audit** as final step of GATE-1 and GATE-2 — retrospective scan catching what monitors miss (SP compliance, version correctness, changelog quality, M6/M7 triggers that should have fired). Added **Monitor Sweep** compact checklist table alongside full narrative definitions — scannable in one pass at fixed moments. Added **non-prompt session closeout** protocol for Adaptation/bookkeeping sessions. Embedded **M6/M7 pre-scan** into the atomic prompt convergence checklist (step 0) — checks happen at the right moment, not from memory. Added **FRAMEWORK LIMITATIONS** section with honest adherence estimates (~70% blended, ~85-90% on structural, ~55-65% on judgment monitors). Added **PRISM-lite** profile: core ~40% of framework at ~90% adherence for simpler projects, with Complexity field in Setup to select. Added learning #28 (adherence calibration). v1.5 built via str_replace (9 targeted edits).

### v1.6 — 2026-04-10

**Evidence-based prompt framing.** Replaced identity-based role prompting ("You are a [SPECIALIST ROLE]") with lens framing ("Analyze through the lens of [SPECIALIST DOMAIN]") across all prompt templates. Based on Wharton (2025) and USC (2026) research showing expert personas degrade factual accuracy by 3-5% on knowledge benchmarks while only improving tone/structure — benefits achievable through behavioral writing instructions instead. Rewrote **Prompt Design Principle #3** with research citations. Updated **atomic prompt template** opening. Updated **Layer 2 template** with explicit writing-quality instructions for the deliverable ("Write with authority, lead with conclusions, be direct about uncertainty"). Added learning #29. Principle: describe the output, not the author.

### v1.7 — 2026-04-18

**Structural evolution.** Largest revision since v1.3's cold audit. Three big moves: (1) retired the PRISM-lite binary, replaced with **Scope Flags** at Setup — five orthogonal toggles (Multi-LLM enrichment, Cross-prompt dependencies, External stakeholder, Layer 2, Expected session count) that activate specific framework machinery, defaulting to full scope for uninitiated users; (2) converted enrichment from opt-in to mandatory opt-out **Enrichment Scoping** at Setup, closing the failure mode observed in comparative analysis where enrichment framed as optional was silently skipped; (3) split v1.6's "Scouting" role into **Discovery** (Setup-phase, maps problem space, can reshape Prompt Strategy) and **Coverage** (prompt-phase, enriches a specific prompt's findings). **Opener rewrite:** new subtitle ("A Framework for Context-Disciplined, Multi-Session LLM Research and Audits"), problem-statement opening replaces the descriptive-first framing, eight definitional bullets replace the v1.6 "core moves" enumeration, "What's next?" established as the universal re-entry prompt for start/resume/"where was I?", "HOW TO READ" renamed to "HOW TO USE", generalised origin line (no project-specific names), Glossary gains **Atomic prompt** and **Specialist lens** entries. Also: new **SP-8** (canonical file integrity + `[LLM] \| [Prompt ID] \| [Description]` look-alike filename convention); GATE-2 backtrace reframed as informational **Quality Report** feeding Layer 2 rather than gating it; GATE-2 cool-down check made purely technical (fresh-session check only, no hours) with separate researcher-facing notes on recency bias, anchoring, and confirmation comfort added to Phase 4 introduction; **M5/M12 unified dimensionally** as Attachment Pressure / Conversation Pressure with combined ~700K-token threshold; atomic prompt template gains **Writing Standard** block extending v1.6's behavioral-instruction philosophy beyond Layer 2 to every specialist prompt; new **[NULL RESULT]** convention for explicit "investigated, found nothing material" reporting; Starter header now records PRISM version alongside Starter version (critical for post-hoc reading of which framework rules were in force); **Learnings Register gains Status column** (🟢 Active / 🟡 Qualified / 🔴 Superseded) applied to all prior entries; GATE-0 gains Prompt content readiness check (#10), Overdue Reruns output slot, and the conversation-history cross-reference is promoted from optional to mandatory with time-boxing; GATE-1 backtrace gains Header-sync check; M10 trigger "GATE-1 failed" clarified to exclude in-session fixes (those are GATE-1's Fail path, not M10 territory); SP-6 threshold gains explicit calibration note (err toward the lower end of the 8-12 variance); Assumption Register schema reconciled to 7 columns across prompt template and Starter structure; Discrepancy Check table header standardised to "This prompt's finding"; USC PRISM (Hu et al. 2026) naming collision footnoted once so future readers don't confuse techniques; "Ron" generalised to "the user" throughout the framework file (metadata authorship line preserved); v1.0 row in this Version History generalised from project-specific names to "real-world competitive research and product audit projects"; new learnings #30-32 capture the rationale for enrichment being opt-out, the Discovery/Coverage split, and the PRISM-lite retirement respectively; Learnings #7, #27, #28 marked Superseded or Qualified accordingly. Source: review-and-discussion session on v1.6 + comparative analysis of a v1.6 project against its pre-PRISM equivalent + a separate opener-rewrite session, handed off to a fresh build session via a 26-item methodology spec and an opener-handoff file to avoid mode-switch fatigue (mirrors the Layer 2 cool-down principle the framework itself codifies). Built via create_file for the initial v1.7 rebuild per SP-6; opener incorporation applied via surgical str_replace edits (7 non-cascading replacements, under SP-6 threshold).

### v1.7.1 — 2026-04-18

**Naming hygiene, two small fixes, and one behavioural addition.** Minor version bump addressing v1.7 taste-check feedback. (a) **Naming hygiene** — all project-specific proper nouns ("Solace," "SpherePoint," project-specific numbers like "~43 days," specific line counts like "2343 lines") generalised to neutral descriptors in the framework body; Skill description trigger list switched from specific project filenames (`SP_CompResearch`, `SP_starter`, `solace_audit_master`) to patterns (`*_starter_v*.md`, `*_audit_master*.md`) — strictly more powerful as triggers. Authorship metadata ("Maintained by: Ron Kuper + Claude") preserved. Principle: names belong in Starter instances, not in PRISM.md. (b) **Learnings Register status fixes** — three entries where the displayed status contradicted the entry's content moved from 🟢 Active to 🟡 Qualified (Browser batching and Simulation stall are project-specific and "not in PRISM"; Learning #16's parenthetical already admitted qualification). Lineage table Source column stripped of named projects; Lineage section headers renamed ("From SpherePoint" → "Early Research Project," "From Solace" → "Early Audit Project"). (c) **Monitor Sweep disambiguation** — M12 row split into two rows so the individual-threshold check (session > ~500K) and the combined check (attachments + conversation > ~700K) are separately visible rather than crammed into one cell. Footnote updated to clarify M5's status (single-dimension on its own trigger; the combined M5+M12 check is the sweep item). (d) **New behavioural rule** (Enrichment Scoping, full-decline flag) — if the Multi-LLM enrichment Scope Flag is `full` or `minimal` but every proposed enrichment is declined, Claude flags the mismatch with a two-option resolution (update the flag to `none`, or keep the flag and proceed with the asymmetry recorded) rather than proceeding on a heuristic. Matches PRISM's flag-over-assume stance. (e) Version History gains a one-line footnote clarifying the shared 2026-04-10 date on v1.0–v1.6 entries. Build method: `create_file` rebuild via a deterministic Python transformation script over v1.7 — ~17 discrete edits is past SP-6's `>~8 sequential` threshold, so the single-pass rebuild was the right call (the previous addendum draft's "well within SP-6 territory" counting was optimistic). No structural changes; no monitors added or removed; no SPs modified.

### v1.7.2 — 2026-04-18

**QA pass — three targeted corrections.** Minor version bump addressing v1.7.1 review feedback. (a) **Reverted two Lineage-table demotions from v1.7.1.** "Browser batching for timeouts" and "Simulation stall at a known threshold" moved back to 🟢 Active, reconciling with their unchanged 🟢 Active detailed entries (#19 and #20). v1.7.1 demoted them on the rationale "project-specific (not in PRISM)," but that rationale conflates two distinct states: a learning *qualified by newer learning* (🟡) vs a learning that is *in force as a project-level practice and deliberately scoped out of the framework* (🟢 with a note in the "Became in PRISM" column). The Status legend reads "🟢 **Active** — currently in force" — nothing about being embedded in PRISM machinery. The "Project-specific (not in PRISM)" note in the Became column already carries the scope-out signal; the status column should stay 🟢. Learning #16 remains 🟡 (its own text admits qualification — "two-file" wording superseded by single-file). No changes to detailed entries; only the Lineage table rows move. (b) **Lineage-table entry for Sequential edit stall synced to "~8-12 edits"** to match Learning #11 and SP-6's own calibration note (previously said "~12 edits," understating the observed variance). (c) **M5 trigger narrowed; quality-degradation feel-check consolidated into M12.** v1.7's M5 trigger bundled two conceptually distinct things: attachments-exceed-threshold (a measurable condition) and Layer-2-synthesis-quality-feels-degraded (a qualitative self-assessment). The latter fits M12's model — M12 already has a "Claude self-assesses quality degradation" clause — and it's about thinking-load, not attachment-load. M5's trigger is now attachments-only; the degradation clause in M12 absorbs "missed cross-references, weak pattern-finding" from what was in M5. Cleaner dimensional separation (M5 = attachments, M12 = conversation + thinking-quality), and M5's action template no longer has an awkward branch. No monitor added or removed. Build method: `str_replace` (7 non-cascading edits — within SP-6's `≤~8` threshold). No structural changes; no SPs modified; no new monitors.

### v1.7.3 — 2026-04-18

**Versioning-scope clarification.** Patch bump. Makes explicit that PRISM and the Starter use two different versioning schemes, closing an ambiguity that had gone undocumented since v1.0. **What was ambiguous:** VERSION MANAGEMENT opened with Starter-specific logic (canonical/non-canonical, major = whole number, minor = decimal) but never said the rules were Starter-scoped. PRISM's own Version History uses major.minor.patch numbering that *looks* like the same scheme. A reader absorbing canonical/non-canonical for the first time could (and did, in a review session) apply it to PRISM's own versioning. **What's now explicit:** (a) A new **"Scope of these rules"** subsection at the top of VERSION MANAGEMENT declares all rules in the section are Starter-scoped; PRISM itself uses standard semantic versioning (MAJOR.MINOR.PATCH). Table distinguishes the two schemes at a glance. Semver meanings named for a methodology file: MAJOR = breaking/structural, MINOR = additive (new Monitor, new SP, new feature), PATCH = corrections/clarifications/no behavioural change. (b) GATE-0 output template updated to render PRISM version as `v[X.Y.Z]` (was `v[X.Y]`). (c) Starter header template updated to render `PRISM v{X.Y.Z}` (was `v{X.Y}`). (d) Monitor section's self-referential "bump the PRISM version when the Monitor list changes" now names the level explicitly — adding a Monitor is additive → MINOR bump. (e) A one-line note above the Version History table points the reader to the Scope subsection. No behavioural changes; no Monitor, SP, or structural additions; numbering on past Version History rows unchanged (v1.7.1 and v1.7.2 were already correctly patch-level under semver). Build method: `str_replace` (7 non-cascading edits — within SP-6's `≤~8` threshold).

### v1.7.4 — 2026-04-18

**Subtitle simplification and context-engineering nod.** Patch bump. (a) **Subtitle** — shortened from "A Framework for Context-Disciplined, Multi-Session LLM Research and Audits" to "A Framework for LLM Research and Audits." The v1.7 subtitle made the case-for-PRISM in the title itself (two distinct claims: context-discipline, multi-session); durable subtitles orient rather than argue. "Multi-session" is also a current-LLM-landscape framing that will date as context windows grow — "LLM Research and Audits" is what it actually is. The attributes pulled from the subtitle are not lost: they're carried by the opener's one-liner ("across prompts, across sessions, and across the context limits of any single chat") and by two of the eight definitional bullets. Triple-billing stops; single placement at the level where the attributes earn their keep remains. (b) **Context-engineering nod** — parenthetical `(or context-engineered)` added to the "context-disciplined" bullet in the opener. Both phrasings were deliberate choices, and "context engineering" is the term-of-art practitioners will recognise. The file already uses "context-engineering" twice elsewhere in the opener (lines describing what Claude applies at Setup); the parenthetical makes the acknowledgment visible at the point where the phrase is first bolded rather than leaving it implicit. No behavioural change; no Monitor, SP, or structural addition. Build method: `str_replace` (4 non-cascading edits — well within SP-6's `≤~8` threshold).

### v1.7.5 — 2026-04-18

**External-review QA pass — nine hygiene items from a Gemini Pro Deep Thinking review of v1.7.1.** Patch bump. All items are schema reconciliation, portability fixes, taxonomy cleanup, and one mechanical prerequisite for an existing monitor. No behavioural changes to Gates, Monitors, or Standing Principles; no new machinery. (a) **SP-8 filename delimiter changed from pipe (`\|`) to em-dash (` — `)** for cross-platform portability. Pipe is illegal in Windows filenames and shell-active on Unix, which creates problems when projects are downloaded, scripted over, or moved between machines. Em-dash is filesystem-safe everywhere and visually unambiguous. Rationale added inline in SP-8; GATE-0 check and Delivery Folder tree updated to match. (b) **Assumption Register column header standardised to `Conflicts`** — v1.7's reconciliation claim missed that the prompt template still said `Conflicts with` while the Starter structure template said `Conflicts`, which could cause column-mismatch hallucinations at convergence. Now consistent across both. (c) **Decimal-numbering example clarified** — Version Management's example sequence line `Adaptation: new prompt P4.1 promoted` reworded to `Adaptation: P4.1 enrichment promoted` to remove ambiguity. The rule (decimals reserved for nested enrichment sub-prompts, never for injected specialist prompts) is unchanged; the example was just misleading. (d) **Status Tracker legend gains 🚫 DROPPED** — the Adaptations section explicitly permits dropping a planned prompt, but the Status Tracker legend offered no symbol for that state. Mirrors the Rerun Register's existing 🚫 cancelled. (e) **Action Log `Status` column dropped** — v1.7's Starter structure template had a 5th column on the Action Log that blurred the line with the Rerun Register (which is where live task state belongs per "Which log gets what"). The Action column already captures what was done; no residual outcome field needed. Schema now matches the log's intended role as a historical event log. (f) **Scope Decision taxonomy cleaned up** — the Setup > Scope Decision paragraph listed "Red Team, Fact Check" as example primary specialist dimensions for competitive research projects, which directly contradicted their Phase 2 definition as enrichment roles. Replaced with actual specialist lenses (Market Sizing, Pricing & Packaging, Go-to-Market, Competitive Landscape, Regulatory, Team & Org) and added an explicit note distinguishing specialist dimensions from enrichment roles. (g) **Assumption Register gains Date column** to make M8 (Stale Source) mechanically functional. M8 triggers on sources >12 months old, but nothing in the framework required sources' dates to be captured — M8 was therefore relying on the LLM to spontaneously notice dates while scanning. Date column (YYYY-MM minimum, YYYY-MM-DD if known) added to both prompt template and Starter structure; notes mention M8 as the downstream consumer. (h) **Short-project rule tightened** from qualitative "lighter touch on Rerun Register, M10 (issues rarely have deferral targets in short projects)" to concrete behavioural rule: "M10's deferral-target check is stricter — a valid SP-2 deferral target must exist in the current session or the immediately next one; otherwise scheduled explicitly in the Rerun Register or fixed in-session." Qualitative instructions degrade under pressure; concrete rules survive. (i) **P1-case escape hatch added to Discrepancy Check** in both the canonical rule (Prompt Design Principle #7) and the prompt template. If no prior findings exist (the first prompt in the sequence), the instruction is now to state that explicitly rather than fabricate prior entries to fill the table format. Closes a mandatory-format-produces-hallucinated-content failure mode. Source: Gemini Pro Deep Thinking review of v1.7.1 surfacing 14 items across QA bugs, operational edge cases, and strategic enhancements; six QA bugs and three edge-case/strategic items accepted or accepted-with-modification in this patch. Four strategic items (Layer 2 [NULL RESULT] aggregation, Layer 1 confidence upgrades from Fact Check, qualitative token-pressure bands, manual Revert Protocol) deferred to v1.8 — they add behaviour, which is a minor-level change per the semver rules codified in v1.7.3. One item (tool-agnostic caveat for SP-6/SP-7) declined as hedging against a use case PRISM doesn't target. Build method: `str_replace` (13 non-cascading edits across distinct sections — above SP-6's `≤~8` threshold on count, but structurally non-cascading because each edit sits in a different section and touches no shared state; the count-based threshold is a proxy for working-memory load, and this set doesn't produce it). New learning #33 added (external-review practice).

### v1.8 — 2026-04-18

**Minor bump — four behavioural additions deferred from v1.7.5.** All four items were accepted from the Gemini Pro Deep Thinking review of v1.7.1 but held from the v1.7.5 patch because each adds behaviour (not just correction), which triggers a minor-level bump under the semver rules codified in v1.7.3. (a) **Layer 2 [NULL RESULT] preservation.** The v1.7 [NULL RESULT] convention made "investigated, found nothing" visible inside prompt findings, but Layer 2 cold synthesis had no instruction to preserve these through to the final deliverable — standard LLM summarisation drops absences to save space. The Big Picture Synthesis step (Layer 2 template §5) now instructs preservation explicitly, with rationale: a clean Red Team, an unable-to-refute Fact Check, or a Coverage pass with no material gaps are verified absences that *increase* confidence in the thesis; dropping them silently removes that signal. Layer 2 Quality Checks (§7) gain a matching line. (b) **Layer 1 Fact Check reconciliation rules.** The framework has introduced [UNVERIFIED] tags (v1.0 era) and Fact Check enrichment (v1.0 era) for a long time, but never specified mechanically how FC results reconcile the tags. Phase 3 Layer 1 Convergence gains a new Fact Check reconciliation subsection: **Confirmed** → strip [UNVERIFIED] inline, upgrade Assumption Register confidence 🟡→🟢, append FC source; **Partially confirmed** → keep tag with caveat, confidence stays 🟡; **Refuted** → strike through the claim, trigger M7, log the correcting claim as a new Register entry (the struck-through original stays for audit trail); **Unable to verify** → tag remains, FC attempt logged in Register, confidence stays 🟡 or moves to 🔴 if FC found partial contradicting signal. Explicit framing that these mutations are *corrective* (epistemic status sharpening) and therefore safe for Layer 1, not *interpretive* (which would be Layer 2). Closes a loophole that was implicit since v1.0. (c) **Context Pressure Bands.** New shared reporting convention (🟢 Comfortable / 🟡 Getting warm / 🟠 Curate now / 🔴 Migrate) replacing specific-number reporting in GATE-0, M5, and M12. Rationale: LLMs are bad at estimating their own context usage; a specific count like "~142K tokens" *looks* precise but isn't. Qualitative bands are honest about what the estimate is worth. Thresholds: 🟢 <200K, 🟡 200–400K, 🟠 400–700K, 🔴 >700K — these are calibration points, not cliffs. The bands report *combined* working set (attachments + conversation + reasoning); M5 and M12 continue to fire on their own dimensional triggers (~300K attachments, ~500K conversation) regardless of band. Band is the combined headline; per-dimension numbers are the breakdown. GATE-0 output template, GATE-0 check #9 description, M5 action, and M12 action all updated to use the band. New GLOSSARY entry. (d) **Manual Revert pattern documented in Adaptations** — not as a formal Adaptation type, not as new machinery, just a paragraph describing the pattern. If a convergence goes wrong (hallucinated source, wrong file integrated, retracted citation), the user attaches a prior Archive/ version, Claude bumps the version *forward* (not backward — SP-8's filename discipline still applies: version number is a filename uniqueness guarantee, not a state identifier), Changelog entry is narrative and [MATERIAL]-tagged with full rationale, Rerun Register captures any canonical work from the discarded versions that needs redoing, Assumption Register and Action Log retain historical entries from the discarded period (intentional audit trail). Also notes that frequent reverts on a project are themselves a signal — M6 or M7 should have caught the upstream problem earlier. Three items deferred from Gemini's review continue deferred into future versions: none — all four accepted items are in this bump. One item (tool-agnostic caveat for SP-6/SP-7) remains declined. New learning #34 captures the overall v1.7.5+v1.8 response to external review. Build method: `str_replace` for v1.8 edits (7 non-cascading edits across distinct sections — at SP-6 threshold on count but structurally non-cascading; the count is a proxy for working-memory load, and this set doesn't produce it). Build split across two sessions due to tool-budget exhaustion in the v1.7.5+v1.8 back-to-back build — mirrors the M12 migration pattern the framework itself codifies.

### v1.9 — 2026-04-18

**Minor bump — superseded 90 minutes after ship by v1.9.1.** Shipped with two major additions: (1) `ask_user_input` UX integration + SP-9 (Silence is never consent), for decision points with clean discrete options (Setup Scope Flags with "Keep all defaults" shortcut, Enrichment Scoping per-prompt approve/decline, M10 classification, Adaptation confirmation; prose fallback when the tool isn't available); (2) LLM access Scope Flag (`claude-only` / `multi-vendor`) plus an execution envelope on the attach map with three new columns (Web Search, Deep Research mode, Recommended vendor), role-based vendor recommendations, Adaptive Thinking as a Setup-level flag, a consistency check between access and enrichment flags, and a GATE-0 surfacing check for the envelope. New learnings #36 (silence as structural temptation), #37 (role-based recs beat named-vendor), #38 (defer to platform-level flags where the platform has finer signal). **Status:** superseded by v1.9.1 in the same session — user raised second thoughts that the multi-vendor machinery was over-specified for a fluid problem domain (vendor capabilities drift on a 3-6 month cycle), too much framework surface, aging badly by design. v1.9.1 strips the vendor machinery while keeping the useful parts (SP-9, `ask_user_input`, learnings #36-38). Build method: deterministic Python transformation script over v1.8 (~20 edits across distinct sections). Entry kept in Version History as a record of the brief existence and as context for v1.9.1's walk-back.

### v1.9.1 — 2026-04-18

**Patch — walk-back of v1.9's multi-vendor machinery plus targeted additions from dogfooding and workshop.** v1.9 shipped 90 minutes before v1.9.1's build with two major additions: (1) ask_user_input + SP-9, (2) LLM access Scope Flag + execution envelope with role-based vendor recommendations + access/enrichment consistency check. Workshop session surfaced that the multi-vendor machinery was over-specified for a fluid problem domain where vendor capabilities drift on a 3-6 month cycle — too much framework surface, too much adherence risk, aging badly by design. v1.9.1 strips the machinery while keeping the useful parts as prose guidance. **Stripped:** LLM access Scope Flag (back to 5 flags, not 6); access/enrichment consistency check; vendor declaration at Setup; three execution envelope columns (Web Search / Deep Research / Recommended vendor) → replaced by single `Execution notes` prose column; GATE-0 check #11 as separate check → folded into existing attach map surfacing; `Prompt Execution Guidance` as separate Setup subsection → collapsed into a paragraph under attach map; role-based vendor recommendation system as framework machinery → replaced by Claude-generated prose recommendations at Setup; fallback language formal pattern → gone (prose is advisory, not structured); Adaptive Thinking as Setup-level field → mentioned per-prompt in execution notes instead; Adaptations trigger "LLM access flag upgrade" → gone. **Kept from v1.9:** SP-9 (Silence is never consent); ask_user_input integration across Setup Scope Flags / Enrichment Scoping / M10 / Adaptations; learnings #36 (silence), #37 (role-based recs), #38 (defer to platform). **New in v1.9.1:** SP-10 (Verify current state before recommending — dogfooded during design, reveals training staleness on fast-moving platform features); `Execution notes` single column on attach map with two output shapes (single-LLM preferred→fallback, multi-LLM independent set); Deep Research routing guidance as Setup subsection with the "Google the alphabet" anti-pattern called out; Output Quality Check with six signals split across two locations (live watch in prompt template for signal #6 preemptive scope-down, full OQC in convergence checklist with cross-reference); GATE-1 backtrace gains OQC check; soft reminder in Enrichment Scoping when enrichment is full/minimal (acknowledging multi-LLM assumes vendor diversity the user may or may not have); learnings #39 (transformation-script build method, promoted from v1.7.1/v1.9 observation), #40 (Deep Research routing), #41 (preemptive scope-down as thinkless signal), #42 (SP-10 dogfooding meta-learning). **Net effect:** framework surface reduced vs. v1.9, while adding genuinely useful capabilities (SP-10, OQC, routing guidance) that v1.9 didn't have. Build method: deterministic Python transformation script over v1.8 baseline (not v1.9 — v1.9 is superseded before meaningful use). Source: workshop session including SP-10 dogfooding run, user-provided screenshots of preemptive scope-down behaviour on Opus 4.6, user-provided summary of Deep Research routing case from a music theory platform project. Build executed in fresh session after prior session hit context pressure (textbook M12 migration — the framework eating its own dogfood).

### v1.10 — 2026-04-18

**Minor bump — union response to two external reviews of v1.7.1 plus v1.9.1 workshop additions.** Responds to a Claude Pro review and a ChatGPT Pro review of v1.7.1 (both received after v1.9.1 shipped), combined with two user-proposed workshop additions. Several items from each review were already addressed in v1.7.2–v1.9.1 (Execution Package → v1.9.1's Execution notes column; Context Pressure Bands → v1.8; SP-9 silence-is-never-consent → v1.9); v1.10 handles the remaining union plus workshop additions. Scoped as MINOR per v1.7.3's semver rules because the release adds behaviour (new Setup subsections, new GATE-0 check, new Monitor threshold model, new framework subsection). **Silent bugs fixed:** (a) Scope Flags `minimal` enrichment definition contradicted Enrichment Scoping triggers — `minimal` now strictly limits proposal to Coverage + Fact Check; Deep Research / Red Team / User Voice are proposable only under `full`, with Adaptation upgrade required mid-project. (b) Cross-prompt dependencies = no over-disabled M7 — M7 stays active (assumption conflicts can occur between independent prompts citing the same benchmark with different values); only M6 dormant. (c) Layer 2 = no over-disabled M12 — M12 stays active (conversation pressure applies to any multi-turn session, not just pre-Layer-2); only M11 and GATE-2 dormant. (d) GATE-2 terminology drift in Framework Limitations — "backtrace audit" references updated to distinguish GATE-1's backtrace (per-prompt) from GATE-2's Quality Report (project-level). **Rhetoric tightened:** Opener's "always knows where the project is" softened to "designed to recover state reliably and tell you what comes next" per review of overclaim vs. Framework Limitations' 70% blended adherence estimate. "Complete execution package" qualified as "complete execution package with best-effort guidance" to match v1.9.1's prose-based Execution notes reality. "Foolproof per prompt" retained per user decision. Wharton persona-prompting 3-5 pp citation softened to unquantified "factual accuracy on knowledge benchmarks" — the specific figure wasn't easily verifiable from accessible summary pages (external review finding) and the figure isn't load-bearing for the design decision it backed (lens framing over persona assignment, settled since v1.6). Citations retained. **Architectural hardening:** (1) New Runtime Profile subsection at Setup — declares Host, effective context budget, file ops availability, conversation history search availability, delivery mechanism. Enables graceful behavior across hosts and percentage-based threshold calibration. Recorded in Starter's Prompt Strategy section via new Runtime Profile template field. Can be changed mid-flight via Adaptation if user switches surfaces. (2) Percentage-based M5/M12 thresholds (30% / 50% / 70%) replacing absolute-only 300K/500K/700K — reference absolute figures shown for 1M (default) and 200K (common paid plan) as calibration anchors; 500K derived by halving 1M columns. Context Pressure Bands table gains percentage column and two absolute-reference columns; M5/M12 trigger and action templates reference both percentage and absolute; GLOSSARY M5 and M12 entries, Monitor Sweep M12 and M5+M12 rows, Context Pressure Bands trailing paragraph, M5 "Combined with M12" note, M12 "Combined with M5" guideline all updated for consistency. Historical Version History entries retain their original absolute-threshold wording as audit trail. Learning #22 tightened from "1M tokens on current Claude models" blanket to specific-surface language with percentage-based adaptation. Status moved to 🟡 Qualified. (3) Execution notes minimum content — the coverage rule tightened from "(as applicable per prompt)" to "must cover all four topics, per prompt", with a clarifying paragraph about default coverage and GATE-0 verification. GATE-0 check #11 added (returned after v1.9→v1.9.1 walkback, simpler form) verifying coverage at prompt-handoff session start. GATE-0 Pass output template gains execution-notes line and percentage-of-effective-context annotation on the Context line. **Workshop additions:** (1) Attachment Discipline subsection after HOW TO USE THIS FILE — documents when PRISM.md is and isn't needed (framework-running sessions yes; Phase 1 specialist prompt sessions no), reinforces atomic prompt principle, helps users manage context budget. Addresses a user-facing question that was implicit in the framework but never documented. (2) Setup session context management — M12 migration protocol applied to Setup with resumable-stage enumeration (Scope Flags + Runtime Profile + Discovery / Prompt Strategy outline / Execution notes + SP-10 / prompt texts / Enrichment Scoping). Handles the case where SP-10 verifications + Discovery + prompt-writing accumulate enough context to require session migration mid-Setup. Non-default; activates only when needed. **Other updates:** Setup Inputs list gains Runtime Profile bullet. Glossary gains Runtime Profile and Attachment Discipline entries. "What Claude produces" Prompt Strategy bullet and v0 Changelog example updated to mention Runtime Profile. GATE-0 check #9 description references percentage-of-effective-context. New Learning #43 — external-review cycle caught issues that seven releases of internal review missed (v1.7.2 through v1.9.1); reinforces Learning #33. Also captures the prose-vs-structure tension resolution on Execution notes: v1.7.1 no structure → v1.9 over-structured → v1.9.1 prose → v1.10 required-content-in-prose as settling point. **LLM compatibility notice** added to HOW TO USE THIS FILE (late addition during build, user-proposed): PRISM is designed for Claude; the methodology transfers to any capable LLM but the session-management machinery (`present_files`, `create_file`, `str_replace`, `conversation_search`, `ask_user_input`, Claude Skills) doesn't; non-Claude users point to the Runtime Profile's `Host = other` graceful-degradation path. Helps users running other LLMs recognise the mismatch before attaching the file. **Source:** two external reviews of v1.7.1 (Claude Pro and ChatGPT Pro) delivered after v1.9.1 shipped, plus v1.9.1 workshop session. Two triage handoffs produced from these reviews were converged for this build after user authorisation to bump to v1.10 if warranted by the union's scope. **Build method:** deterministic Python transformation script over v1.9.1 baseline (~30 non-cascading edits across distinct sections — well past SP-6's `≤~8` count threshold, but the count is a proxy for working-memory load and this set doesn't produce it since each edit sits in its own section). Net growth: ~70-100 lines (Runtime Profile, Attachment Discipline, Setup fail-safe are documentation-heavy; other edits are near-zero-net). No new SP; one new GATE-0 check; percentage-based thresholds are a parameterisation of existing M5/M12 monitors, not new Monitors.

### v1.10.1 — 2026-04-18

**Patch — LLM compatibility notice activated and opened to contribution.** The Change 21 blockquote added in v1.10 sat in HOW TO USE THIS FILE as passive documentation: any LLM reading the file would absorb it as context, but without an explicit directive no LLM could be relied on to surface it to the user at session start. A non-Claude user arriving fresh to PRISM would therefore not see the compatibility warning unless they happened to read the file directly. v1.10.1 expands the notice in two ways. (a) **LLM-facing directive.** A second blockquote paragraph now tells the LLM reading this file, explicitly, to surface the compatibility notice at the start of the first session if the LLM is not Claude, and not to skip on the assumption the user has already read the file. Most LLMs follow embedded operating-document instructions when they're clear and early; this converts the notice from passive to active. Compliance isn't guaranteed — PRISM can request, not enforce — but the directive is low-ambiguity and any reasonable LLM should honour it. (b) **User-facing contribution invitation.** A third blockquote paragraph invites users running PRISM on another vendor to have their LLM adapt the Claude-specific machinery (`present_files`, `create_file`, `str_replace`, `conversation_search`, `ask_user_input`, Claude Skills) to its environment, and to share working ports, patches, and "here's what broke" notes back. Most Claude tool calls have equivalents on GPT / Gemini / Mistral / other platforms; some need prose workarounds. Framing is open-source stance: cross-vendor adaptations are the kind of contribution the framework grows through, and welcoming them explicitly is cheaper than assuming they'll happen. No behavioural change for Claude — Claude already surfaces GATE-0 output at session start, so the new directive is a no-op on the primary target. No new machinery, no new Monitor, no new SP. Patch per v1.7.3 semver: corrections/clarifications with no behavioural change for the primary target. Build method: `str_replace` (3 edits — header version bump, notice expansion, Version History row — all non-cascading, well within SP-6).

### v1.10.2 — 2026-04-18

**Patch — markdown table rendering fix.** A single blank line at row 1980 (between the v1.7.5 and v1.8 rows of the PRISM Version History table) was silently terminating the table in most markdown renderers, causing every entry from v1.8 onward to render as plain text instead of as table cells. On mobile Claude.ai the effect was stark: the v1.7.5 cell rendered in a single very-narrow column while v1.8 through v1.10.1 rendered as full-width prose below the broken table. Desktop renderers are more forgiving of the break but still inconsistent. **Root cause:** the blank line was introduced during the v1.8 build when the v1.8 row was inserted after the v1.7.5 row via `str_replace`; the replacement pattern concatenated an extra newline between the v1.7.5 row's closing delimiter and the v1.8 row's opening delimiter — two newlines where one was needed — inserting a blank line inside the table. Markdown tables terminate on any blank line, so everything below the blank rendered as prose. **Shipped silently through v1.8, v1.9, v1.9.1, v1.10, and v1.10.1** — five releases — until a user reviewing v1.10.1 on Claude.ai mobile sent a screenshot showing the v1.8 row below a broken table. Five releases of regular verification (grep-based checks, adherence spot-checks, structural section-header scans) did not catch it because none of them scanned for blank lines *inside* tables. **Fix:** single `str_replace` removing the blank line between the v1.7.5 and v1.8 rows. No content changes; no behavioural changes; no impact on any historical entry's wording. **Mitigation against recurrence:** new Learning #44 captures the "verify table integrity post-edit" rule — any build that touches a table (adding rows, reordering, editing cells) must scan the table for blank lines before delivery. Preferred implementation is a small awk pass (as was used to diagnose this bug) scanning every file section that opens with a table header until it closes. Adopting this as a default build-verification step closes the gap. Build method: `str_replace` (4 non-cascading edits — header version bump, blank-line removal, Version History row, Learning #44). Within SP-6.

### v1.10.3 — 2026-04-18

**Patch — v1.10.2's own documentation was itself markdown-hostile.** v1.10.2 fixed a table-break (blank line between rows) but introduced a second, more severe table-break in the process: its own Version History cell contained backtick code spans that held literal pipe characters, describing the broken and fixed byte sequences. Pipes inside code spans inside table cells is a known-fragile construct; parsers disagree violently on how to interpret them. Three renderers, three different failure modes on the same file: Claude.ai web rendered the row but squeezed into a single narrow column (garbled); a standalone markdown viewer app silently dropped the entire Version History table (no error, content just missing); the Claude mobile app crashed the file view on open (hard fail). The specific combination had never appeared in PRISM's file before, because no prior Version History entry had ever needed to describe the table's own syntax using code-span examples. Novel pattern, novel failure — caught within hours because the mobile crash was dramatic. **Fix:** rewrite the problematic sentence in prose, describing the byte-sequence difference in words rather than showing it as code spans. All technical content preserved; only the representation changed. Learning #44 extended to cover both table-break failure modes (blank-line-inside-table, pipes-inside-code-span-inside-cell) alongside the existing mitigation pattern. Build verification should now scan for both. **Three-patch sequence worth noting.** v1.10.1 activated the compatibility notice, v1.10.2 fixed a five-release-old blank-line table-break, v1.10.3 fixed a rendering bug that v1.10.2's own documentation introduced. Each patch was small and cleanly scoped; the cost of not catching the underlying rendering fragility at v1.10's build was three sequential patches to reach a file that renders cleanly across web, mobile, and standalone viewers. Also: practical rule surfacing from the cycle — when describing markdown syntax *inside* a markdown file, prefer prose to literal code-span examples whenever the example would contain table-hostile characters. The meaning is preserved; the failure mode is not triggered. Build method: four `str_replace` edits (header version bump, v1.10.2 entry prose rewrite, Learning #44 rewrite, v1.10.3 row added). Within SP-6. No behavioural change; pure rendering-correctness patch.

### v1.10.4 — 2026-04-18

**Patch — Version History restructured from table to heading-based format for mobile renderer compatibility.** v1.10.2 and v1.10.3 crashed the Claude.ai mobile app on file open despite v1.10.1 opening cleanly. Binary scan (UTF-8 integrity, BOM, CRLF, control characters, invisible Unicode codepoints) returned clean — no encoding corruption, no tool-introduced noise. Content-level comparison between v1.10.1 and v1.10.3 isolated the Version History table as the likely cause. In v1.10.1 the table was broken at the v1.7.5/v1.8 boundary by the v1.8-era blank-line bug (documented in Learning #44(a)), so only roughly 7 rows ever rendered as table cells; rows v1.8 through v1.10.1 rendered as plain prose. v1.10.2's blank-line fix restored the full table, and every subsequent patch added more rows. Each row's Changes cell contains 2-7KB of heavily-nested markdown (bold, italic, code spans, parenthetical enumerations). Mobile renderers apparently have a memory or DOM-complexity ceiling for tables with many long cells; v1.10.1 never crossed it because the table was always partially broken, while v1.10.2 onward did. The three-renderer failure pattern (Claude.ai web rendered with visual glitches; standalone markdown viewer silently dropped the table; Claude.ai mobile hard-crashed) is consistent with each renderer hitting its complexity ceiling at a different threshold. **Fix:** convert the Version History section from a single table into a series of H3 headings followed by paragraph body — one heading per version, with the date inline in the heading. Same information, same order, same audit trail; no table structure to stress the renderer. Each version is now a first-class section with its own anchor, which also improves navigation for long reads. Every historical entry's text is preserved exactly — only the surrounding markdown wrapper changes from `| row |` to H3 + body. **Three-patch sequence culminating here:** v1.10.2 fixed the blank-line bug, v1.10.3 fixed a pipe-in-code-span regression introduced by v1.10.2's own documentation, v1.10.4 addresses the underlying fragility (table-with-many-long-cells) rather than treating symptoms. **New Learning #45** captures the rule: for release-notes-style content that grows unboundedly, prefer heading-based format over tables — cumulative table complexity is a fragile construct across mobile renderers regardless of whether any individual cell is correct markdown. Tables remain appropriate for true tabular data elsewhere in the framework (Scope Flags, Monitor Sweep, Context Pressure Bands, etc.) where cells are short and regular. **Honest uncertainty:** the exact mobile-crash cause isn't conclusively proven; the heading restructure is the most likely fix, and if it doesn't resolve it the restructured file is a cleaner base for further diagnosis than the table form was. **Build method:** deterministic Python transformation (Learning #39 pattern) — reads v1.10.3, extracts and parses every VH row, reformats as H3 headings, writes v1.10.4. Single pass, 20 non-cascading transformations. Switching back to Python for this work in part because the user observed the crashes emerging coincident with `str_replace` usage; while binary scan confirmed no tool-introduced corruption, defensive tool choice costs nothing.

*The v1.0–1.6 entries share date 2026-04-10 — the framework was distilled from prior research and audit work in a single concentrated pass. v1.7 is the first evolution informed by comparative project data.*

---

*End of PRISM framework. Framework name: PRISM. Artifact name: Starter. Feed the starter, and the baking takes care of itself.*

---

*\* Why "Starter"? A sourdough starter is a living culture — you feed it, it grows, and each bake makes it stronger. Same idea here. The Starter file accumulates findings, the Learnings Register accumulates wisdom, and both get better with every project. It's also, quite literally, where every PRISM project starts.*
