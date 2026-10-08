# Write a screenplay

Read the [editing workflow](../SKILL.md) first to choose the story, pacing, and
verification. This reference describes the file format; it does not replace those
editing decisions.

Before writing a screenplay, run `cirro.sh schema` (or `cirro.cmd schema` on Windows;
see [setup](../../setup/SKILL.md)). The output is the authoritative JSON Schema for
supported fields, event types, defaults, and units. Use `validate` to check the
screenplay against the recording and get mapped times.

The screenplay has `version: 1` and `recording`, `edit`, and `render` sections.
Recording events use `source_ms` and full-recording pixel coordinates. Clip `start_ms`
and `end_ms` use source time; camera and overlay times use story time. Ranges include
the start and exclude the end.

Use ordered clips with a source range and optional speed (default 1). Keep the ranges
continuous and split clips to change speed. Camera motion and overlays continue across
clip boundaries. Without a camera, the video stays full-frame; omitted captions and
highlights draw nothing.

The required `edit.cover.at_ms` selects the nearest fully composed story frame. That
frame is encoded first, followed by the complete story. Keep it within the derived story
duration. Do not shift authored timestamps for this extra frame.

`recording.events` is optional. Omit it when no trustworthy logs are available. Pointer
events generate an animated cursor and require cursor-free footage; keyboard events
generate input badges independently. Captions, camera motion, and privacy masks work
without events.

Use recorded `move`, `click`, `double_click`, `drag`, `scroll`, `shortcut`, and `typing`
events. Clicks animate the cursor. Keep the recorded platform information for shortcuts.
Typing `display` is one of `{"mode":"protected"}`, `{"mode":"count","characters":8}`, or
an explicitly safe `{"mode":"text","text":"appearance"}`. Never include sensitive values
or lengths.

All positions, camera centers, and rectangles use recording pixels. Zoom 1 shows the
full frame. Captions use `start_ms`, `end_ms`, and `text`; highlights and masks use
those times plus `rect: {x,y,width,height}`. Masks must cover private pixels throughout
the story and its cover.

Set appearance in `edit.style`: hex accent color, cursor size, camera response time in
milliseconds, and reduced motion. Use the built-in cursor.

Keep the original sequence and make important actions and results readable. Do not use
speed or masks to conceal a failed task.

Keep recorded event order and timestamps, including events that share `source_ms`.

## Example

This example uses an 18-second, 960 × 540 macOS recording. Replace its path, events, and
geometry with values from the actual capture; do not invent actions. `recording.webm` is
relative to the screenplay file.

```json
{
  "version": 1,
  "recording": {
    "path": "recording.webm",
    "platform": "macos",
    "dimensions": {"width": 960, "height": 540},
    "events": [
      {"type": "move", "source_ms": 0, "position": {"x": 100, "y": 180}},
      {"type": "shortcut", "source_ms": 800, "key": "K", "modifiers": ["CMD"]},
      {"type": "click", "source_ms": 1500, "position": {"x": 650, "y": 200}},
      {"type": "double_click", "source_ms": 2500, "position": {"x": 180, "y": 220}},
      {"type": "drag", "source_ms": 15500, "from": {"x": 180, "y": 300}, "to": {"x": 650, "y": 320}},
      {"type": "typing", "source_ms": 16000, "display": {"mode": "protected"}},
      {"type": "scroll", "source_ms": 16500, "position": {"x": 650, "y": 350}}
    ]
  },
  "edit": {
    "clips": [
      {"start_ms": 0, "end_ms": 3000, "speed": 1},
      {"start_ms": 3000, "end_ms": 15000, "speed": 6},
      {"start_ms": 15000, "end_ms": 18000, "speed": 1}
    ],
    "cover": {"at_ms": 2000},
    "camera": [
      {"at_ms": 0, "center": {"x": 480, "y": 270}, "zoom": 1},
      {"at_ms": 1000, "center": {"x": 384, "y": 270}, "zoom": 1.4},
      {"at_ms": 3000, "center": {"x": 480, "y": 270}, "zoom": 1}
    ],
    "captions": [
      {"start_ms": 0, "end_ms": 3000, "text": "Open the command menu"},
      {"start_ms": 5000, "end_ms": 8000, "text": "Move the item and enter protected text"}
    ],
    "highlights": [
      {"start_ms": 800, "end_ms": 2700, "rect": {"x": 384, "y": 162, "width": 336, "height": 81}}
    ],
    "redactions": [
      {"start_ms": 0, "end_ms": 8000, "rect": {"x": 800, "y": 85, "width": 130, "height": 51}}
    ],
    "style": {"accent": "#4a8fff"}
  },
  "render": {"width": 960, "height": 540, "fps": 24}
}
```

The clips keep all source footage and produce an 8-second story: 3 seconds at normal
speed, 12 source seconds compressed into 2 seconds, then 3 seconds at normal speed. The
drag at source time 15,500 ms therefore appears at story time 5,500 ms. The redaction
covers the entire story, including the composed frame selected at 2,000 ms for the
cover. The cover is encoded as frame zero, before the story; it adds one frame without
changing any authored timestamps.
