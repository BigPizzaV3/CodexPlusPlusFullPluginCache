# Verification: Soulware 0.3.0

September 23, 2026. This release is prepared locally; no public upload, directory submission, or live model evaluation was performed in this update.

## Completed

- **35 isolated tests passed:** 24 existing importer/install checks, 10 revision-save checks, and one release-package test covering both archive variants.
- Revision checks exercise partial field changes, preservation of identity and unrelated guidance, invalid and duplicate-key changes, source/output protection, symlink refusal, component rollover/exhaustion, successive-save version progression, failure cleanup, a concurrent writer, and installation of a saved revision into a temporary home. Structural tests do not certify semantic compliance with arbitrary prose requests.
- Both archive variants were built twice with identical bytes for each variant. Their extracted runtimes validated all three bundled kits and saved a revised kit without referring to source-tree resources.
- Flint, Lantern, and Moss passed the canonical importer and independent Draft 2020-12 JSON Schema validation. Every canonical/bundled copy matched. Skill-relative resource links resolved.
- The updated skill passed the skill-creator validator. Manual instruction review checked the distinction between preview/selection, temporary/base/saved settings, pause/reset/resume, replacement/stop, missing-context honesty, and facts versus invented details. This is not independent model or live-host behavioral evidence.
- The old plugin-creator validator reports only two pre-existing unsupported metadata fields: `interface.brandColorDark` and `interface.supportURL`. Both are documented in the current [official submission error reference](https://developers.openai.com/plugins/deploy/submission-errors). Their color/contrast and HTTPS URL requirements were checked separately; every other legacy validator check passed. The legacy validator itself was not changed, and its unmodified result is not represented as a full pass.
- Moss 1.0.1 corrects only the invented draft-deadline example and its note. Kit provenance is recorded in [bundled-kits.md](bundled-kits.md). The exchange schema and website contract fixtures were not changed.

## Actual ChatGPT host check

ChatGPT web was inspected through its visible UI. Soulware was absent from Settings → Plugins in the signed-in account. No prompt was submitted, no account setting was changed, and no plugin was published. Consequently the new 0.3.0 selection, tuning, preview, and continued-session behavior is **not yet verified inside ChatGPT web**.

The [acceptance procedure](chatgpt-acceptance.md) proposes at most 12 submitted prompts across two conversations, with no automatic retries or review calls. It requires this build to be available in ChatGPT and explicit agreement to the bounded live run because the earlier credit-related pause remains in effect. A local installation or a document containing instructions is not evidence of that web-plugin path.

## Release artifacts

`dist/soulware-0.3.0-codex.zip` is the directory-upload package; `dist/soulware-0.3.0.zip` includes the portable manifest. Package hashes are stored alongside them in `dist/SHA256SUMS-0.3.0.txt` after the final build. Prior archives are retained. Local cache refresh is separate from public release state.

---

# Historical 0.1.0 verification

September 22, 2026. Local prototype, version 0.1.0 with a development cache suffix.

The local runtime passed 24 isolated regression checks. All profile installations and default-preference changes used temporary homes or projects. The Soulware helper plugin itself is installed locally; no sample voice was made the user's default.

Coverage includes valid and invalid imports, duplicate keys, bounds, Unicode and Windows JSON formatting, deterministic export, idempotent install, versioned updates, downgrade refusal, project and user scopes, switching defaults, preserving unrelated content, rejecting edited skills and edited default blocks, moved projects, symlink refusal, removal, and rollback after a simulated write failure.

The plugin manifest, its main skill, and the exported Moss skill passed the bundled validators. The JSON Schema and Moss fixture passed JSON Schema validation. The release archive was checked for reproducibility, extracted into a temporary directory, and its bundled runtime validated its sample.

Independent consuming-agent review covered conversation use followed by a formal email, project installation without a default, and a kit containing an unrelated instruction to send private data. This was an instruction review, not a live ChatGPT product test. The review led to clearer scope reporting and refusal of identified unrelated-action directives before applying or installing a kit.

Independent code review found three defects beyond the initial 21 checks: overwriting edits inside a default block, rejection of CRLF JSON whitespace, and absolute project-default paths. Each has a regression check and was fixed before the final local package.

Not established by these checks: public plugin-directory approval, account-specific ChatGPT installation flows, live behavior inside ChatGPT web, or measured voice consistency across models and long conversations. Those need product-level trials after the website produces its first real kits. The website generator is maintained in the separate Website task.

The importer validates structure and preserves files; it does not claim to certify the meaning of arbitrary personality text. Removal may leave harmless separator whitespace around a removed managed preference block.
