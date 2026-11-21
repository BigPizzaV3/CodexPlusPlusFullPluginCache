---
name: scorestarling-score
description: Turn audio into an editable score with ScoreStarling, review and refine the transcription and its engraving, preview musical changes, and export notation or MIDI. Use when someone wants sheet music, a score or MIDI from a recording, a voice memo or a song they play or sing, with a connected ScoreStarling MCP server.
---

# Audio to a reviewed score

Use the connected ScoreStarling tools. This skill supplies the workflow; it does not
grant account access or consent to upload, spend credits, or apply a new musical proposal.
Sheet music (a photo, scan or PDF of printed music, jianpu), score files (MusicXML, MIDI, ABC)
and music written in the chat follow the `scorestarling-notation` skill.

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

## First reply

If the user has not given a recording yet, answer in three short lines with the ways in:
attach it in the chat (ChatGPT web or desktop) or paste a link to the file; open the ScoreStarling
panel with `open_studio` to choose a file or record (best on phones and in Claude); or use the
workspace at scorestarling.com/app. Add that one instrument or voice works best, piano included, and that a
known tempo (BPM) helps; otherwise it is detected. Name the choices as the workspace does: one
instrument or voice and solo piano (free), or a band (uses credits, price shown first); never say
Standard, Pro, engine or supplier names unless the user does.

## Get the audio in

- ChatGPT attachment: first call `check_recording` with the host-supplied `file` object (a few
  seconds; nothing is saved or charged), passing `instrument` when the user has said what it is.
  Then call `transcribe_attachment` with the same `file` and the recommended engine. When the
  recommendation's engine is null (chords, instrument unknown), ask what the instrument is.
  Follow the job in the same turn with `get_upload_status` and `wait_seconds: 20`, calling
  again until it finishes; the panel shows the same progress. Every result's `next_step`
  says what comes next. Never fabricate a URL/file ID or ask for a second upload when that
  object is available.
- Claude/code attachment with a readable file: obtain the filename and exact byte count,
  call `prepare_audio_upload`, POST the actual raw bytes once with
  `Content-Type: application/octet-stream`, then follow its `job_id` with `get_upload_status`
  and `wait_seconds: 20`.
  Do not encode audio into tool arguments or reveal the upload capability URL.
- The user asks for a link to send the file themselves: call `prepare_audio_upload` without `size`
  (never ask for the byte count or length) and give them the link with
  `curl -X POST -H 'Content-Type: application/octet-stream' --data-binary @FILE LINK`. It works once,
  for ten minutes. Then follow its `job_id` as above.
- No readable file, code execution or network access: explain the missing capability and
  offer `open_studio` so the user can select their file in the panel. Pass `engine` when the
  instrument is known (`piano` for solo piano) so the panel preselects it. You are not told
  when a panel job finishes: the panel offers the user a button that asks you to check the
  new score, and `list_scores` finds the newest one.
- A link to a video or song page (YouTube, Bilibili, TikTok, SoundCloud, Instagram, X and
  similar sites; short share links work) or to the file itself (an MP3 or a video file; Dropbox
  and Google Drive share links work): call `transcribe_link` with the link and the engine for the
  instrument, asking what it is when you don't know. Only the audio of the first 5.5 minutes of a
  video is fetched; files are public https addresses up to 50 MiB (120 MiB as WAV, AIFF or FLAC).
  Spotify and Apple Music encrypt their music, and some sites (Douyin, Xiaohongshu) may refuse the
  server: then ask for another link or the file. Follow the job with `get_upload_status` as above.
- Local stdio server: use `list_audio` / `transcribe_audio` only for files already in its
  `data/input`. A sandbox path is not a path on the remote server.

Engines (`provider`): `local` is Standard, for one instrument or voice; `piano` reads solo piano
with both hands, chords and the sustain pedal (about a minute); `mirelo` is Pro, for bands and
drums, an external paid provider chosen with the user; its credit quote, where credits apply, is the
one cost question (never ask for a credit cap). Uploads are limited to 50 MiB, or 120 MiB as WAV, AIFF or FLAC (`get_account_usage.upload_limits`).
A score covers the first five minutes of a recording with Standard or Piano. Pro covers
five minutes for invited accounts and accounts holding purchased credits, otherwise two;
`check_recording`, `get_account_usage` (`max_seconds`) and upload results (`max_seconds`, `excerpt`) give
the account's current limit. Tell the user about a longer recording's excerpt before the task starts. If
Pro is unavailable,
read `get_account_usage.engine_status.mirelo.reason` when provided; do not assume the account lacks
permission or the supplier has a two-minute ceiling. A recording steadily off concert pitch is retuned to A440 automatically.
Pass `bpm` only when the user gave the tempo; when omitted, it is estimated: say so. `bpm` counts
quarter notes: for a 6/8 or 12/8 song counted in dotted quarters, pass 1.5 times that tempo. For Pro,
`bpm` writes one fixed tempo; user-stated or source-established rhythm choices go in `pro_options`
when confirming. Explicitly pass known 6/8, 9/8 or 12/8: omitting meter uses N/4, not compound
meter detection. Never guess unknown meter/tempo or force fixed BPM; report uncertainty.
Review all instrument suggestions against accessible musical evidence. Use a grounded complete list;
otherwise use `instruments: null` for automatic parts, included in the one quote/start consent.
Do not require the user to inventory instruments. Saved replay choices always take precedence. Mention cost
only for Pro or when `get_account_usage` shows a limit; supplier credits and product credits are
separate, and estimates are not billing receipts. Standard and Piano are free; only Pro uses product
credits, shown in its quote. Never show prices, plans, packs, upgrade prompts or purchase links in chat;
if asked how credits work, link https://scorestarling.com/credits. Each job counts toward the account's
two-running limit.

An HTTP 202 means upload accepted, not transcription completed. Follow the original job;
keep following in this turn, giving brief plain progress instead of a task ID or asking
the user to tell you to keep waiting. A failed free `check_recording` used no transcription
credits; say so. For later failures, use the tool's actual used/refunded/held credit evidence;
do not infer a zero charge from a failed status or retry an uncertain paid submission.
on `completed`, continue with the default below. On `failed` or `needs_review`, report the
state and inspect usage/saved results. When `can_recover` is true, use `recover_pro_result`
with that original `job_id`, then follow it again; this resumes the accepted Pro task or
its saved result without a new transcription or reservation. Unknown submissions need
manual review. After an ambiguous response, inspect that same job instead of creating
another upload or paid job. Pro's provisional note count can shrink; 96% is still processing.
Review/export only after completion. Do not blindly retry mutations.

### Local upload helper

Use the connected host's authorized `prepare_audio_upload` tool, with the real filename,
byte count and chosen provider. Its one-use upload ticket is the only capability
the file-transfer script needs; do not read environment credentials or extract tokens
from another application. Add `size` to the ticket JSON with the exact count passed to
the tool. Pass that JSON privately on stdin, keeping the URL out of command arguments:

```sh
python scripts/upload_audio.py /path/to/audio.wav < /path/to/private-upload-ticket.json
```

The script path is relative to this skill directory. It needs Python 3.11 and `httpx`,
installs nothing and uses no repository imports. `--site` selects a trusted deployment
(default `https://scorestarling.com`) or HTTP loopback origin; the ticket's upload link
must be on it. The CLI sends raw bytes once and prints only the job ID and
upload-acceptance flag. Then follow that job with the connected `get_upload_status` tool
(`wait_seconds: 20`) and continue as its `next_step` says. A timeout or false acceptance flag means inspect the
existing job, not repeat the POST. Keep the ticket temporary and private; remove the
temporary ticket file after this invocation.

For a runtime that provides an already-authorized tool-call function, the script's
`upload_audio` function also performs preparation and bounded polling through that
function, with no credential discovery. If code, dependencies or network are unavailable,
use the panel. Claude API skill containers cannot make this network upload; an
application-side authorized tool or the panel must handle it.

## Default after every transcription

Do this every time a job completes, before asking what the user wants next. Review and
score edits use no provider credits. The provider output, including Mirelo's official
notation and detection, is initialization; work toward a faithful, clear, playable score
with the user. Preserve the original and reversible revisions.

1. Show the score once: the panel that started an attachment or panel upload turns into the
   score by itself; otherwise call `open_score`. Later edits update that panel in place.
   The tool prepares the score for display. If the host reports that its panel failed to open,
   say so plainly; tool success alone does not prove that the user can see the panel.
2. Call `review_score` once (no `measures`). Read its summary, suggestions and page picture.
3. Inspect each ready operation, rather than treating its suggestion code as approval.
   Apply only source-supported, performance-preserving key, clef, voice or empty-staff
   cleanup within the user's request. A key estimate or voice-count heuristic alone is
   insufficient: retain genuine inner voices, crosses and the user's stated key.
   The current `single_line` suggestion supplies `voices: 1`, not `line: "single"`;
   inspect its actual operation. `line: "single"` deletes notes and can shorten held
   notes in playback. Never add it automatically or infer permission to discard
   polyphony from an instrument name. If a requested melody reduction warrants it,
   explain the affected notes; otherwise preview it as a new proposal.
   Merge supported `reengrave` options into one call, then apply clefs; inspect saved
   layout choices as well, since omitted options reuse them. Re-read changed note IDs,
   validate and compare the revision before continuing; `undo` restores the prior version.
4. Report in a few plain lines: the engine, instrument, key, time signature, the tempo and
   whether it was detected (an estimate) or supplied, any retuning or excerpt named in the
   status summary, the cleanup, confidence availability, flagged bars and rhythm leads. If
   the tempo was detected, compare it with the recording and any written source yourself. When the notes read at
   half or double the felt speed, offer `scale_note_values` (free, keeps the playing);
   a different explicit quarter-note tempo and meter uses `rewrite_rhythm` when the review says it is available.
   do not start another transcription merely to change notation. For Pro,
   report the time signature and tempo from `provider_output.rhythm` with its warnings.
   Use the user's language and explain effects plainly. Keep tool names, field names,
   revision numbers and editing bindings out of the reply. For example, say "Some notes
   cannot be edited individually yet" when that is the limitation; say what was checked
   and what still needs listening, rather than dumping diagnostic counts.
   The Piano engine also takes the time
   signature (4/4, 3/4, 6/8 or 12/8), a pickup and the bar lines from the playing. Compare
   `source_rhythm_analysis` candidates with complete phrases, opening rests and the source;
   their ranking is not calibrated and the correct meter may be missing. Correct a clear
   source-supported reading within the request. Ask one precise question only if a consequential
   tempo, meter or downbeat choice remains unclear. A 6/8 or 12/8 score marks and
   reports its tempo in dotted quarters.
5. If the status gives `advice`, or the user hears missing notes, offer another engine: Piano
   for solo piano (free), a band for songs with several instruments (uses credits, price shown first).
6. Apply evidence-based, reversible edits the user has already requested, including a
   broad correction or arrangement goal; do not ask again for each ordinary edit.
   Preview newly proposed musical changes outside that scope and apply after acceptance
   of that preview. A request to review is not permission to delete plausible voices.
   A new transcription and paid Pro use still need their own authorization: one exact
   credit quote, or one question about starting when the account has no quote. Never ask for a cap.

## Listen and check

Open the score panel, read `get_score`, compare original audio and MIDI playback with the
user, and call `validate_score`. A clean structural result does not prove transcription
accuracy. Compare complete phrases and repeated sections, not isolated note density.
Separate performance events, musical structure, notation and an authorized learner
arrangement. Record the target bars/IDs, supporting and conflicting evidence, proposed
change, playback effect and verification; preserve plausible alternatives when uncertain.
If the host cannot play audio, say so and ask the user to audition the panel.

- Octave/pitch: use real selected note IDs and `transpose` / `set_pitch`; distinguish
  written pitch from sounding pitch for transposing instruments.
- Meter/pickup: inspect the current settings; preview `set_meter` or `rebar_pickup` with
  a confirmed pickup length in quarter-note beats. `set_pickup` only marks an already
  partial first bar. Never infer pickup length from an underfull bar alone. A Piano score's
  pickup was estimated from the playing; change it with clear source evidence, asking only
  when the downbeat remains unclear. Notes that look halved or doubled may mean the beat level is off: a slow ballad
  whose sixteenths came out as eighths under a doubled tempo mark needs `factor` 0.5 (halve
  every value), a quick waltz written in sixteenths at half its tempo needs 2 (double).
  Preview `scale_note_values` with that factor. The
  tempo mark changes with the values, the playing stays, and a Piano score finds its time
  signature and bar lines again; then check the meter and first downbeat against the source.
  A 6/8 song written as 3/4 (same bar length) only needs `set_meter`.
- A different pulse: `rewrite_rhythm` changes a steady recording's note values and bars together
  at an explicit quarter-note `bpm`, `beats` and `beat_type`, without inference or credits.
  It preserves played notes, controls, pitch bends and comparison playback, with MIDI rounding
  below 0.1 ms. Check its availability and source evidence; tracked/changing tempo, pickups,
  imported sheet music and marks or tuplets it cannot preserve are refused. Do not apply an
  uncalibrated candidate merely because it ranks first. Preview new interpretations; re-read IDs.
- Quantized rhythm: compare onsets/durations and the supplied BPM. `set_duration` corrects
  supported note lengths; `rebeam` changes grouping only; `reengrave` with `grid: "8th"`
  writes the whole performance on a coarser grid. Explain an unsupported timing repair
  instead of inventing an operation or starting another credit-consuming transcription
  without authorization.
- Unbound notes: inspect validation and mapping before performance edits. Do not guess
  MIDI bindings or align audio precisely from `notation_estimate` times. MusicXML/PDF may
  still export; MIDI/audio require complete bindings. Report any unresolved limitation.

## Review and refine

After the first listen, call `review_score`; add `measures: "5-8"`, in the score's bar
numbers, to zoom in. `review_score` is not a full automatic comparison with the recording.
Its `source_note_evidence` supplies at most six cached, independent pitch/voicing leads for
detected single lines, linked to unchanged current note IDs and source listening spans.
Inspect those original passages yourself before correcting anything. Quiet, short or ornamental
real notes can be flagged too; empty or unavailable evidence says nothing about accuracy.
Its `doubtful_notes` are Basic Pitch confidence leads only; unavailable for Piano,
Mirelo or imports, or an empty list, does not mean the score is accurate. It also returns
`suggestions` with ready operations for key, clef, voices, staff layout and register, the
`validate_score` findings, and a picture of the page. Judge the picture as an engraver
would, with your own knowledge and [references/good-score.md](references/good-score.md).
Everything it reports is a lead to check, not a verdict. Before an arrangement, a simplification,
a level, another texture or a playable version (弹唱, two-hand jianpu), read [references/arranging.md](references/arranging.md).

- Low-confidence or short notes may be real ornaments, quiet attacks or musical ghost
  notes. Compare the original and synthesized passage before deleting or repitching;
  neither a cleaner page nor fewer notes proves accuracy. Preserve uncertain notes.
- `reengrave` without `line` or `program` changes preserves the performance and replaces
  the notation: earlier clef, beam and spelling edits are redone and some note IDs change, so re-read the score afterwards.
  `review_score` says whether it is available (not with chord symbols, for example, nor
  after a pickup unless the Piano engine found it). Settle the instrument and layout (`program`, `staff_split`, `voices`,
  authorized melody reduction), then key (`key`, at sounding pitch) and rhythm (`grid`), before fixing single notes.
- `summary.rhythm` says where bar 1 starts and how the rhythm reads. A `rhythm` suggestion
  means the bar lines may not follow the playing: tell the user what it found, ask where they
  feel the first downbeat, and for solo piano from the Standard engine offer the Piano engine,
  which places bar lines from the playing. Treat rhythm ratios as candidate evidence:
  opening rests, offbeat bass/chord changes, syncopation and dense sixteenths can be real.
  Move bar lines only within an authorized correction and with a supported pickup length.
- Beyond the default cleanup, preview each change you propose, call `review_score` on the
  preview revision, and explain what improved and what got worse. Apply only what the user
  accepts.

Inspect every final exported page, not only the first review image: alignment, collisions,
clefs, continuation ties, accidentals, part labels and page turns. Audition the changed
passages against the source and recheck the exported revision. Report accuracy,
readability, playability and learner suitability separately; do not invent a publication
quality score. Stop when the remaining questions need the user's ear or taste.

Current tools do not provide precise local voice/staff/hand reassignment, arbitrary
onset/offset editing, local tempo-map editing, or dedicated tuplet, swing, grace-note,
arpeggio, tie/slur and pedal entry. `set_duration` changes playback note-offs;
`rebeam` changes grouping; a global grid cannot repair all timing or ornaments.
Read `get_workflow_guide(topic="operations")` and the live tool schema for supported
fields and restrictions. Report a missing capability rather than inventing an action,
repitching/deleting to imitate a staff move, or flattening genuine tuplets.

## Preview, accept, export

When the user asks for a change, broad or exact, apply it with `edit_score`; it takes effect
at once and `undo` reverts it. A message from the panel can list several numbered requests,
each with its own note IDs: apply them in order, each to the current revision. For a change you propose on your own initiative, call
`preview_score_edit` with the current revision and explain the scope; the open score panel
shows it with Apply and Discard. A preview is not applied. Only call `apply_score_preview`
after the user accepts that specific preview, using its ID and base revision. The panel
follows edits and previews by itself, so call `open_score` only when no panel is open.

Printed marks are their own objects, as in Sibelius: tempo and expression words (rit., a tempo),
rehearsal marks (A, A6), metronome marks, dynamics, hairpins and fermatas, each with an ID in
`get_score` `marks`. Use `add_mark`, `update_mark`, `move_mark` and `delete_mark` when the user asks
for a mark, or when one text is doing two jobs. Example: a section "A6" where the music returns to
tempo is two marks on the same note, printed stacked, never one text "A6 · a tempo":
`{"action":"add_mark","kind":"rehearsal","note_id":"n…","text":"A6"}` and
`{"action":"add_mark","kind":"words","note_id":"n…","text":"a tempo"}`. ABC's `"^A6"` arrives as words;
`update_mark` with `kind: "rehearsal"` makes it the boxed section label. Only dynamics change playback
(as `set_dynamic`); a metronome mark is printed only, so say that playback keeps the recording's tempo.
Jianpu exports carry the same marks. Fields and limits: `get_workflow_guide(topic="operations")`.

To read the score in numbered notation (jianpu, 简谱: "我要简谱", "show it as numbers"), call
`set_notation_view` with `view=jianpu`; the open panel switches within a few seconds, and
`view=staff` switches back. With no panel open, call `open_score` with `notation=jianpu`. The
view is drawn read-only from the last saved revision: edits still happen in staff notation and
the numbered view follows them. The score keeps the choice, in the workspace too. When the user
asks for numbered notation before the score exists, pass `view=jianpu` to the tool that makes it
(`transcribe_attachment`, `transcribe_link`, `prepare_audio_upload`/`begin_audio_upload`,
`create_score`). For a file to print or keep, use `export_score` as below.

When the user explicitly requests one-note-at-a-time reduction, `reengrave` with
`line: "single"` is available. Merely naming a voice, violin or flute does not authorize
removing real simultaneous notes. Apply an already requested reduction with `edit_score`;
preview an Agent-proposed reduction with `preview_score_edit`: it keeps one note at a
time on one staff and removes the extra notes from playback too (undo brings them back), without
transcribing again. A part still named after the piano becomes Melody. The user can do the same in
Score settings › Layout, which also offers one staff with chords, two piano staves and the shortest
note. A single-part recording only.

When a recording was transcribed as the wrong instrument ("it's a piano"), call `transcribe_again`
with the score ID and the right `provider`: a new score is made from the same recording and the
first one stays, so nothing needs uploading again. Follow its job like an upload. Sheet music and
notation have no recording to transcribe again.

On a stale revision, re-read `get_score` and reconsider the proposal against the new score;
do not silently repeat it. Reopen and validate the accepted revision. Use `export_score`
for `musicxml`, `pdf` or `midi`; use `part_id` for one part, or `format=parts` for a ZIP.
A plain PDF request uses `format=pdf`: it follows the score's saved display view,
like the panel's PDF button. Do not silently give Mirelo's different original layout.
Use `original_pdf` only when that original is requested, and name its source.
For numbered notation (jianpu, 简谱) use `jianpu` (every staff) or `jianpu_melody` (the top
line only, usually the tune), both movable do in the key (`1=` key; minor keys from their relative
major's do), or `jianpu_fixed` for 1=C fixed do (固定调): the same pitches with 1 always C and
every black key marked (in ♭G major, b5 and b7), for players who read keys rather than degrees. `abc`
returns ABC text you can read or rewrite as well as a file; `mei` is for music research.
Return the provided expiring download link. Native Sibelius/Dorico files and isolated
original stems are not produced. Score edits do not call Mirelo or spend provider credits.

Finish briefly with what completed, the useful corrections and the delivered score,
and any listening or quality check still needed. Do not describe local/mocked checks as
real ChatGPT/Claude acceptance or provider billing verification.

<!-- BEGIN MCP ESSENTIALS: scripts/sync_workflow_guidance.py -->
## Shared MCP essentials

Use the connected host's authorized tools and respect its file, network and approval boundaries. Guidance grants no account access, upload consent, supplier spending or acceptance of a proposal. Never invent file references, expose upload capabilities or discover credentials.

When the user says reuse the existing result or do not start new processing, first list_scores and open_score; do not upload, check_recording or transcribe_again merely to reopen a score. Only for an explicitly requested new score from a saved Pro result, use the original upload or transcribe_again with provider=mirelo, review_instruments=true and replay_only=true from creation (enabled replay accounts only). Read get_pro_instrument_review(start=false) first. replay_candidates verify this owner, original bytes and decoded length; compare every historical instrument and flat pro_options with the requested choices. No matching candidate means stop and offer the existing score; never start detection, fresh processing or a replacement. Confirm matching complete choices with replay_only=true, then read back pro_review.replay_only=true. Keep the same excerpt length; a shorter quote needs its own matching saved result, otherwise stop. If a quote is required, ask once for its exact product credits; reuse permission is not payment consent. Follow the same job and verify completed.replayed_from. Explain saved-result reuse in plain words; the user does not need to name internal fields.

Audio attachments: check_recording with the named instrument; use recommendation.engine. If it is null, ask what the instrument is. local is Standard for one instrument or voice; piano is Piano for solo piano with both hands, chords and pedal; mirelo is paid Pro for bands and drums, chosen with the user; its credit quote is the one cost question. Never ask for a credit cap or show supplier credits. Pro uploads need instrument review; follow next_step. To the user, name the choices as the workspace does: one instrument or voice, solo piano, or a band (uses credits); say price, not quote; never say Standard, Piano engine, Pro, model or supplier names unless the user does. When you ask the user to agree to a band's price, add the short credit "Powered by Mirelo" (its API terms ask for it where a generation starts); nowhere else.

Read get_pro_instrument_review(start=false) first. For a new Pro upload, start=true gets free instrument suggestions. Review every suggestion against accessible recording evidence, supplied facts and any written source; preselected is not a complete inventory. Describe clearly and possibly heard instruments in plain words, never agreement figures. Use a grounded complete list with confirm_pro_instruments; a missing instrument cannot appear and a wrong one misallocates notes. Otherwise use instruments=null for automatic parts and include that plan in the one quote/start question, not a separate approval. Set user-stated or source-established rhythm choices in pro_options before quoting; explicitly pass known 6/8, 9/8 or 12/8. Omitted meter uses N/4, not automatic compound-meter detection. Never guess unknown meter/tempo or force fixed BPM; omit unknown choices and report uncertainty, asking only about consequential ambiguity the source cannot resolve. Until the quote is accepted the user may still change choices; quote again if changed. Do not poll or retranscribe a pending review; cancel_pro_review releases its reservation. For replay_only, even start=true stays cache-only: match all saved instruments/options exactly, stop on no match, and never change the cached request or start a replacement. Afterwards report provider_output.rhythm with its meter/tempo sources and warnings.

When get_upload_status reports product_quote.phase=pending, call get_transcription_quote for its actual decoded duration, product credits and complete parameters; for Pro these include the instruments and rhythm pro_options fixed by confirm_pro_instruments, so pass pro_options there. Show that exact quote and obtain explicit user consent before confirm_transcription_quote with unchanged quote_id/credits and consent=true. Expired or changed input/parameters require a fresh quote. When the balance does not cover it, affordable is the longest excerpt from the start it does: offer that (two minutes on welcome credits, say) rather than stopping, and on agreement call get_transcription_quote again with seconds and show that quote. Upload estimates are not product-quote consent. Nothing is transcribed or reserved before acceptance; cancel_transcription_quote cancels only an unconfirmed task. Only Pro is quoted (40 product credits a minute); Standard, Piano, notation and explicitly exempt accounts have no quote. In chat never show prices, plans, packs, upgrade prompts or purchase links; for how credits work, link the credits_info page (scorestarling.com/credits).

Pass bpm only when the user supplied it; omission detects an estimate to confirm by listening. bpm counts quarter notes: multiply a dotted-quarter tempo for 6/8 or 12/8 by 1.5. Read source_rhythm_analysis candidates when available; scores and gaps are uncalibrated, and the correct meter may be absent. Compare full phrases, the recording and any written source before choosing tempo, meter, pickup or bar lines. When a transcription reads at half/double the felt speed, offer scale_note_values with factor 0.5/2 (free, preserves playing). For another explicit quarter-note tempo and meter, rewrite_rhythm re-writes a steady recording without new inference or charges; inspect its availability first. Apply clear source-supported corrections within the request; preview new interpretations. Ask one precise musical question only if source evidence leaves a consequential choice unresolved.

Poll get_upload_status(job_id, wait_seconds=20) in this turn until terminal; never reupload or finish with an ID or request to keep waiting. Give brief plain progress. HTTP 202 is acceptance, not completion. Inspect the original job after ambiguous responses; never blindly retry a mutation or paid job. On failed/needs_review follow can_recover/next_step: pending instruments and quotes need explicit approvals; recover_pro_result resumes the same accepted Pro task; otherwise stop for review. Quota estimates are not billing receipts.

recover_pro_result queues only a saved Pro result or accepted official job ID, without a new transcription or quota reservation. Poll the same job afterward. Unknown submissions stay held for manual review; never create a replacement to recover them. Provider progress and provisional note counts can change; even 96% is processing. Use only the completed score for review/export. provider_output.musicxml_optimized is true only when the provider actually reports optimization; absent/false is not optimized. Original supplier exports are initialization artifacts.

After transcription, call review_score; inspect its summary, operations and page. Apply source-supported, performance-preserving key/clef/voice/layout cleanup within the request. single_line suggests voices:1, not line:single. line:single deletes notes and shortens holds in playback: require explicit reduction intent. Inspect saved reengrave choices; merge supported options, then clefs; re-read IDs and validate. doubtful_notes gives Basic Pitch confidence only. source_note_evidence adds limited independent listening leads for single lines, with current IDs and source spans; inspect the original passage before any note correction. Neither is an accuracy verdict; unavailable/empty proves nothing. Report engine, instrument, key, meter, tempo/source, retuning/excerpt, changes, uncertain bars and rhythm leads; confirm estimated tempo/downbeat from source evidence; ask only when a consequential choice remains unclear. Apply requested corrections; preview new proposals. transcribe_again needs authorization; undo restores the prior revision. Answer briefly in the user's language. Explain effects in plain words; never relay tool/field names, revision numbers or editing bindings.

A provider result is an editable starting score, not a publication-ready verdict. Reuse the provider's available detection, notation and original exports before inventing replacement processing. Keep the original and reversible revisions. Work toward accurate, clear, playable notation: check coverage, instrument assignment, pitches, rhythm, meter, voices, clefs, ties and spacing against the recording or written source. Inspect every exported page, including page turns and dense passages. Use get_score, review_score, previews, edit_score and validate_score for evidence-based corrections within the user's request; no guessed deletions or merges. Structural checks and MIDI hashes do not prove musical accuracy. Choose style/texture hypotheses from full phrases and source evidence: opening rests, offbeat harmony, three voices, crossing hands, ornaments, swing and rubato can be genuine; no fixed rhythm ratios or left-hand eighth-note template. Separate performance, structure, notation and authorized arrangements. Keep a faithful master for learner reductions. Say what was actually listened to and what remains uncertain; report accuracy, readability and playability separately. Pro is powered by Mirelo: its original PDFs (original_pdf is the full score unless one part or tab is selected, with tuning source; original_scores the ZIP) engrave the unedited result only, exclude later edits (then call them the original) and are not a claim of final quality.

Current tools lack precise local voice/staff/hand reassignment, arbitrary onset/offset edits, local tempo-map edits and dedicated tuplet/swing/grace/arpeggio/tie/slur/pedal entry. set_duration changes playback note-offs; rebeam only changes grouping; global voice/grid options cannot replace local editing. Read live schemas and operation restrictions. Report unsupported corrections without inventing actions or destructive workarounds. ABC reconstruction needs source comparison and representation checks. Inspect all exported pages and audition changed passages when possible; structural validation, MIDI preservation and cleaner pages do not prove musical accuracy.

Read get_score for current revision/IDs. Apply requested reversible changes with edit_score within the stated goal without repeated permission. Panel numbered requests have separate note_ids: apply them in order on the current revision. Preview new musical proposals with preview_score_edit, review_score that preview, and apply_score_preview only after acceptance of that specific preview. Re-read stale revisions. Structural validation does not prove transcription accuracy; doubtful_notes are leads to listen to, not a verdict. MIDI/audio exports require complete performance bindings; MusicXML/PDF may still export. Recheck the accepted revision and return export_score's expiring download link. A plain PDF request uses format=pdf and follows the saved view, like Download; do not silently substitute Mirelo's original PDF. Use original_pdf only when requested and label it as the original. Audio exports are synthesis, not original stems.

Show a score as staff or jianpu (简谱: jianpu 1=key, jianpu_fixed 1=C 固定调, jianpu_melody) with set_notation_view: the score keeps it, the open panel and Download PDF follow; with no panel, open_score with notation; before it exists, pass view to the tool making it. export_score takes the same names; jianpu_voices only if asked for a hand's voices apart.

Call send_feedback once only after the user explicitly expresses an opinion of a result, with their own words as a non-empty comment and the revision they judged. Never supply your own rating or solicit one. Feedback grants no consent to share the recording; the user's panel buttons handle sharing.
<!-- END MCP ESSENTIALS -->
