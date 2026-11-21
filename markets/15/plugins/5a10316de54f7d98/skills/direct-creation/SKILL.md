---
name: direct-creation
description: "Use when the user wants one image, short video clip or voiceover made directly in the conversation and has not asked for a Canvas. Shows the credit cost first, then generates and returns the files."
---

# Direct creation

1. Pick a model. If the user did not name one, call `list_models` with `kind` set to `image`, `video` or `audio`, keep models whose `can_generate` is true, choose one that fits the request and tell the user its name. Never guess a `model_id`.
2. Read the options. Call `get_model` when you need settings such as aspect ratio, duration, resolution or voice, and only send values that the model lists.
3. Show the cost. Call `estimate_cost` with the same `model_id` and `settings`, tell the user how many credits it will use, and wait for a yes unless they already agreed to that cost in this conversation.
4. Reference images. For an image the user attached, call `upload_file` and pass the returned URL in `image_urls`. Only public HTTPS URLs are accepted; never pass private, local or internal addresses.
5. Generate once. Call `generate` with a new `idempotency_key`, then call `get_job` until `status` is `done` or `failed`. If you must retry the same request, reuse the same `idempotency_key` so it is not charged twice.
6. Report. Show the finished output from `get_job`. If the job failed, give the error it returned.

If the account does not have enough credits, say so plainly. Do not suggest buying credits or changing plans.
