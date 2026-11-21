---
name: send-letter
description: Write letters with Mail by Pony, check the exact print proof, then send them from a prepaid balance or a one-click payment link.
---

Use the connected Mail by Pony MCP tools; never invent tool results or claim the
plugin is connected before a call succeeds. If agent access is unavailable, show
the actual setup status and stop dependent operations.

Accept only ordinary non-sensitive correspondence. Do not request medical
records, government identifiers, card data, passwords or secrets. State the
content boundary before uploading a PDF or photo; the owner must acknowledge it.
Uploaded art is decoration, not purchased postage.

Read catalog and existing drafts first. Keep text, Markdown and uploaded PDF
formats explicit. Preserve the latest revision and use a fresh idempotency key
for each intended mutation; reuse the same key when checking/retrying it. Never
overwrite a conflict or blindly repeat an uncertain mutation.

For editable multipage letters, use pages with stable IDs and explicit text or
Markdown format. Preserve IDs while editing/reordering; a source may flow onto
several printed sheets. Read the actual preview's page_map before placing art;
anchor it with page_id/page_offset so earlier edits do not move it to another
source page. Legacy text-only updates replace explicit pages. PDF mode prints
the uploaded original while retaining editable pages for switching back.
Preserve the returned handwriting seed and engine_version when reopening or
copying handwritten work; change its seed only for an intentional new variation.
The experimental original_hand style has a separate original_hand seed/engine/
foundation configuration. Check catalog readiness and its exact supported
characters before offering it, retain its experimental/provenance limits, and
preserve both configurations when copying. Never silently replace unsupported
characters or substitute another visible font.

Collect sender and recipient addresses in conversation and save them with
create_draft/update_draft (or reuse IDs from list_address_references). Ask only
for fields listed in address_validation. Never guess a ZIP or claim postal
verification. Never infer ownership from matching email addresses.

Run preview for the exact proof and tell the person what will print: pages,
recipient, options and price. Use show_letter only if they ask for an inline
preview; tool success does not prove the panel rendered.

When the person says to send it:
- If catalog.prepaid.sending_ready is true and list_agent_grants shows an active
  permission for this assistant, call quote_for_send for the final total, then
  send_with_credits with the same idempotency key on any retry.
- Otherwise call create_payment_link and give them the checkout_url. Paying that
  Stripe page approves and sends the letter.
- On INSUFFICIENT_FUNDS share the returned funding link or offer a payment link.
  On grant_required offer a payment link, or tell them they can allow this
  assistant in Account → Credits.

The website review (handoff_url) and the prepare_checkout/checkout tools remain
available for people who prefer to finish there.

Never claim a letter was paid, printed or mailed unless get_order says so.
Queued is not mailed; mailed means handed to USPS, not delivered. Cancel only
when eligible and explicitly requested. Developer docs:
https://www.mailbypony.com/developers .

A dedicated reviewer account uses owned synthetic drafts and Stripe test-mode
payment links. Use create_payment_link only when the reviewer asks to send;
clearly state that no real money moves and test orders are never printed or
mailed. Test checkout accepts card 4242 4242 4242 4242, any future expiry and any
CVC. Never request real card data in chat. The reviewer cannot fund or spend a
prepaid balance, create API keys or grants, or initiate physical fulfillment.
Never invent paid, printed or mailed results; read the actual test order status.
