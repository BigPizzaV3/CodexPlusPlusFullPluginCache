---
name: image-to-video
description: Generate an AI video from one image (Enkio / enkiomv.ai). Use this when the user wants to turn a photo into a video, make an image move, create image-to-video, add motion effects to a static image, or asks how many credits image-to-video costs and which models and resolutions are supported. If the user needs a fixed first-frame + end-frame transition effect, use the enkio:first-end-frame-video skill instead; if the user wants to combine multiple reference images into a new scene, use the enkio:reference-to-video skill instead. The entire workflow is completed through the enkio MCP service.
---

# Image-to-video

Use the `enkio` MCP service to call enkiomv.ai's image-to-video capability and turn
**one image** + a prompt into a video clip.

## Service binding

All capabilities in this skill come from the single `enkio` MCP server, **and it cannot be
replaced**:

- In Codex, its tool namespace is **`mcp__enkio`**--Codex normalizes `-` in server names to `_`, and
  tool names do not include a prefix. Every tool name mentioned below (such as `get_user_profile`)
  refers to the same-named tool under the `mcp__enkio` namespace.
- **If the `mcp__enkio` namespace is not visible, the first judgment is "not logged in", not "plugin
  not installed"**: an MCP server that has not completed OAuth will not register its entire namespace.
  In this case, run `codex mcp login enkio` yourself (not the user), extract the plain `https://`
  authorization URL it prints, and give the user only that link to click -- do not lead with the
  `codex://mcp/login?server=enkio` deep link, since it silently does nothing unless the client has
  registered the `codex://` protocol handler. See `references/auth.md` for the full procedure, and
  explain that after login they must open a new conversation for it to take effect.
- **Never substitute another brand's MCP under any circumstances** (`mcp__selfyz_ai` and
  `mcp__enkio` are two services, two accounts, and two credit pools; cross-use will charge real
  credits to the wrong account). Do not mix in a `task_id` / `job_id`, credit balance, or output URL
  obtained elsewhere.
- When you need to explain which service this skill is connected to, use the `brand` /
  `brand_website` returned by `get_user_profile` and the value of `mcpServers.enkio.url` in this
  plugin's `.mcp.json`. Do not answer from memory or guesswork; if `brand` is not Enkio, stop
  immediately and report an error.

Tasks are **asynchronous**: `i2v_create_task` returns a `task_id` immediately, and you must poll
`i2v_get_task` yourself.

```
0 Log in / check balance -> 1 Choose model -> 2 Decide parameters and quote (confirm before charging)
-> 3 Crop the image locally -> 4 Upload and get URL -> 5 Create task (charges credits)
-> 6 Poll -> 7 Download, display, and deliver
```

## Hard constraints

- **Creating a task charges credits. Before submitting, you must explain the cost to the user and
  obtain explicit confirmation**. Query tools are all free.
- **The image must be cropped to the target aspect ratio before upload**; otherwise the upstream
  service processes it by its own rules, and the composition of the finished video can easily drift.
  The crop specification is provided by `crop` returned from `i2v_get_options`. **The server does
  not accept image binaries; cropping is done locally**.
- **Do not construct or guess parameters such as `user_id`, `example`, signatures, and so on**. The
  server already handles them, and these parameters do not exist in the tool inputs.
- The selectable values for `quality` / `duration` / `mode` **must come from `i2v_list_models`**;
  do not invent them. These three parameters jointly determine the billing template; if the
  combination does not exist, the server will reject it directly.
- Polling cadence: once every 10 seconds, with an upper limit of about 15 minutes. During that time,
  give the user brief progress updates; do not wait silently for a long time.
- When the task `task_status` is `fail`, do not retry blindly. Tell the user the `task_reason`
  first, then ask what to do. Retrying re-submits the task at the normal price--failed credits
  are refunded automatically, and this billing rule was already disclosed when quoting the
  cost, so no new price confirmation is needed here.
- **Before displaying a video, you must download it locally first**. Pasting the remote URL directly
  cannot provide a preview; see "Displaying the output".

## Displaying the output

The finished video is an Enkio **temporary remote URL**. Codex **cannot embed previews for media
files from these domains**, and users cannot open a bare pasted URL.

Use a per-task isolated working directory (so the user's repository is not polluted):

```bash
WORKDIR="${TMPDIR:-/tmp}/enkio-i2v/<task_id>"
mkdir -p "$WORKDIR"
curl -sS -L -o "$WORKDIR/result.mp4" "<video_url>"
```

Videos cannot be embedded for display. Provide the local absolute path, and include the original
remote URL as well so the user can save it themselves. If the download fails (non-200 / empty file),
state clearly that "preview download failed" and provide the remote URL; do not falsely claim that
it has been displayed.

## Step 0: Confirm service binding, login, and credit balance

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
- Validate that the returned `brand` must be **Enkio**. If not, it means the wrong service is
  connected; stop immediately and tell the user.

The returned `credit` is the current credit balance. Record it and compare it with the estimated
cost during the quote in Step 2.

**Membership check (required).** Creating tasks with `i2v_create_task` requires an active membership. If
`get_user_profile()` returns an `is_member` value other than `true`, stop here: call `get_pricing_url`
and give the user the returned `pricing_url` to open in a browser, signed in with the same Wondershare
account used to authorize this MCP, to purchase a membership. Do not continue with model selection,
uploads, quoting, or task creation; after the user says the purchase is complete, call
`get_user_profile()` again and continue only when `is_member` is `true`.

## Step 1: Choose a model

```
i2v_list_models()
-> { count, models: [ { model, model_name, model_desc, qualities, durations_sec,
                        modes, ratios, default_ratio, movement_amplitudes,
                        prompt_limit_length, prompt_hint, combinations, ... } ] }
```

`models[].model` is the model identifier; use it in all later calls. List the available models for
user selection, together with each model's supported resolutions, durations, and modes. If the user
has no preference, choose a cost-effective default combination from `combinations` and explain why.

`combinations` directly gives the credit cost for each "mode + quality + duration" combination;
prioritize it when choosing parameters.

## Step 2: Decide parameters and quote

```
i2v_get_options(model, quality?, duration?, mode?, ratio?)
-> { quality, duration_sec, mode, ratio, credit_cost, crop, prompt_limit_length, prompt_hint }
```

If parameters are omitted, they fall back to the model defaults. The return value explicitly tells
you the final effective values.

**Tell the user the `credit_cost` together with the `credit` balance from Step 0 and wait for
confirmation**. If the balance is insufficient, prompt the user to recharge first (see
references/credits.md for the recharge link and steps); do not force a submission.

## Step 3: Crop the image locally

The `crop` field gives the target aspect ratio and pixel dimensions:

```
crop = { ratio, crop_required, target_width, target_height, strategy, hint }
```

When `crop_required` is `false` (the ratio is `free`), skip this step and upload the original image
directly. Otherwise, first center-crop to the target aspect ratio, then scale to
`target_width x target_height`:

```bash
W=<target_width>; H=<target_height>
ffmpeg -y -i "<original image>" \
  -vf "crop='min(iw,ih*$W/$H)':'min(ih,iw*$H/$W)',scale=$W:$H" \
  "$WORKDIR/input.jpg"
```

If ffmpeg is unavailable, use macOS's built-in `sips`:

```bash
cp "<original image>" "$WORKDIR/input.jpg"
sips --cropToHeightWidth "$H" "$W" "$WORKDIR/input.jpg" >/dev/null
sips --resampleHeightWidth "$H" "$W" "$WORKDIR/input.jpg" >/dev/null
```

After cropping, confirm that the output file exists and that its dimensions are correct
(`sips -g pixelWidth -g pixelHeight`) before proceeding to the next step.

## Step 4: Upload and get a URL

```
create_upload_url() -> { upload_url, headers }
```

```bash
curl -sS -X POST "<upload_url>" -F "file=@$WORKDIR/input.jpg" -H "X-Client-Sn: <value from headers>"
# -> {"c":200,"m":"Success","d":"https://.../input.jpg"}
```

The `d` field in the response is the image URL. `c != 200` means failure; report `m` to the user.
Uploaded files are **temporarily stored and cleaned up on a schedule**. Submit the task as soon as
you get the URL.

## Step 5: Create the task (charges credits)

```
i2v_create_task(model, image_urls=[<image URL>], prompt?, ratio?, quality?, duration?,
                mode?, movement_amplitude?)
-> { task_id, task_status, credit_cost, quality, duration_sec, mode, ratio }
```

- Pass exactly **one** image in `image_urls` (this skill is the single-image workflow).
- `ratio` must **match** the ratio used for cropping in Step 3.
- Parameters must match the set confirmed during the quote in Step 2; otherwise the actual charge
  may not match the quote.
- `prompt` describes the action and camera movement you want in the scene. Its length must not
  exceed `prompt_limit_length`; the model's returned `prompt_hint` is upstream guidance for prompt
  writing and may be used as a reference.

## Step 6: Poll

```
i2v_get_task(task_id) -> { task_status, task_reason, video_url, finished }
```

- `task_status == "success"`: `video_url` is the finished video; proceed to Step 7.
- `task_status == "fail"`: relay `task_reason` to the user and ask whether to adjust parameters
  and retry or give up. Retrying re-bills at the normal price (failed credits are refunded
  automatically); this was already disclosed up front, so you do not need to reconfirm the
  price.
- Other values: queued or generating. Wait 10 seconds, query again, and briefly update the user on
  progress.

## Step 7: Download and deliver

Following "Displaying the output", download `video_url` to `$WORKDIR/result.mp4`, provide the local
path + original URL, and remind the user: the remote link points to temporary storage and will be
cleaned up, and local files under the system temporary directory may also be reclaimed by the
system. They should save the file to their own directory as soon as possible.

## Error handling

Login, connection, and service-binding issues are covered in `references/auth.md` (**when not logged
in, the entire MCP namespace will not appear**; do not misdiagnose it as the plugin being missing,
and never switch to another brand's MCP).
Common error codes and handling are covered in `references/errors.md`; credit and billing rules are
covered in `references/credits.md`; each tool's returned field structure is covered in
`references/workflow.md`.
