---
name: batch-banana
description: Generate images and video, edit images, and run batches with the Batch Banana MCP tools. Use when the user asks to create, edit, upscale, remove a background from, find, or download an image or video, asks for an image in a named look or style, wants many prompts run as a batch, asks what a generation would cost, or asks which Batch Banana workspace is in use.
---

# Batch Banana

Batch Banana runs image generation, video generation, and image edits at third-party model providers and stores every output in the user's workspace library. Every create spends the connected workspace's credits. Quotes, catalog reads, and library reads are free.

## Tools

| Tool | Use |
| --- | --- |
| `list_models` | Image and video models with `tier`, `creditCost`, and `billingUnit` (`output` or `second`). Optional `mediaType`: `image` or `video`. |
| `describe_model` | One model's options, resolution choices, and capabilities. Send every option under `options`, keyed by its `key`, including `options.resolution`. |
| `list_edit_operations` | Edit operations with cost, `requiresPrompt`, reference image range, and `sourceArity`. |
| `describe_edit_operation` | One operation's `params`. |
| `quote_image_generation`, `quote_video_generation`, `quote_image_edit` | Price a request without charging. Returns `creditCost`, `pricingVersion`, `requestHash`. |
| `generate_image`, `generate_video`, `edit_image` | Start a paid job. Returns a job. |
| `get_generation` | Read a job's status and outputs. The only way to learn when a job finishes. |
| `search_styles` | Find a look in the Batch Banana style library by description, list the library by family, or read chosen styles in full. A style's `slug` goes in `generate_image`'s `style`. |
| `search_library` | Find existing work, one result per job, by prompt, kind, model, edit operation, project, or date. Each output has a `fileId`, and each result has the `jobId` that made it. |
| `list_projects` | Project ids for `projectId` on creates and on `search_library`. |
| `get_file` | URLs, size, and dimensions of one file. |
| `import_image` | Turn a public `https` image URL into a file id. |
| `quote_batch`, `create_batch`, `get_batch`, `update_batch` | Batches: price rows, create and run them, follow progress and read results, add rows, retry failed rows. |
| `cancel_batch` | Stop a batch's running run. Only when the user asks. |
| `download_files` | Download links: ZIP files of a batch, one ZIP of up to 50 jobs, or one file. Links work for an hour. |
| `list_workspaces`, `switch_workspace` | The user's workspaces with plan and credits, and moving the connection to another of them. |

## Pick a model

1. Call `list_models` with the media type you need. Match the user's request to `tier` (`fast`, `standard`, `premium`) and cost. Use the `id` field, never the display name.
2. Call `describe_model` before setting anything beyond `prompt`, `aspectRatio`, and `numImages`. Only send options the model lists.
3. If the user names a model, find it in `list_models`. If it is not there, say so and offer the closest match.

Defaults for `generate_image`: `aspectRatio` `1:1`, `numImages` 4 (range 1 to 8). Supported aspect ratios: `21:9`, `16:9`, `4:3`, `3:2`, `5:4`, `1:1`, `4:5`, `3:4`, `2:3`, `9:16`, limited to what the model supports. Ask for fewer images when the user wants one.

## Several different images

When the user wants several different images, such as four concepts, variations in different styles, or one image per product, make one `generate_image` call with `prompt` as a list of prompts (up to 16), not one call per image. Quote the same list once with `quote_image_generation`. A list makes 1 image per prompt unless `numImages` says otherwise, up to 48 images in all. All prompts in one call share the model, aspect ratio and options. One call keeps every image in one results view; separate calls replace each other's view.

## Batches

A batch is a table of prompts that run together, up to 20,000 rows, each with its own model, aspect ratio, image count, style and references if it wants them. Batches need the Max plan; on other plans the create is refused (see Plan refusals).

1. `quote_batch` with `defaults` (at least `model`) and up to 500 `rows`. It prices every row, writes nothing, and lists rows that can't run with the field and fix for each. Fix those first.
2. `create_batch` with the same `defaults` and `rows`, a `name`, a new `idempotencyKey`, and `run.expectedCreditCost` set to the quote's `totalCredits`. The run starts preparing and is charged once when every row is priced. `PRICE_CHANGED` means nothing was charged: quote again.
3. `get_batch` with `waitSeconds` (up to 45) until `inProgress` is false. Call it in a loop; it returns early when the run moves. Clients with the results view already show a live batch card, so say a sentence about progress rather than listing images.
4. Read results with `get_batch` and `results`. For rows that failed, quote with `retry: "failed"`, then `update_batch` with `action: "retry_failed"` and the new `expectedCreditCost`.
5. To stop a run, call `cancel_batch` with the batch `id`, only when the user asks. Images already started finish, and credits for the rest come back.

More than 500 rows: only from a client that can send an HTTP PUT. Write a CSV whose header is `prompt,model,aspect_ratio,images,style,references,options` (only `prompt` is required), `create_upload` with purpose `batch_csv`, PUT the file to `uploadUrl`, `complete_upload`, then pass the upload id as `csvUploadId`.

## Download

`download_files` returns links that work for an hour. Pass exactly one of:
- `batchId` (and optionally `columnId`): ZIP files of up to 1,000 rows each, every file named by its row.
- `jobIds` (up to 50): one ZIP of every output of those jobs, for a normal result.
- `fileId`: one file.

Give the user the links to open in their browser. Never write code to download files. In clients with the results view, the view also has Download and Download all.

## Use a style

When the user asks for a look (watercolor, claymation, 35mm film, a named style), check the style library before writing the look into the prompt.

1. Call `search_styles` with `query` describing the look. It returns the closest styles first, one line each, and the results view shows each style's example images. Read the note in the answer: it says how close the matches are.
2. Pass the chosen `slug` as `style` to `quote_image_generation` and `generate_image`. The server adds the style's reference images and description, so the prompt describes only the subject.
3. The model must take reference images. Check `describe_model` when unsure. Your own `referenceFileIds` still work alongside a style.
4. When nothing fits, write the look into the prompt instead. Style search covers Batch Banana's library of styles, not the user's own work; `search_library` finds that.

## Quote, then create

1. Call the matching `quote_*` tool with the same fields you will send to the create tool.
2. Tell the user the `creditCost` when the request is large (many images, a long video, an edit over many files) or when they asked about cost. For a small single request, go ahead.
3. Call the create tool with:
   - a new `idempotencyKey` for each distinct request, for example a UUID. Reuse the same key only when retrying the exact same request after a network error or timeout; that returns the original job instead of charging again.
   - `expectedCreditCost` set to the quoted `creditCost`.
   The create returns the first job plus `requestCreditCost`, the total charged for the whole request, and `jobIds` when it made several jobs. Report `requestCreditCost` as the cost.
   - `projectId` when the user names a project (from `list_projects`).

Errors from a create:
- `PRICE_CHANGED`: the price moved since the quote. Quote again, tell the user the new cost, and create with a new key.
- `IDEMPOTENCY_CONFLICT`: the key was used for a different request. Use a new key.
- `INVALID_ARGUMENT`: read the message, fix the field (often an option the model does not support), and retry.
- `RATE_LIMITED`: wait, then retry once with the same key.

## Poll until the job finishes

A create returns a job with `status` `pending` or `processing` and `pollAfterMs`.

1. Wait `pollAfterMs`, then call `get_generation` with the job `id`. When the create returned `jobIds`, poll each of them.
2. Repeat until `status` is `completed` or `failed`. If the response keeps saying `processing`, lengthen the wait between calls, up to about 15 seconds. Images usually finish within a minute. Videos can take several minutes.
3. Tell the user the job is running rather than going silent during long waits.

When `status` is `completed`, `outputs` holds one entry per image or video:
- `url`: full resolution. Images are delivered as WebP.
- `thumbnailUrl`: 384px preview, images only.
- `source.url`: the original file exactly as the provider produced it.
- `fileId`: use as `referenceFileIds`, `startFrameFileId`, or an `edit_image` `fileIds` entry.

Never embed outputs with Markdown image syntax (`![...](url)`). Clients that support it already show them in the Batch Banana results view, so describe the result in a sentence instead. Elsewhere, share the URLs as plain links. Every output is also in the user's Batch Banana library.

## Build on existing work

- `search_library` with `query` (2 characters or more) searches prompts by relevance. Without `query` it lists the newest first. Each result is one job with its outputs, cost, model, and references.
- Filter with `kind`, `model`, `operation`, `createdAfter` and `createdBefore`, `projectId`, or `mediaType`. Edits and imports have no prompt, so find them by `kind` or `operation`, not `query`. The date filters do not combine with `query`.
- A page can come back short while `nextCursor` is set, especially with `model` or `operation` filters. Pass `nextCursor` back as `cursor` until it is null.
- An output's `fileId` works as a reference image for generation or as a source for `edit_image`.
- A result's `jobId` works with `get_generation` to see the whole batch it came from.
- To use an image from the web, call `import_image` with its public `https` URL and an `idempotencyKey`, then use the returned `file.id`. Generation and edit tools take file ids, never URLs.

## Edit images

1. Get file ids from `search_library`, a previous job's `outputs`, or `import_image`.
2. Call `list_edit_operations` and pick the operation. Check `requiresPrompt` and the reference image range. Call `describe_edit_operation` when you need its `params`.
3. Quote with `quote_image_edit`. Many images cost the per-image price times the count.
4. Call `edit_image` with `operation`, `fileIds`, any `prompt`, `params`, or `referenceFileIds`, a new `idempotencyKey`, and `expectedCreditCost`.
5. Poll by `sourceArity`:
   - `each`: one job per image. Poll every id in `jobIds`.
   - `one` or `all`: one job, which may hold many outputs.
6. `then` runs one follow-up operation on every output, for example remove the background, then make stickers. Poll a job of the first request until `followUp` appears, then poll each id in `followUp.jobIds`. If every job of the first request failed, there is no follow-up; stop polling.

## Failures and refusals

- A job with `status` `failed` carries `error.message`. Credits for a failed job are refunded automatically. Tell the user the job failed, give the reason, and say the credits were returned.
- Model providers refuse prompts and images that break their content policies, such as sexual content. Batch Banana does not screen prompts before generation, so a refusal shows up as a failed job. Do not reword a refused request to get around the provider's policy.
- Decline before calling any tool when the request is for sexual content, for a realistic image of a real private person without their consent, or for an image meant to deceive people into thinking it is real.

## Workspaces

Every call works in the connection's current workspace: its credits, library and projects. `get_profile` names it. `list_workspaces` shows all of the user's workspaces with each one's plan, credits, and which is current.

Call `switch_workspace` only when the user asks to use another workspace, or agrees to a switch you offered. Never switch on your own, including to get around a refusal: a switch spends another workspace's credits and files work in another library. Users can also choose Change workspace next to the app in Batch Banana under Settings, Connected apps.

## Plan refusals

`PLAN_REQUIRED` means the current workspace's plan doesn't include what was asked for, such as a batch. The error text holds a sentence to give the user word for word: it names the plan that includes the feature, links to the plans page, and offers another of the user's workspaces when one has that plan. Repeat it as written. Do not switch unless the user then asks.

## Out of credits

`INSUFFICIENT_CREDITS` means the connected workspace does not have enough credits for the request. Tell the user how many credits the request needs (from the quote) and that the workspace is short. Suggest a cheaper option if one exists: fewer images, a `fast` tier model, a lower resolution, or a shorter video. Plans and prices are described at https://batchbanana.com/pricing. Do not push upgrades or name plans.

`EMAIL_NOT_VERIFIED` means the account's email address isn't verified yet. Tell the user to open the verification link in the email from Batch Banana, then try the request again. Don't mention credits.

## Sign-in errors

`UNAUTHENTICATED` or `NOT_AUTHORIZED` means the connection is missing, expired, or was revoked in Batch Banana's settings. Ask the user to reconnect Batch Banana in their client. Do not ask for passwords or API keys.

When the user is no longer a member of the connection's current workspace, the error text lists their workspaces and says how to switch. Repeat it as written.
