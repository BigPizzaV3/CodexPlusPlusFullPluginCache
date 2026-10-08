# Verified model constraints

Measured against the live server, not copied from docs. Where a fact was proven in
testing it says so.

## The two rules that break output quality

1. **Never omit `resolution`.** The first value in each allow-list is the default, and it
   is always the lowest. *Proven: a `/orbit` clip with no `resolution` came back 640x640.*
2. **Never substitute a duration.** Durations are per-model. A value outside the model's
   list silently falls back — no error, no warning.

## Video models

| Model | Durations | Resolutions | Ceiling | Notes |
|---|---|---|---|---|
| `ltx-2.3` *(default)* | 6, 8, 10 | 1080p, 1440p, 2160p | **2160p** | Highest quality ceiling. **Does not accept 5s.** |
| `veo-3.1` | 4, 6, 8 | 720p, 1080p, 4k | 4k | `image_url` optional |
| `veo-3.1-fast` | 4, 6, 8 | 720p, 1080p, 4k | 4k | |
| `seedance-2.0` | auto, 4–15 | 480p, 720p, 1080p | 1080p | **Best general choice for people** |
| `seedance-2.0-fast` | auto, 4–15 | 480p, 720p | 720p | Cheap, lower ceiling |
| `seedance-2.5` | 4–30 | 480p, 720p | **720p** | Strong adherence, **lowest ceiling**, refuses people |
| `happy_horse` | 3–15 | 720p, 1080p | 1080p | `image_url` **required** — natural fit for image-to-video |
| `wan-2.6` | 5, 10, 15 | 720p, 1080p | 1080p | `video_url` **required** in reference mode |
| `pixverse-v6` | 1–15 | 360p–1080p | 1080p | |
| `kling-2.6-pro` | 5, 10 | — | — | Ignores resolution |
| `seedance-1.5-pro` | 4–12 | 480p, 720p | 720p | |

## Content refusals — proven

**`seedance-2.5` rejects any source it believes "may contain real person" — including
illustrated and cartoon characters.** Confirmed across three separate uploads in live
testing. Never open a person-centric request on it.

On a safety or content refusal, stop and offer a different subject. Do not retry on
another model to bypass the refusal. If the reason is unclear, stop and clarify it.
Only switch models for a clearly established unsupported input capability; use the
fallback model's stated duration and resolution, and tell the user which model changed
and why, including any duration or resolution change.

**Default fallback ladder:** `seedance-2.0` (1080p) → `ltx-2.3` (6s, 1080p).

## Framing

**`seedance-2.5` image-to-video ignores `aspect_ratio`** and adopts the source image's
ratio. Never promise vertical output on that path. Other models honour the ratio.

## Image-to-video

`image_url` is an **array**. Exactly one URL and no `video_url`/`audio_url` = image-to-video.
Two or more, or any video/audio, = reference-to-video, supported only by `seedance-2.5`,
`seedance-2.0`, `seedance-2.0-fast`, `happy_horse`, `wan-2.6`, `veo-3.1`.

## Uploads

Attached files are **never** handed to this server. `request_image_upload` renders the
upload widget and places resulting URLs into context automatically. `user_upload` is
internal to that widget — never call it directly.

## Organizations

`org_id` is **schema-required and non-nullable** on every model-facing tool — you cannot
omit it or send null. Pass a real id when you have one. When you don't, send an empty
string: the server's gate resolves it (single org, or a remembered choice) and answers with
the id to retry with. If a tool reports that no organization could be
resolved (a first-time user with more than one), call `select_organization`, then continue.
That is a normal step, not an error.

## Finishing

Where a widget renders it polls itself — don't call `fetch_status`. On a text-only host
with no widget, poll `fetch_status` with `id=<uuid>` and `sync: true` until status is
`complete` or `error`.

## Paywall

Free organizations can only run `generate_image` on the default model. Everything else
returns a subscription message carrying an upgrade link — relay it verbatim.
