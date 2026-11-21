---
name: timeline-editing
description: "Place, trim, split, move, retime and delete clips on the Donkey Cut timeline. Use when the user asks to cut, reorder, speed up or rearrange footage."
---

# Timeline editing
Inspect the project before editing. Every track uses start times and allows gaps. add_clip places a project asset; add_overlay_video places footage on an upper track. add_clip with blocks lays out placeholders for footage the user will supply, and replace_item fills them while retaining the edit's timing.
trim_clip uses source seconds. split_at and place_clip use timeline seconds. For uniform forward playback, timeline time = clip.start + (source time - clip.in) / clip.speed. For reverse playback use clip.out - source time. For speed curves use the reported len and returned timing data.
delete_item removes the item and its group, leaving a gap. remove_gap closes a gap on one row; with the magnet on (set_magnet), track 0 closes up on every edit. place_clip places by time; move_clip reorders by index. Growth pushes overlapping neighbors on the same row; shrinking leaves a gap. Read returned ids and timing after each mutation.
set_speed changes uniform speed or reverse playback; set_speed_curve adds a rate curve. detach_audio separates a clip's sound for independent editing. freeze_frame creates a still. set_framing adjusts fit, fill, zoom and pan; set_clip_keyframes animates a clip's transform.
Use select_items to find items from their recorded state and apply batch-capable tools with ids. Measure or watch first when the selection depends on media content. set_clip_hidden and track visibility tools preserve items while excluding them from playback and export.
Transitions sit at cuts and retain their positions as edits move footage. Inspect parkedTransitions after mutations and remove unused transitions. Read transitions-and-fades, color-grading or graphics for styling. Verify the changed span with capture_frame and listen_audio, and use undo or redo for the shared editor history.
