---
name: reference-to-video
description: Generate AI videos from multiple reference images (Enkio / enkiomv.ai). Use when the user wants to combine several images into a video, use one person image plus one clothing/scene/object image to make a video, create reference-image-to-video / multi-image-to-video / reference video, or asks how many images, how many credits, or which models are supported for reference-image-to-video. If the user only wants to animate a single image, use the enkio:image-to-video skill instead; if the user wants a fixed first-frame + end-frame transition, use the enkio:first-end-frame-video skill instead. The entire workflow is completed through the enkio MCP service.
---

# Reference-Image-to-Video

Use the `enkio` MCP service to call enkiomv.ai's reference-image-to-video capability: provide several
**reference images** plus a **prompt**, and the model synthesizes the people, clothing, scenes, objects,
and other elements from those reference images to generate a brand-new video.

## Service Binding

All capabilities in this skill come from the single `enkio` MCP server, and **it must not be replaced**:

- Its tool namespace in Codex is **`mcp__enkio`**--Codex normalizes `-` in server names to `_`, and tool
  names have no prefix. Every tool name mentioned below (such as `get_user_profile`) refers to the tool of
  the same name under the `mcp__enkio` namespace.
- **If the `mcp__enkio` namespace is not visible, the first judgment is "not logged in", not "plugin
  not installed"**: an MCP server that has not completed OAuth will not register its entire namespace.
  In this case, run `codex mcp login enkio` yourself (not the user), extract the plain `https://`
  authorization URL it prints, and give the user only that link to click -- do not lead with the
  `codex://mcp/login?server=enkio` deep link, since it silently does nothing unless the client has
  registered the `codex://` protocol handler. See `references/auth.md` for the full procedure, and
  explain that after login they must open a new conversation for it to take effect.
- **Never substitute another brand's MCP under any circumstances** (`mcp__selfyz_ai` and `mcp__enkio` are
  two separate services, two accounts, and two credit pools; cross-use will charge real credits on the wrong
  account). Also do not mix in a `task_id` / `job_id`, credit balance, or artifact URL obtained elsewhere.
- When you need to explain which service this skill is connected to, use the `brand` / `brand_website`
  returned by `get_user_profile` and the value of `mcpServers.enkio.url` in this plugin's `.mcp.json`;
  do not answer from memory or guesswork. If `brand` is not Enkio, stop immediately and report an error.

The essential difference from `enkio:image-to-video`: single-image-to-video **animates this image**, while
reference-image-to-video **uses these images as references to redraw a video**. The frame does not need
to match any input image exactly.

Tasks are **asynchronous**: `i2v_create_task` returns `task_id` immediately, and you must poll
`i2v_get_task` yourself.

```
0 Log in/check balance -> 1 Choose model (kind=reference) -> 2 Set parameters, image count, and quote (confirm before charging)
-> 3 Crop each reference image locally -> 4 Upload each image to get URLs -> 5 Create task (charges credits)
-> 6 Poll -> 7 Download, display, and deliver
```

## Hard Constraints

- **Every `i2v_*` call in this skill must include `kind="reference"`**. Reference-image-to-video and
  image-to-video use completely different model lists. If `kind` is omitted, you will get image-to-video
  models, and submission will fail with "nonexistent reference-image-to-video model".
- **Creating a task charges credits; before submitting, you must explain the cost to the user and obtain
  explicit confirmation**. All query tools are free.
- **The number of reference images is determined by the model**: `i2v_get_options` returns
  `image_count = { min, max }`; fewer than `min` or more than `max` will be rejected directly by the
  server. The maximum is 3 images.
- **`prompt` is required**, and it is the core input for this mode--reference images only provide material;
  the prompt must clearly state how the frame should combine them. Empty or whitespace-only prompts
  will be rejected directly.
- **Refer to reference images in natural language in the prompt; do not use reference syntax such as
  `@1` or `{img1}`**. The upstream service does not support it and will treat it as ordinary text.
  See "How to Write Prompts" below for the correct style.
- **Each reference image must be cropped to the target ratio before upload**. The cropping specification
  comes from `crop` in `i2v_get_options`, and **the server does not accept image binaries; cropping is
  done locally**.
- **Do not construct or guess parameters such as `user_id`, `example`, or signatures**. The server already
  handles them, and they do not exist in the tool inputs.
- The allowed values for `quality` / `duration` / `mode` **must come from
  `i2v_list_models(kind="reference")`**.
- Reference-image-to-video **does not have a fixed first/end frame mode**; passing `end_frame=true` will
  fail directly.
- Polling cadence: once every 10 seconds, with an upper limit of about 15 minutes. During that time,
  briefly tell the user progress; do not wait silently for a long time.
- When the task `task_status` is `fail`, do not retry blindly. First tell the user the
  `task_reason`, then ask what to do. Retrying re-submits the task at the normal price--failed
  credits are refunded automatically, and this billing rule was already disclosed when quoting
  the cost, so no new price confirmation is needed here.
- **Before showing the video, you must download it locally first**. A remote URL cannot be previewed
  directly; see "Displaying the Artifact".

## How to Write Prompts

Reference images correspond to "reference image 1 / 2 / 3" **in submission order**; the order itself is
semantic. In the prompt, use natural language to describe what role each image plays, how they combine,
and what happens in the frame.

Recommended practice: first confirm with the user what each image is (person? clothing? scene? object?
style?), then write that information into the prompt.

```
✅ The girl in the first image wears the red dress from the second image and slowly walks on the seaside
   wooden boardwalk in the third image, backlit by sunset, with the camera slowly panning right
✅ Let the cat from image one sit on the sofa from image two and yawn, warm indoor lighting, static camera
❌ @1 wears @2 and walks in @3               <- Reference syntax is not supported
❌ Generate a nice-looking video             <- Does not clarify the relationship between the reference images
```

Do not exceed `prompt_limit_length`. The model's `prompt_hint` is upstream guidance on prompt writing;
`prompt_guide_url` is the upstream prompt guide page. You may paraphrase them for the user, but do not
open the page on the user's behalf.

## Displaying the Artifact

The finished video is an Enkio **temporary remote URL**. Codex **cannot embed-preview media files from
these domains**; if you paste the URL directly, the user cannot open it.

Use a task-isolated working directory by convention (do not pollute the user's repository):

```bash
WORKDIR="${TMPDIR:-/tmp}/enkio-r2v/<task_id>"
mkdir -p "$WORKDIR"
curl -sS -L -o "$WORKDIR/result.mp4" "<video_url>"
```

Videos cannot be embedded for display. Provide the local absolute path, and also include the original
remote URL so the user can save it themselves. If download fails (non-200 / empty file), clearly state
"preview download failed" and provide the remote URL; do not falsely claim it was displayed.

## Step 0: Confirm Service Binding, Login, and Credit Balance

**First confirm that the `mcp__enkio` namespace exists.** If it does not exist, do not continue and
do not switch to another MCP. Tell the user that `enkio` is not logged in, then run
`codex mcp login enkio` yourself, extract the plain `https://` authorization URL from its output, and
hand the user only that link to click (do not lead with the unreliable
`codex://mcp/login?server=enkio` deep link). See `references/auth.md` for details, and explain that
**after login they must open a new Codex conversation** for it to take effect (the tool table in the
current conversation will not hot-refresh).

After the namespace is ready, call `get_user_profile()`:

- **Returns 401 / not logged in**: the token is invalid. Run `codex mcp logout enkio` then
  `codex mcp login enkio` yourself, relay the newly printed `https://` login URL to the user the same
  way as above (not the `codex://` deep link), and again they need to open a new conversation. See
  `references/auth.md`.
- Verify that the returned `brand` must be **Enkio**; if not, it means the call is connected to the wrong
  service. Stop immediately and tell the user.

The returned `credit` is the current credit balance. Record it so you can compare it with the estimated
cost in Step 2.

**Membership check (required).** Creating tasks with `i2v_create_task` requires an active membership. If
`get_user_profile()` returns an `is_member` value other than `true`, stop here: call `get_pricing_url`
and give the user the returned `pricing_url` to open in a browser, signed in with the same Wondershare
account used to authorize this MCP, to purchase a membership. Do not continue with model selection,
uploads, quoting, or task creation; after the user says the purchase is complete, call
`get_user_profile()` again and continue only when `is_member` is `true`.

## Step 1: Choose a Model

```
i2v_list_models(kind="reference")
-> { kind, count, models: [ { model, model_name, model_desc, qualities, durations_sec,
                              modes, ratios, default_ratio, movement_amplitudes,
                              min_image_count, max_image_count,
                              prompt_limit_length, prompt_hint, prompt_guide_url,
                              combinations, ... } ] }
```

`models[].model` is the model identifier; use it in all subsequent calls. Briefly list the available
models for the user, including each model's supported resolutions, durations, modes, and **how many
reference images it needs**, and let the user choose. If the user has no preference, choose a cost-effective
default combination from `combinations` and explain why.

`combinations` directly gives the credit cost for each "mode + quality + duration" combination. Prefer it
when choosing parameters.

## Step 2: Set Parameters, Image Count, and Quote

```
i2v_get_options(model, kind="reference", quality?, duration?, mode?, ratio?)
-> { kind, quality, duration_sec, mode, ratio, credit_cost,
    image_count: { min, max }, image_role, crop,
    prompt_required, prompt_limit_length, prompt_hint, prompt_guide_url }
```

If parameters are omitted, they fall back to model defaults. The returned object explicitly states the final
effective values.

After you get `image_count`, **first align with the user on which images to submit and what each one
represents**, then decide how to write the prompt. If the user provided fewer images than `min`, do not
pad with filler images; directly explain how many images the model requires at minimum.

**Tell the user both `credit_cost` and the `credit` balance from Step 0, and wait for
confirmation**. If the balance is insufficient, prompt the user to recharge first (see
references/credits.md for the recharge link and steps); do not force submission.

## Step 3: Crop Each Reference Image Locally

The `crop` field gives the target ratio and pixel dimensions:

```
crop = { ratio, crop_required, target_width, target_height, strategy, hint }
```

If `crop_required` is `false` (the ratio is `free`), skip this step and upload the original images directly.
Otherwise, **every reference image** must first be center-cropped to the target aspect ratio, then scaled to
`target_width x target_height`:

```bash
W=<target_width>; H=<target_height>
i=1
for SRC in "<reference image 1>" "<reference image 2>" "<reference image 3>"; do
  ffmpeg -y -i "$SRC" \
    -vf "crop='min(iw,ih*$W/$H)':'min(ih,iw*$H/$W)',scale=$W:$H" \
    "$WORKDIR/ref$i.jpg"
  i=$((i+1))
done
```

If ffmpeg is unavailable, use macOS built-in `sips` (note that `--cropToHeightWidth` takes **height
before width**):

```bash
cp "<reference image 1>" "$WORKDIR/ref1.jpg"
sips --cropToHeightWidth "$H" "$W" "$WORKDIR/ref1.jpg" >/dev/null
sips --resampleHeightWidth "$H" "$W" "$WORKDIR/ref1.jpg" >/dev/null
```

After cropping, confirm that every output file exists and has the correct dimensions
(`sips -g pixelWidth -g pixelHeight`) before moving to the next step. **Keep the order**: the order of
`ref1/ref2/ref3` is the order of `image_urls` during submission.

## Step 4: Upload Each Image to Get URLs

The upload interface accepts only one file at a time. **Call `create_upload_url` separately for each
reference image**:

```
create_upload_url() -> { upload_url, headers }
```

```bash
curl -sS -X POST "<upload_url>" -F "file=@$WORKDIR/ref1.jpg" -H "X-Client-Sn: <value from headers>"
# -> {"c":200,"m":"Success","d":"https://.../ref1.jpg"}
```

The `d` in the response is the image URL. `c != 200` means failure; report `m` to the user.
**Collect these URLs in reference-image order**; if the order is wrong, the visual composition relationship
will be wrong. Uploaded files are **temporary storage and will be cleaned periodically**; submit the task
as soon as you get the URLs.

## Step 5: Create the Task (Charges Credits)

```
i2v_create_task(model, kind="reference", image_urls=[<URL1>, <URL2>, ...], prompt,
                ratio?, quality?, duration?, mode?, movement_amplitude?)
-> { task_id, task_status, kind, image_count, credit_cost, quality, duration_sec, mode, ratio }
```

- `kind` must be `"reference"`.
- Pass `image_urls` in **reference image 1/2/3 order**, with the count inside the `image_count` range from
  Step 2.
- `prompt` is **required**; see "How to Write Prompts".
- `ratio` must **stay consistent** with the ratio used for cropping in Step 3.
- Parameters must match the set confirmed during the quote in Step 2, otherwise the actual charge may not
  match the quote.
- The returned `end_frame` is always `false`--reference-image-to-video has no first/end frame concept, so
  ignore this field.

## Step 6: Poll

```
i2v_get_task(task_id) -> { task_status, task_reason, video_url, finished }
```

The query interface is shared with image-to-video; there is no need to pass `kind`.

- `task_status == "success"`: `video_url` is the finished video; proceed to Step 7.
- `task_status == "fail"`: relay `task_reason` to the user, and ask whether to adjust
  parameters and retry or give up. Retrying re-bills at the normal price (failed credits are
  refunded automatically); this was already disclosed up front, so you do not need to reconfirm
  the price.
- Other values: the task is queued or generating. Wait 10 seconds, query again, and briefly tell the user
  progress.

## Step 7: Download and Deliver

Download `video_url` to `$WORKDIR/result.mp4` according to "Displaying the Artifact", provide the local
path + original URL, and remind the user: the remote link points to temporary storage and will be cleaned;
the local file is also under the system temporary directory and may be reclaimed by the system. The user
should save it to their own directory as soon as possible.

It is normal for the finished video to differ significantly from the reference images (this mode is
"reference", not "reproduction"). If the user is dissatisfied, first suggest **rewriting the prompt to make
the reference relationship more specific**, rather than immediately switching models and retrying.

## Error Handling

For login, connection, and service-binding issues, see `references/auth.md` (**when not logged in, the
entire MCP namespace will not appear**; do not misdiagnose it as the plugin not installed, and do not switch
to another brand's MCP). For common error codes and remedies, see `references/errors.md`; for credits and
billing rules, see `references/credits.md`; for each tool's returned field structures, see
`references/workflow.md`.
