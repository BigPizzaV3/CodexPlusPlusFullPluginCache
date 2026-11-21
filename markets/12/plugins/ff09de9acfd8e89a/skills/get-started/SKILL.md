---
name: get-started
description: Explains what Get AI Cited measures and how to look up a company's AI visibility, compare a category, check a website's AI readiness, or read a signed-in customer's own reports.
---

# Get started with Get AI Cited

Get AI Cited measures how often AI answer engines (ChatGPT, Perplexity, Claude and Gemini) cite a company's website as a source and name the company when buyers ask category questions. Every figure comes from a dated, published snapshot.

Use the Get AI Cited tools like this:

1. **One company's AI visibility.** Call `get_company_score` with the company name or website. Quote the Cited Score, the snapshot date, the result on each engine and the companies named instead. If the company has not been measured, say so plainly. Never estimate or invent a score.
2. **Compare a category.** Call `list_categories` if the category is unclear, then `get_leaderboard`. Give the snapshot date with the ranking.
3. **Is a website readable by AI?** Call `check_ai_readiness` with the website. Summarise what passed and the most important fix. This checks technical readiness only, not whether engines recommend the company.
4. **How the score works.** Call `get_methodology` and explain the 70% cited / 30% named weighting and what the score does not measure.
5. **The signed-in customer's own data.** Call `list_my_companies` first, then `get_company_report` or `get_answers` for one of those companies. These tools ask the person to sign in to Get AI Cited.

The tools are read-only. They cannot change data, run new scans or see billing.
