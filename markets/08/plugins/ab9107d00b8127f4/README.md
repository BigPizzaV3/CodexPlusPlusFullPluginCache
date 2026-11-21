# DemoPage plugin

Published under the AtomsAI developer identity. DemoPage is operated by SaaS Labs US, Inc.; its legal operator and contact details are on the [Privacy Policy](https://demopage.io/privacy) and [Terms of Service](https://demopage.io/terms).

[DemoPage](https://demopage.io) gives your website visitors a live, narrated demo inside your real product. This plugin lets your AI coding tool build that demo from your code. It maps every screen from your routes, navigation, UI text, and end-to-end tests, writes what each page lets a customer do, and sends the pages to your DemoPage as candidates. You approve the ones buyers should see, and your demo link turns on.

It works in Cursor, Claude Code, Codex, and ChatGPT.

## What's inside

- **The DemoPage MCP server** at `https://app.demopage.io/mcp`. It acts for your DemoPage account only, after you choose "Sign in with DemoPage" and allow the tool.
- **`create-demopage` skill.** Maps the repo, imports the pages, asks you what to approve, then fixes pages that fail their check.
- **`demopage-results` skill.** Summarizes demo visits, leads, and what buyers asked, and suggests which screens to add next.

The same two guides are offered as prompts by the MCP server, so a tool connected without the plugin gets them too.

## What gets sent, and what doesn't

When this plugin runs in a coding client that can read your local repository, your source files stay in that client. The client sends DemoPage the candidate-page fields you review: a title, canonical query-free https address, short visible proof text, one or two sentence description, whether sign-in is needed, optional keywords or click path, and a short note naming the kinds of local sources used. It does not send source files, repository credentials, environment values, or secrets.

The MCP connection itself does not grant repository access. A client without a local filesystem or deliberately attached source files can manage your DemoPage account, but it cannot honestly map code. Once connected, it can read your DemoPage status, catalog, link, readiness results, and the last 30 days of results, including the latest leads. DemoPage stores the connected tool's registered name and connection/last-use times; standard server request times and errors may appear in operational logs. The [Privacy Policy](https://demopage.io/privacy) covers retention and recipients.

Nothing a tool sends goes into a demo by itself. Every page waits for your approval, then it's loaded in a demo browser. If the expected text isn't on the page, the page stays out. Demos never save, send, pay, or delete anything, and checkout, billing, API key, password, and sign-up screens are refused.

## Before you start

You need a DemoPage account. [Start free](https://app.demopage.io/signup) with your work email (no card), or [talk to us](https://demopage.io/early-access). Signed-in pages also need a demo login for your product, which you add in the [portal](https://app.demopage.io/portal), step 5. The [setup guide](https://demopage.io/docs) covers the rest.

## Install

### Cursor

Once DemoPage is listed in the Cursor Marketplace, install it from **Customize**. Until then, copy the `demopage` folder to `~/.cursor/plugins/local/demopage` and run **Developer: Reload Window**.

For the MCP server alone, open the portal's step 6 and choose **Add to Cursor**, or add this to `~/.cursor/mcp.json`:

```json
{ "mcpServers": { "demopage": { "url": "https://app.demopage.io/mcp" } } }
```

Then open **Settings → MCP** and choose **Connect** next to `demopage`.

### Claude Code

Add the AtomsAI marketplace, then install the plugin:

```bash
claude plugin marketplace add gaufire/demopage-plugins
claude plugin install demopage@atomsai
```

To try it from a local copy, run `claude --plugin-dir ./demopage`. Then run `/mcp`, pick `demopage`, and choose **Authenticate**.

For the MCP server alone: `claude mcp add --transport http demopage https://app.demopage.io/mcp`.

### Codex

Add the AtomsAI marketplace, then install DemoPage from the Plugins directory:

```bash
codex plugin marketplace add gaufire/demopage-plugins
```

For the MCP server alone:

```bash
codex mcp add demopage --url https://app.demopage.io/mcp
codex mcp login demopage
```

### ChatGPT

1. Open **Settings → Security and login** and turn on **Developer mode**.
2. Open **Plugins**, choose **+**, and enter `https://app.demopage.io/mcp` with OAuth.
3. Sign in with DemoPage and choose **Allow**.

## Use it

Open your product's repo and ask:

- "Build my DemoPage from this repo."
- "Which demo pages failed their check, and how do I fix them?"
- "What did buyers ask in DemoPage demos this month?"

You can see and disconnect every connected tool in the portal, step 6. Resetting your DemoPage password disconnects all of them.

## Tools

| Tool | What it does |
| --- | --- |
| `demopage_status` | Your website, whether the demo is live, page counts, the last page check, the demo link, and the next step. |
| `demopage_list_pages` | Every page, with its id, approval, and last check. |
| `demopage_import_pages` | Adds mapped pages as candidates, or corrects pages mapped earlier. Nothing goes live from this. |
| `demopage_approve_pages` | Approves or holds pages. Before go-live, this also turns the demo link on. |
| `demopage_check_pages` | Loads every approved page in a demo browser. |
| `demopage_read_site` | Reads your public website again (before go-live). |
| `demopage_get_link` | Your demo link and the embed snippet for your website. |
| `demopage_results` | The last 30 days of visits, demos, questions, pages kept out, and leads. |

## Privacy and terms

[Privacy Policy](https://demopage.io/privacy) · [Terms of Service](https://demopage.io/terms)

## License

MIT
