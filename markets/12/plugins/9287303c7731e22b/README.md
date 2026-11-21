# Streamline Icons

Search, recommend and download [Streamline](https://home.streamlinehq.com) icons, illustrations and design elements from Claude and Cursor. Streamline makes some of the largest icon and illustration sets available: over 100,000 icons and 21,000 elements, in SVG and PNG. It also hosts popular open-source libraries such as Lucide, Heroicons, Phosphor, Font Awesome, Tabler and Material Symbols.

## What's included

- **Streamline MCP server** (`https://public-api.streamlinehq.com/mcp`): tools to browse icon families and sets, search assets, and download SVG or PNG files. Some tools render interactive previews in clients that support MCP Apps.
- **`streamline-expert` skill**: teaches Claude to act as a design-system assistant. It recommends one icon family that fits your product, finds icons for UI concepts, maps other icon libraries to Streamline equivalents, and delivers downloads.

## Setup

When you first use a Streamline tool, Claude or Cursor asks you to sign in with your Streamline account through OAuth. A free account can search and download free assets. Downloading premium assets needs a paid plan. No API key or local configuration is needed.

## Data and privacy

The plugin runs no local code. Everything it does goes through the Streamline MCP server over HTTPS:

- **What's sent:** the tool Claude calls and its arguments, such as search queries, family or set names, and the assets you choose to download, together with your OAuth access token.
- **What's returned:** your account email and plan, catalog results, and short-lived signed download URLs for the assets.
- **Analytics:** Streamline records each tool call (the tool name, its search query, and the MCP client and model in use) against your account to improve search and recommendations.

See the [Streamline privacy policy](https://help.streamlinehq.com/en/articles/5356474-privacy-policy) and the [Streamline API terms of use](https://help.streamlinehq.com/en/articles/11094721-streamline-api-terms-of-use). Assets you download are licensed under your Streamline plan, not under this repository's license.

## Example prompts

- "Which icon sets pair well with the Inter font?"
- "Find me a line-style icon for notifications"
- "Search for free illustrations related to teamwork"

## License

The plugin files in this folder are licensed under the Apache License 2.0. See [LICENSE](LICENSE).
