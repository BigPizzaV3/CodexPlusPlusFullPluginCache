# VDClip: render an MP4

Rendering is the export step — "render it", "export it", "download it", "I want the file"
all mean `render_clip`. A clip must be rendered before it can be published.

## Non-negotiable rules

- Editor projects (`ai_type: "editor"`) are billed **at render time**. Call
  `estimate_cost({ type: "editor", duration_seconds })` and confirm before rendering.
- Clipping and captions results were already charged at creation — re-rendering them is
  free. Do not quote a cost for those.
- `quality` is plan-gated. Check `get_capabilities` before promising a tier.
- Never start a second render while one is unresolved. Read `get_clip` first.

## 1. Start the render

```
render_clip({ result_id, quality?, fps?, method? })
```

| Field | Meaning |
| --- | --- |
| `result_id` | The clip to render, from `list_clips` |
| `quality` | Output quality; plan-gated, omit to let the account default apply |
| `fps` | Output frames per second |
| `method` | `cloud` (backend renders) or `browser` (WebCodecs on the client) |

Returns `render_id` and `version` (the project version the render targets).

## 2. Poll for completion

```
get_clip({ result_id })
```

| Field | Meaning |
| --- | --- |
| `rendering_status` / `render_status` | `created` / `pending` / `completed` / `failed` |
| `download_url` | CloudFront-signed MP4 (~1h TTL); present once completed, `null` otherwise |
| `browser_render_ready` | True when a browser (WebCodecs) render can run |
| `project_version` | Version this clip belongs to |

Poll with bounded backoff and stop on `completed` or `failed`. When the link expires, call
`get_clip` again for a fresh one — never reconstruct a URL by hand.

## 3. Browser renders only: hand over the bytes

`method: "browser"` means the client encoded the MP4 itself, so the bytes still need to
reach storage:

```
request_render_upload({ result_id, content_type, content_length })
  → { upload: { url, headers }, version }
PUT the render bytes to upload.url, echoing every header in upload.headers verbatim
confirm_render_upload({ result_id, version }) → { ok }
```

- `content_length` must be the exact byte size — the PUT is signed for it.
- The headers include `Content-Disposition`, `x-amz-tagging` and `x-amz-meta-*`. Echo them
  as given; changing one invalidates the signature.
- `confirm_render_upload` is best-effort: the render already exists in storage once the PUT
  succeeds, so this call never fails the flow. Check `ok` and move on either way.
- Cloud renders never call this pair — the backend uploads server-side.

## Failure handling

| Situation | Action |
| --- | --- |
| `insufficient_credits` on an editor render | Stop; say how short they are. Do not retry |
| `plan_gated` on `quality` | Name the tier that unlocks it; offer the allowed quality |
| Render stuck in `pending` | Keep polling with backoff; do not start a second render |
| `render_status: failed` | Report it; a retry is allowed, but only one at a time |
| Timeout starting a render | `get_clip` first to see whether it started, then decide |

## Response style

Lead with whether the file is ready. Give the download link and say it expires in about an
hour. If it is still rendering, say the current status and that you will keep checking —
do not invent an ETA.
