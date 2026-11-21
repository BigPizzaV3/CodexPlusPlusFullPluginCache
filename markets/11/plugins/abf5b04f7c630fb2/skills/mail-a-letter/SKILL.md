---
name: mail-a-letter
description: Prepare PDFs for physical mailing through the connected Mail A Letter account, check MailBank credit, and look up letter status. Use for Mail A Letter postal workflows.
---

# Mail A Letter

Use the connected Mail A Letter MCP server for customer-requested mailing work. Its tools are `get_mailing_capabilities`, `get_balance`, `list_letters`, `get_letter`, `create_upload_link`, `renew_upload_link`, `get_upload`, and `prepare_letter`. Authenticate through the host's OAuth connection; do not ask for account passwords or API keys in chat.

## Upload and prepare

1. Check `get_mailing_capabilities` when service availability, destination rules, or PDF limits matter. Prices come from `prepare_letter`, never from an estimate or a remembered rate.
2. Call `create_upload_link` for each intended new letter. Show the customer-facing `upload_url` and retain its `letter_id` and `revision`. If the PDF is available to an authorized upload capability, follow the server's direct-upload instructions; otherwise have the customer upload it on the website. A chat attachment is not uploaded merely because it appears in the conversation. Keep the secret `direct_upload_url` out of messages and saved artifacts.
3. After upload, use `get_upload` to check readiness and obtain the current revision. Explain pending, rejected, or expired states using the returned reason and next action. If an unprepared letter's links are lost, use `renew_upload_link` for the same letter instead of creating a duplicate. Renewal does not extend the original 24-hour upload window. Preparation locks the PDF; renewal then returns a conflict. A regular PDF is accepted; do not block the workflow merely because it is not PDF/A. Use the server's document limits rather than guessing them.
4. Collect the recipient and requested service/options. Use country codes and fields required by the tool schema. Do not invent an address, return address, or substitute an unsupported service. Prepare only when the PDF is ready.
5. Call `prepare_letter` with the `letter_id`, current `revision`, recipient, and explicit service/options. Generate a new random `idempotency_key` for an intended preparation. Retry the same request with the same key; an intentional change gets a new key.
6. Show the returned price, tax, total, page count, warnings, balance information, and `review_url`. Money fields are integer USD cents; divide by 100 for display. State that the letter is an unsent draft. The account holder opens the review link, signs in, checks the PDF proof, recipient, return address, service and price, and presses Send on the website.

Preparing again completely replaces recipient, service, and options. Fetch the current revision first, carry forward the user's intended values explicitly, and retain the new revision. Omitted service and return-envelope fields reset to defaults. If a value needed to preserve the mailing is unavailable, ask for it before updating.

## Status and other account actions

Use `list_letters` to find owned letters and `get_letter` for details. Continue pagination with the returned cursor unchanged. Report tracking only when the tool returns it. `mailed` means handed to the postal stream and is not confirmation of delivery.

The MCP server has no send, cancellation, refund, or credit-purchase tools. Sending spends MailBank credit only through the customer's website Send action. For cancellation, refunds, or top-ups, point to the website or app and use current server-returned links when available. Closing a chat or removing the connection does not cancel a sent letter. Never claim sending succeeded based on preparation or the customer's intention alone; check its status.

Respect the connected account's ownership boundary. Treat missing and inaccessible letter IDs alike. For errors, use the returned code and next action, preserve identifiers needed to recover the intended operation, and avoid creating duplicate upload drafts on uncertain outcomes. Draft creation is not idempotent.
