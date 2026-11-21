---
name: recruiting-board
description: Scout, call, host and offer prospects on the Kickhollow recruiting board, whose true ratings stay hidden until they sign. Use when the user wants to recruit high school football players, scout a prospect or offer a scholarship.
---

Use this skill when a Kickhollow coach works the recruiting board: finding the best prospect, narrowing his rating, winning his interest and offering a scholarship before Signing Day. The user's explicit instructions always come first.

## Flow

1. `get_program` with the recruiting view shows the board: each prospect's position, star rating, the coach's scouted rating range, his interest and what he cares about once a call has found out.
2. A coach has 10 recruiting hours a day. `scout_recruit` (2 hours) sends a scouting trip that narrows the coach's range for a prospect's rating; the stars are only the recruiting services' guess.
3. `call_recruit` (1 hour) raises a prospect's interest and tells what he cares about, such as playing time or a winning program.
4. `host_official_visit` (5 hours) brings a prospect to campus and raises his interest a lot.
5. `offer_scholarship` costs no hours and commits one of the program's scholarships until Signing Day.
6. Prospects are named as on the board or by their id. A prospect's true rating stays hidden from the coach and from every result until he signs, so a reply gives the star rating and the scouted range; no result holds the true rating.
7. On Signing Day (after the 9th game day) recruits pick their schools, and a signed recruit's true rating shows.

## Scope

- Every prospect, school and town is fictional. Real recruits and real recruiting news are outside the game, and ChatGPT answers those itself.
- Each result ends with a short summary suitable to show the user; the card's Recruits tab shows the full board.
