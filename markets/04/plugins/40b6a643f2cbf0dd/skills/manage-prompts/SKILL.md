---
name: manage-prompts
description: Add the questions (prompts) a Radarkit project tracks, group them into topics, and re-ask a prompt to every AI model right now. Use when the user wants to track new questions, organise prompts into topics, or get a fresh answer for a prompt immediately instead of waiting for the next scheduled run.
---

Use this skill when the user wants to add, group, or immediately re-run tracked prompts. It needs a key or connection with the Write permission; if the tools are not listed, say so.

1. Call `list_projects` and pick the project (ask if there are several and none was named).
2. Call `list_topics`. Reuse an existing topic when its name fits. Create one with `add_topic`
   only when nothing fits; the server refuses duplicates and returns the existing topic id.
3. Turn the user's request into prompt texts written the way a real person would ask an AI
   assistant: one question each, under 255 characters, no numbering. Show the list and ask
   for confirmation before adding.
4. Call `add_prompts` once with the topic id and up to 50 prompts. Report what was added and
   what was skipped as a duplicate. New prompts are answered on the project's next scheduled
   run; say when that is (`next_run_at` from `get_project`).
5. Only when the user explicitly asks for an answer now, call `run_prompt_now` for that one
   prompt. It spends one realtime credit from the project owner's balance, so confirm first.
   Afterwards, the fresh answers appear in `list_responses` with `realtime: true` within a few
   minutes; poll `list_prompts` until the prompt's model states read `completed`.

Do not add prompts the user did not confirm. Do not run a prompt now on the user's behalf as
a side effect of adding it. Do not run the same prompt again while it is still processing;
the server answers PROMPT_PROCESSING, wait for it to finish.
