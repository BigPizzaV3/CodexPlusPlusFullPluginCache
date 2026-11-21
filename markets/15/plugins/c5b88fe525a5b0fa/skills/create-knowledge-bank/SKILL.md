---
name: create-knowledge-bank
description: Create a Nshamah knowledge bank (quiz) on a topic, with questions, as a private draft.
---

Use the Nshamah MCP tools. Call list_categories, then create_bank with a specific title, a 2-3 sentence description, the category and the questions; pass a unique idempotency_key. Banks start hidden (draft). Show the user a summary and ask before making it public.
