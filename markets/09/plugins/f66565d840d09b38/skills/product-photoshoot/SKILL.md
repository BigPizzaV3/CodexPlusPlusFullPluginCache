---
name: "product-photoshoot"
description: "Finished product photography in one of ten modes, from a product photo or a description, with one product identity across the set, variants that differ by instruction, the typography three-case rule, and a refinement pass only for defects actually seen. Use when: finished product stills; a packshot, catalog or shop images, lifestyle scenes, a closeup with hands, a Pinterest pin, a hero banner, a social carousel, a static ad set, a product worn or used by a model, a conceptual or CGI-style product image, a restyle of an existing product photo. Not for: a video (product-reel), marketplace listing sets (amazon-listing), a paid ad set with a headline and an offer (ad-creative), a text-led carousel (social-graphics), thumbnails and video covers (thumbnail), portraits of people, a creator on camera with the product (presenter-video)."
---

# Product photoshoot

Produce finished product stills. The product is the hero in every mode. Pick one mode, apply its rules, keep one product identity across the set, and refine only what you or the user can name from the pixels.

## Rules that never bend

- The product's shape, colours, label and proportions survive every image. A drift is a failure to fix, never to present.
- One product in frame unless the mode says otherwise; realistic scale next to hands and props; the reference's visible side, never rotated or mirrored.
- Text follows three cases and only these. The user gave an exact string: write it into the scene as integrated typography on a text-rendering model and check the spelling. The user will add text themselves later: ask for one tonally uniform area that belongs to the scene (sky, a blurred background, a smooth surface), never "empty space", which renders as a flat colour band. The user said nothing about text: say nothing about text either, beyond "no text, no logos, no watermark". Never invented label copy.
- Brand facts come from the user, never assumed.
- A set shares one light, one palette and one surface world; variants differ by an instruction (the preset, the light's direction, the camera angle, the palette), never by paraphrase.

## Intake, typed by what the user gave

Parse the brief and classify it, then ask at most one message, only for the real gaps. A photo and a vague ask: three packshot variants at 1:1, say so, ask nothing. A photo and a named use (a pin, a banner, a shop page): the mode is the use; ask only for the exact text when the use normally carries one. A description only: ask for the product's form, colours and label state when the description leaves them open; the first image becomes the reference for the rest. An existing image to restyle: the restyle mode; ask for the target look only when none was given. A model wearing or using it: the virtual-model mode; ask for the wearer's gender and vibe when unstated. A vague brand ask: three lifestyle variants in the brand's palette. Tie-breakers: platform beats environment (a pin over a lifestyle scene, a banner over a scene, a carousel over a single shot, a named genre over a mood). Counts: 1, 3 or 5. Never ask about models, lenses, lighting terms or resolution.

## Models

google/nano-banana-pro at 2K for every render, the product photo passed in the reference image field (imageUrls) and declared in the prompt; bytedance/seedream-5-pro for every refinement pass (image-to-image on the latest version, never the original); google/nano-banana-pro or black-forest-labs/flux-2-pro for a stage that must render an exact text string (openai/gpt-image-2 only at 1:1, 2:3 or 3:2, the only aspects it renders here); ideogram-ai/remove-background for a transparent cutout; recraft-ai/recraft-crisp-upscale for print sizes.

## Phases

1. Product intake. Look at the product photo inline (or read the description) and write a one-paragraph staging contract to reuse verbatim: object type and form, material and finish, colours, the label state (the exact printed text if legible, otherwise "blank" or "unreadable"), size next to a hand or a mug, how it opens or is used, the weight class (heavy needs two hands and visible strain, light one relaxed hand, tiny pinched near the lens), one honest imperfection that keeps renders from looking like CGI. Lock the angle.
2. First image. Generate index one of the set with the product photo as the reference (or from the description when there is none). Look at it inline against the contract: shape, label, colours, scale. When the product was described rather than photographed, this image becomes the reference for every other image in the set.
3. The set. Generate the remaining variants with the product reference passed on every call, each changing one named thing per the mode. Append the negatives: no extra product, no duplicate, no look-alike; no warped or invented label text; no stock-photo gloss, no HDR glow, no lens flare; no mixing of styles; no flat colour bands or empty grey zones; no waxy skin on hands; no watermark. Launch them together, then wait for each.
4. Refinement. Look at the set inline. Fix only a defect you can see: pick ONE weakest area per pass, name it, and run an image-to-image pass on bytedance/seedream-5-pro on the latest version with "change only X, keep everything else exactly" and a fix in photographic language (flat light: a key from camera left at 45 degrees and a rim on the far side; a warped label: crisp legible print; plastic skin: visible pores and micro-texture, no sheen; a flat band: extend the real environment into it). At most two refinements and three generations per image. Never name a defect you have not seen.
5. Delivery. The final image per index in order, one sentence naming the mode, the ratio and any correction applied, and one next step (a product video from the strongest still, an upscale for print, a cutout for the shop).

## Modes

- Packshot: seamless white or a soft gradient sweep, front three-quarter angle, soft key from the upper left with a gentle fill, true colours, a faint contact shadow, no props, catalog framing with margin on all sides; variants change the angle and the sweep's tone.
- Lifestyle: the product where it lives, in use or within reach, real daylight with a direction, one or two props that belong, the product sharp and the scene honest, the camera at eye level or slightly above; variants change the room and the hour.
- Closeup with hands: tight on the product held or used by one pair of hands, partial face at most, real skin texture, the product's front visible, the action clear (opening, pouring, applying), two hands at most with correct fingers, the grip matching the weight class.
- Pin: vertical 2:3, one product large, a calm palette drawn from the product, a single prop or surface; a tonally uniform area at the top or bottom only when the user will add their own text.
- Hero banner: 16:9 or wider, the product on one side; the headline integrated when the exact string was given, otherwise a uniform area on the other side only when the user will add one; light and palette from the brand.
- Carousel: 3 to 10 connected square slides that read left to right (the hero, the detail, the use, the context, the range); the same surface and light on every slide; a slide is one idea; slide copy, when given, rendered into each slide on a text-rendering model.
- Ad pack: 3 to 6 coordinated square and vertical variants, each a different hook (problem, mechanism, result, comparison, lifestyle), same product, same palette, exact text only where given.
- Virtual model: the product worn or used by a generated adult, plain and unbranded, the product the sharpest thing in frame, wardrobe and setting from the brief, a realism pass on the model (pore-level skin, no beauty-filter smoothing), no real person's likeness.
- Conceptual: surreal or CGI-style (floating, exploded, splash, sculptural, macro); the product's shape and label exact; one idea per image; a restrained palette so the concept reads at a glance.
- Restyle: the existing product image as the canvas; change the aesthetic (light, palette, surface, mood) and preserve the product, its position and the composition; describe only what changes and say everything else stays.

## Prompt shape

Open with the manifest ("image 1 is the product: same label, same visible side"). Then the subject and what it is doing; the setting; the light (source, direction, softness); the camera (distance, angle, lens feel); surface and material detail; the palette; the mood in two words. Concrete nouns beat adjectives. Then the text case, then the negatives.

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
