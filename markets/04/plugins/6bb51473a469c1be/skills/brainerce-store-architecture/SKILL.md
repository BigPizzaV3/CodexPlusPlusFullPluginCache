---
name: brainerce-store-architecture
description: "Decide how a Brainerce catalog should be structured, and diagnose one that is already wrong. Use when the merchant asks how should I organise my shop, should this be a variant or an option, categories or tags, how do I set up my menu, my product list is a mess, or I have hundreds of variants I cannot manage. Answers the modelling question before anything is created: what becomes a variant, what becomes a custom field, what becomes a category, what becomes a tag. Also audits an existing catalog and returns an ordered improvement plan. For store owners, and for developers deciding a data model. Do not choose this to add one product, that is brainerce-product-onboarding. Do not choose this for custom fields in depth, use brainerce-custom-fields. Do not choose this for pages, menus or blog, use brainerce-content-and-navigation. Keywords: catalog structure, variants or options, variant explosion, too many variants, categories vs tags, hierarchy, menu structure, product model, organise my shop, catalog audit."
compatibility: ChatGPT, Claude Code, Claude Desktop, Cursor
maintainer: Brainerce
metadata:
  author: Brainerce
  version: "1.0.0"
---

Get the catalog model right the first time, or find out exactly where an existing one went wrong.

## Core principle

A Brainerce store has five different mechanisms for "this product has a property", and they are not interchangeable. Picking the wrong one is cheap on day one and expensive on day two hundred, because the fix means touching every product. So the modelling question comes before the create call, always.

The single test that resolves most of it: **does this property have its own stock count, its own price, or its own SKU?** If yes it is a variant. If no it is something else, and the rest of this skill says which.

## When to use this skill first

- "How should I organise my shop", "what is the right structure for this".
- "Should size be a variant or an option", "variant or custom field".
- "Categories or tags", "how do I build my menu".
- "I am about to add my first products" and nothing exists yet.
- "I have 400 variants on one product and I cannot manage it".
- "Review my catalog", "is my structure sensible".

## When NOT to use this skill first

- Adding one product now, the model already settled: `brainerce-product-onboarding`.
- Custom fields in depth, including writing values: `brainerce-custom-fields`.
- Pages, navigation copy, policies, blog, SEO: `brainerce-content-and-navigation`.
- A read-only sweep for drafts, empty stock and stuck orders: `brainerce-store-health`.
- Building the storefront code that renders any of this: `brainerce-storefront-build`.

---

## The five mechanisms

| Mechanism | What it is | Own stock? | Where it is set up |
|---|---|---|---|
| **Variant** (from an attribute) | One row per combination, each with its own price, SKU and inventory | Yes | Dashboard variant editor, or `variants` on `create_product` |
| **Modifier group** | A choice at checkout that changes the price but not what you ship | No | Dashboard, Products then Modifiers |
| **Custom field** (metafield) | Structured data on the product; 15 types; can be buyer-facing or a storefront filter | No | Definition in the dashboard, value from chat |
| **Category** | The product's one permanent home in the menu tree | n/a | `create_category`, or the dashboard |
| **Tag** | A flat label that cuts across the tree | n/a | `create_tag`, or the dashboard |

## Want X, use Y

| The merchant wants | The right mechanism |
|---|---|
| Shoppers pick between options and each option is counted, priced and shipped separately | Variant |
| Shoppers pick an add-on that changes the total but not what leaves the warehouse | Modifier group |
| Shoppers type or choose something personal, and it should print on the order | Custom field with Customer Input turned on |
| Shoppers narrow the product list by a property | Custom field of type Select, Multi-select or Yes/No, with storefront filters turned on |
| A spec that only needs to be displayed, never chosen or filtered | Custom field of any type |
| A permanent place in the navigation menu | Category, nested under a parent |
| A collection that cuts across the menu, or a seasonal grouping | Tag |
| Who manufactured it | Brand |
| A different price in another country | Regional pricing, dashboard |
| The same catalog sold in more than one place | Sales channels |

Two of those rows are the ones merchants get wrong, and they have their own rules below.

---

## Rule 1, the variant rule

**A variant exists only for a property that changes price, stock or SKU. Everything else is a custom field.**

The reason is arithmetic. Variants are the Cartesian product of their attributes, so every attribute multiplies. Three attributes with 6, 5 and 15 values is 450 rows, and each row wants its own price, its own SKU and its own stock number. Nobody maintains 450 rows. The catalog stops being edited, stock drifts, and the storefront starts offering combinations that do not exist.

**The worked example, and it is the one to reach for.** A jewellery store sells a ring in several diamond sizes, several metal colours, and every ring size.

- **Diamond size is a variant.** A bigger stone costs more. Price changes, so it earns its own row.
- **Metal colour is a custom field, not a variant.** Same price, same stone, same SKU in most catalogs. Make it a Select custom field with Customer Input turned on, so the shopper still chooses it on the product page.
- **Ring size is a custom field, not a variant.** Same reasoning, and it is the attribute that multiplies hardest.

That takes the product from 450 unmaintainable rows to 6 real ones plus two fields.

**The honest exception, and say it out loud.** If the merchant genuinely holds separate stock per metal colour, boxed and on a shelf, then colour changes stock and it IS a variant after all. The rule is the test, not the answer. Ask "if a customer buys the gold one, which number goes down" before deciding.

### Spotting a variation explosion

You are looking at one when any of these is true:

- A product has more variant rows than the merchant could plausibly count in a stock take.
- Most variant rows carry the same price. A property that never changes the price is not earning its row.
- Whole blocks of rows sit at zero stock and always have, because those combinations were generated but never existed.

The fix to propose: keep the one attribute that moves the price, and demote the others to custom fields with Customer Input. Say plainly that this is a rebuild of that product rather than an edit, and that the variant editor is a dashboard job.

## Rule 2, the navigation rule

**A hierarchical menu is parent and child categories. Tags are for filtering across the tree, never for hierarchy.**

"Mobile" as a parent, with "iPhone" and "Samsung" as children, is how a shopper walks down to what they want. Each category gets its own landing page and a breadcrumb on every product in it. Two or three levels is the practical limit; `create_category` accepts `parentId` and the storefront is built around depth two.

Tags are flat by design. They have no landing page and no children. `summer-sale`, `gift-under-50` and `bestseller` are tags because they cut sideways across the menu and because they change with the season, while the menu should not.

The test: **would removing this label leave the product with no home in the menu?** If yes it is a category. If the product still has a home and this was just another way to group it, it is a tag.

A product normally sits in one category. Putting it in several creates duplicate navigation entries and a breadcrumb that cannot decide what it is.

### Spotting a flat catalog

- `list_categories` returns many categories and none of them has a parent. A store with thirty top-level categories has a menu nobody can read.
- The same words appear as both a category and a tag.
- Tags carry the structural nouns ("phones", "laptops") while categories carry the seasonal ones. That is the two mechanisms swapped.

---

## Review mode, auditing a catalog that already exists

Read only. Diagnose, present the plan, then let the merchant pick. Do not restructure anything mid-audit.

1. **`count_products`** first, so you know whether a sample or the whole catalog is being judged, and say which.
2. **`list_products`**, paging through it. Each product comes back with its variants and its custom-field values, so this is where variation explosion and empty modelling both show up. Note the variant count per product and whether the prices differ across those variants.
3. **`list_categories`**, for the tree. Count how many have a parent. None with a parent on a large catalog is the flat-catalog finding.
4. **`list_tags`**, and compare the names against the category names. Overlap is the swapped-mechanism finding.
5. **`list_product_metafields`** on a few representative products, to see which custom fields are actually in use and which products are missing the ones their neighbours have.

Then report against the four failure modes, most costly first:

- **Too many variants on a product**, with the number and which attribute is not earning its rows.
- **A flat category list**, with the tree you would propose.
- **Tags doing a category's job**, naming the specific tags.
- **A property that should be a custom field and is not recorded anywhere**, which is usually the one costing the merchant filter traffic.

**Use this shape:**

> ✓ I went through 240 products. Three things worth changing, most costly first:
>
> 1. **Solitaire Ring has 300 variants** and 280 of them are the same price. Only diamond size moves the price. Metal colour and ring size should be custom fields the shopper picks on the page, which takes it to 6 rows.
> 2. **All 34 of your categories are top level.** There is no menu to walk down. I would nest them under Rings, Necklaces and Earrings.
> 3. **`rings` and `necklaces` exist as tags as well as categories.** The tags are doing nothing the categories do not, and they split your filters in two.
>
> Also fine: every product has a category, and your custom fields are used consistently across the Rings range.
>
> Number 2 is the one I can do from here. Want me to build that tree?

## Planning mode, before the first product exists

Four questions, then a structure. Do not create anything until the merchant has seen the plan.

1. **What are you selling, and roughly how many lines?**
2. **For one typical product, what does a shopper choose before buying?** List every choice.
3. **Which of those choices changes the price, or is counted separately in your stockroom?** Those are the variants. Everything else on the list is a custom field.
4. **How would a shopper browse to it if they did not use search?** That answer is the category tree.

Then hand back: the category tree with parents and children, the attribute or attributes that become variants, the custom fields with their types and whether each is buyer-facing or filterable, and any modifier groups. Say which parts you can build now and which are dashboard steps.

## What can be done from here, and what cannot

**From this conversation:**

- `create_category` with `parentId`, so the whole tree can be built from chat.
- `create_tag`, after `list_tags` to avoid a near-duplicate.
- `create_product`, including its `variants` array.
- `update_product` to move products between categories. ⛔ `categories` REPLACES the set while `categoryNames` is additive, so read the product first and know which one you want.
- `set_product_metafield` to write a custom-field value, but only for a field some product already carries. See `brainerce-custom-fields` for why.

**Dashboard only, and say so rather than improvising:**

- Creating a custom-field definition, and its type, its allowed values, its Customer Input flag and its storefront-filter flag.
- Attributes and the variant editor beyond what `create_product` accepts.
- Modifier groups, in every respect.
- Regional pricing.
- Deleting anything at all.

## Rules

- Answer the modelling question before creating anything. A product created under the wrong model is a rebuild, not an edit.
- Never propose a variant for a property that does not change price, stock or SKU. Say the arithmetic out loud when refusing.
- Never propose a tag where the merchant described a menu.
- Read before you write. `list_categories` and `list_tags` first, every time, because this connector cannot delete the near-duplicate you create.
- Give the number. "Too many variants" is ignored; "300 variants, 280 at the same price" is acted on.
- When the plan needs a dashboard step, name the exact place, and do not imply you did it.

## Reference files in this skill

- `references/mechanisms.md`: all five mechanisms at field level, including the attribute display types, the modifier group selection and free-quantity rules, and the two custom-field flags. Read it when an argument turns on a detail rather than on the choice.

## Cross-skill connections

- Custom fields in depth, including writing values: `brainerce-custom-fields`.
- Pages, navigation copy, policies and blog: `brainerce-content-and-navigation`.
- Creating the products once the model is settled: `brainerce-product-onboarding`.
- Rendering any of this in a storefront: `brainerce-storefront-build`.
- The exact SDK shape of a category tree or a metafield: `brainerce-sdk`.

Route once, and do not bounce back and forth.
