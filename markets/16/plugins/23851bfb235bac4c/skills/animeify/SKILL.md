---
name: animeify
description: Restyle photos with six anime styles, optional art direction, and composition controls.
---

# Animeify

Use create_animeify with an actual attached photo or a user-supplied public HTTPS image URL. Choose retro, pop, lively, classic, vibrant, or soft. Keep preserve_composition enabled unless requested otherwise. Custom instructions can contain up to 150 characters.

Choose the flow from the current user request. If the user already supplied the required prompt/image and asked to generate, call create_animeify immediately with those inputs. Use the original defaults for unspecified settings. Do not open onboarding first, ask them to re-enter their inputs, or require another Generate click. The SDK generation view shows progress and then the result.

Call open_animeify only for post-install setup, an explicit request for the form, or a generation request that lacks the required prompt/input. The form is onboarding, not the result view. When create_animeify returns state pending, keep the returned id and call get_animeify_result every few seconds until ready or failed. Do not call create again to poll; that starts another generation. The studio automatically checks the job for users. Preserve the visual thumbnail galleries for style selection (and ColoringBook aspect ratios) and their original defaults; do not substitute dropdown selectors.

Pass an image attachment as the image file object returned by the host, or pass image_url. Do not invent a file ID or image URL. Inputs accept PNG, JPEG, or WebP up to 10 MB. Use only one source.

This plugin uses No Auth. Do not ask the user to sign in or link an Imagineers account. Existing daily app limits apply. OpenAI user/org metadata, when supplied by the host, is used for activity attribution and rate-limit grouping; it does not prove account ownership. Do not invent missing user/org IDs.

Show the returned preview and download link. Links are unlisted, accessible to anyone with the link, and expire after 24 hours. Explain failures as returned by the tool. Do not promise exact visual fidelity or successful generation before the tool completes.

The sidebar workspace is workspace_animeify; the conversation panel is panel_animeify. These are user entrypoints. Use choose_animeify_style only if the user asks for help choosing a style; never make it a gate before an already specified generation. Supported hosts show native thumbnail forms; other hosts show the SDK gallery. Mentions resolve public styles/presets via resources/read. Recipe files use .animeify, store prompts/settings only, and are edited through host-managed opaque resources; never invent local paths or embed photos. Preferences apply to new forms on this device only. Discuss actions open editable drafts; they do not send messages automatically.
