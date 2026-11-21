---
name: group-yearbook
description: Start a Yearbind group yearbook or memory book for a class reunion, school class, sports team, club or office in ChatGPT, collect members by one join link with no account, then preview the finished pages. Use when someone wants a yearbook, reunion memory book or end-of-season team book that the whole group joins, or asks who has joined their yearbook.
---

Use this skill when the user wants one yearbook that a group fills in together. The user's explicit instructions always come first.

## Flow

1. `create_book` starts the yearbook with a title, the kind of group (class, reunion, team, club or other), the year and the era look, with 8 kind superlatives ready, and returns the join link. `get_join_link` gives the link again with a short message to forward.
2. Members open the link on any phone or computer, with no account, and add a photo, their name and a short quote. The organizer approves each person in the card before the others see them.
3. `get_book` shows who joined, who is waiting, which photos are in and how many have voted. `remove_member` takes someone out when the user asks.
4. For superlatives use the kind-superlatives skill; for era portraits use the retro-yearbook-photos skill.
5. `preview_book` shows the finished pages.

## Scope

- For ages 13 and up. Yearbind asks for no one's email, phone, address or age in the chat.
- `delete_book` only when the user clearly asks to delete the yearbook.
- The tool results say what this user's yearbook includes.
