---
name: natural-voice
description: Rewrite a draft so it reads like the user talking rather than like generated text, in English or French. Removes stock AI phrasing, em dashes, formula sentence shapes and vague filler, and keeps the user's own habits, learned from their Instagram captions when Saypage is connected. Use before showing any caption, Reel script, comment reply, DM or bio, and for requests like "it sounds like a robot", "make it sound like me", "less AI, please".
---

# Natural voice

Followers can tell when a caption was not written by the person they follow, and a
creator reading a stiff script on camera sounds like an advert. Run this pass on
everything the other skills in this plugin write, before the user sees it.

## 1. Learn how the user writes

- **With Saypage connected**: `get_account`, then `list_instagram_posts` and
  `get_instagram_post` on three to five recent posts the user wrote themselves (skip
  collabs and reposts). Note their language (and whether they mix two), sentence length,
  how they open a caption, emoji (how many, where), capitals, punctuation, sign-offs,
  words they come back to, and `tu` or `vous` in French.
- **Otherwise**: ask for two or three captions, or the transcript of a Reel they recorded.
- Sum the voice up in three or four lines in the conversation, so every later draft uses
  it. Keep their quirks: someone who writes in lowercase with one emoji per line gets
  exactly that. Never pull their style toward a neutral brand tone.

## 2. Sweep the mechanical tells

- **Em dashes** (—, and " – " used the same way): replace each with what a person would
  type on a phone: a comma, a full stop, parentheses, or "and". Keep dashes only if the
  user's own captions use them.
- **Semicolons and colons** mid-caption: usually two sentences instead.
- **Exclamation marks** on most sentences: keep one, where it is meant.
- **Emoji** at the start of every line, or as bullet points: keep the user's own habit,
  not more.
- Curly or straight quotes do not matter: phones type both.

## 3. Replace stock phrasing

Swap each for the plain word, or better, for the specific thing it stands for.

- **English**: delve, dive into, unlock, unleash, elevate, embark, journey (unless it is a
  trip), realm, tapestry, testament to, game-changer, seamless, effortless, vibrant,
  bustling, nestled, curated, indulge, "take it to the next level", "whether you're a X or
  a Y", "in today's fast-paced world", "let's be honest", "here's the thing", "say goodbye
  to", "look no further", "you won't believe".
- **French**: plongeons dans, "dans un monde où", "que vous soyez X ou Y", "n'hésitez pas
  à", un véritable voyage, sublimer, incontournable, "sans plus attendre", "laissez-vous
  tenter", à couper le souffle, "le petit plus".
- **Food and shops**: "a symphony of flavors" / "une explosion de saveurs",
  mouthwatering, "perfect for any occasion", "made with love". Name the flavor, the
  texture or the ingredient instead: "brown butter and lemon zest".

## 4. Rewrite the formula shapes by hand

These need judgement, so rewrite the sentence rather than deleting words:

- The contrast reveal: "It's not X, it's Y" / "Ce n'est pas X, c'est Y".
- Triplets everywhere: "quick, easy and delicious".
- The question-then-answer setup: "The secret? Cold butter."
- Openers that announce: "In this video", "Today I'm going to show you", "Let's talk
  about".
- A closing moral: "Because good food brings people together."
- Every sentence the same length, every paragraph ending on a punchline.
- Engagement bait: "Drop a 🔥 if…", "Who else…?", "Follow for more". One plain ask
  is fine (see `instagram-caption`).

## 5. Make it concrete

Generated text stays vague. Replace adjectives with facts the user gave: a time, a
quantity, a price, a place, a name, what happened. "Super easy" becomes "five ingredients,
one pan". **Never invent a fact to fill a gap**: write `[how long it takes]` and ask.

## 6. Say it out loud (scripts and voiceovers)

Read the script at a speaking pace, about 2.5 words a second. Shorten any line the user
would stumble on, need a breath in the middle of, or never say in real life. Use
contractions and the words they use on camera.

## 7. Show the result

The cleaned text first, ready to copy, then one line on what changed ("removed two em
dashes, 'elevate' and the closing moral; split the second sentence"). When most sentences
need rewriting, start a fresh draft from the user's facts and voice notes: it is faster
and reads better than a patched one.

The aim is text that sounds like the user. Do not present it as a way to pass AI
detectors, and make no promise about what any detector would say.
