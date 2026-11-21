# Safety, licensing, and provenance

## Scientific claims

- Treat every structure, feature interpretation, mutation score, and functional label as a model-generated hypothesis.
- Require experimental validation appropriate to the claim. Do not present a predicted structure as experimental truth, a static structure as molecular dynamics, an SAE label as established function, or a mutation score as measured fitness.
- ESMFold2 output is one static conformational hypothesis. It does not capture kinetics, ensembles, environment-dependent dynamics, binding affinity, or experimental uncertainty by itself.
- ESM Atlas coordinates are model predictions too, not experimental structures.

## Biosafety and acceptable use

Follow the [Biohub Acceptable Use Policy](https://biohub.org/acceptable-use-policy/). Biohub may restrict controlled pathogen or toxin inputs, and a tool then returns `restricted`. Do not work around those restrictions. Legitimate researchers affected by a restriction should use Biohub's elevated-access process. Open weights do not remove the user's responsibility to follow institutional, legal, and biosafety review.

## Licensing

- Released ESM model code and weights are MIT licensed; check the model card for the exact model.
- ESM Atlas data is CC-BY-4.0. Preserve attribution and the source accession in derived work.

## Provenance

On the Biohub MCP route nothing is written, so the answer is the record. End it with the source line in [Point back to the source](show-a-structure.md#point-back-to-the-source). Until the script routes are removed, their sidecars must never contain credentials or raw provider errors.
