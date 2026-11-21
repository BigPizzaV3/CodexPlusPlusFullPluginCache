---
name: prospect
description: >
  Find professional contacts and build targeted lead lists with LeadContact.
  Use when the user asks to find people by role, title, company, industry,
  location, seniority, skills, company size, employment history, or other
  supported professional and company criteria. Do not use to retrieve a
  specific person's background, email address, or phone number.
---

# Prospect

Use LeadContact to turn natural-language criteria into a relevant professional contact list.

## Account Handling

- Use only the LeadContact account connection selected for the current request.
- If multiple accounts are connected and no account has been selected, ask the user to choose an account before performing a lookup that consumes API Credits.
- Never switch to another connected account automatically, including when the selected account has insufficient API Credits.
- Do not merge results, balances, unlocked data, or charges across accounts.

## Step 1 — Parse the Search Criteria

Extract and resolve the supported criteria from the user's request.

- Use only criteria stated by the user or clearly established in the current conversation.
- Map each criterion to a supported `search_people` field.
- Prefer a dedicated structured field over a general keyword field. Use a keyword only when no supported structured field represents the user's criterion.
- Apply each criterion once. Do not duplicate the same concept across structured fields and keywords or switch interpretations between retries.
- Map explicit job titles or named roles, such as CEO or Sales Director, to job-title fields. Map broad departments or functions, such as Sales or Marketing, to job-function fields. If a phrase could materially change the scope depending on the mapping, ask one clarifying question.
- Interpret current-employment language, such as "currently at" or "works at," as a current-company criterion. Interpret past-employment language, such as "previously at," "formerly at," or "worked at," as a previous-company criterion. Do not substitute one for the other.
- Use only company-size values supported by the tool. If the user's range cannot be represented exactly, ask one clarifying question with the closest supported options instead of silently broadening or approximating it.
- Preserve the user's intended scope. Do not add or broaden titles, industries, locations, companies, employment periods, or other criteria unless the user requests or confirms it.
- If the request is too vague or an important criterion cannot be resolved confidently, ask one clarifying question.

## Step 2 — Search Contacts

Use `search_people` with the resolved criteria.

- If the user specifies a result count, continue through the pagination returned for the same query until that count is reached or no more results are available.
- If no count is specified, use the initial result set returned by the tool.
- If the user asks for "all" or "as many as possible," ask for a target count first.
- Count unique contacts returned by LeadContact toward the requested number.
- Do not run additional searches to replace contacts you personally judge to be mismatches; additional searches may consume API Credits.
- Do not change, remove, or broaden the filters to reach the requested count. Only continue the same query through its returned pagination.
- Do not retrieve beyond the requested count or initial result set unless the user asks.

Proceed without an extra confirmation when the request is clear. Do not retry automatically if the request or charging status is unclear.

## Step 3 — Present the Contact List

### Filters Applied

Show the filters used in user-friendly language.

| Filter | Value |
|--------|-------|
| ... | ... |

### Contact List

For multiple contacts, use the following fields:

| # | Name | Title | Company | Location | LinkedIn |
|---|------|-------|---------|----------|----------|

- Present the contacts returned by LeadContact for the applied filters. Do not remove or reclassify them based only on title variations or missing display fields.
- If a contact clearly contradicts an explicit criterion, keep it visible and briefly note the discrepancy. Do not silently discard it or automatically search for a replacement.
- Show optional columns such as Industry, Company Size, or Skills only when returned values help users compare contacts. Omit any column that is empty for every result. Show applied filters separately from contact fields.
- Mark individual missing values with `—`.
- Do not include email addresses or phone numbers unless separately requested and retrieved.
- Use only professional information returned by LeadContact.

### Summary

- Total matches: use `totalEmployeeCount`, only when provided by the MCP server
- Results returned: use `returnedCount`, only when provided by the MCP server
- API Credits charged: use `apiCreditsCharged`, only when provided by the MCP server

Use only counts and charges returned by the MCP server. Present them with user-friendly labels in the user's language. Do not expose the raw field names unless the user explicitly asks for technical or debugging details. Do not calculate values from the requested count or visible rows. If a value is not reported, omit it rather than infer zero.

If no results are returned, state this clearly and suggest one or two relevant ways to adjust the criteria. Do not change the criteria without confirmation.

If partial results are returned, show the available results and explain in user-friendly language why the search stopped.

If API Credits are insufficient, explain the interruption in plain language. Present any completed results and only the actual charge reported by the server. If no charge is reported, omit it rather than infer zero.

If the selected account has insufficient API Credits and other accounts are connected, tell the user that they may switch accounts and ask them to select which account to use before continuing.

Alternatively, tell the user they can go to the LeadContact dashboard to review their API Credit balance and account details.

Do not automatically switch to another connected account. Do not run the search again until the user explicitly selects another account.

Do not invent missing information or expose internal tool names, parameters, identifiers, or raw system errors.

## Step 4 — Offer a Next Action

Offer one relevant next action, such as:

- Look up a selected contact
- Continue with more results
- Refine the search criteria

After presenting the results, wait for the user before running a new search or paid lookup. Only retrieve email addresses or phone numbers when explicitly requested.
