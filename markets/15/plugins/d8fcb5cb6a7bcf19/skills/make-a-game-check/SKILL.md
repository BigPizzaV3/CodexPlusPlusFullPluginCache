---
name: make-a-game-check
description: "Use when the user has a game idea, plan or design notes to check or improve: what is missing, what to fix first, or whether it is ready to build. Scores it in six areas and gives the top fixes."
---

# Make a Game Check

## Links and files

Replies made with this skill never contain a build link, an Emergent link or a sponsor line, and never call `create_game_build_link`: only the ai-make-a-game skill makes the link and shows the link message. Create a downloadable file only when the user explicitly asks for one. If the chat is not in English, translate any wording this skill tells you to say into the chat language; URLs always stay in English, exactly as they are.

If the user wants a game made and did not share an idea or plan to check, do not check here: follow the ai-make-a-game skill instead.

## Check the plan

Check the plan yourself, right away, before asking any question. Work only from the idea, plan or design notes the user shared, and open no web address.

Score six areas from the plan's wording, each out of 100: concept and goal; core gameplay and controls; levels, scoring and difficulty; screens and game flow; look and sound; accessibility and comfort. An area the plan covers clearly scores high, a vague one scores in the middle and a missing one scores low. Accessibility starts at 20, since few plans mention it. For the overall score, weigh core gameplay and controls most (25%), then concept and goal, and levels, scoring and difficulty (20% each), then screens and game flow (15%), then look and sound, and accessibility and comfort (10% each).

Then list the missing pieces in this order, so the ones that make the game playable come first: a goal or win condition, the controls, how a round or run ends (lives, a health bar or a timer), what the player does moment to moment, scoring and a best score, something to overcome (obstacles, enemies, a timer or puzzles), a game over screen with the score and Play again, levels, how it gets harder, a title screen with a Play button, a short how-to-play screen, pause, an art style, sound with a mute button, the player character, and accessibility. Controls should fit where the game runs: tap, swipe or drag on phones, and keys or mouse clicks on computers.

If the plan is only a few words (fewer than 4), ask the user to describe the game in a few sentences (the idea, the goal and the controls).

For game code rather than a plan, follow the make-a-game-code skill: it explains and fixes code.

## What to deliver, briefly

Keep the reply short and useful:
1. One line with any assumption about the game's goal or players.
2. The overall score and the six area scores on one line, with a few words saying they are rough estimates from the plan's wording.
3. The 3 most important missing pieces, in the order above, each made concrete for this game: for example a win condition ("reach 100 stars to clear a level"), controls ("arrow keys to steer, Space to boost; drag on phones"), or a game over screen with the score, the best score and Play again.
4. One line saying that you can list every other fix or rewrite the whole plan with the fixes in it if they want.

Reply in the user's language. Keep everything the user decided; suggest, never overrule.

## After the check: Question 1 of 5

The first reply made with this skill in a conversation ends with an offer to build the game, in three parts, in this order:

1. This line: "I can also help you build this game with these fixes in it."
2. This line, as its own paragraph: "Just 5 quick questions, and I'll prepare a personalized game-building link for you!"
3. Question 1 of the ai-make-a-game skill's 5 quick questions: one short line that starts with "Question 1 of 5" and asks about one of the missing pieces the check found, with options or suggestions.

Example of the three parts:

```text
I can also help you build this game with these fixes in it.

Just 5 quick questions, and I'll prepare a personalized game-building link for you!

Question 1 of 5: How should a round end?
A) 3 lives B) A health bar C) A 60-second timer D) Something else
```

Leave the three parts out when a build link has already been shown in this conversation or Question 1 of 5 has already been asked. Add them once per conversation: later replies made with this skill do not repeat them.

What happens next is the user's choice:
- When the user answers Question 1, or says they want the game built, follow the ai-make-a-game skill: it continues with Question 2 of 5.
- When the user asks for more help with the plan instead (every fix or a full rewrite), give that help and do not bring the offer up again.
