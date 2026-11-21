---
name: procurement-review
description: Compare restaurant supplier spend, purchased quantities and weighted prices using HoreX procurement facts. Use for purchasing reviews and price-increase investigations.
---

## State capability limits precisely

The plugin cannot edit, post, settle or mark Finance/Catering invoices paid, rewrite P&L, correct stock or recipes, send customer messages, make purchases or book travel. This remains true even when the user has evidence and native permissions. Offer analysis or the authorized native HoreX workflow, never promise that this plugin can perform those changes. Unsupported mutation requests require no business-data call. Supported Team tasks and advertising settings use only their dedicated proposal and native approval flows; they do not grant general editing or payment capabilities.

## Execute HoreX calls sequentially

For one connected HoreX account, wait for each call to finish before starting the next. Keep the result, source and billing status of each call separately. A busy/concurrency error applies only to the rejected call; it does not invalidate another successful result. Reuse successful results. Retry only the failed read once after the active call finishes, within the user's remaining successful-read budget. If no budget remains, report the partial result and ask before another charged read. Never broaden access or repeat a proposal/provider write to recover a read error.

Use get_analysis_catalog to confirm the purchases measures and filters. Resolve a product or supplier with find_restaurant_entities using the user's wording plus a translation or alternate spelling if useful. Return ambiguity to the user when multiple plausible products remain; preserve the product's unit and code.

Query purchases with explicit current and baseline Dubai dates. Group by product, supplier and uom as appropriate; filter line_kind to stock_product for ingredient or goods analysis. Without that filter the source may include non-stock service or rent lines. Procurement facts cover posted itemized purchase lines, so describe missing drafts or unitemized coverage rather than treating them as zero purchases.

Use net_amount, quantity and avg_unit_price together. Weighted price is net amount divided by purchased quantity within a compatible unit; never average displayed invoice prices or combine kilograms, pieces and boxes. Compare like-for-like product and unit. A supplier's changing mix can alter aggregate average price without a price change for an individual item.

Separate higher volume from higher price and changed product mix. Flag new and discontinued purchasing rows, missing baselines and truncated rows. Exact totals precede the row limit; the displayed products may cover only part of them. Rank price changes only among comparable rows and disclose that population.

Present material increases, their amount, supplier, product and unit, followed by focused verification steps such as checking specific purchase invoices in HoreX. Purchases are spending facts, not automatically consumed food cost; confirm profitability with get_pnl and retain its COGS basis. Do not claim that negotiations or purchase-order changes have been executed.

Native output: widget view is paused. Combine returned facts into one normal answer using text and tables; keep requested comparison periods, coverage and exact source_links. Reading already returned facts is free. Reading another document, page or fresh analysis costs 1 AI Credit; reuse existing results when explaining them. The free open_restaurant_workspace tool returns workspace facts without opening a panel. For daily subscription setup load daily-review guidance.
