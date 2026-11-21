---
name: ai-visibility
description: Look up, request or check an AI visibility report for a website domain with meraGEO. Use when the user asks how often AI assistants mention a site or brand, wants a meraGEO scan, or asks whether a scan has finished.
---

Use this skill when the user asks how visible a specific website or brand is in AI assistant answers, asks for a meraGEO report or scan for a domain, or asks whether a scan has finished.

Do not use it for general SEO advice, writing content, auditing a page's wording, or questions that do not name a public website domain.

## Tools

- `get_ai_visibility_report`: reads the most recent stored report for a domain. It does not start a scan.
- `start_ai_visibility_scan`: requests a new scan. It reads the site's public pages and asks several AI models category questions. If a recent report already exists it is reused.
- `get_scan_status`: returns not found, scanning, complete (with the score) or failed.
- `get_profile`: returns the connected meraGEO account's id, display name and a masked email. It is read-only and used to tell connected accounts apart; call it only if the user asks which account is connected.

All four tools require the user to sign in to meraGEO. If they are asked to connect their account, tell them that is needed and wait. Do not try to work around it.

## Steps

1. Take the domain from the user. A full URL is fine, the tools reduce it to the domain. If the user did not name one, ask. Never guess a domain.
2. Call `get_ai_visibility_report`.
3. If a report exists, present it: the overall score and label, the per-model figures (how many of the sampled answers mention the site, for each model), and the top issues, exactly as returned.
4. If no report exists, say so and ask whether to request a scan. Call `start_ai_visibility_scan` only after the user agrees, because it starts real work against the site's public pages.
5. After a scan starts, tell the user it takes a few minutes. Call `get_scan_status` when they ask, or at a reasonable interval within the conversation, until the status is complete or failed. Do not poll in a tight loop. When complete, call `get_ai_visibility_report`.
6. If the status is failed, report that the scan did not finish and offer to try again once.

## Presenting results

- Lead with the score and what it covers, then the per-model counts, then the issues.
- Say it is a sample of AI answers at the time of the scan, not a ranking guarantee.
- Report only what the tools return. Do not state causes for a score beyond the listed issues, do not predict traffic, sales or rankings, and do not invent competitors or numbers.
- If a tool returns an error (invalid domain, daily scan limit reached, site not reachable), relay the message plainly. Do not retry in a loop and do not make up a report. If the daily limit is reached, existing reports can still be read.
- Only a public website domain is valid. Decline IP addresses, localhost and private hosts.
- Do not mention pricing, plans or upgrades.
