---
name: map-audio
description: Play an attached recording, inspect its waveform, spectrogram and browser-measured loudness, loop and annotate its timeline, process it through an MFX effect preset, or open PAM, MAP Audio's sampler and sequencer, to play and change a beat in the conversation.
---

# MAP Audio

## Recordings

Use `open_audio_workspace` to open the player. Use `open_demo_audio` when the user
wants to try the supplied synthetic example without attaching a recording. For a recording attached by the user,
call `display_audio_file` with the host-provided file object. Reuse the returned
`audioId` for later playback, region and annotation changes. Never invent a download
URL, file ID, audio ID or server path. `read_audio_chunk` is an app-only byte-transfer
tool; audio bytes should not be placed in conversation text. ChatGPT's desktop app calls
`view_audio_file` itself when the user opens a WAV, FLAC, MP3 or M4A file in the file viewer;
do not call it.

The browser publishes measured statistics, playback position, selected regions and
annotations to the conversation. Use that context when available; wait for analysis
or say a measurement is unavailable instead of inventing values. Measurements and
waveforms do not establish that you listened to a recording.

## PAM

Use `open_pam` when the user wants to make or hear a beat, or to try PAM. When they
name a style, mood or tempo, call `list_pam_presets` first and pass the closest preset's
slug; `open_pam` also takes a variation from 1 to 8 (with a preset) and a tempo in BPM. A new PAM
starts silent: tell the user to press Play inside PAM. The widget reports the loaded preset,
tempo, variation and whether PAM is playing. Describe only what it reports.

When `open_pam` returns a `pamId`, the control tools act on that PAM: `get_transport`,
`start_transport`, `stop_transport`, `full_stop_transport`, `set_bpm`, `load_variation`,
`cancel_queued_variation`, `randomize` and `load_preset`. Pass the `pamId` of the PAM the user
means. `start_transport` works only after the user has pressed Play inside that PAM once.

PAM in ChatGPT runs its browser engine with MAP Audio's presets. It cannot load the
user's own samples, save presets, export audio or control the desktop plugin. Calling
`open_pam` again opens a second PAM; when one starts playing, the others pause.

## MFX

Use `apply_mfx_preset` when the user wants a recording processed with effects (a vocal chain, drum bus,
reverb, distortion, a mix-bus treatment) and does not need MFX itself open. Call `list_mfx_presets` first,
narrowed with a `category` or `query` from the request, and pass the closest preset's slug, with the
attachment or an `audioId`; a variation from 1 to 8 and a tempo for synced effects are optional. Recordings
up to 32 MiB and five minutes (about three minutes of WAV). The widget renders the audio, lets the user compare it with the original and download
it, and reports the processed copy's own `audioId`: pass that to `display_audio_file` to show its loudness.
Until the widget reports it, the processing has not finished; describe only what it reports.

## Scope

Every tool needs the user's MAP Audio account, which ChatGPT asks them to connect. Controlling
PAM from ChatGPT comes with a PAM licence on that account; without one, `open_pam` returns
`control: "not_included"` and the control tools say so. Then the user can still play PAM by hand.
Processing with `apply_mfx_preset` comes with an MFX licence the same way; listing MFX presets does not.
State that plainly and give the link the tool returns; do not mention prices, plans, discounts or
upgrades, and do not offer to buy anything. MAP Audio does not generate sound with AI and has no
checkout, activation or model downloads here. Do not call tools that the connected server does not expose.

Audio IDs and download links are private capabilities and expire after one hour.
Keep them in this conversation. Ask for a fresh attachment when a file expires.
Direct support questions to https://map.audio/contact and privacy questions to
https://audio.map.audio/privacy.
