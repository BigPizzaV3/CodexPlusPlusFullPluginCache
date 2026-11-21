---
name: scorestarling-notation
description: Turn sheet music into an editable, playable ScoreStarling score and convert music between forms. Sources include a photo, scan or PDF of printed music, jianpu (numbered notation), a lead sheet or chord chart, a MusicXML, MIDI or ABC file, or music typed, described or written in the chat. Outputs include MIDI, audio, PDF, MusicXML, ABC, MEI and jianpu. Use with a connected ScoreStarling MCP server whenever music arrives as notation rather than as a recording.
---

# Sheet music and notation to a score

Use the connected ScoreStarling tools. A score made here is a normal ScoreStarling project: it
plays back, opens in the score panel, takes the same edits (`edit_score`) and exports to every
format. Recordings (audio or video) follow the `scorestarling-score` skill instead.

## Reuse an existing score or saved result

When the user says “reuse the existing result” or “do not start new processing”, first
use `list_scores` and `open_score`. Opening a finished score needs no upload, audio check
or new transcription. Do not ask for information already recorded in that score.

Only if the user explicitly wants a **new score from a saved Pro result**, use the original
recording or `transcribe_again`, with `provider: mirelo`, instrument review enabled and
`replay_only: true` **at creation**, before the first review. This is available only to enabled
replay accounts. Never require the user to say internal parameter names.

Read `get_pro_instrument_review(start=false)` first. Match the complete historical
`instruments` and flat `pro_options`, including tempo, meter, subdivision, timing and paper;
the candidates already verify this account, original bytes and decoded duration. Different
choices need a different saved result. If no candidate matches, stop and offer to open the
existing score. Do not start fresh detection, processing or another upload.

Confirm matching choices with `confirm_pro_instruments(replay_only=true)`, then read back
the saved guard. If a quote is required, ask once for consent to its exact product credits;
permission to reuse is not payment consent. Keep the same excerpt length; a shorter quote needs its
own matching saved result. Follow the same job and verify the completed
result includes `replayed_from`. Explain this as reusing a saved result, in ordinary language.

## Preserve and audit source corrections

For PDF/OCR drafts, prefer source-supported local edits over replacing correctly read music.
Keep the original draft. If missing notes or ties require a `create_score` replacement, compare
**all** pitch and rhythm changes between the new and old scores against enlarged original pages.
Check clef, key, staff position, accidentals, grace notes and ties, with the preceding and following
bars. A structurally valid score or a model calling it “corrected” is not proof of source fidelity.
Until those changes have been checked, report the remaining uncertainty rather than complete accuracy.

## Choose the way in

| What the user has | Do this |
| --- | --- |
| A clean PDF or flat scan of printed music, especially piano or several pages | Upload it like a recording (`transcribe_attachment`, `prepare_audio_upload`, `transcribe_link` for a link to the file, or the panel). The server's sheet-music reader takes about 30–50 seconds a page |
| A phone photo, a lead sheet with chord symbols, jianpu, handwriting or a single short page | Read it yourself, write ABC ([references/abc.md](references/abc.md)) and call `create_score` |
| A MusicXML, MXL, MIDI or ABC file | Upload it as it is; a short ABC text can also go straight to `create_score` |
| Music typed or described in the chat, or music you compose or arrange on request | Write ABC and call `create_score` |

These defaults come from measured readings (docs/sheet-music.md in the ScoreStarling
repository). On clean printed pages the reader was as accurate as the best assistants and much
faster. On a real piano page exported from Sibelius it agreed with the assistant's reading on
93.5% of notes and was right in 8 of the 10 bars where they differed. It cannot read jianpu, it
lost the bar structure of a lead sheet, and it read phone photos badly. Strong assistants read
melodies, lead sheets, jianpu and chorales almost perfectly. Dense piano photos stayed hard for
everyone, so read those bar by bar and check carefully. When the user offers both a photo and
a PDF of the same music, upload the PDF.

Uploaded sheet music and score files are read, not transcribed: skip `check_recording`, and
the engine choice and tempo detection do not apply; nothing is paid. A tempo the user gives
(`bpm`) sets playback for a score that marks none. Follow the job with `get_upload_status`
(`wait_seconds: 20`) until it finishes, then do what its `next_step` says.

## Reading the music yourself

1. Look at the whole page first: title, composer, key signature, time signature, tempo mark,
   instruments, number of systems and bars, repeats, pickup. Write them down.
2. Write ABC bar by bar, one line per printed system, with a `%` comment naming its first bar
   number, so you can check it against the page. Copy every accidental the page shows; like
   staff notation, an ABC accidental lasts to the end of its bar, so a later note in the same
   bar written without one keeps it. Count ledger lines from a known note (middle C sits on the
   first ledger line below the treble staff and above the bass staff).
3. Check each bar's beats add up to the time signature, except a pickup and the bar that
   completes it.
4. Call `create_score` with the ABC and the title. Its `warnings` list notation it could not
   read and bars whose lengths do not match the time signature.
5. Call `review_score` and compare its picture with the source bar by bar: pitches,
   accidentals, octaves (bass notes especially), rhythms, ties, tuplets, chord symbols, key
   and time signatures. The picture lays bars out differently from the page, so compare by
   bar number and zoom in with `measures` (`"9-12"`).
6. Fix what differs: `edit_score` for a few notes, with operations such as
   `{"action": "set_pitch", "note_ids": ["<id from get_score>"], "pitch": 62}`, `set_duration`,
   `delete_notes`, `add_chord_tone` or `set_clef`; for many errors, correct the ABC, call
   `create_score` again, then `trash_score` the first attempt. Change a note only where you can
   count its line or space in the source; a note that merely looks higher or lower than in the
   review picture is not enough. In a test on a blurry photo, corrections made by comparing
   shapes turned four right notes wrong. Corrections that make the score match its source are
   part of what the user asked for, so apply them directly rather than as previews. Tell the
   user which bars you were unsure of; when the source is too blurry to count lines, ask for a
   sharper, straight-on photo or a PDF rather than guessing.

For jianpu, `1=C`-style keys give the tonic: map the digits to scale degrees in that key,
dots above or below to octaves, underlines to eighths and sixteenths, dashes to held beats.

## After an upload is read

The imported result is an editable starting score. Preserve the source and reversible
revisions; the goal is faithful, clear, playable notation, not merely a passing validator.
The status says how many bars, parts and notes were read. Call `review_score` and compare its
picture with the original page (the user's file, or ask them to share a picture when you have
none). The reader's typical slips: a missed natural or courtesy accidental, a doubled note in
a chord, a lost tie, and text it cannot read. Correct them with `edit_score` and say what you
changed. If the reader failed or most bars are wrong (a photo, jianpu, handwriting), read the
page yourself as above. `review_score` does not compare the source automatically;
`doubtful_notes` is unavailable for notation imports, which says nothing about accuracy.
Use [the review reference](../scorestarling-score/references/good-score.md) as conditional
checks, not rules that override written opening rests, syncopation, inner voices or ornaments.

Apply clear source corrections and reversible edits within the user's stated goal directly.
When the user asks for faithful or playable music, finish clear source-supported fixes before
ending the turn; listing known missed notes or ties and waiting for another prompt leaves
that request unfinished. If supported edits cannot express the repair, reconstruct ABC only
when the source and required markings are readable, preserve the draft, and check the replacement.
Ask one specific question only when the source leaves a consequential musical choice unclear.
Preview a new arrangement or interpretation outside that goal and apply only after its
acceptance. Keep a faithful master when making a learner version. Read the current
operations guide: precise local voice/staff assignment and dedicated tuplet, tie/slur,
grace-note, swing or pedal entry are not available. Do not invent actions or reengrave
an import to bypass that limit. If rewriting ABC, verify coverage and supported markings
before replacing a version; do not discard the first attempt until the replacement is checked.
Inspect all exported pages, compare changed bars with the written source and audition
playback when available; report uncertainty and unverified exports explicitly.

## Converting

Once a score exists, `export_score` gives every other form of it:

| Wanted | format |
| --- | --- |
| MIDI for a DAW or practice app | `midi` |
| Listening audio | `mp3` or `wav` (General MIDI instruments) |
| Printable sheet music | `pdf`; `pages` for SVG and PNG images; `parts` for one PDF per part |
| Notation software (MuseScore, Sibelius, Finale, Dorico) | `musicxml` or `mxl` |
| Jianpu (简谱) | `jianpu` (every staff) or `jianpu_melody` (top line only; it may not be the melody), in the key; `jianpu_fixed` for 1=C fixed do (固定调) |
| ABC text | `abc`; the text also comes back in the result, so you can read, explain or rewrite it |
| MEI for music research and editions | `mei` |

Jianpu's `1=` follows the score's key signature (movable do; a minor key as its relative major).
`jianpu_fixed` keeps the same pitches in 1=C, each black key marked (b5 for G-flat). Music
printed without a key signature, every accidental written out, comes out as 1=C; when it is
clearly in another key, offer `set_key` so the jianpu reads in that key. For A minor,
`1=C` means the tonic is 6; it does not mean A major. Use full `jianpu` for both hands;
check every staff's digits, octave dots, rhythms and key changes in the exported result.
Changing the notation view does not simplify the music or prove multi-voice export fidelity.

Transpose with `edit_score` `transpose_score` (an interval such as `M2` or `-m3`) so the score,
playback and exports stay consistent; change the playback instrument with `set_timbre`. To
arrange or simplify music, export `abc`, rewrite it, and `create_score` the new version. Share
the returned download links; they expire. For arrangements read [the arranging reference](../scorestarling-score/references/arranging.md).

## Limits

Repeats play once, as written. Playback uses the score's first tempo and any later tempo marks;
without one it plays at 100 quarter notes per minute. Scores from notation are not re-engraved
(re-engraving rebuilds notation from playback); edit their notes instead. Up to ten minutes of
music per score, 50 MiB per file and twelve pages per PDF. Drum tracks in a MIDI file are left
out of the notation.

<!-- BEGIN MCP ESSENTIALS: scripts/sync_workflow_guidance.py -->
## Shared MCP essentials

Use the connected host's authorized tools and respect its file, network and approval boundaries. Guidance grants no account access, upload consent, supplier spending or acceptance of a proposal. Never invent file references, expose upload capabilities or discover credentials.

When the user says reuse the existing result or do not start new processing, first list_scores and open_score; do not upload, check_recording or transcribe_again merely to reopen a score. Only for an explicitly requested new score from a saved Pro result, use the original upload or transcribe_again with provider=mirelo, review_instruments=true and replay_only=true from creation (enabled replay accounts only). Read get_pro_instrument_review(start=false) first. replay_candidates verify this owner, original bytes and decoded length; compare every historical instrument and flat pro_options with the requested choices. No matching candidate means stop and offer the existing score; never start detection, fresh processing or a replacement. Confirm matching complete choices with replay_only=true, then read back pro_review.replay_only=true. Keep the same excerpt length; a shorter quote needs its own matching saved result, otherwise stop. If a quote is required, ask once for its exact product credits; reuse permission is not payment consent. Follow the same job and verify completed.replayed_from. Explain saved-result reuse in plain words; the user does not need to name internal fields.

Sheet music and score files (PDF/images, MusicXML/MXL, MIDI, ABC) use the same upload paths but are read, not audio-transcribed: skip check_recording; no engine choice, tempo detection or provider fee applies. Use local for their upload route. Clean PDFs/flat scans suit the reader. For phone photos, handwriting, jianpu or lead sheets, read the source and write ABC with create_score; also use create_score for music typed/described/composed in chat. Prefer a PDF when both are given.

Poll get_upload_status(job_id, wait_seconds=20) in this turn until terminal; never reupload or finish with an ID or request to keep waiting. Give brief plain progress. HTTP 202 is acceptance, not completion. Inspect the original job after ambiguous responses; never blindly retry a mutation or paid job. On failed/needs_review follow can_recover/next_step: pending instruments and quotes need explicit approvals; recover_pro_result resumes the same accepted Pro task; otherwise stop for review. Quota estimates are not billing receipts.

After reading or create_score, call review_score and compare its page picture with the source bar by bar: pitches, accidentals, octaves, rhythms, ties, key/meter and chord symbols (measures="9-12" zooms in). For a playable/faithful score, correct clear misreadings before finishing; do not merely list errors and wait for another user prompt. Use edit_score for supported changes. If unsupported missing notes or ties require ABC reconstruction, preserve the draft and compare the replacement with the source and playback. Prefer source-supported local edits to preserve correctly read music. If create_score replaces a draft, compare every new-versus-old pitch/rhythm change against enlarged original pages: clef, key, staff position, accidentals, grace notes, ties and neighbouring bars. Preserve the draft. Validation and a model calling it corrected do not prove fidelity; unverified changes remain uncertain, so do not declare complete accuracy. Change notes only where the source supports them, never by comparing shapes alone; report uncertain bars and ask for a clearer source when needed. Do not reengrave notation imports from playback. bpm supplies playback tempo when needed; report the score/file tempo or the 100 BPM fallback, never a detected audio tempo.

A provider result is an editable starting score, not a publication-ready verdict. Reuse the provider's available detection, notation and original exports before inventing replacement processing. Keep the original and reversible revisions. Work toward accurate, clear, playable notation: check coverage, instrument assignment, pitches, rhythm, meter, voices, clefs, ties and spacing against the recording or written source. Inspect every exported page, including page turns and dense passages. Use get_score, review_score, previews, edit_score and validate_score for evidence-based corrections within the user's request; no guessed deletions or merges. Structural checks and MIDI hashes do not prove musical accuracy. Choose style/texture hypotheses from full phrases and source evidence: opening rests, offbeat harmony, three voices, crossing hands, ornaments, swing and rubato can be genuine; no fixed rhythm ratios or left-hand eighth-note template. Separate performance, structure, notation and authorized arrangements. Keep a faithful master for learner reductions. Say what was actually listened to and what remains uncertain; report accuracy, readability and playability separately. Pro is powered by Mirelo: its original PDFs (original_pdf is the full score unless one part or tab is selected, with tuning source; original_scores the ZIP) engrave the unedited result only, exclude later edits (then call them the original) and are not a claim of final quality.

Current tools lack precise local voice/staff/hand reassignment, arbitrary onset/offset edits, local tempo-map edits and dedicated tuplet/swing/grace/arpeggio/tie/slur/pedal entry. set_duration changes playback note-offs; rebeam only changes grouping; global voice/grid options cannot replace local editing. Read live schemas and operation restrictions. Report unsupported corrections without inventing actions or destructive workarounds. ABC reconstruction needs source comparison and representation checks. Inspect all exported pages and audition changed passages when possible; structural validation, MIDI preservation and cleaner pages do not prove musical accuracy.

Read get_score for current revision/IDs. Apply requested reversible changes with edit_score within the stated goal without repeated permission. Panel numbered requests have separate note_ids: apply them in order on the current revision. Preview new musical proposals with preview_score_edit, review_score that preview, and apply_score_preview only after acceptance of that specific preview. Re-read stale revisions. Structural validation does not prove transcription accuracy; doubtful_notes are leads to listen to, not a verdict. MIDI/audio exports require complete performance bindings; MusicXML/PDF may still export. Recheck the accepted revision and return export_score's expiring download link. A plain PDF request uses format=pdf and follows the saved view, like Download; do not silently substitute Mirelo's original PDF. Use original_pdf only when requested and label it as the original. Audio exports are synthesis, not original stems.

Show a score as staff or jianpu (简谱: jianpu 1=key, jianpu_fixed 1=C 固定调, jianpu_melody) with set_notation_view: the score keeps it, the open panel and Download PDF follow; with no panel, open_score with notation; before it exists, pass view to the tool making it. export_score takes the same names; jianpu_voices only if asked for a hand's voices apart.

Call send_feedback once only after the user explicitly expresses an opinion of a result, with their own words as a non-empty comment and the revision they judged. Never supply your own rating or solicit one. Feedback grants no consent to share the recording; the user's panel buttons handle sharing.
<!-- END MCP ESSENTIALS -->
