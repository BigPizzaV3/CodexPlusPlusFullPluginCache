---
name: send-mail
description: Design letters and printed greeting cards, prepare and quote letters or postcards without an account, create preview or checkout links, and check a supplied order reference. Use for PieterPost postal workflows; ordinary email and messaging do not use this skill.
---

# PieterPost guest mail

PieterPost prints physical greeting cards and prints and posts letters and postcards. This plugin works without a PieterPost account, OAuth connection, or API key. Do not ask the user to sign in or create an account. Explain that the user reviews and pays on PieterPost's website before printing and posting.

For letters and postcards, collect the recipient name and structured postal address: `streetAddress`, `postalCode`, `city`, `country`, and `state` where required, or preformatted `addressLines`. Do not guess missing fields. The plugin cannot access saved contacts or account history. Preserve the exact approved message and line breaks.

Use `upload_asset` for a supplied postcard front image, card photo, letter PDF, or custom stamp. Use `kind=postcard-image` for card and designed-letter photos; any aspect ratio is accepted for them. Postcard fronts must be square. Letters support up to three attachments per recipient, and bulk requests support up to 25 recipients. Follow the current tool schema and validation messages.

- For a quote only, call `quote_order` with exactly one of `letters` or `postcard`, then show amount and currency. A quote does not create or send an order.
- For an editable letter preview, call `create_compose_link` with `recipient` and optional `message`, then show the returned URL. It does not create, pay, or send mail.
- For guest checkout, call `prepare_letter` with `letters` or `prepare_postcard` with `postcard`. Show the returned price and recipient summary. Use its `preparedOrderRef` with `create_payment_link`; omit the original mail payload on the payment-link call. Show `paymentLinkUrl` and let the user review and pay. Do not complete payment yourself or claim that unpaid mail has been sent.
- To check an order, call `get_order_status` with the private `orderRef` returned in this conversation or explicitly supplied by the user. It returns minimal payment and fulfillment status. Do not enumerate or guess references. Do not search for another customer's orders.

Create a fresh random UUID `idempotencyKey` for every prepare, preview, or checkout-link operation. Reuse it only to retry the same payload after a timeout. Use a new key for changed content or the separate checkout-link operation. Check a returned order reference before repeating preparation after an unclear result.

Use `mode=test` for explicit tests and demonstrations. `mode=live` is the default for ordinary guest checkout. Always keep the same mode when preparing an order and creating its checkout link. Never change modes to work around an error. Leave paymentMethod unset or auto unless the user requests card or iDEAL.

If an address is rejected or addressWarnings are returned, explain the issue and collect a correction. Set `acceptUsAddressWarnings=true` only after the user accepts the specific warning.

Use `search` and `fetch` for public postal workflow guidance, and include the returned guide URLs in the answer. They cannot retrieve private accounts, contacts, wallets, keys, or order history. This plugin does not send email, track unrelated parcels, sell top-ups, or manage credentials.

## Printed greeting cards

Cards use a separate design and ordering flow. Do not use the letter or postcard prepare, quote, or payment-link tools for a greeting card.

1. Call `list_card_options` for starter designs, sizes, paper, techniques, fonts, and illustrations. Use `sections` to limit the response or `fontQuery` to find a font.
2. Call `create_card_design` with a starter or a blank card and a batch of edits. For a supplied photo, call `upload_asset` first and use its `assetId` in `add_image`. Preserve the person's exact text.
3. After each create or update, call `get_card_preview` with the returned `draftToken` and `pageIndex: 0`, then `pageIndex: 1`. Inspect the actual images for text, placement, contrast, and clipping. Use `previewPages: []` on create/update to avoid rendering twice. A preview URL or design data alone does not mean you have seen the card. If the preview call fails, say that visual inspection is incomplete. Check `characterIssues`, `printIssues`, and `design.card.techniqueIssues`. Explain any fallback character: it prints in DejaVu Sans and can look different. Do not remove it without the person's agreement. Missing characters and blocking technique issues must be fixed before ordering. Fix print warnings where possible and explain remaining warnings.
4. Iterate with `update_card_design`, using `baseVersion` from the latest result. Call `get_card_design` before editing when the person may have changed the editor. On `version_conflict`, inspect the returned current design and reapply only the requested change; do not overwrite unrelated edits. Do not repeat an unclear create or update blindly; read the returned draft first when its token is available.
5. Give the person `editorUrl` to refine and order the card on PieterPost. Creating or editing a draft does not order, pay, print, or send it. Return previews, not a print PDF.

## Designed letters

For a letter with its own look (fonts, colours, a photo or illustration, extra pages) instead of plain text, use the letter design tools. They work like the card tools; the person adds recipients and orders in the editor.

1. Call `list_letter_options` for starter letters, postal layouts, fonts, illustrations, and personal fields. Pick the layout whose `usedFor` covers the recipient's country (A4 with the window left for most countries, A4 France for France).
2. Call `create_letter_design` with a starter or a blank letter, the layout, and a batch of edits. Personal fields such as `{{first_name}}` are filled in per recipient. Preserve the person's exact text, and give long text a tall enough box: text boxes don't grow. For a supplied photo, upload it with `upload_asset` and use its `assetId` in `add_image`.
3. Show the PNG previews; page 0 shows a grey sample address where the recipient's address is printed. Fix every blocking `printIssues` entry (edge, address window, postal zones) and the clashes in `design.printIssuesInOtherLayouts`: they block ordering. Tell the person about low-resolution images and fallback characters.
4. Iterate with `update_letter_design` and `baseVersion`, as for cards. Element texts come back in full; edit from them so nothing is lost.
5. Give the person `editorUrl` to refine the letter, add recipients, and order it. Creating or editing a draft does not order, pay, print, or send it.

The draft token and editor and preview URLs of cards and letters grant access to the design. Share them only with the person in the current conversation. Do not publish them or put them in public logs. Drafts expire 30 days after the last change.
