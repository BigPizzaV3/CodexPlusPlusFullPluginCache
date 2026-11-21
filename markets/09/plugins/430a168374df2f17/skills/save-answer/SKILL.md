---
name: save-answer
description: Draft or capture a UPSC Mains answer and save it to the reader's Laya Mains Notes with its bricks, syllabus topic, revision card and value addition, after showing exactly what will be saved and hearing a plain yes, and change named parts of a saved answer later. Use when the reader asks to save, keep or file an answer, to turn a source such as an editorial into a saved answer, or to change an answer they saved.
---

# Save an answer to Mains Notes

Inputs. The question, or a source to frame one from. The answer when the reader wrote it. The paper and marks when known.

1. Call `get_settings` once in the conversation. Use `default_marks` when the reader names no marks, `save_preview` for how much of the answer the echo shows, and `value_addition_depth` for how much enrichment to draft.
2. Keep the reader's own words when they wrote the answer, and draft only what they ask you to draft. Frame a question from a source the way UPSC asks it, with a directive such as Discuss or Critically examine.
3. Write 3 to 30 bricks, each one self-contained fact or argument drawn from the answer. Star the must-hit bricks, at least one and at most a third of them.
4. Call `fetch` with the id `syllabus` to see the roots and the reader's Optional, then once with `syllabus:<root>` for the paper's tree. Choose the deepest paths that fit, all under one root, the best fit first.
5. Show one echo with the question, the paper and marks, every brick with its stars, the answer (whole or summarised as the setting says), the aids present and the syllabus path. Ask for a plain yes.
6. On yes, call `save_copy_item` with a fresh `idempotency_key`, and reuse that key only to retry the same save.
7. When the result says saved, say it is in Mains Notes. When it says inbox, say it went to the Import inbox for review. Give the link from the result and offer one next step, such as planning its revision with `add_to_plan`.

To change a saved answer, use two turns.

1. Read it with `fetch` and `note:<id>`. Show the exact before and after of each part that changes, including any mnemonic you draft. Say that nothing has been saved and ask whether to save these changes. End the turn here without calling `edit_answer`.
2. Only after the reader approves that displayed wording in a later message, call `edit_answer` with only those parts and a fresh `idempotency_key`. A request such as "change the second brick" or "add a mnemonic" asks you to prepare the change. It does not approve wording the reader has not seen. Approval of an earlier book, plan or answer does not approve this edit.

Bricks and mnemonics go as their whole new list with the existing ids, because a brick left out is removed with its memory.

To remove an answer, call `move_answer_to_trash` after a yes, and say it can be restored in Laya within 30 days.

Many questions at once go through the convert-notes skill. Never save without a yes. Never invent marks, years or facts the reader did not give or ask for. Report a failed save exactly as it happened. The reader's own explicit instructions always outrank these steps.
