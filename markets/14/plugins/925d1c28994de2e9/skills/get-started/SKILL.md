---
name: get-started
description: How to read, search and listen to the Quran with Qurani.ai, and how its references and edition identifiers work.
---

# Getting started with Qurani.ai

Qurani.ai gives read-only access to the Holy Quran: Arabic text in Hafs and other narrations (riwayat), translations, tafsir (commentary), recitation audio, tajweed rules, word-by-word Arabic grammar, and mushaf page layouts. No account is needed.

## References

- An ayah is written as surah:ayah, for example 2:255 (Ayat al-Kursi). A global ayah number from 1 to 6236 also works.
- A word is written as surah:ayah:word, for example 1:1:2.
- Mushaf pages run from 1 to 604 in the Madani mushaf.

## Editions

Texts, translations, tafsirs and reciters are chosen by edition identifier, for example `quran-uthmani` (Arabic), `en.sahih` (Sahih International), `ar.muyassar` (a short Arabic tafsir) or `ar.alafasy.hafs` (Mishary Alafasy). `list_editions` and `list_reciters` find identifiers for other languages, tafsirs and reciters.

## Common tasks

- Read an ayah with a translation: `get_ayah` with editions such as `quran-uthmani` and `en.sahih`. This also shows the ayah card with a recitation player.
- Read a surah, juz or page: `get_surah` or `get_quran_section`.
- Explain an ayah: `get_tafsir`.
- Find ayahs on a topic or phrase: `search_quran`; similar ayahs: `get_similar_ayahs`.
- Listen: `get_ayah_audio` for one ayah, `get_surah_audio` for a whole surah, `get_word_audio` for one word.
- Tajweed: `get_ayah_tajweed`, with `get_tajweed_rule` to explain a rule.
- Grammar: `get_word_morphology` or `get_ayah_morphology`.
- Narrations: `compare_narrations` lists how they differ on a mushaf page.

Qurani.ai returns published texts, translations and tafsir as they are. It does not issue religious rulings.
