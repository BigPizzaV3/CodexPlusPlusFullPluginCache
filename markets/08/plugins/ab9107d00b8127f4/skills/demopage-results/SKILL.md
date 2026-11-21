---
name: demopage-results
description: Summarize how the user's DemoPage demos are doing (visits, live demos, leads, the questions buyers asked most, and pages kept out) and suggest what to add next. Use when the user asks about DemoPage results, demo leads, what buyers asked, or how their demo is performing.
---

# DemoPage results

1. Call `demopage_results` from the `demopage` MCP server. If there is no demo link yet, say so and offer the `create-demopage` skill.
2. Report, in plain sentences:
   - the funnel for the last `days` days: visitors who saw the demo (`seen`), opened it, typed a request, and sent it (`sent`); demos `started` and `finished`; `leads`; and clicks on the call to action (`cta`) and booking link (`booking`);
   - the questions buyers asked most, with counts;
   - pages kept out of demos and why;
   - the latest leads: email, company, and what they wanted.
3. Suggest the next move. For each top question the demo couldn't answer well, and each page kept out, name the screen in this repo that answers it, if there is one. Offer to import or correct those pages with `demopage_import_pages`; the user approves them before they go live.

Lead emails are the vendor's own leads. Show them only to the user, and never copy them into files, commits, or other tools unless the user asks.
