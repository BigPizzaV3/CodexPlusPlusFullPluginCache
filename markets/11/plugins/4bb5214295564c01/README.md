# Oneprofile for ChatGPT

Oneprofile is a go-to-market workspace: you build lists of companies and people, fill them in with researched facts, and write to the ones worth writing to, by email and LinkedIn. This plugin connects ChatGPT to your Oneprofile workspace and teaches it the workflows that get good results there.

It bundles two things:

- **The Oneprofile MCP server** at `https://api.getoneprofile.ai/mcp`, signed in with OAuth. It gives ChatGPT the same tools the AI Assistant inside Oneprofile has, acting as you, in the one workspace you pick when you sign in.
- **Six skills** that tell ChatGPT when and how to use those tools: `find-leads`, `enrich-a-table`, `import-and-export`, `launch-a-sequence`, `triage-replies` and `outreach-review`.

## Package layout

| Path | What it is |
| --- | --- |
| `plugin.json` | Agent Plugins manifest with the OpenAI listing, review test cases and release notes under `extensions.com.openai` |
| `mcp.json` | The remote MCP server and its OAuth settings (Dynamic Client Registration) |
| `skills/<name>/SKILL.md` | One workflow per skill, with `agents/openai.yaml` for its display name and MCP dependency |
| `assets/logo.png`, `assets/icon.png` | Listing logo (1024 px) and composer icon (256 px) |

Build the upload ZIP from this folder with `./build.sh`, which writes `dist/oneprofile-chatgpt-<version>.zip`.

## Data and safety

The plugin stores nothing and runs no code. Everything ChatGPT does in Oneprofile goes through the MCP server to `api.getoneprofile.ai`, over HTTPS, signed in with the user's own Oneprofile account. Reads, changes, and sends or removals reach Oneprofile through separate tools, so each kind can be approved on its own, and the skills ask before launching a sequence, sending a reply or deleting anything. Oneprofile processes data under its [privacy policy](https://www.getoneprofile.ai/privacy-policy) and [terms](https://www.getoneprofile.ai/terms).

## Support

[AI apps guide](https://docs.getoneprofile.ai/integrations/ai-apps) · support@getoneprofile.ai

## License

MIT. See [LICENSE](LICENSE).
