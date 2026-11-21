---
name: tune-ai-agent
description: Use when an admin wants to set up, fix or improve their Ciarem AI agent, or says it answers something wrong, too long, too cold, or transfers when it shouldn't.
---

# Tune the AI agent

Admins only: if a tool answers `requires_admin`, tell the user only workspace admins can change the AI agent.

1. **Find what to fix.** Call `get_ai_setup`. If the user named no problem, also call `get_account_health`, `get_knowledge_gaps` and `get_ai_performance`, and propose the top three fixes. If they named a real conversation, call `explain_ai_decisions` for it.
2. **Reproduce it.** Call `test_ai_reply` with a customer message that shows the problem, and show the reply before changing anything.
3. **Pick the right lever**, one per problem:
   - Tone, language, length, initiative, welcome: `update_ai_settings`.
   - Who the business is and what it sells: `update_business_profile`.
   - A missing or wrong fact (price, hours, policy): `add_knowledge_text` into a knowledge base the answering agent uses (`update_agent` `knowledge_base_ids`), or `delete_knowledge_source` for a wrong one. Pages of the business's own website go in with `add_knowledge_website`, and a source whose indexing failed is retried with `retry_knowledge_source`.
   - A product, plan or price the AI quotes wrong or doesn't have: a catalog record (`add_catalog_record`, the `product-catalog` skill).
   - How to behave in a situation: `add_coaching`, with the customer message and the AI reply from step 2.
   - When to hand over to a person: `create_transfer_rule` / `update_transfer_rule`.
   - Which agent takes which conversations: `update_agent` `when_to_use`.
4. **Apply it.** Say what you will change in one line, then call the tool. Change only what the user asked for.
5. **Test it again.** Call `test_ai_reply` with the same message (a new `test_conversation_id` unless the problem needs the earlier turns), and compare before and after. If it isn't right yet, go back to step 3 with a different lever rather than piling on more corrections.
6. **Check for regressions** after a round of changes: `run_ai_checks`, wait a few minutes, then `get_ai_check_results` and report what didn't pass.
7. Close any recommended action the user fixed with `close_recommendation` (`resolve`).

Never turn the AI off (`set_ai_active`) or delete anything unless the user asked for it.
