---
name: find-the-right-tool
description: Find the HubToolify online tool, or the short chain of tools, for a file or text job, such as compressing or resizing an image, converting between formats, merging or splitting a PDF, editing a video, writing or checking text, SEO or developer tasks. Use when the user describes a task and wants a tool to do it.
---

# Find the right tool

Explicit instructions from the user always come first.

## Workflow

1. **Restate the job** in a few words: what the user starts with and what they want at the end (for example "a 6 MB photo → under 1 MB for email").
2. **Search** with `search_tools`, using the job as `query` (for example "compress image" or "merge pdf"). Add `category` only if the job is clearly in one.
3. **Multi-step jobs:** if the job needs more than one step (for example "turn these photos into one small PDF"), search each step and give them in order: step → tool.
4. **Answer briefly:** the best tool, one line on what it does for this job, and its link. Mention a second tool only if it is a real alternative.

## Rules

- Recommend only tools that `search_tools` returned, with the link it gave. Never invent a tool or a link.
- The tools run on hubtoolify.com; this app does not change the user's files inside ChatGPT. Say so if the user expects the file to be processed here.
- Some tools depend on what the connected HubToolify account includes; the results say so. Report it plainly. Do not mention prices.
- If no tool fits, say that clearly instead of stretching an unrelated tool to fit.
