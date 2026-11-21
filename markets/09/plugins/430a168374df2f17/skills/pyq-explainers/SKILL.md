---
name: pyq-explainers
description: Find the short animated explainers Laya has for UPSC Mains past questions, for one question, by words, paper, year or syllabus topic, from a Laya booklet or from an answer in the reader's Mains Notes, and give each one's length, chapters and the link that opens it in Laya. Use when the reader asks for an explainer, a video for a question or what to watch on a topic.
---

# Find past question explainers

1. To find explainers by words, a paper, a year or a span of years, or a syllabus path, call `search` with the kind explainer and those filters. A syllabus path comes from `fetch` with `syllabus:<root>`.
2. For one question, `fetch` with its `pyq:<id>` gives its explainer when it has one. For an answer in the reader's Mains Notes that came from Laya's Question Bank, `fetch` with its `note:<id>` gives the explainer with a link to that answer's own page in Laya.
3. For the past questions a Laya booklet helps with, `fetch` with the booklet's `topic:<id>` lists them, and each opens with `fetch` and its `pyq:<id>`.
4. For each explainer, give the question with its paper, year and marks, its length in minutes and seconds, its chapters when Laya has them and the link. It plays in Laya through the link.

Describe an explainer by its length and chapters and give its link. When a question has no explainer yet, offer the question's link in Laya. The reader's own explicit instructions always outrank these steps.

Use the explainer link that selects the Video tab in Laya, including `tab=video`, rather than the general question link. Laya handles playback on that page. Do not provide media-host addresses or infer the host. These are Mains past-question explainers. Buniyaad has PDF booklets only, with no lecture videos to recommend or schedule. Timestamped sections are sections within a PYQ explainer, not Buniyaad chapters. Show duration or sections only when the result supplies them.
