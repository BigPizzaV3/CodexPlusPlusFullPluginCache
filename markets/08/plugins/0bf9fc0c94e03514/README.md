# Lots of Sounds plugin package

This directory contains the public OpenAI plugin package for the Lots of Sounds MCP server.

- `plugin.json` is the portable plugin manifest.
- `mcp.json` points to the OAuth MCP endpoint.
- `assets/los-logo.png` is the light and dark plugin icon.

## Before submission

1. Deploy the OAuth MCP endpoint.
2. Confirm that `mcp.json` declares mixed public and OAuth access.
3. Test OAuth discovery, sign-in, tool listing, and account plan checks.
4. Run the OpenAI tool scan and correct all reported errors.
5. Verify the OpenAI developer or organization account and the website domain.
6. Prepare one Pro test account without multi-factor authentication.
7. Record a real ChatGPT or Codex walkthrough of the review cases.
8. Add the demonstration video URL to the OpenAI submission.
9. Confirm that the privacy policy, terms, contact, and support pages are public.
10. Create a ZIP file that has `plugin.json`, `mcp.json`, and `assets/` at its root.

Do not publish the package until the production OAuth connection passes all tests.
