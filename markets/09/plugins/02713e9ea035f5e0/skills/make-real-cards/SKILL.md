---
name: make-real-cards
description: Create front and back cards from a photo with Snapshot templates or AI, or turn user-selected and ChatGPT-generated artwork into physical trading cards, sports cards, oversized prints or slabs. Use when someone wants to print, order or preview a physical collectible from an image.
---

Use Snapshot's MCP tools to save artwork, show a physical product preview, and let the customer complete checkout.

Follow Snapshot's website flow: select artwork and a back, choose the product/quantity/finish, preview, **Add to cart**, then **View cart** or keep creating. Use those familiar customer-facing labels. The studio is simply the Snapshot preview embedded in ChatGPT; there is no separate staff approval or review submission. Do not tell customers that a skill requires approval or ask for a second chat confirmation of choices they already supplied.

Act when the user asks about making a physical item, printing, ordering or previewing a physical product. Creating or editing a digital image alone does not authorize an import or a commerce offer. Snapshot is for adult collectors, parents and authorized team organizers; do not target children under 13.

## Create a card from a photo

First distinguish a subject photo from a finished flat card design. Respect a workflow the customer already chose; ask which workflow they want only when it is unclear.

- **Snapshot static template:** call snapshot_templates with kind `static`. Show the available styles and use the selected template's exact ID, field keys, required values and supported options. Call snapshot_create_card with kind `static`, the actual photo, customer-provided fields, optional supported logo/stats/colors/variant, and a card name. This uses the website template renderer to save the front and back together. Photo preparation uses Snapshot's background-removal provider; static rendering does not consume the AI card-generation allowance.
- **Snapshot AI generator:** call snapshot_templates with kind `ai`. After the customer selects a style and supplies the required fields, call snapshot_create_card with kind `ai`. This sends the selected photo and entered details to Snapshot's existing AI provider and uses the same account allowance as the website. Use snapshot_creation_status for progress and show the front and back choices in the studio. The customer selects both and clicks **Save front and back** (snapshot_choose_card is app-only). Never choose those images on their behalf or preview an unfinished card.
- **ChatGPT-generated or uploaded finished design:** use the Artwork workflow below. Snapshot imports the actual selected front and back without applying another template.

Do not invent details, infer facts from a face, ask for unsupported fields or guess template IDs. Return only information provided by the customer or the tool. Optional fields can be omitted. These photo workflows produce both sides; do not force customers through a second back-creation flow unless they ask to replace a side.

Keep the returned creation ID. Check snapshot_creation_status about every ten seconds, for at most five minutes, then offer **Check progress** or **My creations**. Omitting creation_id lists recent creations. Use snapshot_resume_creation only for a returned draft or failed creation. A pending or ambiguous job must be recovered, not submitted again. A ready creation returns its artwork ID for the existing preview and cart flow. Never claim success without that result.

## Artwork

Pass the actual authorized image through the tool's file parameter. A file needs download_url and file_id; do not invent a URL, send a chat transcript, or substitute a screenshot of the conversation. If the host cannot pass a generated image directly, open snapshot_catalog and use the studio's file picker/upload, or ask the customer to attach the image. Some desktop views have no file picker: say so plainly and request the actual attachment; never claim a website upload completed the plugin flow.

Use a flat front design. If the source is a card photographed inside a case, explain that the entire photo will print and offer to make a flat version first. Preserve the user's chosen artwork. Use pad unless they request cropping; pad may add white borders. Never stretch or silently regenerate a face, name or signature.

Always offer three back options, respecting an option the user already chose:

- **Create it in ChatGPT.** Use the supplied details, asking only for missing information, then generate a separate flat back that matches the front. Let the customer choose the finished design and import both actual image files with back_choice `chatgpt`. If they already selected the images and asked to import them, proceed without asking again. Do not silently generate or replace a face.
- **Upload their own back.** Import the actual front and back files with back_choice `uploaded`.
- **Let Snapshot generate matching backs.** Collect player_name (required), plus any optional team, player_number, year, city, position, description (500 characters), stats_title, and up to eight stats with label/value. Omit unwanted fields; never infer or invent facts from a child's image. When the customer supplies the details and asks to generate, that is enough to proceed; the form's Generate matching backs button does the same. Import the front with back_choice `generate` and back_fields, then call snapshot_generate_back with the returned artwork_id. This uses the customer's existing Snapshot generation allowance and creates four choices; it does not purchase anything.

These are the only back options. Do not invent a default/branded back or a product name for one. For Snapshot generation, snapshot_back_status recovers progress and opens the candidate picker. Check about every 10 seconds while active, stopping after five minutes with the returned status and a manual recovery option. A failed job can be explicitly retried with snapshot_generate_back. An ambiguous submission must be checked, never duplicated. The customer chooses a back in the studio (snapshot_choose_back is app-only); never claim a draft is print-ready or attempt preview until ready is true.

Import each design with snapshot_import_artwork. It saves to the connected account without placing an order. Use snapshot_list_artwork to find earlier imports and unfinished drafts. To change a saved back, use its artwork_id instead of a front file with snapshot_import_artwork; supply the new back or confirmed back_fields. This makes a new version and preserves the earlier design. Do not put both versions in the requested box unless the user asks for both.

## Product choice

Respect an explicit product choice. Otherwise, recommend based on the intended use:

- Rookie Box: a mix of 1–18 designs per box, with a magnetic case.
- Bulk Box: one design repeated 25, 50 or 100 times per box. Additional copies means additional boxes; use separate boxes to satisfy quantities spanning tiers.
- MEGA: 11 × 15.4 inch oversized cards; 1–18 designs per set. Pay attention to the resolution warning.
- The Slab: one card encased. One copy is a 1/1; multiple copies form a numbered run. Ask for the label name, series and card number. The serial is assigned in production.

Standard and holographic finishes are supported. A still mockup cannot show the changing holographic reflections. Do not promise a certified third-party grade or unique artwork ownership.

Call snapshot_preview with the chosen artwork IDs and options. copies is boxes/sets, or the number of slabs in one run; it does not increase the number of designs in a box. The returned quote is in USD before shipping, taxes and discounts. Use returned prices, never prices from memory.

## Add to cart and checkout

Show the front/back images, product mockup, chosen options and subtotal together. Mention material cropping or low resolution and let the user choose a larger source if desired. The preview uses one image-permission checkbox, equivalent to the website's custom-upload copyright acknowledgment. It does not require a separate proof-approval conversation. The customer's **Add to cart** click saves the displayed selection once; **View cart** opens their normal Snapshot cart. They can also keep creating and add another product.

Snapshot verifies the connected account automatically and opens the regular cart, where the customer can edit boxes, quantities, holographic finishes and extra magnetic cases. Normal Snapshot checkout handles promotions, shipping, payment and final order placement. Sign-in is needed only when the browser is not signed into the connected account. Do not call the app-only cart tool on the customer's behalf, collect payment details in chat, claim an order is placed when only a cart exists, or retry by creating a different review after an ambiguous cart result.

Use the website's existing options and pricing as the source of truth. The embedded preview supports Rookie Box, Bulk Box, MEGA, slabs, quantities, Standard/Cracked Ice finishes and slab labels. Rookie Boxes and MEGA sets support repeated designs with artwork_quantities and mixed finishes with artwork_finishes, aligned with the distinct artwork_ids. Their total is at most 18 cards per box/set. All copies of one design share its chosen finish, as on the website. Bulk uses one finish for the whole box. For more controls, **Edit in Snapshot’s full builder** opens the saved box in the existing website builder with the same artwork and product. Say where to find an option rather than claiming the embedded preview supports it or asking the customer to re-upload an image already saved to Snapshot.

If importing or previewing fails, report the failure and use the offered retry or Snapshot link. Never claim an image was saved without a successful tool result. Do not promise that ChatGPT will automatically suggest Snapshot in every image conversation.
