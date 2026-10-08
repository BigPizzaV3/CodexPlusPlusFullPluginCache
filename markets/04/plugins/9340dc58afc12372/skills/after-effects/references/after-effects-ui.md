# After Effects playbook

> **Observe, never assume.** Panel layout depends on workspace and version. These are
> landmarks, not coordinates. Trust the screenshot over this file.

## Landmarks

| Task | Look for |
|---|---|
| Import | **File > Import > File** |
| Project contents | The **Project** panel |
| The comp | The **Timeline** panel, tabbed by composition name |
| Comp settings | **Composition > Composition Settings** — frame rate, duration, size |
| Text | The **Type** tool, or **Layer > New > Text** |
| Keyframes | The stopwatch beside a property in the Timeline |
| Precomp | Select layers, **Layer > Pre-compose** |
| Render | **Composition > Add to Render Queue**, or Add to Media Encoder Queue |

## Read the comp first

Open Composition Settings and note three numbers: **frame rate, duration, frame size**.
Use these as the output target. Inspect scaling and timing when source settings differ;
do not change an existing composition's settings just to match one imported asset.

## Layer discipline

Build bottom to top and name as you go:

```
Text / CTA            <- live text layer, keyframed
Text / Headline       <- live text layer, keyframed
Logo                  <- placed asset or 3D reveal
Plate                 <- generated background/footage
```

Placed assets land wherever the playhead is — check the start time, don't assume zero.

## Animating text

1. **Layer > New > Text**, type the real copy.
2. Animate with **Text > Animate** properties (Position, Opacity, Scale) rather than
   keyframing the whole layer's transform — it's what the property group is for and it
   stays editable.
3. Keyframe entrance and exit separately so timing can be retuned.
4. Ease keyframes — linear motion reads as cheap. **F9** for Easy Ease.

## Standard timings

| Element | Entrance | Hold | Exit |
|---|---|---|---|
| Headline | 12–18 frames | 2–3 seconds | 10–12 frames |
| Lower third | 15 frames | 3–4 seconds | 12 frames |
| Logo reveal | 20–30 frames | 1–2 seconds | hold to end |

Adjust to the comp's frame rate — these assume 24–30fps.

## Precomps

Group related layers before the timeline gets long. A comp with 30 loose layers is not
something a designer will want to inherit. Name precomps for what they contain.

## Rendering

1. **Composition > Add to Render Queue** (or Media Encoder for H.264).
2. Set output module and destination path.
3. Start the render.
4. **Wait and confirm the file exists.** A queued render is not a finished one.

## Saving

**File > Save As** to a new project filename. Never save over the user's project.

## Verification checklist

- [ ] Mixed-rate footage plays correctly at the comp frame rate
- [ ] Every layer named
- [ ] Text layers still live and editable
- [ ] Keyframes eased, not linear
- [ ] Related layers precomped
- [ ] Only requested layers changed; new layers do not obscure unrelated content
- [ ] Project saved under a new name
- [ ] Render confirmed on disk

## Known failure modes

| Symptom | Cause | Fix |
|---|---|---|
| Motion stutters | Possible cadence or timing mismatch | Preview and inspect timing; retime or interpret only if appropriate |
| Animation reads cheap | Linear keyframes | Easy Ease, adjust spacing |
| Text can't be edited later | Generated image of text, or converted to shapes | Rebuild as a live text layer |
| Render "done" but no file | Queued, never started | Check the queue, confirm on disk |
| Layer appears late | Placed at the playhead, not at zero | Check and set the layer start time |
