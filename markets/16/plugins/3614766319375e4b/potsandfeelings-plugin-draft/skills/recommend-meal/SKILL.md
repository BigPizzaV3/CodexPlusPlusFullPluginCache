---
name: recommend-meal
description: Use Potsandfeelings to suggest meals based on location, desired feeling and dietary preferences.
---
Ask for missing country, city or desired feeling before calling recommendPotsandfeelingsMeal. Map everyday wording to supported input enums without inventing restrictions. Use vegetarian for vegetarian requests; the server also accepts its legacy spelling.

When matched=true, present exactly the returned meal name and its recipe. Preserve ingredient quantities, instructions, preparation limitations and separate soup-of-choice handling. Do not replace or embellish the recipe. The recipe may use top-level ingredients and instructions. Never claim all records are independently verified, that regional association establishes origin, or that mood tags guarantee health outcomes.

Only matched=false permits a clearly labelled model suggestion, respecting known dietary preferences. Tool errors are not no-match results; explain the error without fabricating a dataset result. Do not claim ordering, delivery, payments, account access, dataset writes, image generation or medical treatment are supported.
