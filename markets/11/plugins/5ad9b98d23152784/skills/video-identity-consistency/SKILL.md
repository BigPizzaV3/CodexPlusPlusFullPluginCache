---
name: video-identity-consistency
description: "When a character or product must stay recognizable across shots, use its references or established visual traits and the model's reference controls to set stable identity anchors and continuity guidance. Not needed when no character or product recurs across shots or clips."
metadata:
  version: skill-render-ea6bd93365667f6d
---

# Identity across shots

First use the mechanisms the chosen model offers: references, elements, start frames or
identity controls. Text descriptions of the subject's traits supplement this contract where
they help the model hold the subject.

A reference keeps a subject recognizable, not identical. When the user needs the exact pet,
product or person from a photo, start the video from a frame that already contains the subject
and was approved as an image: the frame-first path in `footage-transformation-vfx`.

## Visual anchors

Choose a few traits that truly distinguish the subject: shape, colour, material, texture,
clothing, hardware, logo or a characteristic detail. Repeat them in the same stable wording
from shot to shot when the model's prompting guide recommends text anchoring.

For a product from a reference, take the traits from the asset and keep the user's requirements
for shape, colour, texture and markings. For a character, keep only the traits that matter for
the request and are supported by the available references.

## Series coherence

Keep the chosen style core (light, palette, lens character and camera motion) consistent
exactly as far as the series needs. Change the action, setting or angle according to the plan
while keeping the subject's recognizable anchors.
