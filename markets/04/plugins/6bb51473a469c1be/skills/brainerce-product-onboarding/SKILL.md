---
name: brainerce-product-onboarding
description: "Add a product to a Brainerce store properly, from creating it through to category, tags, stock and publishing. Use when the merchant says add a product, I have something new to sell, list this item, put this in the shop, set up my new range, copy an existing product, or fix the stock count on something. Also covers duplicating a near-identical product and correcting inventory after a stock take. For store owners, not developers. Do not choose this to change price or description on a product that already exists and is set up, that is a quick edit and needs no sequence. Do not choose this for reading reviews or ratings, use brainerce-analytics. Do not choose this to find products that were left as drafts, use brainerce-store-health. Do not choose this to decide variant versus custom field, use brainerce-store-architecture. Keywords: add product, new product, list an item, create product, upload product, stock count, inventory, restock, categorise, tags, publish, duplicate product, product variants."
compatibility: ChatGPT, Claude Code, Claude Desktop, Cursor
maintainer: Brainerce
metadata:
  author: Brainerce
  version: "1.0.0"
---

Get a new product from "I have this thing to sell" to a listing customers can actually find and buy.

## Core principle

A created product is not a finished product. A merchant who is told "done" and then finds the item invisible on their own storefront, uncategorised, or with no stock, has been misled. Walk the whole sequence, and say which parts you skipped.

## When to use this skill first

- "Add a product", "I have something new to sell", "list this".
- "Set up my new range" or several products at once.
- "Make another one like this": duplicating an existing listing.
- "Fix the stock on X", "I counted 40 of these".

## When NOT to use this skill first

- Changing a price or a description on an existing, fully set up product: just do it, no sequence needed.
- "What do people think of this product", ratings and reviews: use `brainerce-analytics`.
- "Find products I left as drafts": use `brainerce-store-health`.
- "Put this product on sale": use `brainerce-launch-a-sale`.
- "Should size be a variant or an option", or any question about how the catalog should be modelled before the product exists: use `brainerce-store-architecture`.

---

## The sequence

Do these in order. Later steps depend on earlier ones, and skipping one is how products end up invisible.

### 1. Look before you create

Call `list_products` with the name the merchant gave. If something close already exists, say so and ask whether they want a new product or an edit to that one. Creating a near-duplicate is easy to do and annoying to undo, and this connector cannot delete the mistake.

If the merchant wants something very like an existing product, `duplicate_product` is faster and less error prone than retyping everything. Duplicate first, then edit the differences with `update_product`.

### 2. Create it

Call `create_product`. Ask for what is missing rather than filling it in yourself:

- **Name** and **price**, always. Read the currency from `get_store`; do not assume.
- **Description**: offer to draft one, but show it to the merchant before it goes live. This is their voice, on their storefront.
- **Images**: if the merchant has image URLs, pass them; the platform downloads and stores the images rather than linking to someone else's server.
- **Variants**: sizes, colours, materials. Ask if the product obviously has them ("a t-shirt" almost certainly does) and do not silently create a single-variant product for something that needs five.

### 3. Put it somewhere customers will find it

Call `list_categories`, then place the product in a real category. If nothing fits, `create_category` makes one, but check the list first; stores accumulate near-duplicate categories fast.

### 4. Tag it

Call `list_tags` before `create_tag`. Reuse an existing tag over creating "Summer" next to "summer" and "Summer 2026". Tags are how the merchant will filter and how sales get targeted later.

### 5. Set stock

Call `set_product_stock`. A product with no stock is not buyable, and a merchant who thinks they have listed something for sale will not check. If the merchant has not said how many, ask; do not default to a number.

`get_product_inventory` reads back what is actually there, and is the tool for a stock take correction as well.

### 6. Offer to publish, do not assume

Products can exist as drafts. Tell the merchant which state it is in and ask before making it visible. "Do you want this live on the storefront now, or held as a draft while you add photos?" is one sentence and prevents both of the bad outcomes.

## Response shape

> ✓ Ceramic Mug is created at 65 ILS, in Kitchen, tagged handmade and gift, with 40 in stock.
>
> It is currently a draft, so customers cannot see it yet.
>
> Want me to publish it, or would you rather add photos first?

**Partly done, use this shape:**

> ✓ Ceramic Mug is created at 65 ILS with 40 in stock.
>
> Two things I did not do: it is not in a category yet, and it has no images. Uncategorised products are hard for customers to find.
>
> Want me to put it in Kitchen?

## Rules

- Never say "added to your store" for a draft. Say it is a draft and what that means.
- Check `list_products` before creating, and `list_tags` and `list_categories` before creating those. Duplicates cannot be deleted from here.
- Ask for stock rather than defaulting to zero or to some number you picked.
- Show generated descriptions to the merchant before publishing. This is their shop's voice.
- `create_product` reaches an external origin when it downloads images from URLs, and running it twice creates two products, not one. If a call is ambiguous about whether it went through, check with `list_products` rather than re-running it.
- `update_product` replaces the fields it touches rather than merging into them. Read the current product with `get_product` before an edit so you know what you are about to overwrite.
- Several products at once: do them one at a time and report as you go. This connector has no bulk create, and a half-finished batch is worse than a slow one.
- This connector cannot delete a product. Say so if the merchant asks, and point at the Brainerce dashboard.

## Cross-skill connections

- Putting the new product on sale: `brainerce-launch-a-sale`.
- Reviews and ratings on it: `brainerce-analytics`.
- Finding old drafts and out-of-stock items across the store: `brainerce-store-health`.
- Deciding variant versus custom field, or category versus tag: `brainerce-store-architecture`.
- Filling in a custom field on the new product: `brainerce-custom-fields`.

Route once, and do not bounce back and forth.
