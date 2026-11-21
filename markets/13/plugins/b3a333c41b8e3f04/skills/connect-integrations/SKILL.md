---
name: connect-integrations
description: Connect a ChatbotGen chatbot to the business's own systems so it can do things for customers — check an order, start a return or refund, answer account questions, open a helpdesk ticket, use a remote MCP server — and send leads and events to a CRM, Zapier, Make or n8n.
---

## Select the chatbot first

Use the active chatbot from this conversation unless the user names another. For an existing chatbot without an active selection, call `list_chatbots`; match the name and website, or show the choices if ambiguous. Connect the account when prompted: integrations only exist on account chatbots, never on demos. If the user is on a demo, say that connecting their own systems comes after keeping the chatbot in an account. Once they are connected and agree, keep it with `claim_chatbot` and `confirmed: true`, then use the returned `chatbot_id`; never create a replacement. Until then, continue with what works now.

## Understand the need before proposing anything

Call `list_actions` to see what is already connected and `get_integration_guide` without a goal to see the options. Ask what customers should be able to do, in their words, one question at a time. Map each need to one goal: `order_status`, `returns_refunds`, `account_lookup`, `helpdesk_ticket`, `connect_mcp_server`, `webhooks`, `automation_platform`, `identity`, `custom_api`. Then call `get_integration_guide` with that goal and follow it.

Explain the three mechanisms in plain words only as needed:

- **Custom action**: the chatbot calls the business's own HTTPS API during the chat (look up, create, update).
- **MCP server**: the chatbot uses the tools of a remote MCP server the business already has.
- **Webhooks**: ChatbotGen sends events (new lead, handoff, booking, conversation) to another system; nothing comes back into the chat.

For Zapier there is a ChatbotGen Zapier app in Zapier's app directory: follow the `automation_platform` guide, which has the directory link and points the owner to the Integrations → Zapier page for the API key. Make and n8n use webhooks. If the business uses a platform without its own API access, say what is missing instead of inventing a workaround.

## Never invent the integration

Ask for the real endpoint URL, method, inputs and the response fields that matter, or ask who their developer is and give them the guide's steps. Never make up URLs, field names, policies or credentials. The guide's `suggested_action` is a template to adapt, not a working configuration.

Credentials and secrets are never handled in chat. Tell the owner to enter API keys and auth headers on the chatbot's Actions page (`actions_dashboard_url`), and to copy the identity and signing secrets from there to their server. If the owner pastes a secret into the chat anyway, do not repeat it, do not put it in an action, and suggest rotating it.

## Safety settings are part of the design

- Anything that reads one customer's private data (orders, account, bookings) needs `requires_verified_user`. On the website that means identity verification (goal `identity`): the site's server signs a short-lived token for the signed-in customer. WhatsApp and Telegram customers are identified by their account automatically. For guests, the endpoint must check two facts together (for example order number and email).
- Anything that changes something (refund, return, cancellation, address change, ticket that emails the customer) also needs `requires_confirmation`: ChatbotGen only runs it after the customer confirms in a later message, whatever the model decides.
- The business's API must verify the request signature and trust the identity token, not an id typed by the customer. Point the developer to the guide's `docs_url`.

## Save, test, verify

Before `save_action` or `connect_mcp_server`, show the complete draft: name, description, method and URL, inputs, header names (not values), verified-customers-only and confirmation settings. Call it with `confirmed: true` only after the owner's explicit yes in this conversation.

After saving, run `test_action` with realistic sample inputs, and a `sample_user` when the action needs a verified customer. A test sends a real request: before testing an action that changes data, say so and use a test record. Report the HTTP status and the relevant part of the response, and explain failures in plain words (wrong URL, missing auth header, signature rejected, missing input). Then use `test_chatbot` with a realistic customer question; answer tests never execute actions, so they show the conversation, not the API call.

For MCP servers, review the returned tools with the owner and turn off any tool customers should not reach (admin, delete, bulk changes) with `connect_mcp_server` and `enabled_tools`.

When something fails later, read `recent_runs` in `list_actions`, explain the error, propose a fix and apply it only after confirmation.

## Finish with a short checklist

End with what is done, what the owner or their developer still has to do (paste credentials, deploy the identity snippet, verify signatures), and how to check it worked (the Actions page run log). Do not promote plans; if a write is refused because of the plan, state it once and continue with guidance.
