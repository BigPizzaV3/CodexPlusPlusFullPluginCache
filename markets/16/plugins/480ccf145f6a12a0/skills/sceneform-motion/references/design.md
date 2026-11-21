# Motion design

Craft for the film itself. The engine reference (`read_motion_reference`
with `document: "engine"`) says how to build each of these; this file says
what to build. [looks.md](looks.md) holds the visual systems to choose
from when the user brings no references.

## Plan the beats

- A hook in the first two seconds, then the point, the proof, and the call
  to action. One idea per beat.
- About three seconds per beat, with an accent roughly every three seconds:
  a word landing, a number counting up, a cut on the music.
- On-screen text holds long enough to read twice: about a third of a second
  per word plus half a second, and never under one and a half seconds.
- The final frame holds the call to action or logo for at least one and a
  half seconds.
- Draw anything exact in code: text, numbers, logos, charts, interfaces.
  Generated video is for live motion only (people, products in real space);
  make it with sceneform-generate and import it.

## Show, do not label

- "Show the product" means the product doing something, with one line of
  copy carrying the meaning. Labels, chips, badges, a HUD, a calendar, a
  phone mockup, or a static headline over footage are explainer chrome:
  they describe instead of show and read as a slide. Use none unless the
  user asks for them.
- One visual language, stated in the storyboard and kept: for example a
  dark stage, serif cards between cuts, brackets only on visual subjects.
  Agreed up front, not discovered on the twelfth correction.
- Decoration starts rationed. A motif (brackets, glow, light leaks, grain,
  a shader look) at full strength on every cut is the version that gets cut
  back to a fifth once the user sees it, so begin at a fifth. "Sparingly"
  is the starting setting, not the correction.
- Brand colours, surfaces and type come from the BrandKit or the user's
  site, read before the storyboard: its neutral, its accent, its serif or
  sans, its interface colours. An invented palette on a brand film is the
  first thing the user corrects.

## Remakes and series

- "Like the last one" means its quality, brand and voice, not its scenes.
  A new film in the series gets a new concept and a new structure; the
  storyboard says what carries over (look, narrator, music family) and what
  is new. A film that reads as the previous one re-skinned is rebuilt.
- Assets are fresh per film: the user's library, their site, and generated
  b-roll cast for this film. Never the previous film's set.
- When the user asks for a remake to come back toward an earlier cut, keep
  the lines and shots they praised word for word and shot for shot, and
  change only what they named.

## Cuts and camera

These are the defaults for a film with no look chosen. A look's own motion
rules replace them: Quiet geometry and Blueprint never cut, Aurora pushes
and scrolls, Dark cinematic pushes in on its holds.

- The default is a hard cut on the beat, with the camera still inside the
  shot. A film is carried by what happens inside its frames and by what
  each cut hands to the next, not by the camera. A hard cut still hands one
  thing across (an element in flight, a colour, a position that the next
  layout picks up); the check's `hardCut` names a cut that keeps nothing,
  which is the reset to avoid.
- Camera moves are rare and large: two or three sweeps in a 30 second film,
  each slow, then fast, then settling, each with parallax (a far layer
  moving slower than the subject, a near layer faster). The rest holds
  still. A drift, roll or whip on every scene is the version that gets
  reverted.
- Stepped animation (elements held on twos, every value on hold keys two
  frames apart at the film's frame rate, while the camera and any footage
  stay smooth) is a look choice that reads as made by hand. State it in the storyboard and apply it to everything
  inside the frame, not to a few layers.
- Where two scenes share a subject, carry it: a push through one element
  into the next scene, or a word that stays while the frame changes.
  Where they share nothing, cut.

## When the user asks for more

- "More X" means two or three more places, not every scene. Add it where
  it serves the message, show the frames, and ask before going further.
  The jump from three sweeps to a sweep on every scene cost a rebuild.
- Keep the values a change replaces (the old tracks, the old timings) in
  the plan file, so a revert is one edit.
- When a correction names an extreme ("super fluid", "way more"), build
  one step past the current version, not the extreme.

## Copy

- Write the on-screen words as one sentence across the whole cut before
  placing any of them, so each line sets up the next ("One second. / To be
  seen. / Or scrolled past."). A line written to fill a slot reads as
  filler.
- Each line is short, holds long enough to read twice, and the last one is
  the line the viewer leaves with.

## Voice and music

- One narrator, clear and unhurried, in the gender and register the user
  asked for. Character voices (a movie trailer, a villain, an elderly
  gentleman, a cartoon) read as creepy on a brand film; use one only when
  the user asks for it. Several voices in one film are a device the
  storyboard names and the user approves first.
- Music is chosen for structure, not genre: a track whose first hit lands
  on the key line and whose drop lands on the proof beat. Generate two or
  three directions, one take each, named by subgenre, lead instrument and
  tempo ("ethereal breakcore, music box and bells over chopped breaks, 170
  BPM"), not by mood words alone, which come back generic. Pick by
  measuring where the hits fall against the script.
- Eleven Music takes a `duration` setting (15, 30, 60, 120, 180 seconds);
  Lyria picks its own length. Either way, measure the file: tracks come
  back longer than asked, so choose the 30 second window whose drop lands
  where the cut needs it and start the layer there.
- Build to the voice first, then lay music under it low enough that every
  word stays clear: measure the voice against the music per second in the
  rendered draft. The mix ducks music under speech by 6 dB by default, and
  dense music still buries a voice at that: set `duck` to 9 or more, or
  lower the music layer's volume under speech, and bring it back for
  wordless beats and the end card.
- Two to four sound effects per ten seconds, each landing on something that
  moves, each at its own velocity. A per-letter tick is one effect, not
  one per letter.
- Social video lands around -14 to -16 LUFS overall, with peaks under -1
  dBTP. A film with effects and no music bed normalises to -16 with hits
  at low velocity; at -14 the limiter crushes every hit by 10 dB or more.

## Footage

- Cut to the references. Measure their shot lengths (the median and the
  shortest burst) and match them; a fast cut is under half a second, and
  bursts shorter still.
- Generated clips are material for hypercuts and textures, not hero shots:
  abstract macros (an eye, ink in water, a fern, a match) cut well, while a
  profile at sunset or a lens aperture reads as stock. Generate three per
  slot and choose from a sheet.
- A clip the engine refuses to decode is re-encoded with your own tools at
  a constant frame rate and re-imported; a clip held on its last frame
  through a time remap is cut to end on that frame instead.
- Anything exact or heavy is better made outside the engine (an image
  sequence or clip from your own tools) and imported, with the engine kept
  for type, brackets, sound and the mix: that exports in minutes where
  full-frame shaders take an hour.

## Type and layout

- One or two type families. Contrast comes from weight and size, not more
  fonts.
- On a phone-first video, headlines run about 6 to 10 percent of the frame
  height and nothing readable is smaller than about 3 percent.
- Text contrast against what sits behind it is at least 4.5 to 1; add a
  scrim or a plate when footage varies.
- 9:16 safe area: keep text and key subjects out of the top 10 percent, the
  bottom 20 percent, and the right 15 percent, where platform buttons and
  captions sit.
- Neighbouring beats differ in layout; the same composition twice in a row
  reads as a stall.
- Anything that must hug a word (a box, an underline, a highlight) is
  placed from the word's measured `ink`, never from its font size.
- Brand colors, fonts, and logo come from the BrandKit; the logo sits on a
  background it stays visible against.

## Captions

- Words come from the script, timed to the speech.
- At most about five words and 32 characters per cue, broken at natural
  phrase ends. Re-chunk rather than shrink the type.
- Captions never cover a face, a product label, or other on-screen text.

## Motion

- Elements enter staggered, a beat apart (A, then B, then C), and land with
  a clear stop: ease out, with a small overshoot for energy and none for a
  calm brand.
- Exits are faster than entrances.
- A hold keeps a little life: a slow drift or a gentle scale of a few
  percent, unless the look is stepped, where a hold is still.
- Cuts and big entrances land on the music's beats.

## Checklist before rendering

- The first frame already shows something.
- Every line of text is on canvas, inside the safe area, and readable at
  phone size in the preview sheets.
- Each beat holds its text long enough to read twice.
- No two neighbouring beats share a layout.
- Every cut hands something to the next frame, or is a deliberate hard cut
  on a beat.
- The call to action holds at the end.
- Sound is present where expected and the voice sits above the music.
