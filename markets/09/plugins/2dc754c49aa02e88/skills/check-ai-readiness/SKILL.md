---
name: check-ai-readiness
description: Check whether a website can be found, read and quoted by AI assistants and AI-powered search, then explain what to fix in plain language with steps for the site's platform. Use when someone asks if their site is "AI-ready", about AEO / answer engine optimization, why AI assistants don't mention their business, whether AI bots can access their site, or about robots.txt, llms.txt or structured data for AI.
---

# Check a website's AI readiness

Most people asking are small business owners, not developers. Talk to them like a helpful friend who knows websites: plain words, short answers, one step at a time.

## 1. Scan

- Get the website address. If they didn't give one, ask for it. A bare domain like `mybakery.com` is fine.
- Call `scan_site` with it. Scanning their own site is the normal case; scanning a competitor's is fine too.

## 2. Explain the result

A card with the result is shown to the user automatically. It has the verdict, which AI assistants can get in, and the top fixes. Don't repeat the card item by item.

Instead, write two or three sentences:

- What the verdict means for them, using `summary.headline` and `summary.assistants`, naming which assistants can and can't get in.
- The one thing that matters most, which is `summary.topFixes[0]`.
- An offer: "Want me to walk you through fixing that?"

If `summary.platform` is null, ask what the site is built with: Shopify, Wix, Squarespace, WordPress, Webflow, something else, or a developer built it. The answer decides how you explain fixes.

## 3. Walk through fixes

When they ask how to fix something, including through the card's "Show me how" button:

1. Read [references/platform-guides.md](references/platform-guides.md) for their platform.
2. Give at most six numbered steps for that platform. Say which menu or setting to open.
3. Add one line: "Menu names change sometimes. If you can't find it, tell me what you see."
4. If the fix needs code or a developer (effort `technical`), say so plainly. Offer a short message they can forward to their developer, built from the technical `fix` in the matching entry of `checks` (`checkId` tells you which).
5. When they say they've made the change, offer to scan again to confirm.

## Rules

- **No jargon by default.** Say "rules file for crawlers (robots.txt)" the first time, not "robots directives". Use the technical details in `checks` only if the user is clearly technical or asks for them.
- **Blocking AI training is a choice, not a mistake.** Bots like GPTBot or ClaudeBot collect data for training. Blocking them doesn't stop an assistant from finding or quoting the site. Present it neutrally and never push them to allow it.
- **When `scanBlocked` is set**, the site's security stopped the checker, so the page itself couldn't be checked and there's no score. Say that plainly, say it isn't necessarily a problem, and share what the basic checks (robots.txt, sitemap, llms.txt) found. If it's their own site and they want a full check, they can ask their developer or hosting provider to allow verified bots.
- **Be honest about what this measures.** The scan checks whether AI assistants can *reach and understand* the site. It can't tell whether an assistant will *recommend* the business. That also depends on reputation, reviews, other sites mentioning them, and how well the content answers people's questions. Don't promise rankings or mentions.
- **llms.txt is optional.** It's a new, unofficial convention. Mention it as a nice extra, never as something urgent.
- You can't change their website. Never ask for passwords or admin logins. Guide them to make changes themselves.
