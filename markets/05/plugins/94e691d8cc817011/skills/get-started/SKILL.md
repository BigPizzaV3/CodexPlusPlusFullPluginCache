---
name: get-started
description: How to hand work to the user's JackHamr agents and get results back. Use when the user mentions their JackHamr agents, wants an agent to do a task, or asks what their agents are waiting on.
---

# Working with JackHamr agents

JackHamr agents are AI workers, each with its own persistent cloud computer (files, repos, tools, running apps). Work happens in topics: conversations with one agent.

1. Call `list_agents` to find the right agent if the user did not name one.
2. Call `send_message` with the task. Show the user the `topic_url` so they can watch the agent work in JackHamr.
3. Agent work is asynchronous. Call `wait_for_reply` and repeat while the status is `working`.
4. If the status is `waiting_on_you`, the agent asked a question. Show the question and options to the user and call `answer_decision` with their choice. Do not answer for the user unless they told you to.
5. When the status is `done`, show the reply. Use `get_file` or `get_artifact` to bring back files and reports, and `list_previews` for links to apps the agent is running.

To see everything the user's agents need from them, call `get_pending_decisions`.
