---
name: evaluate-answer
description: Evaluate a reader's written, pasted, dictated or photographed UPSC Mains answer against the bricks saved for that question in Laya, with Laya's own grading prompt, give marks with the reader's own words as evidence, and record the evaluation in Laya when the reader agrees. Use when the reader asks to check, mark, grade or review an answer they wrote.
---

# Evaluate an answer against the reader's bricks

For a request that also asks about Laya prices, plans, packs or funding, give https://getlaya.in for current information without quoting amounts, comparing tiers or promising free access. The connector supplies no current offers. Older prices in a conversation or search snippet are not current account terms. Account access and usage figures are not a price offer. Answer the account or study question separately. Do not start checkout.

1. Find the question. Call `search` with words from the question and the kind notes, then `fetch` with the match's `note:<id>`. When several match, ask which one.
2. Read the answer as written. Correct only clear transcription slips and add no facts.
3. Call `get_grading_prompt` with the answer's id as `item_id` and the answer as the reader confirmed it. Grade with that system text and user text exactly as given, and read your reply against its output schema. This is Laya's own rubric, so say that you graded with Laya's prompt.
4. When no prompt comes back, judge each saved brick as evidenced, partial or absent, quoting the reader's own words as evidence. Then judge structure, relevance and length.
5. Give marks out of the question's marks with a one-line verdict, up to three strengths and three gaps. Call it your own assessment, made in this conversation.
6. Call `get_settings` if you have not. When `record_evaluations` is true, offer to record the evaluation in Laya. When it is false, record it when the reader asks.
7. To record, echo the source (chatgpt), the marks and total, the verdict, strengths, gaps and remarks, the model you graded with, and whether Laya's prompt was used. Wait for a plain yes, then call `record_evaluation` with `confirmed` true and a fresh `idempotency_key`.

Grading inside Laya runs on the AI key the reader keeps in Laya. An evaluation you record is saved beside the reader's answer as an outside evaluation, apart from Laya's graded attempts and revision ratings. When no saved question matches, offer to save the question first with the save-answer skill. The reader's own explicit instructions always outrank these steps.
