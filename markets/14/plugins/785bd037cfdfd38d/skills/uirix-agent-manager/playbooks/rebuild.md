# Rebuild the instructions

Topic `rebuild` · version 2026-10-02 · served by `uirix_guide({ "topic": "rebuild" })`.

The safe way to rebuild an agent's instructions after setup or knowledge changed: when a rebuild is needed and when it is not, which step to start from, that it is billed and what it replaces, the build quota, what the build warnings mean, and how to restore a saved version.

```
GUIDE rebuild: rebuild the instructions safely

GOAL
The instruction text of every channel matches the agent's current setup and knowledge. The owner knew that it is billed and what is replaced before agreeing, nothing the owner wrote was lost by surprise, and the result is verified.

FACTS THAT MISLEAD
- A setup change reaches the agent's tools at once, and the instruction text only at a rebuild. Until then the text is out of date and the agent can contradict itself.
- A rebuild from the step "instructions" works on a finished agent, not only on a draft.
- A rebuild made here saves the current instruction text as a version first and keeps the owner's greetings by default. Improvement rules survive it. Text edited by hand is replaced.
- Greetings, improvement rules, voice, widget settings and direct edits of the instruction text apply at once and never need a rebuild.
- New documents or pages need the knowledge refresh (reindex_kb), not this rebuild. Rebuild the instructions afterwards only when the knowledge changed a lot, such as a new line of business.

READ FIRST
- get_agent_setup(agent_id): whether the instructions are out of date and why, the knowledge state (summary present, sources waiting), the four greetings, the improvement rules per channel.
- get_build_status(agent_id): whether a build is running, or the last one failed and at which step. Status "none" means only that no recent build is remembered.

CHECKS
- Is a rebuild needed at all? One behaviour to fix is one improvement rule. A greeting, the voice or the widget is a direct edit.
- Does the owner care about instruction text written by hand? Offer the alternative: keep the text and add one improvement rule.
- Is a build already running? Wait for it. Never start a second build on the same agent.

RECOMMEND: which step
- instructions: the default after setup changes. Rewrites the instruction text of the three channels from the current setup and knowledge. Nothing else is rewritten.
- knowledge: rebuilds the knowledge summary from scratch from every saved source (every document and page is summarised again: the costliest step, minutes on a large knowledge base), then runs greeting and instructions. It also regenerates the greeting, the business name and the description. For new documents alone, reindex_kb (the knowledge guide) is the cheaper way: it adds them to the summary the agent has.
- crawl: reads the website again, then knowledge, greeting and instructions. The same regeneration. Only when the website changed a lot or the first crawl failed.
- greeting: rarely right. A greeting is edited directly, for free.
Before knowledge or crawl, note the business name and the description too, and say that they may be rewritten.

APPLY: the safe rebuild
1. Finish every setup change first. One rebuild at the end, never one per change.
2. Check that the knowledge summary exists and no sources are waiting. A rebuild on old knowledge gives old instructions.
3. Note the four greetings as they are now.
4. Tell the owner in plain words: it is billed to the subscription (one line, no amounts), it takes a few minutes, it replaces the instruction text of all three channels including text edited by hand, improvement rules and greetings are kept, and the current text is saved as a version first so it can be restored.
5. After an explicit yes: rebuild_agent with from_step "instructions" and confirmed true. Poll get_build_status every 10 to 15 seconds until the status is done or error.
6. Read the build warnings (conflicting or unclear improvement rules, a text over its size budget, a channel that was not rebuilt) and say what they mean.
7. Call get_agent_setup again. Confirm the instructions are no longer out of date. Compare the greetings with your note: if one changed, put the owner's wording back with update_agent.
8. If the new text is worse, restore the saved version of that channel (list_prompt_versions, restore_prompt_version).

BUILD QUOTA
Every rebuild counts against the account's build quota: 30 builds a day and 2 running at once, unless the account has other limits. On a quota or concurrency refusal say which limit was reached and when to try again. Never retry in a loop.

BUILD WARNINGS
- Conflicting improvement rules: two rules ask for opposite things. Show both and ask which one stays.
- Unclear improvement rule: the builder could not read it. Reword it with the owner.
- Text over its size budget: the instructions of a channel are too long. Reduce the rules or the description.
- A channel "not rebuilt, the previous text stays in use": that channel still runs the old text. Say which one and rebuild again later.
- Knowledge summary not rebuilt: the old summary stays in use and the instructions were written from it.
- Greeting or description not generated: the earlier one stays. Write it with the owner.

RESTORE A SAVED VERSION
list_prompt_versions(agent_id, type) lists the versions of a channel, newest first: incoming is the phone, chat is Website Chat, voice is Voice Chat. Pass version_id to read one text. After a yes, restore_prompt_version puts that text back as a new version: free, applies on the next conversation, one channel at a time. A restored text is the old text, so it is out of date against the setup again: say so.

VERIFY
- test_chat on the channel the owner uses, one topic per conversation (same-topic questions share it, up to 5 messages): one fact, one per changed action phrased so the agent explains without acting, one question the knowledge does not cover.
- test_chat is a dry run (no lead or e-mail is really sent). live_actions true sends for real: never without a yes.

MONEY
Paid: every rebuild_agent run, reindex_kb, every test_chat turn. Free: every read, update_agent, restore_prompt_version. Before the yes say only that it is billed to the subscription, in one line, no amounts. One yes per paid step.

MISTAKES TO PREVENT
- A rebuild without saying that hand written text is replaced.
- A rebuild from crawl or knowledge when instructions was enough.
- "Done" without reading again and testing.

STOP WHEN
The build is done, the warnings were explained, the instructions are up to date, the greetings are the owner's, and the test questions pass. Or the owner chose to keep the current text. Then say what changed and offer the next best step.
```
