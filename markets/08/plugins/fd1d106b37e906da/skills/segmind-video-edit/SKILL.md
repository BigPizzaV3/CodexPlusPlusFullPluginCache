---
name: segmind-video-edit
description: >
  Edit, convert, or caption an existing video with Segmind — trim, cut, crop,
  resize, reformat for a platform, change speed, extract frames or audio, make a
  GIF, concatenate clips, re-encode, or burn in subtitles. Use when the user
  wants mechanical changes to footage they already have rather than new
  generated content. Do not use for generating video, for changing what is
  *in* the frame (that is a video-to-video model), or for upscaling resolution
  (that is segmind-video-upscale).
---

# Edit a video with Segmind

Read [inference-contract](references/inference-contract.md) first.

Everything here runs on Segmind models. There is no local ffmpeg and no sandbox
in this plugin — but there is a Segmind model that *is* an ffmpeg sandbox, which
covers the mechanical edits.

## `video-editor-agent` — natural-language ffmpeg

**$0.30 per generation**, flat, whatever the operation.

```
submit_inference("video-editor-agent", {
  "input_files": ["https://..."],
  "prompt": "crop to 9:16 around the centre and trim to the first 8 seconds"
})
```

- `input_files` is an **array**, even for one file — that is also what makes
  concatenation possible: pass several URLs and say how to join them.
- `prompt` is plain English. Be specific and mechanical: exact times, exact
  ratios, exact sizes. It is driving ffmpeg, not interpreting intent.
- `response_format` is `file` (default) or `json`.

What it covers: trim, cut, crop, scale, pad/letterbox, aspect-ratio reformat,
speed up / slow down, reverse, concatenate, extract frames or stills, extract or
strip audio, mux a new audio track, make a GIF, re-encode or change container.

Because it is one flat price, batch related operations into a single prompt
("trim to 0:03-0:11, crop 9:16, then speed up 1.25x") rather than paying $0.30
three times.

## `veed-subtitles` — burned-in captions

Transcribes and burns styled subtitles in one call.

```
submit_inference("veed-subtitles", {
  "video_url": "https://...",
  "preset": "<required>"
})
```

`preset` is **required** — pick one and name it to the user rather than letting
the call fail. Optionals: `language`, `translation_language` (this is how you
localise a clip), and `srt_content` / `srt_file_url` to burn a transcript you
already have instead of transcribing again.

**Priced per input minute, and the preset you pick doubles it:**

| Preset tier | Up to 1080p | Above 1080p |
|---|---|---|
| Basic | $0.143 | $0.286 |
| **Dynamic** | **$0.286** | **$0.572** |

The nine Dynamic presets — `glass`, `whisper`, `glide`, `glide2`, `fusion`,
`terminal`, `handwritten`, `backdrop`, `backdrop2` — bill **2x**, and they are
exactly the animated styles that suit the autoplay-muted social video this model
is for. `simple` is the default and a Basic one. Translation adds a further
$0.286/min on top. So name the preset *and* its tier when you quote, and above
1080p say so too: the same clip is four times the price at 4K with a Dynamic
preset as at 1080p with a Basic one.

Use it when captions should be *baked into the pixels* — social video that
autoplays muted. If the user wants a separate `.srt`, transcribe with
`whisper-large-v3` instead and hand them the file.

## Ordering

Put the operations in the cheap order:

1. **Upload anything you hold as a path.** `input_files` takes URLs, so a local
   clip goes through `upload_media` first (contract rule 4). Do this without
   asking.
2. **Trim next.** Every later step is billed on what it processes; cutting 60s
   to 8s before upscaling saves ~$2.60 on the upscale alone.
3. Edit / reformat.
4. **Upscale second-to-last** (`segmind-video-upscale`).
5. **Captions last** — burn them at final resolution so the text is sharp and
   correctly sized.

## Rules

1. **Segmind models only.** Do not shell out to a local ffmpeg, suggest the user
   install one, or reach for a non-Segmind service. If Segmind cannot do it, say so.
2. **One flat $0.30 per `video-editor-agent` call** — combine operations into one
   prompt instead of chaining calls.
3. **Trim before you upscale**, always.
4. **Submit, then poll in this turn** until it finishes. Video work outlives a
   blocking call, but it does not outlive your turn — wait for it.
5. **Be mechanical in the prompt.** "Make it look better" is not an edit; "scale
   to 1080x1920, pad with black" is.
6. **`preset` is required on `veed-subtitles`** — choose one explicitly.
