# Render prompt

Use this only when the user asks to see the restyled room and an image generation or editing tool is available. Edit the user's own photo; do not generate a different room.

## Build the prompt

Fill the brackets from the plan and the style sheet. Keep the structural block word for word. Order matters: image models weigh the end of a prompt most, so the room's purpose goes last.

```
Restyle this room photo in the [STYLE NAME] style. Same room, same camera position, same framing.

STYLE:
- Palette: [base colours] with [accent colours]. [balance sentence from the sheet]
- Materials: [four to six materials from the sheet]
- Furniture: [the pieces from "Bring in", with material and colour]
- Lighting: [the lighting from the sheet]
- Composition: [one sentence from the sheet]
- One distinctive piece: [the single characterful object from the plan]
- Avoid: [the sheet's Avoid list]

SCOPE: [low = restyle with small additions and keep the large furniture; mid = replace the key pieces and keep what fits; high = clear the room and replace everything movable]

STRUCTURE — do not change:
- Keep every wall, window, door, opening and ceiling line exactly where and as it is. If the two images were overlaid, they should align.
- Do not add architectural elements that are not in the photo: no beams, columns, arches, vaults, skylights, crown moulding, wainscoting, niches, built-in shelving or fireplaces. A flat plain ceiling stays flat and plain.
- Do not remove, cover or wall over any window, glass wall or glazed door. Curtains may be added, with the glass still visible.
- The floor keeps its material and colour; a rug may lie on it with the floor visible at the edges.
- A pendant or chandelier hangs only from the existing ceiling light point. Other lights are lamps or plug-in sconces.
- Switches, sockets and radiators stay where they are.
- Change only furniture, soft furnishings, rugs, curtains, decorative objects, lamps and art[, and wall paint colour].

This room is a [PURPOSE]: [its anchor from room-purpose.md]. The style above is a look to apply, not a furniture list to place. The result must read unmistakably as a [PURPOSE].

Photorealistic interior photograph, light consistent with the original photo.
```

Include "and wall paint colour" only if the plan repaints the walls.

### With inspiration images

If the user supplied reference images, send the room first and say so in the prompt:

```
IMAGE 1 is the room to restyle. It is the only room to change.
The other images are references for colour, material, furniture style and atmosphere only. Do not copy their layout or architecture. Keep image 1's dimensions and aspect ratio.
```

### Seeing the room empty first

For a high-budget plan, or when the existing furniture confuses the result, offer an empty-room pass first: remove all furniture, rugs, curtains, decor, freestanding lamps and clutter; keep walls, floor, ceiling, windows, doors, built-ins, radiators, trim and fixed lights exactly; same camera angle and light; add nothing. Then restyle the empty version.

## Check the result

Compare the render with the original before presenting it. Score five things from 1 to 10:

1. **Layout** — walls, doors, windows and openings in their original positions; room shape preserved.
2. **Perspective** — same camera angle and vanishing point.
3. **Proportion** — room dimensions, ceiling height and the size of objects relative to the room.
4. **Structural fidelity** — nothing architectural added or removed.
5. **Realism** — looks like a photograph; no warped geometry, floating objects or impossible physics.

What counts against structural fidelity:

- A window or glass wall added to a blank wall, or one removed or turned into solid wall: critical, 1 to 2.
- Invented beams, columns, arches, vaults, skylights, mouldings, wainscoting, niches, built-in shelving, fireplaces or new doors: critical.
- Ceiling changes such as cornices, coves, dropped sections, recessed spots or light strips: 3 to 5.
- The floor resurfaced or recoloured wall to wall: 3 to 5.
- Switches, intercoms, fuse boxes or radiators erased or built over: 4 to 6.

What is fine and never a fault: a new pendant or shade on the original ceiling point, plug-in lamps and sconces, freestanding furniture of any height, curtains, paint, removable wallcovering, a rug of any size with the floor visible at its edges, furniture standing in front of a socket.

Weigh layout and structural fidelity most. A beautiful image that invents a window is unusable for someone who has to live in the real room.

- 8 to 10: show it.
- 6 to 7: show it and name the minor fault.
- Below 6: tell the user what went wrong and retry once. Repeat the full prompt and append one line that names the exact fault and nothing else: "What went wrong last time, fix exactly this and keep everything else: the left window was removed." If the retry also fails, say so and fall back to the written plan.

A render illustrates the plan. It is not a specification; say so if the user treats it as one.
