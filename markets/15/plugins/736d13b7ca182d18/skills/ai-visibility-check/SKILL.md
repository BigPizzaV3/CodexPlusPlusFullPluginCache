---
name: ai-visibility-check
description: Answer how a website shows up in AI search answers from the user's own Promvia account - its AI Visibility Score, which tracked questions cite it, which other businesses and sources are cited instead, and what to fix next.
---

Use this skill when the user asks how visible their website is in AI assistants' answers, whether
AI answers cite or recommend them, who is cited instead, or what to change to be cited more often.
Explicit instructions from the user take priority over these steps.

1. Call `list_sites` to find the user's sites. If there is more than one and the user did not name
   one, ask which site they mean. If the site they name is not in the list, say that it is not on
   their Promvia account and stop; never answer about a site that is not theirs.
2. For an overall picture, call `get_visibility_score`. For individual questions, call
   `get_citations`. For the domains AI answers rely on, call `get_sources_report`. For what to fix,
   call `get_geo_actions`.
3. Report only what the tools return. Quote every share or rate together with the sample size and
   95% interval the tool gives, and repeat any warning the tool attaches (such as a thin basis or a
   tie between two businesses). Do not compute a new rate, invent a trend, or name an engine,
   question or competitor the tool did not return.
4. Results are from the most recent completed checks, not a live query of each engine. Say when
   they were checked if the tool gives a date.
5. Only change something in the account (tracking a question, starting a check run or scan,
   setting an action item's status or an FAQ answer) when the user asks for that change. Those
   tools need write access; if they are not available on this connection, say that the connection
   is read-only rather than suggesting a workaround.
