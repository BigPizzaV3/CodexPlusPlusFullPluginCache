# Customer invoicing

Use this workflow only when the connection exposes invoicing. It requires
current Orders-page access and restaurant, orders, and invoicing read scopes.
Issuance additionally requires an owner/admin role, invoicing write consent,
and enabled server and restaurant/provider workflows. Reconnection alone does
not configure a provider, enable delivery, or supply missing VAT mappings.

1. Establish the exact authorized restaurant. Find the existing sale with
   `find_orders` and inspect it with `get_order_details`. Preparation supports a
   complete sale already settled with the Invoice method; it does not create a
   sale or convert a card/cash payment into an invoice.
2. Use `find_invoice_customers` to find the existing business customer in the
   restaurant's connected provider company. Resolve ambiguous matches with the
   user. Use the returned customer ID; never invent a recipient, contact, email,
   provider company, or VAT code. The tool does not create or edit contacts.
3. Call `prepare_customer_invoice` with the exact returned order ID, business
   date, and customer ID. Delivery and dates come from the returned preview;
   these tools do not accept arbitrary delivery or date overrides. Preparation
   creates a preview, not a provider invoice.
4. Show the restaurant, provider/customer, delivery destination and method,
   invoice and settlement dates, due date, currency, gross/net/VAT, and warnings.
   Wait for explicit approval of those exact details. Preserve the ten-minute
   preview token and the complete prepared input. A changed source, expired
   preview, or changed recipient/amount requires preparation and approval again.
5. Retain a UUID idempotency key before calling `issue_customer_invoice` with
   the unchanged prepared input, preview token, and `confirmed: true`. Reuse
   that key only for an identical request. Report the returned state precisely:
   `pending` means a queued intent, not created, sent, delivered, or paid.

For an existing provider invoice, use `inspect_provider_invoice` with its exact
known provider invoice ID. Report recorded status and totals; sent is not paid.
If issuance or delivery is uncertain, inspect that invoice when its ID is known
and follow returned recovery guidance. Do not create another intent or choose a
new idempotency key to escape uncertainty. If the tools cannot reconcile it,
report the unresolved operation for staff review without claiming success.

Saving a document, preparing an invoice, issuing an invoice, delivering it, and
receiving payment are separate events. Do not infer one from another. Credits,
refund execution, and bank reconciliation are not provided by this workflow.
