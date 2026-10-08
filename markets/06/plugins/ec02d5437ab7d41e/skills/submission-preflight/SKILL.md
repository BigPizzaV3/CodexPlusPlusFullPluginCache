---
name: submission-preflight
description: Run a deterministic preflight for OpenAI plugin manifests, assets, skills, prompts, names, and ZIP structure before dashboard upload.
---

# Submission preflight

Use this skill before every OpenAI dashboard upload or version update.

## Checks

- Parse `.codex-plugin/plugin.json` and confirm the package name matches the outer folder.
- Confirm `interface.defaultPrompt` is an array containing at most three non-empty strings.
- Confirm the subtitle is no more than 30 characters and describes a concrete user benefit.
- For every skill, confirm frontmatter exists, the skill name is normalized, and the combined plugin-name plus skill-name length is within the platform limit.
- Resolve `interface.logo` and `interface.composerIcon`; require square PNG files and verify directory and composer minimum dimensions.
- Confirm every referenced skill and asset exists.
- Confirm the ZIP has `.codex-plugin/plugin.json` at its root and contains no accidental parent directory, secrets, or macOS metadata.
- Run the plugin validator and record its exact result.

## Issue ledger

For every failure, record the observed error, source path and field, smallest fix, validation result, and remaining status. Do not move to dashboard upload while a preflight failure remains.

## Update invariant

When updating an existing published plugin, preserve its plugin ID, package name, developer identity, public metadata, branding, and directory identity. Only upload a newly versioned package after all checks pass.
