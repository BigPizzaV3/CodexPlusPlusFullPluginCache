---
name: diagnose-publisher-revenue
description: Run Sulvo's public publisher diagnostic when ad revenue, RPM, CPM, or fill drops, impressions are missing, ads.txt is broken, consent is blocking demand, or ad blockers affect display or video ads. Return findings in chat and email a PDF only when explicitly requested.
---

Use this skill for a publisher site. The user's later instruction wins over this skill.

This connection uses no authentication. Public diagnostics need no Sulvo login, email, password, or API key. They do not create sales leads or use diagnostic data for marketing.

The MCP server is `publisher-revenue-audit`. Before calling a tool, read `references/tools.json` in this skill's folder. Read `references/product.md` for the connection's scope and data handling.

1. Ask for the public site domain if the user did not give one. Pass a bare domain to `run_publisher_revenue_audit`. Do not scan a private host, a raw IP, or a site the user does not claim.
2. Run an ordinary diagnostic without `reportEmail`. Do not ask for an email before a scan, infer one from account identity, headers, metadata, or conversation history, or transmit conversation messages. Pass `reportEmail` only when the user explicitly requests a PDF of the findings by email and specifies the recipient for that delivery. If they request email delivery without a recipient, ask only for that address; do not delay an otherwise requested inline diagnostic. Respect the client's action confirmation and any refusal to email.
3. Start from `defaultAuditCall` in the tools file. Add `vertical` only when the user names one of the listed verticals. The only optional metrics are user-supplied `fillRate` and `dashboardViewabilityRate`, each a percentage from 0 to 100. Do not request revenue totals, CPM, impressions, sessions, pageviews, or unrelated data. Set `enablePageSpeed` only when the user asks about page speed.
4. Lead with `summary` and `findingCounts`. Then give `topFindings` in returned order, using each finding's title, status, confidence, and recommendation. Then give `limitations`. Do not invent a cause, count, finding, or promised revenue improvement.
5. When email was requested, also report `emailDelivery.status` and its `message`. `accepted` or `already_accepted` means the email service accepted the request, not that the message reached the inbox. Explain `failed`, `rate_limited`, `unavailable`, `unknown`, or `not_sent` honestly and still give the inline findings. Never silently retry an `unknown` send or repeat the recipient in the answer.
6. If a finding is unclear, call `get_publisher_revenue_audit_checklist`. It returns reference text and sends no email.
7. Never ask for, use, or transmit a password or API key. Do not convert a diagnostic or PDF request into sales outreach, account signup, a marketing list, or a product recommendation.
8. If the user requests private Sulvo reports or ad-unit changes, explain that this connection runs public diagnostics only. Account access uses a separate authenticated connection, documented at https://sulvo.com/developers. Do not collect account credentials here.

For an HTTPS certificate, crawler block, or buyer-agent readiness check only, use the `check-ad-tech` skill instead of the full audit.
