# Review test cases

Run these against https://mcp.kookone.com/mcp. Each case starts in a new chat and uses the prompt below word for word. The same prompts are in `.codex-plugin/plugin.json` under `extensions.com.openai.review.test_cases`. `tools_triggered` is the comma-separated list the reviewer must see; extra tools such as `get_company_plan` or `list_companies` may also run. `prepare_checkout`, `place_order`, `pay_order`, `list_orders`, `track_order` and the other order tools must be absent from `tools/list`.

`demo_recording_url` in the manifest is `https://images.kookone.com/images-container/demovideo/demo_recording.mp4`. An empty value would clear a URL already saved in the portal.

## Test account

Prepare one synthetic customer. Credentials go only in Review details, not in this package.

- One company whose plan includes `CONSUMPTION_ANALYTICS` and `MARKETPLACE_ALTERNATIVES`. Sign-in works immediately, without MFA, email or SMS.
- Two saved shipping addresses. The first, Sede in Genova, is in a zone served by at least one in-stock offer for aperol 1L bottiglia and is already the cart delivery address, so the search case does not depend on the address case. The address prompt uses that first address. The second address is not selected.
- The aperol 1L bottiglia offer may already be in the cart at a quantity other than 2. A correct run sets the quantity to 2. A later run must still set 2, not add 2.
- The demo purchase invoices: 12 invoices from 8 September to 4 November 2026, three suppliers, 55 products. The largest spend is Caffè in grani 85% arabica 1 kg (`productCode` `CAF-ARB85-1KG`), priced per kg, so `get_consumption_summary` returns it in the top ten. `list_consumption_products` pages 50 rows, so the first page of this period has `page.hasMore` true.
- Two recipes costed from those invoices: Caffè espresso (7 g of that coffee and 4 g of sugar sachets) and Cappuccino (7 g of coffee and 150 ml of UHT whole milk). Selling prices are on the dine-in channel.
- At least one KOOKone marketplace alternative for that coffee, priced per kg, so a price comparison is possible.
- No real customer, card, or payment token.

## Positive

1. **Search deliverable products.** Prompt: "Find aperol 1L bottiglia I can order for my company and show only offers that can be delivered to my cart address. For each offer list supplier, variant, price, stock, whether it is deliverable, and the product link." Tool: `search_products`. Expect offers for aperol 1L bottiglia that can be delivered to the cart address already set on the account. Each offer shows supplier, variant, price, stock, `isDeliverable` and the returned `productUrl`. At least one offer is deliverable. No keg and no other format. No `productId`, `variantId` or `supplierId` is invented.

2. **Set a quantity in the cart.** Prompt: "Search for aperol 1L bottiglia and set the quantity of the first deliverable offer in my cart to 2." Tools: `search_products`, `set_cart_item_quantity`. The ids come from the search result. The quantity written is 2 and replaces any quantity already in the cart. The reply reports item issues, whether the supplier minimum order is reached, and `cartUrl`. It does not say an order was sent.

3. **Delivery address and checkout handoff.** Prompt: "Use my first saved address as the delivery address of my cart and tell me what still blocks the order." Tools: `list_shipping_addresses`, `set_cart_delivery_address`, `check_checkout_readiness`. The address id is read from `list_shipping_addresses`. The reply lists the blockers and gives `cartUrl`. It says the user still has to place the order and pay on the KOOKone website. It does not say that an order or a payment has already been made.

4. **Full spend ranking from invoices.** Prompt: "Which products did we spend the most on in our purchase invoices from September to November 2026? I want the full list, not just the top ten." Tools: `get_consumption_summary`, `list_consumption_products`. Expect the September–November 2026 total, then the products ordered by spend. The first product is Caffè in grani 85% arabica 1 kg, `productCode` `CAF-ARB85-1KG`. Products are identified by `productCode` and `supplierRef`. The first page does not cover all 55 products: the reply reads the next page or states which share of the total is still unread. The reply does not print a VAT number.

5. **Marketplace alternatives for an invoice product.** Prompt: "Find KOOKone marketplace alternatives for the coffee we buy most on our invoices from September to November 2026, and compare prices only when the unit of measure matches." Tools: `list_consumption_products`, `search_marketplace_alternatives`. The coffee is the top spend from that ranking, Caffè in grani 85% arabica 1 kg, `productCode` `CAF-ARB85-1KG`, priced per kg. `get_consumption_summary` is not required: its product list is only a preview of ten. Prices are compared only on the same unit of measure. When the units differ, both prices are shown and no saving is claimed. The cart is unchanged.

## Negative

The expected refusal is the case description. No tool should complete the request.

1. **Pay an order.** Prompt: "Pay my latest KOOKone order now with my saved card." No payment or order is made and no payment link is invented. The reply says the user still has to pay on the KOOKone website.

2. **Upload a supplier invoice.** Prompt: "Upload a supplier invoice into my KOOKone purchases." No KOOKone tool is called. The reply says the plugin does not upload invoices and points to the KOOKone website. Do not attach a file: the prompt must stand alone.

3. **Track an order.** Prompt: "Track my latest KOOKone order and tell me when it will be delivered." No order tool is called and no delivery status is invented. The reply says tracking is done on the KOOKone website.

## Before recording

Run all eight prompts on the test account. If a named tool does not run, change the prompt, update this file and `plugin.json` together, and run the prompt again. Record only a take that matches the expected result. The shot list is [demo-video.md](demo-video.md).
