# Keep actions aligned with the video

## Log the actions

Use a local JSONL journal or an existing structured event log. Keep the original clock
values and coordinate system. Record:

- The recording or session ID and a monotonically increasing event sequence.
- The action: pointer movement, click or double-click with button, drag with both
  endpoints, scroll with position and direction, shortcut with modifiers, or typing.
- The input-source timestamp, its clock name and unit, and what it measures. If
  unavailable, record monotonic times immediately before dispatch and after the tool
  call completes, along with success or failure. A dispatch interval is not an observed
  input timestamp.
- The original coordinates and their space: desktop logical points, physical pixels,
  window-relative pixels, or browser CSS pixels. Include viewport or window bounds and
  scale.
- The character count for ordinary typing. For protected input, record only
  `sensitive: true`, without text or length. Keep shortcut names only when safe and
  relevant.

For example (illustrative only; do not copy into a real recording):

```json
{"sequence":7,"session_id":"demo-run","action":"click","button":"left","x":640,"y":360,"coordinate_space":"desktop_logical_points","clock":"controller_monotonic_seconds","dispatch_started":102.410,"dispatch_finished":102.493,"status":"success","event_timestamp":null}
```

Add an entry for each real action, including failed calls. Batch typing may have a start
and end time but no per-character timestamps; keep that distinction. Do not log secrets
in command lines or annotations. If event recording requires extra permissions, use an
existing authorized input or tool journal when sufficient.

## Establish video time zero

Prefer the recorder's first-frame time and event times on the same clock. For a
timestamped frame sequence, keep each frame's presentation timestamp. Do not calculate
time from frame index and nominal fps for variable-rate footage.

When the clocks differ, record an explicit mapping. If a known event has event-clock
value `E_anchor` and occurs at decoded video time `V_anchor`, then:

```text
video_time_seconds = event_time - E_anchor + V_anchor
```

Record a harmless synchronization signal whose event timestamp and visible frame can
both be observed, ideally using the same logging process. Keep the anchor and how it was
measured. Do not reconstruct unknown click positions from screenshots. If an application
transition has unknown response latency, its first visible frame is not an exact
input-time anchor.

Check a second anchor near the end for drift, pauses, dropped frames, or clock resets.
Bound alignment uncertainty using the capture cadence and any dispatch interval. Do not
apply a single offset across a recorder pause or clock reset; use separate recordings or
a verified segment mapping. If no trustworthy mapping exists, keep the video and journal
for review and edit without event-driven effects.

Process launch time, file creation time, elapsed conversation time, and the agent's
recollection are not reliable first-frame anchors.

## Normalize coordinates and hand off

The renderer uses pixels in the full decoded video frame, even for a window recording.
Translate the logged coordinates using the recorded capture origin and scale:

```text
video_x = (event_x - capture_origin_x) * video_width / capture_region_width
video_y = (event_y - capture_origin_y) * video_height / capture_region_height
```

Use the same coordinate units for each subtraction. Account for display scaling, browser
device-pixel ratio, window chrome, and recorder scaling. Verify that a known event lands
on its observed control. If the region moves or resizes, record the transform for each
segment or re-record with fixed geometry; do not reuse the initial transform without
checking it.

Use only well-aligned observations for `recording.events[].source_ms` in the
[screenplay](../../create-demo-video/references/screenplay-contract.md), measured in
milliseconds from the first video frame. Keep click buttons, drag endpoints, and
interaction types. Put trustworthy shortcuts and typing in the same event array using
the schema's `shortcut` and `typing` types. Keep uncertainty and raw intervals in the
journal: the renderer expects point timestamps and cannot resolve uncertain intervals.
Omit `recording.events` when logs are unavailable.
