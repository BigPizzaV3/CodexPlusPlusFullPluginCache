---
name: improve-ai-visibility
description: Use when the user wants AI assistants and AI search to recommend their brand more often, asks why competitors appear in AI answers instead of them, or asks which pages of their website to change based on their Searcherries data. Reads the Searcherries tools and turns the evidence into concrete page changes.
---

# Improve AI visibility from Searcherries data

Searcherries tracks how AI platforms answer the customer questions a brand cares about, which competitors and pages they name, and the site's Google Search Console, Bing Webmaster Tools and GA4 AI-traffic data. The Searcherries tools return that data read-only.

## 1. Find the project

- If the user names a brand or domain, call `get-action-plan` with `project` set to it and `audience` set to `marketing` (use `seo` when the user asks about search traffic). It returns dated priorities and the `project_id`.
- If you can read the website's code, look for the site's domain in the repository first (site config, `package.json` `homepage`, `CNAME`, sitemap, canonical URLs).
- If several projects match, or none, call `list-projects` and ask the user which one to use. Never guess.

## 2. Collect the evidence

Use the `project_id` from step 1.

- Gaps in AI answers: `get-ai-answers` with `prominence_max: 1` lists the answers where the brand is missing or only mentioned in passing. Read the full text of at most five of them (`include_answer_text: true`, `limit: 5`).
- Who wins instead: `get-competitors` (default `ranking`) shows the brands the platforms name; `dataset: "detail"` with `competitor` explains one brand.
- Which sources the answers rely on: `get-citations` with `prompt_id` for a gap question shows the cited URLs; `own_site_only: true` shows which of the site's own pages are already cited.
- Search demand: `get-search-performance` with `dataset: "opportunities"` (high impressions, low CTR, long-tail queries) and `dataset: "ai_question_queries"` (question-shaped searches). Use `source: "bing"` for Bing.

If a source is not connected, say so and continue with what is available. Missing data is unknown, not zero.

## 3. Turn the evidence into page changes

For each relevant page, propose specific changes tied to the evidence, for example:

- answer the tracked question directly near the top of the page, in the words customers use;
- state plainly what the product is, who it is for and how it compares, covering the facts the AI answers give for competitors;
- add an FAQ section for question-shaped queries that already bring impressions;
- link to the page from related pages so it is easier to find.

Flag gaps that need a new page rather than an edit.

If you can work with the website's code, find the source file behind each URL (routes, page components, Markdown or MDX content, templates), present the plan first, and edit files only after the user agrees. Otherwise, list the changes by page URL.

## Ground rules

- Searcherries data is read-only and dated. Quote the period of every figure you use.
- Do not invent numbers, rankings or competitors, and do not promise that a change will win a recommendation.
- Visits are not revenue. Do not present AI traffic as sales.
- Keep claims on the site true. Do not add statements the user cannot back up.
