# The five mechanisms, at field level

Distilled from the Brainerce merchant help centre. This is the detail that
decides an argument about which mechanism to use; the rules for choosing between
them are in SKILL.md.

Every one of these is a **module** and can be switched off for a store. If a
merchant says a section is missing from their sidebar, that is where to look:
Settings, then Modules. Do not tell them the feature does not exist.

---

## Attributes and variants

An **attribute** is a reusable option definition (Size, Colour, Storage,
Material) with a list of values. Attach two attributes to a product and the
variant editor generates one row per combination, the full Cartesian product.
Two sizes by fourteen colours is twenty-eight rows.

Each generated row carries its own **image, price, sale price, SKU, MPN,
description, inventory and downloadable flag**. Rows that do not correspond to a
real product can be deleted after generation, which is how a catalog with gaps
(128GB Wi-Fi and 256GB Cellular but no 128GB Cellular) is expressed.

An attribute has a **display type** that only affects storefront rendering, never
the data: Default (text chips or radios), Colour Swatch (each value read as a
colour), Image Swatch (a thumbnail per value), Mixed Swatch.

Two things that surprise merchants:

- **An option value is fixed once created.** Changing it means adding the new
  one, moving variants across, and deleting the old.
- **Renaming or deleting an option hits every product using that attribute**,
  immediately. Deleting an option does NOT delete the variant rows that used it;
  those have to be cleaned up per product.

Variants are also where **per sales channel overrides** live: once marketplace
channels are connected, each variant can carry a different price, sale price,
SKU, stock or name per channel.

## Modifier groups

A choice presented at checkout that changes the order total without creating a
new SKU or consuming inventory. AppleCare tiers, engraving, gift wrap, pizza
toppings.

A group carries:

- **Selection type**: Single (a radio, at most one) or Multiple (checkboxes).
- **Min and max** selections. Min 1 with Max 1 is exactly one, required.
- **Required**, which pairs with a minimum of at least one.
- **Free quantity** plus a **free allocation policy**, which is how "pick three,
  the first is on us" is expressed and which decides which of the shopper's
  picks consume the free slots.
- A **customer-facing name** and a separate **internal name**.
- **Active** or **Archived**. Archiving hides it from new attachments but leaves
  it attached where it already is.

Groups are reusable: build once, attach to many products. There is no tool for
any of this on the ChatGPT surface; it is a dashboard task in every respect.

## Custom fields (metafields)

Fifteen types: Text, Long Text, Number, Yes/No, Date, Date and Time, JSON, URL,
Colour, Dimension, Weight, Image, Gallery, Select, Multi-select.

The two flags that change what a field IS, both under Advanced Options on the
definition:

- **Customer Input** turns the field into a buyer-facing input on the product
  page, with a picker for which products it applies to. The buyer's value is
  saved as a line-item detail on the order. This is the mechanism behind
  engraving text, a monogram, or a ring colour the shopper chooses.
- **Show in storefront filters** exposes the field as a shopper-facing facet.
  ⛔ Available for **Select, Multi-select and Yes/No only**. Not for free text,
  not for numbers, not for any other type. A merchant who wants to filter by a
  number has to model it as a Select with bands.

A definition can also carry **Allowed Values** (which turns free input into a
constrained list), a **Description** shown as helper text in the product editor,
a **Default value**, and a set of **sales channels** to publish the definition to.

The field's **key** is derived from its name, lowercased with underscores:
"Warranty Info" becomes `warranty_info`. That key is what the storefront reads
and what a filter query uses.

## Categories

Hierarchical. Fields on a category: **Name**, **Parent Category**, **Active**,
**Tax** (taxable or a tax class, inherited by products in it unless overridden
per product), **Category Image**, and **Publish to Platforms**.

Each category gets its own storefront landing page at `/categories/<slug>`, a
breadcrumb trail on every product in it, and an entry in the navigation menu.
There is no enforced depth limit, but the storefront is built around two levels
and `create_category` says depth two is the practical limit.

Setting **Active** off hides a category from navigation and from product
selection without deleting it. That is the reversible move; deletion is not
available from the ChatGPT surface at all.

## Tags

Flat. Fields: **Tag Name**, **Active**, **Publish to Platforms**. That is the
whole model, on purpose.

No hierarchy, no landing page of their own, no children. They power custom
collections, filter chips, and promotional grouping without restructuring the
menu. A product can carry as many as it needs.

Convention worth holding to: lowercase and hyphenated, `summer-sale` rather than
`Summer Sale`, because a store accumulates `Summer`, `summer` and `Summer 2026`
within a year and nothing merges them afterwards.

## Brands

The manufacturer or label. Separate from both categories and tags, and the right
answer when a merchant asks where "Bellroy" or "Apple" goes. Assignable from
`create_product` and `update_product` by id or by name with auto-create; there
is no brand listing tool on the ChatGPT surface, so assign by name and let it
match case-insensitively rather than guessing an id.
