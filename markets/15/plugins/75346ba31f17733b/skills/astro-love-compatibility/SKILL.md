---
name: astro-love-compatibility
description: "Use for zodiac compatibility: how two signs match in love, friendship or work, with scores, strengths, challenges and tips, also when the user only knows the birthdays of the two people."
---

# Zodiac compatibility

## 1. Get both signs

- Use the signs the user names.
- If they give a birthday instead of a sign, call `get_zodiac_sign` for it first (month and day, plus the year if given).
- If a sign is missing, ask one short question for it, for example: "What's their sign, or their birthday?"

## 2. Get the match

Call `get_compatibility` with `sign_a`, `sign_b`, `kind` (`love` unless the user asks about friendship or work) and `started_from` as the tool describes it. Use only the data it returns.

## 3. Write the answer

- Start with both symbols and signs and the overall score, for example: "♈ Aries + ♎ Libra in love: 84/100".
- One short paragraph on the bond from `element_mix`, `pace` and `bond`.
- The other scores from `scores` as one line.
- **What works:** from `strengths`. **Watch out for:** from `challenges`. **Tip:** from `tips`.
- Keep it kind and balanced: no sign pairing is doomed or perfect, and every relationship is unique. Sun signs are only one part of a person.
- Reply in the user's language.

## 4. Close

Offer one next step, for example: "Want this week's love horoscope for both of you?"
