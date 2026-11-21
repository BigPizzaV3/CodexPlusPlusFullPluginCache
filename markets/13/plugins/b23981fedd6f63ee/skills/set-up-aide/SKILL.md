---
name: set-up-aide
description: Set up Aide until its AI agent answers the user's customers. Use when the user asks to set up, configure, test or launch Aide, or when get_setup_status shows the workspace is not live.
---

Use the Aide tools to take the workspace to live, one step at a time. The user's explicit instructions take priority over these steps.

1. Call get_setup_status. It gives the `nextStep` and, for each step, the `tool` that does it. Do the steps in order and call get_setup_status again after each one.
2. Company details: ask the questions the step's `detail` lists, in one message, and save the answers with update_workspace.
3. Knowledge: add the company's website with add_website. It imports in the background, so carry on and check it later with get_knowledge_source. Write what the user tells you that the site doesn't say with add_knowledge_article.
4. Agent: read it with get_agent and change it with update_agent when the user asks. Try it with test_agent and continue_agent_test, and show the user the answers.
5. Channel: for website chat, give the user the snippet from get_chat_widget_install to paste on their site. For a support address, call add_support_email, tell the user the address to forward it to, then call send_forwarding_test. For Gmail, Shopify, Zendesk, Front or Gorgias, give the user the link from connect_integration to finish in their browser; once a helpdesk is connected, call set_up_helpdesk.
6. Going live: deploy_agent and set_inbox_ai make Aide answer real customers. Call them only after the user confirms. pause_agent stops the agent.

Do not call start_trial. If a step needs a feature the workspace's plan doesn't include, say which feature, and that the plan is changed in the Aide dashboard. If a tool returns an error, tell the user what it said instead of guessing.
