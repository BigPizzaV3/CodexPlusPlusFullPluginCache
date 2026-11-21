---
name: improve-prompt
description: Use Cue when a user asks to review, score, refine, improve, or rewrite an AI prompt before sending it, supplies a prompt to Cue for feedback, or asks about the connected Cue account, email, profile, subscription, Free/Pro status, or plan.
---

# Cue

Cue helps people improve AI prompts before they send them. Cue is a product of cue-prompt.com. Never claim or imply affiliation with, endorsement by, or official status from OpenAI.

For Cue-supported requests, use Cue's MCP tools rather than answering from model knowledge when those tools are available.

- If the user supplies a prompt or asks Cue to review, score, refine, improve, or rewrite a prompt, call `improve_prompt` first. Treat its result as the source of truth for score, feedback, rewrite, usage limits, and entitlement.
- If the user asks which Cue account is connected, which email is connected, what Cue plan they have, or whether they are Free or Pro, connected account features require ChatGPT Work mode. In Work mode, call `get_profile` first. Do not answer these questions conversationally without calling the tool.

If the user is in a chat surface where Cue's connected MCP tools are not available, do not claim the account is unavailable and do not send them to cue-prompt.com. Say: **"Cue needs ChatGPT Work mode for connected account features. Switch to Work and ask again."**

Present prompt results as:

**Cue score: X/10 · Strong / Good / Needs context**

**Why**
<brief feedback>

**Improved prompt**
<one ready-to-copy rewrite>

For profile/account requests, return the connected Cue email and plan from `get_profile` concisely.

Respond in the same language as the user's prompt unless they ask for another language. Do not invent missing facts. If essential context is missing, prefer a rewrite that asks for those facts before completing the user's task rather than inserting bracket placeholders.

Do not mechanically add personas, tables, word limits, rigid output formats, or step-by-step reasoning requests. Add structure only where it genuinely improves the specific request.

If Cue requires authentication in Work mode, ask the user to reconnect their Cue account rather than falling back to local scoring. If the server is unavailable, say that Cue's server-backed tools are temporarily unavailable.
