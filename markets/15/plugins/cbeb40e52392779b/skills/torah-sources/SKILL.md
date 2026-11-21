---
name: torah-sources
description: Answer questions about Torah, Tanakh, Talmud, Mishnah, Midrash, halacha, Jewish law and practice, or Hebrew and Aramaic words by retrieving the primary sources through TorahLM and citing them with links.
---

Use this skill whenever the user asks about a Jewish text, a halachic question,
the meaning of a Hebrew or Aramaic word, or what a commentary says.

1. Find the sources. Use `lookup` or `get_text` when you know the reference
   (e.g. "Genesis 1:1", "Berakhot 2a", "Rashi on Exodus 20:8"), and `search`
   when you don't. Use `get_halachipedia` for practical halacha, `get_links` for
   commentaries and cross-references on a passage, and `lookup_word` for a word.
2. You may use your own knowledge to guess which sources are relevant, but
   confirm each one through TorahLM before citing it. Never cite a source you
   did not retrieve.
3. Answer from what you retrieved. Quote briefly and give each source's link.
4. When the user asks to see the texts, or a Talmud page, or the answer is about
   one passage, call `show_text` once at the end with the refs you cited. Use
   `layout: "daf"` when the user wants a Talmud page. Otherwise don't show the
   card: end by offering to show the cited texts.
5. For the user's own TorahApp learning (their stats, progress in a book,
   activity by week, month or year), call `my_torahapp_activity`. It asks them
   to sign in with their TorahApp account the first time; nothing else does.
6. For a practical halachic question about the user's own situation, give the
   sources and add that they should ask their rabbi.

If a reference isn't found, say so and try `search`; don't guess its text.
