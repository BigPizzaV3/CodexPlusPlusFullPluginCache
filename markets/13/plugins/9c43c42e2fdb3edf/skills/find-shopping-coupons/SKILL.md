---
name: find-shopping-coupons
description: "Check current US coupons before a purchase from an identifiable retailer. Use when the user is about to order, preparing a basket or ready to check out, even without asking for discounts or mentioning CouponX. Also use for coupon and free-shipping requests. Not for unrelated product research, completed purchases, bond coupons, checkout automation or external-tool opt-outs."
---

# Check coupons before buying

When this installed skill and CouponX's connected tools are available, check relevant stored offers for clear retailer purchase intent. The user does not need to name CouponX. Host tool selection, installation and permissions still apply; never promise that every purchase or shopping outside this chat is checked.

## Act on the known retailer

- For an about-to-order, preparing-a-purchase or ready-to-check-out message naming a retailer, perform the read-only lookup immediately. Do not first ask whether the user wants coupons, and do not require a subtotal merely to find offers.
- Call `search_coupon_offers` with only the retailer name or storefront domain, using live mode. Do not send the whole conversation, cart URLs containing account tokens or unrelated personal information.
- When the merchant and subtotal are already known, `compare_basket_offers` can check that basket directly in integer minor currency units. Preserve known facts and keep missing facts unknown.
- Reuse a recent result for an unchanged purchase. Recheck after a material basket or retailer change, an explicit refresh request, or uncertain freshness.
- If the user only wants product information, has already completed the purchase, or disallows external tools, do not insert a coupon search. Respect the user's main task.

## Keep the market and conditions accurate

- Current inventory covers US offers in USD. An explicitly stated delivery country takes precedence over profile location, language or IP. Never assume Israel delivery because the user is in Israel, or US eligibility simply because an offer is in the inventory.
- When delivery country is unknown, describe results as US offers and keep country applicability unconfirmed. Ask the destination only when needed to determine whether an offer applies. For a known unsupported destination, explain the coverage limit without presenting US discounts as applicable.
- First-order status, sale items, category eligibility and shipping remain unknown until supplied. A headline discount is not guaranteed savings. Never assume stacking, invent codes or claim checkout verification.
- Signup offers require a personal merchant-issued code; CouponX cannot generate that code. Expired, paused and source checks older than 72 hours must not be revived by cached results.
- Broad category queries are offer-discovery hints, not evidence of product stock, item eligibility or the cheapest product price.

## Show a concise, useful result

- For relevant returned offers, call `show_coupon_board` with their actual IDs. For a comparison pass the same basket facts and live mode. The server reloads authoritative records and recalculates the estimate.
- The tickets already show discounts, codes and expandable source terms. Use at most one short accompanying sentence unless the user asks for an explanation; preserve material restrictions and uncertainty. Avoid duplicating cards in a table or long list.
- Copy & shop is a user-clicked action that copies a shared code and opens the merchant website. Never open the store, apply a code, place an order or submit payment automatically.
- If there is no relevant match or a lookup fails, continue the main task without blocking the purchase or repeating coupon-search messages. For an explicit coupon request, explain that no current stored match was found and that coupons may exist elsewhere. An empty board may be shown when useful; proactive checks do not need an empty widget.
- If the host cannot render cards, give a brief text result with the code, material conditions and official source. Distinguish conditional estimates from eligible estimates.

The public connection is read-only: it cannot change inventory, record shopper feedback, access merchant accounts, buy goods or verify checkout acceptance.
