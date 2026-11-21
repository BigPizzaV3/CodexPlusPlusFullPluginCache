---
name: "amazon-listing"
description: "A marketplace image set from one product photo: a compliant main image on pure white, a seven-slot secondary sequence and optional A+ modules, one message per image, mobile-legible text from the user’s claims only, the approved main image reused as the anchor for every other one. Use when: marketplace listing images; an Amazon, Etsy, Shopify or eBay image set, a main image on white, infographic or feature images, an A+ content set, \"listing photos\" for a product page. Not for: general product photography with no marketplace (product-photoshoot), a paid ad with a headline (ad-creative), a video (product-reel), a thumbnail (thumbnail)."
---

# Amazon listing

Produce a compliant listing image set. One product, one message per image, text only from the user's claims, the approved main image as the anchor for every secondary.

## Rules that never bend

- The main image: a pure white background, the product alone and filling about 85 percent of the frame, the reference's visible side, no props, no text, no logos, no hands, square, at least 1600 pixels.
- Secondaries carry exactly one message each; text is short, at least a 24 point equivalent, with strong contrast, rendered on a text-rendering model (openai/gpt-image-2 or google/nano-banana-pro) from the user's claims verbatim. No claim, number or comparison the user did not write; competitor names never appear.
- The approved main image is passed in the reference image field on every secondary as the product; the label, colours and proportions never drift.
- Nothing invented about what is in the box; the contents come from the brief.
- Spelling is read back on every image that carries text; a misspelling is re-rendered, never accepted.

## Intake, only for the gaps

Parse the brief first, then ask in one message only for what it left out: the product photo (required; upload a local one; a description alone gets a packshot first through the product-photoshoot recipe, and that packshot becomes the reference), the scope (main only; main plus secondaries; main plus A+ modules; the full set), the claims allowlist, the box contents, the brand palette. Ask for a missing scope, and for a missing claims list when secondaries are wanted. Never ask about models.

## The sequence

Secondaries in order, each square: a hero in context; features and scale (a dimension callout or a hand for scale); in use; an infographic of three benefits from the claims; a comparison of visible attributes only; a lifestyle scene; a trust image (the box contents laid out, a material close-up).

A+ modules, when in scope, at 3:1 wide: a banner with the product and one line; pain points as three panels; features with callouts; ingredients or materials; how to use in three steps; an endorsement panel only from the user's own quotes.

## Phases

1. Product intake. Look at the product photo inline and write a one-paragraph staging contract you reuse verbatim: the object type and form, material and finish, colours, the label state (the exact printed text if legible, otherwise "blank" or "unreadable"), its size next to a hand, how it opens or is used, one honest imperfection. Lock the angle to the side the photo shows. Lock the claims as a short allowlist.
2. Main image. An EDIT pass, never a reference render: a reference render on google/nano-banana-pro keeps the photo's kitchen or desk no matter how the prompt asks to discard it (verified twice). generate_image on bytedance/seedream-5-pro with the photo in imageUrls, imageSize square_hd, and the prompt "keep the product exactly as it is, same shape, same angle, same finish, and replace everything else with a pure white seamless studio background; the product upright filling about 85 percent of the frame, only a faint soft contact shadow under the base; no props, no text, no logos, no hands" (2048 pixels; a faint grey cast is normal), or openai/gpt-image-2 with the photo in inputImages at 1:1 and quality high when the white must be pure. Wait, look at it inline against the contract and the rules (white, fill, no text). Refine once at most with "change only X, keep everything else exactly". The user approves it.
3. Secondaries. One generate_image per slot in one wave with generate_batch on google/nano-banana-pro at 2K, the approved main image in imageUrls and declared as the product, the message in the prompt, the text as an exact string in quotation marks where the slot carries one with its placement and size, the brand palette for backgrounds and callouts, the contract for the product; the negatives: no extra product, no invented label text, no stock-photo gloss, no HDR glow, no watermark, no other text. A+ modules the same way at 3:1. wait_for_jobs.
4. Check. Look at every image inline with the main image beside it: the same product, legible text at phone size, correct spelling, exactly one message. One refinement per image with "change only"; a misspelling is re-rendered.
5. Delivery. The set in listing order, each with its message in a few words, a note on which claims were used, and one next step (the A+ modules, or a product reel).

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
