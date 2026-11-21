---
name: "social-graphics"
description: "Static social posts where the words live inside the image: the copy written first, one idea per slide, a cover that hooks and promises the swipe, a save call at the end, every slide rendered with its exact text on a text-rendering model in one locked style, spelling checked. Use when: static social posts with words on them; an Instagram or LinkedIn carousel, quote cards, a story sequence, a text-led announcement post, a tip or listicle post, a sticker pack, a meme with a supplied caption. Not for: a product image set (product-photoshoot), a thumbnail (thumbnail), an ad set with a product and an offer (ad-creative), listing images (amazon-listing), any video."
---

# Social graphics

Produce finished static posts with their text rendered inside the image. Copy first, then one locked style, then one render per slide with the exact words.

## Rules that never bend

- The copy is written and shown before any render; the user's exact words are final; a slide's text is short enough to read on a phone (a headline under eight words, a body under twenty-five).
- One idea per slide. The cover hooks and promises the swipe; the last slide asks for a save, a share or a follow in one line.
- Every slide is rendered on a text-rendering model (google/nano-banana-pro at 2K for 4:5 and 9:16; openai/gpt-image-2 only at 1:1, 2:3 or 3:2; bytedance/seedream-5-pro as the backup) with the exact string quoted in the prompt and its placement named; spelling is checked on every render and a misspelling is re-rendered, never accepted.
- One style sheet (the palette, the type feel, the layout grammar, the image treatment, the logo placement) written once and repeated verbatim on every slide; the logo passed in the reference image field when the brand has one.
- No AI-tell praise in the copy: never "literally", "obsessed", "game-changer", "changed my life", "hits different", "you need this", "trust me", "seamless", "effortless".
- Never a real person's face in a meme or a sticker.

## Intake, only for the gaps

Parse the brief first, then ask in one message only for what it left out: the format (a carousel of N, quote cards, a story sequence, a single post, stickers, a meme), the platform and its aspect (4:5 or 1:1 for a feed, 9:16 for stories), the topic or the supplied lines, the brand palette and logo when there are any. Ask for a missing topic or a missing count. Never ask about models.

## Phases

1. Copy. Write every slide's text: the cover line, one idea per slide, the closing call. Show it; a nod proceeds.
2. Style sheet. Write it in five lines: the palette with hex values, the type feel (a bold grotesque, a serif editorial, a handwritten accent), the layout grammar (text top-left with a wide margin, a full-bleed image with a band), the image treatment (flat illustration, photo with a duotone, plain colour), the logo placement. generate_image slide one on google/nano-banana-pro as the draft at the platform's aspect with the style sheet verbatim, the exact text in quotation marks with its placement, the logo declared when passed; the negatives: no other text, no watermark, no misspelling. Wait, look at it inline, read the text back. The user approves it.
3. Slides. One generate_image per remaining slide in one wave with generate_batch, slide one passed as the reference and declared for style continuity ("image 1 is the style: same palette, type and layout"), the style sheet verbatim, the exact text quoted, the platform's aspect. wait_for_jobs.
4. Check. Look at every slide inline: the spelling of every word, legibility at phone size, the style held. Re-render a failed slide with the same prompt; never accept a misspelling.
5. Delivery. The slides in order with each one's line, an offer of a caption and hashtags as text, and a note on the disclosure when the brief is sponsored.

## Stickers and memes

Stickers: a set of 6 to 12 on a plain white ground, one character or motif in one style, each with its short word when given, 1:1, generated in one wave with the first sticker as the style reference; then remove_background on each (ideogram-ai/remove-background). Memes: the supplied caption rendered in the classic top and bottom bands over the described scene, the exact words quoted, never a real person's face.

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
