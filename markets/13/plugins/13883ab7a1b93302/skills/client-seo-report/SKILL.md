---
name: client-seo-report
description: Write a client-ready monthly SEO report from DidYouSEO audit scores and Search Console data, in plain language with wins, problems and next steps. Use when an agency or freelancer asks for a client report, a monthly SEO summary for a client, or an update to send to a client. Requires the DidYouSEO MCP connector.
---

# Client SEO report

Write the report an agency sends a client every month. Clients read the first paragraph and skim the rest, so lead with the outcome.

## Tools

- `list_sites`, `get_site_score` - technical health and open issues.
- `get_search_console_changes` (website, days=28) - month-over-month movement.
- `get_search_console_keywords` (website, days=28) - top queries.
- `get_ga4_organic_traffic` (website, days=28) - visits, conversions and AI-assistant visits, if Google Analytics is connected.

## Steps

1. Call `list_sites` and confirm the client's site.
2. Call `get_site_score`, `get_search_console_changes` with `days: 28`, `get_search_console_keywords` with `days: 28`, and `get_ga4_organic_traffic` with `days: 28`. If Google Analytics isn't connected, leave out the conversion lines.
3. Ask the user for anything the tools can't know: work done this month, the client's goals, and the agency name to sign off with. If they don't have it, leave a clearly marked placeholder.
4. Write for a business owner, not an SEO. Replace terms like "impressions" with "times you appeared in Google" on first use.
5. Every metric needs a "so what". Cut any number that doesn't lead to a decision.
6. Be honest about drops. Explain the likely cause and the plan. Don't hide bad months.

## Output format

```
SEO report - <client> - <month year>

Summary
<2-3 sentences: overall direction, the main win, the main concern>

Results this month
- Visits from Google: <n> (<change>)
- Times you appeared in Google: <n> (<change>)
- Top searches bringing visitors: <3 queries>
- Enquiries or sales from Google visitors (GA4): <n> (<change>)
- Visitors sent by AI assistants like ChatGPT (GA4): <n> (<change>)

Site health: <score>/100 (<change if known>)
- Fixed: <items>
- Still open: <top 3>

Work completed
- [AGENCY TO FILL]

Plan for next month
1. <action and expected effect>
2. <action and expected effect>
3. <action and expected effect>
```

Output Markdown the user can paste into an email or document.

## Limits

- Audits and single-URL checks (`run_seo_audit`, `run_pagespeed_insights`, `analyze_meta_tags`, `check_robots_txt`, `validate_schema`, `serp_preview`, `check_core_web_vitals`, `check_open_graph`, `check_hreflang`) count as page checks. On the Free plan there are 10 a day. If a tool says "Daily limit reached", stop calling them, tell the user the limit resets at 00:00 UTC, and finish with the data you have.
- On the Free plan, the Search Console and Google Analytics tools return a short preview. Say the results may be incomplete.
- Don't mention prices or upgrades. If the user asks how to get more, say plan details are on didyouseo.com.
