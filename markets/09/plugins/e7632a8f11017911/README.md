# Unfetch Agent Plugin

Connect your AI assistant to your marketing data and turn live account evidence into clear, actionable reports.

Unfetch supports:

- Google Ads campaign, keyword, search-term, conversion, budget, and performance reporting
- Meta Ads campaign, ad set, ad, placement, spend, conversion, and performance reporting across Facebook, Instagram, and Messenger
- Google Analytics traffic and conversion reporting
- Google Search Console query and landing-page reporting
- Google Merchant Center product and account issues, free-listing and Shopping product performance, price benchmarks and suggestions, best sellers, and Shopping competitor visibility
- Keyword research, including demand, competition, CPC, and bid estimates
- Web research for current public-page and landing-page evidence
- Follow-up analysis across report results
- Private memories for reporting preferences and business context

Access is read-only by default: a newly connected AI client cannot change campaigns, budgets, bids, ads, analytics properties, Search Console data, or Merchant Center products. In [AI client settings](https://unfetch.com/ai-clients) you can allow a client to propose account changes, which you approve or reject in Unfetch, or to apply changes directly. Account changes also require admin access to the brand and a paid plan. Personal memory tools can save or delete private reporting preferences in your Unfetch account.

## Before you install

1. [Sign in to Unfetch](https://unfetch.com/login).
2. Create or select a brand, then open **Integrations** in that brand's navigation to connect its data sources. [Create a brand](https://unfetch.com/add-brand) if you do not have one yet.
3. Confirm that your [team membership and brand access](https://unfetch.com/team) include every brand you want the assistant to use.

OAuth opens automatically when a supported client connects. Access always follows your current Unfetch team membership and brand assignments.

## Install in ChatGPT and Codex

Install Unfetch once from the ChatGPT plugin directory for ChatGPT web, ChatGPT desktop and Codex:

1. Open [Unfetch in ChatGPT's plugin directory](https://unfetch.com/plugin/chatgpt) and select the plus button to install.
2. Connect your Unfetch account and complete authorization when prompted.
3. Start a new chat in ChatGPT, or a new Codex session, and ask for Unfetch.

The installation includes the reporting skill and MCP connection.

## Install in Claude

Add Unfetch once to your Claude account:

- **Claude web:** open [Unfetch in Claude's plugin directory](https://unfetch.com/plugin/claude), select **Add**, then complete authorization when prompted.
- **Claude Desktop:** open **Customize > Plugins > Discover**, search for **Unfetch**, select it, then click **Add**.
- **Claude Code:** sign in with the same Claude account. Restart Claude Code or run `/reload-plugins` if Unfetch is not available immediately.

If account sync is unavailable, install directly from GitHub by running these commands inside Claude Code:

```text
/plugin marketplace add unfetch-com/agent-plugin
/plugin install unfetch@unfetch-plugins
```

## Install in Gemini CLI

Run:

```sh
gemini extensions install https://github.com/unfetch-com/agent-plugin
```

Restart Gemini CLI after installation if the extension is not available in the current session.

## Install in VS Code with GitHub Copilot

1. Open the Command Palette.
2. Run **Chat: Install Plugin From Source**.
3. Enter `https://github.com/unfetch-com/agent-plugin`.
4. Review the source and confirm the installation.

You can also open **Chat: Open Customizations**, select **Plugins**, and choose **Install Plugin from Source**.

## Other MCP clients

Use the guided instructions on the [Unfetch plugin setup page](https://unfetch.com/plugin). It provides the production Streamable HTTP connection and handles OAuth without API keys or credentials in this repository.

## Access and privacy

- Manage, limit, or revoke connected AI clients and their account access from [AI client settings](https://unfetch.com/ai-clients).
- Manage members and brand access from [Team settings](https://unfetch.com/team).
- Manage data-source connections from **Integrations** inside each brand.
- Review the [privacy policy](https://unfetch.com/about/privacy) and [terms of service](https://unfetch.com/about/terms-of-service).
