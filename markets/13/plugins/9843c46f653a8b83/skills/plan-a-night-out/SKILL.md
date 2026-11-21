---
name: plan-a-night-out
description: Use when the user wants to get friends together in Woosh - tonight or on a later day. Picks between a shout for right now, a poll in a group chat when the day is still open, and an event with invitations when the plan is set. Confirms the place, the time and who it goes to before anything is sent.
---

# Plan a night out in Woosh

1. Find out three things first, asking only for what the user has not said: when (right now, a known day, or still open), where (a place, or "somewhere nice"), and with whom (all friends, a group, or a few people).
2. Look the people up instead of guessing. Use `list_groups` for a group, `list_friends` or `search_people` for people. Use the names the results give.
3. Find the place with `search_places`. When the result offers a stub from Google with no Woosh id yet, pass its `sourceId` to `resolve_place` to get one.
4. Then pick the one way that fits:
   - **Right now or tonight, and the place is known:** a shout with `create_shout`. It goes out at once to the audience you pass (`friends`, `groupIds` or `friendIds`), and anyone in it can join.
   - **The day or the place is still open:** ask the group in its chat. Find the chat with `list_group_chats` or `list_chats`, and send a poll with `send_message` (its `poll` field), one option per day or place. Read the answers later with `read_chat`, then come back to the next step.
   - **The day and place are set:** create the event with `create_event` (the place as `placeId`), then invite people with `invite_to_event`. Use `get_event` to show it.
5. Before calling `create_shout`, `send_message`, `create_event` or `invite_to_event`, say exactly what will go out, when, where and to whom, and wait for the user to agree, unless your app already asks them to confirm each change. These reach other people's phones.
6. If a tool is refused or not available, say so and tell the user where to do it in the Woosh app (`woosh_guide` says where). Do not try another way round it.
