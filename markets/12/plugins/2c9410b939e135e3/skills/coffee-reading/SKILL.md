---
name: coffee-reading
description: Use when the user sends a photo of their Turkish coffee cup or asks for a reading ('kahve falıma bak', 'read my coffee cup'). Reads the cup (kahve falı) from the photo, shape by shape.
---

Fincanya reads Turkish coffee cups (kahve falı) for entertainment and tradition, in Turkish or English. This skill covers a reading from a photo of the user's own cup and questions about what a shape in the grounds means.

## Inputs

- A photo of the inside of the cup, taken from above after the grounds have dried. A photo of the saucer is optional; by tradition it is read for the wish and home.
- Or a question about one shape, such as "kahve falında deve görmek ne demek?" or "what does a bird near the rim mean?". No photo is needed for that.

## Flow

1. `read_cup` takes the cup photo, and the saucer photo when there is one. It finds the rim, outlines up to 8 shapes in the cup and 3 on the saucer, and returns each shape's zone, clock position, size, form and 8 lexicon suggestions. It shows no card and contains no meanings yet.
2. `name_shapes` takes one Fincanya lexicon name per outlined shape: one of its suggestions, or any lexicon entry in Turkish or English. It returns each shape's traditional meaning, a short reading in English and Turkish (`reply_en`, `reply_tr`) that is suitable to show the user as is, and the card with the photo and numbered outlines, where the user can tap a shape to correct it.
3. When the user wants to keep the reading, `save_reading` adds it to their fal defteri (journal). `rename_shape` corrects a shape in a saved reading, `open_journal` shows past readings, `share_reading` makes an unlisted link and `stop_sharing` turns it off. `delete_reading` deletes one reading, or the whole fal defteri, when the user asks.
4. For a question about a shape, `lookup_symbol` searches the lexicon and returns a one-sentence answer (`answer_en`, `answer_tr`).

## Scope

- Every meaning comes from Fincanya's written lexicon of about 400 traditional shapes. The rim stands for the near future, the middle for the present, the bottom for the past and the saucer for the wish and home.
- A reading describes tradition only: the lexicon contains no predictions or advice about business, partnerships, contracts, money, health, law, death, pregnancy or break-ups.
- By tradition the wish (niyet) stays secret, so no tool has an input for it.
- Fincanya reads coffee cups only; palm, tarot and horoscope readings are outside it.
