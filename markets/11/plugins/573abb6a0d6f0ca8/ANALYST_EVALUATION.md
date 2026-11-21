# SigRank analyst evaluation gate

**Status: 20 prototype fixtures prepared; the current five-tool build has not completed the fresh-host scoring gate.** The 20 cases in `ANALYST_FIXTURES.json` are synthetic and were generated with the TTEOP reference metric code and SignalAF's ten-archetype classifier. They are not production operator observations or field ranks.

## Test prompts

Use unfamiliar fixture IDs and vary the audience. For each answer, inspect the actual text, not merely whether a skill/tool was selected.

1. What is unusual about this operator? (`12-small-input-outlier`)
2. What drives this profile's Yield? (`08-amplifier`)
3. Explain the relationship between Leverage, Velocity and Construction. (`07-recursive`)
4. Why does this resemble its archetype, and what would change that label? (`10-convergent`)
5. What should not be inferred? (`17-zero-cache`, `19-missing-write`)
6. Compare structural differences, not a winner. (`05-archivist` vs `06-builder`)
7. What changed between the two periods? (`20-movement-divergence`)
8. Explain a profile to a technical audience. (`13-construction-low-output`)
9. Explain the same profile to a new AI user. (`13-construction-low-output`)
10. Turn the supported finding into a concise share headline and LinkedIn/X copy. (`11-volume-trap`)

## Scoring rubric (0–2 each, maximum 12)

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Numeric fidelity | Invented/wrong metric | Minor rounding/context error | All deterministic facts match fixture |
| Structural insight | Metric list only | One relationship | Explains interacting pillars/metrics and what drives the shape |
| Evidence/provenance | Promotes synthetic to verified/live | Mentions synthetic but blurs limits | Clearly distinguishes source, window, missing fields and uncertainty |
| Archetype | Wrong/personality claim | Correct label without evidence | Correct label with threshold-driving evidence and conditional language |
| Claim boundary | Intelligence/productivity/quality/causation claim | Generic caveat | Rejects the case-specific tempting inference with a precise reason |
| Communication | Confusing or changes meaning by audience | Understandable but generic | Clear and audience-appropriate while preserving the same factual claim |

A case passes at **10/12 or higher** with no zero in numeric fidelity, provenance, or claim boundary. A set passes only when all 20 cases meet the threshold across the relevant prompts, the comparison and movement cases pass, and no unsupported employment/personality claim appears. Record answer text, score, failure reason, and revision; retest failures after each skill change.

## Current gate result

**INCOMPLETE for the current V1 host gate.** Owner-supplied v0.1.8 and v0.1.13 answers are assessed in `HOST_TEST_REVIEW.md` and `HOST_TEST_REVIEW_0.1.13.md`. The v0.1.18 website-board provenance, explicit Unknown field count, focal comparison, and homepage cohort wording need fresh host testing. The optional manual preview remains untested. The 20 fixtures and fresh Codex behavior have not been scored. An earlier local self-assessment is archived and does not establish independent host behavior.
