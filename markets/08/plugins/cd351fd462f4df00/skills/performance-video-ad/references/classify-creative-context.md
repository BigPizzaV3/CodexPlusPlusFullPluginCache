# Classify Creative Context

Run this workflow after strategy lock and before Hook hypotheses.

1. Copy only source-backed values into `creative-context.json`.
2. Keep `audience_temperature` separate from `awareness_stage`: brand contact and problem awareness are different.
3. Classify decision stakes, trust requirement, brand familiarity, audience sophistication, and evidence maturity independently from `market_type`.
4. Record historical creative observations as scoped priors with result, confidence, scope, and source. Never promote one observation into a universal rule.
5. Cite the canonical source for every classification field. If a material field is unknown, keep status `DRAFT`; do not guess and do not run the resolver.
6. Set status `CONTEXT_CLASSIFIED`, then run:

```bash
node scripts/resolve-expression-policy.mjs <job-dir>/creative-context.json --out <job-dir>/expression-policy.json
```

The resolver chooses a default Expression Profile and attention boundaries. It does not approve a Hook, an Animatic, paid generation, or publication.

`market_type` is an input, never the final expression rule. High-trust B2C may resolve restrained; warm familiar B2B with proof may resolve balanced.
