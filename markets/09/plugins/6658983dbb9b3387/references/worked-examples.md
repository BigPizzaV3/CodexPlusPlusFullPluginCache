# Worked examples

All products, values and copy here are fictional training examples. No real buyer data or reusable shop IDs. These show reasoning and deliverables; they are not a template to apply unchanged to another product.

## A. Physical custom desk sign, no MCP

Confirmed seller brief: one engraved clear acrylic sign, 8 × 3 inches, supplied wooden stand; custom name up to 24 characters; minimalist layout; made by seller to order; USD29, quantity5; US dispatch in 3–5 business days, US shipping USD5; seller confirms returns/exchanges not offered. Packed 10 × 5 × 3 inches and 12 oz, measured. Photos not supplied. Keyword metrics absent.

**Positioning:** a readable personalized office/teacher desk sign. Acrylic, engraving and stand are confirmed; no invented glass, gold or sustainability claim. Keywords are relevance hypotheses, not measured demand.

**Title:** Personalized Acrylic Desk Sign with Wooden Stand, Custom Engraved Name

**Complete description:**

```text
Create a clear, personal place on your desk with a custom engraved acrylic name sign. Its minimalist layout keeps your chosen name easy to read, and the included wooden stand holds the sign upright.

WHAT YOU RECEIVE
One clear acrylic sign measuring 8 × 3 inches and one wooden stand. Decorative items shown in any styled photos are not included.

PERSONALIZATION
Enter the name exactly as you want it engraved, including capitalization. Maximum 24 characters. Example: Olivia. Check spelling before placing your order.

DETAILS
Material: clear acrylic sign with a wooden stand.
Design: minimalist engraved name.
Size: 8 × 3 inches, excluding the stand.

PROCESSING AND SHIPPING
Made to order and dispatched from the United States in 3–5 business days. Shipping within the United States costs $5. Carrier transit time is separate from processing; an arrival date has not been confirmed.

PLEASE NOTE
This seller does not offer returns or exchanges under the selected shop policy. Contact the seller about an order issue. No care or outdoor-use claim has been supplied.
```

Tags and the full structural packet are in [physical-desk-sign.json](../examples/physical-desk-sign.json). The final sentence about missing care is a training explanation and should normally stay in review notes rather than sales copy; the JSON packet demonstrates that cleaner version.

**Settings:** category proposal “Desk name signs” must be matched to actual Etsy taxonomy before execution; do not invent a category ID. Personalization text_input required, limit24. Price29 USD, quantity5, no variations. Maker confirmed; processing/shipping/return settings as above. Material field acrylic/wood. Images and actual category/attribute choices remain release blockers. Offline the agent supplies fields to paste and settings to select; it does not claim the shop changed.

## B. Printable weekly planner

Confirmed brief: two non-editable PDF files, A4 and US Letter, one undated weekly layout in each, personal use only. No physical product; software only needs PDF viewing/printing. No cloud-editing link, font pack or commercial rights supplied.

Title: `Printable Weekly Planner, Undated A4 and US Letter PDF`

Opening: “Plan your week with an undated printable layout. This digital set includes two PDFs: one A4 version and one US Letter version.” Follow with real page contents, PDF access/printing and personal-use license. Explicitly state no physical item is shipped. Do not call it editable or offer digital variations. The [digital packet](../examples/digital-weekly-planner.json) has complete sample copy/tags and unknown setup facts kept as blockers.

## C. Photo-only mug request

Seller asks “make the best SEO listing” with a photo of a cream-colored mug. Appearance is observable; ceramic, 11oz, dishwasher safety, manufacture and stock are unconfirmed. Return a provisional product-positioning/title direction, media observations and a small question bundle: material/capacity, customization, price/count, delivery or digital status. Do not publish a description asserting those missing specifications. Still help with confirmed appearance and buyer-question structure; do not refuse because MCP is absent.

## D. Long existing description

Original has specifications, six sizes, installation, processing, exclusions and care mixed with repetitive benefits. First list these factual modules. Reorder into contents/details/size selection/installation/delivery/care. Preserve all six sizes, every mounting exclusion and actual processing term. Give a short before/after summary **and the entire revised description**. Do not collapse the delivery paragraph into a generic “fast shipping” claim.

## E. Existing shipping profile change

Seller authorizes one listing to use an existing paid profile. Read actual listing and full profile/destinations; confirm it has the intended rates. Send only its `shipping_profile_id` through `etsy_update_listing`. Reread assignment and rates. Do not change shared destination rates, inventory, text or state under that authorization.

## F. Uncertain variation write

Etsy accepted the request but a mismatch is reported. Read inventory and compare each property-value combination, SKU, price/currency, quantity/enabled state and processing. Reordering/changed IDs alone is not a business mismatch. Report confirmed values and unresolved differences; do not replay the same write. Keep an exact previous snapshot for seller-authorized recovery, not an automatic rollback that could overwrite newer orders/edits.

## G. Thin evidence, attractive wrong keyword

Keyword CSV shows high searches for “gold desk sign,” but this sign is clear acrylic. Reject it as product mismatch. A relevant phrase absent from the database stays eligible with demand unknown. Do not fabricate zero search volume or a probability of ranking. A thirteen-tag set cannot be repaired by unrelated holiday phrases.
