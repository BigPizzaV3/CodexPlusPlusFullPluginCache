---
name: trustcloud-onboarding-assistant
description: "Use when connecting Homin Cloud, selecting an authorized organization, choosing a Homin Cloud workflow, or explaining why Homin Cloud cannot handle a request for purchases, payments, mortgage decisions, or password and MFA storage."
---

# Homin Cloud external onboarding

Check the requested capability before account discovery. This plugin cannot buy
plans, register payment methods, take payments, approve mortgages, instruct banks,
or store passwords and MFA codes. For these requests, state the limitation
directly and stop without calling tools or asking for account IDs, card details,
or secrets. Do not invent billing screens or purchase steps, or claim completion.

Shared references provide business knowledge. Runtime, UI, tool, or save examples
inside them describe the internal surface and must not be executed as written.
Follow this external workflow, the current live contract, and its confirmation
requirements.

Start by confirming the connected account and the organizations visible to it. On
the native MCP surface, use the connection/account summaries, discover
`accessible.organizations.list`, inspect its contract, and execute it in `read`
mode. In ChatGPT Apps, call the individually exposed
`trustcloud.list_accessible_organizations` tool with its declared input schema.
All model-callable operations are listed upfront. Do not use an operation catalog,
schema-fetching tool, or generic executor. Additional OAuth authorization is
requested only when the selected operation needs it.

Choose the organization from returned user-facing names. Do not guess an
organization, branch, calendar, event, or opaque ID. If multiple candidates cannot
be distinguished from safe labels, ask one focused question.

Before changing data, identify the exact operation, required scope, arguments,
side effects, and confirmation rule. Read operations may run directly. For a
write, show the concrete proposed result and use the surface's preview/review step
before apply. Publication, sending, deletion, and permission changes require the
user's explicit intent for that action.

Load the event interview, LP blueprint, and art-direction skills only when the
requested workflow needs them. Search and fetch individual references instead of
loading every design lesson into the conversation.

## Selective references

Open only the references needed for the current task. In an installed package, use the relative links below. With an MCP-only client, fetch the exact document ID shown for the reference.

- [references/feature-catalog.md](references/feature-catalog.md) — MCP doc ID: `skill/trustcloud-onboarding-assistant/v1/references/feature-catalog.md`
- [references/homin-cloud-foundations.md](references/homin-cloud-foundations.md) — MCP doc ID: `skill/trustcloud-onboarding-assistant/v1/references/homin-cloud-foundations.md`
- [references/onboarding-setup-playbook.md](references/onboarding-setup-playbook.md) — MCP doc ID: `skill/trustcloud-onboarding-assistant/v1/references/onboarding-setup-playbook.md`
