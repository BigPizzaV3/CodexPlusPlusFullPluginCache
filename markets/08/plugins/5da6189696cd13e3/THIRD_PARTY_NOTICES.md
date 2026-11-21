# Third-party notices

## GLiNER.js

The token-level preprocessing and decoding in
`src/engine/gliner-edge.ts` is adapted from
[Knowledgator/GLiNER.js](https://github.com/Knowledgator/GLiNER.js), npm release
`gliner@0.0.19`, licensed under Apache-2.0.

Modifications replace the old runtime and tokenizer dependencies with this app's
shared current runtime, use the Edge model's correct special-token IDs, retain
Unicode offsets, bound overlapping chunks by actual token count, release
tensors, and preserve overlapping accepted coverage.

The full upstream license is distributed at
[`public/licenses/GLiNER.js-APACHE-2.0.txt`](public/licenses/GLiNER.js-APACHE-2.0.txt).

The upstream package does not include a separate NOTICE file.

## Inter

Inter is bundled through `@fontsource-variable/inter` under the SIL Open Font
License 1.1. Copyright 2016 The Inter Project Authors.
The full license is distributed at `public/licenses/Inter-OFL-1.1.txt`.
