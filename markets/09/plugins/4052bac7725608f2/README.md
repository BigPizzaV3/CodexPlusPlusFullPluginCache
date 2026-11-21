# ViewMax plugin

Production MCP: `https://viewmax.studio/api/mcp`.
The plugin connects an existing ViewMax Studio account through OAuth and exposes
14 tools for model selection, existing credit balance, image/video generation,
narration, music, sound effects and task retrieval. It does not expose checkout
or subscription purchases and does not claim AI Director support.

Review scenarios in `.codex-plugin/plugin.json` describe expected behavior;
they do not claim that every scenario has already been exercised in ChatGPT.
Before submission, provide a dedicated reviewer login, synthetic sample data,
a factual accessible walkthrough and a successful current MCP scan. Credentials
must be supplied privately through the submission portal and never bundled.

The account and generation safeguards remain those of the existing ViewMax
service. Use stable idempotency keys and inspect the actual task status.
