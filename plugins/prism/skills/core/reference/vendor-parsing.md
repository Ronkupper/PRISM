<!-- PRISM v2.21.0 Skill bundle (on-demand reference). Vendor parsing observations (Appendix H). Reference.
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

### Heavy-line (`━`) delimiters in mobile-paste inputs

Behavior when an envelope sent via the mobile-app *paste* input path uses
`━━━` heavy-line delimiters — the PRISM dispatch-block convention
(§{appendix.dispatch-conventions}, J.2) — instead of fenced Markdown / YAML.

| Vendor | Status | Observed | Workaround |
|---|---|---|---|
| ChatGPT (mobile paste) | not-tested | — | — |
| Claude (mobile paste) | not-tested | — | — |
| Perplexity (mobile paste) | not-tested | — | — |
| Gemini (mobile paste) | not-tested | — | — |

These rows are **proactive placeholders** seeded by a queued real-device test
(calibration item 10, §{section.empirical-calibration-items}); no vendor has an
observation on record yet. The all-`not-tested` status is therefore expected, and
this section is declared a queued-test section rather than reporting a sighting —
the `━` heavy line is the dispatch convention precisely because it is
fence-collision-safe and has no recorded transport incidents (rationale in J.2,
§{appendix.dispatch-conventions}).

### Per-vendor download / export recipes

The return-handling friction is per-vendor; pre-warn the operator (an operator
hint, not an inline essay). Observed recipes:

| Vendor | Recipe |
|---|---|
| Gemini (Deep Research) | Export to Google Docs → download as `.md`. |
| Claude / ChatGPT | The session creates the file; rename the download to the SP-14 name (rename optional — the return self-IDs via `Ran on`, reconciled on the filename). |
| Grok | Writes the file to its sandbox (e.g. `/home/workdir/artifacts/`); after it saves, ask "give me a download link" to surface the `.md` — a two-step. |

These are observations, not guarantees; re-test stale entries at the release
sweep.

### Passive detection of self-report — capability + template

For the passive pre-fill pattern (§{section.corpus-access-dispatch}, *Passive
pre-fill of self-report*): the load-bearing choice is **naming the right
capability**. Passive recon is a **browse / retrieval** job — name the
Chrome-MCP / authenticated-browse surface (§{section.cowork-surface-capabilities})
plus public web records (DNS, certificate-transparency, IP-WHOIS, app-store),
per the retrieval-shape step (§{section.vendor-selection-at-dispatch}). Do
**not** route it to a synthesis / Deep-Research mode — that silently fails to
fetch. Generalized paste-ready shape:

```
Using the Chrome MCP (authenticated browse) and online web tools, passively
examine and detect as much as possible about [subject]'s stack, server
environment, and [domain of interest], and pre-answer as many of the pending
[questionnaire / self-report] items as passive observation allows. Tag each
finding [OBS] (observed first-hand) / [INF] (inferred from observed signals) /
[ask] (not passively knowable). STRICTLY passive: no scanning, no ID/parameter
manipulation (IDOR), no rate-limit / auth-bypass / upload testing, no
state-changing actions; read key *names*, never token *values*.
```

### Agentic-browser drivers + closed-document IVD seats

**Agentic-browser drivers (Comet, Atlas).** Operator-run third-party agents are
a distinct driver class from PRISM-driven Chrome-MCP
(§{section.vendor-selection-at-dispatch}); investigation-posture single-source,
never a triangulation seat. Reliability is uneven and confident prose is **not**
verified output — every claim needs first-hand confirmation (field: agents
variously asserted no-RSVP / "responsive" / "real labels", each wrong; a probe
asserted "iOS-only", also wrong). Confirm agent-mode + login are actually
engaged before relying on a run.

**Closed-document IVD seats (§{section.independent-validation-dispatch}).** For a
closed-document validation (the deliverable's own arithmetic and internal
consistency, no web), prefer **strong closed-document reasoners** as seats; in
field runs the real in-document catches came from those, while web-oriented /
breadth-first seats produced mostly already-addressed or stylistic items on the
closed-document task. Accept a valid catch from any seat (recall is the point),
but weight a web-oriented seat's *miss* on a closed-document point lightly — its
strength is live-web breadth, not closed-doc recompute.

### HTML → PDF transform hazards for deliverable builds

The engagement report's primary form is single-file HTML rendered to PDF (the
presentation house-style, §{appendix.report-architecture}). Field-observed render
hazards on a WeasyPrint-class HTML→PDF engine — pre-warn for them when building or
validating a PDF deliverable:

- **Flex translucent-background double-paint.** A flex container with a
  translucent background can paint its background twice (parent + item), darkening
  the intended tint. Put the background on a single layer, or use an opaque value.
- **Flex `space-between` title mis-size.** A `justify-content: space-between` title
  row can mis-size or clip its items in the PDF engine where it renders fine in the
  browser. Verify titles in the rendered PDF, not only the browser preview.
- **`@page` vs `html`/`body` background mismatch.** The `@page` background and the
  document background are separate; setting one and not the other leaves a margin
  band in the off colour. Set both, or neither.
- **Real page hierarchy on flat HTML.** A flat HTML document has no native pages —
  use explicit `@page` rules + `page-break-inside: avoid` / `break-before` to force
  a real cover / section / page structure, and embed fonts so the PDF is portable.
- **Orphaned media on slide / section delete.** Deleting a slide or section from a
  built deck or document can leave its media embedded; rebuild from the kept
  content rather than deleting in place, and content-hash-verify the removed media
  is gone (the §{appendix.external-share} image-redaction procedure depends on
  this).

Pair these with the §{principle.SP-18} deliverable-transform guard
(§{section.sp-18-it-must-recompute}): tokenize standalone figures only (exclude
acronym / code digits; strip tags first) so a clarity edit during the transform
does not trip a false figure-drift halt.

---
