---
name: get-started
description: How to answer questions with NetNest SEC Fundamentals, citing the source filing for every number.
---

# Getting started with NetNest SEC Fundamentals

Use these tools for numbers that US companies report to the SEC. Every value comes back with its source filing; cite it.

* Unsure of the ticker: call `search_company` with the company name first.
* Latest key numbers for one company: `get_company` with the ticker.
* Specific metrics or a period (annual, quarterly or ttm): `get_fundamentals`.
* One metric over time: `get_history`, newest first.
* Recent SEC filings across companies (8-K items, Form 4 insider transactions, 13D and 13G stakes): `get_events`. `get_events_head` says whether anything is new since a cursor.

When answering:

* Give the value with its period end, the form (10-K or 10-Q) and the filing date, and link the SEC filing.
* A value marked `derived` was calculated from the inputs listed with it; say so.
* A `null` value comes with a reason; report the reason, never a guess.
* The data has no prices, forecasts, ratings or signals, and it is not investment advice. Decline requests to trade, to predict prices or to recommend buying or selling.
