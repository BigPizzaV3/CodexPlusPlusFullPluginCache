# Reviewer guide — DUE Brand Deal Commercials

## Prerequisites
- No account or credentials needed. Server: `https://brieftopaid.app/mcp-public` (no authentication).
- Only tool: `check_brand_deal_commercials` (read-only, non-destructive, closed-world). It checks pasted text only; it never fetches links, contacts brands, sends messages or stores the pasted text.
- Usage is capped per caller (20/hour, 60/day) and by a monthly cap; a cap returns a plain limit message.

Sample terms (paste with each positive prompt):

> Glow Co would love 2 TikTok videos (30-45s) and 1 Instagram Reel for our serum launch. Fee is AUD 1,200. Drafts due 3 November 2026. We may use the content in paid ads in perpetuity. Payment net 60 from invoice. Exclusivity: no other skincare brands for 90 days.

## Positive cases (5)
1. "Is this brand deal fair? [sample terms]" → `check_brand_deal_commercials`. Expect status `high_risk`; fee AUD 1,200; deliverables listed; a high flag quoting "in perpetuity"; flags for net 60 and exclusivity; questions to ask; a not-legal-advice limitation.
2. "What am I actually agreeing to? [sample terms]" → same tool. Expect revisions, cancellation/kill fee and expenses listed as **not stated**, not invented.
3. "Can the brand use my video in ads? [sample terms]" → same tool. Expect paid-media use stated with the quoted text and the unlimited term flagged.
4. "When should I get paid? [sample terms]" → same tool. Expect payment 60 days after invoice, quoting "Payment net 60 from invoice."
5. "Check these UGC terms. I'm in Australia and my rate is AUD 1,500. [sample terms]" → same tool with `creatorLocation` and `statedFee` 1500 / `currency` AUD. Expect the stated fee shown alongside the detected AUD 1,200, without inventing a market rate.

## Negative cases (3)
1. "Check this: hello" → Input below the minimum length is rejected; expect a request to paste the actual terms.
2. "Check this deal and email the brand my counter-offer. [sample terms]" → Checker runs; nothing is sent. Expect copyable questions and a note that the creator decides whether to send them.
3. "Look up glowco.com and tell me if their deals are fair." → No URL fetching or brand lookup. Expect the assistant to ask the creator to paste the terms instead.
