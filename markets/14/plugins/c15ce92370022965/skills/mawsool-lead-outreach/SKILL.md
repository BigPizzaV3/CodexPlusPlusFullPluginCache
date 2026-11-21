---
name: mawsool-lead-outreach
description: Search Mawsool for B2B people and companies, check wallet credits, reveal work email or phone, and save profiles to a Mawsool list. Use when the user asks for leads, prospects, founders, emails, phone numbers, Mawsool credits, or saving people to a list. Do not use for open-web research or to reveal contacts the user did not request.
---

# Mawsool lead outreach (ChatGPT)

Use the signed-in user's Mawsool MCP tools. Connector URL: `https://mcp.mawsool.tech/mcp`. If those tools are not available, ask the user to connect that connector and sign in to their Mawsool account. Never invent emails, phones, names, companies, or credit balances.

## Tools

| Tool | Use when |
| --- | --- |
| `check-credits` | They ask for balance, or before a reveal if spend is unclear |
| `search` | Find people or companies |
| `contact-only` | They explicitly want email and/or phone for a specific lead |
| `full-info-without-contact` | Profile or company context without a paid reveal |
| `save-to-list` | They ask to save people into a Mawsool list |

## Workflow

1. Call `check-credits` when they ask how many credits they have. Before a reveal, call it when they have not already confirmed they want to spend.
2. Call `search` only after copying closed values from [references/filters.md](references/filters.md): industries, countries, seniority, function, language, company size, revenue, founded year, and years of experience. Use `search_type: "people"` unless they asked for companies. Keep `limit` at or below 25. Start at `page: 1`. Summarize name, title, company, and LinkedIn URL from `items` or `results`.
3. Call `contact-only` only after they ask to reveal email and/or phone for a specific person.
   - `url`: `https://www.linkedin.com/in/...` (turn a slug into that URL)
   - `fields`: `email`, `phone`, or `email,phone`
   - `country`: only if they named one
4. On success, a Mawsool reveal card shows the contacts. Tell the user the card has the result. If the tool text includes `work_email`, `work_phone`, `emails`, or `phones`, repeat those values in the reply. If the product strips them from chat, still point to the card. Do not refuse a reveal the user requested and the tool returned.
5. Call `save-to-list` only when they ask to save. Always pass `list_name`. If they do not name a list, use `Saved from ChatGPT`. Copy `url`, `first_name`, `last_name`, `title`, `company`, `headline`, and `name` from the search row. Leave `create_if_missing` at its default (true).

## Spend

- Search uses 0 wallet credits and 1 daily search slot per call, including each extra page. Free plans are about 75 searches/day; paid plans about 150, unless the account has a custom limit.
- A billable email reveal costs 5 credits. A billable phone reveal costs 20. Both cost 25. A field that was already revealed costs 0. Report `creditsCharged` and `creditsRemaining` from the tool result.
- `contact-only` also marks the profile revealed and adds it to the account's saved leads. That is separate from a named list. Still call `save-to-list` when they want a specific list.
- `full-info-without-contact` does not charge a reveal. Do not use it when they asked for email or phone.

## Failures

- `insufficient_credits`: state the balance and stop. Do not invent contacts.
- `daily_search_limit_reached`: stop paging and say the daily search quota is used up.
- `retry_needed`: call `contact-only` once more with the same `url` and `fields`. If it still needs a retry, ask them to try again in about 30 seconds.
- Missing LinkedIn URL: ask for it before `contact-only` or `save-to-list`.
- Tool error, or a requested field came back empty: say that field was not returned. Do not fill the gap.

## Example

User: "Find VP Sales in the UAE and get the first person's work email."

1. `search` with `search_type: "people"`, `page: 1`, `limit: 10`, `filters: { "job_title": "VP Sales", "location": "United Arab Emirates" }`.
2. Show a short list with name, title, company, and LinkedIn URL.
3. `contact-only` for the first row only, with `fields: "email"` and that row's `url`.
4. Point to the Mawsool reveal card and repeat `work_email` when the tool returns it. Mention `creditsCharged`.
