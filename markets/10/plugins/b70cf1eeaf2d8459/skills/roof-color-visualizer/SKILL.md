---
name: roof-color-visualizer
description: >-
  Open GetRoofReport's roof color visualizer and shingle color visualizer to try
  roof colors on a house photo, or browse shingle catalog examples by brand,
  product line, and color. Use for "Show my house with a brown roof" or "Compare
  GAF Timberline HDZ Charcoal with Owens Corning Duration Onyx Black." House photos
  are uploaded inside the visualizer; catalog images are product examples.
---

# Roof colors

Call `preview_roof_color`. Use optional `brand`, `line`, and `color` filters
for catalog searches. They do not preselect products in the photo visualizer.
Open the visualizer without requiring an address lookup or a Florida address.

The user uploads their house photo inside the visualizer. The tool does not
accept a photo argument. Show the interactive view when supported; otherwise
offer the returned `visualizerUrl`. Claude currently uses catalog previews
and links to the website because its nested frames need host review.

Label catalog photos as examples of the returned brand, line, and color.
Do not present an example house as a transformed photo of the user's house.
When a requested product has no catalog match, say so and offer the visualizer.
