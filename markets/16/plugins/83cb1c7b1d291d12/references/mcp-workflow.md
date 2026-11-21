# Use idea.ai MCP for creative workflows

## Discover the connection and model

Use the connected idea.ai MCP tools. If discovery or sign-in fails, read [connection troubleshooting](connection-troubleshooting.md). Call `list_models` for the relevant modality and `get_model` for the selected model. Treat model IDs in skills as discovery examples, not an availability list or a quality ranking. Validate the current per-modality options, defaults, prompt length, file roles, and cross-role limits. Option spelling is model-specific: for example, `aspectRatio` and `aspect_ratio` are not interchangeable.

## Choose the operation

| Requested operation | Tool | Model capability to inspect |
| --- | --- | --- |
| New image from text, or images from source video | `create_image` | `textToImage` or `mediaToImage` |
| Edit, resize, outpaint, or upscale input images | `edit_image` | `imageToImage` |
| Generate, animate, extend, dub, subtitle, enhance, or clip video | `create_video` | `textToVideo` or `mediaToVideo` |
| Speech, music, effects, or audio processing | `create_audio` | `textToAudio` or `mediaToAudio` |
| Generate a 3D asset | `create_3d_model` | `textTo3D` or `imageTo3D` |
| Transcribe or extract text from supplied media | `extract_text_from_media` | `mediaToText` |

These tools accept `model`, model-specific `options`, optional `prompt` where supported, and `files` for input media. Do not pass the deprecated `modality` argument to them. A model's presence in the catalogue does not guarantee it fits one of these tools; check the exact supported modality. Prefer these operations over `generate` and `generate_with_upload`, which the server marks deprecated for removal on 16 December 2026.

## Upload without starting a generation

For a result generated through this MCP, reuse its full-resolution output URL in the next operation's `files[].url`. `wait_for_generation` and `get_generation` return reusable output metadata. Do not ask the user to reupload it.

For files on the user's device, call the free `upload_media` picker with the needed file types, labels, roles, and aliases. Include all required inputs, such as both a motion image and motion video. The picker returns a `batchId` before the user selects files; it does not start or charge for generation. After the user's next upload-completion message, call `get_upload_batch` with that ID. Check every required slot is present and ready; use `get_upload` for an individual pending upload. Do not reopen the picker or busy-poll an empty batch before the user responds.

When the environment can read a local file and perform HTTP PUT, `create_upload` is a free alternative. Supply its real name, extension, size, and optional matching MIME type. PUT raw bytes to the returned URL with the returned MIME type as Content-Type and no Authorization header; wait with `get_upload` until ready. Never expose the presigned URL in the public package.

Use each ready `uploadId` as `files[].uploadId`, with its correct role and alias; supply either `url` or `uploadId`, never both. A replacement picker-slot session changes the selected upload; the current tool contract says it does not overwrite or delete the previous upload or stored object. Reupload only when needed for a failed or expired upload. Validate measured type, size, duration, dimensions, and frame rate against model constraints. A reference role requiring an alias must have the same distinct alias cited in the prompt as `{{alias}}`. Use numeric rule fields when returned, including `totalMaxMb.maxMb`, and honor the stated units; for example, Nano Banana 2.1 currently returns a combined 60 MiB media-to-image limit. Do not invent unnamed file roles or missing rule parameters.

If the picker cannot render, use a supported direct upload when possible or explain the specific host limitation. Do not tell the user to change network settings or host their file simply because the assistant cannot upload bytes. Do not substitute a different media service.

## Price and authorize the actual inputs

Discovery, model inspection, voice discovery, quotes, upload status, generation status, and `preview_3d` are free. `upload_media` and `create_upload` are free upload operations. The paid operations are `create_image`, `edit_image`, `create_video`, `create_audio`, `create_3d_model`, and `extract_text_from_media`. Do not describe every tool starting with create as paid, or treat transcription as free inspection.

Call the free `quote_cost` before each paid request, including standard-price and reference-based requests. A standard model's `pricing.coinAmount` is a base amount, not proof of the total for every option, file set, or output count. Supply the same prompt and complete options intended for generation. For structured dialogue, quote the actual `options.inputs` script and selected voice IDs; a separate prompt is optional when the model needs none. Preserve that same representation in the paid operation. Text-priced models may quote a maximum prompt length when prompt is omitted, so include the actual script wherever that model prices the prompt.

Supply every `pricing.inputs.options` value and one `inputMedia` entry for every priced file. Include optional roles actually supplied and all references affected by an `aspectFit` rule, even for a standard-price model. Such fitting can add a per-reference surcharge. Include the rule's relevant options and each affected image's measured dimensions, or a ready upload ID with its role. Never assume an empty required-metadata list means an input is free. Respect `pricing.inputs.mediaAnyOf` and the capability's cross-role rules when choosing alternative source roles; do not send both mutually exclusive inputs just to satisfy pricing.

For uploads, send `inputMedia[].uploadId` so the server prices measured metadata. For URL inputs, obtain required dimensions, duration and frame rate from the actual asset or returned metadata; do not guess. Quote defaults are not applied: explicitly resolve all required price inputs. Keep every intended option, then merge returned `resolvedOptions` into that complete option object before generation. Do not discard valid original options merely because the quote omitted them from resolvedOptions. Preserve the same model, prompt, full file set, measured metadata, and options after approval; requote changes to priced inputs or output count.

Explain the deliverables, count, quoted cost, and any reservation/settlement conditions. Seed Audio can quote a maximum for generated audio. Clean Audio settles on vendor-measured input duration and can reserve the source-role maximum for URL-sourced audio even when the quoted amount is lower. Read current tool guidance rather than treating these examples as universal guarantees. Do not promise that every quote is a hard upper bound. If the possible reservation or final charge is not within the user's authorized scope or budget, obtain a supported bounded plan or explain the unresolved amount before spending.

Honor existing authorization and budget; obtain missing spending approval before a paid operation. For batches, establish whether the quote covers one output or the whole request. A failure or uncertain response does not authorize a speculative retry loop or a duplicate paid job.

For speech, get the model's actual `voiceCatalog`. Use `list_voices(facetsOnly=true)` to resolve missing preferences, then offer a small filtered selection with real IDs. Do not list hundreds of voices, invent IDs, select a voice without user choice, or imply catalogue speech requires voice cloning.

## Wait, inspect, and deliver

The paid operation returns a real `generationId` and, in supported hosts, its own updating result view. Call `wait_for_generation` with that ID until it finishes, checking failures and the approved retry limit. Each call waits up to about 45 seconds and adds no duplicate view. After about ten minutes of your own waiting, report the actual running state and that the view will update, unless the user requested continued waiting. Never report a pending job as completed.

Do not call `get_generation` merely to duplicate the operation's result view. Use it when an earlier generation is requested, visual inspection requires an inline image, or the user has no result view yet. Prefer native media; do not extract hidden audio/video URLs from structured results just to repeat playable media. For a completed GLB or glTF output, call the free `preview_3d` once with its existing generation ID when that tool is available, then provide the returned model file URL as well. OBJ, FBX, STL, and USDZ use the returned artifact URL without claiming preview support. A preview failure does not authorize another generation. Do not stack duplicate viewers through repeated preview or get_generation calls. Reuse output URLs internally for follow-ups.

Inspect results against the brief and mark anything unavailable for inspection as unverified. Success does not prove character fidelity, translation accuracy, geometry quality, or SVG editability. Preserve approved assets and original references, and revise only affected outputs within the authorized budget. On `paid_subscription_required`, explain the account requirement and stop retrying. Respect rate-limit guidance, wait before a bounded read retry, and avoid concurrent discovery bursts. A timeout or ambiguous paid response is not permission to submit a duplicate charge: recover the known generation status first, or explain the uncertainty before another paid action.
