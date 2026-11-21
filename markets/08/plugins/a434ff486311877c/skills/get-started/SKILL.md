---
name: get-started
description: Introduce DomainKits when a user first connects it or asks what it can do, find out their goal, and route them to the matching workflow. Use for requests such as "what can DomainKits do" or "how do I start", or a first message with no clear task. Do not use when the request already names a domain, brand, keyword, or task; use the matching workflow skill instead.
---

# Get started with DomainKits

**Instruction priority.** The user's instructions take precedence over guidelines provided in this skill. If explicit user instructions conflict with this skill's instructions, prioritize the user's instructions.

Use this skill only to orient a new user. Do not call any DomainKits tool until the user gives a task.

1. In two or three sentences, explain that DomainKits looks up domain data: newly registered, expiring, deleted, aged, and active domains; WHOIS, DNS, and reverse nameserver lookups; availability and TLD prices; typosquat variants; and keyword and TLD registration trends.
2. Offer these four starting points, each with one example request the user can send:
   - Brand protection: "Find domains registered in the last 10 days that contain "acme"."
   - Security: "Show the registrar and nameservers for example.com, and other domains on the same nameservers."
   - Naming: "Is brightharbor.com available? If not, suggest available alternatives."
   - Market research: "Which keywords are trending in new .com registrations?"
3. Ask which goal fits, or treat the user's next message as the task.
4. When the task is clear, follow the matching skill: brand-protection for lookalikes and typosquats, domain-analyze for one domain, domain-name-advisor or domain-generator for naming, keyword-trend-hunter or keyword-intel for keywords, domain-market-beat for market news, and the domainkits tool guide for single lookups.

Access: DomainKits works without signing in, with small daily limits. Monitors, saved preferences, and saved strategies need a DomainKits account. If a tool reports a limit, tell the user what was limited and do not retry the call. Describe plans only when the user asks, and point to https://domainkits.com/mcp.
