# Submission preparation

## Package scope

This is an author-supplied directory upload package wrapping an existing production server, not a server deployment. No app bindings, credentials, API keys, or server implementation are included. The archive has one top-level `probeauty-ai/` directory matching the manifest name; local source remains in `integrations/chatgpt-plugin/`.

Country targeting uses `publication.countries: []`, the package convention for no country restrictions. Distribution remains subject to ChatGPT availability. Payment requests remain subject to Stripe Connect eligibility, as enforced by the existing server. English is the supplied listing language. Optional dark-mode icons and brand colors are omitted.

## Demo recording to prepare

A real reviewer-accessible walkthrough is needed for this first directory review. Recommend a 3–5 minute MP4 screen recording at 1080p with readable prompts/results; this is a practical recommendation, not a claimed mandated format or duration. Follow any additional portal requirements shown at upload. Use the existing working custom MCP connection and a dedicated account with sample client data. Never show credentials, tokens, or production client details.

1. Show the ProBeauty AI connection and selected workspace. If showing OAuth, keep credentials off-screen.
2. Ask who's scheduled tomorrow; show the returned schedule and workspace-local date.
3. Ask for a 90-minute balayage opening next week; show real returned times.
4. Ask to move sample Maya's Thursday appointment to an available time and text her. Show availability, the short confirmation, your confirmation reply, and actual result. Use an authorized test recipient.
5. Ask when sample Sofia last came in and what she received; show the returned history.
6. Create an authorized test payment request for sample Maya's gel fill; show the amount/currency and text confirmation, returned link, and ProBeauty AI payment page. Do not make a real charge. Use the provider's supported test setup.
7. Show one booking-changes-off response with no retry, or one payment-country-unavailable response. Do not change or bypass server safeguards.

Record actual interactions rather than mockups. Play back the recording to check legibility and secrets. Host it at a URL reviewers can view without requesting access, then supply that URL so `review.demo_recording_url` can be added and the ZIP rebuilt. The recording is not yet supplied.

## Review cases and remaining checks

The manifest includes five positive and three negative cases drafted from the supplied tools. All cases are **Not run** in this workspace. Fixtures describe required sample data, not verified existing records. Confirm the sample setup and run them through the connected host before submitting. Additional coverage should exercise create_booking, cancellation confirmation, privacy, workspace ambiguity, date boundaries, and currency ambiguity.

Live OAuth protected-resource discovery was fetched successfully. Authenticated tool schemas and all server annotations remain independently unverified; inspect through the existing connected MCP client. Do not change or deploy the server from this package. Confirm each tool's readOnlyHint, openWorldHint, and destructiveHint match its actual behavior, including texts.

All four listing URLs returned HTTP 200. Their complete rendered privacy/terms content and coverage still require final review; HTTP success alone does not certify policy compliance.

Prepare dedicated reviewer access and sample data. Enter credentials and login instructions only in secure portal fields, never in this ZIP. Verify the intended developer identity/domain, OAuth connection, imported metadata, required scans, and attestations in the portal. No upload, directory review, or publication has been performed. The source ZIP is packaged, but public submission readiness remains pending the recording, reviewer access, live tests, and portal checks.
