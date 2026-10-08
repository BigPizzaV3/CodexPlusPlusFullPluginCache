---
name: capture-demo-video
description: Record an app or screen for a product demo, with action timing when available for cursor animations or input badges.
---

# Capture a demo video

Choose a recorder that works with the app, machine, and available permissions. For a
local screen or window, use the bundled Cirro recorder or an existing setup. For
synchronized pointer events in a supported Chromium app, use the bundled Chromium
helper. See [recorder options](references/recorders.md) for commands, platform limits,
and alternatives.

For Cirro recording, follow [Set up Cirro](../setup/SKILL.md) to prepare its launcher.

For existing footage, continue with [Create Demo Video](../create-demo-video/SKILL.md).

## Choose how to record

Try to capture action timing by default using the available recorder or input tool
journal. Read [action timing](references/action-timing.md) before recording. Include
clicks, typing, shortcuts, scrolling, and dragging when supported; pointer movement
alone does not describe those actions. Keep partial logs and note what is missing.
If logging is unavailable, continue with the recording rather than blocking the task.
Never invent events or precise timestamps.

- **Keep the original cursor:** record it as part of the video. Captions, zooms, masks,
  and speed changes do not need an event log.
- **Animate the cursor:** record without the cursor and capture synchronized pointer
  events. Use input badges only for actual keyboard events.

If reliable event timing is unavailable, keep the original recording and edit without
those effects.

## Record the story

Choose the task and result you want to show. For a before-and-after comparison, perform
the same task on both versions with comparable app state and recording settings.

Before performing the walkthrough, make a short test recording and inspect it for
permission errors, black frames, and cursor visibility. Check input permissions too
when the walkthrough needs desktop control. If access is denied, use an available
permitted alternative or tell the user which app needs which permission and where to
enable it. After access changes, repeat the test before recording the full walkthrough.

On macOS, native screen or window recording may need approved execution outside
Codex's sandbox, even when Screen Recording consent is already granted. Follow the
[macOS permission guidance](references/recorders.md#macos-permissions-and-sandboxing)
and keep the exception limited to capture commands.

Keep the recording region and scale stable. Show a readable starting
state, perform the task, and leave the result on screen long enough to understand it.
Keep failed attempts and describe what happened.

When collecting events, start logging before the first interaction and align the log
with the video. Record timing uncertainty and protect sensitive input as described in
the timing reference.

Stop and finalize the recording. Stop only processes created for it and restore
temporary settings. Check the footage for missing frames, clipped UI, and private
content.

## Hand off to editing

Keep the original video with the recording settings, task, outcome, and version under
test. Include raw logs and clock and coordinate mappings when collected. Continue with
[Create Demo Video](../create-demo-video/SKILL.md), passing only trustworthy events in
the screenplay.
