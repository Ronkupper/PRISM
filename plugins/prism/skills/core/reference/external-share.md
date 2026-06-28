<!-- PRISM v2.19.0 Skill bundle (on-demand reference). External share reference — one-repo-per-engagement, the de-coded share archive, operator-selectable share modes, the image-redaction procedure, and the canonical-source (read-the-repo-not-the-mirror) block (Appendix L). Fetch when preparing an external handoff.
     Generated from the assembled PRISM.md — edit PRISM.md, not this. -->

## Appendix L — External share (reference)
<a id="appendix-external-share"></a>

Reference-grade detail behind the external-share close (§{section.engagement-closure})
and the canonical-source rule that §{principle.SP-8} carries. The *principle* —
the engagement is externally share-ready by close, and every consumer reads
canonical state — lives in those sections; this appendix is the share-archive
recipe, the operator-selectable share modes, the image-redaction procedure, and
the canonical-source handoff block. In the Skill archive it is the
`reference/external-share.md` bundle, fetched when preparing an external handoff.

### L.1 One repo per engagement, externally share-ready by close

Each engagement lives in (or splits out to) its **own** repository, externally
share-ready by close: an audience-facing README for non-PRISM readers (with the
"Created with PRISM" credit linking the framework repo), descriptive de-coded
artifact filenames as a presentation layer over §{principle.SP-14}, and a passed
privacy / PII-redaction review. Rationale: repository access is per-repo, not
per-folder — a multi-engagement umbrella cannot be shared with one engagement's
client without exposing the others *and* the entire commit history. An engagement
running inside an umbrella splits out at close (subtree split / history filter)
to its own repo, under the heavier external-share redaction regime (including any
carried history).

### L.2 The share archive (the default share artifact)

Rather than sharing a repository link, produce a self-contained **archive** of
the engagement — an easier and safer one-folder handoff (no account needed) that
curates exactly what is exposed:

- **A logical curated tree** — the findings Master · the independent-validation
  panel (§{section.independent-validation-dispatch}) · research passes (each with
  its convergence + per-pass validation) · source exhibits · methodology /
  dispatch envelopes · diligence instruments.
- **De-coded descriptive filenames** as a presentation layer over
  §{principle.SP-14}, with a name-map (friendly → canonical); the repo's
  canonical names stay unchanged.
- **A root `Index.html`** that frames the depth ("N independent AI validators
  reviewed the assessment — here is the complete evidence base"), links every
  artifact, and carries a read-me-first + a redaction note.
- **Expansive — to show the rigor.** Include the full work-product (all passes,
  the validation panel, envelopes, exhibits, the findings Master), precisely to
  evidence the depth of the work.

### L.3 Share modes (operator-selectable)

Three choices the operator sets per share; the image-redaction procedure (L.4) is
the standing **invariant** across all of them:

- **Persistence** — *present-only* (a derived artifact; record its existence, do
  not auto-commit) **or** *repo-committed* (the archive folder + the `.zip`
  committed to the engagement repo).
- **Report inclusion** — the final report (HTML + PDF) *in* the archive **or**
  shipped *separately*.
- **Send shape** — a *two-file* package (report + archive) **or** a fuller
  package (e.g. report PDF + developer action items + the interactive workbook +
  the archive ZIP).

### L.4 The image-redaction procedure (the invariant)

Redaction is **share-copy-only** — the repo's canonical artifacts are never
altered. A text grep cannot see PII inside an image, so screenshot / exhibit
material needs a **visual** pass:

1. Visually inspect every screenshot for member / third-party PII.
2. For a slide deck, **rebuild it from only the PII-safe screens** — do **not**
   merely delete slides, which leaves orphaned media embedded.
3. **Content-hash-verify** each removed image is absent from the rebuilt file.
4. Add a redaction-notice cover.
5. Then text-scrub names / affiliations / contacts and verify the scrub
   (`grep → 0`).

Credentials (a PAT, a `.secrets/` store) are excluded **absolutely**; framework
instrumentation (learnings / meta-learnings / state / the inbox) is a per-share
include / exclude choice, default exclude.

### L.5 Canonical source — read the repo, not the mirror

The canonical store is the engagement **repository**; a convenience
working-folder mirror **lags by construction** (a file committed to the repo is
not auto-copied to a flat mirror). A consumer — a Builder, an Independent
Validation seat, a fresh session — that reads the mirror instead of the canonical
repo can see stale / incomplete state and infer a false defect (e.g. "specs
undelivered" when the repo held them all along). So every consumer reads from a
**fresh repository clone**, never the convenience mirror, and runs a completeness
sanity-check on entry (a known artifact / file count, a manifest — "if you see
fewer than expected, you are on the stale mirror; re-clone"). This is the
read-side complement to write-side mirror staleness, and the application of
§{principle.SP-8} (canonical authority, §{section.sp-8-narrowed-canonical-authority})
to a multi-surface engagement.
