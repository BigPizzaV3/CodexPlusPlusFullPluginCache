# Premiere Pro playbook

> **Observe, never assume.** Panel layout depends on workspace and version. These are
> landmarks, not coordinates. Trust the screenshot over this file.

## Landmarks

| Task | Look for |
|---|---|
| Import | **File > Import**, or double-click empty Project panel space |
| Project contents | The **Project** panel |
| Timeline | The **Timeline** panel with numbered V and A tracks |
| Trim | Drag a clip edge; or the razor tool to cut |
| Titles | **Premiere 25.0+:** the **Properties** panel. **Earlier:** the **Essential Graphics** panel. Check the version — see below. |
| Audio levels | The **Audio Track Mixer**, or clip volume in Effect Controls |
| Export | **File > Export > Media** |
| Sequence settings | **Sequence > Sequence Settings** |

## Sequence settings come first

Before laying down anything, confirm the sequence matches the footage — frame size, frame
rate, and pixel aspect. A mismatch shows as black bars or scaled clips and is far harder to
fix later than to prevent.

If Premiere offers to change sequence settings to match a dropped clip, that is usually the
right answer for a new sequence, and the wrong answer for an existing one.

## Laying out the timeline

1. Import to the Project panel first; wait for thumbnails.
2. Place each clip at the intended time and track. Check insertion versus overwrite and
   linked audio; use another track only when layering is intended. For requested
   replacements, preserve the surrounding timeline.
3. Place at the playhead, then trim to the planned duration.
4. Music goes on an empty audio track, not over existing audio.

## Titles

**Check the Premiere version first** — Adobe moved graphics editing out of Essential
Graphics into the **Properties** panel in **25.0**. In 25.0 and later, select a text layer
and edit it in **Properties**. In earlier versions, use **Essential Graphics** (Browse /
Edit tabs). If you can't tell the version, look for whichever panel exists and trust the
screen.

Use text layers — they stay editable and can be restyled later.
Never use a generated image of text. Each distinct piece of copy gets its own layer.

**Captions: pick one route and say which.**

- **Editable captions** — Premiere's own captions/text, which stay editable in the project.
  Use this when the user wants to keep working on the copy.
- **Burned-in captions** — `generate_video_captions` bakes styled captions into the video
  upstream. Faster and better-styled, but **not editable afterwards**. Place that version
  on a higher track and mute or hide the original so its audio isn't duplicated.

These are different deliverables. Don't promise editable captions and then deliver a burned
version — tell the user which one they are getting.

## Audio

- Duck music under any voice — a bed at full level buries dialogue.
- Check levels peak below 0 dB.
- If the user supplied audio, don't replace it; layer under it.

## Exporting

1. **File > Export > Media**.
2. Set format (H.264 for MP4), preset matching the sequence, and the output path.
3. Export or queue to Media Encoder.
4. **Wait and confirm the file exists.** A queued export is not a finished one — this is
   the single most common false "done" in this skill.

## Saving

**File > Save As** to a new project filename. Never save over the user's project.

## Verification checklist

- [ ] Sequence settings match the footage
- [ ] No pre-existing clip overwritten
- [ ] Clips trimmed to the planned durations
- [ ] Titles are editable graphics, not baked images
- [ ] Music ducked under any voice
- [ ] Project saved under a new name
- [ ] Export file confirmed on disk

## Known failure modes

| Symptom | Cause | Fix |
|---|---|---|
| Black bars around clips | Sequence doesn't match footage | Fix sequence settings, re-lay |
| User's edit destroyed | Dropped onto an occupied track | Undo; use a new track above |
| Export "done" but no file | Queued in Media Encoder, never ran | Check the queue, confirm on disk |
| Clips won't fit the plan | Source duration differs from planned shot | Trim longer sources; generate an extension only if required footage is missing |
