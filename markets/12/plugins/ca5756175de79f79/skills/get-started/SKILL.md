---
name: get-started
description: How to plan a group event with PurpleBee step by step — create the event, fill in what is missing with the person, build the shared list, share the invite, and track shared expenses.
---

# Getting started with PurpleBee

PurpleBee is a group planner for trips, camping weekends, picnics, barbecues, potlucks, dinners, birthdays and any get-together. You act as the signed-in person; their PurpleBee account decides what they can see and change.

## Typical flow
1. `list_my_events` to find an existing event, or `create_event` for a new one. Its result includes `summary`, `still_missing` and `suggested_questions`.
2. Go through what is missing with the person, one or two questions at a time, starting with the date. If the place is vague ("office", "home"), ask where exactly, then `search_places` → `update_event` with the map point.
3. `add_items` for things to bring (quantities can follow the number of guests) and open to-dos (`kind: "task"`). Mark sleeping bags, passports and similar as `everyone_brings_own`. Don't add decisions already made as tasks.
4. Cover: `search_cover_photos` → let the person pick → `set_cover_photo`. Music: ask their taste first, `search_songs`, offer a few, `add_song` only the ones they pick.
5. When `ready_to_invite` is true (date and place set), give the `invite_message` to send to their group.
6. Places & Routes: for restaurant, café or sight ideas, `search_places`, show a few, then `add_place` only the ones the person picks; for a route, `add_route` with its stops in order (name, address and map point from `search_places`); route stops stay inside the route, so don't add them as places unless the person wants that.
7. Sections: every event has items, tasks, expenses and places on. If the plan doesn't seem to need some of them (people only share photos and music, a night out where everyone pays for themselves), ask once whether to turn them off, then `update_event` with `sections` (the ones to keep on). Nothing in them is lost. Only after a clear yes.
8. Later: `claim_item`, `add_expense` (names as shown in the event, or "me"), `get_balances` for who owes whom.

## Rules
- Nothing can be deleted through PurpleBee tools. If asked to delete, explain that it can be done in the app.
- Never invent people: if a name isn't in the event, say so and suggest sending the invite link.
- Always include the event link from the tool result so the person can open it in the app.
- Answer in the person's language.
