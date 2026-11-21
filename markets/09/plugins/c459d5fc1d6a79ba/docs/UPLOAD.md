# TheySaid plugin upload

Upload theysaid-plugin-1.0.0.zip through OpenAI Platform > Plugins > Upload new or existing plugin. Choose the existing plugin if this is an update, and preserve its assigned name/version requirements.

This package uses the portable Agent Plugins format with a Codex compatibility manifest. The remote MCP URL is https://ai.theysaid.io/api/mcp. No tool allowlist is configured; all tools the authenticated server exposes are available for scanning. The supplied JSON documents 34 tools, but live tool discovery has not been authenticated or verified.

The original submission JSON is retained as reference in this directory. Its five positive and three negative test cases have been mapped into plugin.json. Tool annotations and justifications remain reference material; they do not override the live server tool definitions.

Before submitting for review:

- Add the support URL and real brand icon assets, to the root plugin.json extensions.com.openai.interface. Website, privacy and terms URLs were supplied by the publisher and added. Confirm Business is an available dashboard category.
- Add an accessible demo video URL as extensions.com.openai.review.demo_recording_url.
- Confirm country availability and commerce declarations in the portal.
- Complete MCP authentication and domain verification in the portal, then scan the tools.
- Supply dedicated reviewer credentials privately in Review details, if sign-in is required. Never add credentials to this ZIP.
- Replace the example project p1, proposal proposal-123, and example.com checkout URL in review cases with working test-account fixtures. Run all review cases; the provided expected results are not test execution evidence.
- Review automated findings before submission.

Official reference: https://developers.openai.com/plugins/deploy/submission
