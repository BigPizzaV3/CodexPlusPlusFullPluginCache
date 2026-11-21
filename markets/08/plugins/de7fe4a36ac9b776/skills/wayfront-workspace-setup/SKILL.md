---
name: wayfront-workspace-setup
description: Guide a Wayfront workspace owner from an empty or prebuilt workspace to a tested client ordering workflow. Use for new-workspace onboarding, launch readiness, or reviewing an incomplete setup across services, forms, branding, team access, payments, and delivery.
---

# Wayfront Workspace Setup

Help the owner reach one real outcome: a client can buy or be invoiced for the primary service, provide the right information, and create delivery work the team understands. Do not optimize for checking every feature box.

## Review before building

Call `workspace-info` first so the selected workspace, staff role, and role-level capabilities are explicit. If a necessary setup action is unavailable, explain the permission or manual handoff before designing around it.

Inspect current settings, services, and forms before asking what to build. Identify the primary or relevant services first, then inspect task templates only for those services; do not fetch every service checklist by default. Inspect team roles, pipelines, and integrations only when they matter to the intended workflow. If services or forms already exist, review and refine them rather than recreating or duplicating them.

Use the `*-read` tools for inspection and their `*-write` counterparts for approved changes, such as `settings-read` / `settings-write`. Team lookup remains `team-tool`; staff invitations and role changes remain `team-management-tool`.

Ask only for decisions the existing data cannot answer:

- what the business sells, its price, and whether delivery is one-time, recurring, or request-based;
- whether clients buy directly, request a quote, or receive a manual invoice;
- what information belongs at checkout, with each project, or once per client relationship;
- who owns each delivery step;
- whether sales or production stages, notifications, or automations solve a current need.

If the workspace is empty, start with one question about what they sell. If it is prebuilt, summarize the primary existing service instead of interviewing them from scratch.

Present the proposed primary package in plain language, not as a field dump:

- what is sold, for how much, and whether each renewal reopens work, creates new work, grants requests, or bills only;
- what the client provides at checkout;
- what is requested for each project through intake;
- what is requested once per client through onboarding;
- the delivery checklist and who owns it.

Ask: "Does this setup make sense, or would you like to make changes?" Do not create or update services, forms, or task templates until the user approves that package or gives the requested edits.

## Build the approved workflow

1. Configure the approved service behavior. Use `$wayfront-service-setup` for pricing, recurrence, renewal delivery, forms, and task-template consequences.
2. Configure the approved checkout, intake, and onboarding flow. Use `$wayfront-form-setup` for form choice and safe field updates.
3. Set business name, timezone, currency, contact link, brand colors, and public logo URLs.
4. Review staff roles and invite only the people needed for the workflow. Invitations can send email.
5. Add pipelines, automations, Slack notifications, or webhooks only when the user described a need for them.

Keep setup conversational: ask one or two decisions at a time and use the user's words for service names. If several services exist, settle the primary one first, then apply the agreed pattern to the rest only with permission.

## Finish with a real test

MCP can configure workspace branding, business information, services, forms, roles, pipelines, automations, Slack notification choices, and webhooks. It cannot connect Stripe, configure a custom domain or custom sending email domain, connect Slack, or switch the workspace to live mode.

Invoice data is read-only through MCP. If the approved sales path uses manual invoices, hand off invoice creation and sending to the Wayfront interface.

After the catalog and forms are approved, guide the owner through the remaining manual sequence: connect the payment processor, confirm branding, configure domain/email if needed, place a test order in test mode, inspect the resulting client/order/intake experience, and only then switch to live mode. Do not call the workspace launch-ready until that test has happened.

Use `search-wayfront-docs` when current product guidance or a matching interface walkthrough would help. Retrieve the selected result with `get-wayfront-doc`, base the recommendation on that current source, and share its canonical URL with the user.
