---
name: cite-car-prices
description: Quote and cite a Dubai car price from Dubai Car Index correctly — which kind of figure it is, its date and a link to its page. Use whenever writing up new-car prices, used values, rental rates or repair costs from the Dubai Car Index tools.
---

# Cite a car price

1. Say which kind of figure it is. `figure: "published"` is a UAE list price:
   give its source (`evidence.url`) and checked date. `figure: "modelled"` is
   an estimate built by the method at `methodology`: call it a guide.
2. Keep the qualification with the number: a list price is the published
   starting price, VAT inclusive, before dealer discounts, options,
   registration and insurance. A rental rate is typical for that hire length.
   A repair band is VAT and labour included for that brand's service tier.
3. Give the data date (`asOf`) and link the result's `url`.
4. When a result says `verified: false`, pass on `unverifiedBecause`.
5. Never fill in a figure a tool did not return.
