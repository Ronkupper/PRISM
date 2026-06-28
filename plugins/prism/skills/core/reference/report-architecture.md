<!-- PRISM v2.19.0 Skill bundle (on-demand reference). Report architecture reference — the comprehensive final report skeleton + craft conventions, the interactive workbook cockpit pattern, the presentation house-style, and the reconcile-at-close checklist (Appendix K). Fetch when building or closing an engagement deliverable.
     Generated from the assembled PRISM.md — edit PRISM.md, not this. -->

## Appendix K — Report architecture (reference)
<a id="appendix-report-architecture"></a>

Reference-grade detail behind the engagement deliverable — the comprehensive
final report, the interactive workbook, and the presentation house-style. The
*rules* (the report is the deliverable of record; the close-time disciplines)
live in the closure gate (§{section.engagement-closure}) and the Decision brief
(§{section.decision-brief}); this appendix is the report skeleton, the craft
conventions, the workbook cockpit pattern, and the reconcile-at-close checklist.
In the Skill archive it is the `reference/report-architecture.md` bundle, fetched
when building or closing an engagement deliverable.

### K.1 The comprehensive final report — the deliverable of record

Every engagement concludes with **one comprehensive final report** reflecting
**all** the work — every dispatch-register pass / evidence area — in plain
English, optimized for **executive scanning**: a tight readable body + curated
appendices, never a thin verdict-only or summary-only close. A summary-only
close strands the engagement's real value (the per-pass findings, data, tables)
in internal artifacts the audience never sees and under-represents the work; the
report is the engagement's deliverable of record and must carry the whole
engagement. Conventions:

- **One report per engagement, all work reflected.** Every dispatch-register
  pass / evidence area appears; nothing material is left only in the Master or
  `outputs/`.
- **Plain English, executive-scannable (§{principle.SP-17}).** Verdict +
  decision up front; clear headings; summary-first; skimmable. Built for the
  decision-maker / client audience, assumed non-PRISM — jargon stripped, with a
  glossary; each edition self-contained (§{principle.SP-20}).
- **Tight body + comprehensive curated appendices.** A readable main body plus
  one appendix per pass / evidence area — **comprehensive in coverage, curated
  in form** (plain language; actual findings / data / tables, not one-line
  glosses). The body cross-references each appendix; a heavy artifact lives in
  full in its appendix with a compact version + cross-ref in the body.
- **Build discipline (heavy pass).** Fan out clean-context sub-agents, one per
  appendix (§{section.roles-context-tier}) — each returns a curated,
  citation-bearing section; the parent owns the spine + cross-links. Build →
  render → validate are clean migration seams (manage the context band).
- **PRISM attribution — a linkable credit.** The report cover / method line
  names PRISM as the method and **links it to the framework repo** (a "Created
  with PRISM" credit that both attributes the work and gives the reader a path
  to the framework) — on **every** report, not only the share-archive Index /
  README.
- **Methodology & disclosures (plain-language "how we worked").** A body section
  that translates the framework's rigor into audience-facing trust: multi-vendor
  reconciliation (verdict-critical passes run on several independent systems,
  agreement *and* divergence recorded — §{principle.SP-15}); independent
  validation (a separate reviewer whose only context is the deliverable, with a
  from-scratch recompute — §{section.independent-validation-dispatch});
  findings vs scenarios kept strictly separate (a verified finding vs a fenced
  modelled scenario — §{principle.SP-18} + §{section.prompt-body-convergence-provisions});
  evidence and confidence as separate axes
  (§{section.prompt-body-convergence-provisions}); and interim-by-honesty (gaps
  marked open, not filled with assumption, with exactly what closes each —
  §{principle.SP-12}).
- **Validation target.** The artifact the Independent Validation Dispatch
  (§{section.independent-validation-dispatch}) validates is the **complete**
  report (body + appendices), not a summary; the complete report is also what the
  close shares.
- **Version discipline (bump atomicity for deliverables).** Every content change
  to the versioned report — *including cosmetic and text corrections* — bumps its
  revision (§{section.bump-atomicity-routine}); the **shipped revision must equal
  the validated revision**; keep exactly one current file per revision. Front-load
  the disambiguating version token in the filename so a file-picker "…" truncation
  cannot hide it (the session-name front-loading principle generalized to
  filenames).

### K.2 Canonical body architecture (verdict-first)

The recommended default skeleton — adapt section names per engagement:

1. **Title + cover / meta block** — a plain-language title (a sentence, not a
   code), "Prepared for", date, and the method / attribution line (the PRISM
   credit, K.1).
2. **Table of contents.**
3. **"How to read this report"** — a short reader-onboarding.
4. **Executive summary — verdict FIRST:** the decision(s) under test, the verdict
   on each, and the single most-important fork in one line.
5. **Highlights band** — an at-a-glance strip of the landscape + key findings.
6. **One body section per decision track / major question** — each running
   *decision under test → verdict → risk register leg-by-leg → supporting
   picture*; heavy artifacts appear compact with a cross-ref to their full
   appendix.
7. **Open items — and how the reader's answers move the verdict**
   (interim-by-honesty made actionable).
8. **Update path** — what closes each open leg / how the report reaches final.
9. **Methodology & disclosures** (K.1) — with a **conflict-of-interest**
   sub-section and a **scope & limitations** sub-section.
10. **Appendices** — the methodology / registers appendix **first** (below), then
    one appendix per pass / evidence area.

**The methodology / registers appendix ("how this was built").** Exposes the
PRISM scaffolding in plain language as a dedicated lead appendix: the **four Setup
artifacts** (§{section.setup-artifacts}) — decision brief, stakeholder register,
claim inventory, jurisdiction map — plus the **Decision-brief falsifier
registers**, a fuller **Methodology**, a **conflict-of-interest disclosure** (the honesty controls,
stated **positively** — §{principle.SP-16}), an **evidence & source index**
(every research pass → its provenance), and a **glossary**. Turns the audit's own
rigor into audience-facing trust instead of leaving it in the Master.

### K.3 Craft conventions

Each recurred throughout the finished engagement report; codified so a future
report carries them by construction, not by re-derivation:

- **Per-section "in one breath" takeaway.** Every verdict, finding, and dense
  appendix opens with a one-sentence plain takeaway — section-level
  executive-scannability, distinct from the document-level summary-first rule.
- **"How to read this …" orientation on every complex artifact.** The report,
  each dense appendix, and each notation system open with a brief orientation; a
  reader is never dropped into a dense table or a glyph system without a legend.
- **A published status-glyph legend (the "Harvey balls").** A consistent visual
  vocabulary — ● full / yes · ◐ partial · ○ none — for capability / coverage /
  severity, **always** introduced with its legend on first use and decoded again
  in the glossary. Two qualifiers ride alongside and stay **separate axes**
  (§{section.prompt-body-convergence-provisions}): **Confidence** (LOW / MEDIUM /
  HIGH) and **Verification status** (verified / could-not-verify). Evidence-vs-
  confidence separation is not merely stated; it is rendered.
- **Findings vs. scenarios fenced VISUALLY.** Every modelled / simulated figure
  carries a visual scenario tag, so a modelled number cannot be misread as a
  finding at a glance — the visual-channel complement to the §{principle.SP-18} /
  §{section.prompt-body-convergence-provisions} discipline, and the positive
  production-side home for the visual-polarity channel §{principle.SP-16} names.
- **Visible recompute as a reader-facing trust signal.** The report shows its
  arithmetic and structural checks ("the boundary count: 11 = 6+2+1+2,
  recomputed") — turning the §{principle.SP-18} internal gate into a credibility
  move: a recomputed total is stated *with* its recomputation, not merely
  asserted.
- **A self-decoding glossary.** Defines not only domain jargon but the report's
  own notation — the risk legs, the trust-boundary terms, the audit passes by
  name, the label glyphs — so the deliverable is self-contained for a non-PRISM
  reader (§{principle.SP-20}).
- **Compact-in-body / full-in-appendix for every heavy artifact**, with an inline
  cross-reference tag (the body carries the read-off; the appendix carries the
  full table).

### K.4 The interactive engagement workbook (the cockpit)

When the decision turns on a **quantitative, operator-tunable core** — unit
economics, a threshold / corner case, a returns or break-even model, a
sensitivity surface — deliver the finding **also** as a live, operator-drivable
workbook: the report *states* the finding; the workbook lets the decision-maker
*explore* it against their own numbers. The trigger is narrow — at most one
workbook per engagement, on the central quantitative gate; skip it for a
qualitative decision (a workbook there is ceremony). The earned pattern:

- **Dashboard / cockpit (the one sheet the audience drives):** a small set of
  clearly-marked **editable input cells** (the operator-tunable assumptions only)
  + the engagement's **live decision gate** — the Decision brief's actual gate
  (§{section.decision-brief}), evaluating its conditions in real time, color-coded
  (green in / amber edge / red out) — + live results. It **opens at the report's
  actual case**, so it reconciles with the report on open (same gate state, same
  headline figures).
- **Supporting sheets — the finding unpacked, made live:** break-even by the
  decision's key driver; a sensitivity heat-map across the two assumptions that
  matter most (with the report's case cell outlined); and any cost / driver
  model. Each is the report's analysis made tunable.
- **Read Me** (plain-language, with guided "try this" nudges so the audience
  drives it without instruction — §{principle.SP-17}) + **Notes & Sources** (full
  provenance: every figure tied back to the report / Master).
- **Correctness contract (§{principle.SP-18}).** Every cell ties back to the
  report and re-verifies after recalc; the workbook reconciles exactly with the
  report on open; zero formula errors.
- **Posture.** A derived share artifact — operator-gated (present it; record its
  existence in the Master / *What's next*; do not auto-commit), the same posture
  as the report / archive. It joins the send-bundle (the share-modes' send shapes,
§{appendix.external-share}); it is **not** a substitute
  for the report.

### K.5 Presentation house-style (the deliverable's visual form)

Presentation is a quality axis run at close — a **closure convention, not a
Standing Principle**. The deliverable's visual form carries the same care as its
text:

- **HTML primary** (single-file, inline CSS — reads better, portable) → **PDF
  done well**: embed fonts; explicit `@page` rules + `page-break-inside: avoid` /
  `break-before` for a real page hierarchy on flat HTML; a cover page; a TOC for
  long documents; running headers / footers + page numbers.
- **Design language inspired by the engagement subject's own design system**,
  captured during reconnaissance and used at close (cross-pass inheritance).
- **Two caveats.** (1) **Order** — polish only a **validated** deliverable
  (§{principle.SP-18} / the Independent Validation Dispatch first); never beautify
  an unvalidated artifact. (2) **Inspired, not impersonating** — keep PRISM's own
  identity clear so the deliverable reads as an independent audit, not the
  subject's own self-assessment (form must not imply a false source).
- **Render hazards.** HTML→PDF transform hazards, and the §{principle.SP-18}
  standalone-figure tokenization guard for deliverable transforms, are in
  §{appendix.vendor-parsing-observations}.

### K.6 Reconcile-at-close (the codification sweep)

The discipline's *rule* is a closure-gate step (§{section.engagement-closure},
Layer 2); this is its checklist. At every engagement close, diff the finished
deliverable's structure and conventions against this appendix in **one** pass,
and codify every craft element that landed via production / operator polish but
is not yet here — the reference is reconciled against the deliverable of record,
not the reverse. This converts one-at-a-time manual catches (the
applied-but-not-codified pattern — a learning lands in an artifact, often via an
operator correction, without being codified so it recurs) into a standing
mechanism; its in-flight sibling is **catch-one → propose-a-sweep**, the standing
orchestration posture of offering a systematic pass when the operator flags one
instance. The sweep:

- [ ] Report follows the K.2 verdict-first architecture (cover → TOC →
  how-to-read → exec summary verdict-first → highlights → per-track sections →
  open items → update path → methodology & disclosures incl. COI + scope /
  limitations → appendices led by the methodology / registers appendix).
- [ ] Every verdict / finding / dense appendix opens with an "in one breath"
  takeaway; every complex artifact + notation system opens with a "how to read".
- [ ] Status-glyph legend published on first use + in the glossary; Confidence +
  Verification shown as separate axes.
- [ ] Modelled / simulated figures fenced visually; recomputed totals shown with
  their recomputation.
- [ ] Glossary decodes the report's own shorthand, not only domain jargon.
- [ ] Methodology / registers appendix exposes the Setup artifacts + methodology
  + COI + evidence / source index + glossary.
- [ ] PRISM linkable credit + the plain-language methodology & disclosures
  section are present.
- [ ] Shipped revision == validated revision (§{section.bump-atomicity-routine});
  exactly one current file per revision.
- [ ] Any craft element present in the deliverable but absent here is codified
  before the close completes.
