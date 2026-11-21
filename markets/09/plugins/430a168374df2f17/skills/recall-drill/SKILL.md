---
name: recall-drill
description: Revise the reader's own saved answers by recall in three passes, then record how well each brick was recalled once the reader confirms the ratings. Use when the reader wants to revise, memorise or be quizzed on answers saved in Laya.
---

# Revise saved answers by recall

1. Find the answers with `search` and the kind notes, with `list_copy_items`, by the ids the reader names, or as a set from `get_my_laya` with `sets`. Call `get_revision_session` with up to 50 answer ids or a set id, and relay any skipped answers with their reasons. For the next page of a set, pass the result's `next_after` as `after`.
2. Take one question per message in three passes. First the reader recalls the whole answer from the question while you hold the answer back. Then you cue each brick with a short prompt, and the reader answers while you confirm from the brick's text. Last, the reader explains the answer back in their own words.
3. Propose a rating for each brick from what you heard, 1 for missed, 2 for hard and 3 for recalled. Show the bricks with their ratings and wait for a plain yes.
4. On yes, call `submit_review` with `item_result` null, `confirmed` true, a fresh UUID for each event and the current time. Reuse them only to retry the same submission.
5. Say what was recorded and offer to plan the next revision with `add_to_plan`.
6. For a run through revision cards, call `search` with the kind notes and holds revision_card, then `fetch` each `note:<id>`, show the question, wait for the reader's recall, then show the card, then the next.

To save a mnemonic the reader asks for, read the answer with `fetch` and `note:<id>`, and show its mnemonics with the new one. After a yes, call `edit_answer` with the whole mnemonic list, each existing entry keeping its id. Never turn an outside score into a rating. The reader's own explicit instructions always outrank these steps.
