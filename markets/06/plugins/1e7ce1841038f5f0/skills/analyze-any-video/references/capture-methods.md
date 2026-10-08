# Authorized capture methods

## Choose the least lossy available source

1. Original local/uploaded video with audio.
2. Publicly accessible source file plus official captions.
3. Browser playback that the user is authorized to view, captured with supported browser or operating-system tools.
4. User-provided screen recording with system audio.
5. Separate audio, transcript/subtitles, and timestamped screenshots.
6. Public page metadata only.

## Local media

Use `scripts/extract-video-evidence.sh INPUT OUTPUT_DIR [INTERVAL_SECONDS]`. It creates technical metadata, interval frames, scene-change frames, and a manifest; a mono analysis audio track is created only when an audio stream exists. For silent videos the manifest reports `audio_status=ABSENT` and an empty `audio` path, while visual extraction continues. Preserve the original file. Do not overwrite it.

If speech transcription is available through a callable tool, transcribe the extracted audio with timestamps and speaker labels when reliable. Otherwise use supplied captions or clearly state that speech was not transcribed.

## Public webpages

Use a browser tool to inspect what is actually rendered. Prefer official transcript/caption controls and page metadata. Screenshots capture visible frames, not sound or the full temporal sequence.

If the environment supports authorized screen and system-audio recording, confirm the target window, duration, notification/privacy implications, storage location, and user permission before starting. Stop immediately if private material outside the target appears.

## Protected or private sources

Do not defeat DRM, paywalls, authentication, CAPTCHAs, regional restrictions, download controls, or anti-bot mechanisms. A user-provided lawful screen recording or exported file is the fallback. Recording permission and copyright rules vary by context and jurisdiction; flag uncertainty rather than giving definitive legal advice.

## Coverage strategy

- Inspect the opening densely: 0–3, 3–10, and 10–30 seconds for short-form content.
- Capture fixed-interval frames across the entire duration.
- Add scene-change frames and frames around transcript topic changes.
- Inspect the ending and CTA densely.
- For long videos, create chapters first, then sample each chapter and inspect high-impact passages.
- Increase sampling when cuts are faster than the interval or on-screen text changes rapidly.

## Evidence log

Record source, capture date, duration, dimensions, audio availability, caption source, frame strategy, covered segments, failures, and transformations. Mark browser-derived titles/descriptions separately from video evidence.
