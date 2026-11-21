---
name: generate-mv
description: Generate a music MV from audio and images (Enkio / enkiomv.ai). Use when the user wants to make an MV, music video, add visuals to a song, turn photos into a beat-synced video, or modify the storyline, lyrics, role image, cover image, or an individual shot of an already generated MV. The entire workflow is completed through the enkio MCP service.
---

# Generate MV

Use the `enkio` MCP service to call enkiomv.ai's MV Agent and turn one audio track plus several images into an MV.

## Service binding

All capabilities in this skill come from the single `enkio` MCP server, and **it must not be replaced**:

- Its tool namespace in Codex is **`mcp__enkio`**. Codex normalizes `-` in server names to `_`,
  and tool names do not carry a prefix. Every tool name below (such as `get_user_profile`) refers to the tool of the same name in the `mcp__enkio` namespace.
- **If the `mcp__enkio` namespace is not visible, the first judgment is "not logged in", not "plugin
  not installed"**: an MCP server that has not completed OAuth will not register its entire namespace.
  In this case, run `codex mcp login enkio` yourself (not the user), extract the plain `https://`
  authorization URL it prints, and give the user only that link to click -- do not lead with the
  `codex://mcp/login?server=enkio` deep link, since it silently does nothing unless the client has
  registered the `codex://` protocol handler. See `references/auth.md` for the full procedure, and
  explain that after login they must open a new conversation for it to take effect.
- **Never substitute another brand's MCP under any circumstances** (`mcp__selfyz_ai` and `mcp__enkio` are two services,
  two accounts, and two credit pools; cross-use will charge real credits to the wrong account). Also do not mix in
  a `task_id` / `job_id`, credit balance, or artifact URL obtained elsewhere.
- When you need to explain which service this skill is connected to, rely on the `brand` / `brand_website`
  returned by `get_user_profile` and the value of `mcpServers.enkio.url` in this plugin's `.mcp.json`.
  Do not answer from memory or guesswork; if `brand` is not Enkio, stop immediately and report an error.

The workflow has two stages and is **entirely asynchronous**: submission tools return immediately, so you must poll query tools yourself.

```
0 Log in / check balance → 1 Upload materials → [GATE 1] 2 Choose model, confirm parameters and credits
→ 3 Story creation (charged) → [GATE 2] cover + outline + lyrics + storyline
→ 4 Edit storyline/lyrics (free), regenerate cover/role (charged)
→ 5 Shot production (charged) + show shots → [GATE 3] segment images
→ 6 Regenerate a single shot (optional, charged)
→ 7 Retrieve final video (free) → Deliver
```

**Step 5 only shows shot images and does not deliver the final video**; retrieve the final video uniformly in step 7 with `mv_get_production`, which does not charge any credits.

## Mandatory confirmation gates (read this before anything else)

MV generation has **three mandatory user confirmation gates**. They are not suggestions and they
cannot be merged, skipped, or pre-approved. **Clearing one gate never authorizes the next one.**
**Every gate must be presented together with the credit cost of that step** (`step_credit` in the
tool response).

| Gate | Fires when | You must show | You must ask | Forbidden until the user answers |
| --- | --- | --- | --- | --- |
| 1 | `mv_get_options` returns `confirmation_gate: "plan_and_credit"` | every generation parameter (model, audio, images, prompt, aspect ratio, quality) + story-creation credit cost | confirm these parameters, or change them? | `mv_create_story` |
| 2 | `mv_get_story` returns `confirmation_gate: "story_assets"` | cover image + story outline + lyrics + storyline shots, and the shot-production credit cost | edit anything, or start the charged shot production? | `mv_submit_production` |
| 3 | `mv_get_production` returns `confirmation_gate: "segments"` | every shot image + the credit cost of this step | regenerate any shot, or accept them? | delivering `result_url` |

The MCP service reports each gate in its response:

```
requires_user_confirmation: true
confirmation_gate: "plan_and_credit" | "story_assets" | "segments"
blocked_until_user_confirms: ["mv_submit_production"]
user_confirmation_prompt: "GATE 2 of 3 - STOP AND ASK THE USER. ..."
step_credit: { step: "storyboard_production", credit: 150, charged_by: "audio duration", ... }
```

**Whenever `requires_user_confirmation` is `true`: present the artifacts, state the `step_credit`
amount, ask the question, and END YOUR TURN.** Do not call another tool in the same turn, do not
keep polling, and do not assume "the user already said make an MV" counts as an answer. Only a new
user message in this conversation clears a gate.

If you ever find yourself about to call `mv_create_story` or `mv_submit_production`, or to hand
over `result_url`, without a user message in between, you have violated this section - stop and ask
instead.

## Hard constraints

- **The three confirmation gates above are absolute.** Never chain parameter confirmation → story creation → shot production → final video in one unattended run.
- **Every gate must state the credit cost of that step** (`step_credit` from the tool response), not just the artifacts.
- **Operations that charge credits must first explain the cost to the user and obtain confirmation**: story creation, role/cover regeneration, shot production, and single-shot regeneration.
  Free operations: editing the storyline, editing lyrics, compose-only (`compose_only=true`), and query tools (including retrieving the final video in step 7).
- **After every display of a cover, role, or shot image, proactively tell the user they can spend credits to regenerate it**; see "Regeneration prompt".
- **Do not construct or guess parameters such as `user_id`, `example`, or signatures**. The server already handles them, and they do not exist in tool inputs.
- Remember the `task_id` after every submission; every later call must include it.
- Polling cadence: stage one once every 10 seconds, with an upper limit of about 5 minutes; stage two once every 20 seconds, with an upper limit of about 20 minutes.
  During polling, give the user brief progress updates; do not wait silently for a long time.
- When any status is `fail`, do not blindly retry the whole order. First tell the user which
  item failed and the error message, then ask whether to regenerate that item or abandon it.
  Regenerating re-bills that step at the normal price--failed credits are refunded
  automatically, and this billing rule was already disclosed when quoting each step's cost, so
  no new price confirmation is needed here.
- **Before showing images/videos, you must download them locally first**. Directly pasting a remote URL cannot be embedded for preview; see the next section.

## Showing artifacts (important)

The cover image, role image, shot images, and final MV returned by MV Agent are all Enkio **temporary remote URLs**.
Codex **cannot embed previews for images on these domains**; directly pasting a URL will only display a gray placeholder box.

Therefore: **For every image or video that should be shown to the user, first download it locally with `curl`, then show it using the local path.**

Use a task-isolated working directory by convention (to avoid polluting the user's repository):

```bash
WORKDIR="${TMPDIR:-/tmp}/enkio-mv/<task_id>"
mkdir -p "$WORKDIR"

# Use a meaningful <name>: cover / role / seg-00 / mv
# Infer the extension from the URL path; if unavailable, use .png (use .mp4 for video)
curl -sS -L -o "$WORKDIR/<name>.<ext>" "<remote URL>"
```

After downloading:

- Show images using the local absolute path so the user can see them directly in the conversation
- Also include the original remote URL so the user can save it themselves
- If download fails (non-200 / empty file), clearly state "preview download failed" and provide the remote URL so the user can open it themselves;
  do not falsely claim that the image has been shown
- The working directory is under the system temporary directory; you do not need to clean it up proactively, and do not write it into the user's repository

Whenever later steps mention "show", follow this section.

## Regeneration prompt

**Every time you finish showing a cover image, role image, or shot image, proactively tell the user, "If you are not satisfied, you can spend credits to regenerate it."** Do not wait for the user to ask.

The prompt must include:

1. What can be regenerated (cover / role / a shot with a specified index)
2. How many credits each regeneration costs (from `mv_get_options`; see `references/credits.md`)
3. The current credit balance (`credit` from `get_user_profile()`)
4. That regeneration supports natural-language descriptions of the desired changes

For example:

> The cover and role images are shown above. If you are not satisfied, you can regenerate them: cover 10 credits/image, role 10 credits/image.
> Your current balance is 460 credits. If you want changes, say directly what to change, for example, "Change the cover to a night scene with a cooler color tone."

Then **wait for the user to state their choice explicitly before acting**. Do not initiate any charged regeneration on your own.

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
- Verify that the returned `brand` must be **Enkio**. If not, it means the wrong service is connected; stop immediately and tell the user.

The returned `credit` is the current credit balance. `is_member` / `member_level_name` / `expire_time` are membership status.
Remember the balance and compare it with the estimated cost when quoting in step 2.

**Membership check (required).** Creating tasks with `mv_create_story` requires an active membership. If
`get_user_profile()` returns an `is_member` value other than `true`, stop here: call `get_pricing_url`
and give the user the returned `pricing_url` to open in a browser, signed in with the same Wondershare
account used to authorize this MCP, to purchase a membership. Do not continue with model selection,
uploads, quoting, or task creation; after the user says the purchase is complete, call
`get_user_profile()` again and continue only when `is_member` is `true`.

## Step 1: Upload materials

1. Call `create_upload_url()` to obtain `upload_url` and `headers`.
2. Upload directly with shell (the form field name is fixed as `file`), once per file:

```bash
curl -sS -X POST "<upload_url>" -F "file=@/path/to/song.mp3" -H "X-Client-Sn: <value from headers>"
# → {"c":200,"m":"Success","d":"https://.../song.mp3"}
```

3. The `d` in the response is the file URL. `c != 200` means failure; relay `m` to the user.
4. Uploaded files are **temporary storage and will be cleaned up periodically**. After obtaining the URL, submit the task as soon as possible.

## Step 2: Choose model, confirm parameters and credits (GATE 1)

Call `mv_list_models()` to list the available MV models (`models[].model`, `model_name`, qualities, aspect ratios,
and per-stage credits). If there is more than one, briefly list them for the user and let them choose; otherwise
use the only one. `default_model` is used whenever `model` is omitted. The model is fixed once the task is
created, so it cannot be switched for regeneration or shot production later.

`mv_get_options(model=<chosen model>, audio_duration_sec=<audio seconds>)` returns available qualities, aspect ratios, duration range, prompt length limit,
and credits for each stage (shot production is estimated by duration). It always comes back with
`confirmation_gate: "plan_and_credit"`, so **this is GATE 1**.

List for the user, item by item:

1. Every parameter you intend to pass to `mv_create_story`: `model`, audio file, image files, `prompt`, `ratio`, `quality`
2. `step_credit.credit` — the story-creation cost of this step — plus the estimated shot-production cost (`qualities[].estimated_production_credit`)
3. The `credit` balance from step 0; if the balance is insufficient, prompt recharge first (see
   references/credits.md for the recharge link and steps) and do not force-submit

Then **end your turn** and wait for the user to confirm or change the parameters. **Do not call
`mv_create_story` in the same turn.**

Audio duration can be inferred from a local file (for example with `ffprobe`); if it cannot be obtained, omit this parameter for now and show only the unit-price rules.

## Step 3: Story creation (stage one, charged)

```
mv_create_story(audio_urls=[...], image_urls=[...], prompt?, ratio?, quality?, model?)
→ { task_id, task_status, model, model_name, quality, credit_cost }
```

- `model` must be the same `models[].model` you passed to `mv_get_options`; `ratio` and `quality` must come from that model's options.
- `ratio` must be one of the available values from `mv_get_options` (such as `16:9` / `9:16` / `1:1`).
- `prompt` uses the user's natural-language description of style and narrative, and may be left empty.

Then poll `mv_get_story(task_id)` until the outline, cover, role, storyline, and lyrics statuses are all `success`.
Outputs: story outline, cover image, role image, storyline shots (index/start-end time/description), and timestamped lyrics.

Show them to the user (**first download `cover_url` and `role_url` according to "Showing artifacts", then paste the local paths**):

```bash
WORKDIR="${TMPDIR:-/tmp}/enkio-mv/$TASK_ID"; mkdir -p "$WORKDIR"
curl -sS -L -o "$WORKDIR/cover.png" "<cover_url>"
curl -sS -L -o "$WORKDIR/role.png"  "<role_url>"
```

Then provide, in order: cover image, role image, story outline, storyline shots, and lyrics summary.

Once the cover, outline, lyrics, and storyline are all `success`, `mv_get_story` returns
`confirmation_gate: "story_assets"` — this is **GATE 2**:

1. Show the cover image, the story outline, the timestamped lyrics, and the storyline shots
2. State `step_credit.credit`, the credit cost of the shot production you are about to start
3. Follow "Regeneration prompt" (cover/role regeneration is charged; storyline/lyrics edits are free)
4. Ask whether to edit anything or to start the charged shot production, then **end your turn**

**Do not call `mv_submit_production` in the same turn in which the gate fired.** Wait for the user's
explicit go-ahead.

## Step 4: Edits and regeneration (optional)

| Request | Tool | Billing |
| --- | --- | --- |
| Change shot descriptions or timeline | `mv_update_storyline(task_id, storyline)` | Free |
| Change lyrics or timestamps | `mv_update_lyrics(task_id, lyrics)` | Free |
| Role image is unsatisfactory | `mv_regenerate_asset(task_id, "role", prompt?)` | Charged |
| Cover image is unsatisfactory | `mv_regenerate_asset(task_id, "cover", prompt?)` | Charged |

- Both update tools require a **complete list** (not a delta). Modify the full result from `mv_get_story` and write it back.
- Edits can only be made after stage one completes and before submitting shot production.
- Regeneration is asynchronous; after submitting it, return to polling the corresponding status with `mv_get_story`.
- After regeneration completes, **download and show the new image again** (the URL changes). Do not fool the user with the old local file.

Field structures are in `references/workflow.md`.

## Step 5: Shot production (stage two, charged by duration)

```
mv_submit_production(task_id)     # First call, charges credits
mv_get_production(task_id)               # Poll
```

After polling until all `segments[].image_status == 2`, **this step only shows shot images; do not rush to provide the final video**.

Download and show shot images according to "Showing artifacts":

```bash
curl -sS -L -o "$WORKDIR/seg-00.png" "<segments[0].image_url>"   # Name by index and download one by one
```

When there are many shots, show the first few plus any the user names; do not pull all of them at once.

This is **GATE 3**. After showing the shots, state `step_credit` (accepting the shots and
retrieving the final video is free) and follow "Regeneration prompt" to tell the user which shots
can be regenerated and how many credits each costs, then **end your turn** and wait for their
choice:

- If the user wants regeneration → go to step 6
- If the user is satisfied → go to step 7 to retrieve the final video

**Even if `result_url` is already present in the response, do not deliver it before the user
accepts the shots.**

## Step 6: Single-shot refinement (optional, charged)

```
mv_regenerate_segment(task_id, segment_index, image_prompt?, video_prompt?)   # Charged
mv_get_production(task_id)                                                           # Poll this shot
mv_submit_production(task_id, compose_only=true)                                     # Free, refresh final MV
```

- `segment_index` comes from `segments[].index` in `mv_get_production`; do not count it yourself.
- **After regenerating a shot, you must run composition once with `compose_only=true`**, otherwise step 7 will still return the old final video.
- After regeneration completes, download and show the new shot image again (the URL changes), then ask the user whether to keep editing.
- When the user is done editing → go to step 7.

## Step 7: Retrieve final video (no credits charged)

```
mv_get_production(task_id).result_url
```

Call `mv_get_production` again and take `result_url`, which is the composed final MV. **This step does not consume any credits**.

**Only reach this step after the user has cleared GATE 3.**

- If `result_url` is empty: composition has not finished; continue polling at the stage-two cadence.
  If step 6 was just performed and it still does not refresh, check whether the `compose_only=true` composition was missed.
- After obtaining `result_url`, proceed to "Deliver".

## Deliver

First download the final MV to the local working directory, then deliver it:

```bash
curl -sS -L -o "$WORKDIR/mv.mp4" "<result_url>"
```

Provide the local file path + original `result_url`, and remind the user: the remote link points to temporary storage and will be cleaned up,
and the local file is under the system temporary directory and may also be reclaimed by the system. Recommend that the user save it to their own directory as soon as possible.

## Error handling

For login, connection, and service binding issues, see `references/auth.md` (**when not logged in, the entire MCP namespace will not appear**; do not misjudge it as an uninstalled plugin, and never switch to another brand's MCP).
For common upstream error codes and handling, see `references/errors.md`; for credit and billing rule details, see `references/credits.md`;
for return field structures of each tool, see `references/workflow.md`.
