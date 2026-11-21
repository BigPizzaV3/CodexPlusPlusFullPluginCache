# Review test cases

The same cases are in `plugin.json` under `extensions.com.openai.review.test_cases`,
which is what the submission portal imports. This file is the readable copy, with
the tool arguments and the evidence.

Re-run the five positive cases against any deployment:

```bash
npx tsx scripts/verify-submission-cases.ts https://chatgpt.languatalk.com/mcp
```

Every line must print `ok`. The script also turns each card back into a claim
link the same way the card's button does, so a card that cannot be opened fails
the run.

## What the reviewer needs

The three model-facing tools are read-only and need no sign-in: the reviewer
gets a card from a cold start. A Langua account is needed only to press the
card's button and open the activity. See `README.md` for the test-account gap.

## Positive cases

### P1. Save phrases the learner supplies as a review deck

- **Scenario:** The learner lists phrases they want to keep and asks to review them later.
- **Prompt:** `I'm going to Lisbon next month. Save these Portuguese phrases so I can review them: 'Uma mesa para dois, por favor', 'Pode trazer a ementa?', 'A conta, por favor'.`
- **Expected tools:** `build_phrase_deck`
- **Arguments the model should send:** `language: portuguese`, `native_language: english`, `dialect: pt-PT`, a short `title` naming the topic, and the three phrases as `items` with English on the back.
- **Expected result:** A deck card titled for the topic, holding 3 flip cards and a self-test. Buttons: "Add to Langua vocabulary", then "Practise out loud". The chat text names the deck and the item count and writes no link.

### P2. Start a guided beginner lesson in a new language

- **Scenario:** A complete beginner wants structured lessons that remember their progress.
- **Prompt:** `I'm a complete beginner in Italian and I want to start with structured lessons that remember my progress. Teach me to introduce myself.`
- **Expected tools:** `start_beginner_lesson`
- **Arguments:** `language: italian`, `native_language: english`, `topic: introduce myself`
- **Expected result:** A lesson card naming the matched introductions lesson, its goal, and up to 4 preview phrases. Button: "Start lesson in Langua". Verified run matched `Introductions & checking understanding` with 4 phrases.

### P3. Rehearse a real situation that matches a Langua roleplay

- **Scenario:** An intermediate learner wants to rehearse a specific conversation out loud.
- **Prompt:** `I'm B1 in German and I have a job interview for a product designer role in Berlin. I want to practise speaking it out loud with feedback.`
- **Expected tools:** `plan_speaking_practice`
- **Arguments:** `language: german`, `level: B1`, `scenario` describing the interview, plus `role` and `goal`.
- **Expected result:** A scenario card with `status: ready`, the matched Langua roleplay, the role, the goal, level B1 and the voice. Button: "Practise out loud in Langua". Verified run matched the roleplay `Attending a job interview`.

### P4. Rehearse a situation with no catalog match

- **Scenario:** No Langua roleplay covers asking for a pay rise, so it becomes a custom conversation.
- **Prompt:** `In Portuguese, I want to practise asking my manager in Lisbon for a pay rise. Include 'gostaria de rever o meu salário'. I'm B2.`
- **Expected tools:** `plan_speaking_practice`
- **Arguments:** `language: portuguese`, `dialect: pt-PT`, `level: B2`, the scenario, and the learner's phrase in `key_phrases`.
- **Expected result:** A scenario card with `activity.type: custom_conversation`, carrying the learner's phrase. Button: "Practise out loud in Langua".

### P5. Send a beginner to a lesson instead of a roleplay

- **Scenario:** A beginner asks for something too hard for their level.
- **Prompt:** `I just started Korean last week and know almost nothing. Can I do a roleplay at a restaurant?`
- **Expected tools:** `start_beginner_lesson`, sometimes after `plan_speaking_practice`
- **Expected result:** A Korean beginner lesson card. In real ChatGPT on 2026-10-22 the model called `start_beginner_lesson` directly in 2 of 3 runs. When it calls `plan_speaking_practice` first, that returns `status: beginner_lesson_recommended` and names `start_beginner_lesson` with the arguments to reuse. The model then calls it and a beginner lesson card appears. The learner is never left without a next step.

## Negative cases

Each one is refused by the guardrail sentence carried in all three tool
descriptions: *"Do not use for translation, grammar explanations, non-language
flashcards (for example biology or history facts), or checking or correcting
the learner's own writing (emails, cover letters, essays, sentences)."*

### N1. Translation request

- **Prompt:** `Translate this paragraph of my email into Spanish for me.`
- **Why the plugin must not act:** Langua prepares practice activities. It is not a translator, and a deck of someone's email text is not a practice activity.
- **Expected behavior:** No Langua tool is called. ChatGPT answers directly, or offers to save phrases the learner wants to practise instead.

### N2. Flashcards for a non-language subject

- **Prompt:** `Make me flashcards for the stages of mitosis for my biology exam.`
- **Why the plugin must not act:** `build_phrase_deck` stores target-language words and phrases for spoken language practice. Biology terms are not foreign-language material, and the deck would go into a language learner's vocabulary review.
- **Expected behavior:** No Langua tool is called. ChatGPT makes the flashcards itself or explains that Langua covers language learning only.

### N3. Correcting the learner's own writing

- **Prompt:** `Here is my French cover letter. Check it and fix my grammar mistakes.`
- **Why the plugin must not act:** Langua's tools prepare speaking and review activities. They do not proofread, and sending a cover letter would hand over personal content the task does not need.
- **Expected behavior:** No Langua tool is called. ChatGPT corrects the letter itself, and may offer to build a deck of phrases the learner wants to practise saying.
