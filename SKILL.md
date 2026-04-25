---
name: prism-v2
description: PRISM v2.0 — structured multi-session, multi-vendor LLM-orchestrated audit and research framework. Trigger this skill whenever the user invokes PRISM mechanics by name or by recognizable construct: PRISM audit, PRISM v2, begin a PRISM audit, Master file, any filename matching *_master_p*.md, Prompt Strategy, Lens Library, Vendor Selection, Vendor Triangulation, Setup probes or any of P1-P7 by number, Monitor M* or any of M1-M12 by number, Standing Principle SP-*, Execution Envelope, Execution Self-check, Execution Output, Dispatch register, Dispatch shape (equivalence/split/limitation-named), the What is next artifact, context band or 🟢🟡🟠🔴, migration handoff, P0/P1 boundary, three-layer readiness, Claude Project recommendation, Update session, point refresh, Setup artifacts (Decision brief / Stakeholder register / Claim inventory / Jurisdiction map). Also trigger when the user attaches a Master file or a Lens Library file. Do NOT trigger for unrelated audit work, generic prompt engineering, or v1.10.4-specific terminology like Starter, GATE-0/1/2, Scope Flags, Runtime Profile, Assumption Register — those are v1.x and v2.0 supersedes them.
---

# PRISM v2.0 framework loader

This Skill loads PRISM v2.0 — the canonical framework operating document for
structured multi-session, multi-vendor LLM-orchestrated audit and research.

## When triggered

1. Read `PRISM_v2_0_0.md` (version-pinned) or `PRISM.md` (always-current) from
   this Skill's folder, the operator's project, or the attached copy in full
   before responding to the operator's request.
2. Run SP-13 substrate self-check (§10.1.3): declare your model identity and
   confirm Claude Opus 4.6 or 4.7. Halt and ask the operator on mismatch or
   cannot-determine.
3. Run M1 (Missing Inputs, §9.1.1): verify the canonical attachments are
   present — Master, Lens Library, Prompt Strategy (if separate), subject
   brief. Halt with HIGH severity if any required artifact is missing.
4. Run M2 (Version Drift, §9.1.2): compare attached Master version to the
   version *What's next* predicted at last close. Halt on mismatch.
5. Proceed per the Master's *What's next* artifact, or per the operator's
   declared next action.

## Operating discipline

- Treat the framework document as authoritative. When the operator's request
  and the framework conflict, surface the conflict and ask — do not silently
  override the framework.
- Honour Standing Principles persistently (§10). SP-9 in particular: silence
  is never consent. SP-1: never silently regenerate canonical artifacts.
- Write Master + *What's next* at every orchestration turn-close per §5.5
  continuous-state mechanic, regardless of band.
- Apply two-axis tags (`structural | stable` etc.) to any new decision the
  framework adds during operation.
- Emit operator hints per §13 catalog only when a cue applies to the
  specific dispatch — routine turns carry no hints.

## Files this Skill expects in the Project or attached

- `PRISM.md` (always-current) or `PRISM_v2_0_0.md` (version-pinned)
- `PRISM_lens_library.md` v0.9 (canonical catalog; `prism-lens-v0.9` tag)
- `[project]_prism2.0_master_*.md` (the Master)
- `[project]_brief.md` (subject brief, at Setup)

## Relationship to PRISM.md

`PRISM.md` at the repo root carries its own skill frontmatter (`name: prism`,
v1.x fused-file pattern). This `SKILL.md` is the v2-native loader pattern
(`name: prism-v2`) — separate loader, body lives in `PRISM_v2_0_0.md`.
Either pattern works; pick whichever fits your environment.

## What this Skill does NOT do

- Does not regenerate the Master from memory if the file is missing — runs
  SP-1 protocol (§14 missing-handoff recovery).
- Does not silently substitute v1.10.4 mechanics — v2.0 supersedes v1.x
  per DD §10.1; v1.10.4 projects stay on v1.10.4.
- Does not bypass operator ratification at P0→P1 (§6.2 Layer 3).
- Does not auto-retry failed dispatches (§4.4 — surfaces re-dispatch as a
  candidate; operator decides).
