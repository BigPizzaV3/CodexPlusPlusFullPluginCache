---
name: "thumbnail"
description: "Click-worthy thumbnails the way the big channels build them: an information-gap concept from sixteen frameworks, a face locked to a reference, an eleven-block house prompt at 4K, one render per concept, surgical tweaks that change one thing, and text only on an explicit ask. Use when: a YouTube thumbnail, a video cover, a preview image, an Instagram cover, bold viral-style packaging for a video. Not for: the video itself, a product still with no packaging intent (product-photoshoot), a carousel or quote card (social-graphics), an ad with an offer (ad-creative), a poster for print, a logo."
---

# Thumbnail

Produce 1 to 3 finished thumbnails that read at 120 pixels wide. The concept comes first, the face is locked to a reference when there is one, the render is checked, and text appears only when the user asked for it, exactly as given.

## Rules that never bend

- A thumbnail is one idea and one information gap: the viewer must need the video to close it. If it needs a sentence to explain, it fails. It never promises what the video does not show.
- Faces come from the user's reference and stay that person; no reference means a generated adult, never a lookalike of a real one. A reference thumbnail the user shows is read by eye for its framework, palette and layout and never sent to the model.
- No text by default. Text only when the user gave the string, at most four words, rendered in a final pass on a text-rendering model, never over a face.
- Contrast beats detail: one bright subject, one dark ground, one accent colour, nothing small. Subjects fill 40 to 60 percent of the frame.
- One generate_image call per concept on google/nano-banana-pro at 4K; never a count parameter. Three concepts means three frameworks.

## Intake, only for the gaps

Parse the brief: the video's subject and its hook, who is in frame (attached or none), the exact text if any, the platform (YouTube 16:9, Shorts and Reels 9:16, Instagram cover 1:1 or 4:5), the brand palette. Ask in one message only for the hook when the brief has no angle, and for the face when a person is implied but none is given.

## Frameworks, one per concept, brainstorm five before choosing

Before and after; a social post or chat card recreated in the scene; a three-step progression; a real screenshot held or shown; a posed portrait with one emotion; a posed action mid-move; a day or count badge as a physical object; a graphical diagram made physical; a landscape with a tiny subject; a map or aerial with one marker; the object huge and lit like a product; repetition of one object many times; a size difference between two things; a news-clip framing; an amplified-reality exaggeration of something true; a versus split only on an explicit layout ask.

## Models

google/nano-banana-pro at 4K with the face passed in the reference image field (imageUrls) and a logo as a second reference when given; runwayml/gen4-image (referenceImages) when the face must hold across three concepts and drifts; surgical tweaks on bytedance/seedream-5-pro as an image-to-image pass on the render; the text pass on google/nano-banana-pro, black-forest-labs/flux-2-pro or reve/2.1.

## Phases

1. Concept. Write one line per thumbnail: framework, subject, emotion (shock, delight, doubt, disgust, fear, smug, curiosity, pride, exhaustion, anger, deadpan), colour pair, and where any text would sit. Show them; a nod or silence proceeds.
2. Render. One generate_image per concept with the house prompt in eleven ordered blocks, one clause each: the frame (poster grade, one unified frame, no split unless asked); the scene brief in one sentence; the text policy (no text, or the exact string and where); the subjects large, 40 to 60 percent of the frame, with an identity-lock sentence per referenced person ("the person in image 1, same face, hair and skin, no changes to the face"); the key elements (the object, the badge, the screen); logo preservation when a logo is attached ("image 2 is the logo, exact shape and colours"); the location in one line; the composition (one hero on a power third, eyes toward the viewer or the object); the background (a vivid field in the accent colour, a soft vignette, simplified); a named lighting rig on people (a key from the front-left, a soft fill, a rim and hair light in the accent colour); the grade (punchy contrast, saturated, crisp). Then the negatives: no text unless given, no watermark, no extra fingers, no duplicate person.
3. Check. Look at each render inline and describe it in one glance as a viewer would at 120 pixels: if the description needs a second clause, simplify the scene. Verify the identity, no stray text, truthfulness, no extra limbs. Surgical tweaks only, on bytedance/seedream-5-pro: "change ONLY the expression to X, keep everything else pixel-faithful"; allowed scopes are the expression, a background swap, a background recolour, a rim-light recolour. One refinement per concept. Alternate takes when asked: a low-angle hero, an extreme close-up punch-in, a wider tilt; emotions times takes never above sixteen.
4. Text, only when asked. One image-to-image pass on a text-rendering model: the exact string, bold sans, high contrast, placed where the concept reserved space, nothing else changes. Check the spelling inline; a wrong letter is a re-run of this pass only.
5. Delivery. The finals in order with the framework named per thumbnail, one line on which to run first and why, and an offer of a second text variant or an A/B pair.

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
