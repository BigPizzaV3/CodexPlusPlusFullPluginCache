# Stora: ASO & Apple Ads

## You built the app. Put your agent to work on growth.

**More organic growth opportunities. Stronger store listings. Smarter Apple Ads decisions.**

Turn Claude Code, Codex or your supported AI assistant into an ASO and Apple Ads expert that works with your app's data. Tell it what you want to improve. Stora gives it the context to find opportunities, prepare changes and help you decide what to do next.

### Get found by the right users

Find relevant keywords your competitors win. See where your app is gaining or losing search visibility in the App Store and Google Play. Give your agent a clear brief: find the searches worth targeting and turn them into an organic growth plan.

### Give more people a reason to install

Ask your agent to turn search opportunities into localized titles, subtitles and keyword drafts grounded in what your app actually does. Keep experiments organized, review the proposed copy and publish the changes you choose.

### Make Apple Ads spend work harder

Ask where your imported spend goes, which search terms deserve attention and what to investigate next. Get a prioritized plan based on the available campaign and query data, so your next ad decision has evidence behind it.

### Keep growth moving every week

Set up a recurring task in a host that supports scheduling. Have your agent review rank changes, find new keyword opportunities, prepare listing experiments and bring you a weekly growth plan. Stora supplies the workspace data and workflows; the host runs the schedule.

Try this recurring brief:

> Every Monday, review my app's search visibility and Apple Ads data for the past week. Pick the three best growth opportunities, prepare listing experiments for my review and give me a prioritized action plan. Preserve current tracking and drafts unless I explicitly request a change.

Your agent can manage Stora tracking, drafts and experiment notes with write access. You approve and publish store listing changes and apply ad campaign changes separately. Results depend on the app, market and available evidence; recommendations do not guarantee ranking or install gains.

## Start with a goal

- “Find the best opportunities to grow my app's organic installs this week.”
- “Which relevant keywords are my direct competitors winning that I should target?”
- “Improve my App Store and Google Play listings. Prepare drafts I can review.”
- “Audit my Apple Ads spend and prioritize changes that could make it work harder.”
- “Track these terms in Google Play GB, preserving my existing tracking.”

## Connect Stora

Install the plugin in your supported host and follow **Connect Stora**. Sign in at [stora.rocks](https://stora.rocks), select a workspace and choose its access. Read access is sufficient for research and reports. Tracking, drafts and experiment notes require write access. App deletion and imports require an administrator grant. Revoke connections in Stora **Settings → Connected apps**.

For a remote connector, use [Stora's MCP endpoint](https://stora.rocks/mcp) with OAuth. Existing API keys also work for clients that explicitly support them; never put a key in this repository, a URL or a chat message.

## Install in Claude Code

```text
/plugin marketplace add smvls/stora-plugins
/plugin install stora-app-growth@stora-plugins
```

Claude's Directory listing becomes available after review. A public repository is an installation source, not proof of Directory approval.

## ChatGPT and Codex

The root `plugin.json` and `mcp.json` use the portable Agent Plugins format. A public directory listing becomes available after OpenAI review. The `.claude-plugin` and `.mcp.json` files provide Claude compatibility for the same package.

## Evidence and access

Reports identify their app, store, market, dates and evidence gaps. Apple Ads reporting requires data in your Stora workspace. Stora connects to the workspace you choose; this package contains connection settings and skills. The hosted server and customer data are not distributed in this repository.

[Support](https://stora.rocks/support) · [Privacy](https://stora.rocks/privacy) · [Terms](https://stora.rocks/terms)

The package instructions and configuration are MIT licensed. The Stora name and logo identify the service and remain trademarks of their owner.
