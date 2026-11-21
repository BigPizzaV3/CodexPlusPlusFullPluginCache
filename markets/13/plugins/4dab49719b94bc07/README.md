# PartsPerk Agent Plugin package

Portable OpenAI Agent Plugins package for ChatGPT / Codex.

- **Name:** PartsPerk (never “PartsPerk Plugin” / “PartsPerk MCP”)
- **MCP:** `https://partsperk.com/mcp` (streamable-http, auth none)
- **Publisher / support email:** `contact@partsperk.com`
- **Publication:** `EXTERNAL` until OpenAI review + explicit Publish (PG-32)
- **Logo:** hashed from `apps/web/public/brand/partsperk-logo-mark.png`

Verify:

```bash
node scripts/chatgpt-plugin/verify-plugin-package.mjs
node scripts/chatgpt-plugin/build-plugin-zip.mjs
```

Do not set `PARTSPERK_PLUGIN_PUBLIC=true` until PG-32.
