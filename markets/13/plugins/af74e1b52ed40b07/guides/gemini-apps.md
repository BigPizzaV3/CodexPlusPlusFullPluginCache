# Gemini Apps

Gemini Apps does not import a plugin ZIP. Connect the MCP URL in Gemini's web Connected Apps flow.

Skill/plugin version 0.1.41. Gemini does not read that version from a manifest.

MCP URL: https://09vyfnjv.mcp.cofr.io/mcp

## Tools

- run_aoa_mini_assessment: Public, no sign-in
- aoa_ai_opportunity_assessment: OAuth required
- create_aoa_discovery_guide: OAuth required
- run_aoa_full_assessment: OAuth required

Public tools are intended to work before Cofr sign-in. Protected tools require Cofr account linking. Google account login and Cofr sign-in are different steps. OAuth and lazy sign-in for Gemini Apps are unverified.

## Setup

1. On a computer, open gemini.google.com and sign in with a personal Google Account.
2. At the bottom, open Settings, then Connected Apps. If it is missing, open Personal Intelligence, then Connected Apps.
3. Under Custom apps, choose Add a custom app and paste the MCP URL.
4. Choose Next and follow the prompts.

Google currently offers custom apps on the Gemini website for personal Google Accounts, in English, for people 18 or older in the US, with Keep Activity on.

To disconnect, open Settings, then Connected Apps, and remove the custom app. Removing it does not revoke a Cofr account link. Cofr sign-in and revocation for Gemini Apps are unverified.

There is no Gemini plugin upload and no marketplace approval step in this package.

Last verified 2026-10-19: https://support.google.com/gemini/answer/17209137?hl=en
