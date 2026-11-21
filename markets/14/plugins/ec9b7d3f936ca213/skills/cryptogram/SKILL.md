---
name: cryptogram
description: Make printable cryptogram puzzles (cryptoquotes) from quotes with generate_cryptograms, and suggest readings for a cryptogram with solve_cryptogram.
---

# Zovo Cryptogram Maker

Use `generate_cryptograms` when someone wants printable cryptogram puzzles, cryptoquotes or large print cryptograms.

1. Put each quote in `puzzles` as `{quote, author}`. Convert pasted text or a photo of a list into that array. `text` is a fallback for pasted lines.
2. If the user gives no quotes, write suitable public-domain quotes first.
3. Options are `hints` (0 to 5 revealed letters, or `difficulty` easy, medium, hard), `large_print`, `letter_counts`, `encipher_author`, `answer_key`, `title`, `paper` (letter or a4) and `seed`.
4. Share the PDF link and do not reveal the answers unless asked.
5. Only A to Z letters are enciphered. Accented letters and other alphabets stay as written; tell the user when the result says so.

Use `solve_cryptogram` when someone is stuck on a cryptogram. Pass the exact `ciphertext` and any `known_letters` (for example a printed clue Q=T). Report the confidence it returns. A low confidence reading is a guess; say so and offer to try again with a known letter.
