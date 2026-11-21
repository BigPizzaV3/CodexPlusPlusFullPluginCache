---
name: text-to-video
description: Generate an AI video directly from a text prompt (SelfyzAI / selfyz.ai). Use this when the user has no source image and wants a video based only on a written description, says text-to-video / text generated video / text to video / AI generate a video clip, or asks which text-to-video models are supported, how many credits it costs, or how long the output can be. If there is an input image and the user wants to animate it, use the selfyz-ai:image-to-video skill instead; if the transition must be fixed by a first frame + last frame, use the selfyz-ai:first-end-frame-video skill instead. The whole workflow is completed through the selfyz-ai MCP service.
---

# Text-to-video

Call selfyz.ai's text-to-video capability through the `selfyz-ai` MCP service: **no input image is
required**. Provide only a prompt plus parameters such as quality, duration, and aspect ratio, and
the model directly generates a brand-new video.

## Service binding

All capabilities in this skill come from the single `selfyz-ai` MCP server, which **must not be
replaced**:

- Its tool namespace in Codex is **`mcp__selfyz_ai`**--Codex normalizes `-` in server names to `_`, and
  tool names have no prefix. Every tool name below (such as `get_user_profile`) refers to the tool of
  the same name under the `mcp__selfyz_ai` namespace.
- **If the `mcp__selfyz_ai` namespace is not visible, the first judgment is "not logged in", not "plugin
  not installed"**: an MCP server that has not completed OAuth will not register its entire namespace.
  In this case, run `codex mcp login selfyz-ai` yourself (not the user), extract the plain `https://`
  authorization URL it prints, and give the user only that link to click -- do not lead with the
  `codex://mcp/login?server=selfyz-ai` deep link, since it silently does nothing unless the client has
  registered the `codex://` protocol handler. See `references/auth.md` for the full procedure, and
  explain that after login they must open a new conversation for it to take effect.
- **Never substitute another brand's MCP under any circumstances** (`mcp__enkio` and
  `mcp__selfyz_ai` are two separate services, accounts, and credit pools; cross-use will charge the
  wrong account for real). Also do not mix in a `task_id` / `job_id`, credit balance, or artifact URL
  obtained elsewhere.
- When you need to explain which service this skill is connected to, rely on the `brand` /
  `brand_website` returned by `get_user_profile` and the value of `mcpServers.selfyz-ai.url` in this
  plugin's `.mcp.json`. Do not answer from memory or guesswork; if `brand` is not SelfyzAI, stop
  immediately and report an error.

The essential difference from the other two video skills: both of them start from images;
this skill **has no asset upload and no cropping step**. The prompt is the only content input.

Tasks are **asynchronous**: `t2v_create_task` immediately returns a `task_id`, and you must poll
`t2v_get_task` yourself.

```
0 Log in / check balance -> 1 Choose model -> 2 Set parameters and quote (confirm before charging)
-> 3 Create task (charges credits) -> 4 Poll -> 5 Download, preview, and deliver
```

## Hard constraints

- **This skill uses its own independent `t2v_*` tools. Do not mix them with `i2v_*` tools**. The
  text-to-video model list comes from a different upstream field. Passing an image-to-video model
  name into `t2v_*` reports "nonexistent text-to-video model", and vice versa.
- **Creating a task charges credits. Before submitting, you must tell the user the cost and obtain
  explicit confirmation**. All query tools are free.
- **`prompt` is required** and is the only content input for this mode. Empty or whitespace-only
  prompts are rejected directly. Prompt quality almost determines output quality, so it must be
  specific. See "How to write prompts" below.
- **`ratio` must be a concrete aspect ratio (such as `16:9` / `9:16` / `1:1`), not `free`**.
  There is no input image from which the canvas can be inferred, so the server cannot decide for
  you. If omitted, it falls back to the model's default ratio, but **you should proactively confirm
  landscape vs. portrait with the user**.
- **Do not call `create_upload_url`, and do not perform any cropping**. Text-to-video does not
  accept assets. Even if the user provides images, they are not usable for this mode--that request
  should use `selfyz-ai:image-to-video` instead.
- **Do not construct or guess `user_id`, `example`, signatures, or similar parameters**. The server
  already handles them, and they do not exist in the tool inputs.
- Allowed values for `quality` / `duration` / `mode` **must come from `t2v_list_models`**, and the
  four dimensions must form a combination that appears in `combinations`.
- Polling cadence: once every 10 seconds, with an upper limit of about 15 minutes. During that time,
  give the user brief progress updates; do not wait silently for a long time.
- If a task's `task_status` is `fail`, do not retry blindly. First tell the user the
  `task_reason`, then ask what to do. Retrying re-submits the task at the normal price--failed
  credits are refunded automatically, and this billing rule was already disclosed when quoting
  the cost, so no new price confirmation is needed here.
- **Before showing a video, you must download it locally first**. Pasting the remote URL directly
  cannot be previewed. See "Showing artifacts".

## How to write prompts

Text-to-video has **no visual reference at all**; the model can understand the scene only from the
text. If the prompt lacks information, the result will be very random. Therefore the prompt should
cover **subject + action + scene + camera + lighting/style**.

```
✅ An orange cat sits beside a neon street on a rainy night and yawns; the wet ground reflects the
   sign lights, the camera slowly pushes in from the side, cool tones, cinematic feel
✅ An aerial view sweeps over an autumn valley; golden forests ripple in the wind, morning fog has
   not yet dispersed, and the camera keeps tracking forward
❌ A cat                              <- Only the subject; action, scene, and camera are all left for the model to guess
❌ Generate a beautiful video          <- No executable information at all
```

If the user's description is too brief, **help fill it out first and then confirm**. Do not submit
with a single vague sentence--one submission is one charge. You may proactively ask: what is the
subject, what is it doing, what is the scene, what camera movement and mood are desired?

The prompt length must not exceed `prompt_limit_length`. The model's `prompt_hint` is the upstream
prompt-writing hint, and `prompt_guide_url` is the upstream prompt guide page. You may summarize
these for the user, but do not open the page on the user's behalf.

The aspect ratio should match the content: portrait (`9:16`) fits character close-ups and short-form
videos; landscape (`16:9`) fits scenery and cinematic shots.

## Showing artifacts

The finished video is an SelfyzAI **temporary remote URL**. Codex **cannot embed-preview media files
from these domains**; if you paste the URL directly, the user cannot open it.

Use a task-isolated working directory (so the user's repository is not polluted):

```bash
WORKDIR="${TMPDIR:-/tmp}/selfyz-ai-t2v/<task_id>"
mkdir -p "$WORKDIR"
curl -sS -L -o "$WORKDIR/result.mp4" "<video_url>"
```

Videos cannot be embedded for preview. Give the absolute local path and also include the original
remote URL so the user can save it themselves. If the download fails (non-200 / empty file), clearly
state "preview download failed" and provide the remote URL; do not falsely claim that it was shown.

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
- Verify that the returned `brand` must be **SelfyzAI**. If it is not, the call is connected to the
  wrong service; stop immediately and tell the user.

Record the returned `credit` as the current credit balance, and compare it with the estimated cost
when quoting in Step 2.

**Membership check (required).** Creating tasks with `t2v_create_task` is available to accounts
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
t2v_list_models()
-> { count, models: [ { model, model_name, model_desc, qualities, durations_sec,
                       modes, ratios, default_ratio, movement_amplitudes, supports_audio,
                       prompt_limit_length, prompt_hint, prompt_guide_url,
                       combinations, ... } ] }
```

`models[].model` is the model identifier; all later calls use it. Briefly list the available models
for the user together with each model's supported resolutions, durations, modes, and aspect ratios,
and let the user choose. If the user has no preference, choose a cost-effective default combination
from `combinations` and explain why.

`combinations` directly provides the credit cost for each "mode + quality + duration" combination;
prioritize it when choosing parameters.

It is normal that the response **does not contain any image-related fields** (image count, crop,
first/last frame).

## Step 2: Set parameters and quote

```
t2v_get_options(model, quality?, duration?, mode?, audio?, ratio?)
-> { model, model_name, quality, duration_sec, mode, audio, ratio, credit_cost,
    prompt_required, prompt_limit_length, prompt_hint, prompt_guide_url, next_step }
```

Omitted parameters fall back to the model defaults, and the response explicitly states the final
effective values.

- Passing `free` or a value unsupported by the model for `ratio` reports an error directly. If it is
  omitted, the model default ratio is used, but **landscape vs. portrait has a major impact on the
  finished video, so proactively ask the user**.
- `duration_sec` is the actual effective duration and is strongly tied to credits.

**Tell the user both `credit_cost` and the Step 0 `credit` balance, then wait for confirmation**. If
the balance is insufficient, tell the user the required credits and the current balance (see references/credits.md); do not force submission. This step is also when the prompt should be
finalized--confirm parameters and prompt together to avoid back-and-forth changes.

## Step 3: Create the task (charges credits)

```
t2v_create_task(model, prompt, ratio?, quality?, duration?, mode?, audio?, movement_amplitude?)
-> { task_id, task_status, model, quality, duration_sec, mode, ratio, credit_cost }
```

- `prompt` is **required**. See "How to write prompts" for wording.
- Use the `ratio` confirmed in Step 2; it must be a concrete aspect ratio.
- Parameters must match the set confirmed during the Step 2 quote, otherwise the actual charge may
  not match the quote.
- **Do not pass `image_urls`**--that parameter does not exist on `t2v_create_task`.

## Step 4: Poll

```
t2v_get_task(task_id) -> { task_status, task_reason, video_url, finished }
```

- `task_status == "success"`: `video_url` is the finished video; proceed to Step 5.
- `task_status == "fail"`: relay `task_reason` to the user, then ask whether to adjust the
  prompt and retry or give up. Retrying re-bills at the normal price (failed credits are
  refunded automatically); this was already disclosed up front, so you do not need to reconfirm
  the price.
- Any other value: queued or generating; wait 10 seconds, query again, and briefly update the user.

## Step 5: Download and deliver

Following "Showing artifacts", download `video_url` to `$WORKDIR/result.mp4`, provide the local path
+ original URL, and remind the user: the remote link points to temporary storage and may be cleaned
up, and the local file under the system temporary directory may also be reclaimed by the system. The
user should save it to their own directory as soon as possible.

Different generations from the same prompt will differ; this is normal. If the user is dissatisfied,
prefer recommending **making the prompt more specific** (add subject details, camera movement,
lighting, and mood) rather than immediately switching models and retrying.

## Error handling

For login, connection, and service binding issues, see `references/auth.md` (**when not logged in,
the entire MCP namespace will not appear**; do not misdiagnose this as the plugin not being
installed, and do not switch to another brand's MCP). See `references/errors.md` for common error
codes and handling; see `references/credits.md` for credits and billing rules; see
`references/workflow.md` for each tool's response field structure.
