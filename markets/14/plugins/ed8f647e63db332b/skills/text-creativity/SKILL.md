---
name: text-creativity
description: "Choose fonts, colors, layout and motion for on-screen text in Donkey Cut. Use when the user wants titles or captions to look designed."
---

# Text creativity: fifty devices
Ways to make a run of words worth watching. Every one is buildable with the tools you already have — add_text_sequence composes most of them in a single call; the rest are update_overlay, set_overlay_keyframes, set_mask, add_shape and add_overlay_video on top.

Read this before any text-heavy job the user calls flat, boring, samey, or "not creative". The failure mode is always the same: one design repeated a hundred times at dead center. Pick three or four devices from different groups and commit to them for the whole video — a run using twenty devices is noise, and a run using none is wallpaper.

## Rhythm — what changes from line to line
1. **Hero and whisper.** Mark the hook `emphasis: hero`, the throwaway line `whisper`. Size contrast is the single strongest signal that a video was designed.
2. **Small to large.** March size up across a passage: whisper, normal, normal, hero. The build is the payoff.
3. **Large to small.** The reverse, for a line that trails off or an admission.
4. **Section palettes.** Label verse/chorus/bridge with `section` — the rotas restart and the passages stop looking alike.
5. **Escalating repeat.** A repeated hook already steps up size each time it comes round. Push it further by naming the last one hero.
6. **One word per screen.** Break a line into its words as separate lines on the beat. Fast, percussive, made for a drop.
7. **Held line, moving words.** The opposite: one line up for four bars with a slow `push` move under it, while everything else is fast.
8. **The rest.** Leave a beat with nothing on screen before the hook. Silence in the picture makes the next line land.
9. **Off-beat entry.** Start a line a sixth of a second before its vocal rather than on it — text read early feels sung, text read late feels subtitled.
10. **Anticipation card.** A whisper line holding a single word ("almost…") between two loud passages.

## Type — the faces themselves
11. **Two-face pairing.** A display face for the hook, a neutral one for the rest. The bold ensembles already do this; hold it steady rather than adding a third.
12. **Mixed case on purpose.** Caps faces (anton, bebas, bangers, archivo-black) shout; sentence-case faces (montserrat, poppins, space-grotesk, playfair, dm-serif) speak. When a user says everything is shouting, the fix is a mixed-case face, not smaller type.
13. **Handwriting for confession.** caveat and permanent-marker read as a person, not a title card.
14. **Serif for weight.** playfair and dm-serif carry ballads, credits and anything that should feel written down.
15. **Mono for machinery.** mono plus a typewriter entrance for anything that should read as a screen.
16. **Tracking as tone.** letter_spacing 0.06–0.12em on a serif reads expensive; -0.01em on caps reads like a poster.
17. **Line height as pace.** lineHeight under 1.0 on caps packs a block; 1.4 on a serif opens it out.
18. **Stroke instead of shadow.** A heavy stroke (0.03–0.05em) over footage keeps type legible where a shadow goes muddy.
19. **Word-level color.** A per-line `color` on the one line that matters marks it without touching the rest.
20. **The mismatched word.** One word of a phrase on its own element, in another face, tilted, overlapping the rest. Two calls, enormous effect.

## Composition — where words sit
21. **Stop centering everything.** A hundred lines at 0.5/0.5 is the flattest thing text can do. Every layout except `center` fixes it in one parameter.
22. **Stack.** Lines step up and down the middle column so a phrase builds vertically.
23. **Call and response.** `alternate` swings left and right — perfect for question/answer or two voices.
24. **Ladder.** Each line a rung lower, then back to the top: lists, countdowns, verses.
25. **Drift.** A slow diagonal walk for long holds and ballads.
26. **Scatter.** Scattered chaos for punk, comedy and anything frantic.
27. **Corners.** Poster energy — words claiming the edges of the frame.
28. **Left rail.** Pin a whole passage to x 0.22 with align left; the empty right half is the composition.
29. **Overlap on purpose.** Two elements on DIFFERENT rows at the same time, one behind the other — a big pale word behind a small sharp one. Same row would slide them apart, so give the back word a higher lane.
30. **Off-frame bleed.** A hero word sized past the frame edge so it is cropped. Set size well over the fit and let it bleed.
31. **Rule of thirds.** Park the run at y 0.33 or 0.66 rather than 0.5 and leave the other two thirds empty.
32. **Follow the subject.** Over footage, place words in the empty half of the shot and move them when the shot changes.

## Motion — arrival and hold
**Everything here is keyframes.** Entrances, exits, loops and moves are one format: a pose (position, scale, rotation, opacity, letter-spacing) keyed over a normalized window with cubic-bezier easing, plus a range selector that hands the motion from one character to the next — the After Effects text-animator model, the one Lottie serializes. So a named preset and a hand-keyed track are the same object at different levels of precision. Key it directly by default — the track says what pose the element holds at what second, and lands the motion on the frame you mean. The names earn their place on per-letter and per-word motion, which a single pose track cannot express.

33. **Arrival and hold are two decisions.** `in_style` is how it appears; `move` is what it does for the rest of its life. A line with only an entrance freezes the moment it lands.
34. **The moves** — each is a slot beside the entrance and loop, applied for the element's whole hold and composing over whatever the keyframe track does:
- push: A slow zoom in across the whole hold — the workhorse for a line that has to feel urgent.
- pull: A slow zoom out, the frame opening up. Endings, reveals, the last line of a verse.
- settle: Lands oversized and leaning, eases to rest in the first third, then creeps. Hero lines.
- swing: Overshoots past its resting angle and swings back. Playful, hand-drawn.
- punch: Snaps big, snaps back, then creeps. A hit on the beat.
- float: Rises a little the whole time it is up. Dreamy, weightless.
- sink: Drifts down. Regret, endings, a line that gives up.
- driftleft: Slides steadily left across the hold — a parallax bed under other lines.
- driftright: Slides steadily right.
- sway: Leans one way, then the other, and back to level. Drunk, loose, swung.
- arc: Travels along a shallow curve rather than a straight line.
- tiltsettle: Arrives rotated a quarter turn out and unwinds to level.
- breathe: Grows and shrinks a few percent, twice. Living, patient.
- creep: A scale rise so slow you only notice it in the cut. Dread, tension.
- slam: Enormous for two frames, then hard down to rest. Impact.
- orbit: Circles its own resting point once. Playful chaos.
- spring: Overshoots the size and bounces once past it before resting.
- fall: Drops in from above resting position and stops dead. Weight.
- reveal: Starts offset up at zero opacity and eases down into place.
35. **Per-glyph entrances.** rise, drop, grow, flip, swivel, bounce, wave, converge, streak, tumble, scatter, slot, blur, glitch, flicker move a title's letters one at a time. They cost nothing extra and are the difference between a title and kinetic typography. slot rolls each letter up a reel like a scoreboard: counts, years, a name landing.
36. **Typewriter for a reveal.** Slow it to two thirds of the line's hold so the text finishes typing just before it leaves.
37. **Wipe for a band.** A wipe entrance on a line sitting in a shape band reads as a broadcast lower third.
38. **Loops, sparingly.** flicker on neon, float on dreamy, wiggle on comedy — one loop per passage, never on every line.
39. **Exit matters.** A run where every line simply cuts out feels cheap; a 0.2s fade or a converge out costs nothing. A dive out flies into the last letter until its color fills the frame, a transition into whatever comes next.
40. **Contrast the move to the entrance.** A violent entrance (slam, tumble) into a still hold; a soft entrance (fade) into a slow push. Both loud reads as noise.
41. **Match the move to the beat.** punch and slam on hits, push and creep under sustained notes, float and breathe under held vocals.
42. **Key it yourself.** set_overlay_keyframes takes whole poses in seconds from the element's start — a path across the frame, a hold-then-drift, a beat that lands on a specific hit in the music. It is the first reach for motion, because a key lands on the second you name: two or three carry almost everything, and a preset entrance still composes over them.

## Frame and color
43. **Cards as punctuation.** A full-frame color card behind each line, cycling — the color change IS the edit. lyric-card and pastel-pop do it; `cards: true` adds it to any look that has them.
44. **Invert on the hook.** One card in the cycle with the light/dark relationship flipped. The eye reads it as a cut.
45. **Band, not plate.** A shape rectangle at fill_opacity 0.2–0.5 behind a line on a lower row, wider than the text, beats a plate for anything editorial.
46. **Color as the section marker.** One accent per passage, changing at the chorus. Cheaper and clearer than changing everything.
47. **Two colors only.** A frame color and one accent, everywhere. Restraint reads as design; six colors read as defaults.

## Construction — beyond the presets
48. **Masked reveal.** set_mask a linear mask on a title and keyframe it: the line wipes on from one side, no entrance preset involved.
49. **Text behind the speaker.** A subject mask (inverted) on a title over footage sits the words behind the person in the shot. Nothing else in a text video looks as expensive.
50. **Text in the footage.** add_overlay_video a copy of the shot, mask it to the text's shape region, and the picture plays inside the word. The graphics skill's composite-builds section has the geometry.

**How to use this list.** Pick a look for the base design, one composition device, one rhythm device and one motion device, and hold them for the whole video. Then break the pattern exactly once, on the hook. That single break is what a viewer remembers.
