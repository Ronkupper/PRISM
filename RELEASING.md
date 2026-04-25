# Releasing

How PRISM artifacts ship in this repo.

## Why versioned filenames

PRISM is distributed primarily as a **file attachment**, not via `git clone`. A versioned filename (`PRISM_v2_0_0.md`, `PRISM_lens_library_v0_9.md`) lets the file self-document its version wherever it travels — attached to a Claude chat, installed as a Claude Skill, saved to a phone, shared between collaborators. You always know what version you're working with from the filename alone, without opening the file or consulting external metadata.

The repo also keeps a **stable filename** copy (`PRISM.md`, `lens/PRISM_lens_library.md`) for anyone who wants a stable raw URL or fixed path. The stable copy is byte-identical to the version-pinned snapshot at every release tag.

## Release tracks

Three things ship from this repo, on **independent cadences**:

| Track | Stable filename | Pinned snapshot | Tag pattern | Versioning |
|---|---|---|---|---|
| Framework | `PRISM.md` | `PRISM_v{X_Y_Z}.md` | `v{X.Y.Z}` | SemVer (MAJOR.MINOR.PATCH) |
| Lens Library | `lens/PRISM_lens_library.md` | `lens/PRISM_lens_library_v{X_Y}.md` | `prism-lens-v{X.Y}` | MAJOR.MINOR (no patch) |
| Backlog | `PRISM_backlog.md` | `PRISM_backlog_v{n}.md` | *(not tagged)* | Monotonic integer |

The framework and the Lens Library are versioned and released **independently**. A Lens Library bump does not require a framework bump and vice versa. The framework declares its required Lens Library version in its attachment contract; mismatches surface at runtime via M2 (Version Drift), not at release time.

## Singleton + snapshot pattern

For framework and Lens Library, every release leaves two files on `main`:

- The **stable** file (`PRISM.md`, `lens/PRISM_lens_library.md`) — always reflects the latest release on its track.
- The **version-pinned snapshot** (`PRISM_v{X_Y_Z}.md`, `lens/PRISM_lens_library_v{X_Y}.md`) — byte-identical to the stable file at the release tag. Lets attachments self-document.

For backlog, the same pattern applies but without tagging — backlog is not a release artifact, just a persistent working surface.

## Framework release (MAJOR / MINOR / PATCH)

When `PRISM.md` advances to a new framework version (e.g. `v2.1.0`):

1. **Edit `PRISM.md`** with the new framework content. Update the version string in the document header (`# PRISM v{X.Y} — Framework operating document`) and any in-document version references.
2. **Refresh the version-pinned snapshot.** Within the same major line, delete the prior snapshot; at a major boundary, retain the prior major's terminal snapshot (see *Retention*).
   ```bash
   rm PRISM_v{old}.md            # within same major
   cp PRISM.md PRISM_v{new}.md
   ```
3. **Update `SKILL.md`** if the loader contract changed — at minimum, update the `name:` field if the major changed (`name: prism-v{N}`), and any references to `PRISM_v{X_Y_Z}.md` in the load instructions. SKILL.md tracks the framework's MAJOR.MINOR; PATCH releases typically don't require SKILL.md changes.
4. **Update `CITATION.cff`** — bump `version`, update `date-released` to today (UTC), and refresh the `abstract` if the surface changed materially (any MAJOR; most MINORs).
5. **Update `README.md`** *Current version* section: new version number, new snapshot filename link, refreshed surface description.
6. **Refresh `design/`** at MAJOR boundaries — check in the design document and specification that produced the release. MINOR/PATCH releases typically don't add to `design/`; if they do (substantial design rationale worth preserving), add but don't restructure.
7. **Commit, tag, push, release.**
   ```bash
   git add -A
   git commit -m "Release v{X.Y.Z}"
   git tag -a v{X.Y.Z} -m "Release v{X.Y.Z}"
   git push origin main v{X.Y.Z}
   ```
8. **Create a GitHub Release** at the tag (`https://github.com/Ronkupper/PRISM/releases/new?tag=v{X.Y.Z}`). Title: `PRISM v{X.Y.Z}`. Body: surface summary + calibration / report-back items + link to design provenance.
9. **Post a Discussions announcement** in *Announcements* category. Title: `PRISM v{X.Y.Z} released`. Body: link to the release tag, surface highlights, calibration items worth reporting back, link to surface-drift map (Appendix D for v2.x; analogous appendix for future majors), link to `design/` artifacts at the tag. See the `v2.0.0` announcement for shape reference.

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

- [ ] Document version string updated in header and any in-document references
- [ ] Version-pinned snapshot file present and byte-identical to stable file (`diff PRISM.md PRISM_v{X_Y_Z}.md` returns no output)
- [ ] `SKILL.md` reviewed for version drift (loader instructions reference current snapshot filename)
- [ ] `CITATION.cff` version + date + abstract current
- [ ] `README.md` *Current version* section current
- [ ] `design/` updated if MAJOR
- [ ] Commit signed (`gpg.format=ssh`, `commit.gpgsign=true`)
- [ ] Discussions announcement drafted (post after tag push and Release creation)
