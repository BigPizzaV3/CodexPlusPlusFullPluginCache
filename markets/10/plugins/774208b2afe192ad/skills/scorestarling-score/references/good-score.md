# Review a score using musical evidence

Provider output is initialization. The goal is human-reviewed, accurate, clear, playable
notation. Musical conventions help choose testable explanations; they do not establish
what a particular recording contains. The user's source, requested edition and feedback
come first. These examples are not confirmed analyses of Sand or any other user song.

Separate performance events (attacks, releases, pedal and microtiming), musical structure
(beat, phrase, harmony and voices), notation, and an authorized learner arrangement.
For each correction record the bars/IDs, the phenomenon, supporting and conflicting
evidence, the change, its playback effect, how to undo it and what was actually checked.
Compare full phrases and repeated sections. Preserve uncertain alternatives.

`review_score` measures score properties and renders a page; it checks no pitch against the audio
(its `expression` measures only each bar's timing and loudness).
`doubtful_notes` only supplies Basic Pitch confidence leads. Unavailable confidence for
Piano, Mirelo or notation imports, and zero flagged notes, cannot establish accuracy.
Structural validation, a MIDI hash, fewer notes or a cleaner page cannot establish it either.

## Choose an explanation for the passage

Each entry follows: applicable evidence; counterexample; supported action; verification.
Read the live operation schema and `get_workflow_guide(topic="operations")` for exact limits.
Apply reversible corrections the user already requested. Preview new musical proposals
outside that scope and apply after acceptance of that preview; do not request permission
again for each ordinary edit within an authorized correction or arrangement.

1. **Pop piano melody and accompaniment.** Use a recurring melody and harmony pattern
   heard across a phrase. Eighth-note left-hand accompaniment with right-hand melody is
   one example, not a default: block chords, syncopation, left-hand melody and changes of
   texture are counterexamples. Inspect sections with `review_score`; consider supported
   voices/staff layout, clef and beam changes. Replacing an accompaniment pattern is an
   arrangement. Verify the actual rhythm, melody and fills, including section changes.
   [Accompanimental textures](https://musictheory.pugetsound.edu/mt21c/AccompanimentalTexture.html).

2. **Independent voices.** Look for separate melodic continuations, entries and releases.
   Simultaneous chord tones alone do not establish independent voices; voice crossing does
   not exchange their identities. Two voices per staff is not a musical maximum. Treat
   `reengrave voices` as a candidate, not permission to lose an inner line. Check each
   line's continuity, rests and sustain. Precise local reassignment is currently unavailable.
   [Counterpoint](https://musictheory.pugetsound.edu/mt21c/SpeciesCounterpoint.html).

3. **Hands, voices and staves.** In overlapping registers or cross-staff figures, assess
   continuity, reach and time available between attacks. Middle C is not a hand boundary;
   treble staff does not mean right hand. In melody and accompaniment, assign by role, not
   pitch: the melody is usually the right hand's, and broken accompaniment chords that climb
   above middle C (to E♭4, say) stay in the left hand. When each hand plays one note per
   eighth, a note at an eighth that one hand's agreed note already fills belongs to the other
   hand, whatever a pitch split says. Audio may not uniquely identify hand allocation.
   Preview supported staff layout or clefs, without repitching to imitate a staff move;
   local hand/cross-staff editing is unavailable. Verify sounding pitches and a playable
   allocation, identifying uncertain hand choices as proposed fingering.
   [Keyboard notation](https://lilypond.org/doc/v2.24/Documentation/notation/common-notation-for-keyboards).

4. **Broken chords and repeated patterns.** Hear multiple cycles before assuming a pattern.
   An ascending arpeggio is not necessarily Alberti bass; a cadence can genuinely vary a
   repeated figure. `rebeam` may clarify grouping; use `fill_rest`, `add_chord_tone` or
   `set_pitch` only at source-supported locations within the requested correction. Check
   attack order, real variants and harmonic changes; never fill notes from a generic template.
   Once the user or the recording confirms a single-note broken-chord texture (one note per
   hand per eighth, no dyads), a note only one transcription hears beside the figure is
   usually an echo or an octave/harmonic ghost; a clear-looking spectral attack does not
   confirm it. Prefer notes the transcriptions agree on, then the bar's own pattern. A gap in
   a steady eighth figure is usually a missed attack, not a rest: fill it from the same bar,
   preferring the same half bar since harmony often changes mid-bar. A bar holding only its
   bass is one held note, not a bass plus stray eighths.
   [Arpeggiated accompaniments](https://musictheory.pugetsound.edu/mt21c/ArpeggiatedAccompaniments.html).

5. **Swing and syncopation.** Compare long/short timing over several beats and check straight
   sections and real tuplets. Jazz does not always swing; swing is not a fixed triplet ratio.
   Preserve offbeat attacks. `rebeam` changes grouping only; a global grid cannot express
   every swing or tuplet passage. Dedicated swing/tuplet entry is unavailable. Verify both
   readable beat grouping and retained performance timing, rather than pushing attacks
   onto strong beats. [Swing rhythms](https://viva.pressbooks.pub/openmusictheory/chapter/swing-rhythms/).

6. **Rubato and rolled chords.** Follow phrase-level slowing/recovery and sequential attacks;
   distinguish a flexible pulse from a free passage. Rubato does not imply a new meter. A
   section's first note is often held long and phrase ends are held freely: keep the
   parallel phrase's bars and let the tempo map take the extra time, rather than inserting
   or dropping beats. An even grid spreads a slowed repeat ending's few attacks across the
   bar: when they sit further apart than the grid's notes, copy the parallel bar's rhythm.
   Rolled chords need not become tiny notes and rests or simultaneous attacks. Inspect a
   supported quantization preview against the original. Local tempo-map, free rhythm and
   arpeggio entry are unavailable; a held phrase end can carry a printed fermata (`add_mark`),
   which does not change playback. Verify phrase timing and attack order;
   changing the whole BPM is not a substitute for local timing corrections.
   [Played and notated durations](https://www.steinberg.help/r/dorico-se/6.2/en/dorico/topics/key_editor/key_editor_notes_duration_played_notated_c.html).

7. **Short notes and apparent false detections.** Check an audible attack, pitch, repeated
   passages and original/synthesized A/B. A short or quiet note can be a real ornament or
   musical ghost note, rather than a model error. Confidence only prioritizes inspection.
   Use specific IDs for evidence-based deletion/repitching; preserve uncertain notes or
   propose alternatives. Verify that real ornaments survive; lower note density is not
   evidence of correctness. Provider-specific confidence must not be borrowed from another
   model. [Basic Pitch outputs](https://github.com/spotify/basic-pitch).

8. **Pedal, key release and sound decay.** Check pedal events, repeated attacks and harmony
   changes. Acoustic decay, key release and notated duration are different quantities;
   overlap alone does not prove a held voice or an unwanted note. `set_duration` changes
   playback note-offs; do not present it as notation-only cleanup. Independent pedal and
   notation-duration editing are unavailable. Verify repeated attacks and sustained voices
   in both playback and the page. [Piano transcription model](https://arxiv.org/abs/2010.01815).

9. **Beat level, meter and pickup.** Compare accents, bass/harmony and phrase boundaries
   across phrases. Syncopation, anticipation and hemiola can contradict a beat-one guess;
   an opening rest can be real, and an underfull first bar is not automatically a pickup.
   No universal tie-per-note or sixteenth-note ratio determines correctness. Use supported
   `scale_note_values` for an evidenced global half/double issue, `set_meter` for grouping
   and `rebar_pickup` for a confirmed length. Re-read IDs and verify timing, first downbeat
   and later bars. [Rhythmic notation](https://musictheory.pugetsound.edu/mt21c/CommonRhythmicNotationErrors.html).

10. **Repeated phrases as references.** A returning phrase (a repeated verse, the tune an
    octave higher) usually keeps its rhythm. Line the occurrences up and count the
    accompaniment's steady pulse between melody notes: when one sits half a beat or a beat
    off and its bars run unusually short or long, the beat grid drifted, not the player;
    write it like the others. Keep differences the pulse confirms or that change pitch
    (fills, pickups, a slowed final cadence), and ask the user where the pulse stops.
    Aligning can also put every occurrence on the wrong beat (three written two beats late in
    a section that starts on beat 1): count the accompaniment's own pulse from its first
    attack to place the section's first note, and match the parallel section the user
    confirmed. `rebar_pickup` moves every bar line; shifting one passage needs a checked ABC
    reconstruction. Verify each occurrence's first downbeat and bar lengths by ear.

11. **Key, modulation and jianpu.** Use cadences, bass, melodic direction and sustained tonal
    centers; fewer accidentals alone cannot determine spelling, major/minor or modulation.
    `set_key` changes notation; `transpose_score` changes pitch. Full `jianpu` retains all
    staves; `jianpu_melody` takes the top line, which may not carry the melody; `jianpu_fixed` is
    every staff in 1=C fixed do (固定调), each black key marked. In the key, a minor uses
    the relative-major do: `1=C`, tonic 6. Inspect each staff's digits, octave dots, rhythms,
    key changes and multi-voice output; do not assume lossless export.
    [Tonicization and modulation](https://musictheory.pugetsound.edu/mt21c/TonicizationVersusModulation.html).

12. **Learner arrangements.** Use the learner's actual difficulty, comfortable reach, rhythms
    and target tempo. Jianpu does not reduce playing difficulty; two beginners can require
    different changes. Keep a faithful master and create a clearly identified arrangement
    within the authorized goal, using supported note edits or checked ABC reconstruction.
    Explain removed/revoiced material and verify retained melody, important bass and
    recognizable rhythm through the learner's audition or playing feedback. A request for
    the original (原谱) means the faithful transcription with every note of both hands,
    delivered first; arrangements come after it.

13. **Final publication review.** Inspect every actual exported page and dense passage:
    vertical alignment, rhythmic spacing, beams, rests, accidentals, clefs, continuation
    ties, headings and page turns. Equal spacing is not the goal. Ledger lines may suggest
    another clef, but frequent clef changes or moving notes can worsen readability. Check
    instrument-specific range, transposition and reach instead of declaring an octave-span
    limit; bass guitar/double bass octave notation is not a rule for every bass instrument.
    Use supported clef, beam and metadata edits; do not change music to hide a layout defect.
    Report unresolved engraving limits. [MOLA preparation guidelines](https://mola-inc.s3.eu-west-1.amazonaws.com/files/mola3/MOLA-Guidelines-for-Music-Preparation.pdf)
    support performer-oriented preparation and independent proofreading; their orchestral
    part conventions are not universal mobile or jianpu layout requirements.

14. **Expression marks from the recording.** When the user asks for tempo or dynamics marks,
    read `review_score`'s `expression`. Timing: a phrase end running about a quarter slower
    (stretch ≈1.25) is rit., nearer 1.15 poco rit., with a tempo where the next section
    resumes; 1.5 or more is a fermata candidate on that bar's held note. A phrase end's held
    bar often measures short because the player moves on early: read the last two bars
    together. Leave beat-level rubato inside phrases unmarked; a section's long first note is
    not a fermata. When `timing` says the bars follow one fixed tempo, bars cannot show
    slowing: compare repeated phrases' written rhythms instead. Dynamics: compare sections'
    `level_db`; about 3 dB between sections is one step (mp to mf), and a steady fall or rise
    over several bars that are not held is a hairpin. Held bars read decay, and levels depend
    on the mix: propose dynamics with `preview_score_edit` and let the user's ear decide.
    Apply clear timing evidence when the user asked for marks, with `add_mark`.

## Tool effects and remaining limits

The suggestion code `single_line` currently supplies `reengrave voices: 1`; inspect the
actual operation. `reengrave line: "single"` instead removes simultaneous/overlapping notes
and can shorten held notes in playback. It is a reduction, not a notation view. Do not add
it automatically without explicit one-note-at-a-time intent. Omitted reengrave options
reuse saved choices: inspect those before claiming unchanged playback. `program` changes
also affect sound. Reengraving resets clefs/beams/spellings and may replace IDs.

Printed marks are separate objects with IDs in `get_score` `marks`: words (rit., a tempo), rehearsal
letters (A, A6), metronome marks, dynamics, hairpins and fermatas. Add, change, move or delete one with
`add_mark`, `update_mark`, `move_mark` or `delete_mark` instead of rewriting the score; two marks at one
note stay two objects, printed stacked. Only dynamics change playback.

Current tools do not supply precise local voice/staff/hand reassignment, arbitrary local
onset/offset editing, local tempo-map edits or dedicated tuplet/swing/grace/arpeggio/tie/slur/
pedal entry. A global voice cap or grid cannot replace these abilities. Supported duration
edits have chord/binding/rhythm restrictions. Report gaps without inventing action names
or destructive workarounds. Rewriting ABC is a new reconstruction to verify, not proof that
all source details survived.

Finish by separating accuracy, readability, playability and learner suitability. Name the
revision exported, the passages actually heard/compared and any uncertainty; no fabricated
publication score. A passing structure check or preserved MIDI only proves its stated scope.
