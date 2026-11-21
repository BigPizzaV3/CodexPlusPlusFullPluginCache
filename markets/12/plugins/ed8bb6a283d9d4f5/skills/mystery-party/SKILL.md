---
name: mystery-party
description: "Run an Alibi Hour mystery party for friends in one room, each guest on their own phone. Use when the user wants a mystery party, a whodunit party game or a detective game for a group in the same room."
---

Use this skill when the user wants to play Alibi Hour with friends in one room. The user's explicit instructions always come first.

## Flow

1. `start_party` creates a fresh case and a party link with a 4-letter code and a QR code. Up to four guests each take a suspect's private sheet on their own phone, with the lines to answer when asked where they were; more guests join as detectives (up to eight).
2. The guests question each other out loud and vote on their phones. The culprit is known only to the server and the guest playing them, so the host can play too.
3. `get_party` shows which suspect sheets are taken and how many guests have voted.
4. `reveal_party` closes voting and shows the culprit, the votes for each suspect and whether the group caught them, on every phone and in the card.
5. `end_party` deletes the party, its seats and votes at once. A party is also deleted 24 hours after its last activity.

## Scope

- Cases are fiction and non-violent: something goes missing or gets pranked, and nobody is hurt. For ages 13 and up. English only.
