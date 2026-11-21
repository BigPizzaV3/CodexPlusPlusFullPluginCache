# SocialHive GPT Plugin

Official ChatGPT App / Plugin configuration for **SocialHive** (`https://socialhive.pro`).

## Overview
This repository contains the plugin package for OpenAI ChatGPT Apps & Plugins directory:
- **MCP Endpoint**: `https://platform.socialhive.pro/api/mcp`
- **Specification**: Compatible with both Agent Plugins schema (`plugin.json` + `mcp.json`) and OpenAI Codex Plugin schema (`.codex-plugin/plugin.json` + `.mcp.json`).
- **Domain Verification**: `https://platform.socialhive.pro/.well-known/openai-apps-challenge`

## Structure
```
socialhive-gpt-plugin/
├── .codex-plugin/
│   └── plugin.json
├── assets/
│   ├── icon.png
│   ├── icon-dark.png
│   ├── logo.png
│   └── logo-dark.png
├── skills/
│   └── socialhive/
│       ├── SKILL.md
│       ├── agents/
│       │   └── openai.yaml
│       └── assets/
│           └── icon.png
├── .mcp.json
├── mcp.json
├── plugin.json
├── LICENSE
└── README.md
```

## Packaging for Submission
To build the submission ZIP:
```bash
cd socialhive-gpt-plugin
zip -r ../socialhive-gpt-plugin.zip . -x "*.DS_Store" "*.git*"
```
Upload `socialhive-gpt-plugin.zip` directly to the OpenAI Platform dashboard under **Upload new version**.
