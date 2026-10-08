---
name: brainerce-custom-fields
description: "Work with Brainerce custom fields, also called metafields: the structured extra data a product carries beyond its built-in fields. Use when the merchant says add a spec to my products, where do I put materials or care instructions, I need a size guide link on every item, let customers type an engraving, make this filterable on my shop, or set the country of origin on these. Covers the definition versus value split, which of the fifteen types to pick, the two flags that decide whether a field is buyer-facing or filterable, and the common data shapes. Writes values through the connector; definitions are a dashboard step and this skill says so rather than pretending. For store owners, and for developers reading fields on a storefront. Do not choose this to decide whether a property should be a custom field at all, that is brainerce-store-architecture. Keywords: custom fields, metafields, specs, materials, care instructions, engraving, personalisation, storefront filter, product attributes, structured data."
compatibility: ChatGPT, Claude Code, Claude Desktop, Cursor
maintainer: Brainerce
metadata:
  author: Brainerce
  version: "1.0.0"
---

Put structured data on products correctly, and be honest about the half of it that lives in the dashboard.

## Core principle

A custom field is two separate things, and confusing them is the single most common failure here.

- A **definition** is the field itself: its name, its type, its allowed values, whether shoppers can fill it in, whether it can be filtered by. It is created once, in the dashboard, and applies across the store.
- A **value** is what one product holds for that definition. Values are per product, and optionally per variant.

**This connector writes values. It cannot create definitions.** Say that out loud the moment it matters, rather than attempting a write that fails.

## When to use this skill first

- "Add materials / wattage / country of origin / care instructions to my products".
- "I need a size guide link on every item".
- "Let customers type what they want engraved".
- "Make this filterable on my storefront".
- "What custom fields should a jewellery shop have".
- Reading custom fields off a product in storefront code.

## When NOT to use this skill first

- Deciding whether the property should be a custom field, a variant, a category or a tag: `brainerce-store-architecture` owns that call.
- Adding a whole product: `brainerce-product-onboarding`.
- Pages, menus, policies and blog: `brainerce-content-and-navigation`.
- The SDK shape of `product.metafields` in storefront code: `brainerce-sdk`.

---

## The definition, and why it is not here

A definition is created under **Products, then Custom Fields** in the Brainerce dashboard. Creating one sets:

- **Name**, which is also where the key comes from. "Warranty Info" becomes the key `warranty_info`.
- **Type**, one of fifteen. See `references/field-types.md`.
- **Allowed Values**, which turns free input into a constrained list.
- **Customer Input**, which makes the field buyer-facing.
- **Show in storefront filters**, which exposes it as a shopper-facing facet.

None of that is reachable from this conversation, and it is deliberate: a definition is catalog schema, and one bad definition reshapes the product editor for every product and every connected sales channel.

> **If Custom Fields is missing from the merchant's sidebar**, it is a module that can be switched off for a store, not a missing feature. Settings, then Modules.

## ⛔ The definitionId boundary, and how to work inside it

`set_product_metafield` needs a `definitionId`. There is no tool here that lists definitions. A `definitionId` can only be read off a product that **already carries a value for that field**, and it comes back from:

- `list_product_metafields` on a product, which returns every value on it with its definition attached. This is the primary route.
- `get_product`, whose `metafields` array carries `definitionId`, `definitionKey`, `definitionName`, `type` and `value` per entry.
- `list_products`, which carries the same array on each product in the page.

So the honest shape of what this connector can do:

- ✅ **Copy a field onto more products.** One product has `care_instructions`? Read its `definitionId` and set that field on fifty others.
- ✅ **Correct or update a value** anywhere the field is already in use.
- ❌ **Use a definition nobody has used yet.** The merchant created it in the dashboard this morning and no product carries it: its id is not discoverable from here. Ask them to set it once on any product in the dashboard, then this connector can do the rest.
- ❌ **Create the definition.** Dashboard.

Never guess a `definitionId`. Never construct one from the key. Read it.

## The working sequence

### Setting a value on one product

1. `list_products` to find the product, if you do not have its id.
2. `list_product_metafields` on it. Two things come out of this: whether the field is already set, and the `definitionId` you need.
3. If the field is not on this product, find a product that does carry it and read the id from there. `list_products` returns metafields per product, so one page often answers it.
4. `get_product_metafield` before overwriting, so you can tell the merchant what the old value was.
5. `set_product_metafield`.

### Setting the same field across many products

1. Read the `definitionId` once, as above.
2. `list_products` filtered to the set the merchant means, by category or tag rather than by guessing names.
3. Call `set_product_metafield` **one product at a time**, and report as you go. There is no bulk write on this surface, and a half-finished batch that reports success is worse than a slow one.
4. Say the count at the end, and name any product you skipped and why.

### Reading values in storefront code

Values come back on the product as a `metafields` array, one entry per field, each carrying `definitionKey`, `definitionName`, `type` and `value`. Render **by type**, not as text: a Gallery is a list, a Yes/No is a boolean, a URL is a link. The `getProductMetafieldValue(product, key)` helper exported from the SDK parses numbers, booleans and dates for you. `brainerce-sdk` has the exact shapes.

## The two flags that change what a field is

Both are dashboard settings on the definition, and both are worth naming precisely because merchants ask for the behaviour without knowing the flag.

**Customer Input.** Turns the field into an input on the product page that the shopper fills in before adding to cart. The value is saved as a line-item detail on the order, visible in the order detail view next to the product. This is engraving, a monogram, a gift message printed on the item, a colour the shopper picks. It is also the mechanism that keeps a property out of the variant matrix without taking the choice away from the shopper.

⛔ Not the same as checkout custom fields. Anything collected once for the whole order (delivery notes, gift wrapping, a tax id) is a checkout field, a different feature in a different place.

**Show in storefront filters.** Exposes the field as a facet shoppers filter by, alongside category, brand and price. Available for **Select, Multi-select and Yes/No only**. Not free text, not numbers, not any other type. A merchant who wants to filter by wattage has to model it as a Select with bands rather than a Number, and that decision has to be made before the values are entered, because changing a definition's type later means re-entering every value.

Filter values combine as AND across fields and OR within a field.

## Common shapes worth suggesting

Grouped by what merchants actually ask for. Type choices matter: `references/field-types.md` has all fifteen with when each is right.

| The ask | Field | Type | Flags |
|---|---|---|---|
| "What is it made of" | Materials | Multi-select | Filterable |
| "How do I wash it" | Care instructions | Long Text | None |
| "How big is it" | Dimensions | Dimension | None |
| "How heavy" | Weight | Weight | None |
| "Where was it made" | Country of origin | Select | Filterable |
| "Is it certified" | Certifications | Multi-select | Filterable |
| "Is it kosher / organic / vegan" | One Yes/No per claim | Yes/No | Filterable |
| "Link to the size guide" | Size guide URL | URL | None |
| "New, refurbished or open box" | Condition | Select | Filterable |
| "Let them engrave it" | Engraving text | Text | Customer Input |
| "Let them pick the metal colour" | Metal colour | Select with allowed values | Customer Input |
| "Show a spec sheet" | Specifications | JSON | None |

Two habits worth pushing:

- **One claim per Yes/No field** rather than a Multi-select of claims, when the merchant wants each to be its own filter toggle.
- **Select over Text** whenever the merchant can name the values today. Free text cannot be filtered, and a catalog of free text accumulates "Cotton", "cotton" and "100% cotton" as three different things.

## Response shape

> ✓ Care instructions are now set on all 12 linen shirts.
>
> I read the field id off Linen Shirt Oxford, which already had it, then wrote the same text to the other eleven.
>
> One skipped: Linen Shirt Sample is a draft, so I left it alone. Want it done too?

**When the definition does not exist yet:**

> I cannot create the field itself from here, only fill it in. Custom field definitions are made in the dashboard, under Products then Custom Fields.
>
> Create one called Country of origin, type Select, with your countries as the allowed values, and turn on Show in storefront filters so shoppers can narrow by it. Set it on any one product while you are there.
>
> Once one product carries it, come back and I will set it across the rest.

## Rules

- Definitions are dashboard, values are here. Never imply otherwise, and never attempt a write for a field you have no `definitionId` for.
- Read the `definitionId`; do not construct it from the key.
- `get_product_metafield` before overwriting, so the merchant hears what changed rather than only what it changed to.
- A write is an upsert with no undo, and it enqueues a sync to every connected sales channel. Treat it as a change to a live catalog, not a note.
- One product at a time, reporting as you go. There is no bulk write here.
- Filterable means Select, Multi-select or Yes/No. Do not promise a filter on a Text or Number field.
- The value is validated against the definition's type, so a date has to look like a date and a URL like a URL. A rejection is the definition disagreeing with the value, not a broken tool.
- This connector cannot remove a value. Point at the dashboard rather than writing an empty string, which leaves the field set to nothing rather than unset.

## Reference files in this skill

- `references/field-types.md`: all fifteen types, what each is for, and which support filtering.

## Cross-skill connections

- Whether this property should be a custom field at all: `brainerce-store-architecture`.
- Filling in fields while creating a product: `brainerce-product-onboarding`.
- Reading `product.metafields` in storefront code: `brainerce-sdk`.
- Rendering a filter UI from filterable fields: `brainerce-storefront-build`.

Route once, and do not bounce back and forth.
