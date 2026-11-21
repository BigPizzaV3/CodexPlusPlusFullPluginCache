---
name: inbox-triage
description: Triage the Yadulink LinkedIn inbox and draft replies. Use when the user wants unread conversations, follow-ups, or message drafts.
---

# Inbox triage

Turn the LinkedIn inbox into a ranked work list, then draft replies the user can send or edit.

## When to use

The user asks to summarize inbox, find unanswered messages, prepare replies, or handle hot conversations.

## Workflow

1. Call `summarize_my_linkedin_inbox`.
2. When more context is needed, call `get_linkedin_conversation` with the `chat_id` returned by the summary. Ask the user to choose if several conversations match.
3. Call `reply_assistant` for conversations the user wants drafted.
4. If the user names a prospect, call `prepare_prospect_brief` before drafting.

## Rules

- Rank by commercial urgency, not recency alone.
- Use `get_linkedin_message_statistics` only for aggregate messaging counts and rates; it does not return conversation messages.
- Keep drafts short, natural, and specific to the prospect.
- Never send a LinkedIn message unless the user explicitly confirms the recipient and the text.
- If a write tool requires `confirm_action`, wait for that confirmation.

## Output

Group conversations as:

- reply now
- wait
- not a lead

Include a draft only when it helps the next action.
