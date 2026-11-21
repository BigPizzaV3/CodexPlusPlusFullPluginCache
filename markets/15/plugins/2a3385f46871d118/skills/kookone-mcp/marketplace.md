# Marketplace

One company has one cart, shared with the website. A product (`productId`) can be sold by several suppliers. Each offer is one `supplierId` and one or more variants (`variantId`; 0 is the base format). The cart row is `productId` + `variantId` + `supplierId` from a single result. Never guess the triple.

The caller never sends a price. `price` is the supplier standard selling price. `priceLists` are lists reserved to this company. The cart applies the standard price or the lowest applicable list.

Do only what the user asked. Adding products, raising quantities, substituting a product or supplier, changing the delivery address or the shipping option are proposed to the user, never done on your own initiative.

## Find something to buy

1. Choose the company as in [SKILL.md](SKILL.md). `list_companies` when it is unknown.
2. `search_products` with `useCartShippingZone=true` when the user wants to buy, so stock, prices and `isDeliverable` use the cart delivery address. Names and descriptions come from the Italian catalog; translate them in the reply when the user writes in another language. `months` (1–36) keeps only products the company ordered in the last N months; omit it to search the whole catalog.
3. Prefer an offer with `isDeliverable=true`. When several suppliers match, prefer one already in the cart or marked favorite, so its minimum order is easier to reach.
4. `get_product` when the search is not enough: ingredients, facts, gallery, more offers. Offers are capped (search returns up to the server limit, `get_product` up to twice that). `offersTruncated` can be true on both. Pass `supplierId` to read one supplier, or `search_products` with a `SupplierId` filter (`supplierId` from `list_suppliers`).
5. `list_categories`, `list_brands`, `list_price_lists` and `get_price_list_items` narrow or explain a price. They do not replace the offer triple.

Show name, supplier, variant, price, stock, `isDeliverable`, and the returned `productUrl` and `imageUrl`.

An empty result is empty: say nothing was found. Do not fill it with products from memory.

## Paging and truncated lists

- `search_products` pages with `page` (from 1) and `pageSize`; `totalCount` is the total.
- `get_cart` pages its rows with `itemsSkip` (default 0) and `itemsLimit` (default 50, max 100). When `itemsPage.hasMore` is true, call again with `itemsSkip` = `itemsPage.skip` + `itemsPage.limit`. Totals, `suppliers[]` and `warnings` always cover the whole cart, not only the page.
- Other lists take `skip` and `limit` and return `page.hasMore`; read the next page with `skip` + `limit`.

When a list is truncated (`offersTruncated`, `hasMore`, `truncated`), read the next pages or say the answer covers only what was read. Do not call something the cheapest, the only one or missing from a partial list.

## Amounts

Price fields (`price`, `priceInUnitOfMeasure`, `unitPrice`, `standardUnitPrice`, `calculatedUoMPrice`, `minimumOrderThreshold`) are objects with `amount`, `currency` and `unitOfMeasure`. Use `amount` with its `currency`. Cart `totals` are plain numbers in `totals.currency`. Never add amounts in different currencies. A missing `amount` is unknown, not zero: say the price is not available.

## Units and quantities

- `PerUnit`: price per piece or pack. Cart quantity is pieces or packs.
- `UoM`: price per kilogram or liter. `calculatedUoMPrice` is price times `unitOfMeasureValueMax` and is what cart totals use. Cart quantity is still pieces or packs, not kilograms.

Compare two prices only on the same unit. When the units cannot be converted from the data returned, show both prices with their units and do not claim a saving.

A cart write sets the quantity. It does not add to the quantity already in the cart. To add N more, read `get_cart` and pass current + N.

- One row: `set_cart_item_quantity`.
- Two or more rows: `update_cart`, one atomic call (all rows or none). Quantity 0 removes a row.
- One row out: `remove_cart_item`. The whole cart, only when the user asks for it: `clear_cart`.

After every write, read issues. `get_cart` returns `items[].issues`, `warnings` and `suppliers[]` at the root. `update_cart` and `clear_cart` nest them under `cart`, and `update_cart` reports each requested row in `rows[].outcome`: `applied`, `removed`, `unchanged`, `insufficient_stock` (with `availableQuantity`), `not_purchasable`, `not_found`. Report every row that was not applied. Issue codes include `SellingZoneNotAvailable`, `QuantityNotAvailable` and `PriceChanged`.

In the cart, `unitPrice` is the price applied, `standardUnitPrice` the standard one, `priceListId` the list used. Totals separate items, shipping, discounts, VAT and total. They are indicative until checkout on the website.

## Concurrent changes

The cart is shared with the website, so it can change between two calls.

- Only `update_cart` accepts `expectedCartVersion`. Pass the `cartVersion` returned by the previous `update_cart`; the change is refused when the cart changed in between. Retrying the same `update_cart` is safe.
- `get_cart` does not return `cartVersion`, and `set_cart_item_quantity`, `remove_cart_item` and `clear_cart` have no version check. Do not promise the same protection on them.
- When `update_cart` is refused for a version conflict, read `get_cart` again, show the user what changed, and write again only if the user's intent still holds on the new cart.

## Minimum order

`suppliers[].minimumOrderThreshold.amount` is the total net amount that supplier requires, in `minimumOrderThreshold.currency`. It is not the amount still missing. With a 150 EUR minimum and 100 EUR of that supplier's items, the threshold is 150 and 50 EUR is still missing.

When `minimumOrderStatus` is `MinimimOrderNotEnough` (the value is spelled this way), the missing amount is the threshold minus the sum, over that supplier's items on every page of `get_cart`, of quantity times `calculatedUoMPrice.amount` when set, otherwise `unitPrice.amount`. When an amount is missing or the currencies differ, do not compute the gap: say the minimum is not reached and show the threshold.

Reaching a minimum means buying more. Propose products or quantities; add them only after the user agrees.

## Suppliers

`list_suppliers` and `get_supplier` return the company's preference for each supplier; `list_suppliers` with `onlyFavorites=true` lists the favorites.

`set_supplier_preference` takes `supplierId` from `list_suppliers`, `get_supplier` or `search_products`, and `preference` `favorite`, `hidden` or `none` (`none` clears the mark). Set it only when the user asks, and hide a supplier only on an explicit request.

## Delivery

The delivery address decides zones, stock and shipping.

1. `list_shipping_addresses`, then `set_cart_delivery_address` with the address the user chose.
2. Before `create_shipping_address`, call `search_localities` when the comune name may be ambiguous. `create_shipping_address` creates a new address on every call: list first, and after an error list again before retrying.
3. `update_shipping_address` and `delete_shipping_address` change the address book, only on request.
4. `list_shipping_options`, then `select_shipping_option`. `apply_promo_code` and `remove_promo_code` change the discount.

`SellingZoneNotAvailable` means that supplier does not deliver to the cart address. Say so and propose another supplier or address; do not change either without the user.

## Checkout on the website

Use `check_checkout_readiness` while building the cart. It explains what blocks the order. Typical blockers: `CART_EMPTY`, `NO_DELIVERY_ADDRESS`, `SHIPPING_NOT_COMPUTED`, `MINIMUM_ORDER_NOT_REACHED`, `ITEM_ISSUES`. Tell the user each blocker and the tool that would fix it. Do the fixes the user asked for or agrees to, then read the cart again.

When the cart has no blocking issue, give the user `cartUrl`. Tell them they still have to place the order and pay on the KOOKone website. Do not say that an order or a payment has already been made.

Ordering and payment are always done on the website for this release. Do not call `prepare_checkout`, `place_order`, `get_payment_status`, `cancel_payment` or `pay_order`, even if they appear in the tool list.

## Marketplace orders

`list_orders`, `get_order`, `track_order`, `get_order_invoice`, `get_spending_summary` and `reorder` are not part of this connector. Do not offer to look up, track, invoice or pay a marketplace order from the chat. Invoice spend is `get_consumption_summary` in [procurement.md](procurement.md), and only when that tool is listed.
