# Jourvanta MCP package

This portable package connects an assistant to the Jourvanta remote MCP server. It contains public listing metadata and the server URL only. OAuth credentials, reviewer credentials, private account data, and backend source code must never be included in the package.

The initial browser flow links an existing Jourvanta account and grants read or read/write access. Trip operations run through the authenticated server. Deletions and major changes require the assistant to preview the exact action and obtain a separate affirmative reply in chat. This conversational confirmation is host guidance; it is not a server-enforced proof of user approval.

For ChatGPT, ZIP the contents of this directory (with `plugin.json` and `mcp.json` at the archive root) and upload through the publishing portal. Finish domain verification, OAuth configuration, tool discovery, reviewer account access, the recorded walkthrough, and live review cases before submitting. The manifest test cases describe acceptance criteria; their presence is not evidence that live testing has passed.

For Claude, submit `https://jourvanta.com/mcp` as a remote MCP connector through the directory management portal. A public copy of the private backend repository is not required for that connector submission.

Support: https://jourvanta.com/#support
