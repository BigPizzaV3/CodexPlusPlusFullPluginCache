# Open-source foundation

This skill is paired with Microsoft's official Playwright CLI and its agent skill:

- Repository: https://github.com/microsoft/playwright-cli
- License: Apache-2.0
- Installed skill name: `playwright-cli`

Playwright CLI contributes token-efficient snapshots, stable element refs, locator generation, browser sessions, screenshots, and trace/debug commands. It is suitable for independent repeatable browser automation.

For a user's already signed-in MiriCanvas tab, prefer Codex's in-app Browser skill because it can reuse the authenticated session. Playwright CLI is a second route, not a guarantee of access to that same login.

No mature, trustworthy, MiriCanvas-specific open-source automation project was identified during the initial search. This local skill therefore adds site-specific workflow, typography guidance, validation, and recovery rules on top of the maintained Playwright foundation instead of installing an unverified repository.
