---
name: brand-deal-commercials
description: Check, review or explain the commercial terms of a brand deal, UGC brief, influencer contract or collab offer the creator pastes. Use when the creator asks things like "Is this brand deal fair?", "What am I actually agreeing to?", "Check these UGC terms", "When should I get paid?", "Can the brand use my video in ads?", or asks DUE to check a brief. Works without a DUE account.
---

# Brand Deal Commercials

Use the DUE tool `check_brand_deal_commercials` to read the terms the creator supplied. Do not answer from general knowledge alone.

## When to use
- The creator pastes a brief, offer email, contract or list of commercial terms and wants to understand it, check it or know if it is fair.
- The creator asks about fee, payment timing, usage or ad rights, whitelisting/Spark Ads, exclusivity, revisions/reshoots, kill fee, expenses or deadlines in a specific deal.

If no terms were pasted, ask the creator to paste the text (at least a few sentences). Do not fetch links, open social accounts or look up the brand.

## How to call
- `dealText`: the pasted text, unchanged. Remove passwords, bank details or personal contact details if present before sending, and tell the creator you did.
- Optional: `creatorLocation`, `currency` (ISO code such as AUD) and `statedFee` only if the creator gave them. Never guess them.
- If the text is longer than the tool allows, ask the creator which section holds the commercial terms.

## How to present the result
1. One line with the overall status: clear, needs clarification or high risk. State it calmly, without alarm.
2. What the deal states: fee and currency, deliverables, payment timing and trigger, usage and paid-media rights, exclusivity, revisions, cancellation, expenses and deadlines. Quote the evidence for anything important.
3. Keep two lists separate:
   - **Not stated**: terms that are absent. Say they are not in the text; do not call them risky and do not assume an industry default.
   - **Worth a closer look**: risk flags with their severity and the exact quoted words.
4. The questions to ask the brand, ready to copy. Make clear nothing has been sent and the creator decides whether and how to send them.
5. End with the single most useful next action from the result. Mention the free web tool or DUE signup link from the result only when it helps (for example, to keep the collab, invoice and payment date together).

## Never
- Claim a legal review, give legal or tax advice, or say a deal is "safe". Use the tool's limitations wording.
- Invent terms, prices, rates or experience the creator has not stated.
- Encourage contacting the brand, or draft a message as if it will be sent, without the creator choosing to do so.
- Claim DUE sends, signs, approves, invoices or collects payment on the creator's behalf.

If the tool reports a usage limit or that the text is not a brand deal, say so plainly and offer the free web tool link.
