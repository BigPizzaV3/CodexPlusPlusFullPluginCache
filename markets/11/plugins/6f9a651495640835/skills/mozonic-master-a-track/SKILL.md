---
name: mozonic-master-a-track
description: Use when the user wants a track mastered — "master this", "make it release-ready", "loud enough for Spotify/club" — covering target-profile choice and both mastering paths (standalone mastering mode, or mastering a mix already in the library).
---

# Master a track with Mozonic

## 1. Choose the target profile from what the user says

- Spotify / Apple Music / "streaming", or no stated target →
  `streaming_default` (the safe default)
- "as loud as possible on streaming" → `loud_streaming`
- DJ set / club / festival playback → `club_loud`
- spoken word / podcast → `podcast`
- ads / sync / broadcast → `commercial_loud`
- user gives custom specs → `custom` (standalone mastering mode only)

Say which profile you chose and why; ask only if genuinely ambiguous.

## 2. Pick the path

**A. The song is already in the Mozonic library as a mix** — master it via
correction: `mozonic_correct_mix(mix_id=..., target_profile=...)`,
then download with `download_type="mastered"`. (`custom` is not available on
this path.)

**B. A standalone mastering session already in Mozonic** — list sessions with
`mozonic_list_mastering_sessions`, render with
`mozonic_render_mastering_session(session_id=...)`, then download with
`mozonic_download_mastered_track(session_id=..., variant="mastered")`. Use
`variant="input"` to fetch the original for A/B comparison.

**C. A local file not yet in Mozonic** — the plugin cannot upload audio bytes.
Ask the user to upload it in https://app.mozonic.com, then continue using path
A or B once it appears in their library.

## 3. Deliver like a mastering engineer

Mastering is asynchronous — poll, don't claim early completion. When done,
present the download link (it expires), state the profile used, and offer an
A/B against the input. If the user dislikes the result, suggest a different
profile (e.g. streaming_default → loud_streaming) and re-run; each master is
a new render and nothing is overwritten.
