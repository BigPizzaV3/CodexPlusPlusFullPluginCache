---
name: operate-coffee-brand
description: Manage an existing Dripshipper coffee brand's setup, artwork, packaging, connected store products, sample and bulk orders, fulfillment, invoices and support. Use when the user asks to operate their Dripshipper account.
---

# Operate a coffee brand

Connect the user's account when requested by the tool's authentication challenge. Use `get_account`, `get_setup_checklist` and `get_store_connection` to establish relevant account facts. Do not request credentials in chat or assume an account has access to a paid feature.

## Artwork and products

Use `get_branding` to inspect the current artwork and packaging options. Use `prepare_logo_generation` to prepare new concepts or a refinement with the parent generation ID. Return the review link; after the user confirms, inspect `get_operation` and then `get_logo_generation_batch`. Failed or pending artwork is not a usable logo. Uploads use the secure `upload_url`, and full custom-label editing uses `custom_label_editor_url` from the tool.

Use `prepare_logo_selection` or `prepare_packaging_selection` to stage a change. Applying a logo submits it for review; it does not update existing store images. Agree product copy and retail prices with the merchant, then call `import_product` for each product they ask to add, using verified catalog IDs and integer minor-unit prices by size. This starts the import directly; there is no separate Dripshipper confirmation page. Shopify, Wix and WooCommerce are supported. `get_merchant_products` includes existing custom products and review status; use the returned account editor links for custom-label product editing and importing.

Use `get_custom_label_reviews` for current custom-label approval status, rejection reasons and bag previews. Filter by a verified custom label or custom product ID, or by pending, approved or rejected status; paginate using `next_cursor` as `after_id`. A bag preview is not proof of approval. Quote the actual rejection reasons, distinguish custom-label reviews from the store logo review, and never promise a completion date.

For product removal, read `get_merchant_products` first and use its `product_kind` and `id` with `remove_product`. Imported IDs identify a Dripshipper store link; custom IDs identify a custom product. Never substitute a catalog ID or an external store ID. Explain that this permanently deletes the connected store listing and its variants, while retaining the Dripshipper product, label artwork and existing orders. Identify the exact product and connected store, and obtain explicit confirmation in chat before calling the tool. Report the returned result in chat and offer the products link only as an optional reference. Do not repeat an uncertain removal or claim success until the operation confirms it.

## Review and execution

`import_product`, `remove_product`, `cancel_order` and `change_shipping_address` execute the merchant’s authorized request directly. Verify the exact target and intended change in chat before calling them. Requests for advice, a preview or eligibility alone do not authorize execution. Do not send the merchant to Dripshipper to confirm these actions. Report the actual returned outcome, and offer the normal order or product link only if useful.

`prepare_packaging_selection`, `prepare_logo_selection` and `prepare_logo_generation` return previews. Show the exact review URL and summarize the proposed change. The merchant reviews these on Dripshipper. Invoice payments use the dedicated Pay flow below. Never click or submit the final confirmation for them and never describe a pending operation as completed. Use a new `request_key` for a new intent and the same key only for an exact retry. `get_operation` is the source of execution status.

For queued or running imports, explain that processing is underway. For uncertain outcomes, ask the merchant to check their store or contact support; do not create a new import to work around uncertainty. A product may have been created even if a later step failed. Store visibility depends on the destination platform.

## Orders and invoices

Use `create_order_quote` for physical samples, direct orders or bulk quantities. Obtain the actual recipient, address, variant/custom-product IDs and quantities from the user. Tell them the destination may be sent to the shipping carrier to calculate bulk shipping. Do not guess an address. The server calculates prices, discounts, stock availability, supplier tax and shipping. Show the currency, total and external checkout link. The user creates the order on Dripshipper, then pays its invoices separately; never collect card data or describe a quote as paid.

Use `get_orders` for fulfillment and tracking, `get_invoices` for supplier charges and payment status, and `get_order_quote` for checkout recovery. Paginate when needed. Keep customer addresses and other personal information out of unrelated responses.

For an invoice the user wants to pay, call `prepare_invoice_payment` with its verified ID. The widget shows the exact amount, currency and masked saved card. Let the customer press Pay; never invoke the UI-only `confirm_invoice_payment` tool yourself, obtain its private confirmation token, or automate clicking Pay. Preparing a review authorizes no charge. Use `get_invoice_payment` to check the result. Only `paid` confirms success. A processing or uncertain payment must be reconciled before trying any other payment path.

When bank authentication is required, show the exact returned Dripshipper link to finish the same payment. If no eligible saved card exists or inline payments are disabled, use the returned external payment link. New card credentials are entered only on Dripshipper, never in chat. Payment does not guarantee immediate fulfillment; other supplier invoices or store acceptance may remain outstanding.

For cancellation, read the order first and use its internal `id` as `order_id` with `cancel_order`. Use `order_id` for order details and support too; legacy order numbers can be shared by several orders. Never guess among ambiguous matches. Make sure the merchant explicitly asked to cancel that order. Explain that eligibility is checked when the action runs, suppliers may be notified, and refund handling depends on the store; report the returned refund status rather than assuming a refund. Interpret the operation's success field and message, not just its completed state.

For shipping changes, read `get_orders`, verify the exact order, and use its internal `id` with `change_shipping_address`. Obtain the complete recipient name, street, city, US state, ZIP and country from the user; never infer an address. Optional apartment and company fields are cleared when omitted; phone is preserved unless supplied. When the merchant asks to apply a complete replacement address, execute it and confirm the actual saved address returned by the tool. If required details or intent are unclear, clarify in chat first. The normal order detail page is an optional reference; there is no extra confirmation step in Dripshipper. Execution uses the existing Chatbase rules: eligible unshipped US orders with Old Chicago or Temecula, local tracking checks, and ShipStation verification/update when needed. This updates Dripshipper fulfillment, not the storefront address. Treat a manual-review or uncertain result as unresolved and do not issue another change.

For support, offer the Dripshipper Help Center at https://intercom.help/dripshipper-help/en/. Email drafting and sending are unavailable in this plugin. Do not claim that support has been contacted.
