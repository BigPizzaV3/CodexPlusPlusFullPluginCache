# Quick Generation

Read after choosing quick generation. The calling agent organizes the creative steps and calls models directly for media assets; no project creation is needed.

## 1. Select a Model and Prepare Inputs

Use `creation_generation_models` to discover an executable model, requesting `detail="full"` for capabilities, parameters, input roles, and access requirements. Reuse the user's model choice and match the requested media and supported settings; do not invent model IDs, capabilities, or parameters.

Upload local references through the main Skill's upload flow to obtain `file_ref`, then specify supported roles in `inputs`. Reuse an observed output with `inputs[].resource_id`, for example a confirmed image as `first_frame` for image-to-video generation. Input counts, formats, and roles depend on the selected model's capabilities.

## 2. Submit Generation or a Revision

Call `creation_quick_generate` with a new `client_request_id`, `media_type`, `model`, capability, supported parameters, prompt, and reference inputs.

To revise a prior quick output, use an observed `source_task_id` or `source_resource_id`; omitted recipe fields inherit from that source. A new generation or revision uses a new request ID; retrying the same submission retains the original ID and identical input.

Quick generation or history may first require history preparation. Follow returned `next`, `next_step`, and migration-status handles through `creation_quick_migration_status`; after success, retry the original operation with the same request ID. Use `creation_quick_migration_retry` for failed or cancelled preparation only when the user requests it. This is separate from project migration and does not require a new project.

For a service-issued batch or high-cost confirmation, present the actual choice, obtain the user's answer, and submit it with the returned `confirmation_token` and original request ID. Do not invent confirmation or silently switch models to avoid a decision.

## 3. Track Results

Query `creation_quick_status` using the returned `batch_id`, task IDs, or original request ID. Respect `poll_after_seconds` and check each task and its actual resources; acceptance or processing is not completion.

When the first item succeeds, present it using the main Skill's host-specific delivery rules while continuing to track the remaining tasks to terminal. In Claude Code and other hosts, use actual media or URLs from `tasks[].resources[]`; no preview-card call is needed. In Codex, when `creation_media_preview` is exposed, open a card; later results may join it or be grouped into an additional card. Do not repeatedly present unchanged results on every poll. Reconcile partial failures rather than treating one successful item as success for the whole batch.

## 4. Select a Preview Source (Codex Only)

Use this section only in Codex when `creation_media_preview` is exposed. In Claude Code and other hosts, continue status tracking and present the resources returned by `creation_quick_status`, then proceed to review or delivery.

Call `creation_media_preview` with `source="quick"` and either one existing `batch_id` or up to 100 observed `task_ids`; these selectors are mutually exclusive. Use a batch or its whole observed task selection, including pending tasks, for ongoing discovery. For a separate card focused on a particular group, pass that group's observed task IDs rather than the whole batch. A batch may have multiple useful cards.

Do not pass a project ID, epoch, or `resource_ids` for quick previews. If status was queried by the original request ID, use the returned batch or task IDs for preview rather than treating that request ID as a batch ID.

Preview reads only an initialized quick workspace. If history preparation is incomplete, continue the normal preparation flow rather than trying to initialize history with repeated preview calls.

Check actual resources in `tasks[].resources[]`. Follow the main Skill for subsequent refresh and display; do not pass natural-language creative instructions or arbitrary URLs to the preview action.

## 5. Review, Continue, or Cancel

For a reference-image review before video generation, complete and present the image first, retaining task and resource IDs. After the user's confirmation, reference that image in the next quick generation with the supported input role. For requested changes, submit a new revision and preserve confirmed requirements and materials.

For one-pass delivery, continue the needed steps within the user's authorization without adding default stage-by-stage approvals.

Read prior results through `creation_quick_history`, retaining filters and observed task/resource IDs across pages.

On user-requested cancellation, call `creation_quick_cancel` for the exact batch and check its returned state. Completed outputs and actual charges remain. Deliver the media results directly; project final-video export or a project-resource archive is not required.
