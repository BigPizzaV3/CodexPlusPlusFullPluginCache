# Section guidelines

## How to use this document

1. **Orient** — scan the section index to understand what's available and when to reach for each category.
2. **Plan** — choose a flow template that matches the campaign goal.
3. **Build** — use the per-section guidance for placement rules, preferences, and constraints.
4. **Check** — apply the copy rules and missing-data policy before finalizing.

---

## Missing data policy

**Never fabricate store data.** This is the highest-priority rule in this document.

- Never guess or invent URLs, product IDs, collection IDs, discount codes, image URLs, promotional details, contact email addresses, or signature assets.
- Use `search_products`, `search_collections`, `search_links`, and `search_images` to get real values before building sections that need them.
- If a required field cannot be left blank and real data is not available, ask the user for the missing value — or choose a different section type that works with what you have.
- Prefer blank strings or nulls only when the section schema explicitly allows them.

---

## Section index

### Blog

| Section             | Reach for it when…                                                                                                  |
| ------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Featured blog posts | A specific post is worth spotlighting — either as the lead content or as supporting material in a promotional email |
| Recent blog posts   | The campaign should surface recent content automatically without manual curation                                    |

> These two can be used together in the same email. A common pattern is Featured for a lead article, followed by Recent blog posts to fill in supporting content automatically. If a featured post also appears in the recent feed, it will be deduplicated automatically.
>
> In editorial-style emails, product or collection sections work well after a Featured blog post to merchandise anything related to the post's topic. In promotional emails, a Featured blog post can provide supporting context — a how-to, a buying guide, a brand story — after the main product or offer sections.

### Collection

| Section             | Reach for it when…                                                                                                         |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| Collection list     | The email should surface multiple collections as shopping paths — links to categories, not the products inside them        |
| Featured collection | The email should showcase the products inside a single collection, with title, vendor, rating, price, and per-product CTAs |

> Featured collection follows the collection's sort order from Shopify. If specific products need to be highlighted or reordered, use Featured products or Product list instead.
>
> These two can be used together: Featured collection as the primary content block merchandising products from a hero collection, with Collection list below as a secondary "browse by category" navigation row.

### Custom

| Section | Reach for it when…                                                                                                       |
| ------- | ------------------------------------------------------------------------------------------------------------------------ |
| HTML    | The user needs a custom table layout, or is embedding content from a third-party app not directly integrated with Seguno |

### Discount

| Section          | Reach for it when…                                                                             |
| ---------------- | ---------------------------------------------------------------------------------------------- |
| Discount callout | The email has a discount included and it should be highlighted in a specific part of the email |

### Live

| Section   | Reach for it when…                                                                                                                        |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| Countdown | A hard deadline exists and urgency is a core part of the message — the timer runs live on open, not at send time                          |
| QR code   | The email targets an in-person or offline action and the merchant has a URL to encode — event check-in, in-store redemption, POS checkout |

### Media

| Section         | Reach for it when…                                                                                                                                   |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| Flipbook        | A sequence of up to five images should be displayed as an animated GIF — product angles, a step-by-step, a before/after                              |
| Gallery         | Two to four images should be shown as a single cohesive row, each linking to a different destination                                                 |
| Image           | A single strong visual sets the tone or anchors the campaign                                                                                         |
| Image with text | One product, category, or story needs a side-by-side visual and copy pairing with an optional inline CTA — stacks cleanly on mobile                  |
| Video           | The merchant has a YouTube, Vimeo, or TikTok video that demonstrates, entertains, or supports the campaign — links out to the hosted player on click |

### Product

| Section           | Reach for it when…                                                                                                                          |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| Featured products | Specific products should be merchandised with full detail and direct purchase CTAs — add to cart and express checkout per product           |
| Product list      | A set of products should be shown in a compact, scannable grid with a view product CTA — use when browsing is the goal, not direct purchase |

### Separator

| Section | Reach for it when…                                                                                                                          |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| Divider | Two meaningfully different content sections need a clear visual break — blog, product, or event details that should read as distinct blocks |
| Spacer  | Breathing room is needed between related sections without a visible line                                                                    |

### Social

| Section                | Reach for it when…                                         |
| ---------------------- | ---------------------------------------------------------- |
| Featured social follow | The campaign's secondary goal is to grow a social audience |

### Text

| Section                  | Reach for it when…                                                                                                                                     |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Button                   | A standalone CTA is needed to close out a content section that doesn't have an inline CTA — Rich text, Product list, Gallery                           |
| Button group             | Two or more parallel actions should be presented together — reply-style choices, multi-path navigation, or preference capture                          |
| Event list               | The email is promoting one to four time-based events with dates, times, locations, and individual CTAs                                                 |
| Rich text                | Any standalone text content is needed — intro copy, body copy, closing copy, announcements, or a simple headed block                                   |
| Signature                | A human sign-off will build trust, warmth, or response rate — founder-led brands, feedback requests, post-purchase follow-ups                          |
| Testimonial              | A single customer quote with optional star rating should anchor or support the message — social proof, trust-building, or credibility in re-engagement |
| Text columns with images | Two to four parallel messages each need their own small image, title, and copy — benefit pillars, category highlights, FAQs, or feature comparisons    |

---

## Per-section guidance

### Rich text

Has two distinct fields: a heading and a body text area. These serve different purposes and should be treated independently.

**Heading field** — use for simple titled sections where heading style doesn't need precise control. For hero headlines or styled section titles where size, weight, or color matter, use the body text field instead — the body text tools give more control than the heading field.

**Body text field** — supports bold, italic, underline, font size, font color, background color, links, ordered and unordered lists, and alignment. Use this for all body copy, and for any heading that needs specific styling.

**Section-level options:**

- Text alignment: left, center, right — applies to the full section
- Include padding: on by default — turn off when the section needs to sit flush against an adjacent section
- Background color: defaults to brand colors, accepts any hex value
- Heading color: defaults to brand colors, accepts any hex value
- Text color: defaults to brand colors, accepts any hex value

Prefer center alignment for short hero copy in visually simple emails. Prefer left alignment for longer body copy, personal notes, and post-purchase follow-ups.

A single Rich text section can carry a full heading + body copy stack. Only split into separate sections when the heading and body need different background colors or padding treatment.

---

### Button

Use for the main CTA when there is one obvious next step — specifically to close out a content section that doesn't have an inline CTA (Rich text, Product list, Gallery, Blog sections). Sections like Image with text and Featured products have inline CTAs and rarely need a Button section immediately after unless a second distinct action is needed.

**Configurable options:** label, destination URL, link name (alt text), alignment (full width, left, center, right), type (primary, secondary, small), and text size (small, medium, large).

Use primary type for the main CTA. Use secondary or small for supporting actions that shouldn't compete visually with the primary.

One button per section. For two or three parallel actions, use Button group instead.

Always use a real destination URL from `search_links`, `search_collections`, or a specific product. Do not invent URLs.

---

### Button group

Use when two or more parallel actions should be presented together — reply-style choices, multi-path navigation, or preference capture.

**Configurable options:** style (solid or outline) and text size (small, medium, large). These apply to all buttons in the group — individual buttons are not independently configurable.

Supports 1–6 buttons. Buttons fill up to three per row before stacking to the next row. For most campaigns, 2–3 buttons is the practical limit before the group starts to feel like a menu rather than a clear set of choices.

Use outline style when the Button group appears near a primary solid Button and shouldn't compete with it visually.

Prefer Button group over multiple standalone Button sections when the actions are genuinely parallel — same visual weight, same level of importance. If one action is clearly primary and another is secondary, use a Button section for the primary and a text link or secondary Button section for the other.

Every button must use a real destination URL or email link. Do not invent contact addresses or URLs.

---

### Image

Use for a hero visual that sets tone, a single featured product image, or a campaign image pulled from the store.

Supports a linked URL — always ask the user where the image should link if not provided, or pull a relevant URL from `search_links` or `search_collections`. An unlinked hero image is a missed conversion opportunity in most campaigns.

Alt text field is available — always populate it with a meaningful description. Do not leave alt text blank.

No caption field. If the image needs supporting copy, pair it with a Rich text section below, or use Image with text instead.

Use real store image URLs from `search_images`. Never substitute stock placeholders or guessed URLs. If no valid image is available, leave image fields blank when the schema permits, or ask the user.

---

### Image with text

Use when a single product, category, or story needs a side-by-side visual and copy pairing.

Image can be positioned left or right of the text. Choose based on the visual weight of the image and the reading flow of the copy.

Supports an inline CTA button when a link is provided — in most cases this removes the need for a separate Button section immediately after. Only add a standalone Button section if a second distinct CTA is needed below.

Stacks to a single column on mobile. The image appears above the text in the stacked view — keep this in mind when the image and copy need to feel connected.

Prefer this over Text columns with images when the image is large and the content is a single focused story. Use Text columns with images when two or three parallel messages each need equal visual weight at a smaller image size.

---

### Gallery

Use when two to four images should be shown as a single cohesive row, each linking to a different destination.

Renders as a horizontal row of images. Images are cropped to a shared height so they sit flush together — landscape and square images work best. Avoid tall portrait images as significant cropping may occur.

Each image supports its own link — use this when each image is meant to drive to a different product, collection, or page. If all images link to the same destination, a single Image section or Image with text is likely a better fit.

Supports 1–4 images. At one image it behaves like a standard Image section — only use Gallery when two or more images genuinely belong together as a visual row.

Use real store image URLs from `search_images`. Do not populate slots with placeholder images.

---

### Flipbook

Use when a sequence of up to five images should be displayed as an animated GIF.

Creates an animated GIF from a sequence of merchant-provided images — this is not an interactive document or linked catalog. It renders as a single looping animation in the email.

Works well for:

- Multiple angles of a single product
- A short step-by-step or how-to sequence
- Before/after comparisons
- A brief lifestyle or campaign story told across a few frames

The images should be consistent in dimensions — mismatched sizes will produce jarring transitions in the animation.

Do not reach for this as a substitute for a Gallery when the images are unrelated or each need their own link. Gallery is the right choice when individual images need individual destinations.

Always ask the user to provide the image sequence. Do not populate with placeholder images.

---

### Video

Use when the merchant has a YouTube, Vimeo, or TikTok video that supports the campaign.

Displays a cover image pulled automatically from the video URL — the URL must be provided before the section is built, otherwise the cover image will be missing. Always ask the user for the video URL upfront. Do not add this section as a placeholder expecting the URL to be filled in later.

Clicking the cover image links out to the hosted player — video does not play inline in the email.

Works well for:

- Product demonstrations or tutorials
- Brand story or behind-the-scenes content
- Short-form TikTok content repurposed for email

If the merchant doesn't have a video asset, don't suggest this section. Use Image or Image with text instead.

---

### Featured products

Use when specific products should be merchandised with full detail and direct purchase CTAs.

Displays each product with configurable fields: image, title, price, compare at price, description, rating, add to cart CTA, and express checkout CTA (including Shop Pay if configured for the account).

Image can be positioned top, left, or right of the product details. Top alignment works best when the product is the true hero of the section — use left or right when copy and product details need to read together.

Each product has its own add to cart and express checkout CTAs — this makes Featured products the most transactional product section. Reach for it when the goal is direct purchase, not just browsing.

Limit to 4 products. Beyond that the section becomes unwieldy and a Product list or Featured collection is a better fit.

Not all fields need to be enabled for every campaign. A promotional email may benefit from compare at price to show savings. A new arrival email may not need description if the image and title are strong enough. Match the enabled fields to the campaign goal.

Use real product IDs from `search_products`. Do not invent product IDs.

---

### Product list

Use when a set of products should be shown in a compact, scannable grid. Displays each product with title, rating, price, and a view product CTA. More minimal than Featured products — there is no add to cart or express checkout. Reach for this when the goal is browsing and discovery, not immediate purchase.

Supports 1–4 products per row. Recommend 2–3 products per row for best visual balance.

Total product count should be evenly divisible by the products per row to avoid an incomplete final row:

- 2 per row → 2, 4, 6, or 8 products total
- 3 per row → 3, 6, or 9 products total

If the user provides a product count that would produce an incomplete row, flag it and suggest the nearest clean number up or down.

Use real product IDs from `search_products`. Do not invent product IDs.

---

### Featured collection

Use when the email should showcase the products inside a single collection, with per-product detail and CTAs.

Displays products with title, vendor, rating, price, and a per-product CTA. Follows the collection's sort order from Shopify — if specific products need to be highlighted or reordered, use Featured products or Product list instead.

Use the real collection ID from `search_collections`. Do not guess collection IDs or slugs.

Can be paired with Collection list below as a secondary "browse by category" navigation row.

---

### Collection list

Use when the email should surface multiple collections as shopping paths — links to categories, not the products inside them.

Only use when multiple real collections are relevant. Use real collection IDs from `search_collections`.

---

### Discount callout

Use when the newsletter has a discount associated with it and it should be highlighted in a particular part of the email

---

### Countdown

Use when a hard deadline is central to the message — a sale end time, event start, or limited availability window.

The countdown displays the actual time remaining when the subscriber opens the email — not when it was sent. This makes it genuinely effective for real deadlines, and genuinely misleading if used without one.

Can be set to any arbitrary datetime the user provides. Always ask the user for the exact end date and time if not provided. Do not invent a deadline.

Pair with a Rich text section above or below that explains what the deadline is for.

Discount integration is not yet supported in the skill. When it is, the countdown can be tied directly to a discount end date.

---

### QR code

Use when the email targets an in-person or offline action — event check-in, in-store discount redemption, POS checkout.

Encodes a merchant-provided URL. Always ask the user for the URL if not provided — do not guess or substitute a store URL.

Not appropriate for standard ecommerce campaigns where all actions happen online — a Button section with the same URL will perform better in that context.

Discount integration is not yet supported in the skill. When it is, QR codes will be able to encode Seguno discount codes directly, making them especially useful for POS checkout as an alternative to manually entering a code.

---

### Event list

Use when the email is promoting one to four time-based events.

Each event entry supports: title, date, time (EDT), location, button text, button link, and a rich text description. All fields are entered manually — this section does not pull from a Shopify data source.

Supports 1–4 events per section. For a single event, consider whether a Rich text section with a Button better serves the layout — Event list adds the most value when two or more events need to be presented consistently.

Always ask the user for event details before building — date, time, location, and button link at minimum. Do not populate with placeholder event data.

If a registration deadline exists, pair with a Countdown section above to reinforce urgency.

Keep descriptions concise. Event descriptions that run long compete with the date and CTA, which are the most important elements.

---

### Testimonial

Use when a single customer quote with optional star rating should anchor or support the message.

Renders stars, title, author, and quote text in a centered stack. All fields are manually entered — this section does not pull from a review source.

**Fields:**

- Rating: none to 5 stars, configurable in increments
- Star size: adjustable in px
- Title: a short headline for the testimonial — e.g. "Life-changing moisturizer" or "Best purchase I've made"
- Author: defaults to "Valued customer" — always replace with a real customer name or at minimum a first name and initial
- Text: the full quote, supports rich text formatting
- Text alignment: left, center, right — center works well for short quotes
- Include padding: on by default
- Background, rating, and text colors — default to brand colors, accept any hex value

Do not fabricate testimonials. Always ask the user to provide the quote, author, and rating. The default "Valued customer" author should never appear in a finished email.

For multiple testimonials, use separate Testimonial sections stacked with Spacers between them rather than cramming multiple quotes into one text field.

---

### Signature

Use when a human sign-off will build trust, warmth, or response rate — founder-led brands, feedback requests, post-purchase follow-ups.

Renders a handwriting-style sign-off using the merchant's name — no image asset required. The signature is generated from the name field using a configurable handwriting font.

**Fields:**

- Sign-off text (e.g. "Sincerely,", "With love,", "Thanks,") — keep it short and appropriate to the email's tone
- Signature name — use the sender's real name, not the store name, for emails where a personal sign-off is the goal

**Configurable options:**

- Handwriting style: cursive or print
- Style variant: brushed, casual, elegant, or neat — match to the brand tone
- Size: adjustable in px
- Text alignment: left, center, right
- Background, sign-off, and signature colors — default to brand colors, accept any hex value

Note: some languages may not be supported by the handwriting renderer.

Prefer left alignment for personal, conversational emails. Center alignment works for more formal or brand-forward sign-offs.

---

### Text columns with images

Use when two to four parallel messages each need their own small image, title, and copy.

Renders a section-level heading above a row of 1–4 columns. Each column contains an image above a title and rich text body, with an optional CTA button.

**Section-level settings:**

- Heading — optional section title above all columns
- Text alignment: left or center
- Image corners: square, slightly rounded, more rounded, or pill — applies to all column images
- Button type: primary, secondary, or small — applies to all column CTAs
- Background color — defaults to brand colors, accepts any hex value

**Per-column content (each column independently configurable):**

- Show image toggle — image can be hidden per column if not needed
- Image — sourced from Library, Products, Files, Canva, Instagram, or Burst; use `search_images` to find real store images from Library or Products
- Alt text — always populate for accessibility
- Heading — short title, keep parallel in length across columns
- Rich text body — keep concise; long copy in narrow columns becomes hard to read
- Button text and button link — optional per column; each column links independently

The section-level button type and image corner style apply to all columns — there is no per-column style override. Keep content parallel in structure and length across all columns so the row feels cohesive.

The image can be hidden per column — making this section usable as a pure text column layout when images aren't available or would add visual noise.

Prefer this over Image with text when there are two or more equal-weight stories to tell at a smaller image size. Use Image with text when one story deserves full-width side-by-side treatment.

---

### Divider

Use to create a clear visual break between two content sections that are meaningfully different in tone or purpose — for example, between a blog section and a product section, or between two event listings.

**Configurable options:** line style (solid, dashed, dotted), thickness (1–10px), and width (25–100% of email width).

Use solid full-width for strong section breaks between distinct content types. Use dashed or partial-width for softer transitions where a visual cue is helpful but the break shouldn't feel abrupt.

Don't use a divider between every section — overuse removes the visual signal. Reserve it for genuine transitions between distinct content types.

---

### Spacer

Use to add breathing room between related sections without a visible line. Prefer spacers over dividers when the sections are related and the goal is pacing, not separation.

---

### HTML

Use only when no standard section type can represent the requested content, or when the user explicitly requests it.

**Common legitimate use cases:**

- Custom table designs (pricing tables, comparison tables, spec sheets) that no standard section can represent — the user should provide the HTML; do not generate speculative HTML to approximate a layout that a standard section could handle reasonably well
- Embedding content from a third-party app not directly integrated with Seguno — add the HTML section as a placeholder and instruct the user to edit the template directly to insert the embed code; do not attempt to generate or guess the third-party markup

Always prefer a purpose-built section first. HTML carries the highest maintenance risk and the lowest design consistency.

---

### Featured blog posts

Use when a specific post is worth spotlighting — either as the lead content or as supporting material in a promotional email.

The merchant hand-picks which posts appear. In editorial-style emails, product or collection sections work well after a Featured blog post to merchandise anything related to the post's topic. In promotional emails, a Featured blog post can provide supporting context — a how-to, a buying guide, a brand story — after the main product or offer sections.

Can be combined with Recent blog posts in the same email. If a featured post also appears in the recent feed, it will be deduplicated automatically.

---

### Recent blog posts

Use when the campaign should surface recent content automatically without manual curation.

Pulls the most recent posts automatically — no merchant selection required. Use when recency is a selling point or when the merchant publishes regularly and wants to keep email content fresh without manual updates.

Can be combined with Featured blog posts in the same email — a common pattern is Featured for a lead article the merchant wants to spotlight, followed by Recent to automatically fill in supporting content.

---

## Preview reminder

Always call `preview_newsletter` after saving campaign updates. There is no separate save step — `update_email` persists changes immediately. If the user requests further changes after preview, continue iterating with `update_email` and preview again.
