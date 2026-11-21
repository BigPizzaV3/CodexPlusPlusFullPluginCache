---
name: product-ads
description: 商品写真から広告画像の案を作り、選んだ案を修正して保存する。商品広告・SNS告知・広告画像の複数案に使う。
---

Use the user's language and supplied brand facts. Follow explicit instructions over defaults. Ask only for missing facts that affect the image: product, audience, destination, mandatory text. Do not invent discounts, endorsements, performance claims or product features.

1. Import user-attached product photos with import_chat_images using host-issued files. Preserve returned attachmentIds. If no photo exists, ask for one when product likeness matters; otherwise proceed with an explicitly agreed concept.
2. Propose up to three distinct visual directions in a compact list (for example product close-up, use scene, graphic layout). Use list_image_models to select an available reference-capable model; do not require the user to know model names. Use a suitable aspect ratio from its actual capabilities.
3. Use prepare_image with the chosen brief and reference IDs. For distinct directions, prepare separate quotes; count>1 with one prompt does not guarantee distinct designs. Every generation needs the widget's priced click. Never claim generation has started from a quote.
4. Recover each existing job with get_generation; never resubmit because polling is slow. Ask the user to choose a result by its actual output index. Revise with prepare_image and the owned conversationId/source messageId/index so the product photo is retained.
5. Check the result against supplied identity, claims, text, composition and destination. If you cannot see the media, ask the user to confirm; never invent a quality inspection. Point to the per-output save button. Offer image-to-video only when requested.

Template recipes are private. Registration/publication belongs in Studio. Do not offer purchases or commissions in this plugin.
