---
name: fill-knowledge-gaps
description: Use when an admin asks what the Ciarem AI agent couldn't answer, what customers ask that it doesn't know, or wants to teach it missing information.
---

# Fill knowledge gaps

Admins only: if a tool answers `requires_admin`, tell the user only workspace admins can change the AI's knowledge.

1. Call `get_knowledge_gaps` and list the top questions, most frequent first, with one sample customer message each.
2. For each one the user wants to fix, ask for the real answer. Never write the answer yourself: the AI repeats it to customers as fact.
3. Call `search_knowledge` with the question. If an answer is already there but wrong or outdated, replace it: `delete_knowledge_source` once the user confirms, then add the right one.
4. Add it where it belongs:
   - A fact, policy or how-to: `add_knowledge_text`, into a knowledge base the answering agent uses (`list_knowledge_sources` shows them; `update_agent` `knowledge_base_ids` binds one, and replaces the agent's list).
   - Pages of the business's own website: `add_knowledge_website`. It is indexed in the background: say it is ready only when `list_knowledge_sources` shows it READY.
   - A product, plan or price: a catalog record (the `product-catalog` skill).
5. Test each one: `test_ai_reply` with the sample customer message, and show the reply. If `knowledge_still_indexing` isn't empty, wait and test again.
6. After several additions, call `run_ai_checks`, wait a few minutes, then `get_ai_check_results` and report what didn't pass.

A source with status ERROR in `list_knowledge_sources` can be indexed again with `retry_knowledge_source`.
