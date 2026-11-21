---
name: knowledge-base-gap
description: Check whether the SupportFabric AI's knowledge base can answer a customer question, and if not, draft and (with approval) add or update a knowledge-base note so the AI answers it next time. Use when the user says the AI gave a wrong or missing answer, customers keep asking something, or they want to teach the AI a policy, FAQ or product fact.
---

# Fill a knowledge-base gap

## 1. Pin down the question

Get the exact customer question (from the user, or from a conversation via `conversation_get`) and the correct answer if the user knows it.

## 2. Search what the AI already knows

- Call `kb_search` with the question as `query` (try a second phrasing if the first returns nothing relevant).
- If the account has several widgets/stores and it's unclear which one, call `kb_list` and ask the user which store's knowledge base to use.

Decide:

- **Covered and correct** → tell the user which document already answers it; no change.
- **Covered but wrong or outdated** → propose an edit to that document.
- **Not covered** → propose a new note.

## 3. Draft the note

Write it for the AI to use, not as marketing copy:

- A clear title (the question or topic).
- The answer in plain sentences: facts, numbers, conditions, exceptions (e.g. "Delivery inside Lahore takes 1–2 working days; other cities 3–5. Orders after 4 pm ship the next day.").
- Only facts the user gave or confirmed — never invent policies, prices or timelines.

Show the draft and the target category (from `kb_list`) and ask for approval.

## 4. Save after approval

- New note: `kb_add_text` with `category_id`, `title`, `text` (add `active_from` / `active_until` for time-limited offers).
- Edit: `kb_update_text` with the document's `document_id` and the new `text`.

Then run `kb_search` again with the original question to confirm the new content is found.
