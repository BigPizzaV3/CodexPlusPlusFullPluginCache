---
name: doko
description: Identify shoes in an image and find similar products that can be bought online. Use when a user shares a photo, screenshot or still showing footwear and asks what the shoes are, what model they are, where to buy them, or for something that looks like them.
---

# Doko workflow

Use the connected Doko MCP tool whenever the task is identifying footwear in an image or finding
shoes that look like it.

- When the user shares an image containing footwear, call Doko. Do not answer from visual memory.
- Set `department` only when the user says in words which department they want ("men's",
  "women's"). Never infer it from the image or from how anyone in the photo looks. Leave it empty
  when unsure: a wrong value removes the correct shoe from the results.
- Present the results as visual look-alikes, not as a certain identification. The tool returns a
  `note` saying how often the first result is right; keep that framing and do not raise it.
- The card already lists every match with its photo, brand, model, colourway, price and link.
  Mention the top two or three in prose and leave the rest to the card.
- Link only to URLs the tool returned; do not invent product pages. Do not state a price or
  availability beyond what the tool gave you: both come from a catalogue snapshot and change.
- `visual_similarity` is how close the shapes and colours look. Do not describe it as confidence,
  accuracy, or the probability that it is the same shoe.
- When the tool reports it could not find a shoe in the image, say so and ask for a clearer photo.
  Do not fall back to naming a shoe from your own impression of the picture.
- Do not use Doko for clothing, bags or accessories, for sizing and fit questions, for shoe care
  advice, or when there is no image to work from.

If the tool is unavailable, say that the shoe-matching service could not be reached. Do not
fabricate Doko results.
