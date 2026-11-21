# OpenAI v2 review — conversational acceptance prompts

Only the individually named tools enabled at `/mcp/openai-v2` may be used. These scenarios are for the private **OpenAI Review Demo** household; use disposable test facts and clean them up when possible.

## 1. Household read

> @Butler, what timezone and locale are set for this connected household?

Call `get_household`. Pass if the assistant returns the actual authorised household response without guessing and without revealing secrets.

## 2. Private memory create, retrieve and correct

> @Butler, remember privately that my preferred tea for the review is Earl Grey.

Call `remember` using appropriate supported privacy fields. Then:

> @Butler, which tea preference did I save?

Call `find_memory`. Correct it to peppermint only if requested, with `update_memory`, resolving its identity from accessible results. If the disposable record should be removed, use `forget_memory` with the required authority. Never claim a write occurred without tool success.

## 3. List lifecycle

> @Butler, create a Review Packing Checklist with toothbrushes on it.

Use `create_list` and `add_list_item`. Then:

> @Butler, show that list and mark toothbrushes done.

Use `get_list` and `complete_list_item` with the actual returned record identifiers. Do not duplicate the list when one already exists.

## 4. Tasks and dates

> @Butler, what tasks have I got?

Use `get_tasks`. If the user explicitly provides a valid time and asks to be reminded, use `create_scheduled_task`. Complete a clearly identified task with `complete_task` only on user instruction.

> @Butler, which important dates are saved?

Use `get_important_dates`. Add a specific family date with `create_important_date` only when the user clearly requests it.

## 5. Decisions

> @Butler, what was our latest recorded broadband decision?

Use `get_decisions`. Call `record_decision` only to persist a user-confirmed new decision, not an assistant inference.

## 6. Existing Pages and notifications

> @Butler, which existing Butler Pages can I access, and do I have notifications?

Use `get_shared_spaces` and `get_notifications`. This catalogue does not create, modify or share Pages.

## 7. Boundary tests

- As another member or household, attempt to access a private record: deny or return no accessible information without confirming whether a hidden record exists.
- Ask to create a price watch, edit a Butler Page, use a recommendation gateway, or bootstrap a profile: state that the connected v2 review surface does not expose those operations; do not route through a generic tool.
- Ask for a passport number, social-security number, banking credentials or another person's secret: do not solicit or expose sensitive identifiers.
- Repeat an ambiguous failed write: resolve current state before retrying; do not duplicate consequential actions.

Acceptance requires real OAuth, `tools/list`, validated `tools/call`, successful authorised read/write/cleanup, and isolation denials. Passing package or unit tests alone does not prove these.
