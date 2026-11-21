# PixVerse CLI Model Reference

These choices describe supported behavior; the minimum CLI version is defined in
`../pixverse_runtime/cli-compatibility.json`. Query the active offline
`capabilities create <mode> --model <id> --json` before using an unfamiliar
combination; it is authoritative for parameters and media limits. Catalog presence
does not prove account entitlement or live Canvas support.

Plugin defaults remain Sunburst 2K/high for images and Seedance 2.5 1080p for video.
Apply `./quality-policy.md` and membership/preflight gates. This reference supports
explicit alternatives; it does not automatically change the selected route.

## Video Models

The CLI also lists `kling-4.0`, `seedance-2.5-flash` and
`seedance-2.5-480draft`. Inspect the selected mode before use; draft creation
and finalization are distinct operations, not an automatic quality fallback.
For images the catalog also includes `minimax-h3-image` and `seedream-5.5`.

| Model id | Quality | Duration | Aspect notes |
|---|---|---|---|
| `v6` | 360p–1080p | 1–15s | broad ratios including `3:2`, `2:3`, `21:9` |
| `pixverse-c1` | 360p–1080p | 1–15s | broad ratios through `2:3` |
| `seedance-2.0-standard` | 480p–2160p | 4–15s | `16:9`, `4:3`, `1:1`, `3:4`, `9:16`, `21:9` |
| `seedance-2.0-fast`, `seedance-2.0-mini` | 480p, 720p | 4–15s | same Seedance ratios |
| `seedance-2.5` | 480p–1080p | 4–30s | automatic framing/duration and expanded references; no CLI audio toggle, native sound uses provider defaults |
| `minimax-h3-max` | 480p, 768p, 1080p | 5–15s | contextual framing; see below |
| `minimax-h3` | 768p, 1440p | 5–15s | T2V fixed ratios, I2V auto; mixed reference and two-frame transition |
| `flux-3.0` | 720p, 1080p | 5–20s | video/I2V only; includes `2:1`; generated audio supported |
| `wan-3.0` | 480p–1080p | 2–30s | video, reference, and two-frame transition; generated audio supported |
| `gemini-omni-flash` | 720p | 3–10s | `16:9`, `9:16` |
| `happyhorse-1.0` | 720p, 1080p | 3–15s | `16:9`, `9:16`, `1:1`, `4:3`, `3:4` |
| `kling-o3-pro`, `kling-o3-standard`, `kling-3.0-pro`, `kling-3.0-standard` | model-controlled; omit `--quality` | 3–15s | `16:9`, `9:16`, `1:1` |
| `kling-o3-4k`, `kling-3.0-4k` | 4K model tier; omit `--quality` | 3–15s | same Kling ratios; O3 also supports reference |
| `grok-imagine-1.5` | 480p, 720p, 1080p | 1–15s | image-to-video only; ratio comes from input image |
| `grok-imagine` | 480p, 720p | 1–15s | broad ratios through `2:3` |
| `veo-3.1-lite` | 720p, 1080p | 4/6/8s | `16:9`, `9:16` |
| `veo-3.1-standard`, `veo-3.1-fast` | 720p–2160p | 4/6/8s | `16:9`, `9:16` |
| `sora-2-pro` | 720p, 1080p | 4/8/12s | `16:9`, `9:16` |
| `sora-2` | 720p | 4/8/12s | `16:9`, `9:16` |
| `v5.6` | 360p–1080p | 1–10s | broad ratios through `2:3`; `v5.5`/`v5` belong to the specialized modes below |

## Mode Support

| Mode | Supported model families |
|---|---|
| `create video` | v6, C1, Seedance 2.0/2.5, MiniMax H3/H3 Max, FLUX 3, Wan 3.0, Gemini Omni, Happy Horse, Kling including 4K, Grok, Veo, Sora, v5.6 |
| `create reference` | v6, C1, Seedance 2.0/2.5, MiniMax H3/H3 Max, Wan 3.0, Gemini Omni, Kling O3 including 4K, Grok Imagine, v5.6 |
| two-frame `create transition` | v6, C1, Seedance 2.0/2.5, MiniMax H3/H3 Max, Wan 3.0, Kling including 4K, Veo 3.1, v5.6 |
| 3+ frame `create transition` | v5 only |
| `create extend` | v6 or `grok-imagine` |
| `create modify` | v5.5 only |
| `create motion-control` | v5.6 only |
| `create upscale` | 2160p only |

Seedance 2.5 reference accepts up to 30 images, 10 videos, 10 audios, and 50 reference items total.
Wan 3.0 reference accepts up to 10 images, 5 videos, 5 audios, and 20 items total; audio-only input is
allowed. Query the offline model capability before writing a command instead of copying these maxima as
defaults.

## Image Models

| Model | Model id | Quality |
|---|---|---|
| GPT Image 2.5 Flare / Sunburst | `gpt-image-2.5-flare`, `gpt-image-2.5-sunburst` | 1080p, 1440p, 2160p; up to 16 references |
| Nano Banana 2.1 | `gemini-nano-banana-2.1` | Inspect active capabilities for parameters |
| GPT Image 2 | `gpt-image-2.0` | 1080p, 1440p, 2160p; supports `--detail-level low|medium|high` |
| Nano Banana 2 | `gemini-3.1-flash` | 512p, 1080p, 1440p, 2160p |
| Nano Banana 2 Lite | `gemini-3.1-flash-lite` | 1080p |
| Qwen Image | `qwen-image` | 720p, 1080p |
| Nano Banana Pro | `gemini-3.0` | 1080p, 1440p, 2160p |
| Nano Banana | `gemini-2.5-flash` | 1080p |
| Seedream 5.0 Pro | `seedream-5.0-pro` | 1080p, 1440p; up to 10 references |
| Seedream 5.0 Lite | `seedream-5.0-lite` | 1440p, 1800p, 2160p; up to 6 references |
| Seedream 4.5 | `seedream-4.5` | 1440p, 2160p; up to 6 references |
| Seedream 4.0 | `seedream-4.0` | 1080p, 1440p, 2160p; up to 6 references |
| Kling Image O3 / V3 | `kling-image-o3`, `kling-image-v3` | O3: 1080p–2160p; V3: 1080p/1440p |

## Audio Models

- Voice: `speech-2.8-hd`, `speech-2.8-turbo`, `eleven-multilingual-v2`, `eleven-v3`,
  `eleven-turbo-v2.5`.
- Music: `music-3.0`, `music-2.6`, `music-v2`, `music-v1`, `lyria-3-pro-preview`.
- Browse live account-visible catalogs with `pixverse voice models --json`,
  `pixverse voice presets --json`, and `pixverse music models --json`.

## MiniMax H3 Max

Use this route for an explicit H3 Max request. It does not replace the plugin's
Seedance 2.5 1080p video default or Sunburst 2K/high image default.

| Property | Contract |
|---|---|
| Model id | `minimax-h3-max` |
| Modes | `create video` (text/image), `create reference`, two-frame `create transition` |
| Quality | `480p`, `768p`, `1080p`; CLI default `768p` |
| Duration | integer 5–15 seconds; default 5; no `auto` duration |
| Fixed ratios | `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16` |
| Text-to-video framing | fixed ratios only; default `16:9`; `auto` is invalid |
| Image-to-video framing | always `auto`; use reference mode for a requested fixed ratio |
| Reference framing | `auto` or fixed ratios; default `auto`, also with video-only input |
| Transition framing | derived from the two images; no `--aspect-ratio` option |
| References | ≤9 images, ≤3 videos, ≤3 audios, **≤12 total** |
| Audio references | require at least one image or video |
| Prompt | required in all three supported modes |
| Unsupported | generated audio, multi-shot, off-peak, native extend/modify/motion-control, 3+ frame transitions |

Audio input is a reference role, not a promise of generated sound. Omit audio
toggles, `--multi-shot`, `--off-peak`, and Seedance-only `--task-type`. Do not invent
H3 Max-specific input duration, size or format limits: the CLI publishes count
limits and applies shared upload rules; remaining validation is backend-owned.
The older `minimax-h3` has different quality choices (`768p`, `1440p`, default
`1440p`) and no published combined reference-count cap; do not interchange them.

Read the installed offline contract before authoring the selected mode:

```bash
"${PIXVERSE_RUNTIME}" pixverse capabilities create reference --model minimax-h3-max --json
```

Examples are queue-task fragments. Preserve an explicit user quality; otherwise
1080p is a suitable plugin delivery choice for an explicitly selected H3 Max route.

```bash
pixverse create video --model minimax-h3-max --quality 1080p --duration 8 --aspect-ratio 16:9 --prompt "A slow tracking shot through a rain-lit street"
pixverse create video --model minimax-h3-max --quality 1080p --duration 8 --image ./opening.png --prompt "Continue the subject's movement from this frame"
pixverse create reference --model minimax-h3-max --quality 1080p --duration 10 --aspect-ratio 9:16 --images ./subject.png --videos ./motion.mp4 --audios ./voice.wav --prompt "@image1 follows the movement of @video1, guided by @audio1"
pixverse create transition --model minimax-h3-max --quality 1080p --duration 8 --images ./first.png ./last.png --prompt "Move smoothly between these two compositions"
```

Pass the fragment to `queue write` / `queue append`, preflight, and follow the
existing confirmation policy. Catalog presence does not prove account entitlement.

## Image Parameter Differences

`gpt-image-2.5-flare` and `gpt-image-2.5-sunburst` accept `1080p`, `1440p`, `2160p`,
up to 16 image references, and `low`, `medium`, `high`, `xhigh`, `max` detail.
Their ten ratios are `1:1`, `16:9`, `9:16`, `4:3`, `3:4`, `3:2`, `2:3`, `2:1`,
`1:2`, `21:9` at every quality. CLI defaults are Flare, 1080p, low detail, 16:9;
the plugin explicitly selects Sunburst, 1440p, high detail. GPT Image 2.0 retains
only low/medium/high detail. See `./quality-policy.md` for creative defaults.

CLI 1.4.13 introduced `--background auto|transparent|opaque` for Flare and Sunburst
only. The backend determines the output format; do not infer PNG delivery from this flag.
Check the active offline capability before using it on an older supported runtime.

## Audio Parameter Differences

`music-3.0`, `music-2.6`, `music-v2` and `music-v1` accept model-specific lyrics,
auto lyrics or instrumental settings. `music-2.6` remains the default. The CLI lists
`--duration-seconds`, but the service rejects fixed targets (400017), so the queue
refuses it and audio is trimmed locally. `lyria-3-pro-preview` accepts up to 10 image
references and lyric direction in the prompt, but no separate `--lyrics` value.
See `./audio-craft.md`; consult the active manifest for text limits rather than
copying removed limits from historical snapshots.

## Seedance 2.5

`seedance-2.5` is available for `create video`, `create reference`, and two-frame `create transition`.

| Capability | Reviewed contract |
|---|---|
| duration | 4–30 seconds; reference also accepts `auto` |
| quality | 480p, 720p, 1080p |
| video/reference aspect | `auto`, `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16` |
| reference images | up to 30 |
| reference videos | up to 10 |
| reference audios | up to 10 |
| all reference media | up to 50 total |
| reference task type | `auto`, `reference`, `edit`, `extend` |
| CLI audio toggle | unavailable; this does not establish whether native sound is generated |
| generated multi-shot | unsupported |
| off-peak | unsupported |

Plugin defaults follow `./quality-policy.md`: Seedance 2.5 at 1080p for supported video modes,
with `../skills-internal/pixverse-seedance-prompt-enhance/SKILL.md` before prompt/preflight. Its expanded
duration/reference domain also covers ordinary 4–15 second shots. If this runtime lacks the
model, refresh setup instead of silently reverting. Do not attach `--audio`, `--no-audio`,
`--multi-shot`, or `--off-peak`. Preserve requested sound in the prompt; separate sound production
is a creative or repair choice, and ordinary generation adds no automatic audio QA. Remove the
audio track during local export when a guaranteed silent deliverable is required.
