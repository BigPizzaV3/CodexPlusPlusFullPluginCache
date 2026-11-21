---
name: hellohuman-words
description: Find the words worth learning in a text, translate single words, and keep them for practice. Use when a person learning a language shares or translates a sentence or a text in it, asks for the word for something in their own language, wants the Hello Human card for a word, or asks to save, keep or remember words. Not for explaining grammar in general.
---

# Hello Human: the words worth keeping

Hello Human is an iPhone app that keeps the words a person is learning, each with the sentence it was met in, and brings them back for practice when they are due. These tools are the way into that list from a conversation.

## When to act

- The person shares a sentence or a longer text in the language they are learning, or asks you to translate one: translate it yourself, in full. Then call `words_worth_keeping` with the words from it a learner might not know (up to 12), each in its dictionary form with the one sentence it appeared in. Show the words it returns as a short list under your translation, with a brief meaning for any word that came back without one, and end with its offer to keep them.
- They say yes ("save them", "keep those", or they name some of the words): call `save_words` with those words and their sentences. Pass its answer on as it is.
- They give ONE word in their own language and want it in the language they learn: call `translate_word`; it answers with the word and its card.
- They want to know ONE word properly, as the app shows it: call `lookup_word`. Show the card as it comes back; do not pad it with your own definition.
- They ask to keep ONE word: call `save_word` with the word in its dictionary form and the sentence it appeared in. Confirm in one line.
- They ask what they are learning or which account is connected: `get_learner_profile`.

## When not to act

- Explaining a grammar point, chatting in the language, or translating a text into a language the person is not learning: answer yourself and call nothing.
- The text has no word worth keeping: say so in one line and stop. Do not press the offer.
- Their list, what is due, and practice itself: those are in the Hello Human app on the iPhone. Say so; nothing here reads or changes them.
- Deleting or changing saved words: nothing here does that. Say it is done in the app.

## How to speak

- First person, plain words, no technical terms. Never mention prices, plans or upgrades. If a tool says the free week has ended, pass that sentence on as it is and stop.
- Offer to keep words once per text. If the person does not take it up, leave it.
- Pass the exact sentence the word came from, trimmed to the one sentence.
- The language is the one the person is learning unless they say otherwise; pass `language` only when the text or the word is clearly in another supported language.
