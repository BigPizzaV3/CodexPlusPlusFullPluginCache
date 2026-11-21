# Builderii for ChatGPT

Your Builderii boards, right in ChatGPT. Ask what's on a board and get its flows, screens, mind maps and sticky notes as text. Brainstorm onto a board as sticky notes grouped by theme. Get a review of a flow or wireframes, with comments pinned to the screens and steps they're about.

## Install

- **ChatGPT, the ChatGPT desktop app and Codex:** in ChatGPT, open **Plugins → Add → Upload plugin** and choose `builderii-chatgpt-plugin.zip` as it is (don't unzip it). Open **Builderii**, then under **MCP servers** select **Builderii → Authenticate**, sign in to Builderii and **Allow**. Builderii shows with its icon and skills, and in Codex's **MCP servers** under **From plugins** (quit and reopen the desktop app if it isn't listed yet).
- **Just the connection:** open **Plugins**, select **+** and **Add custom MCP server**. Name it Builderii, use the address `https://app.builderii.com/mcp` and choose OAuth, then **Create as a plugin**. Sign in to Builderii and **Allow**. That one has no icon or skills.
- **Trying a local build in Codex:** unzip `builderii-chatgpt-plugin.zip` to `~/.codex/plugins/builderii`, add it to `~/.agents/plugins/marketplace.json` (`"source": { "source": "local", "path": "./plugins/builderii" }`, `"category": "Design"`, `"policy": { "installation": "AVAILABLE", "authentication": "ON_INSTALL" }`) and restart the app.

Builderii's **Settings → Connected apps** has the download and these steps. Use that zip (or `dist/builderii-chatgpt-plugin.zip` after `npm run build`), not a zip of this folder: Finder's Compress puts everything under `chatgpt-plugin/` with `.git` and `__MACOSX` files, so `plugin.json` isn't at its root.

## Connect

The plugin connects to your Builderii account through Builderii's MCP server (`https://app.builderii.com/mcp`). ChatGPT finds Builderii's sign-in by itself: you sign in once and allow it. It acts with your access: any board you can open in Builderii, it can open. Disconnect it any time in Builderii under **Settings → Connected apps**.

## Skills

- **builderii**: how to work in your boards: which tool for what (drawing it yourself or with Builderii's AI, changing diagrams in place), finding boards before making new ones, linking them.
- **app-screens**: design app or website screens as a clickable prototype (from a description or a screenshot).
- **diagram**: draw a flowchart, mind map, sequence diagram, sitemap, roadmap or database diagram, or change one on a board.
- **brainstorm**: put ideas on a board as sticky notes grouped by theme.
- **feedback**: review a flow, wireframes or a prototype and leave comments on the right screens.
- **summarize**: explain a board, or answer a question from it.

## Development

This repository is the plugin in the Agent Plugins 1.0.0 format: `plugin.json` (with `extensions.com.openai.interface`), `mcp.json` (only the server's `type` and `url`: ChatGPT finds the OAuth sign-in from the server's 401, and leaves out a server with any other key), `skills/` (Agent Skills: SKILL.md with name and description only) and `assets/` (icon.png 128 px, logo.png 512 px).

```bash
npm run build   # dist/builderii, dist/builderii-chatgpt-plugin.zip, and a copy in ../web/public/plugins/
```

The build checks the manifest, the skills and the server, then zips the plugin reproducibly (fixed timestamps, no folder entries). When it's checked out at `builderii/infrastructure/chatgpt-plugin`, it copies the zip to the web app (`web/public/plugins/builderii-chatgpt-plugin.zip`), which Settings → Connected apps offers for download. Bump `version` in plugin.json when a skill or the manifest changes, build, then deploy the web app.

The MCP server itself is in the Builderii repository (`infrastructure/cdk/lib/lambdas/api/mcp.mjs`); it signs people in with OAuth (Builderii's `/connect` page, dynamic client registration, PKCE).
