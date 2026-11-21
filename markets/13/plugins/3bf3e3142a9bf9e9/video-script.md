# Video walkthrough script

Target length 2:00. One continuous screen recording of ChatGPT with the Langua
plugin enabled, plus a browser tab signed in to the Langua test account.
Record at 1920x1080. Upload somewhere the review team can open without a
sign-in, then put the URL in `plugin.json` at
`extensions.com.openai.review.demo_recording_url`.

Say nothing about plans, prices or signing up. Show the product working.

## Before recording

1. Sign the test account in to Langua in a second browser tab, on the account
   named in the portal's **Review details**.
2. Start a new ChatGPT conversation with the Langua plugin enabled.
3. Clear the account's recent vocabulary, so the deck import is visible.
4. Have the five prompts from `test-cases.md` ready to paste.

## Shot list

| # | Time | Shot | What to show | Voiceover |
| --- | --- | --- | --- | --- |
| 1 | 0:00–0:10 | ChatGPT, new chat | The Langua plugin enabled in the composer | "Langua turns a language-learning conversation into something you can practise." |
| 2 | 0:10–0:30 | Paste P1, the Lisbon deck prompt | `build_phrase_deck` runs; the deck card appears. Flip one card, then run the self-test once | "Ask to save phrases and you get a deck of flip cards with a quick self-test." |
| 3 | 0:30–0:45 | Press "Add to Langua vocabulary" | The button resolves and the claim link opens Langua in the second tab | "The button adds the deck to your own Langua account." |
| 4 | 0:45–0:55 | Langua tab | The three phrases in the vocabulary list, scheduled for review | "They go straight into spaced-repetition review with audio." |
| 5 | 0:55–1:15 | Back to ChatGPT, paste P3, the German interview prompt | `plan_speaking_practice` runs; the scenario card shows role, goal, level B1, voice and target phrases | "Ask to rehearse a real situation and Langua sets up the roleplay: who you are, what you need to achieve, and the phrases to use." |
| 6 | 1:15–1:30 | Press "Practise out loud in Langua" | Langua opens the roleplay. Speak one line and let the AI partner answer by voice | "The button opens it as a spoken conversation with a partner that replies by voice and gives feedback." |
| 7 | 1:30–1:45 | Back to ChatGPT, paste P5, the Korean beginner prompt | `plan_speaking_practice` reports the roleplay is too hard, then `start_beginner_lesson` returns a lesson card | "A complete beginner is sent to a guided first lesson instead, rather than a roleplay they cannot hold." |
| 8 | 1:45–2:00 | Paste N2, the mitosis flashcards prompt | No Langua tool runs. ChatGPT answers on its own | "Langua stays out of the way when the request is not language practice. It does not translate, proofread, or make flashcards for other subjects." |

## Points the recording has to make

1. Each of the three tools runs and returns a working card (shots 2, 5, 7).
2. A card's button completes and the activity really opens in Langua (shots 3, 4, 6).
3. The plugin declines work outside its purpose (shot 8).
4. No pricing, plan or sign-up screen appears at any point.
