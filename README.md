# PRISM

**PRISM** (Prompts · Research · Iteration · Synthesis · Master) is a structured multi-session, multi-vendor LLM-orchestrated audit and research framework. It splits a research problem into atomic specialist prompts, dispatches each where it runs best across Claude, ChatGPT, Gemini, and Perplexity, and converges their outputs into a single living document called the **Master**.

The framework comes in two forms built from the same source: a single Markdown file (`PRISM.md`) you attach to any LLM chat, and a **Claude Skill plugin** that installs a lean core and fetches reference material on demand. The single file carries its own machine-readable frontmatter, lint contract, embedded Lens Library (Appendix G), and vendor-parsing escape-hatch (Appendix H) so it self-documents across sessions and vendors; the Skill is a verified, deterministic projection of that same content. See [Which form should I use?](#which-form-should-i-use).

> **New in v2.9.0 — installable as a Claude Skill.** PRISM now ships as a Claude plugin that loads a lean core and fetches reference material (the Lens Library, templates, appendices) only as a task needs it, alongside the single-file form. Install with `/plugin marketplace add Ronkupper/PRISM` then `/plugin install prism@prism`. The substrate declaration is also rewritten to a capability tier — Claude, Opus-class — so the framework no longer pins to specific model versions. See the [v2.9.0 release](https://github.com/Ronkupper/PRISM/releases/tag/v2.9.0).

## Orchestration and execution

PRISM separates two layers, and several things in this README make sense only once that split is clear.

**Orchestration** is the reasoning layer that runs the framework — parsing your problem, sequencing atomic prompts, grading scope against the Lens Library, and maintaining the Master across sessions. It was built and tested on **Claude (Opus-class)**. Running orchestration on another vendor's model is likely workable but is untested; a port is a welcome contribution.

**Execution** is the dispatched work — each atomic prompt sent to whichever model suits it best. Execution is deliberately **multi-vendor**: routing prompts across Claude, ChatGPT, Gemini, and Perplexity in triangulation sequences is a core method, not a fallback.

So "PRISM runs on Claude" (orchestration) and "PRISM uses several vendors" (execution) are both true — they describe different layers. The two distribution forms below, and the vendor notes throughout, all concern the *orchestration* layer.

## Quick start

On Claude, install the Skill (recommended):

```
/plugin marketplace add Ronkupper/PRISM
/plugin install prism@prism
```

Invoke PRISM and it activates on its own. On any other vendor — or if you'd rather use one file — attach `PRISM.md` (or `PRISM_v2_9_0.md` for the version-pinned copy) to a fresh chat. Either way:

1. Tell the model the problem you want to audit or research.
2. Follow the Setup probes (P1–P7), iterate against the Lens Library until you clear three-layer readiness, then dispatch atomic prompts per the *What's next* artifact.

For the full comparison, see [Which form should I use?](#which-form-should-i-use).

For a worked example, see §17 of `PRISM.md`. For repository conventions (versioning, contribution channels, lint), see [`CONTRIBUTING.md`](./CONTRIBUTING.md) and [`RELEASING.md`](./RELEASING.md).

## What PRISM is for

- **Multi-vendor research and audits** where one prompt isn't enough and one vendor isn't enough.
- **Coherence across sessions**: continuous Master + *What's next* state means a session you open next week can pick up exactly where the last one closed, even on a fresh chat.
- **Mobile-first operation**: structured filenames, file-based outputs, operator hints, narrow tables, and a "What's next?" prompt are all designed for someone moving artifacts between vendor chats on a phone.
- **Explicit scope-completeness**: the Lens Library catalogs audit-scope lenses and grades the draft Prompt Strategy against them at Setup, so silent omissions surface before any prompt ships.

Orchestration is built and tested on Claude; execution spans Claude, ChatGPT, Gemini, and Perplexity in deliberate triangulation (see [Orchestration and execution](#orchestration-and-execution) above). Porting orchestration to another vendor is untested but likely, and contributions are welcome.

## Which form should I use?

Both forms carry the identical framework — the Skill is a verified, deterministic projection of `PRISM.md`, not a different version or a subset. Choose by where you're running it.

**Use the Skill plugin (recommended) when you're on Claude.** It installs once and activates automatically whenever you invoke PRISM, loading a lean core (~3,400 lines) and fetching reference bundles — the Lens Library, the templates compendium, the appendices — only when a task actually needs them. The advantages compound: far less sitting in context each session, faster and more responsive turns, automatic triggering so there's nothing to attach, and headroom to grow — the framework can keep expanding without every session paying for the whole thing up front. Install:

```
/plugin marketplace add Ronkupper/PRISM
/plugin install prism@prism
```

**Use the single file (`PRISM.md`) when:**

- You're orchestrating on a non-Claude vendor. The Skill is Claude-only; on ChatGPT, Gemini, or Perplexity you run PRISM by attaching the single file (porting orchestration as needed — see [Orchestration and execution](#orchestration-and-execution)).
- You want the whole framework in one artifact — for citation, offline reading, sharing with a collaborator, or a stable raw URL.
- You're moving fast on mobile and just want to attach a single file.

The single file keeps the Lens Library embedded (Appendix G), so a lone `PRISM.md` attachment is fully self-sufficient. The Skill drops that embedded copy and points to the bundled Lens Library instead — the same catalog, fetched on demand. The Skill is specific to Claude's plugin format; the equivalent on other vendors (a Custom GPT, a Gem) would mean rebuilding PRISM in that format, which is contribution territory rather than something provided here.

## Current version

**v2.9.0** — current file: [`PRISM.md`](./PRISM.md). v2.9.0 is a MINOR over v2.8.0, two additive and behavior-preserving changes. First, **SP-13 (substrate declaration) is rewritten to vendor + tier**: PRISM declares its orchestration substrate as Claude, Opus-class / flagship tier — a capability floor, version-agnostic, latest by default — rather than enumerated model versions, removing the version-halt so it runs on the latest Opus. Second, **the framework is decomposed into a Skill archive**: a lean always-loaded core plus on-demand reference bundles (the Lens Library, the templates compendium, and the appendices), packaged as a Claude Skill plugin under [`plugins/prism/`](./plugins/prism). The canonical [`PRISM.md`](./PRISM.md) remains the assembled single-file form; the packaged core references the standalone bundled Lens Library and drops the embedded copy. This release also consolidates the Standing Principles into one canonical home (the former Appendix F folds into §10) and adds cross-file named-reference linting. The version-pinned snapshot at this tag is [`PRISM_v2_9_0.md`](./PRISM_v2_9_0.md) (byte-identical to PRISM.md at the v2.9.0 tag); previous versions are available via git tags per [`RELEASING.md`](./RELEASING.md).

**Previous version:** v1.10.4 ([`PRISM_v1_10_4.md`](./PRISM_v1_10_4.md)) — terminal on the v1.x line. Projects under v1.10.4 remain on v1.10.4; v2 supersedes for new work.

### Why versioned filenames?

PRISM is distributed primarily as a **file attachment**, not via `git clone`. The versioned filename lets the file self-document its version wherever it travels — attached to a Claude chat, installed as a Claude Skill, saved to a phone, shared between collaborators. You always know what version you're working with just by looking at the filename, without having to open the file or consult external metadata. [`PRISM.md`](./PRISM.md) is a byte-identical copy for anyone who wants a stable filename or a stable raw URL.

## Roadmap

Active proposals, deferred items, and declined ideas with rationale live in [`PRISM_backlog.md`](./PRISM_backlog.md) (versioned copy: [`PRISM_backlog_v13.md`](./PRISM_backlog_v13.md)). It's a working document — not canonical, not in force — kept separate from `PRISM.md` so the framework file stays authoritative. Useful if you want to see what's being considered, what's been decided against and why, or what's queued for the next version.

## Related conventions

PRISM is part of an emerging pattern of single-file, plain-text, versioned conventions for LLM context — different surfaces, same shape:

- **[AGENTS.md](https://agents.md/)** — open format for guiding coding agents about a specific repo. Stewarded by the Linux Foundation; in use across 60k+ projects.
- **[design.md](https://github.com/google-labs-code/design.md)** — Google Labs' format for describing a visual identity to coding agents.
- **PRISM.md** — multi-session LLM research and audit framework.

What they share: one file, dual-audience (human-readable rationale + machine-parseable structure), versioned, designed to travel with the work they describe. None of them existed two years ago.

## Related artifacts

The **PRISM Lens Library** ([`lens/PRISM_lens_library.md`](./lens/PRISM_lens_library.md)) is a reference catalog of audit-scope lenses. As of v2.0 it is required attachment to every orchestration session and is graded against the draft Prompt Strategy by the seven Setup probes.

The **PRISM lint catalog** ([`lint_rules.md`](./lint_rules.md)) is the contributor-facing reference for what's checked mechanically on PRs. Two rules active (`PRISM-LINT-01 / named-refs-resolve`, error; `PRISM-LINT-02 / named-refs-orphan-anchor`, info); catalog version 3. A companion cross-file linter extends the same rule IDs across the Skill archive's files (core ↔ bundles ↔ lens). Six reserved slots activate as their dependencies ship.

## Repository contents

- `PRISM.md` — current framework version (singleton: framework body + Lens Library embedded as Appendix G + skill frontmatter; stable filename, always up to date).
- `PRISM_v{n}.md` — versioned snapshot of PRISM.md at the corresponding tag (e.g., `PRISM_v2_9_0.md`); for git-tag recovery per [`RELEASING.md`](./RELEASING.md). Not the primary install target.
- `PRISM_v1_10_4.md` — terminal v1.x release retained at root for projects pinned to v1.10.4.
- `SKILL.md` (repo root) — the standalone single-file skill loader (frontmatter only) that pairs with `PRISM.md`; distinct from the plugin's own loader inside `plugins/prism/`. Use when a decoupled loader / body layout is preferred over the fused `PRISM.md`.
- `plugins/prism/` — the framework packaged as a **Claude Skill plugin**: a lean core (`PRISM_core.md`) plus on-demand reference bundles (`reference/`) and the bundled Lens Library, under `plugins/prism/skills/prism/`. This is the installable form; the marketplace manifest is at `.claude-plugin/marketplace.json`.
- `PRISM_backlog.md` — active/deferred/declined roadmap items. Working document, not canonical.
- `PRISM_backlog_v{n}.md` — versioned copy of the backlog (e.g., `PRISM_backlog_v13.md`).
- `lens/PRISM_lens_library.md` — canonical reference catalog of audit-scope lenses (stable filename). Authoritative for Library evolution; embedded into `PRISM.md` Appendix G for singleton-attach convenience.
- `lens/PRISM_lens_library_v{n}.md` — versioned copy of the Lens Library (e.g., `PRISM_lens_library_v0_9.md`).
- `lint_rules.md` — contributor-facing lint catalog (tag track: `lint-v{N}`).
- `scripts/lint/` — lint scripts executed by the CI workflow.
- `.github/workflows/lint.yml` — PR-only lint workflow.
- `VERSION` — single-line framework-version stamp.
- `CONTRIBUTING.md`, `RELEASING.md`, `SECURITY.md`, `CODE_OF_CONDUCT.md`, `CITATION.cff`, `README.md` — repo conventions.

## License

Framework documentation under [CC BY 4.0](./LICENSE-CC-BY-4.0.txt). Any code (lint scripts, transformations) under [MIT](./LICENSE-MIT.txt). The Code of Conduct is under [CC BY-SA 4.0](./CODE_OF_CONDUCT.md). See `LICENSE-*` files for full texts and [`CITATION.cff`](./CITATION.cff) for citation metadata.
