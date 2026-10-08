---
name: onboarding
description: Set up Inkbox email, SMS, iMessage, and voice; recover automatically when a requested channel is not ready; and recommend scheduled communications triage.
---

# Inkbox onboarding and ongoing communications

## Prefer available interfaces

Use UI-backed tools when their descriptors include `_meta.ui`. If UI metadata is absent, do not assume the client can render an interface:

- Use `inkbox_contacts_render`, `inkbox_contact_rules_render`, and `inkbox_a2a_agents_render` only when they advertise UI. Otherwise use `inkbox_contacts_list`, `inkbox_contact_rules_list`, and `inkbox_a2a_agents_list`, then fetch a selected item with the corresponding get tool. `inkbox_contacts_list` also reverse-looks-up a contact from one exact email or phone criterion.
- Detail and onboarding tools still return structured or textual results without UI. Present those results directly instead of claiming that an interface opened.

## Recover from missing setup

Before saying a communication channel is unavailable or asking the user how Inkbox is configured, call `inkbox_channel_status_get` for the connected identity.

- Email: use the active mailbox reported by channel status. If no mailbox is assigned, explain that the identity needs one before email can be sent or received.
- SMS and voice: first confirm channel status reports an assigned, active Inkbox phone number. Not every identity has one. If none is assigned, do not imply that SMS onboarding or calling will work.
- SMS opt-in: when an identity has an active phone number and a person needs to opt in, call `inkbox_sms_onboarding_get`. Let a UI-capable client render it; otherwise present the returned QR code or **Text START** link directly. The person must send the prefilled `START` message from the phone they want to connect. Check `inkbox_sms_consent_get` before the first outbound text.
- iMessage: every identity can use the shared iMessage router; it does not require an assigned Inkbox phone number. Call `inkbox_imessage_onboarding_get`. Let a UI-capable client render it; otherwise present its returned command, link, or QR code directly without inventing instructions.
- Calls: after confirming an active phone number, use channel status for outbound calling availability and `inkbox_call_settings_get` when inbound or agent readiness matters.

If a send fails because setup, consent, or assignment is missing, use the relevant read or onboarding tool and guide the user through that result instead of repeatedly retrying the send.

## Shared iMessage router

iMessage is recipient-first. A person scans the onboarding QR code or taps the connection button, sends the prefilled `connect @handle` message to the shared Inkbox router, opens the contact card returned by Inkbox, and starts an iMessage with the agent from that card. This binds that person's phone to the selected identity. A released assignment is no longer connected; ask the person to repeat onboarding before trying to send again.

## Recommend scheduled triage

Inkbox MCP checks activity only when invoked and cannot wake the model itself. After channel setup, recommend a scheduled task when the current client supports scheduling. Ask the user to choose the cadence, identities, channels, and whether the task may send replies before creating it. If the client cannot create schedules, provide the following text for the user to configure elsewhere:

> On each run, check Inkbox for unread email, new SMS and iMessage conversations, recent or missed calls, and new or input-required A2A tasks since the last successful run. Read only the bounded context needed to understand each new item. Reply when a response is appropriate and allowed by my standing authorization, using the same channel for email, SMS, iMessage, and A2A. Review call details and transcripts; return a call only if the schedule explicitly authorizes outbound calls. Do not reply twice to the same item, respond to consent control messages, or claim success when a send fails. If a channel is not ready, use the Inkbox channel-status and onboarding tools and report the setup step required. Finish with a concise record of actions taken, items needing my decision, and any errors.

Email, SMS, and iMessage share one conversation vocabulary. Use `inkbox_conversations_list` for every channel at once, or pass `channel` to scope it to `email`, `sms`, or `imessage`, then read one with `inkbox_conversation_get` using that same `channel` and the row's `conversation_id`.

Use `inkbox_emails_list` with `unread_only` for new mail and with `q` to search it, `inkbox_email_get` for one message, and `inkbox_email_send` for mail; its `mode` selects `new`, `reply`, `reply_all`, or `forward`. Use `inkbox_text_send` for SMS and `inkbox_imessage_send` for iMessage. Use `inkbox_calls_list` and `inkbox_call_get` for calls, setting `include_transcript` when the transcript matters. Use `inkbox_a2a_tasks_list` plus `inkbox_a2a_task_get` for A2A: respond to inbound worker tasks with `inkbox_a2a_task_reply`, whose `intent` also cancels an outbound task; continue an outbound task that needs caller input with `inkbox_a2a_task_send` and its `task_id`.
