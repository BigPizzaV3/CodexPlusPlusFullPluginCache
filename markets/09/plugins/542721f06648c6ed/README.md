# Scan.now plugin

This package exposes Scan.now's passive security tools to ChatGPT and Codex through
the remote MCP endpoint at `https://mcp.scan.now`.

The initial tool surface is intentionally focused:

- `scan_website_security` runs a full website audit or a focused TLS, security-header,
  DNS/email, or JavaScript check. It requires an explicit confirmation that the user
  owns the target or has permission to assess it.
- `check_phishing_link` inspects a suspicious URL and its public redirect destination
  for phishing signals.

The portable Agent Plugins manifests are `plugin.json` and `mcp.json`.
`.codex-plugin/plugin.json` and `.mcp.json` are compatibility fallbacks.

Build the uploadable archive from the repository root:

```bash
python3 scripts/build_chatgpt_plugin.py
```

After deployment, smoke-test the live MCP endpoint:

```bash
python3 scripts/check_chatgpt_plugin_live.py https://mcp.scan.now
```

The review recording is published at
`https://scan.now/openai-review/demo.mp4`. Reviewer-portal credentials are entered
separately in the OpenAI review form and are never bundled in this package.
