---
name: card-text-in-image
description: "For text inside a generated image beyond one short headline: several lines, bullets, property labels or badges with icons; covers splitting the supplied wording into exact lines, spelling, placement and label style. Not needed for one short headline."
metadata:
  version: skill-render-ea6bd93365667f6d
---

# Russian text in the frame

The text on a card is drawn by the generative model. Clear wording, short lines and a set
position improve the legibility and accuracy of the lettering.

## Legibility

Generative models reproduce short lettering with a clear hierarchy more reliably than dense
paragraphs and small text. Choose the amount of text and how to split it to suit the task, the
frame size and the capabilities of the chosen model.

## How to put lettering into the prompt

- State explicitly in the prompt which text to render and where it sits in the composition
  ("a large offer at the top", "a bullet near the bottom edge"). Do not count on the model to
  come up with the text itself.
- Write the in-frame text in exactly the words that must appear on the slide, in its own
  language, in quotes or as an explicit list of lines, so that the model does not rephrase it.
- Describe only the visible result: the content of the lettering, its role, its position and its
  visual character.

## Spelling

- Check the spelling and the keyboard layout of the Russian text you ask to render (no words typed
  in the wrong layout, no Latin letters that only look Cyrillic): a mistake on a card is visible
  to every buyer.

## Labels and markers

- Express a property marker in words: describe the label and a simple, clear icon ("a label with
  text and a minimalist water-drop icon for water resistance").
- Keep markers simple and unambiguous, because the model draws a complex pictogram unreliably.
- Describe the labels of one set uniformly (shape, position, style): a consistent rhythm is held
  through identical wording on every slide.

## Check before assembly

- The text is short and fits the frame without small type.
- The spelling is checked.
- The label style matches the rest of the set.

*For the chosen model, keep the intent and the exact in-frame text, and take the model's limits
and capabilities from the current catalog. The chosen model's current prompting guidance owns model-specific syntax;
its live contract owns available fields.*
