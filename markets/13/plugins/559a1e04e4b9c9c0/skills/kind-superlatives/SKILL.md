---
name: kind-superlatives
description: Add kind yearbook superlatives such as "Most likely to" titles to a Yearbind yearbook, let members vote privately, then close voting to reveal the winners in the book. Use when someone wants superlatives for a reunion, class, team or office yearbook, asks which titles to add, or wants to see or close the vote.
---

Use this skill when a group yearbook needs superlatives. The user's explicit instructions always come first.

## Flow

1. Every new yearbook starts with 8 kind superlatives. `add_superlatives` adds more titles. Titles start with a positive opener (Most likely to, Most, Best at, Biggest) and stay away from looks, style or clothes, bodies, dating and put-downs; refused titles come back with the reason, so offer a kinder wording.
2. Members vote privately on the join page. `get_book` shows how many have voted.
3. `remove_superlative` takes a title out when the user asks.
4. `close_voting` runs only when the user asks to close voting; it reveals the winners and makes the book final.

## Scope

- Votes stay private: results show the winners, not the counts or who voted for whom.
- If the user has no yearbook yet, start one with the group-yearbook skill.
