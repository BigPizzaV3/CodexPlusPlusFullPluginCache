# Outbound calling, scheduling and telephony safeguards

`make_call` places a **real** phone call immediately when `scheduled_time` is omitted, or schedules it for an explicit ISO 8601 time when supplied. It may consume account credits and contact a third party. Only send the request after the user approves all key details.

## Required before execution

- Identify the exact existing agent via `list_agents`, confirm outbound calling enabled and an assigned number with `list_phone_numbers`.
- Check available credit with `get_credits` where possible; a credit check does not guarantee a price or successful call.
- Confirm recipient number in E.164 format, country code included, and the user's authority/consent to contact that number. Do not infer numbers from call history, repurpose caller data, or use purchased/scraped lists.
- Clarify purpose and any one-time custom first message / prompt / variables, and ensure these don't misrepresent identity or the fact a voice AI is calling.
- Clarify **now vs scheduled**; for scheduling, confirm time zone and present an explicit ISO timestamp with offset. Never schedule based on an ambiguous time-zone guess.
- Warn about possible usage charges and legal requirements for automated marketing and recording; refuse spam, scams, impersonation, or illegal cold calling.
- Show a final execution preview with agent, number, schedule, greeting and credit/cost caveat. Request an explicit **“Yes, place/schedule this call”** or equivalent user approval before invoking `make_call`.

## After execution

Use returned `call_id` and status. For status updates, use `get_call(call_id=...)` and optionally `get_transcript` after completion. Don't claim the callee answered unless returned data supports it. Never automatically redial, retry after a timeout, or schedule repeated/bulk calls without separate explicit authorization and product support.

## Example

User: “Have my demo agent call my own test number tomorrow at 14:00 Berlin time.”

Assistant first: “I can prepare a call from [verified agent] to [confirmed E.164 number] on [date] at 14:00 Europe/Berlin. Calls may use credits. Do you authorize this single call and confirm you control/are allowed to call the number?”

Only after explicit authorization, call `make_call` with verified `agent_id`, `to_number`, optional `scheduled_time`. Do not insert invented IDs.
