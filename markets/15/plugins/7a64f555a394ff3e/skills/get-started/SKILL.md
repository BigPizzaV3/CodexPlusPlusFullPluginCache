---
name: get-started
description: Introduce Firmium when the user is new to it, asks what Firmium can do, or asks how to use it in ChatGPT. Auf Deutsch z. B. "Was kann Firmium?".
---

Use this skill when the user asks what Firmium is, what it can do, or how to start.

1. Explain in two or three sentences that Firmium provides company data from official European company registers: profiles, management, shareholders and beneficial owners, annual financials, insolvency and sanctions information, a change feed, prospect search and watchdogs that monitor changes.
2. Mention that a Firmium account is required and that the countries and features available follow the user's Firmium plan.
3. Offer three concrete starting points and let the user pick one:
   - "Show me the company profile of <company>."
   - "Who owns <company> and who runs it?"
   - "Find <industry> companies in <region>."
4. Call `ping` only if the user asks whether the connection works.

Answer in the user's language. Explicit user instructions take priority over this skill. Do not describe pricing, plans or upgrades.
