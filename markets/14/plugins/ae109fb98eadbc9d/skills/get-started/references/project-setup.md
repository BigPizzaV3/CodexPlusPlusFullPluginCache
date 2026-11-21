# Project setup choices and availability feedback

Use when collecting source/target language, format or platform during onboarding or episode preparation. Infer already supplied values from the request/file and confirm ambiguities; do not make the user re-enter known answers.

## Keep the next action short and complete

Once language/format/platform are known, stop collecting or displaying them again. Show just the matching export instructions, then one attachment checklist that explicitly names: source subtitle (required), KNP / approved names and terminology (optional), studio protocol / style guide (optional), and approved prior-episode subtitles (optional). Accept accessible reference links as well as attachments; read their contents before relying on them. Do not bury these materials after tables or repeat long preparation steps. If a source file is already supplied, skip the export tutorial. State the target-language Netflix fallback once when no project guide was supplied; keep user overrides scoped to their actual fields.

## Offer choices without inventing UI capabilities

Prefer a searchable language chooser when the host supports it; otherwise offer selectable common-language options using supported controls, or a short numbered/text list. Keep “Other language” with manual entry as a fallback. Do not invent an interactive dropdown, clickable control or submission callback that the host cannot actually render or handle. Explain when ordinary chat input is needed.

Use human-readable names and map them to the correct locale; distinguish Simplified Chinese, Traditional Chinese and relevant regional varieties (for example French France/Canada, Portuguese Brazil/Portugal, English US/UK). Do not convert Traditional Chinese to Simplified to bypass availability. Show common choices, not a fabricated exhaustive support list. An absent bundled guide is not permission to silently use another language's guide; report the missing reference.

Offer actual supported subtitle formats as choices (SRT, VTT, TTAL, TTML, PXTT, DFXP); prefer the supplied file's detected format. Use only known platform names or existing workflow labels; keep an Other/manual option. Source format selection is not proof that an uploaded file parsed successfully.

## Explain unavailable actions beside the action

Read the connected account's `suba_balance.service_availability` before deciding whether a new Chinese translation can start. The account-specific `chinese_translation_available` boolean takes precedence over a generic public notice: true means this account is eligible, false means new Chinese translations are unavailable. Never disable an eligible account merely because the notice describes the public restriction. Missing/failed availability data means eligibility is unverified, not that the account is definitely blocked; recheck before starting and explain what remains unknown.

For an unavailable target, label it in the chooser if possible and place a short persistent explanation immediately beside/below the disabled Continue/Start action; do not rely on a distant banner, color or hover-only tooltip. Example (localize to the user's language):

> Simplified and Traditional Chinese translation are still in development and validation and are not enabled for this account. Choose another available target language to continue. Please do not top up specifically for Chinese translation.

If the host has no such form, give the explanation directly in chat with the available next step instead of drawing a dead button. Update the explanation and button state when the target or verified eligibility changes. Do not silently switch the user's chosen language. A retry/unknown-access state needs its own truthful reason rather than the Chinese-unavailable message.

Scope the restriction to starting the unavailable service: browsing export instructions, preparing/uploading source material and reading/revising/checking/exporting existing work remain available. If Continue only opens export guidance, keep that preparation route available (for example label it “View export steps”) while clearly stating translation cannot start for the unavailable target. Never initiate translation or consume minutes merely because setup choices were filled in.

These are host-rendered guidance requirements, not a new backend form implementation. Changing the plugin does not alter an already rendered conversation or publish the update to other accounts; do not claim a screenshot's old form has been patched without observing it.
