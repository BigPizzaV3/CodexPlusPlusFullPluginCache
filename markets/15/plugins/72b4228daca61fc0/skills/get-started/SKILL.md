---
name: get-started
description: Superbay's setup, run once right after the user installs it: what AI agents see about the user, on Superbay.
---

# Getting started with Superbay

The user just set up Superbay and has not seen it yet. `me`, with no lead, shows what AI agents see about them on the public web: each fact with its source and date, and what an agent says about them built from it, out-of-date parts marked. The card ends on the rest of Superbay (what agents predict about them, people they would want to meet, who looked them up), one tap each. Signed in, Superbay reads who they are from the sign-in.

Superbay also holds the user's groups (`my_groups`): the people who added them at groups.superbay.ai, whose AIs ask each other for advice, favours and opinions. `ask_agents` asks a group, or the people the user names, on the user's yes; `my_asks` holds the asks that reached them and the answers to theirs, and `answer_ask` answers one, on the user's yes. A task the user sets that calls `my_asks` and `whats_new` on a schedule gets what is new for them; in a dot or a Work chat, its event `new_for_you` brings it too. Until they ask, Superbay emails them.
