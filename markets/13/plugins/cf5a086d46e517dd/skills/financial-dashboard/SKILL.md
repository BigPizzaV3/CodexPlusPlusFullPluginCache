---
name: financial-dashboard
description: Create, restyle, refresh, or maintain a private personal-finance dashboard using the user's connected Fina account. Use when the user wants a visual overview of their finances or asks to keep that dashboard updated. Ordinary balance questions and single spending queries use Fina tools directly without creating a dashboard.
---

# Financial dashboard

Read [Fina's shared workflow](references/fina-core.md) and [host capabilities](references/host.md). These cover Fina's voice, onboarding, authorized files/connectors, privacy and the host's actual artifact and scheduled-task tools.

Build an editable dashboard from the authenticated user's current Fina records. Let the host design it in the user's chosen style. Keep the financial meaning consistent across assistants; adapt rendering, persistence and scheduling to the host's actual capabilities.

## Language and connection first

Respond in the user's chosen language, including the first message, questions, errors and dashboard labels. Use an explicit language request first, then the conversation's language; if neither is available, use the saved Fina locale or the host's supplied user language. The English wording of this skill is not a response-language preference. Do not infer currency or timezone from language.

Fina's financial data comes only from its authenticated MCP connection. The host creates the artifact. A native desktop application with a similar name is not this connection and is not required for this workflow.

Before asking about style or claiming access, discover the connected Fina tools through the host's supported tool discovery when necessary. Call `get_setup_status` for a new dashboard or first use in this conversation. Reuse a successful current setup result already obtained in this conversation; installation, a login success screen and a style choice do not establish financial setup or tool availability.

If discovery or the authenticated read fails, explain the observed failure in the user's language and pause the data-dependent workflow. Distinguish unavailable tools, a returned authentication error and a service/network failure. A login may have succeeded even if discovery fails afterward: do not claim the user is logged out without evidence or repeatedly ask them to reconnect. Use the host's existing Fina connection controls for recovery when available. Do not open/control a native Fina app, scrape the website, request credentials in chat or use local tokens as a substitute. Preserve the user's requested style for when access works.

## Check saved setup before design

Use `get_setup_status` and its returned `conversation_guidance`, `onboarding.current_step`, missing fields and saved drafts to decide the next step before asking for style.

- For a new or unfinished financial setup, briefly explain that the dashboard will use the user's saved finances and help resume the missing setup first. Follow the existing Fina onboarding guidance rather than inventing a second questionnaire. Ask only for the current block's missing information; reuse saved answers and records, offer documents or manual entry, and respect explicitly skipped optional blocks.
- A dashboard request alone does not authorize creating accounts or changing financial records. Save only information the user supplies and asks to register through the established onboarding flow. Never mark setup complete, skipped or none merely to proceed to design.
- If the user explicitly chooses to postpone setup and use the records already available, create a partial dashboard only when those records support it, with material gaps visible. Do not silently skip onboarding or fabricate a dashboard from an empty account.
- For a configured account, continue directly without repeating onboarding. Once setup is resolved or explicitly deferred, reuse the requested style and existing dashboard. If style is missing, ask one short question with optional examples translated into the user's language. Accept any description; do not ask for charts, layouts or technical formats.
- Reuse saved locale, timezone and reporting currency. Honor an explicit period; otherwise use this calendar month to date for actual activity and a clearly separate upcoming horizon for projections.
- A dashboard request authorizes financial reads and creation of its private artifact. It does not authorize imports, publishing, sharing, transfers, purchases or unrelated integrations.

## Read the financial facts

Use the connected Fina tools and their live schemas. See [financial facts](references/financial-facts.md) for the specific tool mapping and accounting distinctions.

Start with `list_accounts(detail="summary")` and `get_financial_context(detail="summary")`, then retrieve the bounded spending, transactions, commitments and dated obligations needed for the requested dashboard. Use backend aggregates for period totals. Load account details or positions only where they add useful information.

Cover the user's available financial picture: cash accounts, spending and income, recent activity, subscriptions, card payments, other debts, assets and saved goals. A section's absence from returned data is not evidence of zero. Show material gaps near the affected figure in plain language. Do not manufacture a complete financial profile, live bank balances or a safe-to-spend number.

Do not expose account IDs, tokens, financial documents or the whole tool response as dashboard content. Use account aliases. Keep verified merchant/institution links supplied by Fina; do not guess brand URLs or download logos.

## Design and persist

- Use native private artifacts, files or visualization capabilities available in this host. Produce a real artifact, then return its actual location. If visual creation is unavailable, explain the limitation and provide the useful summary in chat without claiming a dashboard exists.
- Choose layout, typography, charts and interactions to fit the requested aesthetic. Maintain readable contrast, mobile usability, labels and reduced-motion support. Do not require one visual template or a particular third-party plugin.
- Lead with an understandable financial overview. Include a dated transaction view with category and account filters when the renderer supports it, a separate upcoming-payments/projection area, and relevant debts, assets and goals. Use progressive detail rather than loading the entire history into a page.
- Show the reporting period, currency basis and last successful data refresh. Distinguish data refresh time from the observation dates of balances, debts and asset values. Display estimates only where facts are estimated; avoid generic filler labels throughout the interface.
- Keep fetched financial data and the dashboard private. Do not deploy a public website, create a share link or upload financial data to another service without the user's explicit authorization for that destination. No browser-embedded credentials or direct unauthenticated calls to Fina.
- For updates, preserve the artifact's identity, chosen style and user edits. Update data independently of presentation when the host supports it. Never replace a custom dashboard merely because a standard template is easier.

## Make updates real

Read [refresh and scheduling](references/refresh-and-scheduling.md) when ongoing updates are requested or accepted.

When the user accepted a dashboard with recurring updates, completing the task includes using the host's actual Scheduled tasks or automation capability to create the schedule that reads Fina and edits the same artifact. A promise, saved note or reminder alone is not completion. Discover the scheduler, create the real task, keep its returned identity, and verify its saved configuration. If the host cannot do this, explicitly report that automatic updating is incomplete and why. Never silently replace the requested scheduled dashboard with a manual workflow or claim automatic updates without a successfully created schedule. Distinguish saved schedule, successful immediate refresh and successful unattended run.

A standalone dashboard request does not silently authorize recurring work. Offer daily updates briefly after creating it. If the user already accepted recurring updates in the conversation, reuse that authorization; do not ask again. Respect an explicit preference for manual updates.

## Finish

Deliver the dashboard link or file, a short explanation of any material missing coverage, and its actual refresh status. For an active schedule, state its cadence and timezone and where the user can manage it. Avoid repeating the full dashboard in chat. If an access restriction or failure blocked part of the work, preserve valid results, explain that specific restriction, and do not invent a successful result or promote a subscription upgrade.
