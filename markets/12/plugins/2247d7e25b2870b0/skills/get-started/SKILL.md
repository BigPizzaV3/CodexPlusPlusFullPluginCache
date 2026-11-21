---
name: get-started
description: First steps after installing AstrologyApp. Checks which charts are connected and explains what the user can ask.
---

# Get started with AstrologyApp

1. Call `list_charts`. If the result has charts, greet the user by the label of the chart marked `is_self_chart` and say their Sun, Moon and Ascendant in one line.
2. If `charts` is empty and `charts_without_full_map` is above zero, explain that only charts with the Full Map (Mapa Completo) on AstrologyApp are connected and share `activate_full_map_url`.
3. If `charts` is empty and the account has no chart at all, this person is new: offer to create their chart right here. Ask for the birth date, the birth time if they know it, and the birth city; call `search_birth_city`, then `create_chart`. Explain in one sentence that the Full Map is a one-time purchase per chart on AstrologyApp that unlocks the full reading in the app and this conversation, share the `activate_full_map_url` from the result, and tell them to come back and ask anything once it is active. Do not try reading tools before that.
4. If connecting fails because the person has no AstrologyApp account, tell them the connect button opens AstrologyApp where they create a free account (name, email, password, or Google), and then they connect again from here. Never ask for their password in the chat.
5. Offer three things to ask, in the user's language: how today's sky touches their chart, what the week looks like for work or love, and the best days this month for a plan.
6. Keep it short. Write in prose, no headings, in the language the user writes in.
