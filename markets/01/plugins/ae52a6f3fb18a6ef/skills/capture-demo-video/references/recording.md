# Record a Chromium app

This optional Chromium adapter is one way to record a demo. See
[recorder options](recorders.md) for other methods and [action timing](action-timing.md)
for timing journals.

Use this workflow to record a Chromium-based app. It requires Node.js and an existing
Playwright `page` connected to the app through the Chrome DevTools Protocol (CDP).
Follow the app's documented launch and automation setup. Launch Playwright and connect
to the app before recording.

Choose what to show before recording. Keep setup outside the footage, capture only the
intended app, and restore temporary settings afterward. Keep original recordings and
failed attempts. Stop only the recorder and app processes created for this task.

## Capture frames and pointer events

Import [capture.mjs](../../create-demo-video/scripts/capture.mjs) in the Node.js process
that owns the Playwright page. Use a new absolute capture-directory path whose parent
already exists. Call `startCapture(page, directory)` and wait for it to return before
performing the task with normal Playwright input. Call
`capture.stop(task, observedOutcome)` in a `finally` block, keeping the page open until
it finishes. Describe failed or incomplete tasks accurately in the outcome.

The helper hides the source cursor and records renderer frames and trusted pointer
events together, keeping their original timestamps. It supports one stable top-level
document. Do not navigate, reload, resize the viewport, or use pinch zoom during
capture. It does not capture native window chrome, operating-system dialogs, or input
inside iframes. It does not log keyboard events or typed text.

After recording starts, move the pointer to a harmless visible location so its initial
position is observed. Move to the target, pause briefly, then click with real Playwright
input. Show a readable starting state, meaningful intermediate states, and the result.
Leave states such as a search query, its results, or an open menu visible long enough to
understand; 1.5–2 seconds is a useful starting point. Do not slow every routine click or
typing character.

## Encode the recording

Use the Cirro launcher described in [Set up Cirro](../../setup/SKILL.md). On
macOS/Linux:

```sh
sh /absolute/path/to/setup/scripts/cirro.sh encode-capture /absolute/path/capture/manifest.json -o /absolute/path/capture/recording.webm
```

On Windows, pass the same `encode-capture`, manifest, and `-o` arguments to `cirro.cmd`.
This produces `recording.webm` and `recording.json`. Copy the `recording` section from
that JSON into the
[screenplay](../../create-demo-video/references/screenplay-contract.md). The encoder
scales CSS coordinates to actual recorded image dimensions and uses the first compositor
frame's timestamp as video time zero. It samples at 30 fps, holding the last observed
frame through static periods for their recorded duration. Original events remain in
`manifest.json`.

The editor uses these synchronized events to animate the cursor, including movement,
rotation, glow, and click bounce. Movement between observed positions is stylized; it
does not represent the exact physical mouse trajectory.

## Review and edit

Check the recording for missing or unreadable states. Re-record a task that moves too
quickly, keeping the earlier attempt. Keep the task, observed outcome, capture settings,
original frames, and event manifest together so timing and source evidence remain
traceable.

For footage from another recorder, obtain synchronized pointer data and cursor-free
frames before using an animated cursor. Recording-process launch time is not necessarily
first-frame time, and a screen recording alone does not provide pointer metadata. Do not
invent positions or timestamps from screenshots.

Continue with [Create Demo Video](../../create-demo-video/SKILL.md).
