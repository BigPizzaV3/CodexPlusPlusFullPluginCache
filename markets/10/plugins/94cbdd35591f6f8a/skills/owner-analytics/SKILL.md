---
name: owner-analytics
description: Analyzes a connected CrumbPass restaurant's performance, offers, customer retention, visit patterns, and referrals using privacy-safe owner MCP read tools. Use when an owner asks how the business is doing, what changed, which campaign worked, why repeat visits changed, or which guests are inactive.
---

# Owner analytics

The connected restaurant is fixed by OAuth. Never ask for or attempt to inspect another restaurant. Referral tools report performance only; they cannot create or edit referral campaigns. Permanent offer deletion is not available through this integration.

1. Start with `get_business_performance`. Use 7 days for a weekly question, 30 days for a monthly question, or the period explicitly requested.
2. For guest behaviour, call `get_customer_insights`. Use `list_customers` only when a named segment is needed; do not request or expose full contact details.
3. For campaign questions, call `list_offers` and compare offer uses, revenue, discount given, and share of bills. For sharing questions, call `get_referral_stats`.
4. State what the data shows, the comparison period, and any data-limit note. Treat low sample sizes as inconclusive.
5. Give no more than three evidence-based next actions. Do not create, activate, or change an offer unless the owner separately asks.

## Privacy

- Customer results contain names and at most the last four phone digits. Do not reconstruct, guess, or solicit complete phone numbers or email addresses.
- Do not use segments for unrelated profiling or contact-list extraction.
- Aggregate findings are preferred when a named-customer list is not necessary.

## Example

For “Why are repeat visits falling?” call `get_business_performance` and `get_customer_insights`, then explain the measured change, retention rate, inactive repeat guests, and visit pattern. Offer to propose a campaign; do not create it yet.
