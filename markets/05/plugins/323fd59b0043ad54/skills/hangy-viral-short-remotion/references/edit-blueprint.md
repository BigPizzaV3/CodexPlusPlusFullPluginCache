# Viral Short Edit Blueprint

## Source analysis

For each source, record:

- path and immutable source name;
- duration, resolution, orientation, frame rate, video/audio codec;
- stable opening and closing trim points;
- key visible action and usable reactions;
- speech confidence and music/crowd interference;
- blur, black frames, duplicated frames, or camera shake.

Create a contact sheet that samples the full clip, then create denser sheets around candidate moments. Use waveform, scene-change, and RMS analysis as navigation aids rather than editorial truth.

## Timeline grammar

Use a four-part arc unless the material supports a better one:

1. Hook: show the strongest close-up, action, or question immediately.
2. Context: establish who or what is happening in one or two beats.
3. Payoff: reveal the widest, funniest, most emotional, or most informative moment.
4. Exit: land on a clean image or compact call to action.

Prefer action-matched cuts. Alternate close and wide views when sources allow. Use 8-16% punch-ins as a starting range, then inspect faces and edge cropping. Do not use zoom merely to fill time.

## Overlay rules

- Write one idea per overlay.
- Keep Korean copy concrete and visually verifiable.
- Use two lines only when necessary.
- Keep lower text above platform controls.
- Keep text duration long enough for a phone read at normal speed.
- Reuse a restrained palette, typography scale, and entry motion.
- Avoid subtitles derived from low-confidence transcription.

## Remotion structure

Keep reusable timeline data separate from components:

- `SEGMENTS`: source, source in/out, timeline start, duration, crop, scale, and optional motion.
- `CALLOUTS`: start, duration, text, emphasis, and placement.
- Shared components: media frame, overlay, progress rail, transition accent, and safe-area guide.

Use frame-based animation APIs and Remotion media primitives. Do not use CSS keyframes or nondeterministic timers.
