---
name: "character-sheet"
description: "An invented character that stays themselves: a fixed-order identity prompt, one approved hero portrait, a split-screen and a slot sheet of views and expressions in one of five style presets, checked for consistency and kept as the anchor other recipes reuse. Use when: a character sheet, model sheet, reference sheet, turnaround, expression sheet, or one invented character held consistent across views, poses and expressions for later images or videos. Not for: a real person's headshots, a single portrait, a thumbnail (thumbnail), a product (product-photoshoot), a face built from someone's photos."
---

# Character sheet

Invent one character and hold them stable. The deliverable is a hero portrait (the identity reference later work attaches), a split-screen (a standing full body on the left, a tight close-up on the right) and, when asked, a slot sheet of views and expressions.

## Rules that never bend

- Original characters only. A real person is never the seed unless the user supplied their photo and has the right to use it; then this recipe only adds views.
- One character per sheet. A second character is a second sheet.
- The identity prompt is written once in fixed order and repeated verbatim in every prompt; iteration changes one clause and keeps the rest.
- Adults have mature facial structure with defined bone and a real age; never a rounded, youthful face on an adult.
- The slot layout is fixed and named in the prompt; the model may not merge or drop slots. No text, labels or slot numbers in the pixels; no watermark.
- The style preset is stated once and repeated verbatim.

## Intake, only for the gaps

Parse the brief: who the character is (age, build, hair, skin, distinguishing features, wardrobe), the world they belong to, the style preset, the use (stories, a mascot, a game, videos, a virtual presenter). Ask in one message only when the character is undefined beyond a name, or the style cannot be inferred from the use.

## Presets

- Photoreal unretouched: real skin with pores, natural light, a phone or camera feel, no beauty filter, faint sensor noise.
- Editorial: studio light with a direction, clean backdrop, a fashion restraint in colour.
- Anime or 2D: flat colour, a named line weight (thin or bold), a consistent eye style, cel shading.
- 3D stylised: soft global light, rounded forms, subsurface skin, a clay or toy finish named.
- Game concept: painterly, a costume with function, a silhouette that reads at small size, a muted world palette with one signature colour.

## Models

google/nano-banana-pro for photoreal and editorial presets; bytedance/seedream-5-pro for anime, 2D and painterly presets and for the realism pass; the split-screen and the sheet always on a model that takes the hero in its reference image field (imageUrls on the two above, referenceImages on runwayml/gen4-image, which is built for character consistency).

## Phases

1. Identity prompt. Write it in this order, one clause each: the composition clause (one identical original character on every view, a white seamless studio); the identity in a sentence (age, gender, ethnicity when given, build); the face (shape, nose, mouth, jaw, skin texture and tone); the eyes (colour, shape, no glare or reflections); the brows; the hair (cut, colour, finish); the realism module for photoreal presets (pores, fine hair, no retouching, a phone or camera feel); the body; the wardrobe head to toe with materials and colours; the light (soft, even, a direction); the quality tail (sharp, natural colour); the negative tail (no text, no extra limbs, no second person, no glare in the eyes, no beauty filter). Then the preset lines verbatim.
2. Hero portrait. generate_image one three-quarter portrait at 3:4 as a draft; for photoreal presets, a realism pass (an image-to-image pass on bytedance/seedream-5-pro that keeps the framing and face and adds pore-level skin and real material detail, no beauty-filter smoothing). Look at it inline; show it and get a nod. It becomes the reference for everything after.
3. Split-screen. With the hero passed as the reference and declared ("image 1 is the character: same face, hair, skin and wardrobe"): one 16:9 image, a standing full-body view on the left panel and a tight face close-up on the right, same wardrobe, same light, thin gutter, no text.
4. Slot sheet, when asked. With the hero passed as the reference, generate one wide image laid out as a grid of named slots: front, three-quarter, profile, back; then four expressions (neutral, joy, doubt, anger); then two full-body poses. Same wardrobe, same light, plain background, thin gutters, no text. Name every slot in the prompt in reading order.
5. Check. Look at each image inline: the same face in every slot, the same wardrobe, no merged slots, no extra limbs. One refinement pass on a named defect as an image-to-image pass on bytedance/seedream-5-pro with "change only X".
6. Delivery. The hero, the split-screen and the sheet, the identity prompt in prose so the user can reuse it, and the hero's asset key stated once so later requests can attach the same face. Suggest the user keep the key and the prompt in their notes; nothing here is remembered for them yet.

## Pixara tool mechanics

- Discover: recommend_model for a goal, list_models for a service or a capability, describe_model for the exact parameters, the constraints and the price. The models named in this recipe are the ones verified for it; if one has left the catalog, take the newest model with the same tags.
- Run: generate_image, generate_video, generate_voiceover, generate_music and the editing tools return a job id. wait_for_job(id) polls for up to 45 seconds; call it again until the job finishes. A failed job is refunded and its error names the constraint that was hit; fix that and retry once.
- Waves: when several generations do not depend on each other (a shot list, a set of variants, the takes of a voiceover), queue them in one generate_batch call and wait for all of them with wait_for_jobs; one failing job never stops the others.
- Results: every finished asset carries a URL and a key. Pass the URL as the input to the next generation (describe_model names the image, video and audio fields). Pass the KEY to assemble_video, and call get_media_metadata(key) for exact durations before sizing clips.
- Inputs from the user: request_upload then finalize_upload (or upload_widget) for a local file, upload_asset for a URL, list_generations to reuse earlier work.
- Money: prices are per model in list_models; estimate_cost before anything expensive; confirm before choosing a model that costs several times more than an alternative.
- Seeing: images render inline, so look at every image before building on it. You cannot watch video here: when a clip finishes, tell the user what to check (face, hands, lips, unwanted text) and let them confirm before assembly, unless they asked for no check-ins.
- Words on screen are minimal and live inside the picture: a title, a step name or a price is a designed frame from a text-rendering image model (google/nano-banana-pro at any aspect; openai/gpt-image-2 only at 1:1, 2:3 or 3:2, the only aspects it renders here) with the exact string, animated with image-to-video or placed as an image clip; the assembler's text clip is the last resort for a plain line nothing else can carry. Never ask a generation model to render text you did not receive verbatim from the user.
- Captions never come from the assembler or a video prompt: when a piece has speech and the user wants captions, run the finished master through the subtitles tool on zapcap/subtitles with the language, a style as preset when the user wants a particular look (list_caption_styles shows them with previews; the default is clean plain text), position only when the style's own placement does not fit (a percentage of the height from 0 at the top to 80 at the bottom, around 70 for a 9:16 talking piece), and the authored script as referenceTranscript when one exists: one entry per cue with text, startTime and endTime in seconds, which keeps the script's spelling while word timing still comes from the audio. veed/subtitles is the fallback only: when ZapCap refuses the video (no audio track, longer than 30 minutes), when its job fails (one retry on VEED, never a second ZapCap run), when the captions are authored text on a piece with no speech (VEED burns them from srtContent), or when the user picked a VEED style. Never caption one piece with both. The clean master stays the master; the captioned file is the deliverable.
- minimax/hailuo-3-max: resolution is the string "768P" exactly, capitals, its only value (never 480P, and a lowercase 768p is rejected); duration 5 to 15; referenceImageUrls holds at most nine.
- Voices: eleven-labs/v4 for every voiceover (a voiceId from list_voices); minimax/speech-2.8 only when it fails; bytedance/seed-audio-1.0 for voice replication from a sample the user owns, a two-voice dialogue in one take, or spoken lines with sound effects.
- Talk to the user in model display names, never ids, and never narrate these mechanics.
