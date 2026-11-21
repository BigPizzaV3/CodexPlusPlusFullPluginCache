---
name: ai-assistant-traffic
description: Report how many visits a site gets from AI assistants (ChatGPT, Perplexity, Gemini, Claude, Copilot) using Google Analytics 4, compared with the previous period and with organic search, and check that AI crawlers can reach the site. Use when the user asks if they get traffic from ChatGPT or AI search, how AI visits are trending, or whether AI bots can read their site. Requires the DidYouSEO MCP connector with Google Analytics connected.
---

# AI assistant traffic

Show what AI assistants actually send to the site, and whether anything blocks them.

## Tools

- `list_sites` - the sites in the account.
- `get_ga4_organic_traffic` (website, days=28) - organic sessions, engagement, key events and landing pages, plus sessions from AI assistants by source, for this period and the one before.
- `check_robots_txt` (url) - the robots.txt rules that apply to each crawler.

## Steps

1. If the user didn't name a site, call `list_sites` and ask which one.
2. Call `get_ga4_organic_traffic` with `days: 28`. If the user asks about a longer trend, use 90.
3. Report:
   - total AI-assistant sessions this period and last period, with the change
   - each AI source with its sessions and key events
   - AI sessions as a share of organic search sessions
4. If AI sessions are zero or very low, call `check_robots_txt` on the homepage. Check these crawlers: OAI-SearchBot and ChatGPT-User (ChatGPT search and browsing), GPTBot (OpenAI training), PerplexityBot, ClaudeBot and Claude-User, Google-Extended, Bingbot (Copilot uses Bing's index). Say which are blocked. Blocking OAI-SearchBot removes a site from ChatGPT search answers; blocking GPTBot only affects training.
5. Point out the organic landing pages with the most sessions. Pages that already earn search traffic are the likeliest to be cited by AI too, so they are the first to keep current.
6. Be clear about what GA4 can't show: AI answers that mention the site without a click never appear in analytics.

## Output format

```
AI assistant visits, last 28 days: <n> (<+/-x%> vs previous 28 days)
By source: ChatGPT <n>, Perplexity <n>, ...
Share of organic search: <x%>

Crawler access: <all allowed | list of blocked crawlers and what it means>

Next: <one or two actions>
```

## Limits

- On the Free plan the Google Analytics tool returns a short preview of landing pages. Say so if the list looks short.
- `check_robots_txt` counts as a page check. If a tool says "Daily limit reached", stop, tell the user the limit resets at 00:00 UTC, and finish with what you have.
- Don't mention prices or upgrades. If the user asks how to get more, say plan details are on didyouseo.com.
