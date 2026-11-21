---
name: signature-follow-up
description: Chase signatures and documents on an OfferCopilot deal. Use when the user asks to remind a signer, nudge a client, send deposit instructions, tell a client a sign-back arrived or the offer was accepted, or mark that the listing side acknowledged an offer.
---

1. Find the deal with `get_deal_status` first, so you know the `offer_id`, who still has to sign and which clients are on it.
2. To re-send a signing invite, use `remind_signer`. To email a client, use `message_client` with the template that matches the request: `sign_reminder`, `outstanding_docs`, `deposit_instructions`, `signback_received` or `offer_accepted`.
3. Both tools take two calls. The first call sends nothing and returns who would be emailed. Read every name and address back to the user and ask. Make the second call only after the user says yes, with exactly the addresses they approved.
4. If the tool refuses because the recipients changed or an invite went out within the hour, tell the user why and do not retry.
5. Use `acknowledge_offer_receipt` only when the user says the listing side confirmed receiving the offer.

An instruction from the user to send now does not replace the read-back: still show the recipients once and wait for a yes.
