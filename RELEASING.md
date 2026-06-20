# Releasing

How PRISM artifacts ship in this repo.

## Why versioned filenames

PRISM is distributed primarily as a **file attachment**, not via `git clone`. A versioned filename (`PRISM_v2_0_0.md`, `PRISM_lens_library_v0_9.md`) lets the file self-document its version wherever it travels — attached to a Claude chat, installed as a Claude Skill, saved to a phone, shared between collaborators. You always know what version you're working with from the filename alone, without opening the file or consulting external metadata.

The repo also keeps a **stable filename** copy (`PRISM.md`, `lens/PRISM_lens_library.md`) for anyone who wants a stable raw URL or fixed path. The stable copy is byte-identical to the version-pinned snapshot at every release tag.

## Release tracks

Four things ship from this repo, on **independent cadences**:

| Track | Stable filename | Pinned snapshot | Tag pattern | Versioning |
|---|---|---|---|---|
| Framework | `PRISM.md` | `PRISM_v{X_Y_Z}.md` | `v{X.Y.Z}` | SemVer (MAJOR.MINOR.PATCH) |
| Lens Library | `lens/PRISM_lens_library.md` | `lens/PRISM_lens_library_v{X_Y}.md` | `prism-lens-v{X.Y}` | MAJOR.MINOR (no patch) |
| Lint catalog | `lint_rules.md` + `scripts/lint/` + `.github/workflows/lint.yml` | *(no pinned snapshot)* | `lint-v{N}` | Monotonic integer (catalog version) |
| Backlog | `PRISM_backlog.md` | `PRISM_backlog_v{n}.md` | *(not tagged)* | Monotonic integer |

The framework, the Lens Library, and the lint catalog are versioned and released **independently**. A Lens Library bump does not require a framework bump and vice versa. The framework declares its required Lens Library version in its attachment contract; mismatches surface at runtime via M2 (Version Drift), not at release time. The lint catalog releases off-cycle from `PRISM.md`; its tag (`lint-v{N}`) and the `lint_catalog_version` field in `PRISM.md` frontmatter are independent integer counters that may sit at different values.

## Singleton + snapshot pattern

For framework and Lens Library, every release leaves two files on `main`:

- The **stable** file (`PRISM.md`, `lens/PRISM_lens_library.md`) — always reflects the latest release on its track.
- The **version-pinned snapshot** (`PRISM_v{X_Y_Z}.md`, `lens/PRISM_lens_library_v{X_Y}.md`) — byte-identical to the stable file at the release tag. Lets attachments self-document.

For backlog, the same pattern applies but without tagging — backlog is not a release artifact, just a persistent working surface.

The lint catalog (`lint_rules.md`, `scripts/lint/`, `.github/workflows/lint.yml`) does not have a pinned snapshot. The `lint-v{N}` tag marks the catalog state at the moment of release; later catalog edits ride on `main` and a new `lint-v{N+1}` tag is cut when the surface changes meaningfully.

## Framework release (MAJOR / MINOR / PATCH)

When `PRISM.md` advances to a new framework version (e.g. `v2.1.0`):

1. **Edit `PRISM.md`** with the new framework content. Update the version string in the document header (`# PRISM v{X.Y} — Framework operating document`), the frontmatter `version`, `released`, `supersedes` fields, the inline `Currently v{X.Y.Z}` substring inside the frontmatter `description`, the EOF marker, and any in-document version references (§18.1 project identity, §18.2 pinned-URL column, §18.3 currency example, §18.5 citation). When a release **adds or changes a Standing Principle, Monitor, Gate, or Probe**, give it the normativity marker at creation per the title-block tag convention (`[durability | review-trigger | strength? | polarity?]`) — Pattern B applies to new elements going forward, not just the legacy sweep completed in Phase B2 (v2.2.0), so the sweep never needs repeating.
2. **Refresh the version-pinned snapshot.** Within the same major line, delete the prior snapshot; at a major boundary, retain the prior major's terminal snapshot (see *Retention*).
   ```bash
   rm PRISM_v{old}.md            # within same major
   cp PRISM.md PRISM_v{new}.md
   ```
3. **Update `SKILL.md`** if the loader contract changed — at minimum, update the `name:` field if the major changed (`name: prism-v{N}`), and any references to `PRISM_v{X_Y_Z}.md` in the load instructions. SKILL.md tracks the framework's MAJOR.MINOR; PATCH releases typically don't require SKILL.md changes.
4. **Update `.claude-plugin/marketplace.json`** — bump the `version` field on the `prism` entry in `plugins[]` to match the new `plugin.json` version. This is what the Claude desktop update-checker reads; if it is out of sync the Update button stays greyed even though a newer `plugin.json` exists.
   ```json
   { "name": "prism", "version": "{X.Y.Z}", ... }
   ```
5. **Update `CITATION.cff`** — bump `version`, update `date-released` to today (UTC), and refresh the `abstract` if the surface changed materially (any MAJOR; most MINORs).
6. **Update `README.md`** *Current version* section: new version number, new snapshot filename link, refreshed surface description.
7. **Update `VERSION`** — single-line file containing the new framework version on its own line (no trailing whitespace).
8. **Refresh `design/`** at MAJOR boundaries — check in the design document and specification that produced the release. MINOR/PATCH releases typically don't add to `design/`; if they do (substantial design rationale worth preserving), add but don't restructure.
9. **Commit, tag, push, release.**
   ```bash
   git add -A
   git commit -m "Release v{X.Y.Z}"
   git tag -a v{X.Y.Z} -m "Release v{X.Y.Z}"
   git push origin main v{X.Y.Z}
   ```
10. **Create a GitHub Release** at the tag (`https://github.com/Ronkupper/PRISM/releases/new?tag=v{X.Y.Z}`). Title: `PRISM v{X.Y.Z}`. Body: surface summary + calibration / report-back items + link to design provenance.
11. **Post a Discussions announcement** in *Announcements* category. Title: `PRISM v{X.Y.Z} released`. Body: link to the release tag, surface highlights, calibration items worth reporting back, link to surface-drift map (Appendix D for v2.x; analogous appendix for future majors), link to `design/` artifacts at the tag. See the `v2.0.0` announcement for shape reference.

## Lens Library release

When `lens/PRISM_lens_library.md` advances (e.g. `v0.10` or `v1.0`):

1. **Edit `lens/PRISM_lens_library.md`** with the new content. Update the version string in the document header.
2. **Refresh the snapshot.**
   ```bash
   cd lens/
   rm PRISM_lens_library_v{old}.md       # if superseding within same line
   cp PRISM_lens_library.md PRISM_lens_library_v{new}.md
   cd ..
   ```
3. **Update `README.md`** if the Lens Library section needs revision (significant scope or surface change).
4. **Update `PRISM.md`** *only if* the framework's required Lens Library version reference needs updating (e.g., framework now requires `≥ v1.0`). This is a framework edit and triggers a framework PATCH or MINOR release on its own track — handled in a separate commit.
5. **Commit, tag, push, release.**
   ```bash
   git add -A
   git commit -m "Lens Library v{X.Y}"
   git tag -a prism-lens-v{X.Y} -m "PRISM Lens Library v{X.Y}"
   git push origin main prism-lens-v{X.Y}
   ```
6. **Create a GitHub Release** at the lens tag.
7. **Post a Discussions announcement** in *Announcements* if the release is material (new major, significant new lenses, calibration milestone). Patch-grade lens edits don't necessarily warrant an announcement — judgment call.

## Lint catalog release (`lint-v{N}`)

When `lint_rules.md`, the `scripts/lint/` scripts, or the `.github/workflows/lint.yml` workflow advances in a way that changes the catalog surface (a new active rule, a severity change, a rule retirement, output-format change):

1. **Edit the relevant files.** If a new rule activates or the catalog gains/loses entries, also bump `lint_catalog_version` in `PRISM.md` frontmatter — and ship that bump as a framework PATCH on the framework track in a separate commit.
2. **Verify locally.** Run `python scripts/lint/lint_named_refs.py PRISM.md` (zero error findings expected) and `yamllint .github/workflows/lint.yml`.
3. **Tag.**
   ```bash
   git add -A
   git commit -m "Lint catalog v{N}"
   git tag -a lint-v{N} -m "PRISM lint catalog v{N}"
   git push origin main lint-v{N}
   ```
4. **GitHub Release optional.** A Release page on `lint-v{N}` is useful when the catalog surface changes meaningfully (new active rule). Minor-script edits don't warrant a Release.
5. **Discussions announcement** only for material catalog changes.

## Backlog refresh

`PRISM_backlog.md` is a persistent working surface, not a release artifact:

```bash
rm PRISM_backlog_v{old}.md
cp PRISM_backlog.md PRISM_backlog_v{new}.md
git add -A
git commit -m "Backlog refresh: v{new}"
git push origin main
```

No tag. No Release. No Discussions post. The version-pinned snapshot exists only so an attached backlog file self-documents its revision.

## Retention rules

**Within a major line:** the prior MINOR/PATCH snapshot is deleted from `main` on the next release. It remains recoverable via its git tag. This keeps `main` from accumulating stale snapshots.

**At a major boundary:** the prior major's *terminal* snapshot is retained on `main` indefinitely. Example: `PRISM_v1_10_4.md` remained on `main` when v2.0.0 shipped, because v1.10.4 is terminal on the v1.x line and projects pinned to v1.x continue to reference it. The README *Previous version* note signals this retention.

**Lens Library** follows the same rule: prior MINOR within a major line is deleted; the terminal snapshot of a closed major line is retained.

## Recovering a past version

```bash
# Write a past version to a temp location without a checkout:
git show v1.10.4:PRISM_v1_10_4.md > /tmp/PRISM_v1_10_4.md
git show prism-lens-v0.9:lens/PRISM_lens_library_v0_9.md > /tmp/lens_v0_9.md

# Or check out the whole repo state at a tag:
git checkout v2.0.0
```

Tags are protected. Past versions are recoverable from any clone of the repo for as long as the tag exists.

## Pre-release checklist

Before pushing a framework tag:

- [ ] Document version string updated in header and any in-document references (frontmatter `version`, frontmatter `released`, frontmatter `supersedes`, frontmatter `description` inline `Currently v{X.Y.Z}`, EOF marker, §18 references)
- [ ] Version-pinned snapshot file present and byte-identical to stable file (`diff PRISM.md PRISM_v{X_Y_Z}.md` returns no output)
- [ ] `SKILL.md` reviewed for version drift (loader instructions reference current snapshot filename); description prefix matches release
- [ ] `.claude-plugin/marketplace.json` `plugins[].version` bumped to match `plugin.json` (enables the desktop Update button)
- [ ] `CITATION.cff` version + date + abstract current
- [ ] `README.md` *Current version* section current
- [ ] `VERSION` file matches frontmatter `version` and title-block heading
- [ ] **Lint gate clean** — the CI workflow at `.github/workflows/lint.yml` runs the `scripts/lint/` catalog against `PRISM.md` and reports zero error-severity findings. At v2.1.0, this is `PRISM-LINT-01` (named-refs-resolve). Active rules grow as the catalog evolves: when Pattern A's schema lands, `PRISM-LINT-03`, `-04`, `-05`, and `-07` become active. `PRISM-LINT-06` (element-marking-completeness) remains catalog-reserved at info-severity after Phase B2 (v2.2.0) — promotion to warning is a separate decision after operators live with the marked file. Info-level findings from `PRISM-LINT-02` (orphan anchors) are acceptable and do not block release.
- [ ] `design/` updated if MAJOR
- [ ] Commit signed (`gpg.format=ssh`, `commit.gpgsign=true`)
- [ ] Discussions announcement drafted (post after tag push and Release creation)
