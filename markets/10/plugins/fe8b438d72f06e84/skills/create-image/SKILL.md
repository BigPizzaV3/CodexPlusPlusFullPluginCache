---
name: create-image
description: Create or edit images with RTST (rtst.ai) on the user's account — text-to-image, editing or restyling a photo, variations, grids and several samples, on any RTST image model. Use when the user asks RTST to generate, draw, design, edit or vary a picture, and when an RTST card button asks for a variation, an edit, a different image model, a retry, or to use an image as a reference.
---

# Create an image with RTST

Tools: `get_model`, `list_models`, `estimate_cost`, `generate_image`, `job_status`,
`enhance_prompt`.
Bringing in the user's own image is the `use-my-media` skill.

1. **Pick the model.** If the user named one, call `get_model` with their wording
   (`type: "image"`) and use the exact `name` it returns. If it returns several
   `matches`, take the one the user meant or ask. Otherwise choose one yourself from
   `list_models` (`type: "image"`, no card) by each model's `description` and
   `credit_cost` (`is_free` models suit quick drafts), and tell the user which you
   picked. Call `show_models` only if they ask to see the models. Never invent a model
   name.
2. **Read the model's `params`.** Each image model lists the controls it accepts
   (`key`, `type`, `options` or `min`/`max`). `aspect_ratio`, `resolution`, `quality`
   and similar keys go inside `generate_image`'s `params` under exactly that key,
   using only a listed option. `samples` is its own argument (the model's `max`
   applies). A model that does not list a key does not take it.
3. **Write the prompt.** Expand a terse request into a detailed prompt: subject,
   action, setting, lighting, mood, composition, style; for photographic looks add
   camera, lens and aperture. If the user wants help with wording, `enhance_prompt`
   returns a richer version; show it before using it.
4. **Images in.** Editing or referencing needs hosted https URLs in `image`: the first
   is the image to edit, the rest are references (up to the model's
   `reference_images` max). Get them with `use-my-media`.
5. **Quote when it costs.** For a paid model, `samples` > 1, a grid or a higher tier,
   call `estimate_cost` with `type: "image"` and the same arguments you will generate
   with, and tell the user the credits. If `can_afford` is false, do not submit:
   show `balance` and point to https://rtst.ai/pricing.
6. **Generate** with `generate_image`. Output is private to the user's library; send
   `private: false` only if the user asks to publish it.
7. **Finish the job.** If `state` is `"pending"`: in ChatGPT the card finishes it, so do
   not call `job_status`; elsewhere call `job_status` once with `kind: "image"` and
   `sync: true`. Never resubmit a job that is still running.
8. **Reply.** In ChatGPT a card shows the result: do not repeat the URLs; say which
   model ran, what it cost, and offer a next step (variation, edit, animate with
   `create-video`). Where no card renders (Codex, Claude Code), give the image
   URL(s) and `web_url`.

If a generation is refused for safety, say so and suggest a different prompt; do not
switch models to get around a safety filter. If it failed for credits, show `balance`.

## Messages sent by RTST card buttons

- "Generate another variation of that image with rtst.ai, same style, different
  composition." → same model and prompt, varied composition.
- "Edit the image … with rtst.ai: …" → `image: [that URL]` plus the user's instruction.
- "Use this image as the reference for my next rtst.ai generation: …" → keep the URL for
  the next generation's `image` (or a video's frames, via `create-video`).
- "Use the … (…) image model on rtst.ai for my next image. Ask me for the prompt if
  needed." → use that model (`get_model` for its `params`); ask for the prompt if none
  was given.
- "Retry that rtst.ai generation with an adjusted prompt or a different model." → read
  why it failed first; for a safety refusal change the prompt, not the model.
- "Generate a … with rtst.ai: …" (an empty gallery's Create button) → start here, or in
  `create-video` for a video.
