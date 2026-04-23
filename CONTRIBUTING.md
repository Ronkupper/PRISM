# Contributing to PRISM

Thanks for your interest. PRISM evolves the same way it asks users to work: through real projects surfacing gaps, with findings that feed back into the next version. Contributions are welcome on that basis.

## Channels

Four channels, roughly lightest to heaviest:

### 1. Share what you built

If you adapted PRISM for a non-Claude LLM (GPT, Gemini, Perplexity) or built tooling around it, open a [Discussion](https://github.com/Ronkupper/PRISM/discussions) under *Show and Tell* with a link and a short note on what you did, what worked, and what broke. This directly helps others in the same situation.

### 2. Report bugs or friction

Framework bug, internal contradiction, unclear section, broken link? Open an [Issue](https://github.com/Ronkupper/PRISM/issues). Include:

- What version of PRISM you're on (from the filename or the `Version:` line in the file)
- What you were trying to do
- What happened vs. what you expected

### 3. Propose changes to the framework

Check [`PRISM_backlog.md`](./PRISM_backlog.md) first — your idea may already be there as an active proposal, a deferred item, or declined-with-rationale (which is also worth reading, to see what directions have already been considered).

If it's new:

- Open a Discussion under *Ideas* with the proposal and the rationale
- If it gains traction, it moves into the backlog as an Active proposal
- When it's ready to ship, it's incorporated into the next version of `PRISM.md` per the process in [`RELEASING.md`](./RELEASING.md)

Pull requests directly against `PRISM.md` are welcome, but expect the substance of any non-trivial change to be discussed first. `PRISM.md` is the canonical framework file; changes there ship via version bumps, not commit-by-commit edits.

### 4. Minor fixes

Typos, broken links, formatting bugs, obvious grammar issues — open a PR directly, no discussion needed.

## What to avoid

- Proposals that add machinery without a clear failure mode they prevent — PRISM tries to keep surface area to a minimum
- Proposals that hardcode specific LLM vendor names into `PRISM.md` — vendor capabilities drift too fast for that to age well (see declined item "Named-vendor recommendations" in the backlog)
- Large rewrites without prior discussion — they're expensive to review and rarely merge clean

## Code of conduct

Participation is governed by the [Code of Conduct](./CODE_OF_CONDUCT.md). By contributing, you agree to uphold it.

## License

By contributing, you agree that your contributions will be licensed under the same terms as the rest of the repository (see [README](./README.md#license)). Framework documentation under CC BY 4.0; any code under MIT.
