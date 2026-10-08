---
name: blog-post-writer
description: "Use when an estate or letting agent asks for a UK property blog post, news article, local market update, website article, or topic ideas that should be grounded in Propalt property or market data. Match an existing brand voice when the user supplies examples or a website can be accessed; do not require web access or a Word-document runtime to complete the writing task."
---

# Blog Post Writer

Write useful local property content backed by real Propalt facts.

## Workflow

1. Establish the intended area, audience, topic, and approximate length. If the user has no topic, use relevant Propalt market data to suggest two or three angles.
2. If the user supplies prior articles or accessible website content, mirror the useful parts of the tone and structure. If that content cannot be accessed, ask only for a short tone preference when it materially affects the result; otherwise use a warm, direct, knowledgeable estate-agent voice.
3. Pull only the Propalt data needed for the article. Typical choices:
   - `get_monthly_market` / `get_quarterly_market` for trends;
   - `get_hpi` for HPI history from a full postcode;
   - `selling_property_market_activity_properties_for_sale_post` or `letting_property_market_activity_properties_for_let_post` for current stock;
   - `get_comparable_by_property_id` for a resolved property's evidence;
   - `get_nearby_schools`, `get_nearby_transport`, or `get_nearby_amenities` for supported location content;
   - `get_demographics`, `get_households`, `get_income`, or `get_crime` only with supported geographic inputs and only as aggregate area context.
4. Write the article around 3–5 meaningful facts rather than dumping statistics.
5. Attribute Propalt-derived figures clearly as Propalt data. If external current context is needed and available, attribute it separately rather than presenting it as Propalt data.

## Writing rules

- No fabricated local facts, streets, prices, catchments, or statistics.
- Do not claim a school catchment from `get_nearby_schools`; it provides proximity, not catchment eligibility.
- Avoid em dashes and stock AI phrasing. Use concrete local language and short paragraphs.
- Do not make claims about a particular resident from aggregate demographic data.
- If a requested statistic is unavailable, omit it or say it is unavailable instead of filling the gap from memory.

## Delivery

Return a publish-ready article in chat by default. If the user explicitly requests a `.docx` and the host provides document-generation capability, create the file; otherwise provide clean copy that can be pasted into a CMS or Word. Do not make successful completion depend on installing packages.
