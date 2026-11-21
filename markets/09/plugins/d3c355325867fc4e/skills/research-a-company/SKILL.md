---
name: research-a-company
description: Build a short, sourced profile of a company from its website, including what it does, its brand and its key pages. Use when the user asks what a company does, wants a company overview, or wants its logo, colours or fonts.
---

Use this skill when the user names a company or gives its domain and wants to understand it. Work in this order and stop as soon as the question is answered.

1. Call `brand` with the company's `domain`. It returns the name, description, logos for light and dark backgrounds, colours and social profiles. If the user only asked for the logo, call `logo` with the `domain` instead.
2. If the user wants to know what the company offers or how it describes itself, call `scrape` on its homepage. Add its pricing or about page only when the question is about pricing or history; set `preferStructure` to true on pricing pages.
3. If the user wants to know what is on the site, call `map` with the homepage URL and show the relevant pages instead of reading them all.

Write the answer:

- Lead with a one or two sentence summary of what the company does, in its own words where possible.
- Then give only the details the user asked for, such as offering, pricing tiers, logo links, colours or fonts.
- Link every page you read.

When data is missing:

- If `brand` returns no description or no logo, say it was not found. Do not describe a logo or colour you have not seen.
- If the domain does not resolve or belongs to a different company than the user meant, say so and ask which company they meant.

Do not:

- Guess headcount, funding, revenue or founders. Report them only when a page you read states them, and cite that page.
- Read every page of the site when a single page answers the question.

The user's explicit instructions take priority over this skill.
