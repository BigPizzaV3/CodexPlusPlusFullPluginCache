---
name: agent-training
description: Teach an AssistLoop agent new knowledge. Use when the user wants to add text or a Q&A to an agent, train it on pages of a website, fix or retrain a source, or check whether training has finished.
metadata:
  short-description: Teach an agent with text, Q&A and web pages
---

Help the user add knowledge to one AssistLoop agent and follow its training.

1. Find the agent. If the user did not name one, call `list_agents` and ask which agent
   to use. Call `list_sources` to see what it already knows.
2. Text: call `add_text_source` with the text and a short title. Q&A: call
   `add_qa_source` with one or more questions and the answer. Use the user's wording;
   do not add facts they did not give.
3. A website:
   1. Call `start_website_crawl` with the address. It runs in the background.
   2. Call `get_crawl_results` with its `crawl_task_id` until the status is completed.
      Show the pages found, and which are already in the agent's library. If the status
      is failed, say the crawl failed and stop.
   3. Let the user pick pages, then call `train_website_pages` with those urls. Pages
      already saved are refused unless the user asks to replace them (`replace_existing`).
   4. Follow the fetch with `get_training_progress`.
4. To fix a saved web page, read it with `get_website_source`, then call
   `update_website_source_content` with the full page text, correction included (it
   replaces the whole stored text, so never send only the changed part), and its
   `content_hash` as `base_content_hash`. Then call `retrain_source` so the agent learns
   the change.
5. To retrain any source, call `retrain_source`. It refuses a source still waiting for
   its previous result; say so and check again later.

Training runs in the background. Report it as sent or in progress, and only say it is
trained when `get_training_status` reports trained. Never claim it finished early.
If a tool refuses (a plan or storage limit, a private address), say what it said.
