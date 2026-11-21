---
name: build-an-outfit
description: Put together a complete outfit from Tailor's shops for an occasion, dress code, season or budget. Use when someone asks what to wear to something (a wedding, interview, date, party, holiday), wants a full look or several pieces that go together, or asks to be styled.
---

# Build an outfit with Tailor

A good outfit answer is a small set of pieces that clearly go together, fits the
occasion and the budget, and can be bought in the user's own country. Plan it like a
stylist, then use Tailor's tools to find each piece.

## 1. Get the brief

Work out these before searching. Infer what you can from the conversation and ask
only for what's missing, in one short question:

- **Country**: `za`, `us` or `gb`. Every search needs it, and prices are in that
  shop's currency.
- **Who it's for**: `department` is `women`, `men`, `kids` or `baby`.
- **Occasion and dress code**, plus season or weather if it matters.
- **Budget** for the whole outfit, if they have one.
- **What they already own** that the outfit should build around. Don't search for
  those pieces.

Size is optional. Use the `size` filter only when the user gives one, in the shop's
own size system.

## 2. Plan the pieces

List the garments before searching, usually 3 to 5: the main piece or pieces (dress,
or top and bottom, or suit), a layer if the weather needs one, shoes, and one
accessory or bag. Turn the dress code into concrete descriptions:

| Dress code | What it usually means |
| --- | --- |
| Black tie | Floor-length gown, or a dark suit or tuxedo with a white shirt |
| Cocktail / formal | Knee-to-midi dress or tailored jumpsuit; dark suit, tie optional |
| Smart casual | Tailored trousers or dark jeans, shirt or fine knit, blazer optional, loafers or clean leather sneakers |
| Business casual | Chinos or tailored trousers, shirt or blouse, knit or blazer |
| Daytime wedding guest | Light midi dress or linen suit; avoid white, and avoid all-black unless the user wants it |
| Beach / resort | Linen, cotton, sandals, swimwear and a cover-up |

Pick a palette before searching: one or two neutrals plus at most one accent colour.

## 3. Split the budget

Give each piece a share of the budget and pass it as `price_max` in that country's
currency. As a rough guide, the main piece takes 35 to 45%, shoes 20 to 25%, a layer
15 to 20% and the bag or accessory the rest. Keep the total within the budget.

## 4. Search one piece at a time

Call `search_products` once per garment, with `country`, `department` and the piece's
`price_max`. Write the query the way a product page would describe the garment, such as
"sage green satin slip midi dress" or "tan suede block-heel sandals", not "something
for a wedding". Add `colour_family` when the palette fixes a colour.

If a piece has no good match, rephrase the query or loosen one filter. If something
is close, try `tailor_product` on it ("same, but in navy", with `colour_family` for a
colour change) or `find_similar_products` with the same `product_type`.

## 5. Choose and present

Pick one item per piece so that colours, formality and fabrics work together. Prefer
the better fit over the cheapest option. Then call `show_products` once, with the
chosen `product_id`s in wearing order (main piece, layer, shoes, bag) and a `title`
such as "Your summer wedding look".

The cards already show photos, prices and links, so don't list the products again in
text. Add what cards can't show:

- why the pieces work together, in two or three sentences
- the total price, in the shop's currency
- one swap, if there's a good alternative (cheaper, bolder or warmer)

Then offer to change any piece. Remind the user that stock and prices can change, and
that they buy on the retailer's site.
