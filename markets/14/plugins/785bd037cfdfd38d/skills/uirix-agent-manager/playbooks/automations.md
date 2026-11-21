# Always on: webhooks into Zapier, Make and your own systems

Topic `automations` · version 2026-10-25 · served by `uirix_guide({ "topic": "automations" })`.

The path that needs no model and no schedule: signed UiriX webhook events (a new outcome, a conversation ended or escalated, a summary ready, a call completed or failed) into Zapier, Make or the owner's endpoint. When to choose it over a routine; creating, testing and watching an endpoint.

```
GUIDE automations: always on, with webhooks

GOAL
What must happen the moment the agent records something (a lead into the CRM, an alert to the team, a row in a sheet) happens without anyone running anything: UiriX posts a signed event to an endpoint, and an automation hub or the owner's system does the rest.

FACTS THAT MISLEAD
- A scheduled task IS available to the owner: it is a feature of the owner's client (Claude scheduled tasks and Claude Code routines, ChatGPT scheduled tasks, Gemini scheduled actions), written as a prompt that calls the UiriX tools. The routines playbook writes it. Never answer that scheduled tasks are not available.
- A routine runs on a schedule in the owner's client and needs a model; a webhook fires within about a minute of the event and needs none. Real time or no model available: webhook. Judgement needed (which leads matter, what to write), or the owner asked for a scheduled task: routine.
- The events: outcome.created (a new lead, ticket, order, meeting, transfer, callback, payment promise, dispute, RSVP, with its contact and details), conversation.started, conversation.ended (with the transcript), conversation.escalated, summary.ready, call.completed, call.failed, call.no_answer. Test conversations fire none of them.
- NOT webhook events: call.received, message.left, call.started, errand.completed, lead.created are the chat app's own subscriptions; create_webhook refuses them. A call to the agent reaches a webhook as conversation.started / .ended and summary.ready; a lead as outcome.created.
- outcome.created leaves as soon as the tool call is on record: it carries the contact and the details, and the conversation summary only when it already exists. A receiver that needs the summary listens to summary.ready as well, or reads the conversation.
- Every delivery is signed with the endpoint's secret and carries a stable delivery id; retries and replays send the same bytes. The receiver must answer 2xx within 10 seconds and deduplicate on the delivery id.
- The secret never passes through the chat: create_webhook masks it and gives secret_location (the agent, Integrations, Webhooks), where the owner presses New secret and copies it; the old one signs 7 more days. A hub that verifies signatures (Zapier, Make) gets it pasted there; else the owner accepts unsigned processing knowingly.
- An endpoint receives the events of every agent of the account unless agent_ids limits it to some agents. When the owner talks about one agent ("this agent's leads"), create it with agent_ids of that agent, so the other agents' conversations do not go there. list_webhooks shows agent_ids and where each endpoint came from (created_via).
- An endpoint that fails 50 deliveries in a row is switched off by the platform (disabled_reason). list_webhooks shows it; update_webhook with enabled true switches it back on after the fix.
- The connector never deletes an endpoint; disable it with update_webhook. The owner deletes one in the dashboard: the agent, Integrations, Webhooks, where each agent's endpoints and delivery report are listed.

READ FIRST
- list_webhooks: what already exists, which events, enabled, failures.
- list_deliveries(status failed or endpoint_id) when something did not arrive.

ASK
1. What should happen, on which event, in which system.
2. Whether the owner has an automation hub (Zapier, Make) or an endpoint of their own, and the URL to post to (public https).
3. Which events, for which agent (one agent or every agent of the account), and whether test deliveries may be sent now.

APPLY: a new automation
1. Agree the event list from the facts above; outcome.created for "new lead into the CRM", conversation.escalated for "alert the team", call.completed and call.failed for "results of API calls".
2. create_webhook with the URL, the events and, for one agent, agent_ids (skip_ping true if the receiver already rejects unsigned requests). A receiver that checks signatures gets the secret from secret_location, never from the chat.
3. test_webhook: a signed ping. Ask the owner whether it arrived where the hub shows incoming requests.
4. For a hub: tell the owner which fields of the event to map (outcome: type, contact.name, contact.phone, contact.email, details, conversation_id, agent_name).
5. Create one real event with the owner's agreement (a marked test lead through the test flow is NOT delivered; a real conversation is), or wait for the next real one, then list_deliveries to confirm delivered.
6. Mark the hand-over policy: a hub that writes to the CRM makes mark_synced unnecessary for that destination; say so, so a later routine does not send the same leads again.

APPLY: something did not arrive
1. list_deliveries filtered by endpoint, agent and status: pending (retrying), failed (dead after the ladder), delivered.
2. Read the last error (status code, timeout). A 4xx is the receiver's; a timeout is the receiver taking over 10 seconds.
3. After the fix: replay_delivery for the missed ones (same bytes, fresh signature). An endpoint that was switched off: update_webhook enabled true.

APPLY: the choice, routine or webhook
Write it for the owner in two lines: webhook = instant, no model, fixed mapping, needs a hub or an endpoint; routine = scheduled, with judgement, in this client, needs the client's permissions. Many setups use both: the webhook for the raw event, the routine for the morning summary.

VERIFY
- test_webhook delivered, then a real event with status delivered in list_deliveries.
- The target system shows the record or message the event produced.

MONEY
Free: list_webhooks, create_webhook, update_webhook, test_webhook, list_deliveries, replay_delivery, list_outcomes, mark_synced, uirix_guide. The hub may charge per task.

MISTAKES TO PREVENT
- A plain http URL, a private host or a UiriX host as the endpoint: refused.
- Promising the summary in outcome.created: it is there only when the summary already exists.
- Asking for the secret in the chat: it is never shown here, only replaced in the dashboard (New secret).
- Leaving a disabled endpoint disabled after the receiver was fixed.
- Running a routine that duplicates what a webhook already writes.

STOP WHEN
The endpoint exists, a test ping and a real event were delivered, the owner knows where the secret is (the dashboard), the mapping and the retry rules, and knows which destinations the webhook now owns.
```
