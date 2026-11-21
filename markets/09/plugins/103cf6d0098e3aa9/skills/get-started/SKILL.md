---
name: get-started
description: Show a new user what Glippy GEO can check and how to ask for it.
---

# Getting started with Glippy GEO

Glippy checks how ready a public website is for AI search engines and AI agents. Always work from a domain the user names. If they have not named one, ask which site to check instead of guessing.

Offer these starting points:

- **Full report:** "Check the AI readiness of example.com." Uses `analyze_domain` and shows a scored report with prioritised fixes.
- **Quick score:** "Give me a quick GEO score for example.com." Uses `get_geo_summary`.
- **Compare sites:** "Compare example.com with competitor.com." Uses `compare_domains` for 2 to 8 sites.
- **AI-crawler rules:** "Which AI crawlers does example.com block?" Uses `check_robots_txt`.
- **llms.txt:** "Does example.com have an llms.txt?" Uses `check_llms_txt`.

After a first result, these follow-ups work well:

- "What does my score mean?" or "Why is Structured Data low?" (explain-score skill)
- "Draft the top fixes for me." (draft-fixes skill)
- "Which AI crawlers should I allow?" (ai-crawler-policy skill)
- "Write an llms.txt for my site." (write-llms-txt skill)
- "How do I compare with my competitors?" (competitor-benchmark skill)

What to tell users when it matters:

- Glippy analyses the homepage and standard discovery files, not every page of the site.
- It reads only public files, identifies itself as GlippyBot, and skips sites whose robots.txt disallows GlippyBot. If a tool says it did not fetch a site, pass that on and do not retry.
- Results are cached for about ten minutes, so an immediate re-run shows the same result.
- After a report, offer to draft the top fixes (for example JSON-LD structured data or robots.txt rules) for the user to apply themselves. Glippy cannot change the site.
- Do not suggest renaming or 301-redirecting existing URLs to make slugs more descriptive or to match navigation labels. Redirects on established URLs cost more in search than a readable slug gains. Readable slugs are advice for new pages; only redirect URLs that are actually broken.
