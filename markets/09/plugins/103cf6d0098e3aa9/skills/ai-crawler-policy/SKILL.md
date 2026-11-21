---
name: ai-crawler-policy
description: Help a site owner decide which AI crawlers to allow or block in robots.txt, separating training crawlers from AI search and user-triggered fetchers, and draft the rules.
---

# Choosing an AI-crawler policy

Use this when the user asks which AI bots to allow or block, whether blocking GPTBot hurts them, or for robots.txt rules for AI crawlers.

## Check the current policy first

Run `check_robots_txt` on the domain the user named. Report what it found, then explain the choices. If the tool says it could not read robots.txt, say that is a fetch failure, not proof the file is missing, and do not retry.

## The three kinds of AI crawler

Explain the choice in these terms. They have different trade-offs:

1. **Training crawlers** collect content to train models. Examples: GPTBot, ClaudeBot, CCBot, Google-Extended, Applebot-Extended, Meta-ExternalAgent, Bytespider. Blocking them keeps content out of future training data. It does not remove the site from AI search answers.
2. **AI search and citation crawlers** build the indexes that answer engines cite. Examples: OAI-SearchBot (ChatGPT search), Claude-SearchBot, PerplexityBot, Applebot, Bingbot, Googlebot, DuckAssistBot. Blocking them removes the site from those answers and links. Most sites that want AI visibility should allow these.
3. **User-triggered fetchers** load a page when a person asks an assistant about it. Examples: ChatGPT-User, Claude-User, Perplexity-User, Google-Agent. Several operators document that robots.txt may not apply to these requests, so a block may not be enforced.

A common setup for a business that wants to be found in AI answers: allow search, citation and user-triggered crawlers, and decide training on its own merits. Present this as an option, not a rule. Publishers with licensing concerns often block training and allow search.

## Drafting the rules

- Use one `User-agent` group per crawler with `Disallow: /` to block or `Allow: /` to allow.
- Under RFC 9309 a crawler follows only the group that names it. The `User-agent: *` group applies only to crawlers with no group of their own. A site with `Disallow: /` under `*` therefore blocks every AI crawler that is not named, so add explicit `Allow: /` groups for the crawlers the user wants.
- Keep the user's existing rules and `Sitemap:` lines. Show the full new file, or a clear "add this" block.
- Blocking Googlebot or Bingbot also removes the site from normal search. Never suggest blocking them as an AI measure. Google-Extended is the separate token for Google's AI training.

## Limits to state

- `check_robots_txt` reports the stated policy only. It does not test what the site actually serves each crawler. A firewall or bot manager (for example Cloudflare's AI bot blocking) can block crawlers that robots.txt allows. If the user's AI visibility is low despite an open robots.txt, suggest they check those settings.
- robots.txt is a request, not access control. Compliant crawlers follow it; others may not.
