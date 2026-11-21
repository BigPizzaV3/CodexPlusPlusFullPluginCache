---
name: get-started
description: Use ChatAgentix as the user's executive assistant, sales and marketing team - catch up on calls and messages, text, email, call, manage the calendar, add contacts, schedule follow-ups, report on the business, update agent knowledge, answer social conversations, publish posts and manage deals, appointments, email drafts and outreach campaigns after the user approves a draft.
---

# Working with the ChatAgentix assistant

ChatAgentix gives the user AI employees. The executive assistant has its own
phone number, answers the user's calls, screens callers, takes messages and keeps
the calendar. Sales and marketing agents follow up with leads, work the deals
board, post on social media and run outreach campaigns. These tools let you check on it
and have it act for the user. They only reach the signed-in user's own account.

## Catching up

- "What did I miss?" or "What did my assistant do?" → `get_activity_summary`.
  Mention unread messages and items waiting for the user first, then the latest
  call summaries, then anything sent or placed from ChatGPT.
- "Read my messages" → `list_messages`. Give who left each message, how to reach
  them and what it's about. Use `mark_message_read` only when the user asks to
  clear or mark a message.
- For more call detail → `list_recent_calls`.
- To answer someone, pass the `contact_id` shown on their message to
  `prepare_text_message`. ChatAgentix picks the channel they last wrote on
  (social conversation or text) and the result says which; show it to the user.
- "Did they reply to my text?" → `get_text_conversation` with the contact's
  `contact_id`. `list_messages` also returns recent `text_replies`. Replies are not
  pushed into the chat; check when the user asks.

## Acting for the user

Nothing leaves the user's account until the user approves a draft.

- **Texts and emails are two steps:**
  1. Find the person with `search_contacts` to get a `contact_id` (for an email to
     someone who isn't a contact, use `email_address`). Then call
     `prepare_text_message` or `prepare_email`. Nothing is sent.
  2. Show the user the recipient and the exact content from the draft and ask
     them to approve it. Call `send_prepared_message` with the `draft_id` only
     after they say yes. To change the wording, prepare a new draft.
  One recipient per draft. If the user asks to message many people at once or to
  skip the approval, prepare the drafts and still ask before sending.
- **Calendar:** use `list_calendar_events` to check the schedule and
  `create_calendar_event` with ISO-8601 times that include the user's timezone
  offset. If the result reports a conflict, tell the user what overlaps and retry
  with `allow_overlap=true` only if they say so.
- **Moving or cancelling an event is two steps:**
  1. Get the `event_id` from `list_calendar_events`, then call
     `prepare_calendar_change` with `action` `move` (and `new_start_time`) or
     `cancel`. Nothing changes yet.
  2. Show the user the event, the change and the attendees who will be notified,
     and ask them to approve it. Call `apply_calendar_change` with the
     `draft_id` only after they say yes.
- **Phone calls are two steps:**
  1. `prepare_phone_call` with who to call and a clear goal that includes the
     details the assistant needs (date, time, party size, names). Nothing is
     dialed.
  2. Show the user the name, number and goal from the draft and ask them to
     confirm. Call `place_phone_call` with the `draft_id` only after they say yes.
     If they correct the number, pass it as `phone_number`.
  The call keeps going if the chat closes. Use `get_phone_call_result` when the
  user asks how it went, and `cancel_phone_call` to cancel a draft or stop a call
  in progress.

Sending the same draft or placing the same call draft twice never sends or dials
again; the tool returns the earlier result.

## Running a business account

These tools work for business accounts. If a tool answers that a feature isn't
available or isn't turned on for the account, tell the user that, give them the
link from the result, and don't try another tool to work around it.

- **Social inbox:** `list_social_conversations` (direct messages and public
  comments), then `get_social_conversation` to read one. To answer, call
  `prepare_social_reply`. If `can_reply` is false, tell the user why
  (`reply_note`) instead of drafting.
- **Social posts:** `list_social_posts` shows connected accounts and recent
  posts. `prepare_social_post` drafts a text post for the accounts the user
  picks (or every account that accepts a text post), now or at `publish_at`.
  Posts with images are made in ChatAgentix.
- **Contacts:** `prepare_contact_change` adds up to 10 leads or customers
  (`contacts`), or edits one (`contact_id` plus the fields to change,
  `add_tags`, `remove_tags`, `note`). A new entry that matches an existing
  contact's phone or email updates that contact; the draft says so. Merging and
  deleting contacts is done in ChatAgentix.
- **Follow-ups:** `list_follow_ups` shows open and overdue follow-ups.
  `prepare_follow_up_change` with `action` `create`, `reschedule`, `cancel` or
  `complete`. A new follow-up is carried out by the agent itself at `due_time`:
  `type` `message` sends a text or email, `call` phones the contact. Always tell
  the user that before they approve.
- **Business report:** `get_business_report` for "how are we doing", pipeline,
  conversion and per-agent questions. Report only the numbers it returns.
- **Online store sales:** `get_store_report` reads the connected Shopify or
  WooCommerce store live: orders, gross and net sales, refunds, sales per day,
  best sellers, stock running out and recent orders. Read-only. If a store shows
  `available: false`, tell the user the `reason` it gives.
- **Agent knowledge:** `list_knowledge` lists what agents answer customers from
  (`article_id` reads one in full). `prepare_knowledge_change` adds or rewrites
  an article; agents use it with customers right away, so use only facts the
  user gave and show the full text.
- **Customers and deals:** `get_contact` for a contact's details, tags, notes,
  history, open appointments and open follow-ups. `list_deals` for the board, its stages and deals.
  `prepare_deal_change` with `action` `create` or `move`.
- **Appointments:** `list_appointments`, then `prepare_appointment_change` with
  `outcome` `confirmed`, `completed`, `no_show` or `cancelled`.
- **Email drafts:** `list_email_drafts` shows emails the user's agents wrote and
  are holding for approval. `prepare_email_draft_decision` with `decision`
  `send` or `discard`. Wording changes are made in ChatAgentix.
- **Outreach campaigns:** `list_prospecting_campaigns` and
  `get_prospecting_campaign` for results and leads. `prepare_campaign_stop`
  stops one; a stopped campaign can't be resumed. Campaigns are created and
  started in ChatAgentix.

**Every business change is two steps.** The prepare tool saves a draft and
changes nothing. Show the user exactly what the draft says, including its
`note` or `effect` (a public reply, an agent that keeps answering, automatic
follow-ups a deal stage starts, a follow-up the agent sends by itself, a calendar event that is removed), and call
`apply_prepared_action` with the `draft_id` only after they say yes. Running the
same draft twice never does it again.

## Several agents

Business owners may have more than one agent. If a tool returns
`agent_selection_required`, ask which agent to use (`list_agents` gives names) and
call again with `agent_id`.

## Not available here

- No payments, money transfers, purchases or account changes, and no access to
  anyone else's account. Say these aren't available in ChatGPT.
- If a result has `test_mode: true`, it came from the review sandbox: tell the user
  nothing was actually sent or dialed.
- If Google Calendar isn't connected, tell the user to connect it in ChatAgentix
  settings.
