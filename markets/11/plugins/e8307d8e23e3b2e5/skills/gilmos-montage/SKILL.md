---
name: gilmos-montage
description: "Read and edit a gilmOS project's saved montage timeline using approved media, stable storage paths and revision checks. Use for montage edit decisions; this MCP does not render or export a finished video."
---

# Edit montage decisions in gilmOS

Resolve the project and call `gilmos_get_montage`. Its result is `{montage, library, scenes, mediaPrefixes}`. `montage` contains `document` and `revision`; it is null if none has been saved. The library contains approved/final shot videos, retained scene renders and approved audio, not every sandbox draft.

Preserve the existing timeline and apply only the requested edit. An empty library does not mean the project has no media: eligible production takes may not yet be approved. Do not change approval statuses merely to make them appear in a montage.

## Document contract

Read [examples.json](references/examples.json) when constructing arguments. The document is:

```json
{
  "version": 1,
  "timeline": {
    "clips": [],
    "tracks": [],
    "settings": {"width": 1920, "height": 1080, "fps": 24, "bgColor": "#000000"}
  },
  "imports": []
}
```

Use this empty document only when an empty montage is explicitly intended; do not replace a loaded montage with it. Preserve fields the requested edit does not touch.

- Timeline `display.from`, `display.to`, durations and trim times use **microseconds**, not seconds or frame numbers. A five-second span is `5_000_000`. Trim uses source time and must account for playback rate.
- Media clip `src` uses `storage://project-medias/<storagePath>`. Use actual library/project paths under allowed `mediaPrefixes`. Signed preview URLs, decoder thumbnails and client-only fields must not be persisted.
- Supported clip types include `Video`, `Audio`, `Image`, `Text`, `Caption`, `Effect`, `Transition`. Every clip has a unique ID and belongs to exactly one track through `track.clipIds`. Track IDs are unique.
- Keep valid settings: even width/height in 128..4096 and fps in 1..60. A clip must have a finite nonnegative start and end greater than start. Imports must reference project storage.
- Do not combine a scene render with the individual shots it already contains unless the user explicitly wants repetition. Use scene/shot numbers to preserve narrative order.

## Save with concurrency control

Send `gilmos_save_montage` the loaded revision and modified full document; use revision 0 only when `montage` was null. On a revision conflict, reread and reapply the bounded edit to the new state if still appropriate. Never force a blind overwrite or discard another member's work.

After success, read the montage again and confirm the persisted change/revision. The result is a saved edit decision document, not a rendered film. Do not claim export, playback validation or a download unless a tool actually produced that output.
