---
name: harakah
description: Check and fix Arabic text in motion-graphics code (Remotion .tsx/.jsx, HyperFrames/GSAP/HTML, canvas, three.js) with the check_arabic and fix_arabic tools. Use when creating or editing a composition or animation that contains Arabic text, and before rendering one. Catches split letters, wrong direction, Latin-only fonts, letter spacing and mixed digits.
license: MIT
metadata:
  homepage: https://harakah.si
  package: harakah-fixer
---

# Harakah: Arabic motion fixer · حركة

Arabic letters join. Animation code that splits text into per-letter boxes (`text.split("")`,
`Array.from(text)`, SplitText `chars`, `inline-block` spans), forgets `dir="rtl"`, uses Latin
fonts, tracks letters apart, mixes digit styles or draws letters one by one on a canvas
**renders as disconnected, backwards Arabic**. Harakah finds these and fixes them safely, and
keeps the per-letter animation.

## Tools

- `check_arabic { code, kind?, digits? }`: lists the Arabic problems in one file's code, with line numbers. Changes nothing.
- `fix_arabic { code, kind?, digits?, split? }`: returns the repaired code plus a list of changes and anything left to fix by hand.

Send the code of **one file** per call (an HTML/GSAP/HyperFrames page or one Remotion component, up to 200,000
characters). `kind` is `html` or `remotion` and is detected when omitted. `digits` is `eastern` (default), `western` or `keep`.
`split` is `zwj` (default, keeps letter boxes joined) or `word` (animate whole words).
The tools only see the code you send. Don't send files that hold secrets or personal data, and don't send code that has no Arabic in it.

## Workflow

1. **After writing or editing** a composition that contains Arabic, call `check_arabic` on that file's code.
2. **If it reports problems,** call `fix_arabic` with the same code and give the user the fixed code (or apply it to the
   file when you can edit files). The fix adds `harakah:` comments at every change. Keep them, since they explain the change.
   - For Remotion, the fixed code may import `./harakah-arabic` (`splitArabic`, `formatDigits`, `ArabicText`). Tell the user to
     get it from the `@harakah/remotion-arabic` package or by running `npx -y -p harakah-fixer@0.5.0 harakah-fix fix <project> --write`.
   - Items under `remaining` weren't changed automatically. Edit them yourself following the message.
3. **Check again** with `check_arabic` on the fixed code. Don't call a composition done, or tell the user it's safe to render,
   while it still reports errors or warnings (`ok` is false).
4. **Projects:** check the files that contain Arabic one at a time. On a computer with Node.js 22.12+, the user can check a whole
   project and render before/after proof locally with `npx -y -p harakah-fixer@0.5.0 harakah-fix gate <project>` and
   `harakah-fix compare <project>`.

If a tool call fails or returns an error, say so and don't claim the Arabic was checked.

## Writing new Arabic compositions (do this from the start)

Read [references/arabic-motion.md](references/arabic-motion.md) before writing Arabic motion: splitting, direction, letters in motion, sizes and timing, fonts, digits. The essentials:

- Animate per letter with `splitArabic(text)` (keeps joining with ZWJ) or per **word**. Never use `text.split("")` or `Array.from(text)`.
- In Remotion, prefer `<ArabicText text="…" by="letter|word" />` from `harakah-arabic`.
- `dir="rtl"` and `lang="ar"` on the Arabic container. Mixed Arabic+Latin lines: wrap Latin in `<bdi>`.
- Motion follows reading order: staggers start on the right, reveals and entrances run right to left.
- Canvas: one `fillText` per word with `ctx.direction = "rtl"`. three.js: troika-three-text / drei `<Text>` with an Arabic `.ttf` as `font`, never `TextGeometry` / `<Text3D>`.
- Fonts (OFL): **Alexandria** for display, **IBM Plex Sans Arabic** for text. Don't use Latin-only fonts for Arabic.
- No `letter-spacing`, `text-transform` or italics on Arabic. No `text-align: left`.
- Digits: Eastern by default (`١٬٢٥٠٬٠٠٠`, using ٬ and ٫ separators). Don't mix Eastern and Western digits on one line.

Docs and source: https://harakah.si.
