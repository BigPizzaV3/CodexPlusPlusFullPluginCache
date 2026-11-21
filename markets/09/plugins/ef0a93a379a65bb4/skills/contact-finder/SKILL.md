---
name: contact-finder
description: Finds decision makers at a German company for given roles (management, sales, purchasing, IT, HR, marketing, finance, sustainability) with sources, using the Implisense real-time contact search. Use when the user asks who to contact at a company or for a contact person in a specific function.
---

# Contact Finder

Find the right business contacts at one German company, with the sources that prove each person. Answer in the user's language.

## Workflow

1. **Resolve the company.** If you don't have its Implisense ID yet, call `company_profile` (or `search_companies` if the user describes the company rather than naming it). If the name is ambiguous, ask which company is meant before going on.
2. **Pick the roles.** Map the user's wording to the role codes `find_contacts` accepts: `MANAGEMENT`, `SALES`, `MARKETING_COMMUNICATIONS`, `PROCUREMENT`, `HUMAN_RESOURCES`, `IT`, `FINANCE`, `SUSTAINABILITY`. Leave `roles` empty for the standard profile.
3. **Run the search.** Call `find_contacts` with `company_id` and `roles`. It researches public sources in real time, costs 3 Implicents per company (refunded if it fails) and takes about a minute. If the user asks for several companies, say what it will cost and confirm first.
4. **Collect the result.** If `find_contacts` returns a `job_id` with status `running`, wait about 30 seconds and call `get_contact_results` with that `job_id` (free). Repeat until the status is no longer `running`. Results are deleted one hour after the search finished.

## Output

Per person: name, role, and the published business channels (email, phone, LinkedIn) — followed by the source URLs. Then:

- Mark entries with `unconfirmed: true` as unconfirmed and suggest checking them before reaching out.
- A phone number with `phoneType: switchboard` is the company's main line, not a direct dial — say so.
- If no one was found for a role, say that plainly and suggest the management from `company_profile` as a fallback.

## Rules

- Business contacts only. Never search for or present private addresses, private phone numbers or other personal details.
- Use only what the tools return; never guess email addresses from name patterns or invent people.
- For the registered management (managing directors, board, authorized signatories) `company_profile` is enough and costs less — use `find_contacts` when the user needs a specific function or direct contact details.
