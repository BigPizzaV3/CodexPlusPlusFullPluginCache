---
name: scene-continuity
description: Make consecutive scenes read as one continuous take — same room, same light, same time of day, matching camera — by generating later scenes from earlier stills, and make clips flow into one another by deriving the next still from the previous one and animating with an end frame. Use for shot/reverse-shot, a sequence in one location, before/after pairs, a continuous action across scenes, or when the user says the scenes do not feel connected.
---

# Scene continuity

## The mechanism

- `reference_image_urls` on a `generate_image` item conditions that picture on pictures Screel already stores: a finished scene still, a bank picture, an earlier result. The urls come from `get_project` (each scene's `image_url`) or from `get_document`.
- A batch item may carry its own `reference_image_urls`; it replaces the top-level list for that item. So one call can say: scene 2 continues scene 1's still, scene 4 continues scene 3's.
- The url pictures come first in the numbered inputs, then the reference documents' pictures. Keep the character documents on the item as well: a still alone carries the room but loses the face on a close-up.
- The limit is 14 pictures per generation, url pictures and document pictures together.

## Waves, because a still has to exist first

1. Wave one: batch every scene that depends on nothing — the establishing shots, the first scene of each location — with `generate_image` `images[]`, each item with its `reference_document_ids`.
2. Call `get_job_status` once when the batch is done, then `get_project` to read the finished `image_url` of each still.
3. Wave two: batch the scenes that continue those stills, each item naming its anchor still in `reference_image_urls` plus its character documents. Chains longer than two waves are rarely worth it; the third generation from a generation drifts. Anchor every later scene to the wave-one still of that location, not to the previous scene.
4. Do not wait on a wave with repeated status calls; the progress card updates on its own. One `get_job_status` between waves is enough.

## Prompting a continuation

- Say what stays and what changes: "Same kitchen and morning light as the reference, camera now on the other side of the table, Rin sits down". The model keeps what you name as unchanged and moves what you describe.
- Name the camera move in film terms: reverse shot, push in, wider, low angle, over-the-shoulder. Keep the lens feel consistent within a sequence ("same wide lens").
- Fix time of day and weather in every prompt of the sequence. A still anchors the room; it does not stop the model from turning noon into dusk if the prompt is silent.
- One deliberate change per scene. A scene that changes camera, time and action at once stops reading as a continuation.

## Common sequences

- Shot / reverse shot: generate the two-person wide first; both close-ups continue it, each with its own character document first in `reference_document_ids` and the wide still in `reference_image_urls`.
- One location, many beats: one wide establishing still; every later beat anchors to it.
- Before / after: generate "before"; "after" continues it with only the change described.
- A journey: no continuity across locations. Continuity is per location; the character documents carry the subject across.

## Flowing shots: derive, then animate to the next still

A clip starts on its own still. With `end_frame` it also ENDS on a chosen still, so when scene N+1's still is a later moment of scene N's shot, scene N's clip plays from one to the other and scene N+1 picks up exactly where it landed. Use this for one continuous action across scenes: a walk to the door, a reveal, a turn of the head, a vehicle crossing the frame.

1. Generate scene N as usual (wave one).
2. Derive scene N+1 FROM scene N's still: a `generate_image` item for scene N+1 with scene N's `image_url` in `reference_image_urls` and a prompt that says what stays and what moved: "the same shot and camera as the reference, five seconds later: she has reached the door and her hand is on the handle". One deliberate change; keep the camera and the light. Keep the character documents on the item.
3. Read both stills. If N+1 broke the framing, `refine_image` it ("match the camera and light of the reference") with scene N's still in `reference_image_urls`.
4. `animate_scene` scene N with `end_frame` "next" and a motion prompt that describes the move between the two pictures ("she walks to the door and reaches for the handle"). The clip's duration is the time that move takes; 3-5 seconds suits one action. Several scenes go in one call: each item carries `end_frame` "next", or the top-level `end_frame` "next" covers every item, and the last scene of a chain takes none.
5. Scene N+1 animates on its own afterwards, or renders as a still; either way it starts on the picture the previous clip landed on.

- A chain drifts like any derivation: after three or four derived stills, anchor the next one to the establishing still again and start a new chain.
- The end frame must exist before the animate call, so a chain is always two waves: every still first, the clips second.
- `end_frame` also takes a scene id or a Screel image url for a jump that is not the next scene; 'next' on the last scene is an error.
- Do not use an end frame between scenes that cut to a different place or angle; the model would morph one into the other. A cut is a cut: animate each scene alone.

## Edits keep continuity too

- `refine_image` on a scene still with `reference_image_urls` of the neighbouring still and the same `reference_document_ids` pulls a scene back into line ("match the light and colour of the reference").
- A scene whose still is animated later keeps its still as the clip's first frame, so continuity of stills is continuity of the video.

## When not to bother

- Stand-alone scenes, montages and location changes gain nothing from anchors and lose time to the extra wave. Use documents alone and batch everything at once.
- If credits are short, skip wave two: matching prompts (same location words, same time of day, same lens) get most of the way.