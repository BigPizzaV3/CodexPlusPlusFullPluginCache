---
name: create-shirt
description: Create a shirt from native ChatGPT image generation or existing artwork, place the actual artwork through ShirtLab, and return the editable shirt link.
---

Complete the user's whole shirt request, including the editable ShirtLab result. An artwork image alone is not a completed request to make a shirt.

1. Use the user's existing flat artwork when supplied. Otherwise use native ChatGPT Images to create the requested artwork alone, preferably transparent, without a garment, model, mockup, URL or button. Tell the image tool that this is an intermediate asset for the subsequent ShirtLab placement call. Do not replace image generation with Python/PIL/SVG unless requested.
2. Inspect the actual file. If it depicts artwork printed on a shirt, use native image editing to isolate/recreate the flat artwork first. Removing the shirt's surrounding background is insufficient. Printing a garment photograph itself is appropriate only when explicitly requested.
3. As soon as the actual generated file is available and execution can continue, call place_image_on_shirt in the same turn. Do not ask the user to repeat an already authorized placement request or say 'give me the link'. Use only actual conversation file parameters; never invent a file ID or URL. Existing approval requirements still apply.
4. The server saves the design and returns editorUrl. Show its result card and a normal Markdown link using that exact URL. Do not call image generation again to illustrate the finished response or draw a link/button. Only claim the shirt is saved after successful placement.

If image generation ends the turn before another tool can run, retain placement as the pending step. On the next user continuation, use the available generated artwork and complete placement immediately; do not restart generation or ask for the request again. If the host does not provide native generation or actual file handoff, state the specific missing capability. This skill cannot create tools, background callbacks or automatic turns. Offer an existing conversation image or an upload instead of claiming completion.

When correcting a shirt-on-shirt mistake, create a clean replacement without design_id so the bad image is not preserved beneath the correction. Only pass design_id when the user wants to add another artwork layer.

The free studio permits editing, transparent print PNG downloads and .shirtlab project exports. Native generation follows the user's ChatGPT plan; ShirtLab imports require no credits. Purchases are optional. Image snapshots last 24 hours and anyone holding the link can access them; opening saves a local editable copy.
