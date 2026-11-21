---
name: cross-border-cost
description: Use when someone asks what an online purchase from another country really costs at the door (import duty, VAT or GST, the landed total), where a named store ships from, or why a duty applies. Calls the Crossave tools instead of estimating.
---

# What a purchase from abroad really costs

A price shown by a foreign store is rarely what the buyer pays. Duty and VAT
are charged on delivery. Use the Crossave tools to compute them rather than
working the figures out yourself, and present them as estimates: customs and
the carrier set the final amount.

## Which tool

- A named store ("from wafuu.com", "on snipes.com"): call
  `costo_totale_dal_negozio`. It reads the store's real shipping origin and its
  published delivery charge, then computes duty, VAT and the total.
- Only countries and an amount ("a 300 EUR gadget from China to France"):
  call `calcola_costo_totale`.
- "Where is it cheapest?" / "best price delivered to me" for a named item:
  call `migliori_offerte` and show its card (up to 3 offers with a certain
  total and a button to all offers on crossave.com).
- Not sure which category value to pass: call `elenco_categorie` first.
- "Where does this store ship from?": call `sede_del_negozio`.
- "What does this store charge for delivery?": call `costo_spedizione`.
- "Why does this item pay that duty?": call `spiega_regola`.

## How to answer

- Lead with the total, then the breakdown (duty, EU handling fee, VAT).
- When the tool says the total is a minimum (`totale_e_un_minimo`) or a figure
  is not known, say so plainly. Do not fill the gap with a guess.
- Repeat the tool's warnings, such as a courier clearance fee.
- Close with the comparison link the tool returns, so the user can check live
  prices.

## When not to use it

Do not use these tools for services, business imports at scale, travel
allowances, or anything that needs a licensed customs broker. Do not use them
for questions unrelated to buying goods from another country.
