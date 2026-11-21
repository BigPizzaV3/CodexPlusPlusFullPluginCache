---
name: get-started
description: First steps with Japanese Skills · 言の葉. Use right after the plugin is installed, or when the user asks what it can do or how to study Japanese words, kanji and grammar with it. Sets the explanation language, walks through one word and one grammar point at the user's level, then offers a short check.
---

# Get started with Japanese Skills · 言の葉

Goal: show the user, with examples at their level, what the lookups do, then let them continue on their own.

1. Ask which language they want explanations in: Simplified Chinese (lang "zh-Hans"), Traditional Chinese ("zh-Hant"), English ("en") or Korean ("ko"); for any other language use "en" and explain in the user's language. Ask roughly where they are: just starting, or a JLPT level from N5 to N1. Use that lang in every call after this.
2. Ask for a Japanese word they want to know, or offer one for their level (for example 食べる at N5). Call `lookup_word`. Explain the reading and its pitch accent, the meaning, and for a verb whether it is godan or ichidan and two or three of its forms. Mention the play buttons on the word card only when the result has recordings.
3. Offer a grammar pattern at their level (for example 〜てもいい at N4), or take one they name. Call `find_grammar`, give the meaning and the example with its translation, and link the page.
4. If they are interested, call `lookup_kanji` for a kanji from the word and list a few of the words that use it.
5. Offer a short check: two or three questions built only from what the results returned, such as a reading, a verb form or the meaning of the example. Correct answers briefly and kindly.

Rules:
- Use only what the tools return. If a lookup finds nothing, say so; don't guess a meaning or reading.
- Link each result's page and name the site, Japanese Skills · 言の葉.
- These tools cover single words, kanji and grammar points. Translate longer texts without them, and don't present such translations as coming from the site.
- If the user asks about the site's practice levels or courses, call `list_courses` and pass on the levels, courses and links. Don't quote prices or plans.
- The plugin needs no personal details, so don't ask for any.
