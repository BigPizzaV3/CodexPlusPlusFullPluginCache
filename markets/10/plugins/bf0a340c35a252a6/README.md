# Pretture ERP AI ChatGPT Plugin

This folder contains the upload package for the Pretture ERP AI plugin.
It uses the current OpenAI Agent Plugins layout:

- `plugin.json` is the portable plugin manifest.
- `mcp.json` registers the hosted Streamable HTTP MCP server.
- `skills/get-started/SKILL.md` provides onboarding guidance.
- `.codex-plugin/plugin.json` and `.mcp.json` provide compatibility metadata.
- `assets/` contains listing icon/logo/screenshot files referenced by the manifest.

## Before Upload

Verify these values before creating the ZIP:

1. `mcp.json` and `.mcp.json`
   - Replace `https://mcp.pretture.com/v1/mcp` if your production MCP endpoint is different.
2. `plugin.json`
   - Confirm `supportURL`, `privacyPolicyURL`, and `termsOfServiceURL` are live HTTPS pages.
   - Confirm `author.email` is the right support or developer contact.
   - Confirm the privacy policy covers the plugin data practices required by OpenAI review: data categories, use purposes, recipient categories, retention timelines, and user controls.
   - Confirm `extensions.com.openai.review.demo_recording_url` points to the reviewer-accessible walkthrough video.
3. OpenAI dashboard
   - Enter reviewer credentials separately in Review details. Do not put test credentials, passwords, JWTs, API keys, or reviewer-only instructions in the ZIP.
   - Complete organization or business verification for the publisher identity.

## Validate And Package

From this directory:

```bash
python3 scripts/validate_package.py
./scripts/package.sh
```

The packaging script creates:

```text
../pretture-ai-chatgpt-plugin.zip
```

The ZIP is built with `plugin.json` at the archive root, which is accepted by the plugin submission portal.

## Upload

Open the OpenAI Platform plugin dashboard, upload the ZIP, resolve automated findings, then submit the draft for review.
