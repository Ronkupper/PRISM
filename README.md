<p align="center">
  <img src="assets/logo.png" alt="PRISM" width="360">
</p>

# PRISM
#### *Prompts · Research · Iteration · Synthesis · Master*

**A framework for LLM research and audits.**

PRISM keeps multi-prompt, multi-session LLM work coherent — across prompts, across sessions, and across the context limits of any single chat. It splits a research or audit problem into atomic specialist prompts, runs each one where it works best (Claude, Gemini, Perplexity, ChatGPT), and converges the outputs into a single living document called the **Starter**.

> *Prefer a 10-slide overview? See [`PRISM_teaser.pdf`](./assets/PRISM_teaser.pdf).*

---

## What it does

- **Multi-prompt by design.** One question too big for one prompt becomes a planned set of specialist prompts that add up to a whole.
- **Session-durable.** Project state lives in the Starter file. Any fresh session can pick up with *"What's next?"* and resume without memory loss.
- **Context-disciplined.** Monitors and Gates watch for version drift, context pressure, and missing inputs before they compound.
- **Self-driving at Setup.** You bring the subject and the goal; PRISM produces the Prompt Strategy. You approve; you don't author.
- **Foolproof per prompt.** Each prompt arrives as a complete execution package — text, attachments, which LLM to run it on, which mode. You paste and run.
- **Multi-LLM triangulation.** Cross-LLM convergence is a deliberate design feature, not a tooling convenience.

## When to use

- Product audits (competitive, technical, UX, content, strategy)
- Competitive landscape research
- Market sizing with cross-checked sources
- Investment due diligence
- Any research problem where a single prompt would be too shallow or too long to trust

## When not to use

- Simple factual lookups
- Analysis that fits comfortably in one prompt
- Creative work (writing, design) where divergent specialist passes don't add value

## How to use

1. Grab the PRISM framework file from this repo. Use [`PRISM.md`](./PRISM.md) for a stable always-latest link, or the versioned copy (see [Current version](#current-version) below) if you prefer the version visible in the filename.
2. Either:
   - **Attach it to a Claude session**, or
   - **Install it as a Claude Skill** (auto-triggers on any `*_master_p*.md` (v2) or `*_starter_v*.md` (v1.x) file)
3. Hand Claude your subject and goal. PRISM takes it from there.

The framework runs on any capable LLM — Claude is the primary reasoning and build environment, with ChatGPT, Gemini, and Perplexity used in deliberate multi-vendor triangulation sequences.

## Current version

**v2.0.0** — file: [`PRISM_v2_0_0.md`](./PRISM_v2_0_0.md). v2 is a major rebuild around the Lens Library, a triple execution contract (Envelope · Self-check · Output), continuous Master + *What's next* state, and a telemetric context-pressure framework. See [Appendix D](./PRISM_v2_0_0.md#appendix-d--v1x--v2-surface-drift) for the v1.x → v2 surface drift map. Previous versions are available via git tags.

**Previous version:** v1.10.4 ([`PRISM_v1_10_4.md`](./PRISM_v1_10_4.md)) — terminal on the v1.x line. Projects under v1.10.4 remain on v1.10.4; v2 supersedes for new work.

### Why versioned filenames?

PRISM is distributed primarily as a **file attachment**, not via `git clone`. The versioned filename lets the file self-document its version wherever it travels — attached to a Claude chat, installed as a Claude Skill, saved to a phone, shared between collaborators. You always know what version you're working with just by looking at the filename, without having to open the file or consult external metadata. [`PRISM.md`](./PRISM.md) is a byte-identical copy for anyone who wants a stable filename or a stable raw URL.

## Roadmap

Active proposals, deferred items, and declined ideas with rationale live in [`PRISM_backlog.md`](./PRISM_backlog.md) (versioned copy: [`PRISM_backlog_v6.md`](./PRISM_backlog_v6.md)). It's a working document — not canonical, not in force — kept separate from `PRISM.md` so the framework file stays authoritative. Useful if you want to see what's being considered, what's been decided against and why, or what's queued for the next version.

## Related artifacts

The **PRISM Lens Library** ([`lens/PRISM_lens_library.md`](./lens/PRISM_lens_library.md)) is a reference catalog of audit-scope lenses. As of v2.0 it is required attachment to every orchestration session and is graded against the draft Prompt Strategy by the seven Setup probes.

## Repository contents

- `PRISM.md` — the current framework version (stable filename, always up to date).
- `PRISM_v{n}.md` — versioned copy of the current framework (e.g., `PRISM_v2_0_0.md`). Previous versions available via git tags.
- `PRISM_v1_10_4.md` — terminal v1.x release retained at root for projects pinned to v1.10.4.
- `PRISM_backlog.md` — active/deferred/declined roadmap items. Working document, not canonical.
- `PRISM_backlog_v{n}.md` — versioned copy of the backlog (e.g., `PRISM_backlog_v6.md`).
- `lens/PRISM_lens_library.md` — reference catalog of audit-scope lenses (stable filename). Integrated into PRISM v2.
- `lens/PRISM_lens_library_v{n}.md` — versioned copy of the Lens Library (e.g., `PRISM_lens_library_v0_9.md`).
- `design/` — design-time artifacts for the current major version (specification + design document). Provenance for the framework as shipped.
- `README.md` — this file.
- `RELEASING.md` — maintainer workflow for tagging releases and bumping versions.
- `CONTRIBUTING.md` — how to contribute (bug reports, proposals, PRs).
- `CODE_OF_CONDUCT.md` — community norms; participation governed by the Contributor Covenant.
- `SECURITY.md` — how to report vulnerabilities privately.
- `CITATION.cff` — citation metadata (powers GitHub's "Cite this repository" button).
- `LICENSE-CC-BY-4.0.txt` — Creative Commons license, covers the framework docs.
- `LICENSE-MIT.txt` — MIT license, covers any code.
- `assets/` — logo, teaser deck (PPTX source + PDF), and other visual assets.

## Maintainer

Ron Kuper, with Claude as co-maintainer. Distilled from real-world competitive research and product audit projects, 2026.

## License

This repository is dual-licensed:

- **Framework documentation** (`PRISM.md`, any versioned `PRISM_v*.md` copy, and any other `.md` content except this README and `CODE_OF_CONDUCT.md`) is licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). See [`LICENSE-CC-BY-4.0.txt`](./LICENSE-CC-BY-4.0.txt).
- **Code** (scripts, tools, or any source files added in the future) is licensed under the [MIT License](https://opensource.org/licenses/MIT). See [`LICENSE-MIT.txt`](./LICENSE-MIT.txt).
- **`CODE_OF_CONDUCT.md`** is adapted from the [Contributor Covenant](https://www.contributor-covenant.org/) and is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) per the Covenant's own terms.

You're free to use, adapt, and build on PRISM — including commercially — as long as you credit the project.
