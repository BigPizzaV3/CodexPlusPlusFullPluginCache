# Arranging and simplifying: choose a paradigm from evidence

Read this when the user asks for an arrangement, a simplification, a level (简易版, 五指版),
another texture or style, a piano version of a band or orchestral piece, an accompaniment to
sing with (弹唱) or a playable two-hand jianpu. Reviewing stays in [good-score.md](good-score.md).

## Ground rules

- The faithful transcription is the master. An arrangement is a new, named score beside it,
  made only on the user's request. Never edit the master into an arrangement and never
  "correct" a transcription toward a familiar pattern: if the recording disagrees, it wins.
- A paradigm is a hypothesis about one section, not a template for the song. "Pop piano: RH
  melody, LH broken chords" is one card among many below. Choose per section from evidence
  (recording, transcription, the user's goal) and name the evidence.
- Ask only what the evidence leaves open; otherwise go ahead with stated defaults that keep the
  song's meter, feel and key changes unless the user asked otherwise, and offer alternatives.
- Talk to users in plain words ("very easy", "beginner", "easy piano"): level codes (L0–L5) and
  card numbers (P1–P17) are for your planning only, never for replies or score titles.
- An easier version must be easier to play by default, not only to read: lower at least one
  playing axis (below) and offer the original texture as the next step up.
- Never change a melody note, leading tone or chord quality to avoid black keys or accidentals;
  one accidental is easier than a wrong note.
- Report every class of change against the master: removed notes, octave shifts, simplified
  rhythms, transposition, new patterns, a dropped key change.
- An arrangement of a copyrighted song is a derivative work: fine for the user's own practice;
  ScoreStarling grants no right to publish, sell or perform it (not legal advice).

## Step 0: what is the source?

| Source | "Faithful" means | A piano score of it is |
| --- | --- | --- |
| Original solo piano piece or performance | What the pianist played | A transcription; simplifying is arranging |
| Someone's piano cover (Bilibili, YouTube) | The cover's notes, not the original song | A transcription of the cover |
| Band or produced track | No single piano part exists | Always an arrangement (reduction) |
| Voice or one melodic instrument | The melody | A lead sheet; any accompaniment is added |
| Solo fingerstyle guitar | Guitar notation or tab | A piano version is an arrangement |
| Orchestra, film cue, choir | The parts | A piano version is a reduction |

## Step 1: what does the user want?

| Deliverable | Contents | What users call it |
| --- | --- | --- |
| Note-for-note transcription | Everything played, original key | 还原版, 扒谱, "exactly as played" |
| Lead sheet | Melody + chord symbols (+ lyrics) | 旋律+和弦, 即兴伴奏谱 |
| Piano & vocal | Accompaniment for a singer; melody in RH optional | 弹唱版 |
| Piano solo / cover | Melody on top + accompaniment, any level | 钢琴独奏, 钢琴版 |
| Easy / beginner | Graded simplification of the solo | 简易版, 初级, 入門 |
| 5-finger / big-note | One fixed hand position, plain rhythm | 五指版 |
| Two-hand jianpu | RH row over LH row (see Jianpu) | 双手简谱 |

For 还原版 or "exactly as played", apply no card below: use them only as listening hypotheses
and to choose notation (meter, voices, beaming, a swing mark). Messy-looking notation is fixed
with notation tools, not by making the playing regular; offer a tidier arrangement separately.

## Workflow

1. Name the source (Step 0) and the deliverable (Step 1) in one line.
2. Settle the master first, by ear: beat level and meter (3/4 or 6/8), pickup, swing or
   straight; the melody (see Reduction priority 1);
   key changes (accidentals that persist for a section after a new dominant 7th, e.g. B7 → Em,
   mean a new key the signature misses). `set_key` changes only the opening key: report an
   unmarked change in the master and mark it with `K:` in the new score.
3. Map the sections (intro, verse, pre-chorus, chorus, bridge, outro); read each one's cues
   (below) and pick a card and a level for it. Note where the texture changes.
4. Ask the open questions (Questions), a few at a time.
5. Write the arrangement: `export_score` the master as `abc`, rewrite it and `create_score` a
   new score titled in plain words with song, version and key (e.g. "… — Easy piano, 1=C").
   Start a new key with `K:` at its bar so jianpu prints the new `1=`. Transpose only the copy.
6. Verify: A/B each section against the master (melody notes, rhythm and contour, bass at
   changes, chord spelling under the key signature, hooks, key changes, section weight); check
   every exported page; report changes per difficulty axis. The learner's playing decides.

## Reading a section

Per section, not per song: harmonic rhythm (chords per bar; pushed an 8th early?); the bass or
LH onset grid (8ths, 16ths, triplets, swung); notes struck together (block) or one after
another (broken); bass placement (every beat, 1 and 3, 1 only); who carries the melody; the
accents that make the beat (two, three, four or six per bar); the drum pattern (backbeat on 2
and 4, cross-stick, four-on-the-floor, brushes, clave). Describe only what you have read, e.g.
"verse: RH melody / LH 1-5-8 in 8ths; chorus: RH melody in octaves / LH octave bass + chord".

## Reduction priority

1. Melody: the top voice in a piano solo; in 弹唱 it may be left to the singer. Find it from the
   sung line and the verse's contour and register, not the highest note: a cover's chorus often
   doubles the tune in octaves or puts octave hits or a hook above it.
2. Bass at chord changes.
3. Chord identity: root, 3rd, 7th. Drop 5ths and doublings first; never drop the 3rd.
4. The rhythmic signature: anticipations, groove, swing, the 6/8 lilt.
5. Hooks: intro riff, counter-melody, interlude, the last-chorus lift.
6. Fills, inner motion, doublings.

Shift a note by an octave before deleting it. Rhythm edits are style edits: straightening
anticipations or swing changes the genre, so offer them as options, never as cleanup.

**Section weight.** Verse lighter, chorus fuller: more voices, octave bass or melody, a wider or
busier LH, a stronger rhythm; intro and interludes carry the hook. Keep the contrast at every
level, even the easiest (single LH notes in the verse, two-note LH chords in the chorus).

## Difficulty ladder

| Level | Typical content |
| --- | --- |
| L0 5-finger | Both hands in one position, simple key and rhythm |
| L1 very easy | RH melody; LH single bass notes or simple chords, little movement or syncopation |
| L2 beginner (≈ grades 1–3) | Rhythms simplified where needed; basic LH pattern; close inversions |
| L3 easy piano (≈ grades 2–4) | Whole song; original bass line and syncopation kept |
| L4 intermediate | Broken or arpeggiated LH, inner chord tones, pedal |
| L5 piano solo / advanced cover | Octaves, wide arpeggios, fills, full voicings |

For beginners (L0–L2) simplify the accompaniment's rhythm before thinning notes: syncopated or
off-beat LH stabs become on-beat notes or chords (beats 1 and 3, or 1 only). Keep the melody's
rhythm, real triplets and the swing or 6/8 feel as written unless the user asks; a notation-only
change (swing written as straight 8ths) is not an easier version. Then lower other axes one at a
time and name the cost: hand positions (inversions, a fixed position); span (close voicings,
octave shifts); notes at once; note rate; key (changes the sound; move key changes with it);
pedal; reading load (ledger lines, octave dots). Keep the bass at changes and the hook. Levels
are labels, and two beginners differ (a weak reader, a small hand): ask; invent no single score.

## Paradigm cards

Cues → texture (hands) → ladder → not when. Each card is one option for one section.

**P1 Lead sheet, chord accompaniment (即兴伴奏).** Cues: the user sings or plays along; the
source is one voice or instrument; they ask for chords. Melody + chord symbols; the player picks
a pattern (the Chinese syllabus: 柱式 block, 半分解 bass then chord, 分解 broken, 八度/十度 bass,
8-beat/16-beat). L1 symbols only → L3 a written accompaniment (P2–P4, P16). Not when every note
is wanted, or the chords are ambiguous (offer two readings).

**P2 Pop ballad, broken chords (分解/琶音).** Cues: one steady LH note stream (8ths; 16ths when
slow) spelling the chord, bass on each change, pedal; lyrical slow or mid-tempo songs. LH 1-5-8,
1-5-8-5, 1-5-10, long 1-5-1-2-3. L1 root in whole/half notes → L2 1-5-8 in quarters → L3 1-5-8-5
in 8ths → L4 tenths, long arpeggios, RH chord tones → L5 octave melody. Not when: the record
plays block, syncopated or riff parts; uptempo or dance grooves; swing; 6/8 (use P6's figures).

**P3 Block and semi-broken (柱式/半分解), pads.** Cues: three or more notes together; held pads,
a quarter pulse, repeated 8ths, the "1 (2) &" syncopation; bass on strong beats and chords on
weak ones. Fuller choruses, anthems, hymn-like or gospel ballads. L1 whole-note triads in close
inversions → L3 bass + chord → L4 syncopated with anticipations → L5 octave bass. Not when the
part is really broken; respace close triads below about C3.

**P4 Driving pop/rock, 8-beat and 16-beat.** Cues: backbeat on 2 and 4; hi-hat 8ths or 16ths;
bass on root 8ths; chords pushed an 8th early; half-time choruses. LH takes the bass guitar
(root, octaves, root–5th), RH the melody over chord stabs; drum accents move into the LH rhythm.
L1 LH root halves → L2 repeated root 8ths → L3 octaves → L4 RH stabs → L5 16-beat fills. Not
when: ballad sections, an arpeggiated keyboard part.

**P5 Waltz and 3/4.** Cues: one strong beat in three; bass on 1, light chords on 2 and 3
(oom-pah-pah) or broken 1-5-3. L1 dotted-half bass → L2 bass + two chords → L3 broken 8ths.
Not when the 8ths group 3+3 under two strong beats (P6); a real hemiola stays as written.

**P6 Compound 6/8 and 12/8.** Cues: whole sections divide each beat into three; long-short
(quarter–eighth) melody inside each group of three; bass every dotted quarter; LH figures in
threes. Slow ballads, folk, doo-wop and soul (repeated triplet chords), 12/8 blues, barcarolles.
LH rocking 1-5-8-10-8-5, or bass on dotted quarters. L1 dotted-quarter bass → L2 two-note rocking
→ L3 broken 6/8 → L4 RH triplet chords. Not when: swing (P9); a few triplets in 4/4. A 6/8 song
written as 3/4 keeps its notes: `set_meter` on the master after the user confirms the count;
`bpm` counts quarters (dotted-quarter tempo × 1.5).

**P7 Classical, chorale, hymn, SATB.** Alberti (low–high–middle–high), chorales, independent
voices: the composer's text is the master and easier editions (Alberti → blocks) are
arrangements; do not pop-ify. Choirs: S/A on the treble staff, T/B on the bass staff, stems
up/down; L1 melody + bass → L2 melody + LH triads → L3 four parts.

**P8 Two-step bass: stride, boom-chick, polka, march.** Cues: bass (root, 5th or octave) on 1
and 3, chord on 2 and 4; country and folk alternate root and 5th, often with a cross-stick
backbeat; stride leaps wider and usually swings; ragtime is straight. One LH layer alternating
bass and chord. L1 bass on 1, chord on 3 → L2 root/5th + chord inside an octave → L3 octave
basses → L4 tenths. Not when: 3/4 (P5); a boogie ostinato (P10).

**P9 Swing jazz.** Cues: long–short 8ths across many beats (the ratio varies with tempo),
walking bass, ride or brushes, comping on 1 and the "and" of 2, 7th chords. Solo piano: LH
shells (root–7th, root–3rd), RH melody with guide tones; with a bassist, rootless voicings. L1
RH melody, LH roots or shells in halves on 1 and 3 → L2 the comping rhythm ("and" of 2) → L4
rootless voicings. Notation: straight 8ths plus a "Swing" mark; real triplets stay triplets (a
learner can read one). ScoreStarling has no swing playback: straight 8ths play straight, triplet
notation plays swung; say so and let the user choose. Not when: Latin, straight ballads.

**P10 Blues shuffle, boogie-woogie.** Cues: 12-bar I–IV–V; one LH figure moved with each chord,
eight notes to the bar; shuffle or straight. L1 root–5th halves → L2 root–5th/6th shuffle → L4
full boogie with RH riffs. Not when the record plays straight rock (P4).

**P11 Bossa nova, samba.** Cues: not swung; bass on 1 and 3 (root, 5th) with short pickups;
offbeat chords in a two-bar pattern; 6, 9, maj7 chords. Write 2/4 or 4/4 and say which. L1 LH
root–5th on 1 and 3 → L2 one offbeat RH chord a bar → L3 two-bar comping. Not when swung.

**P12 Afro-Cuban montuno, clave.** Cues: 2-3 or 3-2 clave (ask or flag it); a one- or two-bar
piano ostinato in octaves, aligned to the clave. L1 melody + roots loses the style (say so).

**P13 Band → piano (reduction).** Map roles: lead vocal or melody instrument, bass, harmony
instruments, hooks (intro riff, lead line, counter-melody), drums. Match the groove per section
with P2–P6 or P8–P12, apply the reduction priority, make the chorus fuller, put the hooks in the
intro and interludes, let the LH rhythm imply the drums, then check span and speed per hand.
The multitrack transcription is the master; generator output is one arranger's choice to review.

**P14 Orchestral, film, stage → piano.** Keep melody and bass whole; redistribute harmony; drop
filler; collapse doublings; fast repeats → tremolo; pads → held chords; keep rhythmic activity
and motives consistent. Ask: rehearsal reduction (complete) or performance solo (idiomatic)?

**P15 Anime, J-pop, C-pop covers.** Cues: verse, pre-chorus, chorus; royal road IV–V–iii–vi; key
changes, often from pre-chorus into chorus (frequently by a third) and at the last chorus; dense
16-beat production. Cover texture: RH melody (octaves or chord tones in choruses), LH wide
arpeggios in ballads or driving octaves in fast songs, the record's hooks in intro and
interludes, strong section contrast; many covers of one song are valid. Keep key changes: an
easier key moves every section by one interval (choose it for the main section). If the user asks
for one key ("in C", "no black keys"), deliver it, say in one line that this flattens the key
change, and offer a version that keeps it (one interval, a new `1=` at the change).

**P16 Piano & vocal (弹唱).** Cues: the user will sing; the lyrics matter. The piano need not
carry the tune (double it only if asked); keep the voice's register clear; give the hook to the
intro, interludes and ending; LH bass + RH chords in the song's rhythm. L1 LH root + RH triad
per chord → L2 半分解 → L3 broken or rhythmic grooves. Ask who sings and their range (key).

**P17 Solo fingerstyle guitar.** Cues: thumb alternating bass strings on the beat, melody above,
open strings ringing (Travis picking). Faithful: treble clef an octave lower, melody stems up,
bass down, tab optional. Piano: thumb → LH, melody → RH; strummed parts → a chord chart (P1).

## Jianpu as the deliverable

ScoreStarling's jianpu writes one row per staff and merges a hand's voices into stacked chords, so a
note held under moving notes is printed again at each of them. If the user wants the held voice shown
once, export `jianpu_voices` or `jianpu_fixed_voices` (a second row for it), or make the hand one rhythm
in an authorized arrangement. Minor keys read from the relative major, a new `1=` prints at each key-signature
change and only triplets are drawn among tuplets. Thin dense LH arpeggios (long underlines, many low
dots) or offer a chord-symbol version (P1); keep complex polyphony and rhythm in staff notation.
Digits read the same in every key but hands do not: `1=♭G` is mostly black keys. Offer the
original and an easier key as separate versions, each key change with its own `1=`; a player who
reads fixed do gets the same pitches as `jianpu_fixed` (1=C, 固定调, each black key marked). Jianpu alone
does not make music easier to play. When a minor song is wanted "in C" or without black keys,
tell the user once, plainly: it becomes A minor, written `1=C` with 6 as home.

## Questions (only what the evidence leaves open, a few at a time)

1. Player: level, comfortable span (octave? ninth?), pedal, staff or jianpu, black keys.
2. Purpose: solo, singing along, accompanying someone, an exam or lesson, study.
3. Key: original or easier; keep the key changes?
4. What must stay: intro, interlude, a riff, the last chorus, the original rhythm.
5. Feel: counted in 2, 3, 4 or 6; swung or straight.
6. Length and versions: the whole song or a section; the master stays; the new version's name.

## Sources

Summarized in our own words. Open Music Theory 2e: [popular music](https://human.libretexts.org/Bookshelves/Music/Music_Theory/Open_Music_Theory_2e_(Gotham_et_al.)/07%3A_Popular_Music),
[swing](https://viva.pressbooks.pub/openmusictheory/chapter/swing-rhythms/),
[compound meter](https://viva.pressbooks.pub/openmusictheory/chapter/compound-meters-and-time-signatures/),
[jazz voicings](https://human.libretexts.org/Bookshelves/Music/Music_Theory/Open_Music_Theory_2e_(Gotham_et_al.)/06%3A_Jazz/6.03%3A_Jazz_Voicings).
[Hutchinson, accompanimental textures](https://musictheory.pugetsound.edu/mt21c/AccompanimentalTexture.html); [Belkin, score reduction](https://alanbelkinmusic.com/score-reduction/);
[Takamori et al. 2017](https://ipsj.ixsq.nii.ac.jp/record/183046/files/IPSJ-MUS17116013.pdf) (good piano arrangements);
[Nakamura & Yoshii 2018](https://arxiv.org/abs/1808.05006) (reduction by difficulty); [POP909](https://arxiv.org/abs/2008.07142);
[Sheet Music Direct, arrangement types](https://blog.sheetmusicdirect.com/2018/09/piano-arrangements-explained.html); [曹西征 et al. 2016](https://www.htu.edu.cn/_upload/article/files/9b/5f/8a780bb245a7a566eb452f47e86a/7d680af8-1860-4d35-ab29-9b3272002af2.pdf)
(柱式, 半分解, 分解); [Li 2026, anime-song modulation](https://www.mtosmt.org/issues/mto.26.32.1/mto.26.32.1.li.html);
Wikipedia (numbered notation, stride, boogie-woogie, bossa nova, guajeo, Travis picking, royal road).
