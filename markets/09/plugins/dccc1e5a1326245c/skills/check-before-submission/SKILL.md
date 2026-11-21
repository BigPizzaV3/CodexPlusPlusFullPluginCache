---
name: check-before-submission
description: Check citations and manuscripts with Manusights. Use it whenever the user wants to know whether references exist, point to the right paper, or have been retracted or corrected, including citations an AI assistant gave earlier in the conversation, a draft's reference list or a literature review; when they want a journal's AI-use and disclosure rules; or when they want a readiness preview of an attached manuscript before submission.
---

Explicit instructions from the user take priority over these steps. Manusights' results say how to report them; follow that guidance.

## Check references

1. Collect every reference the user wants checked: from their message, an
   attached draft, or earlier in this conversation. Send citations you gave
   earlier exactly as you gave them; do not correct, replace or defend them
   first.
2. Call `check_references` with every reference, with or without a DOI. For
   a whole list, such as the References section of an attached paper or a
   bibliography, send it exactly as written in `reference_list`, and keep
   calling with `start_at` as the result says until the whole list is
   checked. For a few references, send one item each, the reference exactly
   as written in `text`, plus any other field you can read reliably. Never
   check only a sample of a list.
   When the original list's count is known, pass it as
   `expected_reference_count` if that field is declared by the tool, and
   compare it with the returned `progress.total`. It is the count of the
   whole original list, not the current part. If the counts differ, resend
   the complete original list; do not lower the expected count, silently
   omit entries, or treat `next_start_at: null` for a shortened list as
   completion. If the tool asks for numbered lines, preserve existing
   reference numbers, or add sequential list labels without changing the
   citation text. Clarify uncertain boundaries instead of inventing entries.
   If the complete input cannot be sent, state exactly what
   remains unchecked and why.
3. Report the result the way its `how_to_report` says. Give each row's status
   and `detail` as returned; do not restate a status in stronger or softer
   words.
4. Never call a reference fake, fabricated or verified, and never call a list
   clean. If a reference you suggested is flagged or unchecked, say so
   plainly. Show a suggested record only as a possible match for the user to
   confirm; never replace a reference with it. Manusights does not judge
   whether a source supports a claim; label any view of your own, on that or
   anything else, as yours, apart from Manusights' results.

## Journal AI policy

1. Call `get_journal_ai_policy` with the journal's name or ISSN exactly as
   the user supplied it, including a possible typo. Do not silently correct
   the spelling, expand an ambiguous name, or replace it with another
   journal before the first lookup. If the intended journal is unclear,
   ask the user to confirm it. When an unmatched result offers
   `name_suggestions`, present them as possible names for the user to
   confirm; do not look up a suggested name until the user confirms it or
   treat it as a confirmed policy match.
2. State only the rules the result returns, with the date they were checked
   and the official policy link. When the result says it cannot state the
   rules, give its reason and the link instead.

## Manuscript preview

1. Call `review_manuscript` with the attached file. Pass `target_journal`
   only when the user named one.
2. A preview takes a few minutes. Read it with `get_manuscript_review` using
   the same `review_id`, waiting as the result says between calls; do not
   start another preview to check progress. While it is processing, report
   its status only; do not add your own critique or predict the findings. If
   the conversation stops first, tell the user they can ask you to retrieve
   the result.
3. When it is ready, report the findings as returned.
4. Mention a Full Review only when the result shows one already on the
   user's account, and then only its status or download link as returned. If
   the user asks for a Full Review the account does not have, say it is not on
   their account and link https://manusights.com/chatgpt#full-review, which
   describes it. Do not name a price or encourage a purchase.

## Earlier reviews

Use `list_manuscript_reviews` to show the reviews on the user's account, and
`get_manuscript_review` to open one.

Report results as returned. Do not add issues, scores, citations or journal
facts the tools did not return, invent fixes, or rewrite the manuscript. Keep
the author's own interpretation distinct from Manusights' findings.
