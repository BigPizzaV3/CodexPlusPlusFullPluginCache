---
name: empire-image
description: Route one bounded image-generation or image-edit request to a current non-OpenAI OpenRouter media endpoint, preview and authorize its cost, validate the returned image, and quarantine it outside the repository while Codex remains in control. Use for image prompts, icons, illustrations, transparent assets, image variations, reference-image edits, or an explicit request for Empire image generation.
---

# Empire Image

Generate one image through Empire's shared media runtime. Never let an external
renderer write to the repository.

## Workflow

1. Resolve the plugin root two directories above this `SKILL.md`, then resolve
   the shared runtime as `$PLUGIN_ROOT/scripts/empire_media.py`. Never resolve
   it relative to the user's current working directory.
2. Preview the route before generation:

   ```bash
   python3 "$PLUGIN_ROOT/scripts/empire_media.py" image route "PROMPT" \
     --repo "$PWD"
   ```

   Add only user-requested options such as `--model`, `--size`,
   `--aspect-ratio`, `--quality`, `--output-format`, `--background`, `--n`,
   `--seed`, or `--reference`. Never silently replace a pinned model.
   When the user says free, zero-cost, or Absolute Zero, add
   `--cost-mode free` to both preview and generation. If no proven zero-cost
   endpoint exists, stop; never substitute a paid image route.

3. Show the selected model and icon, exact endpoint provider, supported
   parameters, estimate, catalog state, and warnings. If the user has not
   approved this exact route and maximum cost in the current request, ask for
   confirmation. Do not invent a cost ceiling.
4. Generate only after approval, passing the returned `approval_token` and the
   approved maximum:

   ```bash
   python3 "$PLUGIN_ROOT/scripts/empire_media.py" image generate "PROMPT" \
     --repo "$PWD" --approve-route ROUTE_TOKEN --approve-cost USD
   ```

5. Present the returned local image as a quarantined artifact. Include its
   model chip, provider, SHA-256, byte size, actual cost, approved maximum, and
   text fallback. Do not use raw HTML.
6. Promote it into the repository only in a separate, explicit Codex action.
   Regeneration is a new paid request and requires a new route preview.

## Rules

- OpenAI media models are excluded from both automatic and pinned Empire
  routes because Codex is already the OpenAI lead. If the user explicitly
  requests an OpenAI media model, use the native OpenAI image workflow rather
  than representing it as an Empire contribution.
- Send only the prompt and explicitly selected reference images.
- Never expose keys, raw base64, or provider request bodies.
- Keep provider output advisory and outside the repository.
- If route or price changes, preview again before calling the provider.
- Treat free image understanding and free image input as distinct from free
  image generation. Only an endpoint with a calculated `$0.00` output cost
  satisfies `--cost-mode free`.
- Interpret natural-language requests such as “use Empire to generate an
  image” as this workflow when the skill is enabled. Preserve every stated
  aspect-ratio, format, model, reference, and cost constraint.
- If generation outcome is unknown, report the pending reservation; do not
  claim zero cost or automatically retry.
- If the image does not render in the active Codex surface, provide the local
  clickable file path and compact text provenance.
