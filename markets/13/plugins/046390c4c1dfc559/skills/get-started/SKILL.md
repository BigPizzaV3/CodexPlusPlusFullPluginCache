---
name: get-started
description: Set up Human Forward Findability after installing it, confirm the connection works, and show the user their first score.
---

Help the user get their first findability report in ChatGPT.

1. Explain in one line what the plugin does: it reads the Findability report for their store or site, which scores how findable the brand is in Google, in AI answers and to AI shopping agents, and lists what to fix.
2. If the connection has not been authorised yet, tell them the sign in page asks for two things: the site (their store or site domain) and the connect code from Settings in the Human Forward app (app.humanforward.io or the Shopify app). No password is involved.
3. Call `get_overview`. If it returns a score, summarise it in two or three sentences: the number out of 100, the weakest of the three parts (search, AI answers, agent readiness), and the single biggest fix from `get_todo`.
4. If it returns an upgrade note instead, say plainly that the connector is part of the Scale plan and give the plan link from the note. Do not try other tools; they return the same note.
5. If there is no completed check yet, offer to start one with `run_check`, say it takes one to three minutes, and poll `get_overview` until the status is done.
6. Suggest the three prompts that work well next: "What should I fix first?", "What did ChatGPT say about us?", and "Can AI shopping agents buy from my store?".
