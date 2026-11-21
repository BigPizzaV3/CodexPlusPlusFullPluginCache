# Visual Treatment and composite preflight

## Purpose

Separate low-fidelity comprehension approval from final-picture direction. After the Animatic communicates the approved Hook and Body, define how the decisive objects will look, move, and carry meaning before freezing the production handoff.

## Treatment contract

Create `visual-treatment-contract.json` with one to three candidates. Use still final-look frames for normal Taste selection. Require a moving binding proof only when at least one risk is present:

- a new visual grammar;
- a primary exact semantic surface bound to the moving world;
- high world-binding risk.

Do not force moving proof for a known, static, screen-native End Card solely because its exact text is a primary semantic surface.

Do not require three finished moving Treatments for every job.

For each semantic carrier object, declare:

- what the viewer must understand from it;
- whether meaning is carried by motion, exact surface, character, environment, editing, or a mix;
- whether exact surface load is none, supporting, or primary;
- whether the object is screen-native or bound to the generated world;
- one content authority, one geometry owner, one motion owner, and one binding mode;
- the exactness/readability windows;
- a fallback that preserves the viewer job.

One semantic object must have one geometry owner. Do not generate one card and independently animate a second foreground card that is supposed to be the same object.

## Planning versus production

Planning owns the viewer meaning, treatment candidates, semantic objects, risk profile, and selected final look. Production owns the zero-cost or local feasibility proof and whether the chosen binding route can be executed.

After one Treatment is approved, invoke `$performance-video-production` in `PREPRODUCTION_FEASIBILITY`. It may create local styleframes, 2.5D/3D mockups, tracking tests, or a short composite proof. It may not call a paid provider, rewrite Creative, or promote the proof to final media.

Only a ready `compositing-feasibility-gate.json` may be hashed into production handoff v4.
