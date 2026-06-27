<!-- PRISM v2.17.0 Skill bundle (on-demand reference). Worked example flow + empirical calibration items (sections 15-16). Reference.
     Generated from the assembled PRISM.md — edit PRISM.md, not this. -->

## 15. Worked example flow
<a id="section-worked-example-flow"></a>

This section walks a complete audit through v2.0's mechanics. Subject:
hypothetical career-coaching SaaS audit ("Atlas"). Sketch, not rubric;
illustrates how the constructs chain in real use.

```
Session 1 — Orchestration. Operator: "Begin PRISM v2 audit on
Atlas career coaching SaaS. Brief attached: atlas_brief.md."

[SP-13 substrate self-check fires: Claude, Opus-class, match.]
[Setup recommendation surfaces (§8.1):]
  "Recommend creating Claude Project 'Atlas Audit'. [...]
   Proceed without? [yes/no]"
[Operator: yes, create.]

[P0.1 — Probes 6, 7, 1, 3 fire.]
  Probe 6 (Domain Reconnaissance) surveys career-coaching domain
    practice. Surfaces: ICF competencies; CLAS multicultural standards;
    APA ethics for coaching adjacent to therapy. Outputs Jurisdiction
    map (§6.4.4): US (federal) FTC + state UPL rules; EU AI Act for
    any algorithmic matching.
  Probe 1 grades against Lens Library v0.15. Initial coverage map:
    LL-U-001..005 — three covered, two uncovered. Domain triggers:
    Pack 1 (using product), Pack 4 (proving results), Pack 5 (laws).
    Pack 2 partial, Pack 6 doesn't-fire.
  Probe 3 produces Decision brief: "Should sponsor invest additional
    capital in Atlas?" Stakeholder register: founders, investors,
    current users, prospective users, regulator.
[Master P0.1 written. What's next emits: P0.2 with probe iteration.]

[P0.2 — Probes 4, 1, 2 fire. Saturation not yet reached.]
[P0.3 — Probes 1 (re-grade), 5 (falsifier) fire. Coverage saturates.
 Layer 1 clears.]
[P0.4 — Operator ratifies. P0 → P1.]
[Master bumps from p0.4 to p1.0.]

Session 2 — Orchestration. Operator: "Continue Atlas. Master
attached."

[M2 fires silent (version match).]
[Vendor Selection runs for P2.1 — efficacy claim review.]
  Refresh: confirms Claude analytical depth fits; multi-vendor not
    needed at this prompt; adversarial-style alternative not
    material.
  Recommended: Claude Opus 4.7 / standard. Dispatch rationale:
    analytical claim adjudication.
[Envelope produced. What's next emits dispatch-ready payload.]
[Operator dispatches Claude. Output returned. Reconciliation: match.]
[Layer-1 convergence ingests. Master findings section P2.1
 populated.]

[P2.2 — efficacy evidence base. Vendor Selection recommends:
  multi-vendor (equivalence) — Claude + Gemini Pro DR + Perplexity.
  Rationale: source breadth (Perplexity), long-context synthesis
  (Gemini), analytical depth (Claude).]
[Operator dispatches all three. Two return; Perplexity fails.]
[§4.4 graceful degradation: Vendor Triangulation fires at N=2;
 delta notes the live-web breadth dimension is missing.]
[What's next surfaces Perplexity re-dispatch as a candidate.]
[Operator declares "running later" on Perplexity. Status:
 scheduled.]

[Multiple sessions. M5 band 🟡 from session 4. Curation observations
 in What's next from then on. Cloud-drive saves at every session
 close. Master updated continuously.]

[Session 7. M5 reads 🟠 mid-session. Curation directive: "Active.
 Defer further Layer-1 ingestion to fresh session. Next natural
 seam: P3.1 convergence in 2 turns."]
[P3.1 convergence completes. Migration handoff produced.]
[Operator opens Session 8 fresh. Attaches handoff + Master + Library.
 Continues seamlessly.]
```

What this illustrates:

- **Setup is iterative, not waterfall.** Three or four P0 turns
  iterating against the Library before P0→P1 ratification.
- **Vendor Selection is per-dispatch.** Single-vendor on P2.1, multi-
  vendor on P2.2, decision driven by per-prompt analytical needs.
- **Asymmetric returns are absorbed gracefully.** Perplexity fails;
  Vendor Triangulation fires at N=2; the gap is named, not blocking.
- **M5's bands rise gradually.** Session 4 hits 🟡; session 7 reaches
  🟠; migration triggers at the next natural seam.
- **Migration is planning, not rescue.** Session 7 closes cleanly at
  the seam; session 8 opens fresh with full context.

---

## 16. Empirical calibration items
<a id="section-empirical-calibration-items"></a>

These items v2.0 does not fix because they require real-use signal.
Surfaces calibrate post-release on the dogfood run and operator
feedback channel.

1. **Probe iteration floors and ceilings.** Current: minimum 2, soft
   ceiling at 4. Calibrate against real Setup runs.
2. **Probe 1 *fires-maybe* operator-fatigue.** Volume of *maybes* per
   project; mitigation effectiveness of judging-LLM silent resolution.
3. **§{section.currency-maintenance-point-refresh} point-refresh fatigue.** Frequency of `stale-refresh` per
   project; threshold for advisory accumulation toward Update session.
4. **Probe 7 lens accretion path.** Lenses surfaced by domain-
   practitioner survey that aren't in the catalog. Where do they go:
   per-project Learnings Register, staging area for Update-session
   promotion, or other?
5. **Multi-vendor Self-check verification.** Verify Self-check block
   adherence on Gemini, ChatGPT, Perplexity. Currently Claude-family
   verified only.
6. **M5 band thresholds.** Volumetric thresholds (50KB / 200KB; 20 /
   40 turns; etc.) are rev. 1 draft estimates. Calibrate against real
   sessions.
7. **Update session trigger threshold.** Rev. 1 draft: 3 stale-pattern
   accumulations across 6+ months. Calibrate against real maintenance
   cadence.
8. **SP-16 negation-audit signal.** Volume of called-for /
   uncalled-for tags per Output; false-flag rate on legitimate
   contrastive framing; LL-D-019 ("Who said otherwise?") fire rate on
   document-review subjects. Calibrates Elephant-Rule strictness.
9. **SP-16-family and output-gate signal.** Intensifier and hedge
   false-flag rates on legitimate usage; step-6 recompute catch rate;
   validation-dispatch yield (findings per run that the producing
   session had passed); LL-D-020 ("Help or ammunition?") and LL-D-021
   ("Does a stranger follow?") fire rates. Calibrates family
   strictness and validation-dispatch cadence.

These ride into the dogfood run as flagged items. Telemetry on each
feeds the v2.1 minor version.

---
