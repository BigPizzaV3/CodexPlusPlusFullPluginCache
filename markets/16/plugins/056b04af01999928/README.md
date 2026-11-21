# Token Saver

Token Saver is an independent skills-only plugin inspired in part by ideas in [Caveman](https://github.com/juliusbrussee/caveman), an open-source project by Julius Brussee. It is not an official Caveman product and does not bundle or run the Caveman software.

This package offers conversational guidance for concise responses, meaning-preserving compression, and practical reviews of token-heavy prompts or supplied text. ChatGPT plugin skills do not intercept model traffic, inspect local histories, run a CLI, calculate billed tokens, or guarantee cost reductions.

## Included skills

- `concise-response`: concise, answer-first output while preserving essential meaning and safeguards.
- `safe-text-compression`: compress user-provided text without corrupting technical or decision-critical payloads.
- `token-efficiency-review`: find avoidable prompt/context overhead and offer reversible, measurable experiments.

## Source and attribution

- Upstream project: <https://github.com/juliusbrussee/caveman>
- Upstream license: Apache-2.0 (current repository); review its `LICENSING.md` and notices for older or third-party content before copying any source files.
- This plugin contains original instructions, not copied Caveman files or logo assets.

## Limitations

Text compression can remove nuance. Keep the original, preserve negation/numbers/units/code/paths/errors/uncertainty, and review the compressed output before relying on it. For medical, legal, financial, safety, security, or operational decisions, favor completeness and source verification over brevity.
