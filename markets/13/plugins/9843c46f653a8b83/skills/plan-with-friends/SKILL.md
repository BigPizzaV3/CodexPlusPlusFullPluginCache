---
name: plan-with-friends
description: Use when the user wants to plan or catch up with friends in Woosh - upcoming events, RSVPs, what a group chat decided, polls, and shared expenses. Reads first, and confirms with the user before any change other people will see.
---

# Plan with friends in Woosh

1. Start by reading. Use `list_events` for what is coming up, `get_event` for one event, `read_chat` for what a group said, `get_poll` for a vote, and `get_expense_ledger` for who owes what.
2. Name people and places the way the results do. Never ask for or repeat a phone number, and never guess someone's location: use places as the results give them.
3. Before a change other people will see (an RSVP, a vote, a message, a new event), say what you are about to do and wait for the user to agree, unless your app already asks them to confirm each change.
4. If a tool says the user has not allowed an action, tell the user and point them to Settings -> AI assistants in the Woosh app. If a tool is not available, tell them where to do it in the app (`woosh_guide` says where). Do not try another way round it.
