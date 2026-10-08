# How Phase 6 Works: Storyboard Layout, Visual Staging & The Inheritance Rule

Phase 6 takes the locked Two-Column AV Shooting Script (from Phase 3) and visually stages each shot onto a multi-panel storyboard grid.

---

## 1. The Inheritance Rule: No Duplicate Decisions

> [!IMPORTANT]
> **Inheritance from Phase 3**:
> - Phase 6 **DOES NOT re-decide Shot Size or Camera Angle**. Those are locked upstream in [Phase 3 Shooting Script](../phase-03-shooting-script/HOW-PHASE-3-WORKS.md).
> - Phase 6 **INHERITS** the assigned shot size (`size.ews`, `size.mcu`, etc.) and camera elevation (`angle.low`, `angle.high`) directly from the Phase 3 table.
> - **What Phase 6 Owns Exclusively**:
>   1. **Visual Composition**: How elements are balanced inside that inherited frame ([composition.md](./composition.md) - 69 cards).
>   2. **Actor Staging & Eyelines**: The 180° axis, subject vectors, and physical staging ([blocking-staging.md](./blocking-staging.md) - 64 cards).
>   3. **Panel Architecture**: 3x3 contact sheets and aspect framing ([storyboard-panel-architecture.md](./storyboard-panel-architecture.md)).
>   4. **Animatic Timing**: Synchronizing frame duration to audio beats ([animatic-beat-timing-grid.md](./animatic-beat-timing-grid.md)).

---

## 2. Upstream & Downstream Production Flow

```
Phase 3: Shooting Script
   │ (Locks Shot Size, Angle & AV Duration)
   ▼
Phase 6: Storyboard Layout (Inherits Shot Size & Angle)
   │ ├── Applies Composition & Rule of Thirds (composition.md)
   │ ├── Sets Actor Blocking & 180° Action Line (blocking-staging.md)
   │ └── Assembles Multi-Panel Storyboard Deck (storyboard-deck-template.md)
   ▼
Phase 7: Image Prompt Engineering
   │ (Slot 3 Transcribes Inherited Size + Angle + Adds Optical Lens)
```

---

## 3. Reference Cross-Links
- **Inherited Camera Sizes**: [Phase 3 Shot Sizes](../phase-03-shooting-script/shot-sizes.md)
- **Inherited Camera Angles**: [Phase 3 Camera Angles](../phase-03-shooting-script/angle-height.md)
- **Inherited Named Framing**: [Phase 3 Named Framing](../phase-03-shooting-script/framing-named-shots.md)
- **Downstream Keyframe Prompts**: [Phase 7 Image Prompt Engineering](../phase-07-image-prompt-engineering/PHASE.md)
- **Full Phase 6 Cards**: [INDEX.md](./INDEX.md) & [LOOKUP.md](./LOOKUP.md) (194 cards)

## The render mode travels through this phase

Every panel carries the render mode it is in, from this set:

<!-- GENERATED:render-modes — do not edit by hand. Generated in the source package -->

**The render modes.** Every value this field takes, and what each one means. Generated from the table in [`ENGINE-CHECK.md`](../ENGINE-CHECK.md), which is the authority — widen a definition there and it widens everywhere, which is the failure this block replaces.

| Value | What it means |
| :--- | :--- |
| `photoreal` | Made to read as photographed. Real optical values: focal length, aperture, depth of field, Kelvin, and a film stock or sensor look where one is wanted. |
| `rendered_cg` | 3D / rendered CG: rendered geometry with a virtual camera, so the optical values apply — but no film gate, so grain is an added effect rather than a property. State the **surface** as well as the optics: what the thing is made of. |
| `flat_2d` | Flat 2D / cel: drawn or painted: cel, ink, watercolour, gouache, a painterly animated look. No lens, no aperture, no Kelvin, no stock. The art style, line weight, ink and colour treatment replace them, and the light direction and palette temperature are stated in words. |
| `stop_motion` | Stop motion / physically made: photographed objects moved frame by frame. Real optics, handmade surface, and a motion signature of its own — uneven cadence, held extremes, no true motion blur. |
| `built` | **Assembled in a graphics or motion layer rather than generated at all** — a chart, map, counter or diagram built from real values; an animated diagram; **a typographic or kinetic-text sequence**; a title card. It reaches no image or video engine, carries no optical values and no art style, and a prompt written for it returns plausible nonsense. Where a shot is `built`, the engine record reads `engine: none - built`. |
| `multi_look` | Two or more looks: the piece deliberately alternates. Declare each constituent look by its machine value, say what the cut between them means, and tag every row and every prompt with the one it is in. |

<!-- /GENERATED:render-modes --> **Phase 3 records it in the Mode & Look cell, this phase carries it on the panel, and Phase 7 and Phase 8 each read it to decide which vocabulary every optical, surface and motion field is filled with.**

On a single-look piece it is one value stated once on the deck. **On a piece that alternates two looks it is per panel**, declared at the top of the deck as a `LOOKS:` line and tagged on each row — a reconstruction documentary cutting between photographed footage and drawn rebuilds is the standard case, and so is a film cutting between two photoreal registers such as interview and reconstruction. **Where both looks share one machine value** — captured museum photographs and generated reconstructions, both `photoreal` — the `LOOKS:` line names each by that value plus its register in words (`A = photoreal, captured · B = photoreal, generated`), and every row is tagged `A` or `B` the same way.

This guide did not mention the render mode at all while Phases 1, 3, 7 and 8 each carried it, which left the one phase between the shot table and the prompt as the place it could be dropped. The handoff list in [`handoff-to-stills.md`](handoff-to-stills.md) names it as a required item.

**On a song that names or teaches something on a beat, the thing is in frame on that beat.** An arrival move — a train pulling in, a door opening, a character popping up — finishes before the downbeat, so the item is already alone in frame when the word is sung. The Teaching Song kit in [`../phase-05-song-generation/formats-music.md`](../phase-05-song-generation/formats-music.md) names the picture arriving a beat behind the word as that format's failure; check every arrival panel against the timing map's downbeats.
