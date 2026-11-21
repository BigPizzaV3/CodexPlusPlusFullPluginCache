---
name: generate-image
description: Generate images with AI (SelfyzAI / selfyz.ai), supporting text-to-image and image-to-image. Use when the user wants to generate an image, turn a photo into a certain style, change a photo's background/outfit/art style, says text-to-image / image-to-image / AI drawing, or asks which image-generation models are supported, how many credits they cost, or what resolution they can produce. The output is images; to generate videos, use the selfyz-ai:image-to-video, selfyz-ai:first-end-frame-video, or selfyz-ai:text-to-video skills instead. The entire flow is completed through the selfyz-ai MCP service.
---

# AI Image Generation

Call selfyz.ai's image-generation capability through the `selfyz-ai` MCP service: provide a prompt,
and optionally several input images, to generate images. **The same `any2i_*` tool set covers both
text-to-image and image-to-image**--with no input images it is text-to-image; with input images it is
image-to-image. Whether a model needs images, and how many, is determined entirely by that model's
own configuration.

## Service binding

All capabilities in this skill come from the single `selfyz-ai` MCP server and **must not be replaced**:

- Its tool namespace in Codex is **`mcp__selfyz_ai`**--Codex normalizes `-` in server names to `_`, and
  tool names do not carry a prefix. Every tool name below (such as `get_user_profile`) refers to the
  tool of the same name under the `mcp__selfyz_ai` namespace.
- **If the `mcp__selfyz_ai` namespace is not visible, the first judgment is "not logged in", not "plugin
  not installed"**: an MCP server that has not completed OAuth will not register its entire namespace.
  In this case, run `codex mcp login selfyz-ai` yourself (not the user), extract the plain `https://`
  authorization URL it prints, and give the user only that link to click -- do not lead with the
  `codex://mcp/login?server=selfyz-ai` deep link, since it silently does nothing unless the client has
  registered the `codex://` protocol handler. See `references/auth.md` for the full procedure, and
  explain that after login they must open a new conversation for it to take effect.
- **Under no circumstances may you substitute another brand's MCP** (`mcp__enkio` and
  `mcp__selfyz_ai` are two services, two accounts, and two credit pools; cross-use will really charge the
  wrong account). Do not mix in a `task_id` / `job_id`, credit balance, or artifact URL obtained
  elsewhere.
- When you need to explain which service this skill is connected to, rely on the `brand` /
  `brand_website` returned by `get_user_profile` and the value of `mcpServers.selfyz-ai.url` in this
  plugin's `.mcp.json`; do not answer from memory or guesswork. If `brand` is not SelfyzAI, stop
  immediately and report the error.

Tasks are **asynchronous**: `any2i_create_task` returns a `job_id` immediately, and you must poll
`any2i_get_task` yourself.

```
0 Log in/check balance -> 1 Choose model -> 2 Set quality and quote (confirm before charging)
-> 3 Only with input images: crop locally -> 4 Only with input images: upload each image to get URLs
-> 5 Create task (charges credits) -> 6 Poll -> 7 Download, preview, and deliver
```

## Hard constraints

- **Image generation and video generation use separate tool groups, and their tools are
  not interchangeable**. The image-generation task identifier is **`job_id`** (not the video's
  `task_id`), and the result is an **`image_urls` array** (not a single `video_url`). Always poll
  with `any2i_get_task`; a video query tool returns no `image_urls`.
- **Creating a task charges credits; before submitting, you must explain the cost to the user and get
  explicit confirmation**. All query tools are free.
- **`prompt` is required**. An empty prompt, or one containing only whitespace, will be rejected
  directly.
- **The number of input images is decided by the model**: `any2i_get_options` returns
  `image_count = { min, max }`. `min` equal to 0 means images may be omitted (text-to-image);
  `max` equal to 0 means the model **does not accept input images at all**, and forcing them in will
  be rejected. Any count outside the interval is rejected.
- **Credits vary only with quality**, not with aspect ratio, number of input images, or prompt
  length. Therefore, within the image-count limit, adding another image or writing a longer prompt is
  "free".
- **When there are input images, every image must be cropped to the target ratio before uploading**.
  The crop specification comes from `crop` in `any2i_get_options`; **the server does not accept image
  binaries, and cropping is done locally**. When `ratio` is `free`, no cropping is needed.
- **Do not construct or guess `user_id`, `example`, signatures, or similar parameters**. The server
  already handles them, and they do not exist in the tool inputs.
- The allowed values for `quality` / `ratio` **must come from `any2i_list_models`**.
- Polling cadence: once every 5 seconds, with a limit of about 5 minutes. Image generation is usually
  much faster than video generation, but still give the user brief progress updates; do not wait
  silently for a long time.
- When a task's `job_status` is `fail`, do not blindly retry. Tell the user the `job_reason`
  first, then ask whether to retry or give up. Retrying re-submits the task at the normal
  price--failed credits are refunded automatically, and this billing rule was already disclosed
  when quoting the cost, so no new price confirmation is needed here.
- **Before showing images, you must download them locally first**. Pasting a remote URL directly
  cannot preview it; see "Displaying artifacts".

## How to write prompts

**Text-to-image** (no input images): the model has no visual reference, so describe the image
clearly--subject + action/pose + scene + composition/viewpoint + lighting/style.

```
✅ A corgi wearing sunglasses sits on a vintage motorcycle, afternoon backlight, film grain, shallow-depth-of-field close-up
❌ A dog                                <- The scene, style, and composition are all left for the model to guess
```

**Image-to-image** (with input images): the prompt describes **what you want this image to become**.
You do not need to repeat what is already in the image; focus on "what to change and what to keep".

```
✅ Replace the background with snowy mountains, keep the person and clothing unchanged, and make the overall tone cool
✅ Convert it to a watercolor illustration style while preserving the original composition
❌ A person standing in front of snowy mountains                        <- It does not say whether to "modify" or "redraw", so original-image features are easily lost
```

When there are multiple input images, refer to them in natural language by submission order ("the
person in the first image", "the clothing in the second image"). **Do not use reference syntax such
as `@1` or `{img1}`**; the upstream does not support it and will treat it as plain text.

Do not exceed `prompt_limit_length`. The model's `prompt_hint` is upstream guidance on writing
prompts, and `prompt_guide_url` is the upstream prompt guide page. You may paraphrase them to the
user, but do not open the page on the user's behalf.

## Displaying artifacts

The finished images are **temporary remote URLs** from SelfyzAI. Codex **cannot embed-preview media
files from these domains**, and users cannot open a bare pasted URL.

Use a per-task isolated working directory (so the user's repository is not polluted):

```bash
WORKDIR="${TMPDIR:-/tmp}/selfyz-ai-any2i/<job_id>"
mkdir -p "$WORKDIR"
curl -sS -L -o "$WORKDIR/result1.png" "<image_urls[0]>"
```

`image_urls` may contain multiple images; **download every image** and name them in order. Images can
be shown directly to the user, and the original remote URLs should be included as well so the user can
save them manually. If download fails (non-200 / empty file), clearly say "preview download failed"
and provide the remote URL; do not falsely claim it has been displayed.

## Step 0: Confirm service binding, login, and credit balance

**First confirm that the `mcp__selfyz_ai` namespace exists.** If it does not exist, do not continue and
do not switch to another MCP. Tell the user that `selfyz-ai` is not logged in, then run
`codex mcp login selfyz-ai` yourself, extract the plain `https://` authorization URL from its output, and
hand the user only that link to click (do not lead with the unreliable
`codex://mcp/login?server=selfyz-ai` deep link). See `references/auth.md` for details, and explain that
**after login they must open a new Codex conversation** for it to take effect (the tool table in the
current conversation will not hot-refresh).

After the namespace is ready, call `get_user_profile()`:

- **Returns 401 / not logged in**: the token is invalid. Run `codex mcp logout selfyz-ai` then
  `codex mcp login selfyz-ai` yourself, relay the newly printed `https://` login URL to the user the same
  way as above (not the `codex://` deep link), and again they need to open a new conversation. See
  `references/auth.md`.
- Validate that the returned `brand` must be **SelfyzAI**; otherwise the call is connected to the wrong
  service. Stop immediately and tell the user.

The returned `credit` is the current credit balance. Record it and compare it with the estimated cost
when quoting in step 2.

**Membership check (required).** Creating tasks with `any2i_create_task` is available to accounts
with an active membership. If `get_user_profile()` returns an `is_member` value other than `true`,
stop here: tell the user that this feature is not included in their current account, so no task
will be created and no credits will be used. Do not continue with model selection, uploads,
quoting, or task creation. Keep it factual and do not steer the user toward any plan; only if the
user asks about plans, call `get_pricing_url` (when that tool is
available) and share the returned informational `pricing_url`.
If the user later says their account status has changed, call `get_user_profile()` again and
continue only when `is_member` is `true`.

## Step 1: Choose a model

```
any2i_list_models()
-> { count, models: [ { model, model_name, model_desc, qualities, ratios, default_ratio,
                       min_image_count, max_image_count, accepts_images, requires_images,
                       prompt_limit_length, prompt_hint, prompt_guide_url,
                       credits: [{ quality, quality_display, credit }] } ] }
```

`models[].model` is the model identifier; use it for all subsequent calls.

**First filter models based on whether the user has images**:
- User only provided text -> choose a model with `min_image_count == 0`
- User provided images to modify -> choose a model with `accepts_images == true` whose count interval
  can accommodate the number of images

Briefly list the available models for the user, including each model's supported qualities, ratios,
and required number of images. If the user has no preference, choose the default quality from
`credits` with a reasonable cost-performance tradeoff and explain why.

## Step 2: Set quality and quote

```
any2i_get_options(model, quality?, ratio?)
-> { model, model_name, quality, ratio, credit_cost,
    image_count: { min, max }, accepts_images, requires_images, crop,
    prompt_required, prompt_limit_length, prompt_hint, prompt_guide_url }
```

If parameters are omitted, they fall back to the model defaults, and the response clearly states the
final effective values.

**Tell the user both `credit_cost` and the `credit` balance from step 0, then wait for
confirmation**. If the balance is insufficient, tell the user the required credits and the current balance (see references/credits.md); do not force submission. Quality is the only
dimension that affects credits, so if the user thinks it is expensive, suggest lowering quality
first.

## Step 3: Crop input images locally (skip if there are no input images)

The `crop` field gives the target ratio and pixel dimensions:

```
crop = { ratio, crop_required, target_width, target_height, strategy, hint }
```

When `crop_required` is `false` (the ratio is `free`), skip this step and upload the original images
directly. Otherwise, **every input image** must first be center-cropped to the target aspect ratio and
then scaled to `target_width × target_height`:

```bash
W=<target_width>; H=<target_height>
i=1
for SRC in "<input image 1>" "<input image 2>"; do
  ffmpeg -y -i "$SRC" \
    -vf "crop='min(iw,ih*$W/$H)':'min(ih,iw*$H/$W)',scale=$W:$H" \
    "$WORKDIR/src$i.jpg"
  i=$((i+1))
done
```

If ffmpeg is unavailable, use the macOS built-in `sips` (note that `--cropToHeightWidth` is **height
first, then width**):

```bash
cp "<input image 1>" "$WORKDIR/src1.jpg"
sips --cropToHeightWidth "$H" "$W" "$WORKDIR/src1.jpg" >/dev/null
sips --resampleHeightWidth "$H" "$W" "$WORKDIR/src1.jpg" >/dev/null
```

After cropping, confirm that every output file exists and has the correct dimensions
(`sips -g pixelWidth -g pixelHeight`) before moving on. **Keep the order unchanged**; it is the order
of `image_urls` when submitting.

## Step 4: Upload each image to get URLs (skip if there are no input images)

The upload endpoint accepts only one file per request, so **call `create_upload_url` separately for
every image**:

```
create_upload_url() -> { upload_url, headers }
```

```bash
curl -sS -X POST "<upload_url>" -F "file=@$WORKDIR/src1.jpg" -H "X-Client-Sn: <value from headers>"
# -> {"c":200,"m":"Success","d":"https://.../src1.jpg"}
```

The `d` in the response is the image URL. `c != 200` means failure; report `m` to the user.
**Collect these URLs in order**. Uploaded files are **temporary storage and are cleaned up
periodically**; after getting the URLs, submit the task as soon as possible.

## Step 5: Create the task (charges credits)

```
any2i_create_task(model, prompt, image_urls?, quality?, ratio?)
-> { job_id, job_status, model, image_count, quality, ratio, credit_cost }
```

- `prompt` is **required**; see "How to write prompts".
- Do **not pass** `image_urls` for text-to-image; for image-to-image, pass them in order, and ensure
  the count falls within the `image_count` interval from step 2.
- `ratio` must **match** the ratio used for cropping in step 3.
- `quality` must match what was confirmed during the step-2 quote; otherwise the actual charge will
  not match the quote.

## Step 6: Poll

```
any2i_get_task(job_id) -> { job_status, job_reason, image_urls, image_count, finished }
```

Note that the input parameter name is **`job_id`**, not `task_id`.

- `job_status == "success"`: `image_urls` are the finished images; proceed to step 7.
- `job_status == "fail"`: pass `job_reason` to the user and ask whether to adjust the prompt
  and retry or give up. Retrying re-bills at the normal price (failed credits are refunded
  automatically); this was already disclosed up front, so you do not need to reconfirm the
  price.
- Other values: queued or generating; wait 5 seconds and check again, with a brief progress update to
  the user.

## Step 7: Download and deliver

Following "Displaying artifacts", download **every image** in `image_urls` to `$WORKDIR`, show them
to the user, and provide the local paths + original URLs. Remind the user: remote links point to
temporary storage and will be cleaned up; local files under the system temporary directory may also be
reclaimed by the system, so they should save the images to their own directory as soon as possible.

It is normal for the same prompt to generate different results each time. If the user is unhappy,
first suggest **making the prompt more specific** rather than directly switching models and retrying.

## Error handling

For login, connection, and service-binding issues, see `references/auth.md` (**when not logged in, the
entire MCP namespace will not appear**; do not misjudge this as the plugin not being installed, and
especially do not switch to another brand's MCP). See `references/errors.md` for common error codes
and handling; `references/credits.md` for credits and billing rules; and `references/workflow.md` for
the return-field structures of each tool.
