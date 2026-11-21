---
name: setup
description: Use when the user runs setup for SVGMaker, asks how to get started, or asks what SVGMaker can do. Checks the account, says how credits and saving work, asks what to make and starts the first image.
---

1. Call `svgmaker_account_info` with no arguments. Tell the user their premium credits and credits as two separate numbers. If both are 0, say they have no credits left right now and stop. Do not recommend or push a plan or a purchase.
2. Tell the user in two short sentences how it works: SVGMaker makes the image in their SVGMaker account, and every result shows as a card with a preview and an Open button that shows the image on svgmaker.io. Whether they can download it there depends on their SVGMaker plan. Images made on a free account are public in the SVGMaker gallery; paid-account images stay private unless they share them.
3. If the plugin was installed during a task, carry on with that task. Otherwise ask one question: what do they want to make (a logo, an icon or icon set, an illustration, a sticker, a T-shirt print, a cut file, a pattern), or do they have an image to turn into an SVG?
4. Follow the skill for what they pick. Ask everything that skill needs in one message, each question with a recommended answer, then make it.
5. Every SVGMaker image is made with the SVGMaker tools and shown in the SVGMaker card. Do not show a picture from your own image generation or from the web as the SVGMaker result.
6. After the card, say what was made in one short sentence and offer one next step (a change, another size or colour, a matching piece).
