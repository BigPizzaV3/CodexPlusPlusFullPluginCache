---
name: topper-copies
description: Find toppers' answer copies in Laya that help with a UPSC Mains question or a syllabus topic, say how each copy relates to the question and why, and give the link to each copy in Laya, where the reader reads it. Use when the reader asks for topper copies or toppers' answers for a question or a topic.
---

# Find topper copies for a question

1. Find the question with `search` and the kind mains. For an answer in the reader's Mains Notes, `search` with the kind notes finds it, and `fetch` with its `note:<id>` names the Question Bank question it came from. An answer the reader wrote alone has none. When several match, ask which one.
2. Call `fetch` with `toppers:<question id>` for that question's copies, closest first. Pass `page` for the next page when the result gives one. `fetch` with `pyq:<id>` also names the closest copies.
3. For copies on a topic, by a topper or a publisher, or by paper or year, call `search` with the kind topper and the filters the reader names, such as a syllabus path as `node`.
4. Show each copy with the topper, the year and rank, the publisher, the paper and question number, how the copy relates to the question and Laya's reason, and the link into Laya. Keep Laya's order.
5. For one copy in more detail, call `fetch` with its `topper:<id>`. It names the questions the copy is linked to.
6. The reader opens the link to read the copy in Laya.

Laya gives a copy's details and its link, and the pages open in Laya. Describe a copy by those details alone. When Laya returns no copies for a question, say so and offer the question's link. The reader's own explicit instructions always outrank these steps.
