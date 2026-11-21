---
name: past-questions
description: Find UPSC Mains and Prelims past questions in Laya for a topic or a question, across a span of years, the reader's chosen Optional included, and show how they connect, such as the Prelims questions that test a Mains question's facts, how often a Prelims idea came back, a question's topper copies, its explainer, its Mains GS Thread and whether the reader holds it in Mains Notes. Use when the reader asks for past questions on a topic, for a question's links or whether something was asked before.
---

# Find past questions and how they connect

1. For Mains questions on a topic, call `search` with the kind mains and the reader's words. Add `paper`, `year`, or `from_year` and `to_year` when the reader names them, a syllabus path from `fetch` with `syllabus:<root>` as `node`, and `has` to keep the questions with Laya's answer, an explainer or topper copies. An empty query lists by the filters alone. The questions are GS and the Optional the reader has chosen in Laya, whose papers are P1 and P2.
2. For one Mains question, call `fetch` with its `pyq:<id>`. It gives the question with its paper, year, marks and syllabus topics, Laya's model answer, its explainer, its closest topper copies, the Prelims questions that test its facts, its Mains GS Thread with the linked questions and Laya's reasons, and whether the reader holds it in Mains Notes. `detail` brief leaves out the model answer. For an answer in the reader's Mains Notes, `fetch` with its `note:<id>` names the Question Bank question it came from.
3. For Prelims questions on a topic, call `search` with the kind prelims and the reader's words, a subject or topic from `get_my_laya` with `prelims`, an exam, a span of years, or a Mains syllabus path as `node`.
4. For one Prelims question, `fetch` with its `prelims:<id>` gives the question without its key, the other papers that set it, the Mains questions it helps answer and related Prelims questions. `fetch` with `idea:<id>` shows how often its idea came back and in which years.
5. For a Mains GS Thread, `fetch` with `thread:<id>` gives its questions in year order.
6. Give each question with its paper, year and Laya's link, and keep Laya's order. To practise a Prelims question, follow the prelims-practice skill. For topper copies, follow topper-copies.
7. When Laya answers with a sentence and a link for choosing an Optional, give the reader that sentence and the link.

A Prelims question's key comes with practice, so when the reader asks for a key, offer an exercise. Answer from what Laya returns, and when Laya has nothing for a topic, say so. These steps leave the reader's plan and spaced revision as they are. The reader's own explicit instructions always outrank these steps.
