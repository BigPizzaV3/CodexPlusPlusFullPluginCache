---
name: aurora-tour-finder
description: Find and compare bookable northern-lights tours or related experiences returned by AuroraReach. Use when the user asks for an aurora tour, activity, guided chase, photography experience, bookable option, price comparison, or what they can reserve near a destination. Combine offer details with AuroraReach viewing conditions when that helps choose between offers.
---

# Aurora Tour Finder

Use AuroraReach offers as the booking source and preserve its tracked URLs exactly.

## Workflow

1. Resolve destination, date, group needs, transport/pickup preferences, budget, and other constraints already present in the conversation.
2. Prefer `get_offers` for discovery and `get_offer` for details when available.
3. If the user asks which tour is best for actual aurora viewing, also use AuroraReach forecast/planning information so the recommendation reflects expected conditions.
4. Rank offers by fit to the user's constraints and viewing plan, not merely rating or price.
5. Return a small shortlist, normally three options or fewer.
6. Use the exact affiliate/booking URL returned by AuroraReach. Never construct, strip, canonicalize, or replace GetYourGuide or Viator booking URLs.
7. Make clear when booking takes place on an external provider.
8. Never imply that AuroraReach or ChatGPT completed a purchase unless an actual purchase-capable tool explicitly did so.

## Output

For each option provide the most useful returned details, such as:
- title/provider;
- price/currency;
- rating/review count;
- duration/start/pickup information;
- why it fits;
- returned booking link.

Lead with the best match and explain why in one sentence.
