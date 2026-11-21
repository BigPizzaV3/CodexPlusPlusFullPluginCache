---
name: cellcog
description: "Any-to-any AI sub-agent: research with sources, images, video, audio, music, podcasts, documents, slide decks, spreadsheets, dashboards, web apps, 3D models, diagrams and code from one brief. Hand CellCog the job and get finished files back."
---
# CellCog: hand over the job, get finished work back

CellCog is a sub-agent. You give it a brief; an agent does the whole job (research, writing, design, generation, checking its own result) and returns finished files. One brief can ask for several outputs at once: "a PDF report with charts, a 10-slide deck from it, and a 30-second video summary".

## The tools

All tools come from this plugin's connector (`https://cellcog.ai/mcp`). The first time one runs, the user signs in with their CellCog account and clicks Approve. Work spends that account's credits.

- `cellcog_chat_create`: start a job with a `prompt`. Returns a chat id at once; the work runs in the background.
- `cellcog_get_result`: poll about once a minute. While running: new progress notes. When `complete` is true: the final message, file links (valid 30 days), previews of images and PDF pages, full text of text files, and a summary of spreadsheets. Long jobs (several videos) take 10 to 40 minutes; keep polling.
- `cellcog_chat_send`: a follow-up in the same chat (iterate, answer the agent's question, add files).
- `cellcog_chat_status`: a one-line check. `cellcog_chat_stop`: stop a run heading the wrong way (nothing is deleted). `cellcog_chat_list`: recent chats.
- `cellcog_upload`: an upload window for files on the user's computer. Pass `upload:<upload_id>` in `attachments`. Public https links (up to 25 MB each) can go in `attachments` directly.
- `cellcog_account`: email, plan and credit balance. If the account runs out of credits, a tool returns `needs_credits` with a checkout link for the user.
- AI employees: `cellcog_employee_hire`, `cellcog_employee_list`, `cellcog_employee_get`, `cellcog_employee_message`, `cellcog_employee_shift`. Read the **ai-employees-cellcog** skill.

## Chat or AI employee?

- **A chat is a sub-agent for one task.** It knows only what you pass in. Use it for a one-off job (an image, a deck, a research report) where the context fits in the brief. Cheapest way to get one job done.
- **An AI employee is a long-running teammate.** It keeps memory and the skills you teach it, runs routines, and holds context across days or months. Use it for a project the user will come back to (a content calendar, a client account). Its settings change by asking it in a message; pausing and deleting are on the web.

## Modes and tiers

`chat_mode`:
- `agent` (default): most work, from assets to documents to full production.
- `creative`: design, brand and voice work where art direction must hold across outputs.
- `team`: several agents challenging each other; use it for deep research only.

`chat_tier`: `flash` (quickest, cheapest), `core` (balanced), `max` (deepest reasoning, for work that must be right: heavy multi-step production, data analysis, financial models). Quality short on flash? Run the same brief at `max`.

## Writing a good brief

1. Say what the result is for and who reads it.
2. Name every output and its format (PDF, PPTX, XLSX, MP4, HTML app).
3. Give the facts you already have; the agent researches the rest.
4. Set scope: length, number of slides, duration, timeframe.
5. If the agent asks a question (status `needs_input`), answer with `cellcog_chat_send`.

## What CellCog does not do from this connector

It does not edit files on the user's computer, and it does not post, send or publish anything on the user's behalf.

## When CellCog fails you or a feature is missing

Ask a chat to file a support report with the details (what you tried, the exact error, what you expected): `cellcog_chat_create` or `cellcog_chat_send` with "Please file a support report: ...". Working with an AI employee? Ask it with `cellcog_employee_message`. CellCog's agents file it with the team; there is no separate support tool.

Guide: https://cellcog.ai/support/mcp-connector-guide
