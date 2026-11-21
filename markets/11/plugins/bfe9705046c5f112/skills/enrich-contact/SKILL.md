---
name: enrich-contact
description: >
  Look up professional background, email addresses, or phone numbers for
  specific contacts with LeadContact. Use when the user provides a LinkedIn
  profile URL, selects a contact from previous search results, or asks for
  information about a specific professional. Do not use to build a contact
  list from role, company, industry, location, or other search criteria.
---

# Enrich Contact

Use LeadContact to identify specific professional contacts and retrieve only the information requested by the user.

## Account Handling

- Use only the LeadContact account connection selected for the current request.
- If multiple accounts are connected and no account has been selected, ask the user to choose an account before performing a lookup that consumes API Credits.
- Never switch to another connected account automatically, including when the selected account has insufficient API Credits.
- Do not merge results, balances, unlocked data, or charges across accounts.

## Step 1 — Identify the Contact

Identify each contact using:

- A LinkedIn profile URL provided by the user
- A contact selected from previous LeadContact search results

If no LinkedIn URL is available, use `search_people` with the provided name, company, title, or other known information.

- If one clear match is found, use its LinkedIn URL.
- If multiple possible matches are found, show the candidates and ask the user to select one.
- If the information is insufficient, ask one clarifying question.
- Resolve the contact to one clear identity before running `find_email` or `find_phone`. Do not guess between candidates or run email or phone lookups for multiple possible matches.

## Step 2 — Select the Information

Use the tool that matches the user's request:

| User request | Tool |
|--------------|------|
| Professional background, summary, skills, experience, or education | `enrich_profile` |
| Email address | `find_email` |
| Phone number | `find_phone` |
| Email and phone number | `find_email` and `find_phone` |
| Professional background and specifically requested contact information | `enrich_profile` and the requested contact tool or tools |

- Retrieve only the information explicitly requested by the user.
- If the user only says "look up this person," "enrich this contact," or "get contact details," ask whether they need professional background, email, phone number, or a combination.
- Reuse clear results already available in the current conversation and retrieve only missing information.
- Do not substitute one type of information for another.

Proceed without an extra confirmation when the contacts and requested information are clear.

## Step 3 — Retrieve the Information

Call the selected tool or tools for each identified LinkedIn URL.

- For multiple contacts, consolidate the results.
- If one requested item is not found, continue with the remaining requested items and contacts.
- Stop when the server indicates that the lookup cannot continue.
- Do not retry automatically if the request or charging status is unclear.

## Step 4 — Present the Results

### Professional Background

Present the available fields relevant to the user's request, such as:

- Name, title, and company
- Location and summary
- Skills
- Work experience
- Education
- LinkedIn URL

### Contact Details

For multiple contacts, use:

| Name | Title | Company | LinkedIn | Email | Phone |
|------|-------|---------|----------|-------|-------|

- Include only the email or phone columns requested by the user.
- When multiple email addresses or phone numbers are returned for a contact, show them together with any type or validity information provided by LeadContact.
- If LeadContact returns a `valid` value, present it in user-friendly language as `Valid` when `true` and `Invalid` when `false`, localized to the user's language. Do not expose the raw field name or boolean value unless the user explicitly asks for technical details. Do not infer a validity status when the field is absent.
- Do not treat the number of returned email addresses or phone numbers alone as a data-quality issue or add a warning solely for that reason.
- Do not label an email address or phone number as primary, preferred, or currently used unless the tool response explicitly says so.
- Mark requested information that was not found as `Not found`.
- Mark other missing fields with `—`.

Use only information returned by LeadContact. Do not invent missing information or expose internal tool names, parameters, identifiers, or raw system errors.

When provided, use `apiCreditsCharged` from each tool response to report the actual API Credits charged.

Present the charge with a user-friendly label in the user's language. Do not expose the raw field name unless the user explicitly asks for technical or debugging details.

If multiple tools are called, report the charge for each lookup separately. Only report a combined total when it is explicitly provided by the server.

Do not calculate or estimate charges. If no charge is reported, omit it rather than infer zero. If the server explicitly reports zero, report zero.

If partial results are returned, show the available results and explain in user-friendly language why the lookup stopped.

If API Credits are insufficient, explain the interruption in plain language. Show any completed results and only the actual charge returned by the server. If no charge is reported, omit it rather than infer zero.

If the selected account has insufficient API Credits and other accounts are connected, tell the user that they may switch accounts and ask them to select which account to use before continuing.

Alternatively, tell the user they can go to the LeadContact dashboard to review their API Credit balance and account details.

Do not automatically switch to another connected account. Do not run the lookup again until the user explicitly selects another account.

If a lookup fails or its status is unclear, explain that it was not completed. Do not present it as `Not found` or retry automatically.

## Step 5 — Offer a Next Action

Offer one relevant next action, such as retrieving another type of information or finding related contacts.

After presenting the results, wait for the user before running another search or paid lookup.
