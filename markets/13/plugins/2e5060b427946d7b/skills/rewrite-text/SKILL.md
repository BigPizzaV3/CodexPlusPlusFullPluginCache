---
name: rewrite-text
description: Rewrite text the user has already written with Akmon. Use when the user supplies existing text and asks to humanize it, paraphrase it or reword it, or asks how many Akmon words they have left.
---

Use the Akmon tools to rewrite text the user provides. Do not use them to write new content, translate or summarize.

1. Get the full text and the mode. If the user has not named a mode, ask which one they want before calling a tool. Never pick a mode for them.
   - humanize_text modes: Deep rewrite (deep_rewrite), Academic Deep Rewrite (academic_deep_rewrite), Sentence Precise (sentence_precise), Academic Precise (academic_precise). The sentence modes work with English and Korean text.
   - paraphrase_text modes: Standard (standard), Fluency (fluency), Formal (formal), Academic (academic), Simple (simple), Creative (creative). Korean text also has casual_enhanced, academic_enhanced and jasoseo.
2. Call the tool with the user's text exactly as given, plus the chosen mode. If the tool returns a list of modes instead of a result, show it to the user and wait for their choice. Nothing is processed in that case.
3. humanize_text needs at least 100 words per call. If the text is shorter, tell the user. If it is longer than one call allows, split it at paragraph breaks and join the results in order.
4. Show the rewritten text as returned, then the mode and words-left lines. Do not edit the result unless the user asks.
5. For questions about remaining words, call get_account_status.
6. If a tool reports an error or a reached limit, relay that message only. Do not add links or suggestions of your own.
