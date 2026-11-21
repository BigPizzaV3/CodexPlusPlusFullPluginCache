---
name: analyze-prices
description: Understand typical asking prices for a product and draw price histograms from aggregate data in the user's currency.
---

Call `analyze_prices` with a specific product query and the shopping country when known.

- For a specific product, pass `models` with its manufacturer model identifier and known same-model aliases. Use the base identifier in the search query. Matching ignores case, spacing, and punctuation, so formatting changes need no alias; `+` means Plus and remains a distinct model qualifier. Separated color/region suffixes such as `/B` remain eligible; attached suffixes such as `SA` require an explicit accepted alias. Do not guess aliases or use fuzzy matches. Omit `models` only for broad category searches; ask for the model identifier when the product is ambiguous.
- Model matching checks product/offer titles and variant option values without AI. Conflicting codes in the same numeric model family, common qualifiers such as Pro/Max/Ti, English accessory/compatibility cues, bundles, kits, multipacks, and offers without an accepted identifier are omitted. A distinct qualified model needs its complete identifier in `models`. It cannot verify catalog identity or detect every accessory reference.
- eBay open-box/New Other and New with defects are grouped with refurbished and used offers as secondhand, never new.
- Always pass `currency`: use the user's requested currency or an established currency preference from the conversation. Use `USD` when unknown. Keep shopping country and display currency independent.
- The server converts prices into the requested currency. Display returned integer minor-unit amounts in normal currency units; do not apply exchange rates again.
- Omit `bucketCount` for automatic histogram sizing independently for each condition after currency conversion. Pass an integer from 2–30 when the user requests a number of buckets or more or less detail; it applies to each eligible group and includes an overflow bin when present. The effective count may be lower for identical prices or currency precision.
- Explain the median, middle price range, sample size, and relevant messages. Sample size counts offers, not unique sellers. Keep conditions separate.
- Describe results as sampled asking prices. Product identity and final shipping, taxes, stock, and payment exchange rates may be unconfirmed. Explain returned matching limitations. If statistics are unavailable, report the limitation without inventing values.

When the user requests a histogram or price distribution chart:

- Use available visualization tools to draw each group's `bins`, using each bin's `count` for the number of offers. If unavailable, show a table of price intervals and offer counts.
- Finite bins include `lowerInclusive` and `upperInclusive`; the next bin starts one minor unit above the previous upper bound. An overflow bin has `upperInclusive: null` and starts at its `lowerInclusive`; label it as an open-ended range such as `$500+`. Keep empty bins and use returned counts without inventing individual prices or re-binning.
- Draw groups without overflow as numeric histograms. For groups with overflow, use labeled bucket bars because the final interval has no numeric width. Keep conditions in separate charts or panels; boundaries can differ between conditions, so do not overlay counts by bin index.
- Mark each group's median when available. For a chart with overflow, use an annotation or callout instead of positioning the median against a fabricated overflow width.
- Groups with fewer than five observations have null `statistics` and empty `bins`; explain the missing distribution. If all groups have empty bins, no group has enough observations for a histogram.
