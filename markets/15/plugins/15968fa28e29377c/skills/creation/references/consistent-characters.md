# Consistent characters in lesson images

Use when the teacher asks for a recurring character, mascot, or cast with the same appearance across a lesson's slides or interactive activities.

## Create a new cast

Describe the character's defining appearance, clothing and illustration style in `additional_instructions`. Ask the lesson generator to establish the cast in the first illustration and use that original as the visual reference for every later scene. Repeat identifying details while changing the scene, action and expression. Use AI images for this request; if the teacher explicitly requested web-only images, resolve the conflict before creating.

This guides generation; a matching name in a prompt alone does not provide reference pixels. Read the completed lesson with `get_resource` and check the image reference metadata before claiming continuity. Report generating or failed images honestly.

## Boundaries

Generated references belong to the same lesson. Do not pass an image ID from another lesson or an arbitrary URL as a character reference. This connection does not import attachments or edit an existing lesson.

Recreating a lesson from its prompt does not preserve visual identity. There is no exposed saved character library or supported cross-lesson import workflow. Do not promise consistent character images across independently generated lessons or printable documents. Explain that limit when the teacher asks for it.
