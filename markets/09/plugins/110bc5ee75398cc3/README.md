# Batch Banana plugin

Generate images and video, and edit images, with [Batch Banana](https://batchbanana.com) from ChatGPT, Codex, Cursor, and any client that loads [Agent Plugins](https://agent-plugins.org).

The plugin contains:

- `mcp.json`: the Batch Banana MCP server, `https://mcp.batchbanana.com/mcp` (Streamable HTTP).
- `skills/batch-banana/SKILL.md`: how the agent should pick models, quote costs, start jobs, poll for results, and handle errors.
- `plugin.json`: the Agent Plugins manifest, with the ChatGPT and Codex listing under `extensions.com.openai`.
- `.cursor-plugin/plugin.json`: the Cursor manifest.

## What it does

- Generate images from a prompt and optional reference images, with a choice of models and aspect ratios.
- Generate video from a prompt, a start frame, or reference images.
- Edit images: background removal, upscales, and text-guided edits.
- Search your Batch Banana library and projects to build on earlier work.

Every output is returned as a URL and saved to your Batch Banana library.

## Requirements

You need a Batch Banana account. When you connect, your client opens batchbanana.com, you sign in, and you choose the workspace to connect. No API key is involved: the server uses OAuth.

Generations and paid edits spend that workspace's credits. Quotes, model lists, and library searches are free. A job that fails is refunded automatically.

## Install

### ChatGPT and Codex

Install Batch Banana from the Plugins Directory once it is listed.

To connect the server directly in Codex CLI:

```bash
codex mcp add batch-banana --url https://mcp.batchbanana.com/mcp
codex mcp login batch-banana
```

### Cursor

Install Batch Banana from the Cursor Marketplace once it is listed.

To connect the server directly, add it to `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "batch-banana": {
      "url": "https://mcp.batchbanana.com/mcp"
    }
  }
}
```

Cursor opens a browser window to sign in the first time the server is used.

### Other MCP clients

Point the client at `https://mcp.batchbanana.com/mcp` with the Streamable HTTP transport. The server supports OAuth dynamic client registration and Client ID Metadata Documents.

## Links

- Website: https://batchbanana.com
- Support: https://batchbanana.com/support
- Privacy policy: https://batchbanana.com/privacy
- Terms of service: https://batchbanana.com/terms

## License

MIT. See [LICENSE](LICENSE).
