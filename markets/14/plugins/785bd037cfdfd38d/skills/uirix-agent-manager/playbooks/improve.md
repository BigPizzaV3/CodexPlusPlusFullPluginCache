# Improve the agent

Topic `improve` · version 2026-10-02 · served by `uirix_guide({ "topic": "improve" })`.

Making an agent answer better: training with test questions (also for a new agent), learning from recent conversations, fixing one behaviour with a rule or one fact in the knowledge, tidying the improvement rules, rewriting the instructions of one channel and restoring a saved version.

```
GUIDE improve: make the agent answer better

GOAL
The agent answers real questions correctly, in the right tone, and moves the customer to a next step. Every fix is the smallest one that works, the owner approved its wording, and it was tested again.

FACTS THAT MISLEAD
- Each channel has its own instruction text and its own improvement rules: phone (surface incoming), Website Chat (chat), Voice Chat (voice). A rule saved on one channel does nothing on the others.
- update_prompts REPLACES the rule list of a channel: always send the existing rules plus the new ones.
- Rules and direct edits of the instruction text apply on the next conversation. No rebuild. Rules survive a rebuild, hand edited text is replaced by one (rebuild playbook).
- Fewer rules work better: every rule costs space in every conversation. More than about 10 on a channel is a reason to tidy.
- test_chat is a dry run: the agent's actions (lead, ticket, order, e-mail) are accepted and NOT carried out, and the conversation stays out of the metrics. Every turn is still billed.
- The knowledge summary is the only knowledge the agent has. Judge an answer against it and against the instructions, never against what you know yourself.

READ FIRST
- get_briefing(period, agent_id) when the owner asks whether the agent needs work: training.recommended, the reason, each signal with the conversations that show it and where its fix is made. Start from the first signal. No signal means no reason to change a working agent.
- get_agent_setup(agent_id): what the agent really does on each channel, the knowledge outline and its gaps, how many rules each channel has and whether they conflict, the average quality of recent conversations.
- get_prompts(agent_id, surface): the full instruction text of a channel, its rules and the last rules review (conflicts, unclear rules).
- get_kb_summary when a fact must be checked or corrected.

CHECKS
Start from the findings of get_agent_setup: rules that contradict each other, unclear rules, rules saved but missing from the text the agent runs on, instructions longer than the platform aims for, a low quality score, no recent conversations. Then:
- Is there anything to learn from? list_conversations for the window (limit 1) and the age of the agent. A new or quiet agent has no conversations: say so plainly and offer test questions, or a longer window.
- Quality: the average score, and the issues named in the summaries of recent conversations.
- Rules: how many per channel, and a rule that exists on the phone and is missing on chat.

RECOMMEND: route every fix by its type
- A FACT (an address, a price, opening hours) that is wrong or missing goes to the knowledge.
- A BEHAVIOUR ("do not say hello", "always ask for the phone number") becomes ONE short imperative improvement rule on the right channel.
- A STRUCTURAL problem (the text itself is wrong) is a rewrite of that channel, only after the owner approved the new text. Prefer a rule when a rule is enough.
By issue of the quality score: unanswered_question is a knowledge fact. no_next_step is one rule, or a way to take the customer's details (Agent setup). tool_error is a missing detail or a connection (Agent setup). contradicted_itself usually means instructions out of date (rebuild playbook). wrong_language is the language setting or one rule. too_long, repeated_itself and asked_again are one rule or the tone. ignored_request is something the agent cannot do yet.

ASK
Which channel: Website Chat (default), Voice Chat or phone? Then only what the chosen item needs: the owner's own questions, how many days back, or what should change.

APPLY: train with test questions (also for a new agent)
Say which step you are on.
1. Ask whether the owner has questions of their own. If not, write about 10.
2. Write them from the knowledge summary, the instructions and the capabilities: facts (hours, prices, address), things the knowledge does not cover (the agent must admit it or hand over), a tone and language check, and one probe per capability (a dry run: the action is accepted, nothing is sent). The owner's questions come first. Show the list and let them add, remove or reword.
3. Say the cost once: every question is one billed chat turn. Wait for the yes.
4. Group the questions by topic. Questions on the SAME topic go into one test_chat call (up to 5 messages, send_greeting false, the chosen channel), as a customer would ask them; a new topic gets a new conversation so that answers do not influence each other. Never one conversation per question: every conversation carries the whole instructions and knowledge again, and the cost is per turn either way. The unanswered flag marks a reply the agent could not give.
5. Show a table: question, what the agent answered (shortened), verdict (correct, wrong, did not answer), why. Mark "check" when unsure and let the owner overrule.
6. For every miss propose the fix by its type, show the wording, apply after the owner approves.
7. Offer to run the failed questions again and show before and after.
8. Offer to keep the questions that matter as the agent's saved test questions (testing playbook), so every later change is checked against them.

APPLY: improve from recent conversations
Ask how many days back (default 7). list_conversations for the window with summaries. Start from the quality score and the issues of each summary, then read with get_conversation the ones with unanswered turns, an escalation or a low score: at most 10. Propose at most 5 rules per channel, one imperative sentence each, with one example conversation. Apply only after the owner approved the list.

APPLY: fix a behaviour (one rule)
get_prompts first. Then update_prompts with refinement_rules = the existing rules plus the new one, on the right surface. Keep the list short. Show what you saved.

APPLY: fix a fact
get_kb_summary with max_characters 100000 (every window). Add or correct the line in the right place. Save the same fact as a text document: add_document, keep_verbatim true for an exact detail such as an address or a price list, title "Training corrections" plus the date. Then send the FULL summary back with update_kb_summary. A summary longer than 100,000 characters is not sent back: save the document only and offer the knowledge refresh (reindex_kb: paid, needs a yes). NEVER call reindex_kb on your own.

APPLY: improvement rules (view, tidy, remove)
Show the rules per channel with the conflicts and the unclear rules of the last review. Propose merging duplicates and removing what the instructions already say. Send the complete list that should remain, and only after the owner approved it.

APPLY: rewrite the instructions of one channel
Show the proposed text, or the changed passages, and get a yes before update_prompts with instructions: it replaces the live text of that channel and saves a version that can be restored.

APPLY: restore a previous version
list_prompt_versions for the channel: show label, date and notes. restore_prompt_version only after the owner names the version: it replaces the live text.

VERIFY
Read again (get_prompts or get_kb_summary) and confirm the rule or the fact is there. Then ask the question that failed once more, on the same channel.

MONEY
Billed: every test_chat turn (say it once for a batch and wait for the yes; one or two questions need no separate approval) and reindex_kb. Free: every read, update_prompts, update_kb_summary, a text saved with add_document, restore_prompt_version.

MISTAKES TO PREVENT
- A new rule saved without the existing ones.
- Rules stacked where one would do, or a rule on the wrong channel.
- A rewrite where a rule was enough.
- A verdict judged against your own knowledge.
- live_actions true on a test without the owner's yes: it creates a real record and sends a real e-mail.
- A knowledge refresh without a yes.

STOP WHEN
The misses the owner cared about are fixed and pass when asked again, the rule lists are short and free of conflicts, and the owner knows what changed on which channel.
```
