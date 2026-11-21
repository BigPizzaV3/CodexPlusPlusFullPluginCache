---
name: get-started
description: How to work in an Algomo workspace with the Algomo tools - read chatbots and conversations, stage configuration changes in an edit session, test them, and publish. Use when the user asks about their Algomo chatbots, customer conversations, knowledge base or workflows.
---

# Working in an Algomo workspace

Algomo is an AI customer-conversation platform. A workspace configures chatbots that talk to its website visitors through a messenger widget. The Algomo tools act on the workspace the user connected.

## Finding your way around

- `get_workspace` says which workspace and user the connection acts as.
- `get_product_overview` explains how chatbots, workflows, cards, knowledge base pages and the other parts fit together. `get_entity_type_info` describes one of them in detail.
- `list_chatbots`, `list_workflows`, `list_agents` and `list_knowledge_base_pages` show what the workspace has.

## Reading conversations

`list_conversations` lists customer and test conversations, with filters for chatbot, visitor, dates, and whether a person took over. `get_conversation_messages` reads one. Test conversations are marked as such and are never customer traffic.

## Changing configuration

Configuration changes are staged, reviewed, then published.

1. `create_session` opens an edit session and returns its `sessionId`.
2. The create, update and delete tools take that `sessionId`. Nothing is live yet.
3. `get_session_changes` shows what is staged and `validate_session` checks it.
4. `get_dashboard_link` with the `sessionId` gives a link where the user can see the staged changes in the dashboard.
5. `send_test_message` with the `sessionId` shows how a chatbot replies with the staged changes.
6. `publish_session` makes the changes live. It cannot be undone, so confirm with the user first. `discard_session` drops the staged changes instead.

Messenger settings and tasks are not staged: those tools take effect at once.

## Things that run for real

`send_test_message`, `run_workflow` and `run_agent` execute the chatbot's or workflow's own tools. A workflow that sends an email or calls an outside system does so, and runs use the workspace's credits. Say so before running one.

## Onboarding

Some workspaces have to finish onboarding before configuration can change. `get_setup_status` reports whether that applies and what the next step is.
