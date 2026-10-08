# Create a Google Flow Video

Create the approved visual story as a still image first, then offer a copy-ready Google Flow image-to-video prompt. Do not create a CTA, CTA text, phone number, button, sales ending, or marketing-poster layout anywhere in this workflow.

Follow the stages in order. Ask only one question in each message.

## Stage 1 — Select the hook

Use the confirmed business profile and video goal. If the topic, product, offer, or occasion is essential but unclear, ask for that one detail first.

Read and apply [ddd-hooks.md](ddd-hooks.md). Suggest exactly three business-specific hooks and ask the user to select 1, 2, or 3. Do not create the visual story yet.

## Stage 2 — Create the visual story

Turn the selected hook into one cinematic scene. Describe the action inside the image, not a poster layout. Include:

- Person or main subject
- Emotion
- Environment
- Lighting
- Camera angle and framing
- Background
- Key action or moment

Do not include CTA copy, phone numbers, buttons, text overlays, typography, logos, poster layout, or an ending sales frame.

After showing the visual story, ask only:

> **Do you approve this visual story?**
>
> 1. Yes, create the visual
> 2. Create another visual story

If the user selects 2, create one meaningfully different visual story for the same approved hook and ask for approval again. Do not generate an image until the user selects 1.

## Stage 3 — Create the approved visual

Use the available image-generation capability to create the approved visual story as a high-quality cinematic still image. The image is the starting frame/reference image for Google Flow, even if the user casually calls it a poster.

- Preserve supplied brand, product, character, and reference-image details.
- Keep the composition clean and suitable for animation.
- Do not add CTA, phone number, button, headline, caption, logo, text overlay, poster layout, or sales message.
- If image generation is unavailable, explain that plainly and provide the final visual-generation prompt instead. Do not pretend an image was created.

After delivering the image, ask only:

> **Do you want the video prompt for Google Flow?**

## Stage 4 — Create the Google Flow prompt

If the user says yes:

1. Tell them in normal readable text: **Upload the visual created above to Google Flow as the starting image, then paste the prompt below.**
2. Put only the video-generation prompt inside one fenced code block so it is easy to copy.
3. Make the prompt self-contained and specify:
   - Subject movement and facial expression
   - Natural environmental motion
   - Camera movement
   - Lighting continuity
   - Realistic physics and temporal consistency
   - Scene pacing and approximate duration when useful
   - What must remain unchanged from the uploaded image
4. State inside the prompt: no CTA, no text overlays, no phone number, no button, no logo reveal, and no added objects or claims.
5. Do not place setup instructions inside the code block.

After the code block, give up to three short readable instructions for using it, then show the main menu. If the user says no, show the main menu.
