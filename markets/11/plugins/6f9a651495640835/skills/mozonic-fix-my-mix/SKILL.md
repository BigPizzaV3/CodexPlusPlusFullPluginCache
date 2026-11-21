---
name: mozonic-fix-my-mix
description: Use when the user asks what's wrong with a mix, wants it improved, or says "fix it" — interpreting Mozonic's analysis, running the DSP autofix (optionally with a genre flavor or a mastering pass), and delivering the corrected file.
---

# Analyze and fix a mix with Mozonic

## 1. Locate the mix

Find it with `mozonic_list_mixes` (or use a mix ID from an earlier response).
If the song is not in the library yet, direct the user to upload it in the
Mozonic app at https://app.mozonic.com first.

## 2. Read the analysis

`mozonic_get_mix(mix_id=...)` returns the analysis. Translate it for
a musician — talk about muddy low end, harsh highs, squashed dynamics, or
quiet loudness rather than raw numbers, and quote the numbers (LUFS, dB
ranges) as supporting evidence. Lead with the 2–3 findings that matter most.

## 3. Run the autofix

`mozonic_correct_mix(mix_id=...)`. Options:

- `genre` plus `genre_intensity` — for example, `genre="hiphop"` and
  `genre_intensity=0.5` to flavor the correction.
  Genres: pop, hiphop, rock, edm, rnb, acoustic, jazz, lofi, ambient,
  country (or none). Only add this when the user names a genre or vibe.
- `target_profile` — appends a mastering pass after correction
  (streaming_default, loud_streaming, club_loud, podcast, commercial_loud).
  Use when the user wants a release-ready file, not just a fixed mix.

The original audio is never overwritten — corrections create a new render, so
it is always safe to run.

## 4. Wait, then deliver

Correction is asynchronous: poll `mozonic_jobs_active` every 15–30 seconds and
only report completion when the job finishes. Then get the file:
`mozonic_download_mix(mix_id=..., download_type="corrected")` — or
`download_type="mastered"` if you passed a `target_profile` in step 3. Present
the presigned URL and mention it expires, so download promptly.

## 5. Close the loop

Offer the natural next steps: compare against the original
(`download_type="original"`), discuss the changes via `mozonic_chat`
(pass `mix_id` for context), or master it for release (see the
mozonic-master-a-track skill).
