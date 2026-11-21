---
name: check-ad-tech
description: Check a publisher's HTTPS certificate, ad-crawler blocks, or buyer-agent readiness. Use for SSL errors, robots.txt blocking Google or Amazon ad bots, adagents.json, or whether an AI buyer can find the site. Return findings in chat; email a PDF only when explicitly requested.
---

Use this skill for one technical check. The user's later instruction wins over this skill.

This connection uses no authentication. Run its tools without a Sulvo login, email, password, or API key. Diagnostics do not create sales leads or use inputs for marketing.

The MCP server is `publisher-revenue-audit`. Each tool below takes a bare public `domain`. The only optional contact input is `reportEmail`, and only for a PDF the user explicitly requests to that recipient. Results include Markdown text and `structuredContent`; these tools have no `outputFormat` argument.

- Certificate, HTTPS, or SSL: call `check_https_certificate`.
- robots.txt, ad crawlers, AmazonAdBot, or Google ad bots: call `check_crawler_blocks`.
- Buyer agent, adagents.json, or agentic readiness: call `run_agentic_readiness_audit`.
- A quick setup pass that is not a revenue question: call those three tools. Each sends its own PDF only if that delivery was requested; do not add unrequested emails.

Report the tool result. Do not invent a failure. If `skipped` is true, say the site could not be reached and the check did not run. An empty `rows` list means the tool returned no findings, not proof the site is fine. If evidence says the page could not be fetched, such as `ENOTFOUND` or a timeout, report that limitation.

For an ordinary check, omit `reportEmail` and do not ask for email. If the user explicitly requests an emailed PDF, use only the recipient specified for that delivery. If no recipient was given, ask only for the address needed to fulfill that request. Never infer contact details from account identity, headers, metadata, or conversation history, and never send conversation messages. Respect client confirmation and any refusal to email.

Always return the inline findings. If email was requested, report `emailDelivery.status` and its `message` accurately. `accepted` and `already_accepted` are provider acceptance, not proof of inbox delivery. Explain `failed`, `rate_limited`, `unavailable`, `unknown`, or `not_sent` without hiding findings. Never silently retry an `unknown` send. Do not repeat the recipient in the answer.

If the user asks why revenue, CPM, RPM, fill, or ads.txt is down, use `diagnose-publisher-revenue`.

Do not request or transmit passwords or API keys. Do not turn a diagnostic or PDF request into sales outreach, signup, or marketing. Private account reports and ad-unit changes require the separate authenticated Sulvo connection, documented at https://sulvo.com/developers.
