---
name: map-audio
description: Analyse an attached recording's tempo, key, loudness against streaming targets, tonal balance, stereo and sections with MAP Audio's own engine, compare it with its source or reference tracks, play it with its waveform and spectrogram, loop and annotate its timeline, master it with Master Sculpt, process it or a built-in loop through an MFX effect preset, open PAM, MAP Audio's sampler and sequencer, to play, change and export a beat in the conversation, or render MAP Audio presets, drum hits and CM-FX and CMI programs through the Music API.
---

# MAP Audio

## Analysis

Use `analyze_audio` when the user asks about a recording's tempo or BPM, key, loudness or LUFS, how loud it is
for Spotify, Apple Music or YouTube, true peak or clipping, low end or brightness, stereo width or mono
compatibility, or its sections. Pass the attachment or an `audioId`. Quote its numbers and notes instead of
estimating, offer `tempo.alsoReadAs` when the user hears the tempo at half or double, and say a value is
unavailable when it is null. It reads WAV, AIFF, FLAC and MP3 up to 32 MiB and ten minutes; for anything else,
pass on its error. Measurements do not mean you listened to the recording, and they cannot identify a song,
an artist, lyrics or a genre.

`analyze_audio` takes one extra per call. `compare` (an attachment) or `compareId` (an `audioId`) is the recording this
one was made from, such as the dry take behind a processed file; the result adds `comparison`, whose verdict says
whether the two are identical, differ in level only, by a linear change, are out of alignment (call again with the
`latency` it suggests) or differ otherwise. `references` or `referenceIds` (one to three reference masters) add
`triage`, where the mix leaves their envelopes, worst first. `spectrogram: true` adds a PNG and a series of 16 windows
of band energy and stereo correlation; `windows` (1 to 64) gives the series alone. In ChatGPT a compared file may
run up to five minutes, and a mix and its references up to three each (less above 44.1 kHz).

After an analysis, offer its `suggestions`: `open_pam` with a suggested preset at the recording's tempo, or
`apply_mfx_preset` with a suggested MFX preset, passing its `bpm` when it has one.

## Recordings

Use `open_audio_workspace` to open the player. Use `open_demo_audio` when the user
wants to try the supplied synthetic example without attaching a recording. For a recording attached by the user,
call `display_audio_file` with the host-provided file object. Reuse the returned
`audioId` for later playback, region and annotation changes. Never invent a download
URL, file ID, audio ID or server path. `read_audio_chunk` is an app-only byte-transfer
tool; audio bytes should not be placed in conversation text. ChatGPT's desktop app calls
`view_audio_file` itself when the user opens a WAV, FLAC, MP3 or M4A file in the file viewer;
do not call it.

The player analyses the recording it opens and publishes that analysis's summary, the playback
position, selected regions and annotations to the conversation. Use that context when available;
call `analyze_audio` for the full measurements, or say a measurement is unavailable instead of
inventing values. Measurements and waveforms do not establish that you listened to a recording.

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

With the same `pamId`:

- `set_parameters` sets PAM's parameters by id. Look ids, ranges and units up with `get_parameter_info` first. A value
  outside its range is refused, and so is the whole call, with nothing written. An effect's `cellN_<effect>Enabled`
  flag takes 0 or 1. A `macro_*` id does not switch its macro on. The answer says which values PAM holds. A preset
  still loading in PAM, or one that starts loading during the write, refuses the call: make it again once it has loaded.
- `load_sample` loads an attachment or an `audioId` into a cell (`cellId` 1 to 8): up to 32 MiB and five minutes.
- `export_audio` records what PAM plays, 1 to 16 bars (default 4), as a WAV with its own `audioId` and a one-hour
  download link. It records in real time from the next bar line and starts a stopped transport, so it needs the user
  to have pressed Play once. Bars that would run past five minutes at PAM's tempo, or past the 96 MiB the app stores,
  are refused before anything records: ask for fewer. `export_preset` saves the open preset as a `.preset` file with a one-hour download link;
  no audio tool opens it.

With the same `pamId`, `get_cmfx` and `set_cmfx` read and write a cell's CM-FX effect program, and
`get_cmi` and `set_cmi` a cell's CMI instrument program. Call `list_cm_operators` for the cmfx/1
format, its operators and the factory effects and starter instruments, start from the nearest one,
and check a new program with `check_cm` before writing it. A program the compiler refuses comes
back with every problem and is not written.

PAM in ChatGPT runs its browser engine with MAP Audio's presets. It cannot host plug-ins, run PAM's AI
models or control the desktop plugin. Calling `open_pam` again opens a second PAM; when one starts playing, the
others pause.

## MFX

Use `apply_mfx_preset` when the user wants a recording processed with effects (a vocal chain, drum bus,
reverb, distortion, a mix-bus treatment) and does not need MFX itself open. Call `list_mfx_presets` first,
narrowed with a `category` or `query` from the request, and pass the closest preset's slug, with the
attachment or an `audioId`; a variation from 1 to 8 and a tempo for synced effects are optional. Recordings
up to 32 MiB and five minutes (about three minutes of WAV). The widget renders the audio, lets the user compare it with the original and download
it, and reports the processed copy's own `audioId`: pass that to `analyze_audio` to measure it or `display_audio_file` to show it.
Until the widget reports it, the processing has not finished; describe only what it reports.

To hear a preset without a recording, pass `loop` instead: `break`, `bass`, `synth`, `vocal` or `pulse`, with
`bars` (1 to 16, default 4) or `seconds` (up to 30), never with `bpm`. The widget renders and plays the loop and
stores nothing: there is no `audioId` or download.

## Mastering

Use `master_audio` when the user asks to master a mix, make it louder for streaming or match reference tracks.
Pass the attachment or an `audioId`, and up to three references (attachments or `referenceIds`). The defaults are
-14 LUFS and a -1 dBTP ceiling; `lufs` and `ceilingDbtp` change them. It reads mono or stereo WAV, AIFF, FLAC and
MP3 up to 32 MiB and three minutes at 44.1 kHz (less at higher sample rates), references too, and stores a 24-bit
master under its own `audioId` with a download link. The player opens the master with the report under it (moves,
loudness, each constraint as measured, and the references' findings, each with a button that asks for a master that
holds it); `analyze_audio` measures it further. Quote the result's moves, levels and each constraint's predicted and measured value, and read its
notes out: a true-peak limiter holds the ceiling, checked at 16x oversampling, so a loud target is reached by limiting;
`limiterReductionDb` says how hard it limited, and the notes name a target the renders did not reach.

References change nothing on their own. The result's `triage` lists where the mix leaves their envelopes, worst
first; to act on a finding, call `master_audio` again with the same files and a constraint of bound `envelope`,
such as `{id: "top", metric: "bandLevel", channel: "mid", bands: [4000, 12500], bound: "envelope", hardness:
"soft", weight: "agreement", reason: "brighter than the references"}`. Every constraint needs a `reason` that
says what the user asked for. At most four constraints may be hard, counting a hard loudness target; bound section classes or the whole track, not a
time range.

## Music API

`search_presets`, `get_preset`, `preset_render`, `synth_drum`, `cm_render`, `pattern_generate`, `get_credits`,
`get_job` and `cancel_job` use the MAP Audio Music API. They work only for an account with Music API access, which is
invite-only. Use `preset_render` when the user wants a PAM factory preset rendered to WAV: find its slug with
`search_presets` (web PAM's preset slugs are not the same list). It draws on the account's own render-minutes, which
`get_credits` reports. `synth_drum` renders drum hits with PAM's drum synths. `cm_render` renders a cmfx/1 program,
a CM-FX effect over a test signal (`stimulus`) or an instrument from `notes`, and returns its level, spectral
centroid, tail, trips and warning codes, with no PAM open and no render-minutes: check the program with `check_cm`
first, since a refused one renders nothing and the answer does not list its problems. Quote its measurements; they
do not mean you listened to it. `pattern_generate` returns drum and bass patterns; its MIDI file stays with the
Music API account. A render still running after 45 seconds returns
`status: "pending"` with a `jobId`: call `get_job` with that value as `id` until it finishes, then the audio opens in the player under its
own `audioId`. An identical call within five minutes returns the same job, so change the `seed` for another take.
Quote the licence sentence the result gives. When a tool says the account has no access, has not accepted the terms
or has no render-minutes left, say so, with the documentation link when the tool gives one. When it says the
connection was approved before it covered the Music API, tell the user to disconnect MAP Audio in ChatGPT and connect
it again.

## Scope

The player, `analyze_audio`, the PAM and MFX preset lists, `open_pam`, `get_parameter_info`, `list_cm_operators`,
`check_cm` and `apply_mfx_preset` on a built-in loop or the example need no sign-in. Controlling or exporting from PAM, MFX on the
user's own recordings, `master_audio` and the Music API tools need the user's MAP Audio account. Called signed out,
such a tool answers that the user is not signed in, and ChatGPT offers the sign-in: tell the user, then call it
again once they have signed in. Signed out, `open_pam` returns `control: "sign_in"` and no `pamId`; the user can still
play PAM by hand, and a PAM opened after signing in can be controlled. No tool needs a PAM or MFX licence.
Do not mention prices, plans, discounts or upgrades, and do not offer to buy anything. MAP Audio does not make
songs, vocals or sounds from a text prompt, and has no checkout, activation or model downloads here. Do not call
tools that the connected server does not expose.

Audio IDs and download links are private capabilities and expire after one hour.
Keep them in this conversation. Ask for a fresh attachment when a file expires.
Direct support questions to https://map.audio/contact and privacy questions to
https://audio.map.audio/privacy.
