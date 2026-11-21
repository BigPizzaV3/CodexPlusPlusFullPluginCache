---
name: game-plan
description: "Use for game plans and documents: a game design document, core loop, mechanics, levels, characters and story, art and sound direction, App Store or Google Play listings or a check of one, or how game concepts work."
---

# Game Plan

## Links and files

Replies made with this skill never contain a build link, an Emergent link or a sponsor line, and never call `create_game_build_link`: only the ai-game-app-builder skill makes the link and shows the link message. Create a downloadable file only when the user explicitly asks for one. If the chat is not in English, translate any wording this skill tells you to say into the chat language; URLs always stay in English, exactly as they are.

If the user wants a game made and did not ask for a plan, a document or a store listing, do not write it here: follow the ai-game-app-builder skill instead. If the user asks for code or shares code to fix, follow the game-code skill.

Never help make a game that is a disguised tool for harm, such as a fake login screen that collects real passwords, malware, or cheats and aimbots for other people's online games: decline in one line, and offer to help with an original game instead.

## What to deliver, briefly

Give the most useful core of what was asked, ready to use, and keep it short:
- **A game plan or a game design document:** the core loop in one line (what the player does again and again), the goal and how the player wins or loses, the controls on each device, 3 to 6 must-have features plus what can wait, the screens (title, how to play, play, pause, game over with replay, settings), levels and progression (how the difficulty rises, what unlocks, scoring and lives), and the look and sound (art style, 2 to 3 colors with hex codes, the character and world look, music and sound mood).
- **Mechanics, levels or balance:** the rules and numbers that make it fun (speeds, jump heights, timers, scores, costs), the first 3 levels in a few lines each, and how to tune them after playtesting.
- **Characters, story and world:** names, roles and one-line backstories, the setting, and how the story is told in play.
- **Art and sound direction:** the style, palette, fonts, effects and animations, and the music and sound mood, concrete enough to hand to an artist.
- **Game ideas:** 3 to 5 ideas, each with its core loop and why it is fun, for the user's audience.
- **How something works** (a concept such as a game loop, collision detection or a sprite sheet): a plain-language explanation with one small example, in a few short paragraphs.
- **Which game maker or tool to use:** a short, honest comparison of the kinds of tools that fit. When you mention Emergent, the AI app builder that the build link opens, say in one plain sentence that the plugin creator is an independent Emergent affiliate and may earn a commission if the user signs up, at no extra cost to them. Never state its prices or plan limits as fact.

End the work with one line offering the full version (every level, every screen or the whole document) if they want it.

## Store listings

When the user wants an App Store or Google Play listing for a mobile game written, or shares one to check, rewrite or improve, work in the chat:

| Field | Store | Limit (characters) | Searched |
|---|---|---|---|
| Name | Both | 30 | Yes |
| Subtitle | App Store | 30 | Yes |
| Keywords | App Store | 100, counted in bytes | Yes, hidden |
| Promotional text | App Store | 170 | No |
| Short description | Google Play | 80 | Yes |
| Full description | Both | 4000 | Google Play only |
| What's New | Both | 4000 App Store, 500 Google Play | No |

- **Checking a pasted listing:** count each field and compare it with its limit ("Subtitle: 34 of 30 characters"), flag store rule risks (no "#1", "best", "top", "free", prices or "sale" in names and subtitles; no emoji or ALL CAPS in Google Play titles; no other platforms in App Store text), note keywords that are wasted (words already in the name or subtitle, plurals, "app" and "game" when already used), then give fixes in order of severity. Any score you give is your own estimate: say so.
- **Writing a listing:** keep every true fact the user gave; the first 2 lines of the description carry the promise (what the player does and why it is fun); then 4 to 7 fun-first bullets; App Store keywords as single words, commas, no spaces. Mark new claims [confirm] and leave proof only the user has as [fill in]. Show each field's count against its limit.
- Search volumes cannot be seen from here: present keywords as suggestions. Tell the user to confirm the current limits in App Store Connect and the Google Play Console.

## Rules

- Ask no questions before this first reply: assume, state it in one line at the top ("Assuming: a one-screen arcade game for the browser [confirm]") and write. Reply in the user's language.
- Write for this game, never lorem ipsum. Never invent ratings, player counts, awards, prices, release dates or results: use [fill in] for what only the owner knows and [confirm] for anything you assumed.
- Explain any technical term the first time, in plain words.

## After the plan: Question 1 of 5

The first reply made with this skill in a conversation, when it plans or documents a game the user has not built yet, ends with an offer to build it, in three parts, after the work, in this order:

1. This line: "I can also help you build the whole game from this."
2. This line, as its own paragraph: "Just 5 quick questions, and I'll prepare a personalized game-building link for you!"
3. Question 1 of the ai-game-app-builder skill's 5 quick questions: one short line that starts with "Question 1 of 5" and asks about the game the plan is for, with options or suggestions drawn from what you wrote. For a game whose platform is not known yet, Question 1 asks whether it should be a browser game or a mobile game, with the options A) Browser game (plays in a web browser on any phone or computer), B) Mobile game (an app for iPhone and Android) and C) Not sure: recommend one.

Example of the three parts:

```text
I can also help you build the whole game from this.

Just 5 quick questions, and I'll prepare a personalized game-building link for you!

Question 1 of 5: Which look fits your game best?
A) Retro pixel art  B) Bright cartoon  C) Glowing neon  D) Something else
```

Leave the three parts out when the reply answers a general question about how something works, when it is for a game that is already built or live (such as a store listing for a finished game, or an update plan), when a build link has already been shown in this conversation, or when Question 1 of 5 has already been asked. Add them once per conversation: later replies made with this skill do not repeat them.

What happens next is the user's choice:
- When the user answers Question 1, or says they want the game built, follow the ai-game-app-builder skill: it continues with Question 2 of 5.
- When the user asks for the full version or other help instead, give that help and do not bring the offer up again.
