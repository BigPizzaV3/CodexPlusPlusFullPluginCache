# Simplio3D pricing block types

## Item price blocks (the formula combines these into the unit price)

| Type | What it does |
|---|---|
| `base-price` | A fixed starting price. Always present and can't be deleted. |
| `price-group` | A price per variant of one or more linked option blocks (dropdown, select-material, checkbox, toggle, carousel, modular, number-input). |
| `price-table` | A 1-D or 2-D lookup: the price at the intersection of two selections (for example Width × Height). An axis must be a single-choice block, a number input or a modular block. |
| `unique-price` | Modular projects: prices a module by how many are placed, optionally depending on another selection. |
| `variable` | A named number used in the formula: a slider value, or a value that depends on a selection. |
| `markup` | A sell price from a private cost: a markup percentage or a target margin. Shoppers never see the cost. |
| `tier` (per unit) | A unit price that depends on the quantity ordered (for example 1–9, 10–49, 50 and above). |

## Step blocks (applied after the formula, in this order; never formula terms)

| Type | What it does |
|---|---|
| `tier` (order level) | Replaces a block's price for the whole order depending on the quantity. |
| `discount` | A percentage or fixed amount off the order, or off selected items. |
| `charge` | A setup or labor charge, once per order or per unit. |
| `freight` | Shipping: a flat amount, by destination zone or by weight; several options let the shopper choose. Can also be "quoted separately". |
| `tax` | A tax rate the seller entered (inclusive or exclusive), with an optional list of approved tax IDs that are exempt. |

## Order quantity

A project can let shoppers order several units. The quantity comes from a number input, the placed modules, checkbox selections or a variable. The unit price is multiplied by it before discounts, charges, shipping and tax.

## Price status

`calculate_price` returns `cpq.status`: `final`, `estimate` (the store checkout or the seller finalizes something), `pending` (something is missing: quantity, shipping choice or tax rate) or `quote-required` (shipping quoted separately), with the reasons.

## Number inputs

When a price group, table axis or variable is linked to a number input, each numeric parameter's price is **per unit**: the shopper's value × the unit price.

## Formula

The formula combines item blocks with `+ − × ÷` and parentheses. With no formula, every enabled item block is added up. With a formula, only the blocks it names count.

## SKUs

Price groups, variables, price tables and unique prices can each carry a SKU per variant or cell (Enterprise Modular projects). A Shopify "SKU-matched cart" checkout uses them to add real store products to the cart, so a missing or duplicate SKU breaks that line at checkout.

## Tax and display

Currency, symbol position and decimals are project settings (`get_project_settings`), as is the single tax rate used when the project has no Tax block. `calculate_price` applies them to its total.
