# App Listing Screenshots — AI Plugin & MCP Server

Unified plugin and Model Context Protocol (MCP) server for **ChatGPT**, **Codex**, and **Claude**.

Create App Store and Google Play listing images directly in AI conversations. Renders on the App Listing Screenshots Cloudflare Worker with Skia/CanvasKit WASM, returns full-resolution PNGs, and packages them into a ZIP archive without requiring local graphics software or manual API keys.

- **MCP Endpoint**: `https://listingframe.benbaler.workers.dev/mcp`
- **Transport**: Streamable HTTP / Server-Sent Events (SSE)
- **Authentication**: Automatic anonymous OAuth (each client receives an isolated anonymous workspace; no API key needed)

---

## 1. ChatGPT Installation

### Option A: Upload Plugin Archive (Developer Mode)
1. In ChatGPT, open **Settings** → **Security & login** (or **Developer Settings**) and enable **Developer mode**.
2. Go to **Plugins** / **Connected Apps** → **Create plugin** (or **Upload new version**).
3. Select this `app-listing-screenshots-plugin.zip` archive.
4. Confirm connection and authorize the plugin.

### Option B: Connect MCP Server directly
1. Under **Settings** → **Connected Apps** / **MCP Servers**, choose **Add Server**.
2. Enter the Server URL: `https://listingframe.benbaler.workers.dev/mcp`
3. Authentication: select **OAuth** (connects automatically without manual credentials).

### How to use in ChatGPT
Attach your app screenshots or mockups and prompt ChatGPT:
> *"Create three App Store screenshots (1320×2868) using my attached captures. Use a deep blue background with headlines 'Track Daily', 'Stay Focused', and 'Reach Goals'. Show me the previews and provide the ZIP download."*

---

## 2. Codex Installation

### Option A: Plugin Directory
Extract this archive into your Codex plugins folder:
```sh
mkdir -p ~/.codex/plugins/app-listing-screenshots
unzip app-listing-screenshots-plugin.zip -d ~/.codex/plugins/app-listing-screenshots
```
Codex automatically detects `.codex-plugin/plugin.json`, `.mcp.json`, and the bundled `create-screenshots` Skill.

### Option B: Configure MCP in Codex
Add the remote MCP server to your `~/.codex/config.json` or `~/.codex/mcp.json`:
```json
{
  "mcpServers": {
    "app-listing-screenshots": {
      "type": "streamable-http",
      "url": "https://listingframe.benbaler.workers.dev/mcp"
    }
  }
}
```

### Option C: Standalone Skill
Copy `skills/create-screenshots` to your project's `.agents/skills/` or `~/.codex/skills/`.

---

## 3. Claude Installation

### Option A: Claude Desktop (macOS & Windows)
Add the MCP server to your Claude Desktop configuration file:
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

Add the following under `"mcpServers"`:
```json
{
  "mcpServers": {
    "app-listing-screenshots": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://listingframe.benbaler.workers.dev/mcp"]
    }
  }
}
```
*(If your MCP client supports direct HTTP streaming, point directly to `https://listingframe.benbaler.workers.dev/mcp`)*.

Restart Claude Desktop. You will see the tools icon (hammer) with App Listing Screenshots tools enabled.

### Option B: Claude Code (CLI)
Run in your terminal:
```sh
claude mcp add app-listing-screenshots -- npx -y mcp-remote https://listingframe.benbaler.workers.dev/mcp
```

### Option C: Claude Projects / Custom Instructions
Copy the instructions from `skills/create-screenshots/SKILL.md` into your Claude Project instructions.

---

## Available Tools

- `list_screenshot_options`: List supported dimensions, store presets (App Store, Google Play), font families, colors, and layout schemas.
- `create_screenshot_series`: Create ordered screenshot slides with titles, backgrounds, and device frames from uploaded files, data URLs, or the built-in demo.
- `update_screenshot_series`: Update specific slide titles or styling while preserving uploaded captures.
- `export_screenshot_series`: Render full-resolution PNGs, display inline previews, and generate a signed ZIP download link (valid for 1 hour).
