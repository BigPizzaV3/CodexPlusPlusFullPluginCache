# Context-to-expression rules

## Resolution precedence

1. Cold, unknown-brand traffic with high trust or high decision stakes resolves to `restrained_b2b_social`.
2. High-trust B2C resolves to `restrained_b2b_social` even though the market is consumer.
3. Scoped evidence that strong visual creative underperformed shifts the prior toward `restrained_b2b_social`; keep the signal source and confidence.
4. Warm, retargeting, or existing-customer traffic with proof and brand familiarity may resolve to `balanced_social_brand` with product or proof demonstration.
5. Cold, low-stakes, low-trust B2C may resolve to `balanced_social_brand` with stronger native-format or visual candidates.
6. Ambiguous contexts resolve to `balanced_social_brand`, medium intensity, and an optional trend wrapper.

The resolver never selects `spectacle_experiment` as the portfolio default. Spectacle remains separately purpose-bound and approval-bound.

## Interpretation

`restrained` does not mean weak or slow. Move attention strength into workplace contradiction, social tension, semantic tension, or imminent consequence. Reduce decorative intensity, motion density, and simultaneous concepts while keeping source-backed semantic tension, insight strength, and emotional specificity high when the context supports them.

Resolve visual and message policies independently. A visually restrained result may still require `semantic_tension: high`, `insight_strength: high`, `emotional_specificity: high`, and `claim_certainty: calibrated`. Never treat a prohibition on spectacle as a prohibition on a strong recognition shift.

`balanced` does not mean spectacle. It permits one bounded branded transition or a clearer product/proof demonstration while retaining evidence and trust boundaries.

Treat rule output as an interpretable prior. Store `reasoning`, `confidence`, and `source_fields`; do not pretend the resolver has campaign evidence.
