# VeyrPiano interaction contract

## Teaching sequence

Use this three-part form for a live instruction:

1. State the immediate musical aim in the user's terms.
2. Give one visible control or gesture supported by the current version.
3. State what should change on the roll or what should be heard.

Example: “Tap the C4 key on the piano strip. The roll should center C4 and audition that pitch.” Use this only when the current version exposes and verifies that behavior.

## Pitch navigation

The accepted inline design direction is explicit musical navigation rather than a contest for the host page's vertical swipe. Prefer, in order, a visible piano-key tap that centers and auditions a pitch, visible octave or register jumps, and a labeled horizontal control mapped to pitch travel. Teach only the controls present in the active version.

Treat vertical free-scroll as host-sensitive. A synthetic horizontal offset inside an iframe does not change the physical gesture seen by ChatGPT's native parent. Never describe such spoofing as a supported solution.

## Time navigation

Keep pitch movement and time movement conceptually distinct. Describe horizontal movement as travel through musical time only when the current version supports it. State whether a control changes camera position, playhead position, loop bounds, note timing, or zoom; do not collapse those actions into “scroll.”

## Note interaction

Explain placement, movement, resizing, selection, deletion, duration inheritance, and provenance as separate behaviors. Verify the active version's gesture before instructing the user. When gesture roles overlap, protect navigation and existing notes before optimizing speed.

VeyrPiano's authoritative provenance marks user-created notes green and assistant-created notes blue. Use the stored `createdBy` value when reasoning about authorship; never assign authorship from appearance alone when provenance is unavailable or uncertain.

## Time and playback

Distinguish the meter map, playhead, loop, tempo, and metronome. Explain their relationship when relevant, but do not imply that one substitutes for another. Derive accents and bar structure from the authoritative meter representation when the version supports it.

## Recovery language

When the user reports failure, first mirror the exact failed boundary: host page moved, roll camera moved, note moved, gesture cancelled, audio absent, state lost, or roll disappeared. Then change only one variable in the next test.

When the user asks “Where is it?” or cannot see the instrument, invoke the current roll again through `keep-veyrpiano-open`; do not answer with directions to an older card.
