# Still-image design record



What is decided about a frame, as opposed to a shot. This is the record behind every keyframe, reference sheet, poster and thumbnail, and it is filled before an image prompt is written.



It is separate from shot planning on purpose. A still has no movement and no duration, and the questions that matter to it, which references contribute and which must not, what may vary and what may never drift, where the safe areas are, are questions a shot card has no room for.



### The Still-Image Design Record

**Also called:** the one-still route, frame record, the poster and cover path  
**What it is:** The record filled instead of a shot table when the deliverable **is** an image — a poster, key art, a thumbnail, a podcast or album cover, a packshot, an exhibition panel, a reference sheet — rather than a frame feeding a sequence. On this route Slot 3 of the image prompt is authored here, not inherited from Phases 3 and 6, because there is no shot upstream to inherit from.  
**Effect on the audience:** Nothing directly; it is what stops the one thing they will see being designed by default. A cover built from a frame-grab mentality is composed for a moment in a story rather than for a tile in a feed, and it fails at thumbnail size.  
**Used for and where it works best:** Any single-image deliverable, and the only route available to a piece with no picture that still owes one still — an audio episode's cover art is the standard case. Fill the record before the prompt, and take the generation tile from `ENGINE-CHECK.md` rather than cropping a wide frame square.  
**Best in:** formats: Poster / Static Design, Thumbnail / Social Card, Product Still / Packshot, Museum Installation, Podcast, Editorial / Magazine Image | genres: all  
**Avoid when:** The image is a keyframe that a video prompt will animate. That is the shot-fed path, and Slot 3 inherits — see the Inheritance Law in HOW-PHASE-7.  
**Prompt:** `not a prompt line but a record: fill the design record below before writing the still's prompt`  
**Yields to:** The shot-fed keyframe route: the Phase 3 shot table plus the Inheritance Law in HOW-PHASE-7-WORKS section 3 (an authority written in words, not a card id; kf.* is its craft shelf) — The image is a keyframe a video prompt will animate.  
`still.design_record`

---

## 1. Master Still-Image Design Record Specifications

Copy and fill this block. `required` means the key must remain present even when its value is `null`;
conditional keys state the value that activates them. These are separate axes: a podcast cover can be
a `finished_still` deliverable, use `references_to_image`, have no motion conditioning, keep text in a
built layer, approve only the layout, and derive from an earlier candidate without confusing any two
of those decisions.

```yaml
still_image_design_record:
  still_id: null                         # required, stable id
  deliverable_type: null                 # required: poster / key_art / thumbnail / packshot / cover / exhibition_panel / reference_sheet / editorial_still / project_native
  purpose: null                          # required
  audience_function: null                # required
  image_conditioning_mode: null          # required: text_only / references_to_image / image_edit / composite
  motion_conditioning: none              # required: none / start_frame / end_frame / start_end_pair
  text_owner: built                      # required: built / none; exact text never belongs to the image generator
  approval_scope: null                   # required: concept / composition / identity / text_layout / final_delivery, or an explicit list
  lineage:                               # required
    status: null                         # source_direct / source_adapted / source_combined / derived / invented / transformational
    parent_ids: []
    successor_of: null
    repair_scope: null
  references: []                         # required; each row has id, contributes, must_not_contribute, source
  invariants: []                         # required
  permitted_variation: []                # required
  forbidden_drift: []                    # required
  aspect_and_crop:
    aspect: null                         # required
    crop_behavior: null                  # required
    safe_areas: []
    protected_content: []
  design:
    composition: null                    # required
    light_behavior: null                 # required
    perspective: null                    # required
    materials_contact_occlusion: null    # required
    attention_order: null                # required
  exact_text: []                         # required when text_owner=built; each row has string, language, source, placement, finishing_owner
  motion_reserve: null                   # required when motion_conditioning is not none; mover, path, clear_space, non_final_state
  start_end_delta: null                  # required when motion_conditioning=start_end_pair; exactly_one_difference, held_invariants
  candidates: []                         # required; id, decision, rationale
```

Filled shape example:

```yaml
still_image_design_record:
  still_id: podcast-cover-01
  deliverable_type: cover
  purpose: episode cover art
  audience_function: remain legible at feed-thumbnail size
  image_conditioning_mode: references_to_image
  motion_conditioning: none
  text_owner: built
  approval_scope: [composition, identity, text_layout, final_delivery]
  lineage: {status: derived, parent_ids: [portrait-approved-03], successor_of: cover-draft-02, repair_scope: title hierarchy only}
  references:
    - {id: portrait-approved-03, contributes: identity only, must_not_contribute: background and wardrobe, source: project portrait shoot}
  invariants: [approved face, black wool coat]
  permitted_variation: [background texture]
  forbidden_drift: [age, eye colour, face geometry]
  aspect_and_crop: {aspect: '1:1', crop_behavior: centre-safe for circular preview, safe_areas: [title top third], protected_content: [eyes, mouth]}
  design: {composition: centred half-length portrait, light_behavior: soft left key, perspective: eye level, materials_contact_occlusion: coat collar contacts neck and does not cover jaw, attention_order: face then title}
  exact_text:
    - {string: 'EPISODE TITLE', language: en, source: approved brief, placement: top third, finishing_owner: layout}
  motion_reserve: null
  start_end_delta: null
  candidates: [{id: cover-draft-03, decision: selected, rationale: face and title survive 160 px preview}]
```
