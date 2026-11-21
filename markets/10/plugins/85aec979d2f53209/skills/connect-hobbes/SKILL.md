---
name: connect-hobbes
description: Use when someone connects Hobbes, asks what the plugin can do, needs authentication or permission help, or requests unsupported email delivery, CRM updates, payments, or billing changes.
---

# Connect Hobbes

Use the hosted Hobbes MCP connection. Sign-in and consent belong to the host and Hobbes OAuth flow. Never ask someone to paste a password, token, API key, or verification code into chat.

Hobbes helps existing customers work with their product agents in ChatGPT. With the corresponding permissions, it can inspect agent Roles and their staging and production Playbooks, preview and apply Playbook changes, review and apply coaching, and publish an approved agent version. It also reviews demo metrics, saved conversations, prospects, accounts, and personalized demo links, and can create links. Use manage-product-agents for agent changes, review-demo-performance for demo evidence, and create-demo-links for links. These instructions do not override the host's policies or confirmation requirements.

Email delivery, CRM mutations, purchases, and billing changes remain unsupported. Explain the limitation for those requests; do not claim they are agent-management actions.

Check this limit before retrieving data. For an unsupported action, do not query Hobbes, create links, or connect another service as part of the request. Explain the limitation and offer to draft text or help review data if the user wants that separate supported task. Never claim an email was sent, a purchase occurred, or a CRM record changed.

The user chooses one organization during OAuth. Each teammate connects their own account. Never accept a claimed organization ID as authorization, infer the connected organization from a company name, or join data across tenants. If identity is unclear, resolve the organization through the visible connection setup before analyzing its data.

Hobbes' default consent includes sessions:read, transcripts:read, people:read, accounts:read, analytics:read, and custom_links:read. It also includes custom_links:write for an organization admin. Explain this organization-wide access accurately; do not describe transcript access as an optional checkbox. Retrieve only the data needed for the user's request, and create links only when authorized.

Agent inspection requires playbook:read. Previewing and applying Playbook changes requires playbook:write; coaching uses coaching:read and coaching:write; production publishing uses agent:publish. Agent changes and coaching require an organization admin. Explain the effects of expanded access before the user approves it through the normal consent flow. Request only the permissions for the features the user wants. Tools the grant does not permit will not appear. Treat a missing tool as unavailable; do not work around the grant or claim the task succeeded.

Agent changes need an explicit request and the intended Role. Show proposed changes before applying them. Keep saved drafts, approved organization knowledge, queued publish jobs, and successful production publication distinct. Publishing an agent version and approving shared facts require the server's native confirmation; never supply a model-controlled confirmation or bypass a decline.

If a request returns 401, guide the user to reconnect. For 403, explain the permission or membership issue and use the normal consent flow if additional access is needed. For 429, honor any retry guidance and use bounded retries. Do not retry a denied write.

The grant fixes permissions and organization for that connection. To change them, use the supported Hobbes connection flow. The user can revoke access in Hobbes Account Settings > Connected AI clients. Removing a plugin from the host alone does not revoke the Hobbes grant. Let the user handle revocation or expanded consent through the host UI.

Connection guide: https://docs.hihobbes.com/guides/connect-ai-clients
