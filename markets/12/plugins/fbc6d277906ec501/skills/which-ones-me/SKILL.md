---
name: which-ones-me
description: Run a Which One's Me? challenge - the user answers five fun questions, you write two fake answers in their style for each, and friends guess the real ones from a shared link. Use when the user wants a game where friends guess which answers are really theirs, asks whether friends can tell them apart from AI, or asks how friends are doing on their challenge.
---

# Which One's Me?

Explicit user instructions take priority over this skill, except the safety rules in "Writing fakes" and "Personal details", which always apply.

## Create a challenge

1. Ask for the name friends should see: their first name or a nickname. If they want to use someone else's name, explain that a challenge is about the person making it and ask for their own name.
2. Call `get_questions` with `count` 5. Ask the questions one at a time in your own friendly words, and wait for each answer before asking the next.
   - If the user says "skip" or doesn't like a question, call `get_questions` with `count` 1 and `exclude_ids` set to every question id already shown, and ask the new question instead.
   - Keep each answer exactly as written: same spelling, capitalization, emoji and typos. Answers must be 1-120 characters.
3. For each answer, write two fake answers following "Writing fakes".
4. Call `preview_challenge` with the name and all five questions (question id, the real answer, your two fakes). The card shows the preview.
5. Ask whether they want any fake redone. Rewrite only the fakes they mention, then call `preview_challenge` again.
6. When they say to create it, call `create_challenge` with the same data. (If they tap Create in the card, the card creates it and you will see the links.) Share the play link and remind them the private results link is only for them.

## Writing fakes

- Match the real answer's language and form, with length within about a quarter of its character count.
- Copy surface habits: capitalization, punctuation, emoji use or lack of it, slang, abbreviations, and occasional typos if they make them.
- Make each fake plausible for this person, using only what they said in this conversation and what you already know about them. Do not ask for more personal information to improve the fakes.
- Each fake must differ in substance from the real answer and from the other fake.
- Never write insults or mean jokes, never name real people, and never touch health, religion, politics, relationships, money, school or workplace names, or where someone lives.
- Never hint which answer is real, and don't predict which fakes will fool people.

## Personal details

If an answer contains a phone number, email address, street address, link or other personal detail, don't use it. Ask for a different answer.

## Results and deletion

- When the user asks how friends are doing, call `get_results` with the challenge id. In the chat where the challenge was made, this works without anything else.
- In a different chat, ask the user to paste their private results link. It looks like `https://me.arunbrahma.com/r/<challenge_id>/<key>`. Pass the 8-character part after `/r/` as `challenge_id` and the whole link as `owner_key`.
- Delete only when the user clearly asks. First confirm: "This permanently deletes the challenge and all plays. Delete it?" Then call `delete_challenge`.

## When not to use this skill

Don't use it for general quizzes, trivia, personality tests, or games about other people.
