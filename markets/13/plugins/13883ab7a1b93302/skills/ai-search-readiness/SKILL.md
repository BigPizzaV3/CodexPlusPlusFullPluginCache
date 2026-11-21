---
name: ai-search-readiness
description: Check whether ChatGPT, Perplexity, Claude, Copilot and Google AI Overviews can find, read and cite a page - AI crawler access in robots.txt, indexability, structured data, and a title and description that state the answer. Use when the user asks if their page is ready for AI search, why ChatGPT doesn't cite them, how to get cited in AI answers, or for a GEO or AEO check. Requires the DidYouSEO MCP connector.
---

# AI search readiness

AI assistants can only cite pages their crawlers can reach and a search index has kept. Check those basics first, then what makes a page easy to quote.

## Tools

- `check_robots_txt` (url) - the robots.txt rules that apply to each crawler.
- `run_seo_audit` (url) - indexing blockers (noindex, canonical, status code) and on-page issues.
- `validate_schema` (url) - structured data found and its errors.
- `analyze_meta_tags` (url) - title, description and headings.

## Steps

1. Get the page URL. Use the page that answers the question the user wants to be cited for, not only the homepage.
2. Call `check_robots_txt`. For each crawler, say allowed or blocked:
   - OAI-SearchBot and ChatGPT-User: ChatGPT search and browsing
   - PerplexityBot: Perplexity
   - ClaudeBot and Claude-User: Claude
   - Bingbot: Bing, which Copilot and others use
   - Googlebot: Google Search and AI Overviews
   - GPTBot and Google-Extended: model training only, not search answers. Blocking these doesn't remove the page from AI search.
3. Call `run_seo_audit`. Anything that stops indexing (noindex, a canonical to another URL, a 4xx or 5xx status) blocks AI search too.
4. Call `validate_schema`. Note Article, FAQPage, HowTo, Product, Organization or LocalBusiness where they fit the page. Structured data must match what the page shows.
5. Call `analyze_meta_tags`. Check that the title and description state the topic in the searcher's words, and that the H2 headings read like the questions people ask.
6. Give a verdict: Ready, Ready with fixes, or Blocked.

## Output format

```
Verdict: <Ready | Ready with fixes | Blocked> for <url>

Crawler access: <table of crawler, allowed/blocked, what it affects>
Indexing: <ok, or the blocker>
Structured data: <found types, errors>
Easy to quote: <title, description, headings - what to change>

Fix first: <up to 5 actions, blockers first>
```

Add: "A direct 40-60 word answer as the first paragraph, and a visible updated date, make a page easier to cite." Don't claim that any change guarantees a citation.

## Limits

- This uses 4 page checks. On the Free plan there are 10 a day. If a tool says "Daily limit reached", stop, tell the user the limit resets at 00:00 UTC, and report what you have.
- Don't mention prices or upgrades. If the user asks how to get more, say plan details are on didyouseo.com.
