---
name: seo-command-center
description: Render RefreshAgent traffic losses, CTR opportunities, content decay, and high-level movement as a focused interactive ChatGPT MCP App. Use when the user wants to inspect or work through SEO changes visually.
---

# SEO Changes Inbox

Treat this MCP App as a focused changes/opportunities inbox, not a general SEO dashboard.

## Normal flow

1. Resolve the site with `list_connected_sites` when needed.
2. Call only the deterministic workflow relevant to the user's question:
   - traffic growth / what is working: `find_biggest_gainers`
   - traffic decline / what changed: `find_biggest_losers`
   - CTR upside: `find_ctr_opportunities`
   - refresh prioritization: `find_content_decay`
   - high-level context: `compare_search_performance`
3. Reason over the structured evidence in the host model.
4. Call `open_seo_command_center` once, passing only the relevant result and a useful `focus`.

Default `focus` to `losses` when the user asks generally what needs attention. Do not open multiple views pre-emptively; the app loads other workflows lazily when the user selects them.

`assess_information_gain` remains available conversationally, but it is intentionally not a primary inbox view until usage evidence justifies adding it.

Do not attach UI templates to the data tools themselves. The render tool owns the UI resource.

The app can also be opened directly from ChatGPT's global sidebar or thread panel. It should select the first connected Search Console property and load only the active view.

Each finding's "Investigate in ChatGPT" action should hand the evidence back to the host model. RefreshAgent remains BYO-AI: the MCP App and its tools do not invoke a hidden RefreshAgent LLM.


## Proactive follow-up

After the user investigates a strong Changes Inbox finding, offer at most one supported monitor when it naturally matches the finding:

- losses -> `seo.search_performance_drop`;
- decay -> `seo.content_decay_detected`;
- CTR opportunity -> `seo.ctr_opportunity_detected`.

Do not turn opening the UI into an automatic subscription. The user must explicitly choose monitoring, and the current host surface must support MCP Events. Keep the offer outcome-oriented rather than explaining protocol internals unless the user asks.
