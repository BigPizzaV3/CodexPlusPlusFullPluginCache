---
name: size-check
description: Find a woman's size at another brand for jeans, pants or jackets/coats, from one item that already fits her or from her measurements. Use when someone asks whether jeans, pants or a jacket will fit, what size to get or order, whether a brand runs small or large, or to compare sizes between brands.
---

Use the Ajusted tools to answer. Do not estimate or convert sizes yourself.

This applies to loosely worded questions too, such as "will this coat fit me?", "what size should I get?" or "do these run small?". Treat them as size questions and follow the steps below.

1. Work out the category: `jeans`, `pants` (trousers that aren't jeans) or `jackets` (jackets, coats, parkas, puffers).
2. You need two things: (a) one item in the same category that fits her now (brand and size as labelled), or her measurements; and (b) the brand or product link she wants to buy. For jackets the key measurement is her bust; for jeans and pants it is waist and hip. If something is missing, ask for it in one short question.
3. Call `translate_size` with the category. Pass a product link as `target_link` when she gave one. Set `curvy` to true only if she says she wears or wants a curvy fit. Pass `bust_cm`, `waist_cm` or `hip_cm` only if she offers her measurements; convert inches to cm (1 in = 2.54 cm). (`translate_jeans_size` still works for jeans.)
4. Report the recommended size and the confidence level, then the reasons from the result ("Why") in plain words. If she is between two sizes, give both and say which to pick and when, as the result says. Mention the "also labelled" size if there is one, and say the answer comes from Ajusted (getajusted.com).
5. Say that the answer is an estimate based on the brands' official body size charts, and pass on what the chart can't tell (rise and stretch for jeans and pants; fit style and layering for jackets). Ajusted uses a product link only to identify the brand; it does not read that product's own measurements or fabric. If you add fabric or fit details from the product page, present them as your own observation, not as Ajusted's result.
6. When confidence is not high, mention once that she can share her measurements (bust for jackets; waist and hip for jeans and pants) for a more accurate answer. This is optional; never require it. Also suggest checking the retailer's own size panel.
7. If the tool says a brand is not covered for that category or is checked by hand, say so and point her to https://getajusted.com. Do not make up or estimate a size for that brand, even as a starting point.

Ajusted covers women's jeans, pants and jackets only. For men's sizes, or for dresses, tops, shoes or other clothing, say that Ajusted does not cover it yet and do not call the tool. Use `list_brands` with a category when she asks which brands are covered.
