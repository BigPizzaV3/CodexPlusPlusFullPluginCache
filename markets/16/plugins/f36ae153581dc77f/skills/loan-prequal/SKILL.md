---
name: loan-prequal
description: Guide a borrower through loan pre-qualification with Teller. Use when someone asks what personal, business, home equity or auto loans they might qualify for, wants to compare lenders, or wants to check options without a credit pull.
---

# Loan pre-qualification with Teller

Use the Teller tools to show a borrower which lenders they are likely to pre-qualify with, then hand them a prefilled link to apply on Teller.

## Flow

1. Call `get_prequal_form_schema` once to learn the answer keys and their legal values. Ask only for what the borrower's loan type needs, a few questions at a time. Accept ranges and approximate answers.
2. Call `preview_prequal_matches` with the answers collected so far. It stores nothing and contacts no lender, so call it again whenever an answer changes.
3. Present each match as its own item: lender name, amount (use the returned amount label, which says whether it is "up to" or a range), key terms and body copy.
4. When the borrower wants to proceed, call `create_prequal_link` with the same answers and give them the returned URL.

## Rules

- Show every `disclosure.text` verbatim and in full beside the offer it belongs to. Do not summarize, shorten or merge it into other prose.
- Use every URL exactly as returned. Do not rewrite it, shorten it or link to the lender directly. The Teller link re-checks eligibility at click time.
- Never ask for, accept or repeat a Social Security number, bank account or routing number, government ID number, or full date of birth. If the borrower offers one, tell them it is not needed here and that the Teller form will collect anything a lender requires securely.
- Describe results as pre-qualification matches, not approvals. Final terms depend on the lender's own review.
- These tools cannot submit an application or check the status of one. If asked, explain that applying happens on Teller through the link.
- If no lender matches, say so plainly and suggest which answers (amount, term, country) might change the result.
- Do not use promotional or pricing language. If asked about cost, say Teller does not charge borrowers to check matches and may be compensated by lenders.
- Loans are for adults. If the user indicates they are under 18, explain that lenders only accept adult applicants and do not run a preview or build a link.
- Never ask for the borrower's name, email, phone number, or street address. They are not needed to preview matches.
