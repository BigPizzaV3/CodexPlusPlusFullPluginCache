---
name: sceneform-generate
description: Generate images, video, speech, music, sound effects, voice changes, lip sync, and talking avatars with Sceneform, and edit, animate, upscale, or reframe existing media. Use when the user wants any of these from a brief, a reference, or a file they already have, including a viral remix, a narrated storybook explainer, or a restyled clip. NOT for ads or carousels (sceneform-ad-studio), BrandKits or Personas (sceneform-brand), animated text and graphics (sceneform-motion), or posting (sceneform-publish).
license: MIT
metadata:
  author: sceneform
  version: "0.11.0"
---

# Generate with Sceneform

You are the art director and the prompt writer. Sceneform sends your prompt
to the model exactly as you write it, so the result is only as specific as
the prompt. The craft lives in reference files: read one by calling
`load_skill` with this skill's name and the file's `path`, or open it when
this skill is installed locally.

## Steps

### 1. Read the brief

Name the kind (image, video, speech, music, and so on), the deliverable,
where it will appear, and how many. Take every value the user gave. Fill the
rest with defaults: one output, the aspect ratio of the destination (the
craft references list them), and the style the subject and brand imply.

Ask only about a gap that blocks a useful result, and bundle up to three
short questions in one message:

- the subject, when nothing describes it;
- whose face, when a specific real person must appear and there is no photo
  or Persona;
- what to change, when the user rejects a result without saying why.

Model, lens, lighting, and prompt wording are your decisions. When the user
says "just make it", "go ahead", or similar, ask nothing: state the plan in
one sentence and generate.

When the work is for the user's brand or product ("our", "my shop", a
product name), read it first with `list_brand_kits` and use its facts.
Claims, prices, colors, and label text come only from the user or the kit.
A UGC or creator video, or any ad for a brand or product, belongs to
sceneform-ad-studio: `generate_video_ad` writes the script and shots from
your concept, which beats a hand-written video prompt.

Done when every value has a source (the user said it, or you chose the
default) and you can state the plan in one sentence.

### 2. Load the craft for the kind

| The request | Read |
| --- | --- |
| An image, an image edit, upscale, background removal, reframe | [references/image.md](references/image.md) |
| A video clip, an animated image, a Reshoot of a clip | [references/video.md](references/video.md) |
| Speech, music, sound effects, voice change, lip sync, avatar | [references/audio.md](references/audio.md) |
| A viral remix, a storybook explainer, a restyled clip | [references/short-videos.md](references/short-videos.md) |
| Working from the `sceneform` CLI | [references/cli.md](references/cli.md) |

Then pick the model by the job. A model the user names wins; otherwise start
here:

| The job | Model |
| --- | --- |
| An ad, a UGC or creator video, a product demo | Not `generate_video`: sceneform-ad-studio, `generate_video_ad` |
| Any other video: people talking, dialogue and sound, several shots, references | Seedance 2.5 (the default) |
| Trying a video idea cheaply | Seedance 2.5 at `resolution: "draft"`, then `finish_draft` |
| Fast physical action: sports, dance, stunts | Kling 4.0 |
| A clip that must follow reference clips closely, or 4K | Gemini Omni Flash 1.2 |
| Many references at once, or copying a reference clip's motion | H3 Max |
| An image with text, a design, an ad, a product photo, or an edit | GPT Image 2.6 Sunburst (the default) |
| A photoreal scene, an illustration or cartoon character, or many reference images combined | Nano Banana Pro |
| An edit of a real photo that must keep the person's face | Seedream 5.0 Pro |
| A candid phone photo of a person, with no product or text in frame | Soul 2.0 |

For a job the table does not cover, [references/models.md](references/models.md)
lists every model by kind with what it is best and worst at, what it takes,
and what it makes.

For an image or a video, read the chosen model's own guide. Call
`query_generation_options` with `action: "search"`, the `kind`, the model's
name as `query`, and `available_input_kinds` for any references (for a job
the table does not cover, `action: "recommend"` with a few task words
instead). Pick the first option whose `input_roles` cover every reference
you will pass; when the model cannot take them, say so and offer the closest
one that can. Then call it with `action: "get"` and that `option_ref`. Its
`prompt_guide` says how that model reads a prompt, how long a good one runs,
and whether it renders sound. Pass the same `option_ref` to `generate_image` or `generate_video` so
the guide and the model match. When the tool is out of reach, the model's
row in `references/models.md` links the same guide.

Done when you have read the reference for the kind and, for an image or a
video, the guide for the model you will use. Each is read once per
conversation.

### 3. Write the prompt

Follow the structure the reference gives for the mode, in the order the
`prompt_guide` prefers. Where the two differ, the `prompt_guide` wins: it
belongs to the model.

When you cannot follow a model's guide (you have not read it, or the user
handed you a one-line brief to build on), pass `enhance_prompt: true` on
`generate_image` or `generate_video` instead: Sceneform rewrites the prompt with that
model's playbook before it generates, keeping every `@{ref:…}` mention. A
prompt you wrote from the guide needs no rewrite, and a prompt the user asks
you to send as is goes unchanged, without `enhance_prompt`.

Done when every line of the reference's checklist holds for this prompt, you
passed `enhance_prompt: true`, or the user asked for their prompt as is.

### 4. Generate

- Each kind has its own tool: `generate_image`, `generate_video`,
  `generate_speech`, `generate_music`, `generate_sound_effect`,
  `change_voice`, `lip_sync`, `generate_avatar`, `upscale_image`,
  `remove_background`, `reframe_image`. Each takes `requests`, a list of
  what to make.
- One prompt: one request. Variations of the same image or video prompt are
  one request with `amount` (up to 4).
- Different prompts or references of one kind: one call with up to 12
  requests. Each other kind is its own call.
- A set that must match (one product in several scenes, a series): follow
  the reference's set rules, which lock one visual description across every
  prompt.
- References are refs Sceneform returned: an output's `asset_ref`,
  `search_library` results, a `persona_ref`, `product_ref`, or
  `element_ref`. Where the prompt uses one, write `@{ref:<ref>}` with the
  exact ref you pass (`@{ref:media_abc123}`); Sceneform swaps in the token
  the model reads. A mention of a ref you did not pass is refused. Files attached in the conversation go in `attachments`. A
  pasted link goes through `import_media`. A file on the user's device
  comes in through `open_upload`; in a host without Sceneform cards, follow
  its `without_card` steps.
- To file results in a Project or folder, pass `project_ref` or
  `folder_ref` (`list_projects`, `list_folders`; `create_project` and
  `create_folder` make new ones when the user names one that does not
  exist).

Done when every requested item has started, or came back as a quote or an
error you relay.

### 5. Follow the result

A result with `card_offered: true` was given to the host as a Sceneform
card, which shows progress and the finished media. Sceneform cannot see
whether the card is on screen. Say it is on its way and stop. When a later
step of the request needs the output (an image to animate next), or the user
asks for the file or cannot see the result, call `wait_operations` with its
`operation_ref`. Without the flag, call `wait_operations` (it holds up to 25
seconds per call). Call again only
for operations still queued or running, or an entry whose error is
`retryable`; `succeeded`, `failed`, `canceled`, and any other error are final,
so report them. Starting the same job again to check on it charges twice.

### 6. Check and deliver

You often cannot see the output. Before calling it good, run
`analyze_media` on its `asset_ref` with a question built from the
reference's checklist: "Does the label read MORNING, spelled right? Are the
hands natural?" Report what you checked, and say plainly when you checked
nothing.

When the check finds one clear defect, name it and offer the fix from the
reference's fix table. A fix is a new paid generation: run it once the user
agrees, or when they already asked for hands-off work or the best possible
result. Change only the defect, and stop after two fixes per output.

Without a card, give each finished `url` as a plain link, not an embedded
image, so the user keeps it. Reads such as `get_operation` and progress
checks never show a card. Call `show_card` only when the user wants to
review something now, with only what belongs together: an earlier result
they ask to see again, a before and after, the variants of one request, or a
set they asked to compare. Never use it to recap the session's outputs; each
review point gets its own card. When showing a card, say in one sentence
what it shows and give the file links only when the user asks for a file or
cannot see the card. Add one sentence naming any choice the user did not
make ("4:5 for the Instagram feed"). Leave prompts, refs, and model names
out unless asked.

## Spending

Generation starts at once and charges the credits it returns.

- Pass `quote_only: true` when the user asks what something costs, and on
  every spend call for the rest of the conversation once they ask you to
  check with them before spending.
- For a quote (`status: "awaiting_confirmation"`), give its summary and
  credits in one sentence, and call `confirm_actions` with its `action_ref`
  only after the user says yes. With `card_offered: true` the host was also
  given a card with Generate and Skip buttons; say they can approve there. Confirming the same
  `action_ref` twice never charges twice.
- A quote with `shortfall` cannot start yet: relay `shortfall.message` and
  stop. Once the account can pay, the same `action_ref` starts it.
- In a batch, retry only the item that failed with `retryable: true`, with
  its own tool. Resubmitting the batch charges every item again.
- A failed generation is not resubmitted silently: a retry is a new paid
  request, so ask first.

## Errors

Every tool error has a `code`, a safe `message`, and `retryable`.

- `INSUFFICIENT_CREDITS`: tell the user and stop. `get_credit_balance` shows
  the balance and `list_credit_transactions` where credits went.
- `SUBSCRIPTION_REQUIRED`: the account has no active plan. Tell the user a
  plan is needed and stop.
- `OPTION_UNAVAILABLE` or `PLAN_STALE`: query the options again and call the
  tool again; pass `quote_only: true` again if the user was still deciding.
- `NOT_FOUND` from `confirm_actions`: the quote expired or belongs to
  another account. Quote again.
- `TEMPORARY_FAILURE`: relay the message and any `support_ref`. When
  `retryable` is true, retry once after a pause.
- A call that timed out may have started: find it with `list_operations`
  before anything else.
