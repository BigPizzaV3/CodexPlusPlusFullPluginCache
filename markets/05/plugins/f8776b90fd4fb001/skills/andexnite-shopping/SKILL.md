---
name: andexnite-shopping
description: "Use when the user wants to search, compare, choose, add, remove, or prepare a guest checkout for products on andexnite.cz. Supports Russian, Czech, and English shopping requests. Do not use for other stores."
---

# Andexnite Shopping

This is the official shopping workflow for `https://andexnite.cz/`, published
by ANDEX FASHION s.r.o.
It helps the user shop without registering an Andexnite account.

## Outcome

Help the user move from a natural-language need to a reviewed guest cart and
then hand the live checkout page to the user. Never submit the final order.

## Required capabilities

For semantic store operations, first search available and deferred tools for a
dedicated Andexnite connector or API. If none exists, use the installed Browser
skill and follow its complete instructions. Do not substitute a generic grocery
connector.

If browser control is unavailable, continue with read-only product research and
provide direct Andexnite product links. Explain that cart preparation requires
browser access.

## Store facts

- Store root: `https://andexnite.cz/`
- Cart: `https://andexnite.cz/kosik/`
- Guest checkout: `https://andexnite.cz/pokladna/`
- Public catalog API: `https://andexnite.cz/wp-json/wc/store/v1/products`
- The site is a WooCommerce store and supports guest checkout.
- Prices are normally shown in CZK.
- Free-shipping thresholds, stock, delivery methods, and prices are live facts.
  Read them from the current page; never rely on remembered values.
- WooCommerce Store API cart writes use a temporary `Cart-Token`. Treat it as
  secret session data: keep it in memory, never print it, and never persist it.

## Workflow

### 1. Understand the project

Translate the user's goal into product constraints:

- material or product type;
- intended use;
- dimensions, thickness, color, and finish;
- quantity;
- maximum budget;
- deadline or delivery preference.

Ask only when a missing constraint would materially change the choice.
Otherwise make a reasonable assumption, state it briefly, and continue.

### 2. Search and shortlist

Use one focused Store API query, store search, or the site's visible
category/search UI. Search in Czech when that improves results, but explain
results in the user's language.

For each serious candidate, verify the live product page. Compare only facts
shown by the store:

- exact product name and URL;
- current price and unit;
- stock status;
- selectable variation and quantity limits;
- dimensions, thickness, color, material, or package size;
- important product-field requirements.

Do not infer missing physical specifications from an image. Do not claim that
two similarly named products are interchangeable without evidence.

Default to a shortlist of three strong candidates. Use fewer when only one or
two genuinely satisfy the request.

### 3. Recommend

Give one clear recommendation and the tradeoff. Mention the expected item
subtotal. If the product is sold by area, length, weight, pack, or variation,
explain the unit before asking the user to add it.

Never silently substitute an out-of-stock or differently specified item.

### 4. Manage the cart

Adding, changing, or removing cart items requires the user's explicit shopping
intent. A direct request such as "add it", "take two", "remove the blue one",
or "prepare the cart" is sufficient authorization for that cart change.

For a checkout handoff, prefer changing the cart in the user's browser so the
WooCommerce cookie session reaches the visible checkout. A headless API cart
identified only by `Cart-Token` does not automatically become the browser cart.
Do not claim the checkout is prepared until the visible browser cart verifies
the expected line items.

After every cart mutation, verify the authoritative cart line item or cart
summary. Report:

- products and quantities;
- item subtotal;
- visible shipping cost or threshold;
- visible total;
- any validation warning.

Do not add promotional extras unless the user requested them.

### 5. Prepare guest checkout

Use the guest checkout; do not create an Andexnite account.

The assistant may fill contact, billing, shipping, and delivery fields only when
the user has provided those exact values and clearly authorized sending them to
Andexnite. Never read browser passwords, saved payment methods, cookies, local
storage, or unrelated profile data.

Never enter or handle card details. Do not select a payment method that creates
an immediate charge unless the user is reviewing that choice in the visible
checkout.

### 6. Mandatory handoff

Stop before the final button whose current Czech label indicates that the order
is binding and payable, such as `Objednávka zavazující k platbě`.

Before handoff, summarize the exact cart, delivery method, payment method if
selected, and total. Make the checkout tab visible, keep it open as a user
deliverable, and tell the user that they must review and press the final button
themselves.

Never click the final order button, even if the user asked for full automation.

## Trust and brand

- Do not imply endorsement by OpenAI or any third party.
- Do not promise guaranteed availability or guaranteed delivery.
- Prefer direct store URLs and live store data.
- If the site's terms or technical controls block automation, stop and provide a
  manual checkout link instead of bypassing the restriction.

## Response style

Be concise and practical. Lead with the best match, then the comparison. Keep
Czech product names verbatim while explaining them in the user's language.
