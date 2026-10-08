---
name: compatibility-walkthrough
description: Guide a friendship or love compatibility lookup between two zodiac signs or birthdays. Use when the user asks to compare compatibility, match two signs, or find the widget's compatibility percentage. Open the correct star-sign view and guide the client-only interaction; never invent or claim model access to the displayed score.
---

# Compatibility Walkthrough

Open the primary sign's profile and guide the user to the requested client-side compatibility entry.

## Inputs

Resolve:

- the primary person's star sign or birthday
- the other person's star sign or birthday
- `friendship` or `love`

When a birthday is supplied instead of a sign, read [the zodiac date ranges](references/zodiac-date-ranges.md). Ask for clarification when a numeric date is ambiguous or a date is invalid.

## Workflow

1. Resolve both signs and the compatibility type. Minimize personal data: after deriving a sign from a birthday, use the sign rather than forwarding the birthday to the tool.
2. If both signs are the same, explain that the widget omits the active sign from its compatibility list, so it cannot display a same-sign percentage. Offer to show the shared sign profile instead.
3. For two different signs, call `horoscope` with:
   - `starSign`: the primary sign
   - `route`: `star-sign`
   - `reason`: a concise explanation naming the requested compatibility type and counterpart sign
4. Tell the user to select `Friendship` or `Love` in the widget, then locate the other sign in the displayed list.
5. If the user wants an interpretation, ask them to provide the displayed percentage. Never infer the score from the tool response or claim to read the widget interaction.
6. When the user provides the score, restate it accurately and offer a brief, non-deterministic takeaway plus one constructive conversation prompt.

## Output

Return the two resolved signs, compatibility type, exact widget steps, and either:

- `Score awaiting user lookup`, or
- the user-reported score with a clearly entertainment-oriented interpretation

## Boundaries

- The `horoscope` tool exposes a star-sign view but no model-visible compatibility data.
- Do not fabricate a percentage, scrape the widget, or imply that compatibility predicts relationship success.
- Do not provide high-stakes relationship, mental-health, legal, or safety advice from an astrology score.
