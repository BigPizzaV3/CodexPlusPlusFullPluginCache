---
name: social-neuron-account-setup
description: Check Social Neuron readiness, explain missing access, and help connect the social accounts needed for a requested workflow.
---

For installation or linking guidance, identify the current host or client from the provided context. If it is unknown, ask which host the user is using before giving host-specific steps. When the host is already known, proceed without asking again. Use verified instructions for that host. Uploading a ZIP prepares a package for submission; installation is a separate host-specific step, so do not describe ZIP upload as installing the plugin.

The host model and Social Neuron generation providers are separate. Use only model/capability information exposed by the current host or live tool schema; ask for a model choice only when it materially affects an available option. Do not infer the user's ChatGPT plan, model, context window or other installed connectors. The host's subscription does not pay Social Neuron credits or another service's bill. Existing Social Neuron access can work without those optional services. OAuth consent grants access, not a purchase mandate.

Use `get_account_status` first to establish the authenticated account's granted scopes, plan entitlements, credits, project context, and connection readiness. Installation alone does not prove OAuth or platform publishing is ready. Use the host's connection flow when authentication is missing; never ask for a password, API key, bearer token, or client secret in chat.

For a specific destination, use `list_connected_accounts` and retain the exact returned account ID and project ID. When several brands or accounts are available, ask the user to choose among the verified options before writes. Never invent an ID or select the first account silently. A read-only or paid-feature restriction should produce a clear explanation and the account's available next step, not repeated failing calls or an invented price.

Distinguish missing OAuth scope from account entitlement. For insufficient_scope or a scope-related 403, explain the needed permission and use the host's reconnect/consent flow when the user wants that access. An entitlement_required response or 402 means the account does not currently include the capability; explain the limitation and available account options neutrally. Reconnecting does not grant a paid entitlement, and an upgrade does not repair a missing OAuth grant. Do not repeatedly retry the blocked operation.

Preserve the user's brief and offer a feasible alternative, such as preparing a text draft, when a capability is unavailable. Explain existing entitlements neutrally and use already-owned credits. This public plugin must not promote or initiate digital-credit purchases, subscription upgrades or top-ups, or provide links that start those transactions. If a tool response suggests adding credits or upgrading, report the entitlement limit and available non-purchase alternatives without repeating that purchase direction.

When the user wants to connect a supported platform and the granted scope permits it, use `start_platform_connection`. Present its browser link for the user to open and complete consent. Do not open or replay that single-use link on their behalf. Call `wait_for_connection` after they complete the flow, respecting its timeout. Verify the resulting account with `list_connected_accounts`. A returned link, pending state, or timeout does not establish a successful connection. After a timeout, report the unresolved state and give the user a chance to finish before creating another link.

Separate ChatGPT-to-Social Neuron OAuth from the social platform's OAuth. A platform connection still needs the right account permissions and supported content format. Describe only the capabilities reported by the live account and tool schema. In particular, do not assume every listed platform supports every media format, analytics feature, or account type.

For brand-memory continuity, resolve the selected Social Neuron project and read get_brand_profile or get_brand_runtime when the workflow needs voice, audience or saved preferences. Identify the returned context used; if absent, ask for the missing brief instead of claiming saved memory exists. Another client can retrieve that context only after authorizing access to the same account and project. Each host keeps its own OAuth grant. Installation and conversation history are not shared brand memory, and access to one project never authorizes another.

End with a compact readiness result: selected project and destinations, missing access or connections, credit/budget constraints, and the next operation the user can complete. A setup check never schedules content or enables autopilot.
