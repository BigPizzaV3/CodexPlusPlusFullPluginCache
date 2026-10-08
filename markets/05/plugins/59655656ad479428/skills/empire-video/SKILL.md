---
name: empire-video
description: Route one bounded text-to-video or image-guided video request to a current non-OpenAI OpenRouter media model, preview and authorize cost, manage the asynchronous job, validate the MP4, and quarantine it outside the repository while Codex remains in control. Use for video prompts, landing-page loops, image-to-video, reference-guided clips, or an explicit request for Empire video generation.
---

# Empire Video

Generate one video through Empire's shared asynchronous media runtime. Never let
an external renderer write to or execute inside the repository.

## Workflow

1. Resolve the plugin root two directories above this `SKILL.md`, then resolve
   the shared runtime as `$PLUGIN_ROOT/scripts/empire_media.py`. Never resolve
   it relative to the user's current working directory.
2. Preview a short route. Use four seconds when the user gives no duration:

   ```bash
   python3 "$PLUGIN_ROOT/scripts/empire_media.py" video route "PROMPT" \
     --repo "$PWD" --duration 4 --resolution 720p \
     --aspect-ratio 16:9 --no-audio
   ```

   Add only user-requested `--model`, `--duration`, `--resolution`, `--size`,
   `--aspect-ratio`, `--audio`, `--seed`, or `--reference` options. Never
   silently replace a pinned model.
   When the user requests free or Absolute Zero generation, add
   `--cost-mode free` to preview and submission. Stop if no proven zero-cost
   route exists.

   When the user asks for the longest or maximum free duration, list the live
   video catalog first. Collect the published `supported_durations` from
   eligible non-OpenAI models, then preview those durations from longest to
   shortest with `--cost-mode free`. Select the first proven `$0.00` route.
   Do not infer a duration, cross the free lane, or dispatch while searching.

3. Show model and icon, supported output settings, estimate, catalog state, and
   expected asynchronous behavior. Ask for confirmation of the exact route and
   maximum cost unless already explicit in the current request.
4. Submit only after approval:

   ```bash
   python3 "$PLUGIN_ROOT/scripts/empire_media.py" video generate "PROMPT" \
     --repo "$PWD" --duration 4 --resolution 720p \
     --aspect-ratio 16:9 --no-audio \
     --approve-route ROUTE_TOKEN --approve-cost USD
   ```

5. Poll or resume using the returned safe job ID:

   ```bash
   python3 "$PLUGIN_ROOT/scripts/empire_media.py" video status --job JOB_ID
   python3 "$PLUGIN_ROOT/scripts/empire_media.py" video wait \
     --job JOB_ID --timeout 45
   ```

   A bounded wait may return `timed_out` with `resumable: true`. Report that
   state and run a later `status` or another bounded wait; never hide a long
   blocking poll inside one Codex turn.

6. Present the quarantined MP4 or a clickable local-file fallback with model
   chip, job ID, SHA-256, byte size, actual or pending cost, and provenance.
   Promotion into the repository is a separate explicit Codex action.

## Rules

- OpenAI media models are excluded from both automatic and pinned Empire
  routes. Use a native OpenAI video workflow for an explicit OpenAI request.
- OpenRouter video generation is incompatible with enforced ZDR. Report that
  conflict instead of weakening the user's privacy setting.
- Never persist the prompt, reference bytes, signed URLs, or credentials in the
  job record.
- Never download from an arbitrary provider-returned URL. Use the authenticated
  OpenRouter content endpoint for the validated local job ID.
- Timeout means `resumable`, not canceled. Never submit an automatic retry.
- A failed job without provider cost evidence remains `provider_cost_unknown`.
- Treat `--audio` and `--no-audio` as hard requirements. If a model does not
  publish audio-control capability, exclude it instead of claiming the option
  will be honored.
- Interpret natural-language requests such as “use Empire to generate a video”
  as this workflow when the skill is enabled. Preserve every stated modality,
  duration, aspect-ratio, audio, model, and cost constraint.
- Never autoplay or execute downloaded content.
