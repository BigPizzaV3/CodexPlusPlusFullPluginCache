---
name: validation-and-packaging
description: Validate plugin structure, metadata, assets, and produce a reproducible ZIP.
---

Run the plugin validator after every structural change. Check normalized names, required manifest fields, skill frontmatter, asset references, JSON syntax, icon dimensions, and ZIP contents. Preserve the source folder and rebuild the ZIP deterministically enough to make reuploads traceable. Report the exact validation result and artifact path.

Before any dashboard upload, run a submission preflight:

- Require `interface.defaultPrompt` to be an array of no more than three strings.
- Require the user-facing subtitle to be no more than 30 characters.
- Check the combined plugin-name and skill-name length against the platform limit.
- Require both `interface.logo` and `interface.composerIcon` to resolve to square PNG files and verify their minimum dimensions.
- Confirm the ZIP contains `.codex-plugin/plugin.json` at its root and every referenced skill and asset.
- Record each check as pass/fail in an issue ledger with the exact file and field involved.

Do not upload a package with a known preflight failure. If the platform reports a new constraint, fix the smallest local cause, rerun the full preflight, and create a new traceable version.
