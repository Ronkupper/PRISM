<!-- PRISM v2.16.0 Skill bundle (on-demand reference). Vendor parsing observations (Appendix H). Reference.
     Generated from the assembled PRISM.md — edit PRISM.md, not this. -->

## Appendix H — Vendor parsing observations
<a id="appendix-vendor-parsing-observations"></a>

`[methodological | review-if: release-sweep | recommended]`

This appendix records empirical observations of how dispatched-content
vendors handle PRISM-shaped inputs (envelopes, atomic prompts, attached
artifacts). Entries are observations, not specifications: a status like
`stripped` documents what was seen on a given date, not what a vendor
guarantees. The appendix is consulted at dispatch time when shaping
envelopes for a target vendor and at release-sweep time to re-test stale
entries.

**Status taxonomy.** Status column values are drawn from a closed
vocabulary:

- **passthrough** — vendor preserves the content as-is.
- **stripped** — vendor removes the content silently from inputs (paste,
  upload, web fetch).
- **mangled** — vendor preserves the content but alters it in transit
  (re-encoding, restructuring, character substitution).
- **error** — vendor returns an error or refuses to process the content.
- **not-tested** — no observation on record; placeholder when other
  vendors in the section have entries.
- **observed-once** — single anecdotal observation; not generalizable;
  the entry exists to mark a sighting for follow-up confirmation.

**Maintenance protocol.** Entries are append-only between releases. Any
orchestration session that surfaces a vendor parsing gap creates a new
entry (or updates an existing one) under the relevant content-type
heading. At each MINOR or MAJOR PRISM release, entries with an `Observed`
date older than twelve months are re-tested or annotated `† stale`. The
appendix's maintenance surface is shared with the cross-vendor adaptation
workstream; contributions from that workstream land here as new H3
sections (new content types) or new rows in existing tables (new vendor
observations for an existing content type).

**Per-content-type sections.** Each content type is a separate H3
sub-section so per-vendor tables stay narrow and mobile-readable. New
content types are added as new H3 sections rather than as additional
columns in an existing table.

### Markdown / YAML fences in mobile-paste inputs

Behavior when an envelope sent via the mobile-app *paste* input path
contains fenced Markdown or YAML blocks (` ``` ` / `---`).

| Vendor | Status | Observed | Workaround |
|---|---|---|---|
| ChatGPT (mobile paste) | stripped | 2026-05-15 | Treat mobile paste as an unsupported input path for fenced content. Inline-expand per §{section.atomic-prompt-self-containment}; verify the envelope as received before relying on contract structure. |
| Perplexity DR | not-tested | — | — |
| Gemini DR | not-tested | — | — |
| Claude Research | not-tested | — | — |

The ChatGPT mobile observation prompted §{section.atomic-prompt-self-containment}
in v2.0.2: inline-expanded definitions of PRISM shorthand inside the
dispatched prompt body ensure semantic integrity even when fences are
silently dropped in transit. The `not-tested` rows are placeholders;
re-test at the next release sweep or when a session next dispatches
fenced content via mobile paste on those vendors.

---
