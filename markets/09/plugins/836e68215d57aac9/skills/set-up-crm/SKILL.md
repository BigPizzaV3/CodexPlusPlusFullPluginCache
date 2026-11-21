---
name: set-up-crm
description: Use when an admin wants to organise contacts and chats in Ciarem with funnel stages, custom contact fields, Inbox labels or quick replies.
---

# Set up the CRM

Admins only: if a tool answers `requires_admin`, tell the user only workspace admins can change these settings.

1. Call `get_crm_setup` for the funnel stages and contact fields that exist.
2. **Funnel stages.** `save_funnel_stage`: a new stage needs a `name`, a `description` of what a contact in it has actually done (the AI reads it to decide a move) and a `key`. Ask whether the AI may move contacts there on its own (`ai_agent_kinds`) or only people do (`[]`). Before `delete_funnel_stage`, say how many contacts are in the stage (`contact_count`) and wait for a yes: it can't be undone. Stages are reordered on the Contacts page.
3. **Contact fields.** `add_contact_fields`, up to 15 per call. Say which kind you chose for each and wait for a yes, because kind and key can't change later: DROPDOWN for one choice, MULTI_SELECT for several, TEXT for anything people type, including codes and phone numbers.
4. **Inbox labels.** `create_conversation_tag`, with a `description` of when the label applies, which the AI labeler also reads.
5. **Quick replies.** `add_quick_reply` with the message in the business's own words; it can use `{{contact.first_name}}` and `{{agent.first_name}}`. Share it with everyone unless the user says otherwise.
6. Say what was created. If a tool refuses, give its reason instead of retrying with other values.

Nothing here edits or deletes a contact.
