---
name: first-end-frame-video
description: Generate transition videos from a fixed first-frame image and end-frame image (Enkio / enkiomv.ai). Use when the user wants a first/end-frame video, specifies a starting image and an ending image, asks to turn one image into another, or wants a transition, transformation, or outfit-change effect between two images. If there is only one image and no need to specify an ending image, use the enkio:image-to-video skill instead; if the user wants to combine multiple reference images into a new scene, use the enkio:reference-to-video skill instead. The whole flow is completed through the enkio MCP service.
---

# Fixed First/End-Frame Video Generation

Call enkiomv.ai's image-to-video capability through the `enkio` MCP service to generate a video that
smoothly transitions from a **first-frame image + end-frame image**. The first frame of the finished
video is exactly the first-frame image you provide, and the last frame is exactly the end-frame image you provide.

## Service Binding

All capabilities in this skill come from the single `enkio` MCP server and **must not be replaced**:

- Its tool namespace in Codex is **`mcp__enkio`**. Codex normalizes `-` in server names to `_`, and the
  tool names themselves have no prefix. Every tool name mentioned below (such as `get_user_profile`) refers to
  the tool of the same name under the `mcp__enkio` namespace.
- **If the `mcp__enkio` namespace is not visible, the first judgment is "not logged in", not "plugin
  not installed"**: an MCP server that has not completed OAuth will not register its entire namespace.
  In this case, run `codex mcp login enkio` yourself (not the user), extract the plain `https://`
  authorization URL it prints, and give the user only that link to click -- do not lead with the
  `codex://mcp/login?server=enkio` deep link, since it silently does nothing unless the client has
  registered the `codex://` protocol handler. See `references/auth.md` for the full procedure, and
  explain that after login they must open a new conversation for it to take effect.
- **Under no circumstances may you substitute another brand's MCP** (`mcp__selfyz_ai` and `mcp__enkio` are two
  different services, two accounts, and two credit pools; cross-use will really charge the wrong account), and do
  not mix in a `task_id` / `job_id`, credit balance, or artifact URL obtained elsewhere.
- When you need to explain which service this skill is connected to, use the `brand` / `brand_website` returned by
  `get_user_profile` and the value of `mcpServers.enkio.url` in this plugin's `.mcp.json`. Do not answer from
  memory or guesswork; if `brand` is not Enkio, stop immediately and report an error.

Tasks are **asynchronous**: `i2v_create_task` returns `task_id` immediately, and you must poll
`i2v_get_task` yourself.

```
0 Log in/check balance -> 1 Choose a model that supports first/end frames -> 2 Set parameters and quote (confirm before charging)
-> 3 Crop both images to the same ratio -> 4 Upload each image to get URLs -> 5 Create the task (charges credits)
-> 6 Poll -> 7 Download, preview, and deliver
```

## Hard Constraints (Specific to This Skill)

- **You must choose a model whose `supports_fixed_end_frame` is true**, retrieved with
  `i2v_list_models(end_frame=true)`. Ordinary image-to-video models will be rejected directly by the server if you pass two images.
- **You must provide two images**: the `image_urls` order is fixed as `[first-frame URL, end-frame URL]`,
  **If the order is wrong, the finished video will be reversed**. Before submission, confirm with the user which image
  is the starting image and which is the ending image.
- **Both images must be cropped to the same ratio**, and you **must not use the `free` ratio**. Inconsistent
  first/end-frame sizes can cause a jump in the transition.
- **The prompt should describe the process of changing from the first frame to the end frame**, not a standalone
  description of either frame. The `fixed_end_frame_prompt_hint` returned by the model is the upstream guidance for
  this scenario; prefer it.

## General Hard Constraints

- **Creating a task charges credits. Before submitting, you must explain the cost to the user and obtain explicit confirmation**.
  All query tools are free.
- **Images must be cropped before upload**. The crop specification is provided by `crop` from `i2v_get_options`, and
  **the server does not accept image binaries; cropping is done locally**.
- **Do not construct or guess parameters such as `user_id`, `example`, or signatures**. The server has already handled them,
  and they do not exist in the tool inputs.
- Allowed values for `quality` / `duration` / `mode` **must come from `i2v_list_models`**. Do not invent them.
- Polling cadence: once every 10 seconds, with an upper limit of about 15 minutes; briefly report progress.
- When `task_status` is `fail`, do not retry blindly. First tell the user the `task_reason`,
  then ask whether to retry or give up. Retrying re-submits the task at the normal
  price--failed credits are refunded automatically, and this billing rule was already disclosed
  when quoting the cost, so no new price confirmation is needed here.
- **Before showing the video, you must download it locally first**. A remote URL pasted directly cannot be previewed.

## Showing the Artifact

The finished video is an Enkio **temporary remote URL**. Codex **cannot embed-preview media files from these domains**;
if you paste the URL directly, the user will not be able to open it.

```bash
WORKDIR="${TMPDIR:-/tmp}/enkio-i2v/<task_id>"
mkdir -p "$WORKDIR"
curl -sS -L -o "$WORKDIR/result.mp4" "<video_url>"
```

Video cannot be embedded for display. Provide the local absolute path, and also include the original remote URL.
If the download fails (non-200 / empty file), clearly state "preview download failed" and provide the remote URL.
Do not falsely claim it has been displayed.

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
- Validate that the returned `brand` must be **Enkio**. If not, it means the call is connected to the wrong service;
  stop immediately and tell the user.

The returned `credit` is the current balance; record it for later.

**Membership check (required).** Creating tasks with `i2v_create_task` requires an active membership. If
`get_user_profile()` returns an `is_member` value other than `true`, stop here: call `get_pricing_url`
and give the user the returned `pricing_url` to open in a browser, signed in with the same Wondershare
account used to authorize this MCP, to purchase a membership. Do not continue with model selection,
uploads, quoting, or task creation; after the user says the purchase is complete, call
`get_user_profile()` again and continue only when `is_member` is `true`.

## Step 1: Choose a Model That Supports First/End Frames

```
i2v_list_models(end_frame=true)
-> { end_frame_only: true, count, models: [...] }
```

**You must include `end_frame=true`**. All returned models support fixed first/end frames. If `count` is 0, there are
currently no available models; tell the user truthfully and do not fall back to forcing a single-image model.

List the selectable models for the user together with their supported resolutions, durations, and modes. If the user
has no preference, choose a cost-effective default combination from `combinations` and explain why.

## Step 2: Set Parameters and Quote

```
i2v_get_options(model, quality?, duration?, mode?, ratio?, end_frame=true)
-> { quality, duration_sec, mode, ratio, credit_cost, image_count, image_role, crop, ... }
```

**Remember to include `end_frame=true`**. The server will also validate whether the model supports the capability and
whether the ratio is legal, and will mark `image_count` as 2 and `image_role` as `["First frame", "End frame"]`.

If the model's default ratio is `free`, the server will report an error requiring a fixed ratio instead. Choose a
non-`free` ratio from `ratios`, such as `9:16` for vertical video or `16:9` for horizontal video.

**Tell the user the `credit_cost` together with the `credit` balance from Step 0 and wait for
confirmation**. If the balance is insufficient, prompt the user to recharge first (see
references/credits.md for the recharge link and steps).

## Step 3: Crop Both Images to the Same Ratio

`crop` provides the target ratio and pixel dimensions. **Run exactly the same crop command for the first frame and the end frame**:

```bash
W=<target_width>; H=<target_height>
for NAME in first end; do
  ffmpeg -y -i "<$NAME original image>" \
    -vf "crop='min(iw,ih*$W/$H)':'min(ih,iw*$H/$W)',scale=$W:$H" \
    "$WORKDIR/$NAME.jpg"
done
```

If ffmpeg is unavailable, use macOS's built-in `sips`:

```bash
for NAME in first end; do
  cp "<$NAME original image>" "$WORKDIR/$NAME.jpg"
  sips --cropToHeightWidth "$H" "$W" "$WORKDIR/$NAME.jpg" >/dev/null
  sips --resampleHeightWidth "$H" "$W" "$WORKDIR/$NAME.jpg" >/dev/null
done
```

After cropping, **you must verify that the two images have exactly identical dimensions** before continuing:

```bash
sips -g pixelWidth -g pixelHeight "$WORKDIR/first.jpg" "$WORKDIR/end.jpg"
```

## Step 4: Upload Each Image to Get URLs

```
create_upload_url() -> { upload_url, headers }
```

Upload the two images separately, and **remember clearly which URL is the first frame and which is the end frame**:

```bash
curl -sS -X POST "<upload_url>" -F "file=@$WORKDIR/first.jpg" -H "X-Client-Sn: <value from headers>"
curl -sS -X POST "<upload_url>" -F "file=@$WORKDIR/end.jpg"   -H "X-Client-Sn: <value from headers>"
# Each returns {"c":200,"m":"Success","d":"https://.../xxx.jpg"}
```

The `d` in the response is the image URL. If `c != 200`, it failed; report `m` to the user.
Uploaded files are **temporary storage and will be cleaned up periodically**. Submit the task as soon as possible after obtaining the URLs.

## Step 5: Create the Task (Charges Credits)

```
i2v_create_task(model, image_urls=[<first-frame URL>, <end-frame URL>], prompt?, ratio?,
                quality?, duration?, mode?, movement_amplitude?)
-> { task_id, task_status, end_frame, credit_cost, ... }
```

- **`image_urls` must contain two elements, with the first being the first frame and the second being the end frame**.
  The order must not be reversed.
- `ratio` must match the ratio used for cropping in Step 3.
- Parameters must match the combination confirmed during the Step 2 quote; otherwise the actual charge may not match the quote.
- `prompt` describes **how the first frame changes into the end frame** (motion, camera movement, transition method),
  referencing `fixed_end_frame_prompt_hint`.
- The returned `end_frame` should be `true`; if it is `false`, only one image was passed, so stop and check.

## Step 6: Poll

```
i2v_get_task(task_id) -> { task_status, task_reason, video_url, finished }
```

- `task_status == "success"`: `video_url` is the finished video; proceed to Step 7.
- `task_status == "fail"`: relay `task_reason` to the user and ask whether to retry after
  adjustments or abandon the task. Retrying re-bills at the normal price (failed credits are
  refunded automatically); this was already disclosed up front, so you do not need to reconfirm
  the price.
- Other values: queued or generating. Wait 10 seconds, query again, and briefly tell the user the progress.

## Step 7: Download and Deliver

Follow "Showing the Artifact" to download `video_url` to `$WORKDIR/result.mp4`, then provide the local path + original URL.
When delivering, remind the user to check whether the first and end frames match expectations, and explain that both
the remote link and the local temporary file may be cleaned up, so they should save another copy promptly.

## Error Handling

For login, connection, and service binding issues, see `references/auth.md` (**when not logged in, the entire MCP namespace
will not appear**; do not misjudge this as the plugin not being installed, and especially do not switch to another brand's MCP).
Common error codes and handling are in `references/errors.md`; credit and billing rules are in `references/credits.md`;
return field structures for each tool are in `references/workflow.md`.
