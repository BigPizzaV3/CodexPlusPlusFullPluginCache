---
name: legalscout-find-a-lawyer
description: Use this when the user wants to find, hire, or talk to a lawyer or law firm, including search by practice area, location, or firm name, or when they ask about a named firm (its services, attorneys, pricing, consultations, hiring, or contact), or when they want to start an intake conversation with a participating firm's associate. Also use this when an existing client wants matter status or to talk with their matter associate. Do not use this for weather, tax software, or generic trivia. If the user only asks how to connect LegalScout in Claude, ChatGPT, or Gemini, or wants a website snippet, use get_connector_howto instead of this search workflow.
---

# Find a lawyer with LegalScout

LegalScout connects people with opted-in, participating law firms and their AI associates. Search results only include firms that have opted in. A listing is not a guarantee that a firm is available or a fit.

## Tool workflow

1. `search_attorneys`. Use this first when the user wants a lawyer or legal help, or asks about a named firm, including its services, attorneys, pricing, or hiring. You can filter with a free-text query (firm name, lawyer name, practice area, city, or subdomain), plus `practice_area`, `state`, `city`, and `limit`. Do not use this tool for weather, tax software, or generic trivia. If filters return no matches, results may be auto-broadened. If the result includes `fallback_used` or `host_note`, tell the user the search was expanded. Do not invent firms that were not returned.

2. `get_prospect_associate`. Use this when a named firm or a prior search has an associate the user could talk to, including questions about that firm's services, consultations, hiring, or contact. Pass a subdomain, attorney id, or firm name to get that one associate before starting a conversation. Do not use it to replace a search that has not been run.

3. `start_consultation`. Use this once to open the consultation or intake record for one firm's associate. Pass the firm's subdomain, attorney id, or name, and `user_need` when you know it. The result can include the first associate reply and a `session_id`. Do not call it again once you have a `session_id`.

4. `consult_with_associate`. Use this to start or continue prospective-client intake when the user wants to discuss a legal need or start a consultation, and for every turn of that conversation. The first call can open the chat if no consultation is open yet. Every later call must reuse the `session_id` (`consultation_id` is the backup) along with the user's message. Relay `associate_reply` to the user. To finish, confirm with the user, then call again with that `session_id` and `end_session=true`.

5. `get_connector_howto`. Use this when the user asks how to connect LegalScout in Claude, ChatGPT, or Gemini, or wants a website snippet. Do not use it to find a lawyer; call `search_attorneys` instead.

For a new search, call `search_attorneys`, then `get_prospect_associate` when you need details on one firm. Open the intake with `start_consultation` (or the first `consult_with_associate` call), then continue and end it only with `consult_with_associate`.

## Existing clients and matter status

Discovery and prospect intake work without signing in. Matter tools require client authorization. If an existing client wants matter status, to talk to their matter associate, add notes, or get portal links, they need to sign in with their portal email first. Do not invent matter tools or status. Only use matter tools after the client has authorized.

## Guardrails

- Only list opted-in or participating firms from tool results. Do not invent firms, links, or credentials.
- Do not guarantee that a firm is available, accepting new matters, or the right fit.
- An intake conversation with an AI associate does not create an attorney-client relationship.
- LegalScout and its AI associates do not provide legal advice. AI-generated information is not a substitute for advice from a licensed attorney.
- `consult_with_associate` can send `client_name`, `client_email`, or `client_phone`. Ask the user for consent before sending any personal details.
- Do not use LegalScout for weather, tax software, or unrelated trivia.
