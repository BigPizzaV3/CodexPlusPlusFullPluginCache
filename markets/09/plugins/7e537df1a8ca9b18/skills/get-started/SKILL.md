---
name: get-started
description: Welcome a new InsertChat user in ChatGPT, confirm the connected workspace, set their preferences, and open InsertChat when the user chooses Set up or asks for onboarding.
---

# Get started with InsertChat

Use this skill right after the user installs the InsertChat plugin or chooses Set up.

1. Call `list_agents` to confirm the connection and see the user's assistants. Never guess assistant IDs.
2. Briefly explain that InsertChat runs their AI receptionist and website assistant. Here they can review the front desk, prepare replies, look up leads, and check knowledge training. In supported hosts the workspace also opens beside ChatGPT, with navigation and reply-box drafts; otherwise use the server tools and return drafts in chat.
3. Call `settings_read` with `{}`. Ask one question at a time, using anything the user already said:
   - "Which page should InsertChat open on?" (Home, Inbox, Contacts, Knowledge, or Reports).
   - If they have more than one assistant: "Which assistant should I use by default for the inbox?"
     Let them skip. Call `settings_update` with only the values they changed, and confirm from the returned values; never claim a save that failed.
4. Open InsertChat:
   - No assistants: call `open_insertchat` with path `/setup` so they can create one.
   - Otherwise call `open_insertchat` with `{}` to open their start page.
5. Offer one next step and wait for their choice:
   - "Show me what needs me in the inbox" → `get_front_desk_brief`. Use `filter_inbox` as well only when that view tool is available.
   - "How did my front desk do this month?" → `get_report_summary`.
   - "Check what my assistant's setup is missing" → `get_setup_status`.

If they installed the plugin during an existing task, continue that task in the same conversation after step 4.

For `add_source_url`, use the exact URL the user requested; ask only if it is missing or ambiguous. Omit `agent_uid` to let the user pick the assistant. Explain that it imports only that page and uses one credit and one source slot.

Never send messages for the user: `draft_reply` only fills the reply box. Send the user to InsertChat (`open_insertchat` or `open_agent_settings`) for deleting assistants, changing credentials, billing, or publishing.
