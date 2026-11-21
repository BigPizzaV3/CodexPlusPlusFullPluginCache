---
name: ando-alert-channel
description: Set up or refine alerts and event feeds from connected apps in an Ando channel. Use when a user wants to route external events to a channel, adjust filters and delivery, or troubleshoot an existing feed.
---

# Set up an alert channel

Read [Ando basics](../../references/ando-basics.md) for identity, current-schema discovery, access, and write authorization. Discover only tools needed for this request.

Connect the intended provider events to an Ando channel and verify how people will read and act on them.

## Clarify intent before implementation

Resolve the desired provider/account/project, event types, destination and audience, filters or severity threshold, and whether the user wants delivery only or agent follow-up. Ask about unresolved intent before changing configuration; do not re-ask for information already supplied.

For follow-up, clarify whether the agent should react to each event, check periodically, or use judgment, and what actions it may take. Use [the looped-channel skill](../ando-looped-channel/SKILL.md) for that additional workflow. Do not automatically add autonomous investigation, task creation, or provider mutations to an alert-delivery request.

## Discover and connect

Inspect workspace identity, access, existing channels, feeds, and current tool schemas. Reuse the requested installation or route when possible. Discover connected apps through the current exposed schemas: compact catalogs use `list_connections`, `search_app_tools`, and `get_app_tool_schemas` (older compact servers use `list_app_tools`); legacy catalogs may expose `list_tools` and `get_tool_schemas`. Verify the actual account and provider namespace.

Distinguish provider access for agent investigation, inbound delivery into Ando, and any agent runtime that handles the delivered events. Verify each required piece independently. Do not infer that an OAuth connection creates an alert feed.

Prefer Ando's supported provider installation and native cards. For Sentry, read [the Sentry setup reference](references/sentry.md). For other providers, inspect their current Ando guide and supported ingress before proposing a custom webhook. Use an existing authorized API route only after inspecting its current schema. A generic custom adapter is additional implementation, not an assumed built-in capability.

When exposed, compact `get_setup_instructions` with mode `webhook` (or legacy `setup_webhook`) returns guidance for outbound Ando delivery. It does not set up an inbound provider feed. Setup instructions are agent-only and may require a managed runtime; inspect the current schema and eligibility. If an admin or provider consent step is required, prepare the configuration and provide the specific handoff. Keep credentials and signing secrets in supported secret-entry/storage surfaces.

## Choose the presentation

- Native rich card: default for a supported issue or alert. Preserve source identity, source link, current state, and meaningful fallback text. Inspect supported rendering and actions rather than inventing fields or buttons.
- Existing miniapp: use when users need a triage list, assignment input, or a structured decision. Discover its creation/action contract and update existing instances when appropriate.
- New miniapp: use when the requested interaction has no suitable existing surface. Follow [Ando's miniapp guide](https://docs.ando.so/docs/ando-mcp/publish-miniapps) and current tool schemas; use [Build a mini app](../ando-build-mini-app/SKILL.md). Publishing a release, installing it, granting provider access, and successfully using it are separate steps.

Use one primary action and the minimum context needed to act. Read-only page queries must not mutate a provider; provider writes need the supported confirmation contract and account grants. An “acknowledge” action must say whether it changes local triage state or provider state. A card or miniapp must not expose personal provider data to a broader audience. Avoid arbitrary HTML or executable scripts in native card payloads.

## Verify the route and lifecycle

Use a provider-supported test or an authorized representative event. Confirm delivery to the intended channel, rendering, source link, and any requested agent response. Where supported, verify that a later state change updates the existing object or thread and that a duplicate delivery does not create duplicate work. Label sample cards as previews; they do not prove live delivery.

Verify miniapp actions against persisted state and their actual target when included. Read back the route, filters, and destination. Report what is configured, what was tested, remaining setup, and where to disable the feed or follow-up. A connected account alone is not completion.
