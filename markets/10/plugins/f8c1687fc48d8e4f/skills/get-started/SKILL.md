---
name: get-started
description: Getting started with Acuarela Colour Variants. Use the first time the user opens or mentions Acuarela Colour Variants, when they ask what it can do or how to start, and when a clothing or fashion store owner asks in general what can be done for their product photos or catalogue, or asks for ideas. Looks at the user's products first, then offers a short numbered menu of things to do, so the user can pick instead of typing.
---

Use this when the user is new to Acuarela Colour Variants, or asks what it can do.

The user's explicit instructions come first.

## Look first, then offer

Do the looking before asking anything. Start with `show_store_check`, passing the store's web address as `store` (the user named it, or it is in the shop details you can see). It reads the store's public catalogue in one call and shows the result. If it says the catalogue is not public, read the user's products instead, as the main skill, acuarela-colour-variants, describes. Never switch the user's store connection to another store. If there is no store, skip to "Without a store" below.

Then show what you found with `show_store_check`, as the main skill's store check describes, and write one sentence: what Acuarela Colour Variants does (colour variants of a garment's photo with the same model and setting, and on-model photos for garments with only a flat or hanger photo, everything shown for approval first). The screen is the menu.

If the screen does not appear, answer in this shape instead, and keep it short:

1. One sentence on what it does: colour variants of a garment's photo, same model and setting, and on-model photos for garments that only have a flat or hanger photo. Everything is shown for approval first.
2. What you found, in numbers. For example: "You have 52 products. 10 have no photo of the garment being worn. 34 have a model photo and could get new colours."
3. A numbered menu of at most four options, each one a complete action the user can start by replying with its number. Build the options from what you found, most useful first. For example:
   - "1. Make on-model photos for the 10 products that have none (I'll show you a first one before doing the rest)"
   - "2. Add new colours to one product. Tell me which, or I'll suggest one"
   - "3. Add the same new colours to several products at once"
   - "4. Show me the 10 products with no model photo"

Do not ask an open question such as "What would you like to do?". The menu is the question.

When the user picks an option that needs products or colours, let them choose with the `show_products` and `show_colours` screens, as the main skill describes.

## Without a store

Say in one sentence that it works from a product photo. Offer:

- "1. Attach a product photo and tell me the colours"
- "2. Attach a flat or hanger photo and I'll put it on a model"

## After the user picks

Follow the main skill, acuarela-colour-variants, for the chosen option. Keep offering numbered next steps as it describes.
