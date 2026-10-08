# Better Plans 0.1.5 release checks

## Scope

0.1.5 is a narrow interface/packaging revision based on `better-plans-plugin-0.1.4-revised.zip`. It does not change the Better Plans planning framework, activation logic, tool library, operating reference, or behavioral rules.

## Changes

- Updated both plugin manifests from version 0.1.4 to 0.1.5.
- Removed `defaultPrompt` from the portable and compatibility plugin manifests.
- Removed `default_prompt` from `skills/better-plans/agents/openai.yaml`.
- Added `assets/icon-reverse.svg`, using the existing no-space icon geometry with the reverse `#F4F1EC` treatment.
- Added the matching skill-local `skills/better-plans/assets/icon-reverse.svg`.
- Updated plugin `composerIcon` and skill `icon_small` to the reverse icon.
- Preserved the 0.1.4 root portable manifest, discovery metadata, `logoDark`, `brandColorDark`, descriptions, keywords, capabilities, and all substantive Skill content.

## Release checks

- [ ] Import/submission accepts the 0.1.5 ZIP without schema errors.
- [ ] No Better Plans preset/default prompt appears unexpectedly in the normal ChatGPT interface.
- [ ] The small/composer icon uses the reverse mark where surfaced.
- [ ] The larger dark-mode logo still uses `assets/logo-dark.png`.
- [ ] Better Plans still activates on the positive prompts in `activation-regression-0.1.4.md`.
- [ ] Better Plans still avoids full activation on the negative/boundary prompts in `activation-regression-0.1.4.md`.
- [ ] Existing behavioral parity checks remain unchanged.
