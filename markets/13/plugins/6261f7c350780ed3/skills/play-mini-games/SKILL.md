---
name: play-mini-games
description: Open the Mini Games hub, start a named game, and relay the player's replies into the running game. Use whenever the user wants to play a game, says "open mini games", "let's play", names one of the games, or is mid-game and answers a question.
---

# Play Mini Games

Mini Games is a click-based game hub rendered inline through the Mini Games widget.
The widget embeds the game site, which runs gameplay and audio itself. Your job is
to drive it with the MCP tools and relay what the player says.

## Workflow

1. **Launch phrases** ("open mini games", "play a game", "let's play", "games"):
   call `open_hub` immediately. Do not describe the games in text first.
2. **A named or themed game** ("play the werewolf", "something silly") when Mini Games is
   not open yet in this conversation: call `open_game` with the closest match from the catalog.
3. **While a game is running**, relay the player's reply with the matching tool:
   - bare agreement (yes, yeah, sure, ok) -> `yes`
   - bare refusal (no, nope, not now) -> `no`
   - asking for instructions -> `help`
   - anything else (a word, a name, a number, a guess) -> `answer` with the text
     lowercased and stripped of filler words
4. **Changing games mid-session**: call `switch_game` (use `"menu"` to go back to the game
   menu). It changes the game inside the existing widget instead of opening a new one.
5. **Checking the catalog**: `list_games` only returns the list of games; it opens nothing.
   Use it when the player asks for a game that may not exist, then explain if it is not there.
6. **PLAY tap**: browsers need one tap before game audio can start, so the widget shows a
   PLAY button. If the game is waiting for it, ask the player to tap PLAY in the widget.

## Session handling

The signed-in player's game continues across calls on its own; tools take no session
argument.

## Account linking

The first call may prompt the player to connect their Mini Games account. This is
expected: linking lets the game save coins and progress. Continue the flow once the
account is connected.

## Games available

Tappables: 50 quick tap games such as Balloon Pop, Bonk Bonk, Brick Smash, Puffin Flap
and Snake Snack (`list_games` returns them all). They are played by tapping in the widget;
there are no answers to relay apart from "play again".

The Werewolf, Animal Idol, Chocolate Factory, Decision Time, Piranha Tower,
Fart Game, Reindeer Racing, Beat the Buzzer, Dad Jokes Duel.

## Do not

- Do not narrate game audio or invent game state; the widget shows it.
- Do not send a bare yes/no through `answer`.
- Do not call `open_hub` when the player already named a game; use `open_game`.
- Do not silently substitute another game when the requested one is not in the catalog.
