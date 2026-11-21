# AI agent management and phone number routing

## List or inspect agents

Use `list_agents(search=?, client_id=?)` and `get_agent(agent_id=...)`. Only report parameters returned, including language, first message, prompts, voice and LLM. Agency filters require authorized `client_id`. A request to change LLM, voice, KB or integrations is outside the observed mutation toolset; do not claim completion.

## Create an AI agent (`create_agent`)

Gather the required values: `name`, a complete `prompt` setting duties, guardrails, escalation and user expectations, and the exact `first_message`. Optional `language` (`de`, `en`), description and inbound/outbound enabled flags. Defaults enable **both directions**, so ask whether outbound calling should really be on; choose a least-privilege flag when not requested. Preview all chosen fields and side effects, get final approval, then invoke the tool once. Confirm only the real returned ID/status. Explain that no inbound answering occurs until a number is connected.

Suggested draft sections for agent prompts: role, objectives, supported questions, data source, clarification strategy, personal information handling, transfer/escalation criteria, unsupported requests, end-of-call confirmation. Do not promise tools or workflows the actual agent doesn't have.

## Update a prompt (`update_agent_prompt`)

1. Resolve target agent via `list_agents` / user-supplied ID.
2. Fetch `get_agent` and preserve the complete current prompt.
3. Compose a **full replacement**, not a partial patch; display the intended change and warn that a replacement overwrites the previous text.
4. Ask explicit approval identifying the agent and final prompt. Execute once only after approval.
5. Report actual tool result; if failure, do not claim an update.

## Phone numbers

Use `list_phone_numbers` to inspect assignments. `connect_phone_number(phone_number_id,agent_id)` can move an already assigned number from another agent; it is not “add another number without side effects.” `disconnect_phone_number(phone_number_id,agent_id)` stops that agent answering its calls. Before either: show number, current owner, target owner (if applicable), service interruption risk, and request explicit approval. Don't use either tool to purchase a new number.

If a phone number is missing or the user lacks permission, do not invent a new number. Offer accurate next steps in Voico platform/support.
