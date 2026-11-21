---
name: restyle-room
description: Turn a room photo or description into a concrete restyling plan in a named interior style. Use when the user wants to redesign, restyle, redecorate, refresh or make over a room, asks how their room would look in a style (Scandinavian, Quiet Luxury, Amalfi Coast, mid-century and so on), wants several versions or directions for one room, or shares a room photo and asks what to do with it.
---

Produce a restyling plan the user could act on this weekend: what stays, what goes, what comes in, where it sits, and how it is lit. The plan is specific to their room, not a description of the style in general.

The user's explicit instructions always win over the defaults in this skill. If they say they own the home and want to retile, plan for that. If they say "no plants", there are no plants.

## 1. Read the room

Work from the photo if there is one, otherwise from the description. Establish:

- **The shell**: walls, floor, ceiling, windows, doors, built-ins, radiators, fixed lighting, sockets. Treat it as fixed.
- **The movable layer**: furniture, rugs, curtains, lamps, art, plants, objects.
- **Size and light**: small, average or large; where daylight comes from.
- **Purpose**: what the room is for. If it is ambiguous, ask; everything else hangs on it.

Name what you see ("the grey three-seater under the window", "the pine wardrobe on the left wall"). If a photo shows fewer than three walls, say what you cannot see and plan only for what is visible. `references/photo-tips.md` has the advice to give when a better photo would help.

Never guess measurements from a photo. Ask for the room's dimensions when a recommendation depends on them (sofa length, rug size, walkways).

## 2. Settle the three choices

Ask only for what is missing, in one short message. If the user gave enough to start, start.

- **Style.** Use a look from `references/styles-index.md`. If the user names a style that is not in the library, pick the closest look, say which one and why, and carry on. If they have only a theme or no idea at all, give contrasting directions as described in `references/variations.md`, or suggest the find-your-style workflow. If they bring inspiration images instead of a style name, use the decode-a-look workflow first.
- **Budget level.** Low, mid or high, as defined in `references/budget-levels.md`. Default to mid.
- **Renter or owner.** Default to renter rules: nothing structural, nothing that needs a landlord.

## 3. Load the style sheet

Read the full sheet for the chosen look at `references/styles/<slug>.md` before writing the plan. Do not write the plan from the index line alone.

Each sheet has two layers. The first (essence, palette, materials, shapes, light, composition, signature moves, avoid) holds for any room and any tenant. The second, "The full-build version", lists concrete pieces and staging rules; use it to choose actual furniture and objects, and pass anything fixed to the building through the sheet's renter swaps.

## 4. Fit the look to the room's purpose

A style is a look, not a furniture list. Most sheets are written through a living room. Read `references/room-purpose.md`, fix the room's anchor piece (the bed, the desk, the dining table), and translate any piece that belongs in another kind of room into its equivalent here. A bedroom plan that reads like a lounge is wrong.

## 5. Write the plan

Use this structure. Keep it tight; a plan nobody finishes reading helps nobody.

1. **The idea** — two sentences: what this room becomes and the one move that does most of the work.
2. **Keep** — existing pieces that already fit the look, and anything the user said must stay.
3. **Remove or relocate** — what fights the look.
4. **Bring in** — new pieces in order of visual impact. For each: what it is, material and colour, rough size class, where it goes. Scale to the budget level.
5. **Palette** — three to five colours from the style sheet, with hex values where the sheet gives them, and where each one lands (walls, large upholstery, accent).
6. **Layout** — where the main pieces sit and why. Apply `references/scale-rules.md` for small and large rooms.
7. **Lighting** — the lamps and bulb warmth the style sheet calls for, with positions.
8. **Renter notes** — for every built-in or structural feature the look normally asks for, the freestanding or removable equivalent from the sheet's "Renter-friendly swaps" section or from `references/renter-swaps.md`. Skip this section for owners who asked for construction.
9. **Do first** — the three steps to take this week, cheapest first.

### Standing defaults

Apply these to every plan unless the user or the style sheet says otherwise. They are ordinary interior practice.

- **One living element**: a single plant, branch or vase of flowers. Never a jungle.
- **One warm metal** somewhere in view: brass, bronze or copper on a lamp, a frame or a table base.
- **Generous negative space**: leave floor and wall empty on purpose.
- **One distinctive piece**: a single object with character (an odd vintage lamp, a sculptural chair, one strange vase) so the room looks designed for someone, not assembled from a catalogue. One, not three.

Where a sheet contradicts a default (a look that forbids plants, or allows no accent), the sheet wins. Where the user contradicts either, the user wins.

### Rules for the plan

- Keep every permanent feature exactly as it is unless the user asked to change it. Do not invent beams, arches, fireplaces, mouldings, skylights or built-in shelving, and do not remove or move windows or doors.
- Respect the sheet's limits where it gives numbers (how many accent colours, how many statement pieces, how many objects per surface). They are what keeps the look from turning to mush.
- Recommend types of pieces, not brands or shops. Do not state prices as facts. If the user wants costs, give ranges and label them estimates.
- Do not present a guess about the room as an observation.

## 6. Optional: show it

If the user asks to see the result and an image generation or editing tool is available, build the prompt from `references/render-prompt.md`, using their photo as the base image, and check the result as that file describes before presenting it. Tell the user plainly if the image changed the room's structure (a window gone, a wall moved), then retry once.

If no image tool is available, say so and offer the plan as a written brief instead.

## 7. Follow up

Offer one next step that fits: sibling versions of this look (`references/variations.md`), a completely different look for the same room, a phased shopping plan, or the same look at another budget level.

## When not to use this skill

- Structural, electrical, plumbing or building-code questions: say this is styling advice and recommend a qualified professional.
- Exteriors, gardens and floor plans drawn from scratch: outside what this workflow covers. Say so and help generally if you can.
