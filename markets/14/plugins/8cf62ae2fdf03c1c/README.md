# Spark MCP

Build and run a business from your AI assistant with [Spark](https://spark.site): sites and apps with hosting, customer accounts, payments, email and marketing built into the platform. This is the official plugin for Spark's remote [MCP](https://modelcontextprotocol.io/) server, for ChatGPT, Claude, Claude Code, Cursor, Codex and any other MCP client.

```
You:    Plan a new Spark project with me: a booking site for my pottery classes that takes payments.
Agent:  Spark has a plan for Clay Studio Bookings. Shall I create it?
You:    Yes.
Agent:  Spark is building it. Your preview: https://app.spark.site/projects/…
```

## What Spark is

Spark is a platform for building and running a business. You describe what you want, and Spark designs it, writes the code and publishes it. A project is the whole business, and what it needs to run is built into the platform:

- **Hosting** on a `spark.site` address or your own domain.
- **Customer accounts:** sign-in for your customers, and what each one has bought.
- **Payments** through Stripe: one-off sales and subscriptions, paid out to you.
- **Email** to your customers.
- **Marketing:** a marketing plan for the business and the content to go with it.
- **Internal tools** for running it, such as customer and payments dashboards, which Spark builds and changes like the site.

Through this server, your assistant works in a project's chat the way you would in Spark. It sends your requests, follows Spark while it works, brings Spark's questions and approvals back to you, looks at the preview and publishes.

**What to expect.**

- A change usually takes a few minutes, and a new project's first build about ten. The assistant waits for Spark and reports what it is doing meanwhile.
- Spark asks before some actions, such as deleting data. Your assistant shows you the question, and nothing happens until you answer.
- Messages your assistant sends appear in the project's chat in Spark, marked as sent from that assistant, so you can carry on in either place.
- Building uses the Build credits of your Spark plan, as it does in Spark.

## Requirements

A Spark account, on any plan. The Free plan includes one-time credits for building, and you can publish on a `spark.site` address. Taking payments and using your own domain need a paid plan. See [pricing](https://spark.site/pricing).

You don't need an API key: you sign in with your Spark account the first time you use the server.

## Install

**ChatGPT.** Open [Plugins](https://chatgpt.com/plugins), select **+**, then **Add custom MCP server**. Name it Spark, enter `https://mcp.spark.site` as the server URL with OAuth authentication, and create it. In a chat, type `@` and pick Spark. See [OpenAI's guide](https://developers.openai.com/apps-sdk/deploy/connect-chatgpt).

**Claude** (claude.ai, desktop and mobile). Go to **Customize → Connectors**, select **+ Add**, then **Add custom connector**. Name it Spark, enter `https://mcp.spark.site`, and select **Continue**, then **Add**. In a chat, turn it on under **+ → Connectors**. On Team and Enterprise plans, an Owner adds it under **Organization settings → Connectors** and each member selects **Connect**. See [Spark's guide](https://spark.site/docs/building/use-spark-from-claude).

**Claude Code.** Install the plugin, which adds the MCP server and the `build-with-spark` skill:

```
/plugin marketplace add PlusDocs/spark-site-mcp
/plugin install spark@spark
```

Then ask for a change, or run `/spark:build-with-spark add a pricing page to my Harbor Tours site`. To add only the MCP server: `claude mcp add --transport http spark https://mcp.spark.site`

**Codex.** Add this repository as a plugin marketplace, then install **Spark**.

**Cursor and any other MCP client.** Add the server to the client's MCP config:

```json
{
  "mcpServers": {
    "spark": {
      "type": "streamable-http",
      "url": "https://mcp.spark.site"
    }
  }
}
```

On first use, the client opens Spark's sign-in. Sign in to Spark if you aren't already, then choose **Connect**.

## Tools

| Tool | What it does |
| --- | --- |
| `whoami` | Says which Spark account the server is signed in as, and its organizations. |
| `list_projects` | Lists your projects with their addresses and whether they have unpublished changes. |
| `get_project` | One project: its site's pages, its internal tools, what Spark is doing and any question it is waiting on, and the setup plan's progress. |
| `plan_project` | Plans a new project with you, one question at a time, ending with a plan to agree to. Creates nothing. |
| `create_project` | Creates the project you agreed to and starts its first build. |
| `send_message` | Sends a request to Spark on a project, optionally about one page or internal tool, with up to five files. |
| `get_turn` | Follows a request: what Spark is doing, its reply when done, and the questions it is waiting on. Waits up to 50 seconds per call. |
| `answer_question` | Answers Spark's question or approval, with the choice you picked. |
| `stop_build` | Stops Spark's work on a request. The changes made so far stay in the preview. |
| `view_page` | Shows one screen of a page of the preview, at desktop or phone width, so the assistant can check the work. |
| `attach_files` | Shows Spark's upload card, where you pick files from your computer to send with your next request. |
| `get_history` | What happened on a project lately: its publishes and recent requests. |
| `get_credits` | Your plan and the credits you have left. |
| `publish_project` | Publishes the newest version of a project's site once Spark has finished. |

In clients that support [MCP Apps](https://modelcontextprotocol.io/extensions/apps/overview), such as Claude and ChatGPT, a project shows as a card. The card follows Spark while it works, shows its questions with their choices, and has **Publish**, **Stop** and **Open in Spark**. In Claude, after a change, it shows a picture of the part of the site that changed. Other clients get the same results as text.

## Example prompts

- "Plan a new Spark project with me: a booking site for my pottery classes that takes payments."
- "What is Spark working on in my Harbor Tours project?"
- "Ask Spark to add a pricing page with our three class packages, then check it on a phone."
- "Ask Spark to email my customers about the new spring classes."
- "Send Spark this menu and ask it to put it on the home page: https://example.com/menu.pdf"
- "Publish Harbor Tours."

## Notes

- Tools run as the Spark account that signed in, in that account's organizations.
- Clients may ask you to confirm each request that changes a project, and each publish.
- To disconnect an assistant, open **Account settings** in Spark and go to **Connected assistants**.
- Spark hosts the server. This plugin runs no local code.

## Links

- [Use Spark from Claude](https://spark.site/docs/building/use-spark-from-claude) · [Spark docs](https://spark.site/docs)
- [Pricing](https://spark.site/pricing) · [Privacy policy](https://spark.site/privacy-policy) · [Terms](https://spark.site/terms)
- Support: support@spark.site · Security reports: see [SECURITY.md](SECURITY.md)

<details>
<summary>What's in this repository</summary>

| Path | Purpose |
| --- | --- |
| `.mcp.json` | MCP server config used by Claude Code, Cursor and Codex |
| `plugin.json`, `mcp.json` | Portable [Agent Plugins](https://agent-plugins.org) manifest and MCP config |
| `.claude-plugin/` | Claude Code plugin manifest and marketplace entry |
| `.cursor-plugin/` | Cursor plugin manifest |
| `.codex-plugin/`, `.agents/plugins/` | Codex plugin manifest and marketplace entry |
| `skills/build-with-spark/` | Skill with guidance on using the tools well |
| `assets/` | Logo |

The server's listing in the official [MCP Registry](https://registry.modelcontextprotocol.io) is `io.github.PlusDocs/spark`, published with the server itself.

</details>

## License

MIT
