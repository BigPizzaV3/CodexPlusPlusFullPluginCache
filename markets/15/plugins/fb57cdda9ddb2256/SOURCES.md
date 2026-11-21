# Packaging sources

Verified on 27 October 2026.

1. [OpenAI package guide](https://developers.openai.com/plugins/build/plugins) documents the portable manifest, MCP transport, provided OAuth client and optional setup skill.
2. [OpenAI authentication guide](https://developers.openai.com/plugins/build/auth) documents account authorization and per request scope verification.
3. [Claude custom skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills) documents a named skill folder inside a ZIP and its metadata.
4. [Claude Skills](https://support.claude.com/en/articles/12512180-use-skills-in-claude) documents the separate personal upload and enablement flow.

Package structure does not establish account connection, account eligibility, a running schedule or public directory publication.