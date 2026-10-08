# Recorder options

Use the application's existing capture support when it fits. Make a short test recording
and inspect it before recording a longer task. Capture audio if needed; Cirro produces
silent video.

## Record a local screen or window with Cirro

Follow [Set up Cirro](../../setup/SKILL.md) first. On macOS, also follow the
[permission guidance](#macos-permissions-and-sandboxing) below. On macOS/Linux:

```sh
sh /absolute/path/to/setup/scripts/cirro.sh record --list --json
sh /absolute/path/to/setup/scripts/cirro.sh record --window WINDOW_ID --duration-ms 5000 -o /absolute/path/recording.webm --json
```

On Windows, use `cirro.cmd` with the same arguments. Select a screen with
`--screen SCREEN_ID` or a window with `--window WINDOW_ID`, using an ID from the current
listing. Refresh the listing after display or window changes. If the walkthrough
includes dialogs outside the selected window, record the screen and check that the test
recording includes them.

Set `--duration-ms` to limit the recording, or omit it and stop the foreground recording
with Ctrl-C; the first interrupt finalizes it. The default is 30 fps with the system
cursor visible. Use `--cursor hidden` only when adding a separately recorded,
synchronized pointer. Cirro writes a silent WebM and an adjacent JSON file with a
screenplay-ready `recording` section and capture diagnostics; neither output may already
exist. It does not record pointer or keyboard events. Keep the JSON alongside the video,
and use the [action timing guide](action-timing.md) for a separate event journal.

Windows uses GDI; Linux requires an authorized X11 display. Native Wayland is unsupported,
so use an available Wayland-compatible recorder. Minimized, hidden, protected, or
GPU-only windows may not
produce usable pixels. X11 window capture stops if the window closes, is unmapped, or
shrinks below its original size.

### macOS permissions and sandboxing

Screen Recording consent and Codex's execution sandbox are separate. The sandbox can
block native capture services even when macOS consent is already granted, producing
`permission_required`. Repeated consent prompts or changing the cache path will not
resolve that sandbox restriction.

Use the execution tool's normal approval flow, or an existing matching grant, to run
Cirro's `record` commands outside the sandbox. This includes source listing and
permission requests. Limit the exception to those capture commands; keep inspection,
validation, and rendering in the normal sandbox. Keep the same verified launcher,
cache path, and output paths so the recording is available for editing afterward.

macOS Screen Recording consent is still required. `record --list` checks access without
prompting; `record --list --request-permission` requests it. Follow the OS prompt or
enable access in System Settings, relaunch if necessary, and repeat the short test
recording in the approved execution context.

If execution outside the sandbox is unavailable or denied, use an available permitted
recorder or ask the user for a recording made with Screenshot or QuickTime. Do not
disable sandboxing for the whole task.

## Other recorder options

| Environment | Recorder | What to check |
| --- | --- | --- |
| macOS desktop | Screenshot toolbar (Shift–Command–5), QuickTime screen recording, or an available screen-capture CLI | Save the original MOV or other output. Check permissions, the selected region, and cursor behavior. The start button or CLI launch is not a first-frame timestamp. |
| Windows desktop | Snipping Tool's recording mode or an existing desktop recorder | Check that the selected region includes popups and dialogs. Keep an input journal when event-driven effects are wanted. |
| Linux desktop | Desktop screencast UI, OBS, or another recorder compatible with the current X11 or Wayland session | Wayland capture may require a screen-sharing portal and user selection. Do not assume X11 capture works on Wayland. |
| Multiple desktop platforms | OBS display or window capture | Choose the source and cursor setting, avoid scaling the source, and check popups. Establish clock anchors separately unless the setup already records them. |
| Remote desktop or computer-use tools | Existing session recording or screenshots with actual capture timestamps | Export action coordinates and recording-relative times if available. Check their documented meaning; a tool response timestamp may mark completion rather than input injection. |
| Chromium development app | Existing Playwright/CDP page with the bundled capture helper | Records compositor frames and pointer events together; limited to the supported document and browser content. Keyboard input needs a separate journal. |
| Other recorder, camera, or existing file | Original file in its existing format | Inspect dimensions, frame timestamps, orientation, and decoding. Use a finalized file with readable duration metadata and correctly oriented decoded frames. |

Keep the original file. If orientation is stored only in rotation metadata, create an
intermediate with the rotation applied to its pixels before setting camera positions or
masks; check that a decoded frame is upright. For interrupted or streaming recordings
without duration metadata, finalize or remux a copy and check its duration and frame
timestamps before editing. If timing or geometry changes, update the event mapping to
match the intermediate.

For Chromium, read [the helper workflow](recording.md). Its Node.js and Playwright
prerequisites apply only to that method.

FFmpeg can capture from platform devices, but device names, permissions, and supported
encoders depend on the installed build. Check its device list and capture help before
constructing a command. Use a suitable available encoder and preserve source quality;
the recording need not be WebM. Do not install a new FFmpeg distribution just to match
an example. Cirro does not grant screen-capture access or log desktop input.

Platform setup references:

- [Apple screen recording](https://support.apple.com/guide/mac-help/take-a-screenshot-or-screen-recording-mh26782/mac)
- [Microsoft Snipping Tool](https://support.microsoft.com/en-us/windows/apps/use-snipping-tool-to-capture-screenshots)
- [GNOME screenshots and screencasts](https://help.gnome.org/gnome-help/screen-shot-record.html)
- [OBS sources](https://obsproject.com/kb/sources-guide)
- [FFmpeg capture devices](https://ffmpeg.org/ffmpeg-devices.html)
