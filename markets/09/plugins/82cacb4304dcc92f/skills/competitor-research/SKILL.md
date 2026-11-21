---
name: competitor-research
description: Find keywords worth targeting for organic app growth from direct competitors' verified rankings and localized product evidence in Stora.
---

Select the app, platform and storefront through `get_context` and `list_apps`. Read `get_competitors`, `get_competitor` and `get_competitor_gaps`. Use `get_competitor_keywords` for a specific rival. Follow pagination and check research run status, ranking depth, dates and sources.

Prefer direct competitors serving the same user need. Assess the app's actual features and localized live listing before recommending a term. A word in a competitor's title, autocomplete candidate or cross-market visibility is a lead; verified rank evidence and product relevance determine whether it is useful. Do not convert candidates into proven demand, or a reference market into localized demand.

When the user requests new research, queue `discover_competitor_keywords` for the chosen competitor and market, then report the returned run, ETA and progress. A queued or incomplete job is not completed research. Avoid repeated discovery for an already queued run.

For each recommended gap give the rival's observed rank, our observed rank or capture absence, storefront, date, relevance reason and uncertainty. If the user requests tracking, use `get_keyword_config` and `ensure_keyword_scopes` for exact pairs, preserving existing markets. Role or intent changes through `set_competitor_role` and `label_intents` need a reason grounded in the current product.
