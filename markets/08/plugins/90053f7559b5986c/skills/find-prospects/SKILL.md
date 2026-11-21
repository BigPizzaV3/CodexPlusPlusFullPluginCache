---
name: find-prospects
description: Preview a LinkedIn prospect search in Yadulink, then import a clean list only after the user confirms. Use for ICP searches, shortlists, and list creation.
---

# Find prospects

Turn an ICP description into a previewed Yadulink search. Import only after the user confirms the plan.

## When to use

The user wants to find people, build a list, import prospects, or search by role, industry, or location.

## Workflow

1. Clarify audience, geography, language, and exclusions if they are missing.
2. Call `preview_outreach_search` first. Never skip preview.
3. Summarize the resolved filters, estimated volume, risks, and exact `credits.total_cost` quote.
4. Ask the user to approve that exact import cost.
5. After confirmation, call `execute_outreach_search` once with the returned `execution_requirements.max_credits` and a new idempotency key. The tool itself creates the named list.
6. Offer `clean_and_score_contact_list` if the imported list looks noisy.

## Rules

- Prefer fewer relevant profiles over a large weak list.
- Do not launch a sequence from this skill unless the user explicitly asks after seeing the list.
- Never reuse an idempotency key after changing the query, count, or list name.
- Keep Yadulink safety limits visible: this is controlled outreach, not unlimited sending.
- If the user mentions another workspace account, pass `target_account` only when they named it.

## Output

Show:

- the search plan in plain language
- who would be included and excluded
- the confirmation needed before import
- the list name to use if import proceeds
