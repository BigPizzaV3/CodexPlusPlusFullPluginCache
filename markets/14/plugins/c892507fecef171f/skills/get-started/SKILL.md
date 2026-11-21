---
name: get-started
description: Start using DC Hub in ChatGPT. Shows what DC Hub can answer about data-center sites, power, grid, fiber and deals, with example questions to try.
---

# Get started with DC Hub

DC Hub answers questions about where data centers can be built and powered, using live, dated data. Every tool is a read-only lookup. Nothing is changed in DC Hub or in your account. No sign-in is needed.

## Try asking

- "What is the live grid situation and time to power in ERCOT for a 200 MW data center?"
- "Rank the top 5 US data-center markets by DCPI verdict and show time to power."
- "Find operational data centers in Ashburn, Virginia over 50 MW."
- "What are the hazard, water and fiber conditions at 33.45, -112.07 for a data center?"
- "Show recent hyperscaler data-center deals and this year's M&A transactions."

## What to expect

- Answers carry an as-of date and a citation line. Quote them as "DC Hub (dchub.cloud), as of <date>".
- Some fields may come back as previews. The response marks the withheld fields and returns the rest; never fill them in with guesses.
- For questions that span several topics (power, queue, fiber, market), the `execute_plan` tool runs the steps in one call.
