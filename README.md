# PRISM

**PRISM** (Prompts · Research · Iteration · Synthesis · Master) is a structured multi-session, multi-vendor LLM-orchestrated audit and research framework. It splits a research problem into atomic specialist prompts, dispatches each where it runs best across Claude, ChatGPT, Gemini, and Perplexity, and converges their outputs into a single living document called the **Master**.

The framework ships as a single Markdown file (`PRISM.md`) that can be attached to any LLM chat or installed as a Claude Skill. It carries its own machine-readable frontmatter, lint contract, Lens Library (embedded as Appendix G), and vendor-parsing escape-hatch (Appendix H) so the file self-documents across sessions and vendors.

> **New in v2.5.0 — repo-backed persistence.** Point a PRISM engagement at a GitHub repo and it becomes the durable home for the whole engagement: your inputs, the Master, every dispatched prompt and returned report, and the running *What's next*. Any session resumes exactly where the last one left off — even a fresh chat — and you can switch surfaces freely, desktop to mobile and back, with the repo as the shared state. It's the `repo_backed` value on the persistence axis; see the [v2.5.0 release](https://github.com/Ronkupper/PRISM/releases/tag/v2.5.0).

## Quick start

The fastest path:

1. Attach `PRISM.md` (or `PRISM_v2_7_0.md` for the version-pinned copy) to a fresh Claude chat.
2. Tell Claude the problem you want to audit or research.
3. Follow the Setup probes (P1–P7), iterate against the Lens Library until you clear three-layer readiness, then dispatch atomic prompts per the *What's next* artifact.

For a worked example, see §17 of `PRISM.md`. For repository conventions (versioning, contribution channels, lint), see [`CONTRIBUTING.md`](./CONTRIBUTING.md) and [`RELEASING.md`](./RELEASING.md).

## What PRISM is for

- **Multi-vendor research and audits** where one prompt isn't enough and one vendor isn't enough.
- **Coherence across sessions**: continuous Master + *What's next* state means a session you open next week can pick up exactly where the last one closed, even on a fresh chat.
- **Mobile-first operation**: structured filenames, file-based outputs, operator hints, narrow tables, and a "What's next?" prompt are all designed for someone moving artifacts between vendor chats on a phone.
- **Explicit scope-completeness**: the Lens Library catalogs audit-scope lenses and grades the draft Prompt Strategy against them at Setup, so silent omissions surface before any prompt ships.

The framework runs on any capable LLM — Claude is the primary reasoning and build environment, with ChatGPT, Gemini, and Perplexity used in deliberate multi-vendor triangulation sequences.

## Current version

**v2.7.0** — current file: [`PRISM.md`](./PRISM.md). v2.7.0 is a MINOR over v2.6.0: it adds **recommended-sources-on-lens**, an optional `recommended_sources:` field on the Lens Library that attaches a framework-curated list of external reference sources — each with a mandatory framing and recency caveat — to a lens's material question. It is populated on two high-yield lenses, LL-D-008 ("Compared to what?", competitive substitution) and LL-D-009 ("Does it pay back?", commercial viability), and absent on the rest. The embedded Lens Library (Appendix G) and its standalone mirror both advance to v0.12. The field is additive and backward-compatible — it carries no behavior change at this release; the consuming build that auto-populates the corpus-access Envelope from this field follows next. The version-pinned snapshot at this tag is [`PRISM_v2_7_0.md`](./PRISM_v2_7_0.md) (byte-identical to PRISM.md at the v2.7.0 tag); previous versions are available via git tags per [`RELEASING.md`](./RELEASING.md).

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

The **PRISM lint catalog** ([`lint_rules.md`](./lint_rules.md)) is the contributor-facing reference for what's checked mechanically on PRs. Two rules active at `lint-v1`: `PRISM-LINT-01 / named-refs-resolve` (error) and `PRISM-LINT-02 / named-refs-orphan-anchor` (info). Five reserved slots activate as their dependencies ship.

## Repository contents

- `PRISM.md` — current framework version (singleton: framework body + Lens Library embedded as Appendix G + skill frontmatter; stable filename, always up to date).
- `PRISM_v{n}.md` — versioned snapshot of PRISM.md at the corresponding tag (e.g., `PRISM_v2_7_0.md`); for git-tag recovery per [`RELEASING.md`](./RELEASING.md). Not the primary install target.
- `PRISM_v1_10_4.md` — terminal v1.x release retained at root for projects pinned to v1.10.4.
- `SKILL.md` — standalone skill loader (frontmatter only); use as an alternative to the fused `PRISM.md` when a decoupled skill / body layout is preferred.
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
