# Song Stems, Locked Audio Timing & Video Handoff

18 cards. Splitting generative music stems, locked audio timing extraction, synchronized SRT/LRC generation, beat-grid alignment, and bridge to visual phases.

> **This is the handover, not the mix.** Which stems exist, what timing is locked, what the edit is
> given — all decided here, because they determine what gets generated and measured. Levels between
> those stems, ducking against dialogue, and the final loudness of the master are set by the owner in
> his own edit, against the actual material.

---

### Generative Stem Separation Protocol

**Also called:** AI stem split, vocal/instrumental extraction, 2-stem isolation, Suno stem separator (this card was two until September 2026; the second one's id was suno.stem_isolation_mastering)  
**What it is:** Separating the generated master song into discrete Vocal Stems (clean acapella) and Instrumental Stems (backing track) using neural source separation. Its release form is separating the finished song into at least a vocal stem and an instrumental stem for final mastering in the edit — with the engine platform's own separation where it offers one, otherwise with an external separator. Before splitting, check the plan, the split mode and the credit cost. **Suno** offers Stem Separation as a separate, paid-only platform feature, not a v6 model feature. **Auto Split** gives up to 12 stems for 50 credits. **Split from Mix** takes one instrument or the vocal plus the remainder, at 10 credits per extraction (20 in total). **Advanced Split** picks from about 100 instruments at 10 credits per stem (20 in total). Pro gets Auto Split and Split from Mix; Premier also gets Advanced Split. Suno may charge even when the chosen instrument is not in the song. Stem files download when the stems exist, and a song counts as one download whatever the formats or stems. These are derived separations, not lossless original multitracks. Deliver them labelled as derived, with the untouched source mix beside them, and inspect bleed and artefacts before mastering. The Studio multitrack export (Premier) and Suno's download formats are on `suno.v6_engine_architecture`.  
**Effect on the audience:** Enables independent mixing, EQ presence adjustment, and audio sweetening in the final video edit without phase artifacts. Enables professional studio-grade mixing, EQing, and mastering that transforms a generated track into commercial radio quality.  
**Used for and where it works best:** Mandatory post-processing step on every Suno and Lyria song before video integration. Every generated song destined for commercial release, streaming platforms, or video integration.  
**Best in:** formats: All music video and video production, All commercial music releases | genres: All  
**Avoid when:** Baking vocal and music into a single unalterable stereo file. Releasing raw un-mastered stereo files with uneven volume dynamics directly to platforms. And a cue handed to the re-recording mixer as score, which needs the four-way split of `score.four_way_score_stems` — more than a vocal/instrumental pair, the case named under Yields to.  
**Example:** `workflow: Ingest generated song WAV -> neural stem separator -> export VOCAL_STEM.wav and INST_STEM.wav, both unmastered with headroom intact; their balance is set in the edit.` — or, as an export spec: `export_spec: Separate stems -> vocal + instrumental, exported as lossless files (the project's delivery choice), both unmastered with headroom intact. The de-essing, the presence, the balance between them and the final loudness are set in the edit.` — or, on Suno: `capability_check: plan, split mode and credits | Auto Split, or Split from Mix on the vocal | export_spec: labelled derived stems plus the untouched source mix; inspect bleed and artefacts before mastering`  
**Source:** reference — Suno official pages, read 2026-09-23: Advanced Stem Separation, https://help.suno.com/en/articles/12702337 ; Pricing, https://suno.com/pricing ; Release Notes, https://suno.com/release-notes ; What types of files can I download, https://help.suno.com/en/articles/13926081 ; What counts as one download, https://help.suno.com/en/articles/13926145 . The Lyria side of this card is in the adapter in ENGINE-CHECK.md.  
**Shelf life:** dated — Suno's split modes, plans and credit costs as read on 2026-09-23. Recheck plan, split types and credit cost before execution and at least every 30 days.  
**Yields to:** `lyria.native_multitrack_stems` — More than a vocal/instrumental split is needed; Lyria 3.5 offers no stem output on any surface (see `lyria.native_multitrack_stems`). On Suno, Auto Split above gives up to 12 stems.  
`song_handoff.stem_separation_protocol`

---

### Locked Audio Measurement (The Golden Rule)

**Also called:** audio-locked timebase, frame-accurate song timing  
**What it is:** Deriving the exact duration of every scene, verse, and chorus strictly from the measured milliseconds of the final approved audio master.  
**Effect on the audience:** Guarantees that visual cuts land with surgical precision on musical beats, drum fills, and vocal lines.  
**Used for and where it works best:** Core pipeline bridge: Phase 5 exports the locked timing ledger; Phase 3 (the shot table), then Phase 6 (Storyboard), builds shot lengths from it.  
**Best in:** formats: Music Video, Trailer, Rhythmic Montage | genres: All  
**Avoid when:** Drawing storyboard frames with arbitrary durations without any musical timebase. *(Provisional Mode: In prompts-only or pre-generation runs where audio has not yet been synthesized, construct a provisional timing grid mathematically derived from the declared BPM and metre/measure count, explicitly flagged `pending_measured_duration`, with the planning BPM written beside it (BPM=X); re-measure and lock to millisecond audio once generated at the spend gate).*  
**Example:** `timing_ledger: Verse 1: 00:14.250 to 00:38.500 (duration: 24.25s = exactly 582 frames @ 24fps). In prompts-only mode: 8 bars @ 120 BPM = 16.0s provisional.`  
**Source:** assumption — the package's working figure, not a published standard; the frame and bar values are arithmetic (seconds × fps; bars × beats × 60 ÷ BPM), and the locked value is the one measured from the audio master.  
`song_handoff.locked_audio_measurement`

---

### Line-by-Line Timestamp Extraction

**Also called:** lyric timestamping, vocal onset detection, word-level timecodes  
**What it is:** Extracting the exact millisecond start and end timecodes for every single line and stanza sung in the generated track.  
**Effect on the audience:** Provides the foundational sync map for animated lyric typography, subtitle generation, and visual character performance.  
**Used for and where it works best:** Lyric videos, karaoke displays, and lip-sync video generation in Phase 8.  
**Best in:** formats: Lyric Video, Music Video, Animated Short | genres: All  
**Avoid when:** Guessing line start times by eyeballing the waveform roughly.  
**Example:** `timestamps: Line 1: [00:15.200 -> 00:19.450] "Nineveh stands above the river plain" (duration: 4.25s).`  
**Source:** assumption — the example's timecodes are illustrative, not a published standard; take the real ones from the rendered audio.  
`song_handoff.line_timestamp_extraction`

---

### Synchronized LRC & SRT Subtitle Generation

**Also called:** synced lyrics export, subtitle master file  
**What it is:** Exporting timestamped `.lrc` and `.srt` subtitle files matching the final song master with frame-accurate sync.  
**Effect on the audience:** Enables instant sing-along lyrics on YouTube, Spotify, and social media platforms, boosting viewer retention.  
**Used for and where it works best:** Standard delivery package for music streaming platforms and video uploads, where the file carries sing-along lyrics and every sung line gets its cue. Where the .srt is instead the subtitle a video audience reads, above all a translation, cue it by `textimg.subtitling_a_sung_line` — at the musical phrase, a repeated refrain once, a held line released early — and keep the every-line timing for the .lrc.  
**Best in:** formats: All released songs and music videos | genres: All  
**Avoid when:** Uploading unsynchronized plain text transcripts that fail to follow the singing beat.  
**Example:** `lrc_spec: [00:15.20]Nineveh stands above the river plain / [00:19.45]The lions roar beneath the temple gate.`  
`song_handoff.lrc_srt_generation`

---

### Beat Grid & BPM Detection

**Also called:** tempo mapping, transient grid alignment, beat clock  
**What it is:** Analyzing the audio master to establish the exact BPM (Beats Per Minute) down to two decimal places and mapping downbeat grid markers.  
**Effect on the audience:** Enables video editors to snap cuts, transitions, camera shakes, and flash frames exactly to musical downbeats.  
**Used for and where it works best:** Pre-visualizing music video edits in Phase 6 and Phase 8.  
**Best in:** formats: Music Video, Action Trailer, Dance Short | genres: All  
**Avoid when:** Editing on an un-mapped timeline where cuts drift randomly between beats.  
**Example:** `bpm_map: 112.50 BPM; 1 beat = 533ms (12.8 frames @ 24fps); downbeat every 2.133 seconds.`  
**Source:** assumption — the package's working figure, not a published standard; the example tempo is illustrative and the ms and frame values are arithmetic from it (60/112.5 = 0.533 s = 12.8 frames at 24 fps; 4 beats = 2.133 s); measure the real BPM from the master.  
**Yields to:** `anim_time.tempo_drift_rubato_alignment` — Rubato or free-meter material with no steady BPM.  
`song_handoff.beat_grid_detection`

---

### Song Architecture to Storyboard Shot Mapping

**Also called:** verse-to-visual mapping, structural scene tagging  
**What it is:** Dividing the song's musical sections into visual storyboard chapters: Intro (Establishment), Verse (Narrative), Chorus (Emotional Impact).  
**Effect on the audience:** Transforms a song into a compelling cinematic story rather than a disorganized montage of random b-roll.  
**Used for and where it works best:** The formal handoff document passed from Phase 5 to Phase 3 (the shot table), then Phase 6 (Storyboard Layout).  
**Best in:** formats: Narrative Music Video, Concept Film | genres: All  
**Avoid when:** Changing visual scenes in the middle of a continuous lyrical sentence.  
**Example:** `mapping: Intro -> Scene 1 (Archaeological dig); Verse 1 -> Scene 2 (Ancient king waking); Chorus -> Scene 3 (Grand palace spectacle).`  
`song_handoff.song_to_storyboard_mapping`

---

### Dynamic Dialogue Insertion Ducking

**Also called:** song dialogue window, musical dialogue pocket  
**What it is:** Declaring, at named timecodes, that spoken dialogue is going to sit on top of the song here and that a window has to exist for it. What belongs to this phase is the **window**: where it opens, where it closes, that it ends on a musical boundary rather than mid-phrase, and that the song is written or chosen with a section sparse enough to take a voice. **How far the song comes down inside that window is a level, set in the edit** — a dense chorus and a bare verse do not move by the same amount, and this package carried two different figures for it, which is what a card gets for deciding a level it cannot hear.  
**Effect on the audience:** Blends music video aesthetics with cinematic dialogue scenes; the speech is fully intelligible over the music.  
**Used for and where it works best:** Theatrical music videos that feature spoken drama scenes between verses.  
**Best in:** formats: Cinematic Music Video, Musical Film | genres: Drama, Action  
**Avoid when:** Sudden harsh volume cuts that sound like the music paused accidentally, or a window that opens mid-phrase rather than on a musical boundary.  
**Example:** `handover: dialogue window opens at 01:45 as Verse 2 ends and closes on the downbeat of Chorus 2. Song comes down for it and swells back on that downbeat — depth and recovery set by ear in the edit.`  
`song_handoff.dialogue_insertion_ducking`

---

### AI Vocal Pitch & Formant Audit

**Also called:** pitch correction pass, autotune check, vocal tuning audit  
**What it is:** Auditing the generated AI vocal track with pitch detection software to ensure all sustained notes are in tune with the backing chords.  
**Effect on the audience:** Eliminates painful off-key notes or sour microtonal drift that ruins an otherwise brilliant song.  
**Used for and where it works best:** Quality control before releasing the vocal master. Apply subtle pitch correction (Melodyne style) if needed.  
**Best in:** formats: Commercial Pop, Theatrical Anthem | genres: All  
**Avoid when:** Traditional microtonal scales where intentional quarter-tones are falsely "corrected" to standard Western notes.  
**Example:** `audit: Scan vocal stem for chromatic drift; lock terminal note of chorus to perfect A440Hz.`  
**Yields to:** `score.microtonal_quarter_tone_tension` — Maqam or microtonal material with intentional quarter-tones.  
`song_handoff.vocal_tuning_audit`

---

### Music Platform Loudness Mastering

**Also called:** Spotify/Apple/YouTube mastering, streaming loudness target  
**What it is:** Knowing which streaming services this release is going to, and that each of them normalises loudness to its own published target rather than rewarding a loud master. The destinations are a release decision and are named here; the targets belong to those services on the day, are looked up then, and are set at master time in the edit. They differ between services and they have been revised, so they are never carried in a card.  
**Effect on the audience:** Prevents streaming platforms from turning the song down and squashing its dynamic punch.  
**Used for and where it works best:** Final audio export for all music distribution.  
**Best in:** formats: Streaming Release, Digital Single | genres: All  
**Avoid when:** Mastering for maximum loudness — every one of these services will normalise it back down, and the dynamics do not return.  
**Example:** `handover: release goes to <named services> — master to each one's current published integrated target with true-peak headroom, checked on the day.`  
**Yields to:** `sync.broadcast_lufs_sync_mastering` — The track is a sync placement for broadcast or theatrical.  
`song_handoff.platform_loudness_mastering`

---

### Audio-Only Release Bundle Package

**Also called:** single release package, audio delivery archive  
**What it is:** Compiling the final audio release bundle: 24-bit 48kHz Master WAV, 320kbps MP3, Instrumental WAV, Acapella WAV, and synced LRC file.  
**Effect on the audience:** Provides a complete, professional commercial release ready for immediate upload to DistroKid, Spotify, or Bandcamp.  
**Used for and where it works best:** Final delivery when the project is an "Audio-Only Song" requiring no video clip.  
**Best in:** formats: Audio-Only Song Release, Album Track | genres: All  
**Avoid when:** Delivering messy, un-labeled audio files with generic names like "track1_final_v2.wav".  
**Example:** `bundle: {SONG_MASTER_48k24b.wav, SONG_INST_48k24b.wav, SONG_ACAPELLA_48k24b.wav, SONG_LYRICS.lrc}.`  
**Yields to:** `song_handoff.music_video_bridge_phase_6` — The song continues into a music video.  
`song_handoff.audio_only_release_bundle`

---

### The Music Video Handoff Bridge to Phase 3 and Phase 6

**Also called:** storyboard bridge, video handoff manifest  
**What it is:** Packaging the locked audio master, beat grid metadata, line timestamps, and song structure map for Phase 3 (the shot table), then Phase 6 (Storyboard Layout).  
**Effect on the audience:** Guarantees that the storyboard artists and AI prompt engineers know the exact duration and emotional goal of every shot.  
**Used for and where it works best:** Mandatory transition gate when the user chooses to create a Music Video for the song.  
**Best in:** formats: Music Video Production | genres: All  
**Avoid when:** Handing on to Phase 3 with arbitrary durations that ignore musical structure. *(Provisional Mode: In prompts-only workflows where audio generation is deferred, Phase 3 and then Phase 6 ingest a provisional BPM/metre-based timing grid calculated from song sections and bar counts, allowing complete visual storyboard and prompt engineering before audio synthesis).*  
**Example:** `handoff_manifest: audio_path: master.wav (or provisional_bpm: 120), total_duration: 03:24.120, beat_grid: 112.5 BPM, timestamp_file: timing.json.`  
**Yields to:** `song_handoff.audio_only_release_bundle` — The song ships as audio only, no video clip.  
`song_handoff.music_video_bridge_phase_6`

---

### Dynamic Energy Waveform Visualization

**Also called:** energy envelope export, waveform density map  
**What it is:** Generating an acoustic density map showing where the song's energy peaks, drops, and pauses across its timeline.  
**Effect on the audience:** Informs the visual director where to place high-motion camera moves (during energy peaks) and quiet still shots (during valleys).  
**Used for and where it works best:** Cinematography planning and VFX placement in Phase 6 and Phase 8.  
**Best in:** formats: High-Budget Music Video, Action Trailer | genres: All  
**Avoid when:** Cutting fast kinetic action scenes over quiet solo flute passages.  
**Example:** `energy_map: Section A (0:00-0:30): Low (25%) -> Section B (0:30-1:15): High (85%) -> Climax (2:30-3:00): Peak (100%).`  
`song_handoff.energy_waveform_map`

---

### Lip-Sync Video Phoneme Export

**Also called:** phoneme timing ledger, mouth shape cue sheet  
**What it is:** Generating a frame-accurate phoneme ledger for the lead singer's vocal track to feed into AI lip-sync video models.  
**Effect on the audience:** Enables flawless synchronization between generated singer face videos and the singing audio track.  
**Used for and where it works best:** Pre-processing for Runway, HeyGen, SyncLabs, and LivePortrait music video generation in Phase 8.  
**Best in:** formats: AI Singer Avatar, Music Video | genres: All  
**Avoid when:** Trying to lip-sync video without an isolated, dry vocal stem.  
**Example:** `phoneme_cues: Frame 120: /b/ -> Frame 123: /a/ -> Frame 126: /b/ -> Frame 130: /ɪ/ -> Frame 134: /l/ (Babylon).`  
**Yields to:** `dubbing.lipsync_no_lips` — The singing character has a beak or a rigid jaw.  
`song_handoff.phoneme_timing_export`

---

### Instrumental Stem Dynamic Re-Balancing

**Also called:** backing track re-mix, instrument EQ carve  
**What it is:** Once the song has been split, the instrumental stem can be re-balanced against the vocal it used to contain — leads pulled back where they crowd the voice, low end firmed up underneath it. This is a mix pass on a timeline and every value in it is set in the edit, always with the vocal stem playing; done in solo it will be wrong, because the whole point of the move is a relationship between two things.  
**Effect on the audience:** Creates a polished, professional master rather than a separated stem that still sounds separated.  
**Used for and where it works best:** Final polish on Suno and Lyria instrumental stems, after separation and before the master.  
**Best in:** formats: Commercial Music Releases | genres: All  
**Avoid when:** Re-balancing the instrumental in solo, without the vocal stem playing against it.  
**Example:** `handover: instrumental stem crowds the lead vocal — carve room for the voice and firm the low end, always with the vocal up.`  
`song_handoff.instrumental_rebalance`

---

### Chorus Repetition Visual Differentiation

**Also called:** chorus visual escalation, non-repetitive video rule  
**What it is:** The strict music video rule that while the chorus audio repeats verbatim, the visual imagery for each chorus MUST escalate in scale and spectacle.  
**Effect on the audience:** Prevents boredom; Chorus 1 establishes the feeling, Chorus 2 widens the scale, Chorus 3 explodes with full visual catharsis.  
**Used for and where it works best:** Planning music video storyboards in Phase 6.  
**Best in:** formats: Music Video | genres: All  
**Avoid when:** Re-using the exact same video clip for Chorus 2 and Chorus 3.  
**Example:** `escalation: Chorus 1: Singer solo in temple; Chorus 2: Singer with 20 dancers; Chorus 3: Massive crowd of thousands with fire torches.`  
`song_handoff.chorus_visual_escalation`

---

### Acoustic Ending Ring-Out Tail Preservation

**Also called:** reverb tail preservation, final decay protection  
**What it is:** Ensuring the final audio export preserves the complete, natural acoustic decay of the last musical chord (3 to 6 seconds) without an abrupt cutoff.  
**Effect on the audience:** Allows the emotional resonance of the song to settle into peaceful silence; prevents harsh digital truncation.  
**Used for and where it works best:** The ending of every musical master file.  
**Best in:** formats: All musical tracks | genres: All  
**Avoid when:** Slicing the audio file immediately after the final drum hit, cutting off the natural room reverb tail.  
**Example:** `export_rule: Extend master timeline 6000ms past the final instrumental strike to capture 100% natural reverb decay to -inf dB.`  
**Source:** assumption — the package's working figure, not a published standard; set the tail length against the measured decay of the rendered master.  
`song_handoff.ending_ringout_preservation`

---

### Cross-Genre Extended Suite Linking

**Also called:** multi-part song suite, progressive track link  
**What it is:** Stitching two distinct generated tracks into a single progressive suite (e.g. Acoustic Folk Intro -> Epic Metal Climax) with a seamless tempo bridge.  
**Effect on the audience:** Delivers an unforgettable, progressive musical journey that defies generic commercial song formulas.  
**Used for and where it works best:** Epic conceptual masterpieces, film overtures, and dramatic rock/folk operas.  
**Best in:** formats: Concept Album, Epic Overture, Theatrical Suite | genres: Epic, Progressive, Folk Metal  
**Avoid when:** Abrupt, un-tempo-matched cuts between wildly clashing musical styles.  
**Example:** `bridge_spec: Track A (Acoustic Oud 72 BPM) accelerates over 8 bars using frame drum to match Track B (Heavy Rock 110 BPM).`  
`song_handoff.extended_suite_linking`

---

### Archival Master Checksum & Vaulting

**Also called:** audio asset vaulting, session master preservation  
**What it is:** Hashing (SHA-256) and vaulting the final 24-bit 48kHz WAV master, stems, lyrics, and metadata into a permanent project archive folder.  
**Effect on the audience:** Guarantees that the audio master can never be accidentally modified, overwritten, or lost across future pipeline revisions.  
**Used for and where it works best:** The final archival closing step of Phase 5.  
**Best in:** formats: All released projects | genres: All  
**Avoid when:** Leaving final masters scattered across temporary download folders.  
**Example:** `archive_command: Move master WAV and stems to /masters/song_v1/ and generate SHA-256 integrity checksum.`  
`song_handoff.master_vaulting_checksum`
