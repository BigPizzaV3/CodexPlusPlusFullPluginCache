---
name: daily-whodunit
description: Play today's Alibi Hour case, a daily non-violent whodunit with four suspects and one liar, or start an Alibi Hour mystery party for friends in one room. Use when the user wants a mystery game, a whodunit, a detective game or a daily logic puzzle, or a mystery party game for a group.
---

Alibi Hour has one case a day, the same for everyone, and a new one at 00:00 UTC. Something has gone missing; four suspects account for six ten-minute times; one suspect, the culprit, lies in every statement, and the other three tell the truth. The statements and the culprit are stored on Alibi Hour's server: a statement is known once ask_suspect returns it, and the culprit once the user has accused someone. The user's explicit instructions always come first.

## Flow

1. show_daily_case opens today's case file in a card: what went missing, where and when, the map of four rooms, the four suspects, and the questions left (10 a day).
2. ask_suspect takes a suspect and one of the case's six times and returns that suspect's statement word for word. Working out the culprit is the user's puzzle.
3. accuse_suspect records the user's one final accusation. The result says whether the user's own answers proved it, par for the case, and when the next case opens.
4. show_case_results shows a closed case's solution (up to 30 days back); get_my_stats shows the solving streak; create_share_link makes a result link that keeps an open case secret.

## Party mode

start_party sets up a fresh case for a group in one room: a 4-letter code, a link and a QR code. Up to four guests take a suspect's private sheet on their phone and up to eight join as detectives. get_party shows how it's going; reveal_party shows the culprit and the votes on every phone; end_party deletes it.

## Scope

- Cases are fiction and non-violent: something goes missing or gets pranked, and nobody is hurt. For ages 13 and up. English only.
- Alibi Hour doesn't write stories on request; a made-up mystery is ChatGPT's own job.
