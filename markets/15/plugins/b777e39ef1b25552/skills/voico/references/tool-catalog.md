# Voico MCP tool catalog — discovered October 2026

**Source of operation names:** Voico MCP tools available in the current ChatGPT integration during packaging. This is a descriptive inventory, not a hardcoded local tool declaration. Actual tool availability, authorization, argument validation and response schemas are controlled by the remote server. Tool results are dynamic dictionaries, so validate returned keys instead of assuming a fixed JSON shape.

| Tool | Arguments / behavior | Classification / cautions |
| --- | --- | --- |
| `list_agents` | Optional `search`, `client_id`. List names, IDs, direction settings. | Read; client filter only when authorized. |
| `get_agent` | Required `agent_id`. Get prompt, first line, language, LLM, voice, settings. | Read; confidential agent prompt. |
| `create_agent` | Required `name`, `prompt`, `first_message`; optional `language`, `description`, `inbound_call_enabled`, `outbound_call_enabled` (both default true). | **Write**, creates billable-capable configuration; confirm; new agent not live without number. |
| `update_agent_prompt` | Required `agent_id`, full replacement `prompt`. | **Write**, overwrites previous prompt; back it up by reading first, show diff, confirm. |
| `get_call_stats` | Required ISO 8601 `start_date`, `end_date`; optional `agent_id`, IANA `timezone` (default Europe/Berlin), `include_series` (default false). | Read; comparison with previous equally long period; include series for per-day breakdown. |
| `get_monthly_costs` | Optional IANA `timezone` (default Europe/Berlin). | Read; this month's call costs, number costs and total. |
| `get_credits` | No arguments. | Read; current credit balance in EUR. |
| `make_call` | Required `agent_id`, E.164 `to_number`; optional `first_message`, `prompt`, `variables` object of string to string, `scheduled_time` ISO 8601, `phone_number_id`. | **External write + financial effect**; real call now or scheduled. Strict affirmative consent; no unsolicited calls. |
| `list_calls` | Optional `agent_id`, `client_id`, `status` (`scheduled`, `in-progress`, `done`, `failed`), `direction` (`inbound`, `outbound`), `created_after`, `created_before`, `search`, `page` (>=1), `page_size` (1–50). | Read; paginated, newest first, outcomes and summaries. Only `search` agent names/phone numbers; do not assert full-text transcript search. |
| `get_call` | Required `call_id`. Get metadata, outcome, duration, numbers, summary, extracted fields. | Read; can expose personal information. |
| `get_transcript` | Required `call_id` for finished/transcribed call. | Read; fails if call in progress or not transcribed. Agent turns without text may indicate tool execution. |
| `list_clients` | No arguments. Partner agency end customers with `client_id`. | Read; may fail for non-agency accounts. |
| `list_phone_numbers` | Optional `agent_id`. List owned numbers and their assignments. | Read; don't leak unrelated phone numbers. |
| `connect_phone_number` | Required `phone_number_id`, `agent_id`; reassigns existing connected number. | **Operational write**; may remove it from prior agent and change live traffic. |
| `disconnect_phone_number` | Required `phone_number_id`, `agent_id`. Disconnects number. | **Operational write**; calls to the number won't be answered by that agent. |

## Not supported by these discovered tools

Do not pretend that the tools can buy numbers, delete calls/transcripts, retrieve raw audio files, set billing plans, issue refunds, configure third-party CRMs, modify arbitrary agent settings besides prompt, or run bulk marketing campaigns. These could exist elsewhere in Voico, but **are not part of this observed MCP toolset**.

## MCP review annotations to verify in server implementation

- Reads: `readOnlyHint=true`, `destructiveHint=false`, `openWorldHint` based on actual external reach.
- `create_agent`, `update_agent_prompt`, `connect_phone_number`, `disconnect_phone_number`: `readOnlyHint=false`; destructive flag must reflect semantics of overwritten prompts / live route moves. Avoid falsely labelling changes as read only.
- `make_call`: `readOnlyHint=false`, `openWorldHint=true` for calls to external phone network, and an accurate destructive flag reflecting financial/operational effects.

These are a **verification checklist**, not claims that annotations were inspected or updated on the server. A package cannot set server-owned tool annotations.
