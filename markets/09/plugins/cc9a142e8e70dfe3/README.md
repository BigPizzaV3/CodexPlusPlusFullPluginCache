# ChatGPT plugin package — AdvPulse

The package uploaded to the OpenAI platform's Plugins page (platform.openai.com/plugins) to list the public ADV search
in the ChatGPT plugin directory. It is a manifest around the live server `https://api.advpulse.ai/mcp`; no code.
Values come from `.pm-wiki/raw/docs/2026-10-02-chatgpt-plugin-submission-pack.md`. Format: agent-plugins 1.0.0
(`plugin.json`, `mcp.json`, `assets/`); OpenAI's listing and review fields live under `extensions.com.openai`.

Build the ZIP from inside this folder so `plugin.json` sits at the archive root:

    cd chatgpt-plugin && zip -r -X ../advpulse-plugin-1.0.0.zip plugin.json mcp.json assets README.md

`demo_recording_url` (under `extensions.com.openai.review`) is added once the walkthrough video exists; a new version
needs a bumped `version`.
