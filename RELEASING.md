# Releasing

How PRISM versions ship in this repo.

## Why tag

The repo keeps only the *current* version of `PRISM.md` on the `main` branch; past versions are recovered by checking out their git tag. Without tags, old versions are lost the moment a new release overwrites the file.

## Initial push (v1.10.4, once)

After the first `git push -u origin main` at repo creation:

```bash
git tag -a v1.10.4 -m "Initial public release: PRISM v1.10.4"
git push origin v1.10.4
```

The tag should then appear at `https://github.com/<user>/prism/releases/tag/v1.10.4`.

## Future version bumps

When `PRISM.md` is updated to a new version (e.g. v1.11.0):

1. Edit `PRISM.md` with the new framework content.
2. Refresh the versioned copy:
   ```bash
   rm PRISM_v{old}.md
   cp PRISM.md PRISM_v{new}.md
   ```
3. Update the README's **Current version** section with the new version number and filename link.
4. Commit, tag, push:
   ```bash
   git add -A
   git commit -m "Release v{new}"
   git tag -a v{new} -m "Release v{new}"
   git push origin main v{new}
   ```

Backlog files (`PRISM_backlog.md` / `PRISM_backlog_v{n}.md`) follow the same refresh pattern but are typically not tagged — just pushed to `main`.

## Recovering a past version

```bash
# Write the file to a temp location without checking out the tag:
git show v1.10.4:PRISM_v1_10_4.md > /tmp/PRISM_v1_10_4.md

# Or check out the whole repo state at a tag:
git checkout v1.10.4
```
