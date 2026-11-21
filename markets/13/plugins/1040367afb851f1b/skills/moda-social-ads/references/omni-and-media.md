# Image generation within designs

Generate imagery wherever it elevates the design. Report the usage receipt as information. A billing rejection means the team is out of credits or capped: surface the hint and stop; do not retry it.

## Images inside a design (metered unless marked FREE)

Create the layout and an ordinary image-capable shape first. Then call:

```json
{"canvas_ref":"cvs_…","node":"[id canvas_apply_markup returned, or from canvas_read]","operation":{"kind":"generate","prompt":"[complete image instruction]","model":"nano-banana-lite"}}
```

Use `canvas_edit_image` with this object. It fills that shape; it never returns a standalone image. The call waits for placement. On complete, inspect with `canvas_screenshot`. If it returns working, repeat the identical call to wait on the same job; `task_status` is an optional recovery check. Other shapes, typography, masks and layout stay editable. For an existing image use operation.kind=`edit`, `outpaint`, `upscale`, or `remove_background`. Edit/transform reads its source from the target; generate can take operation.reference_images. Use one target per call.

Ordinary `media_remove_background(image)` performs matting on an existing image. Generative high-quality cutout belongs to `canvas_edit_image` with operation.kind=`remove_background` and high_quality=true. Start with standard matting: generative isolation can drop secondary foreground elements, so compare results.

`media_fetch_logo(domains=["example.com"])` retrieves existing company marks for FREE. Verify the echoed brand and license for the intended use. `media_video_frames` inspects existing team video for FREE. Audio/video generation, reframe and video upscale are unavailable on this connector.

Outpaint continues the existing frame without a prompt. Supply operation.aspect_ratio OR per-side expand_top/bottom/left/right, never both. Limits remain 2048px per side and 4MP expanded canvas. Price counts source and result. Upscale takes scale=2 or 4.

Identical requests resume the same operation, even after completion; a fresh repeat_token requests another variation for a new charge. Resuming and placement recovery bypass the generation rate limit. If placement fails, use operation.kind=retry_placement with task_ref and the original or a replacement node on the same canvas; omit repeat_token. Active or completed placements cannot be redirected. A target changed by another editor produces a conflict, never a silent overwrite. quote=true preflights without generation.

### Choosing an image model

Model strengths are shared across Moda surfaces. The model defaults to the standard image model; choose an explicit model for a particular strength. The live capability cards appended to this guide define accepted ratios, resolutions and model_params. Copy them exactly.

<!-- generated: image-model roster. Authored in backend/app/services/media/image/ (label + roster_line, falling back to description); regenerate with: uv run python -m scripts.render_model_roster -->
- **NanoBanana 2 Lite** — Fastest, lowest-cost baseline; the default when nothing else is demanded.
- **NanoBanana 2.1** — The balanced Gemini tier — better than Lite for everyday work, well short of Pro's price.
- **NanoBanana Pro** — The Gemini premium tier for the most complex, high-fidelity briefs, and the dearest of the three.
- **GPT Image 2.0** — Strong in-image text rendering.
- **Ideogram V4** — Crisp posters, logos and accurate in-image text. Billed by megapixel rather than per call, so cost tracks output size.
- **FLUX.2 Pro** — The FLUX.2 workhorse: general-purpose quality with multi-reference editing, at the family's lowest price.
- **FLUX.2 Flex** — The only image model with sampler control: guidance scale and inference steps.
- **FLUX.2 Max** — The FLUX.2 family's top tier for realism and precision, and its dearest at ordinary sizes.
- **Seedream V5 Lite** — The Seedream workhorse: full-size output at the family's lowest price.
- **Seedream V5 Pro** — More detail per pixel than Lite, but a smaller maximum size; pick Lite for large canvases.
- **Recraft V3** — Style-rich design generation and single-image editing; vector styles cost 2x.
- **Seedream 4.5** — The previous Seedream generation, kept for its own look rather than its size.
- **Recraft V4.1** — Design-first raster artwork for production — the entry Recraft V4.1 tier.
- **Recraft V4.1 Pro** — Recraft V4.1 for hero imagery, campaigns and print, at six times the entry tier's price.
- **Recraft V4.1 Utility** — A faster, lighter Recraft V4.1 for high-volume work, at the entry tier's price.
- **Recraft V4.1 Utility Pro** — Pro-grade Recraft output on the faster Utility runtime, at Pro's price.
- **Recraft V4.1 Vector** — Editable SVG output — logos, icons, and illustration systems.
- **Recraft V4.1 Pro Vector** — Large-format editable SVG for detailed professional illustration — Recraft's top vector tier, and its dearest route.
- **Grok Imagine** — Cheap generation and multi-image editing — the entry Grok tier.
- **Grok Imagine 2.0** — The current Grok generation, priced on both quality and resolution.
- **Grok Imagine Pro** — The quality tier of Grok v1 — the same surface, dearer output.
- **Kling Image V3** — Kling's image line at one flat rate, with single-image editing.
- **Kling Image O3** — The 4K Kling line, with a multi-image edit list; 4K costs double.
- **Ideogram 4.5** — Ideogram's newest model: strong typography, and edits that follow a source image. Flat per image at any size, priced by quality.
<!-- /generated: image-model roster -->

### Image rules

- Your `prompt` goes to the model VERBATIM — nothing is added or rewritten. Write the complete instruction: subject, style, composition, and (for edits) exactly what to preserve.
- Aspect ratio / resolution / model params are per-model enums — copy values exactly from the model's capability line; an unlisted ratio fails the call rather than snapping.
- Source images are modified/preserved content; reference images guide style, palette, or composition. Here the source is the target's current image; references go in operation.reference_images.
- Sources and references share an unlabeled provider channel. Specify what to preserve versus change and inspect for unintended copying. Text or marks intrinsic to a depicted object belong in the image prompt.
- Preserve exact typography and logos as editable layers; generate the imagery that supports them.
- Look at the result with your own vision before describing it. Refine the prompt or change model when it misses.





## Imagery is a default quality lever

Generated imagery is a DEFAULT quality lever, not a last resort. Covers, heroes, section breaks, and full-bleed closers get generated imagery wherever it elevates the design — styled to the brand's palette and mood. Reuse brand-kit assets and the user's own uploads (`file_search` / the `upload` tool) when they are the actual subject matter; `file_search(query, source='stock')` adds stock photography (place the `stock_unsplash_…` id verbatim; credit the result's `attribution` wherever the photo appears); markup `<image icon="query"/>` covers functional UI icons; an icon/vector-only system is a deliberate style choice, never a cost fallback.
