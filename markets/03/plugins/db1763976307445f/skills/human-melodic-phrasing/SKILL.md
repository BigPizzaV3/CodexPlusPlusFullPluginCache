---
name: human-melodic-phrasing
description: Compose melodies, licks, riffs, solos, bass lines and vocal lines for Music Block that sound like a musician played them rather than a scale generator. Use whenever composing any melodic line, and when a user says the result sounds robotic, mechanical or boring.
---

Use this skill when composing any pitched line for Music Block: a guitar lick,
a horn melody, a bass line, a vocal phrase, a piano right hand. It does not
cover fingering (see playable-fretted-parts) or instrument ranges (see
instrument-ranges-and-idioms).

The Music Block format has no dynamics, accents, staccato, grace notes, ties
or slurs. Everything human about the line must therefore come from four
things you do control: which notes, which rhythms, where the rests are, and
the technique markings on fretted instruments. Write with that in mind.

## Workflow

1. Name the idiom (blues, bebop, pop, folk, funk, classical) and open the
   matching file in `references/` if one exists. Its target notes and
   rhythmic habits override the generic advice here.
2. Design a motif: a two- to four-note idea with a distinctive rhythm that
   fits in half a bar or one bar.
3. Draw a phrase map before writing notes. For a 4-bar example: bar 1 states
   the motif, bar 2 repeats it with one change, bar 3 contrasts (new contour
   or register), bar 4 resolves and leaves space. For 2 bars: state, then
   answer. For 8 bars: two 4-bar phrases where the second ends more
   conclusively.
4. Place the target notes on strong beats, then fill between them.
5. Write the rhythm with rests and one or two syncopations, then the pitches.
6. Add technique markings (fretted) at the expressive points.
7. Run the self-check, then call the tool.

## Motif and repetition

- Repetition is what makes a line sound intentional. Every example longer
  than one bar should repeat at least one rhythmic or melodic cell.
- Vary a repeat by one parameter at a time: transpose it to the next chord,
  change its last note, displace it by an eighth, or invert its direction.
- A lick that never repeats anything is the single most common "generated"
  tell. So is a lick where every bar is different.

## Breathing and space

- End phrases before the barline or on the downbeat, then rest. Never fill
  every beat of every bar. In a 4-bar lick, at least one full beat is rest.
- Not every bar starts on beat 1. Use pickups: start a phrase on the "and" of
  4 or on beat 4 of the previous bar, with rest beats first so the tool keeps
  the notes in place.
- Long notes are phrasing too. A held note with vibrato after a run is how
  players mark a phrase end.

## Contour

- Mostly stepwise motion (seconds and thirds). One larger leap per phrase,
  then move back by step in the opposite direction.
- One clear peak per phrase, usually in the second half. Do not visit the
  peak twice.
- Avoid sawtooth scales: running straight up or straight down for more than
  five notes in a row without a change of direction or a repeated note.
- Avoid the arpeggio wander: chord tones cycled up and down in even values
  with no goal note.

## Target notes and harmony

- On beats 1 and 3, land on chord tones of the current chord (3rd and 7th
  say the most; the root says the least). Tensions and passing notes go on
  weak beats and offbeats and resolve by step.
- Over a dominant chord, tensions (b9, #9, #11, b13) resolve down by half
  step into a chord tone of the next chord. Over a ii-V-I, aim the line at
  the 3rd of the I chord on its downbeat.
- Approach a target from below by half step or from above by scale step;
  enclosures (one note above, one below, then the target) are idiomatic in
  jazz and blues.
- When the example demonstrates a scale, still phrase it: group the scale
  into a rhythm, end on a chord tone, add one rest.

## Rhythm

- Mix values inside a bar: eighths with one dotted figure, a triplet, or a
  quarter placed on an offbeat. A bar of eight identical eighths is fine once
  per example, not in every bar.
- Syncopate with rests and dotted notes, since ties are not available: a
  dotted quarter on the "and" of 1, an eighth rest before beat 3, a note on
  the "and" of 4 that ends the bar.
- For swing, bebop, shuffle and jazz-blues set the example's `feel` field
  and write straight eighths. Never fake swing with 12/8 or triplets.
- Keep one rhythmic motif recognisable across bars; change pitches more than
  rhythms.

## Technique markings as expression (fretted parts)

- Slide into the first note of a phrase or into a target note.
- Hammer-ons and pull-offs for pairs of eighths or sixteenths in a run;
  they mark the legato a player would use.
- Bends at phrase peaks; a full bend to the target with vibrato is a phrase
  ending in blues and rock.
- Vibrato on quarter notes or longer that end a phrase.
- Two to four markings per lick. A marking on every note is as robotic as
  none.

## Avoid list

- Unbroken streams of eighths or sixteenths with no rest.
- Straight scale runs of six or more notes in one direction.
- Identical rhythm in every bar.
- Every phrase starting on beat 1 and ending on the root.
- Arpeggios cycled up and down with no target.
- Constantly new material with nothing repeated.
- A wide leap followed by another leap in the same direction.
- Tension notes on strong beats without resolution.

## Self-check before calling the tool

- The line has one motif that appears at least twice, varied once.
- There is at least one rest per two bars and a pickup or offbeat start
  somewhere.
- Strong beats carry chord tones; tensions resolve by step.
- No run longer than five notes in one direction; one peak per phrase.
- Rhythm varies within bars but a cell recurs across bars.
- Swing is set through `feel`, not through note values.
- Fretted parts carry two to four technique markings at expressive points.
