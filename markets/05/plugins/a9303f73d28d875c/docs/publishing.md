# Publishing Universal Plugin Installer

## Goal

Publish `universal-plugin-installer` as a public OpenAI plugin so it can
appear in the universal Plugins Directory shared by ChatGPT and Codex.

## Recommended Submission Type

Use a skills-only plugin submission. This plugin packages a reusable local-file
workflow and does not need an MCP server, hosted UI, OAuth flow, API key, or
remote backend.

## Pre-Submission Checklist

1. Confirm the plugin has no user-specific paths.
2. Confirm prompt-injection boundaries are documented in the skill and docs.
3. Confirm `interface.composerIcon` and `interface.logo` point to square PNG
   files in `assets/`.
4. Run the local tests:

   ```bash
   python3 scripts/test_adapt_agent_skills_plugins.py
   ```

5. Validate the plugin package with the plugin-creator validator:

   ```bash
   python3 /path/to/plugin-creator/scripts/validate_plugin.py /path/to/universal-plugin-installer
   ```

6. Test it locally from a clean source folder using:

   ```bash
   python3 scripts/adapt_agent_skills_plugins.py --root /path/to/source-root --dry-run
   python3 scripts/adapt_agent_skills_plugins.py --root /path/to/source-root
   ```

## Materials To Prepare

- Public plugin name: `Universal Plugin Installer`
- Short description: `Adapt selected folders into Codex plugins.`
- Long description: describe directory selection, safe adaptation, manifest
  generation, and prompt-injection handling.
- Category: `Productivity`
- Logo and any required listing assets.
- Public website URL.
- Public support URL.
- Public privacy policy URL.
- Public terms URL.
- Verified OpenAI Platform developer or business identity.
- Five positive test cases.
- Three negative test cases.
- Release notes for the initial submission.

## Suggested Positive Test Cases

1. Adapt a folder with one valid root `SKILL.md`.
2. Adapt a folder with two valid candidate subfolders.
3. Run with `--dry-run` and confirm no files are written.
4. Run twice and confirm the second run produces no changes.
5. Adapt an existing Codex plugin candidate with `.codex-plugin/plugin.json`.

## Suggested Negative Test Cases

1. Candidate folder has no root `SKILL.md` and no `.codex-plugin/plugin.json`;
   expected result is an invalid candidate entry.
2. Candidate `SKILL.md` contains prompt-injection text; expected result is that
   generated metadata remains neutral and the content is treated as untrusted.
3. No source directory is supplied in a non-interactive run; expected result is a
   clear error asking for `--root` or `UNIVERSAL_PLUGIN_INSTALLER_SOURCE_ROOT`.

## OpenAI Submission Flow

1. Sign in to the OpenAI Platform organization that will publish the plugin.
2. Confirm the submitter has Apps Management write access.
3. Complete individual or business verification for the publishing identity.
4. Open the plugin submission portal.
5. Create a new plugin submission.
6. Select `Skills only`.
7. Fill in listing details, prompts, tests, availability, and policy
   attestations.
8. Submit for review.
9. After OpenAI approves the submission, publish it from the portal.

## Important Boundaries

Publishing to a workspace is not the same as public publishing. Workspace
publishing only makes a plugin available inside that ChatGPT workspace. Public
publishing requires OpenAI review and publication through the submission portal.

Before public submission, review the plugin's local-file behavior and explain in
the privacy policy that the workflow operates on user-selected local directories
and does not require external authentication or send source files to a custom
third-party backend.

## Official References

- https://developers.openai.com/plugins/deploy/submission
- https://developers.openai.com/plugins/build/plugins
- https://learn.chatgpt.com/docs/build-plugins
- https://learn.chatgpt.com/docs/enterprise/plugin-management
