---
name: brainerce-launch-a-sale
description: "Set up a sale, promotion or discount on a Brainerce store and confirm it is actually live. Use when the merchant says take 20% off, run a sale, put the winter range on sale, launch a promotion, create a discount code, set up a voucher, offer free shipping over a threshold, or schedule a Black Friday or holiday deal. The core of this skill is the choice between an automatic discount that applies by itself in the cart and a coupon code the shopper has to type, because getting that wrong is the mistake merchants notice. For store owners, not developers. Do not choose this to review how a past promotion performed, use brainerce-analytics. Do not choose this to hunt for expired or forgotten promotions across the store, use brainerce-store-health. Keywords: sale, discount, promotion, promo code, coupon, voucher, percent off, money off, BOGO, buy one get one, free shipping, bundle, Black Friday, clearance, markdown."
compatibility: ChatGPT, Claude Code, Claude Desktop, Cursor
maintainer: Brainerce
metadata:
  author: Brainerce
  version: "1.0.0"
---

Take a merchant from "put this on sale" to a promotion that is live, correct, and described back to them accurately.

## Core principle

You are helping someone run their shop. They do not think in entity names, rule types or ISO timestamps, so do not make them. Ask about the sale in the words they used, then translate. Never report a promotion as created until a listing tool has shown it back to you.

## When to use this skill first

- The merchant wants money taken off something: a product, a category, an order total, or shipping.
- The merchant asks for a discount code to hand out.
- The merchant wants a promotion scheduled for a date range or a named shopping event.
- The merchant asks whether a sale they set up is running.

## When NOT to use this skill first

- "How much did the sale make", "did the promotion work", "what is my revenue this week": use `brainerce-analytics`.
- "Find promotions I forgot to turn off", "audit the store": use `brainerce-store-health`.
- "The order should have had the discount on it": that is an order question, use `brainerce-order-handling`.

---

## Step 1: automatic discount, or a code? Decide this before anything else

Two different things are called a discount, and they behave differently for the shopper.

| | Automatic discount | Coupon |
|---|---|---|
| Tool | `create_discount_rule` | `create_coupon` |
| Shopper experience | Price drops by itself in the cart | Shopper must type a code at checkout |
| Who gets it | Everyone the rule targets | Only people who have the code |
| Merchant says | "20% off all jackets", "sale next week", "free shipping over 200" | "a code for my newsletter", "SPRING20", "a voucher for this customer" |

**The default is the automatic discount.** When the merchant says "give 10% off everything next week" and never mentions a code, they mean the price drops on its own. Reach for `create_discount_rule`.

**Use `create_coupon` only when** the merchant asks for a code, names a code word, or wants something they can hand to specific people.

**When it genuinely could be either, ask one short question before creating anything:**

> Quick check before I set this up: should the 20% come off by itself for everyone, or do you want a code that customers type in at checkout?

⛔ Never create a coupon and then describe it as an automatic discount. A merchant who is told "the discount is live" and then sees full prices on their own storefront has been given a wrong answer, not an imprecise one.

## Step 2: gather what the promotion needs

Ask only for what is missing, and only what changes the result.

- **What is on sale.** Everything, a category, specific products, or the order total. Use `list_products` or `list_categories` to resolve names the merchant used into real ones. If a name matches nothing, say so and offer the closest matches rather than picking one.
- **How much.** A percentage or a fixed amount. Read the store's currency from `get_store` rather than assuming; do not say dollars to a merchant selling in shekels or euros.
- **When.** A start and an end. "Next week" and "for the weekend" need turning into real dates, so state the dates you are using in your confirmation and let the merchant correct them.
- **Limits, only if the merchant raises them.** Usage caps, per-customer caps, a budget ceiling, whether it can stack with other offers.

Do not invent limits the merchant did not ask for, and do not ask about every optional field. A promotion with sensible defaults that they can adjust beats an interrogation.

## Step 3: create it

**Automatic discount:** call `create_discount_rule`. Pick the type from what the merchant described:

- `PRODUCT_DISCOUNT`: money off specific products or a category.
- `ORDER_DISCOUNT`: money off the order total.
- `BUY_X_GET_Y` and `BUY_X_GET_X`: buy one get one, and its variants.
- `VOLUME_DISCOUNT`: cheaper per unit at higher quantities.
- `SHIPPING_DISCOUNT`: free or reduced shipping.
- `BUNDLE`: a set of products priced together.

**Coupon:** call `create_coupon` with the code the merchant chose. Codes are normalised to uppercase, so tell them the code as it will actually appear. If they want to know what the coupon would take off a real order before announcing it, `preview_coupon_for_order` computes it without applying anything.

## Step 4: verify before you claim it worked

Call `list_discount_rules` (or `list_coupons` for a code) and confirm the thing you just created is there with the status you expect. A creation call that returned without an error is not the same as a promotion the shopper will see.

If it is scheduled rather than active, say so plainly. Merchants read "live" as "working right now".

## Step 5: tell the merchant, in their words

**Automatic discount, use this shape:**

> ✓ Your 20% off sale on Winter Jackets is set up and starts Monday 3 November, ending Sunday 9 November.
>
> Customers do not need a code. The lower price shows up on its own in the cart.
>
> Want me to turn it on now instead of Monday, or add anything else to it?

**Coupon, use this shape:**

> ✓ Your discount code SPRING20 is live now and runs until 31 March. It takes 20% off the order.
>
> Customers have to type SPRING20 at checkout for it to apply, so it only reaches the people you share it with.
>
> Want me to check what it would take off a typical order?

**Could not do it, use this shape:**

> I could not set that up: there is no category called "Wintre Jackets" in your store. The closest ones are Winter Jackets and Jackets. Which did you mean?

## Rules

- Verify with a listing tool before you say it is live. Every time.
- Say "code" out loud whenever a coupon is involved, and say "no code needed" whenever it is a discount rule. The distinction is the whole point.
- Use the store's real currency from `get_store`, and give dates as dates rather than "next week".
- If the merchant asks for a discount on something that does not exist, name the closest real matches and stop. Do not put the sale on a product you guessed at.
- Turning an existing promotion off is `toggle_discount_rule`, and it is worth offering when a merchant sounds worried about how much a sale is costing.
- This connector cannot delete a coupon or a discount rule. If the merchant wants one gone rather than switched off, say that removal is done in the Brainerce dashboard.
- Never describe stacking behaviour you did not set. If the merchant asks whether the new sale combines with an existing one, read the rules back with `list_discount_rules` rather than guessing.

## Cross-skill connections

- Performance of a promotion after the fact: `brainerce-analytics`.
- Sweeping the store for expired or forgotten promotions: `brainerce-store-health`.
- A specific order that should have been discounted: `brainerce-order-handling`.

Route once, and do not bounce back and forth.
