---
name: agent-settings
description: Change an AssistLoop agent's settings. Use when the user wants to rename an agent, switch its AI model, rewrite its system prompt, or decide when chats go to people instead of the AI.
metadata:
  short-description: Rename, change model, prompt and handoff
---

Help the user change the settings of one AssistLoop agent.

1. Find the agent. If the user did not name one, call `list_agents` and ask which agent
   to use. Call `get_agent` to show its current name, model and handoff settings before
   changing anything.
2. Name or model: call `update_agent` with only what changes. For a model, call
   `list_ai_models` first and use the id of the model the user chose; do not guess it.
   Renaming and changing the model need an owner or admin of the organization.
3. Handoff: call `update_agent` with `human_intervention` true to let visitors ask for a
   person, or `only_human` true so the AI never answers and teammates reply to every
   message. Explain the effect before changing it.
4. System prompt: `update_agent_prompt` replaces the whole prompt, and no tool can read
   the current one. Before changing it:
   - For a change to part of the prompt, ask the user to paste their current prompt from
     the AssistLoop dashboard, and edit that text. Never rebuild the old prompt from
     memory or guess what it says.
   - Tell the user the old prompt will be overwritten and cannot be restored from here.
   - Show the full new prompt and send it only after the user confirms it.

Report the settings the tool returns. If a tool refuses (your role, a plan limit, a model
that is not offered), say what it said and stop.
