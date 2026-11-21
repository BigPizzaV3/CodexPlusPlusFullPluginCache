# ScreenshotAgent plugin 0.4.0

Connects ChatGPT and Codex to the ScreenshotAgent MCP server at `https://screenshotagent.com/mcp`. OAuth is discovered by the host. The package contains no server code, API wrapper or credentials.

| File | Purpose |
| --- | --- |
| `plugin.json` | Agent Plugins 1.0 manifest: identity, listing, review test cases, release notes |
| `mcp.json` | The one Streamable HTTP MCP server |
| `skills/managed-screenshots/SKILL.md` | When to use the tools and the judgment around them |
| `assets/logo.png` | 1024 × 1024 listing and composer icon |

## What changed from 0.3.0

- The skill no longer restates arguments, result fields or polling intervals. Those live in the MCP tool descriptions and output schemas, which OpenAI rescans and updates without a new ZIP. `references/tool-contract.md` is removed: it was pinned to an older server commit and had drifted.
- The skill no longer tells the model to post signed image links as Markdown images. Hosts with MCP Apps show images and search results inline.
- The manifest adds `supportURL`, `privacyPolicyURL` and `termsOfServiceURL`, which MCP review requires, plus five positive and three negative review test cases and release notes.

## Not in the package

- The demo recording URL. Add it as `review.demo_recording_url` or enter it in the dashboard.
- Reviewer credentials. Enter them in the dashboard under Review details; ZIP metadata rejects them.
- Commerce declaration and country availability. Left out so the dashboard's saved values are kept.
