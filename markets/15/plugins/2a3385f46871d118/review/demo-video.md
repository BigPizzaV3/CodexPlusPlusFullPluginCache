# Demo video

Record in **ChatGPT on the web**, at https://chatgpt.com, signed in with the test account from [test-cases.md](test-cases.md). Select the KOOKone app in the composer and start a new chat for every prompt. The tool trace has to stay visible.

The ChatGPT desktop app is acceptable only if that same app is connected and the tool names expand on screen. The review team retries the cases on chatgpt.com, so the web recording is the one to send.

www.kookone.com appears once: when a reply returns `cartUrl`, open that link in the browser and stop on the cart page. Do not type the prompts on the KOOKone website, and do not pay.

Publish the recording where a reviewer can open it without an account (unlisted video or a stable link). Put that URL in `extensions.com.openai.review.demo_recording_url` and upload the package again. A generated clip is not a substitute.

Paste each prompt word for word. Leave each tool name on screen long enough to read. Open the row **Worked for …**. The sentence “Searching … in the marketplace” is a label and does not open. The tool name is on a row inside that block, often titled with the tool title (for example “Search KOOKone products”) or “Called tool”. Do not show a password, a VAT number, a card, an OAuth token, or a real customer.

1. Connect the test account and show the one company. Hide the password. No prompt.
2. New chat. Prompt: `Find aperol 1L bottiglia I can order for my company and show only offers that can be delivered to my cart address. For each offer list supplier, variant, price, stock, whether it is deliverable, and the product link.` Show the open KOOKone trace and a deliverable 1 L bottle: supplier, variant, price, stock, `isDeliverable`, and `productUrl` taken from the tool result. No keg.
3. New chat. Before sending, the aperol 1L bottiglia row is already in the cart at a quantity other than 2; show that cart if it is already on screen. Prompt: `Search for aperol 1L bottiglia and set the quantity of the first deliverable offer in my cart to 2.` Show `search_products` and `set_cart_item_quantity` with quantity 2, then the row, the item issues, the supplier minimum, and `cartUrl`. Say that this is not an order.
4. New chat. Prompt: `Use my first saved address as the delivery address of my cart and tell me what still blocks the order.` Show `list_shipping_addresses`, `set_cart_delivery_address`, and `check_checkout_readiness`. Read the blockers and `cartUrl`. Open the link in the browser and stop on the KOOKone cart. Do not pay.
5. New chat. Prompt: `Which products did we spend the most on in our purchase invoices from September to November 2026? I want the full list, not just the top ten.` Show `get_consumption_summary` and `list_consumption_products`. The first product is Caffè in grani 85% arabica 1 kg, with `productCode` `CAF-ARB85-1KG` and `supplierRef` in frame. The first page leaves a remainder: show the next page or the unread share. Do not expand a payload that contains a VAT number.
6. New chat. Prompt: `Find KOOKone marketplace alternatives for the coffee we buy most on our invoices from September to November 2026, and compare prices only when the unit of measure matches.` Show `list_consumption_products` and `search_marketplace_alternatives`. The coffee is Caffè in grani 85% arabica 1 kg, `productCode` `CAF-ARB85-1KG`, taken from the spend ranking. Compare the marketplace offers only when both prices are per kg. The cart quantity does not change.
7. Three new chats, one prompt each. The trace stays empty of KOOKone tools, and each reply sends the user to the KOOKone website.
   - `Pay my latest KOOKone order now with my saved card.`
   - `Upload a supplier invoice into my KOOKone purchases.`
   - `Track my latest KOOKone order and tell me when it will be delivered.`

Record only after a cold run of the same prompts on the same account. If a required tool does not run, fix the prompt in the manifest before keeping the take.
