---
name: commonplace
description: Find large used items (fitness equipment, furniture, hot tubs, golf carts) on Commonplace with the delivered price to a ZIP, or help a seller price, list and manage an item.
---

Use the Commonplace tools when the person asks to find, price, buy or sell a large second-hand item.

Finding an item:
- Use catalog_search_listings. Pass deliver_to (a ZIP or "City, ST") whenever the person says where it would go, so prices include delivery.
- For "under $X" pass max_price_usd as X minus one cent.
- Use catalog_get_listing for full detail and delivery_quote_listing for a delivery quote to one place.
- Purchases are completed on trycommonplace.com. Give the person the listing link; do not ask for payment details.

Selling:
- Use listing_resolve_category first, then pricing_quote_payout to turn a take-home into the buyer price.
- Every tool that changes something needs confirmed: true. Call it first without confirmed to show a preview, and set confirmed to true only after the person agrees to that exact change.
- Payments, payouts, passwords and contact details are out of reach of these tools.

Questions about delivery, inspection, returns or fees: use support_search_help and quote platform_policy.
