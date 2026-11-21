---
name: lyra-copy-competitor-ad
description: "Use when the user wants to remake a competitor's or reference video ad for their app, e.g. \"copy this competitor ad\", \"make an ad like this one\", \"remake this video for my app\", \"do this TikTok / Reel for us\", or a Meta Ad Library / TikTok video link. Analyses the reference and builds the new video in Lyra. Static references go to lyra-copy-competitor-static."
---

# lyra-copy-competitor-ad

Mini skill. Takes a video ad that works for someone else, finds out **why** it works, and rebuilds that mechanism for the user's app: their pain, their feature, their person, their words, their brand. Four jobs in order: **analyse** the reference (Step 1a) → **go to the Brand Kit** and take every fact from it (Step 1b) → **ask the user** how to retell the reference, with variations (Step 1c) → **rewrite** the script for the brand (Step 2) → **generate** the new video in Lyra.

**Canvas layout → `lyra-workflow-layout`.** Every workflow this skill builds or changes is laid out by `lyra-workflow-layout`: sections in reading order with a STEP note above each one, the team's color code, clear node labels and the final check. The layout lines in this file only say which sections this creative needs.

**Statics have their own skill.** A static reference (one image, a carousel, several statics) or a static made from a competitor video's key frame → `lyra-copy-competitor-static` (static teardown by Reference L, layout map, new prompt, Nano Banana Pro build, variants). This file is for video.

**The Brand Kit is never skipped.** Close remake or free adaptation, the new ad always gets its name, audience, pains, feature, person, words, claims, offer, colors and ending from the user's Brand Kit (and the user's words in this chat). The reference gives only the mechanism.

**This is a way of thinking, not a script.** The rules below are defaults and good practice. Use judgment: when a different structure, shot or line serves the user's app better, do it and say why in one line. Only a few things are fixed: the line between mechanism and identity (next section), truth (no invented claims, reviews or numbers; the competitor's claims are never ours), the Brand Kit's facts, Lyra's technical limits, and the user's explicit choices.

**Base skill first.** Everything not written here follows `lyra-video-ad-generation`: the 8 steps, instruction order, app card, plan table and stages, run options with credits, run and report, prompt rules, models (Reference A), brief and scenes (B), audio (C), app UI (D), consistency (E), prompt craft (F), errors (G), de-slop (H), Brand Kit (I), Meta app ads (J). This file only adds what is specific to copying a reference. If the two disagree, the user wins, then this file, then the base skill.

**Other skills for their parts.** Once the reference is understood, the new video is built by the rules of the format it belongs to:
- a person talking to the phone (UGC, talking head, vlog, skit, interview) → `lyra-ugc-video` for the person, place, camera setup, voice and speech;
- the first 1 to 3 s, or several openings on the copied body → `lyra-video-hooks`;
- app screens, UI motion, end card → `lyra-ui-motion-video` (UI fidelity is hard there and here);
- anything else (lifestyle, POV, cinematic, stylized) → the base skill.

---

## What we copy, what we never copy (hard)

A competitor's ad is a **proof that a mechanism works on this audience**, not material to reuse. We copy the mechanism, never the identity.

| Copy (the mechanism) | Never copy (the identity) |
|---|---|
| the concept and the angle (the bet the ad makes on the audience) | their brand name, app name, logo, icon, slogan, catchphrases |
| the hook mechanism (kind, first frame idea, first move, line structure) | their exact lines, captions and on-screen text (rewritten every time) |
| the structure and beat order (hook, pain, demo, proof, CTA) | their people: faces, look, voice; no lookalike actor, no cloned voice |
| timing and pacing (beat lengths, cut rhythm, a new stimulus every N s) | their footage: never re-cut, crop, trace or overlay their video or frames in our ad |
| shot types, framing, camera setup and moves | their UI, screens and features (our screens come only from our screenshots) |
| the format (UGC selfie, POV, split screen, skit, UI motion…) | their claims, numbers, ratings, reviews, awards, offer and price |
| the audio role (native speech vs VO, music energy, where the SFX hits) | their music track, jingle or sound logo (music is generated from a description) |
| the CTA position and type (soft spoken tip, end card) | their brand colors and trade dress as a whole look; their mascots or characters |

**Rewrite test for every line.** A line keeps its **job** (callout, confession, objection, proof, CTA) and may keep its **shape** ("POV: you…", a question with a stake, a list of three tries), but its words are new and built from the user's Brand Kit. No sentence of ours shares a run of about five words with theirs, unless it is an ordinary phrase anyone would say ("try it tonight"). If a line only works with their product, it doesn't go in.

**Look test for the whole video.** Would a viewer who saw both ads think ours is theirs, or made by them? Then too close: change the person, the place, the palette or the line until the answer is no. The mechanism can be the same; the ad must look and sound like the user's brand.

---

## Two modes: close remake or free adaptation

The user picks the mode in Step 1c, after the teardown and the Brand Kit. Recommend one with one line why. **Both modes are built on the Brand Kit**: the remake is the reference's ad told with the brand's name, pains and offer; the adaptation is the reference's idea retold for the brand's audience, in its tone, usually ending on the app.

| | **A. Close remake** | **B. Free adaptation** |
|---|---|---|
| What stays | the same beats in the same order, beat lengths within about ±0.5 s, the same shot types, framing, camera setup and moves, the same hook mechanism and format, the same audio role | the idea, the angle, the hook mechanism and the structure; everything else is redesigned for the brand |
| What changes | the app name, pain, feature, person, place, words, voice, music, palette, UI, CTA, offer and ending (all from the Brand Kit) | everything the remake changes (from the Brand Kit), plus the shots, the place logic, the number and length of beats, the format if a better one fits, and an ending of our own with the app |
| Pick it when | the reference is a proven winner (running a long time, often 60 days or more in Meta Ad Library), the same audience and category, and the mechanism fits the app truthfully | a different audience, category or positioning; the mechanism depends on something the user doesn't have; or the user wants "the idea, not a copy" |
| Risk | too close to the competitor (run the look test) | losing the thing that made it work (keep the hook mechanism and the beat order) |
| Test value | isolates execution: "does this format work for us too?" | tests the concept in our own voice |

Both modes can run as an A/B test on one teardown: same app card, one remake, one adaptation. Name them so the media buyer sees which is which.

---

## Step 1 additions: the reference and the request

1. **The reference video.** Ask for it if missing. Accepted sources:
   - a video file in the chat or a public direct link to the file → `create_upload` ({url} for a link) → `attach_upload` into the workflow. Lyra takes MP4, WebM, MOV up to 200 MB, 1 minute and 4K;
   - a Meta Ad Library, TikTok or Instagram page link: usually a web page, not a file, so it can't be fetched. Ask the user to download the video and send the file, or upload it in Lyra (`open_upload_widget`). Don't retry the page link;
   - a **static ad** (one image or carousel cards) → hand over to `lyra-copy-competitor-static`;
   - several references for one idea: one teardown per reference, then say what they share (the shared part is the mechanism).
   Check `list_uploads` first: the user may have uploaded it already.
2. **Why this ad.** Ask in the same message, one line each, all optional: what do you like in it (the hook, the format, the pacing, the humour)? How long has it been running, and is it a known winner? Whose ad is it (the competitor's app, so we keep their name out of everything)? The ad copy, if they have it (title, caption, body, description from Meta Ad Library): it helps the analysis fill gaps. The mode question comes later, in Step 1c, once Claude knows the reference and the Brand Kit.
3. **The request.** What the user wants changed or kept ("same but for students", "in Portuguese", "30 s instead of 15", "our mascot instead of a person"). The user's request wins over the reference.

**Defaults (state, don't ask):** mode recommended by Claude, user picks · same length, ratio and platform as the reference (9:16, Reels / TikTok if unclear) · English, or the language the user asks for · models as the base skill (Seedance 2.5 for people, Seedance 2.0 for stylized or UI-led, 720p by default (1080p on the user's choice), sound on) · Nano Banana Pro for every image · no video reference connected to generation (see "Video reference" below) · an app ending (store-style end card or a phone moment with a real screenshot) offered in Step 1c · competitor's name only inside the "Reference teardown" note.

**Recommended first run:** A. Images first (character and keyframes), as in the base skill. The analysis itself runs before the plan.

---

## Step 1a: analyse the reference

Two paths, one standard. Use Path 1 when it's available, Path 2 when it isn't, and both when Path 1 leaves gaps. The result is always one **teardown** with two layers, saved in the user text node "Reference teardown":

- **Layer 1, creative classification:** one JSON object in the team's video ad analysis standard (Reference K at the end of this file: taxonomy, schema, rules). It says what the ad **is**, in fixed categories the team can compare and pattern-match across many ads.
- **Layer 2, production breakdown:** what Claude needs to **rebuild** it: shot list with times, person, camera setup, voice, pacing, don't copy list. Layer 1 alone isn't enough for a remake.

### Inputs and order of evidence (both paths)

- **Frames every 3 s across the whole video:** the primary source of truth for every visual field. Analyse the full arc (opening, middle, end, loop), never only the first frame.
- **Audio transcript, timestamped** (Whisper): secondary; the primary source for `hook_text` when the hook is spoken (narration, testimonial, dialogue).
- **Ad copy** (title, caption, body, description), when the user has it (Meta Ad Library shows it next to the video): tertiary, only to fill gaps not seen in the frames or heard in the transcript.
- Every field rests on evidence. Nothing is invented: a gap is marked "not seen" / "not heard" in layer 2, and in layer 1 the source field says `inferred` where the schema allows it.

### Path 1: Lyra's Creative Analysis node

Lyra has its own analysis node, **Creative Analysis** (action `pattern_import`): Upload Video → Creative Analysis → format, structure and hook of the reference. The MCP tools can **run** it and **read** it, but can't **create** it.

1. Look for it: `get_workflow` on the user's workflow (or the one they name). A Creative Analysis node already on the canvas → connect the attached reference upload to it if it isn't (`connect_nodes`), read its price, say it, run it after a yes (`run_node`, then `get_run_results` until done), read the output.
2. No such node → ask once: "Lyra's Creative Analysis node gives its own breakdown of the reference. Add an Upload Video and a Creative Analysis node on the canvas and tell me, or I can analyse the video myself. Which do you prefer?" Don't wait in silence: if the user prefers, go to Path 2.
3. **Output already in the standard** (Reference K) → it becomes layer 1 after a check: exact property names, exact enum values, all required fields, `visual_summary` first, `cta_custom_text` when `cta_type` is `custom`, 2 to 5 `key_claims` in the claim format, 2 to 3 hex colors, no extra properties. **Output in another shape** → map it into the standard. Where it's silent (a field, the shot list, exact timing, voice, camera setup), fill from Path 2 if you can, or mark "not in the analysis" and ask the user.
4. The node's output is a source, not the script. The rewrite (Step 2) is still written by Claude, by this file's rules, from the user's Brand Kit.

### Path 2: Claude's own analysis

Claude analyses the video itself when it can see it.

- **The file is in Claude's environment** (attached in the chat, or in a folder Claude can read) **and there is a shell with ffmpeg:**
  - duration and size: `ffprobe`;
  - cuts: `ffmpeg -i ref.mp4 -vf "select='gt(scene,0.3)',showinfo" -f null -`, read the timestamps;
  - **frames for layer 1, every 3 s:** `ffmpeg -i ref.mp4 -vf "fps=1/3,scale=720:-1" frames3s/%03d.jpg`;
  - **extra frames for layer 2:** one per cut, and about two per second in the first 3 s (the hook);
  - **transcript with timestamps:** whisper if installed (for example `whisper ref.mp4 --model small --word_timestamps True --output_format json`); otherwise read the burned-in captions from the frames, or ask the user for the spoken text with rough times;
  - **colors:** the 2 to 3 dominant colors across the frames as hex (a short script over the frames, for example k-means on downscaled pixels), most dominant first.
  Then look at every frame in order and write both layers.
- **No shell, or the video can't be opened:** ask the user for screenshots about every 3 s (at least the first frame, each new shot and the last frame), the spoken words with rough times, and the ad copy if they have it. Build the teardown from them and mark what they don't cover.
- **Never describe what you didn't see or hear.** A teardown with honest gaps is better than an invented one.

### Layer 1: creative classification (JSON)

Written exactly by the standard in Reference K:

- **one valid JSON object**, the schema matched literally: exact property names, exact enum values, no additional properties, all required fields;
- **`visual_summary` first**: the full arc in time order (what opens, what the middle shows, how it ends or loops), concrete frames, presenter actions, scene and style shifts, key on-screen text and the spoken hook transcribed exactly; never a generic "the ad promotes…";
- **`key_claims`**: 2 to 5 items, each `"[exact element from the frames or transcript] — [the rhetorical mechanism: why it works, what resistance it removes]"`; a visual element doing the persuasion is described as what is shown; nothing that isn't in the frames or transcript;
- **frames first** for visual fields, the **transcript first** for a spoken `hook_text`, ad copy only for gaps;
- `cta_custom_text` whenever `cta_type` is `custom`; `color_palette` 2 to 3 hex codes, most dominant first.

In a pipeline that expects the raw object, return only the JSON, nothing before or after it. In this skill the JSON goes into the "Reference teardown" note, and the user gets a short readable version in Step 1c.

**How layer 1 feeds the rest of the skill:**

| Field | Used for |
|---|---|
| `visual_summary` | the base of the shot list (layer 2) and of the side by side script (Step 2) |
| `hook_type`, `hook_text`, `hook_source` | the hook mechanism to keep and its kind and type in `lyra-video-hooks`; the line itself is rewritten, never reused |
| `narrative_arc`, `scene_structure` | the spine and the beat order; one clip with "cut to" or separate clips (base Step 2 reasons) |
| `presenter_type`, `video_subject`, `has_human_face` | which skill builds it and who is on screen: `real_person_UGC`, `presenter_talking_head` → `lyra-ugc-video` · `app_screen_walkthrough`, `screen_only` → `lyra-ui-motion-video` · `animated_character` → stylized on Seedance 2.0 · `hands_only_POV` → hands-only shots, no face · `voiceover_only` → VO node over B-roll |
| `video_production` | the polish level and look: `UGC_handheld` → raw phone-real · `studio_directed`, `talking_head_produced` → elevated · `app_mockup_animated` → UI motion with design frames · `screen_recording_live`, `screencast_tutorial` → our real screenshots only, never a fake recording · `AI_generated_video` → still de-slop rules |
| `video_pacing`, `format` | the cut rhythm and the length (timing contract) |
| `audio_style` | native speech in the clip (`dialogue`), a VO node (`voiceover`), a music node (`music_only`, `mixed`), nothing (`silent`) |
| `on_screen_text_style`, `text_to_visual_ratio`, `copy_structure` | the Video Editor text plan (captions, headlines, lists); never in a generation prompt |
| `emotional_tone` | the tone of the new lines, inside the Brand Kit's tone of voice (the kit wins on a conflict) |
| `offer_framing`, `cta_type`, `cta_source` | the CTA slot, its type and where it sits; the content comes from the Brand Kit's offer (theirs is never reused; no offer in the kit → no offer) |
| `social_proof_type` | which proof slot the ad has; filled only with the Brand Kit's real proof, otherwise dropped or replaced by a demo |
| `key_claims` | the mechanism behind each claim (kept) and their exact wording (never reused); feeds "Their claims" and "Why it works" |
| `color_palette` | the reference's palette, replaced by the brand palette (look test) |

### Layer 2: production breakdown (template)

Short, factual, one line per field, in the same note under the JSON:

1. **Header:** platform · ratio · polish level (raw, elevated, stylized) · language · whose ad (internal only).
2. **The bet (one line):** "They bet [audience] will [action] because [concept] addresses [pain] through [mechanism]." This is what we copy.
3. **Hook detail (0 to 3 s):** kind (visual, verbal, combined) · first frame · first move · text on frame 1 · sound · awareness level it targets (`lyra-video-hooks`).
4. **Shot list** (one row per shot, times from the cuts):

| # | Time | Beat (hook, problem, solution, proof, offer, cta, end card) | Shot and framing | Camera setup and move | What happens | Spoken line | On-screen text | Sound | Cut to next |
|---|---|---|---|---|---|---|---|---|---|

5. **Person:** archetype (mirror, friend a step ahead, skeptic, insider, two people) · age range · look and energy · setting and time of day · voice (gender, age, accent, pace, energy).
6. **Pacing detail:** number of cuts · average shot length · where the energy rises · new stimulus every N s.
7. **Audio detail:** words per second · music (genre, tempo, energy curve, vocals or not) · SFX hits.
8. **The app in the ad:** how the product is shown (the change on the person, the result in life, the phone moment, real screens) · when · for how long.
9. **CTA and end:** spoken CTA, caption, end card.
10. **Their claims** (from `key_claims` and anything else said or shown, listed so we never reuse them).
11. **Why it works:** 2 to 3 short reasons.
12. **Don't copy list:** the identity elements of this ad by name (their app name, slogan, actor look, sound logo, mascot, color look).
13. **Can't be reproduced truthfully:** what depends on something the user doesn't have (a real review, a celebrity, a feature, a number, a physical product) and the nearest truthful version.

**Example (short, fictional).** Layer 1:

```json
{
  "visual_summary": "Opens on a handheld front-camera selfie: a woman in her twenties drops onto a pillow in a dark bedroom, phone held above her face, and says \"I tried every sleep hack on TikTok.\" Text overlay: \"every. single. one.\" Three fast jump cuts follow (2.5 to 6 s), each closer: a mug of tea, earbuds in, counting on her fingers. At 6 s she turns the phone screen toward herself, not visible to the viewer, and says \"This one says asleep in 10 minutes.\" Cut at 10 s to B-roll: her eyes closed, the phone face down on the duvet. Ends at 13 s back on the selfie, smiling: \"It's free, just try it.\" Word-by-word captions at the centre throughout.",
  "hook_type": "UGC_testimonial",
  "hook_text": "I tried every sleep hack on TikTok.",
  "hook_source": "transcript",
  "narrative_arc": "problem_agitate_solve",
  "presenter_type": "real_person_UGC",
  "scene_structure": "single_continuous",
  "on_screen_text_style": "mixed_overlays",
  "video_production": "UGC_handheld",
  "video_subject": "presenter_talking_head",
  "format": "video_6_15s",
  "emotional_tone": "empathetic_relatable",
  "copy_structure": "story_arc_narrative",
  "offer_framing": "free_trial",
  "cta_type": "try_free",
  "cta_source": "transcript",
  "key_claims": [
    "\"I tried every sleep hack on TikTok.\" — a confession of failure puts her on the viewer's side before any product appears; the viewer's own failed tries become the proof that the problem is real.",
    "Three jump cuts: tea, earbuds, counting on her fingers — the old ways shown fast and closer each time, so the frustration builds without a word of explanation.",
    "\"This one says asleep in 10 minutes.\" — a specific time promise turns a vague hope into a result the viewer can test tonight.",
    "Eyes closed, phone face down on the duvet — the result is shown on the person, not on the screen; sleep itself is the demo."
  ],
  "social_proof_type": "user_quote",
  "color_palette": ["#1B2233", "#E8B27A", "#F2F2F2"],
  "has_human_face": true,
  "text_to_visual_ratio": "visual_dominant",
  "video_pacing": "medium",
  "audio_style": "dialogue"
}
```

Layer 2:
> Header: TikTok · 9:16 · raw · English · a sleep app (internal).
> Bet: they bet women 20 to 30 who can't fall asleep will install because a tired confession at 2 am makes the app feel like a friend's tip.
> Hook detail: combined · she drops onto the pillow · text "every. single. one." · pillow thump · problem aware.
> Shots: 5 cuts, average 3 s; 0 to 2.5 s selfie in bed (handheld, arm's length); 2.5 to 6 s three jump cuts, one per hack, closer each time; 6 to 10 s phone moment, screen toward her; 10 to 13 s eyes closed, phone on the duvet (B-roll); 13 to 15 s back to selfie, soft CTA.
> Audio detail: about 2.4 words per second; no music; room tone.
> Their claims: "asleep in 10 minutes" (theirs, never reused).
> Why it works: pain in 2 s in her words; the three failed hacks are the viewer's own history; no screen needed.

---

## Step 1a (static): moved

Static references (one image, a carousel, several statics) and statics made from this video's key frame are analysed and built by `lyra-copy-competitor-static`: the static standard (Reference L), the measured layout map, the transfer map by zones, the Nano Banana Pro prompt and the variants. When a video copy and a static copy of the same reference are wanted, run this skill for the video and that skill for the static, on the same Brand Kit sheet.

---

## Step 1b: the Brand Kit (always, in both modes)

Right after the teardown, before a single line is rewritten, Claude goes to the Brand Kit. This step is never skipped, in the remake as much as in the adaptation: the reference says **how** the ad works, the Brand Kit says **what** the new ad is about and **who** it talks to. Nothing is taken from the competitor's brand, and nothing is invented to fill a gap.

**Which Brand Kit** (base Reference I):
1. A Brand Kit given in the chat → use it.
2. Otherwise check what the workflow has: `get_workflow` (the kit assigned to the workflow) and `list_brand_kits` (the kits in the workspace).
3. **Exactly one** candidate → confirm in one line: "I'll make it for {kit name}, right?"
4. **More than one** (several kits on the workflow, or none assigned and several in the workspace) → ask which one, with their names. Never mix two kits in one ad. Two apps wanted → two separate builds, one kit each.
5. **None** → ask once: send it here, or should I check and connect one of the workspace's kits? Or type the essentials: app name, what it does, audience, pains, the feature to show, approved claims, offer, tone, logo and screenshots.
6. Once chosen, `assign_brand_kit` on the workflow if it isn't assigned yet.

**Read it fully and fill the Brand Kit sheet** (top of the "Transfer map" note), one line per field:
app name exactly as written, and how it's pronounced · what it does · audience and segments · pains in their words · desires · objections · features (mark the one that answers the reference's pain) · approved claims and proof · forbidden claims · offer and CTA · tone of voice · positioning (sets the polish level) · colors and fonts · assets (logo, icon, screenshots, end card, store badges) · markets and languages · must include / must exclude.

**Gaps.** A missing pain → 3 to 5 pain hypotheses in the audience's words, to confirm (as in `lyra-video-hooks` Step 1). Missing screenshots → the screen stays hidden, or ask for them. No approved claim → no claim. A gap is never filled from the competitor's ad.

**Conflicts.** The user's words in the chat win over the kit; name the conflict in one line. If the reference's mechanism clashes with the kit (a chaotic brainrot ad for a premium finance brand, a body before/after for a health app, a must exclude), say so and propose the adaptation that keeps the mechanism inside the brand's rules.

## Step 1c: ask the user, and offer variations

One message, after the teardown and the Brand Kit sheet, before any build. Every option in it is written with the Brand Kit's real name, audience, pain, feature and offer, so the user sees their own ad, not an abstract plan.

1. **The reference in 3 to 4 lines**, from both layers: the bet, the hook (`hook_type`, the hook line), the arc (`narrative_arc`), the format and look (`presenter_type`, `video_production`), why it works (`key_claims`).
2. **The mode question**, both options told in Brand Kit terms, with a recommendation:
   - **A. Close remake:** "the same ad beat for beat, but it's {app name}: {pain from the kit}, {feature}, {persona from the kit's audience}, {offer}, ending on {app ending}."
   - **B. Free adaptation:** "the same idea and hook, retold for {audience from the kit} in {tone from the kit}, with our own scenes and an ending with {app name}."
3. **2 to 3 variations of how to present the reference our way**, one line each, each built on the Brand Kit, one recommended. Ways to vary (pick what fits the reference and the kit):
   - another pain or segment from the kit (the same body for "students" and for "night-shift workers");
   - another persona or place (a different archetype from the audience, the pain moment in another spot);
   - problem first vs app first (the app named in the first 2 to 3 s);
   - another format for the same mechanism (UGC → UI motion, split screen, talking object);
   - another hook on the same body (`lyra-video-hooks`, mode A);
   - another medium: a static ad from the video's key moment, one concept tested across placements (built by `lyra-copy-competitor-static`);
   - another ending (see 4).
4. **The ending with the app.** Unless the reference already ends on the product in a way the user wants to keep, offer an app ending and ask which: a **store-style end card** (`lyra-ui-motion-video`) with the kit's icon, app name, benefit line and CTA · a **phone moment** with a real screenshot of the key screen · the **person with the result** and the app name in the caption.
5. **Only the questions still open**, in the same message: missing kit fields, screenshots, language, length.

Each variation the user picks becomes its own concept (`C1`, `C2`…) with its own transfer map, script and Video Editor; more takes of one variation are `count`, not new concepts (base rule).

**Example (short, fictional app Calmly).**
> Reference: 15 s UGC storytime, a tired confession in bed at 2 am, three failed sleep hacks, the app as the last try, a soft CTA. It works because the pain lands in 2 s in her own words.
> Brand Kit: Calmly, the only kit in this workspace. Make it for Calmly, right?
> A. Close remake: the same five beats and timing, but it's Calmly: Mia, 21, a student whose brain won't stop at 2 am, tries tea, podcasts, counting sheep, then the 5-minute wind-down timer; ends on the Calmly end card "Sleep in 5 minutes · Get".
> B. Free adaptation: the same confession hook, retold as a walk and talk the next morning, "I actually slept", ending on the phone with your real timer screen.
> Variations: V1 the remake above (recommended: proven format, same audience) · V2 the same body for the kit's second segment, young nurses after night shifts · V3 app first: she opens Calmly in the first 2 s, then the confession.
> Ending: the Calmly end card, or the phone with your timer screenshot? Send me the timer screenshot if the screen should be seen.

---

## Step 2 addition: the transfer map and the new script

### The transfer map

Before writing a line, map each part of the reference to the user's app, for the mode and variation the user picked in Step 1c. The "Ours" column comes **only** from the Brand Kit sheet (Step 1b) and the user's words. One line per element: **reference → ours · keep / translate / drop · why**. It goes into the "Transfer map" text node and, short, into the concept.

| Element | Reference | Ours (from the Brand Kit) | Action |
|---|---|---|---|
| Audience | women 20 to 30, can't sleep | students 18 to 25, can't switch off | translate |
| Pain | can't fall asleep | brain won't stop at 2 am | translate |
| Hook mechanism | combined: drop onto pillow + confession | same mechanism, new beat and line | keep (remake) |
| Old way beat | three failed hacks | tea, podcasts, counting sheep (from reviews) | translate |
| Feature | their sleep stories | Calmly's 5-minute wind-down timer (real screenshot) | translate |
| Claim | "asleep in 10 minutes" | none approved → result shown on the person, no number | drop |
| Person | their actress | Mia, 21, character card from our audience | translate |
| CTA | "it's free, just try it" | real offer from the Brand Kit: "It's free. Try it tonight." | translate |
| Music | none | none | keep |
| Ending | soft CTA on her face | Calmly end card: icon, "Sleep in 5 minutes", Get (picked in Step 1c) | translate |

**Rules for the map:**
- Every beat of the reference has a row. A beat we drop is written as dropped, with the reason.
- Their pain becomes the **closest real pain** in the user's pain map, said in the user's audience's words. If none is close, the mechanism doesn't transfer: say so, and offer the adaptation mode or another reference.
- Their feature becomes **one real feature** of the user's app that answers that pain. Never borrow a feature the app doesn't have.
- Their claims are dropped by default; a claim comes back only if the user's Brand Kit has its own approved one.
- Their person becomes a persona from the user's audience (`lyra-ugc-video` casting), different in look from theirs.
- Their palette and look become the user's brand palette, at the same polish level.

### The new script

Written by Claude into the "Script" text node (base Reference B), from the transfer map.

- **Timing contract.** Remake: the same beats in the same order, each beat within about ±0.5 s of the reference, the same total length. Adaptation: the total length from the request, beats as the new structure needs. Durations always add up exactly.
- **Word budget per beat.** Count the reference's words per beat and match them closely, then check against the base pace (about 2.5 words per second, speech ending about 1 s before the clip ends). A translation into another language usually runs longer: shorten it, never rush it.
- **Same job, new words.** Each line keeps its job and may keep its shape; the words come from the Brand Kit and customer words. Run the rewrite test on every line.
- **Hook first.** Write the hook with `lyra-video-hooks` (line checks, 6 to 10 words, text 2 to 6 words marked for post). In remake mode it keeps the reference's hook kind and mechanism; in adaptation mode it may change if a stronger hook for this pain exists, said in the plan.
- **On-screen text and captions** are rewritten too, marked for post (Video Editor only, never in a prompt).
- **Side by side in the concept.** Show the user the script next to the reference, beat by beat:

| Beat | Time | Reference (what it does) | Ours (what we do and say) | Kept | Changed |
|---|---|---|---|---|---|

The concept the user approves (base Step 2) has: the Brand Kit it is built on · the mode and variation picked in Step 1c · transfer map in short · the side by side script · the ending · the plan table · the model question.

---

## Best way to build it

The format of the reference decides the build. The user's explicit choices override any row. Models and prices: base Reference A.

| If the reference is | Build by | Graph | Models |
|---|---|---|---|
| UGC, talking head, storytime, vlog, skit, interview | `lyra-ugc-video` | character image (our persona, count 2) → one Seedance 2.5 clip, speech in quotes, the reference's cuts written as "cut to" → B-roll and UI insert if the reference had them → Video Editor | nano-banana-pro · seedance-2.5 |
| A hook-led ad, or the user wants several openings on the copied body | `lyra-video-hooks` (mode B, or mode A on the new body) | as the hook skill | as the hook skill |
| UI motion, floating phone, demo of screens | `lyra-ui-motion-video` | our screenshots → design frames → one Seedance 2.0 frame clip per shot → end card → Video Editor | nano-banana-pro · seedance-2.0 |
| Lifestyle, POV, cinematic, real people without speech | base skill | character image → one multi-shot clip with "cut to" in the reference's order → VO + music → Video Editor | nano-banana-pro · seedance-2.5 |
| Illustration, cartoon, stylized, moving text | base skill | keyframe per shot in our style → Seedance 2.0 with frames → Video Editor | nano-banana-pro · seedance-2.0 |
| The mechanism is one signature movement (a dance, a gesture, a fall) | base skill | our character image + **a motion video we own or film**, never their footage → Kling 3.0 Motion Control; speech parts stay on Seedance 2.5 | kling-v3-motion-control · seedance-2.5 |
| Longer than 30 s | base Reference A | the script split in two parts at a natural beat, same references, two clips, joined in the Video Editor | seedance-2.5 |
| A split screen, chat thread or comment reply | `lyra-video-hooks` (catchy formats) | as the hook skill; bubbles and comments stylised, our own text | nano-banana-pro · video_composer |

**Shots, not micro clips.** As in the base skill, one multi-shot clip by default; split only for the base reasons (over 30 s, a UI insert, different models or exact frames, a failed shot, the user asks). A remake with many quick cuts still fits in one Seedance 2.5 clip when the cuts are written as "cut to" with their lengths.

### Video reference (the competitor's video in the generation node)

By default the reference video is **only analysed**: it sits in Section "Reference" and is **not connected** to any generation node. The montage comes from the script Claude writes (shot list with times), as the base skill's reference policy says.

Only in **remake mode**, and only when the user asks for the rhythm to be copied closer, the reference can go into the Seedance clip as **one video reference used as an editing reference only** (cuts, pacing, camera rhythm). Then:
- say once that it can leak their look (faces, outfit, colors, text, logo) into ours;
- write its job first in the prompt: "[Video1] is an editing reference only: copy its cut rhythm, shot lengths and camera energy. Do not copy its people, faces, clothing, places, colors, text, logos or sound.";
- check the result with the user against the "Don't copy list" before anything else; any leak → disconnect it and rerun with the script only.
Never use their footage as a frame, a layer, a B-roll or a motion source.

**Layout.** Section "Reference" (the uploaded reference, the Creative Analysis node if any, "Reference teardown" and "Transfer map" notes; nothing here feeds generation by default) → then the base layout: Sources (script note, character, screenshot uploads) → Images → Clips → Audio → Video Editor. Labels: "Ref: sleep app UGC (analysis only)", "Script: remake C1", "Mia: bed 2 am (clip)", "Final: C1 remake · storytime sleep".

---

## Prompt rules (copy)

| Node | Write | Avoid |
|---|---|---|
| Reference teardown (text) | layer 1: one JSON object by Reference K; layer 2: the production breakdown; facts only, gaps marked "not seen" / "not heard" | guesses; enum values that aren't in the schema; paraphrased claims; long praise of the ad |
| Transfer map (text) | one row per element: reference → ours → keep / translate / drop → why | their lines copied in as "ours" |
| Script (text) | the new lines per beat with times and word counts; captions marked for post; the side by side table | their exact words, product name, slogan, claims |
| Character image | our persona's card from the user's audience (UGC rules); the reference's framing and camera setup described in words | their actor's description ("like the girl in the ad"); a lookalike; their outfit or set |
| Video clip | roles of references first ([Image1] is our character…), then the reference's shot plan **in words**: framing, camera setup, action per beat, "cut to" with lengths, our lines in quotes, sound line (when someone speaks: voices and scene sounds only, "no music, no background music, no soundtrack, no score", base Reference C), end state | "as in the reference video", "same as the competitor"; their text, logos, colors; a video reference without its job stated |
| Music | genre, tempo and energy curve of the reference's track, described | their track, the song name, the artist name (error) |
| VO | our words only, sized to the beat timing, ~1 s shorter than the video | their wording translated line by line |

Every prompt is self-contained (base rule): describe the shot itself, never "like the reference". The model never sees the competitor's ad unless a video reference is connected on purpose.

---

## Run options (copy)

**Run order, not a menu** (base Step 6): after the user's yes, run all of it in this order without offering options. Stop between stages (the look first, then the rest) only when the user asked for it, or when the plan is expensive and that was said in the approval message.

As in the base skill, credits read from the nodes, per option. The analysis comes first and on its own: **Path 1** costs what the Creative Analysis node shows next to Run (say it before running) · **Path 2** costs no credits. Then: **A. Images (recommended):** character and keyframes · **B. Clips** for the picked images, with VO and music · **C. Everything** → Video Editor. Remake and adaptation together: the same options, multiplied by two.

---

## Truth, rights and brand safety

- The competitor's ad is a reference for analysis. Their footage, frames, audio, music and text are never part of our ad.
- No competitor name, logo or product in our ad, and no comparison with them by name. A comparative ad that names a competitor is a legal question for the user's team, not a default; this is not legal advice.
- Their claims, numbers, ratings, reviews and awards are theirs. Ours come only from the user's Brand Kit or the user.
- No lookalike of their actor or creator, no cloned voice, no copy of their mascot or characters.
- Trends and formats are free to use; specific creative work isn't. When in doubt, move the ad further from the reference (adaptation mode).
- AI people follow `lyra-ugc-video` Truth and disclosure: never presented as real customers; remind the user once about the platform's AI label.
- **Brand safety** (Lyra's System Preamble, base Reference B): no profanity, no political statements, no unsubstantiated health claims, and no digs at the competitor even without its name. The Brand Kit's **forbidden claims are enforced absolutely**, in every line, caption, visual and VO, even when the reference makes that claim; if the user asks for one, say once that it is on the kit's forbidden list and leave it out unless the user confirms the kit is outdated.

---

## Deliverable and naming

1. A "Reference teardown" note and a "Transfer map" note in Section "Reference".
2. The new "Script" note with the side by side table.
3. All planned images, clips, audio and one Video Editor per final (two when remake and adaptation run as an A/B).

Name every final with a code the media buyer can paste into Ads Manager: `B{batch}-A:{angle}-F:Copy-{format}-{Remake|Adapt}-R{reference}-C{concept}`, e.g. `B5-A:BrainWontStop-F:Copy-UGCStorytime-Remake-R1-C1`. Static finals are named by `lyra-copy-competitor-static`. Add `H{n}` when hooks from `lyra-video-hooks` are tested on it, and `P{n}` for personas. The competitor's name stays out of the code; `R1` points to the teardown note.

---

## Common mistakes (copy)

| Mistake | Prevention |
|---|---|
| Script written before the reference is understood | Teardown first, then the Brand Kit, then the questions, then the transfer map, then the script |
| Brand Kit skipped "because it's a close remake" | Step 1b in both modes; every name, pain, feature, claim and offer from the kit |
| Several kits on the workflow or in the workspace, one picked silently, or two mixed | Ask which kit; one kit per ad |
| Gaps in the kit filled from the competitor's ad | Pain hypotheses to confirm, hidden screen, no claim |
| Mode asked as an abstract choice | Both modes and 2 to 3 variations told with the kit's real name, audience, pain and offer |
| No app at the end | Offer the app ending in Step 1c: end card, phone moment or result + caption |
| Classification by the first frame only, or enums invented | Frames every 3 s across the full arc; values only from Reference K |
| Claims paraphrased or added from the ad copy | `key_claims` quote the frames or transcript exactly; ad copy only fills gaps |
| A static reference built with this video skill | `lyra-copy-competitor-static` |
| The teardown describes things Claude didn't see or hear | "Not seen" / "not heard" + ask; frames and transcript only |
| Waiting for the Creative Analysis node that isn't there | Ask once, offer Path 2, keep moving |
| Their lines translated or lightly reworded | Same job, new words; rewrite test on every line |
| Their claim ("asleep in 10 minutes") reused for our app | Their claims listed and dropped; ours only from the Brand Kit |
| A feature borrowed from their app | One real feature of ours per transfer map; no fit → adaptation or another reference |
| Our actor looks like theirs, same outfit, same room | Persona from our audience; look test |
| Their palette and look kept, so our ad reads as theirs | Our brand palette at the same polish level |
| Their video connected to generation by default | Analysis only; video reference only on request, in remake mode, with its job stated and a leak check |
| Their footage used as B-roll, frame or motion source | Never; for motion transfer use footage we own |
| "As in the reference video" in a prompt | Describe the shot in words; prompts are self-contained |
| Remake drifts in timing or beat order | Timing contract: same beats, about ±0.5 s each |
| Adaptation loses the hook mechanism | Keep the bet, the hook mechanism and the beat order |
| Their song or artist named in the music brief | Describe genre, tempo and energy; no names |
| Competitor's name in the final's name or on screen | Internal teardown note only; `R{n}` in the code |
| A 60 s reference promised in one clip | Two parts joined in the Video Editor (base Reference A) |
| Page link from Ad Library retried as a file | Ask for the downloaded file or an upload in Lyra |

## Quality gates (copy)

- **Stage 0 (teardown, Brand Kit, map and script; Claude checks before sending):** the Brand Kit chosen and confirmed (asked when there was more than one)? Its sheet filled, gaps marked? Mode, variation and ending picked by the user, all told in the kit's terms? Layer 1 a valid JSON object by Reference K (exact names and enums, all required fields, `visual_summary` first, claims in the claim format, analysed on frames every 3 s across the whole video)? Every field of layer 2 filled or marked as a gap? The bet in one line? Every reference beat mapped (keep, translate, drop)? Pain and feature real for our app? Their claims dropped? Lines pass the rewrite test? Timing adds up (remake: each beat about ±0.5 s)? Word counts fit at a calm pace? Don't copy list written?
- **Stage 1 (images):** our persona from our audience, clearly not their actor? Our palette and setting? The reference's framing and camera setup there? (Plus the base, UGC or UI stage 1 checks.)
- **Stage 2 (clips):** beats in the reference's order and rhythm? The hook lands like theirs, in our words? If a video reference was used: no leak of their people, colors, text or logo? (Plus the format's stage 2 checks.)
- **Stage 3 (final), side by side:** ask the user to watch both one after the other. Same mechanism, same energy in the first 3 s? Is it clear in one watch what **our** app does? Anything that still says "competitor" (a phrase, a look, a sound, a color)? Promise matches our store page? Captions, CTA, 9:16, planned resolution, length, name with its code? AI label reminder given?

## After the test

Read the test as in `lyra-video-hooks` (After the test). A reference that wins for a competitor is a hypothesis for us, not a promise: judge ours by our own KPIs (hook rate, hold rate, cost per trial, payers). Say what won: the mechanism (the copy works → make more on this bet with new hooks, personas, languages) or not (the mechanism doesn't transfer to our audience → note it, try the adaptation or another reference). Save the teardown and the result to the project's hook or creative repository, so the next copy starts from what we already learned.

---

## Reference K. Video ad creative analysis standard (layer 1)

The team's standard for classifying a video ad. Claude follows it word for word for layer 1 of every teardown, and checks the Creative Analysis node's output against it.

**Role.** A performance marketing creative analyst for video ads: extract structured classification data from the creative.

**Inputs.** Frames extracted every 3 s across the whole video (primary source of truth; analyse the full arc, not just the first frame) · the audio transcript, timestamped, from Whisper (secondary: spoken hooks, narration, testimonial content) · optional ad copy fields: title, caption, body, description (tertiary support only).

**Core requirements.** Exactly one valid JSON object that conforms to the schema · no preamble, markdown fences or explanation when the raw object is requested · exact property names, exact enum values, no additional properties · `visual_summary` always the first field · outputs limited to evidence in the creative and these rules.

**Priority rule.** Frames are the source of truth for visual fields · the transcript is the source of truth for `hook_text` when the hook is spoken · title, caption, body only fill gaps not visible in the frames or transcript · the full arc matters: opening, middle and end.

**What to examine before classifying.** All frames in sequence: what appears in the first 1 to 3 s (hook setup) · how the narrative or visual structure develops across scenes · whether a presenter is shown, and in what context · the dominant visual subject across the full duration · which on-screen text overlays appear and when · how the video ends or loops.

**`visual_summary`.** A concrete visual-mechanical description of the full arc, not a generic marketing summary: in time order (what opens, what the middle shows, how it ends) · specific frames, on-screen text, presenter actions, scene changes · key on-screen text and the spoken hook transcribed exactly · distinct scene or style shifts named ("hard cut to full-screen graphic slide", "loops back to opening frame") · no "the ad promotes…" unless tied to the concrete mechanic.

**`key_claims`.** For each claim: (1) quote or closely reference the exact language, phrase or visual element in the frames or transcript, never paraphrased, never invented; (2) explain the rhetorical mechanism, how this element communicates value or overcomes resistance. Format: `"[exact element from creative] — [explanation of why this works / what it communicates]"`. A visual element doing the persuasion is described as what is shown and why it works as a claim. No claims the frames or transcript don't support.

### Taxonomy

**`hook_type`** (the primary persuasion mechanic of the opening 3 s): `problem_solution` names a pain, then frames the product as the fix · `before_after` shows or implies a state change · `social_proof` leads with others' behavior, ratings or adoption · `UGC_testimonial` first-person user voice or a real person sharing their experience · `curiosity_gap` withholds information to create a gap that demands resolution · `fear_urgency` anxiety, loss aversion, fear of missing out · `question` a direct question to the target audience · `statistic_claim` a specific number, percentage or data point · `POV_first_person` puts the viewer in the scenario with "you" or first person · `tutorial_how_to` a promise to show how to do something · `unboxing_reveal` sequential discovery or unwrapping · `comparison_vs` contrasts two options, brands or states · `transformation` the journey or change process, not just the endpoint · `day_in_life` follows a character through a scenario · `GRWM_get_ready` get-ready-with-me, product in a routine · `reaction` a visible emotional reaction · `myth_busting` challenges a common belief · `listicle` numbered or bulleted list as the structure · `controversy_hot_take` provocative or polarizing opening · `authority_expert` credentials, expertise or professional context · `emotional_story` a narrative with an emotional arc · `product_demo` the product shown in use as the immediate hook · `challenge` invites the viewer to try something.

**`hook_source`** (where the hook text was found): `on_screen_text` overlay on the frame · `transcript` spoken by a presenter or VO, not visible as text · `title` · `caption` · `body` · `description` (ad copy fields) · `inferred` from the overall intent, no explicit source.

**`narrative_arc`** (story structure across the full video): `talking_head_direct` presenter speaks to camera the entire video, no scene structure · `hook_demo_cta` hook scene → product demonstration → end card or CTA · `hook_loop` opens and closes on the same or near-identical scene, built for replay · `problem_agitate_solve` the pain is shown and worsens before the solution · `listicle_sequential` numbered items one by one · `multi_segment_compiled` 3+ distinct scenes or styles stitched together, often by VO · `transformation_reveal` linear before to after, payoff at the end · `testimonial_monologue` one person's story start to finish, no cutaways · `social_proof_compilation` several testimonials or reactions edited together · `unboxing_reveal` tension builds toward a reveal · `tutorial_step_by_step` ordered steps · `comparison_walkthrough` alternates option A and option B · `educational_explainer` structured teaching, instructor pacing · `single_shot_loop` one continuous take, no edits, built to loop · `GRWM_routine` product integrated in a get-ready routine · `reaction_to_content` presenter reacts to something shown on screen.

**`presenter_type`** (the primary on-screen presence): `real_person_UGC` selfie-style, phone-held, casual · `real_person_expert` a person in an authority setting (uniform, lab, trade show, professional tools) that signals credibility without stating it · `real_person_lifestyle` a person in an aspirational context, not speaking to camera · `celebrity_influencer` a recognizable public figure or verified creator · `AI_avatar` a synthetic human presenter · `animated_character` illustrated or cartoon presenter · `voiceover_only` a voice, no person on screen · `hands_only_POV` first-person hands, no face at any point · `none` no human presence.

**`scene_structure`** (spatial and temporal organization): `single_continuous` one location, one setup, no meaningful scene cuts · `two_scene_ab` exactly two scenes with a clean A to B transition · `hook_plus_demo` a short hook scene, then an extended demo · `multi_segment_complex` 3+ scenes with meaningfully different styles or locations · `looping_hook` opens and closes on identical or near-identical frames · `rapid_montage` many clips under 2 s each · `screen_only` the whole video is an app or screen recording.

**`on_screen_text_style`**: `subtitle_captions` word-by-word captions following speech, at the bottom · `headline_overlays` large standalone text blocks, not following speech · `kinetic_typography` text animation is the main visual · `app_ui_labels` text inside a shown app interface · `infographic_labels` text in a designed full-screen graphic slide · `mixed_overlays` captions and headlines together · `emoji_text_hybrid` emoji used prominently with text · `none` no text overlays.

**`video_production`** (dominant production style): `UGC_handheld` phone-shot throughout, natural, unpolished · `studio_directed` professional light, controlled set, directed shots · `screen_recording_live` a real device screen captured as is, status bar and real UI visible · `app_mockup_animated` polished animation of app UI, not a real recording · `graphic_animation_only` motion graphics only, no live footage · `mixed_live_and_graphic` real footage with designed graphic slides · `mixed_UGC_and_screen` UGC footage with app screen cutaways · `stock_footage_produced` stock clips with branded graphics or VO · `AI_generated_video` visibly AI-generated throughout · `documentary_cinematic` cinematic, intentional handheld, observational · `slideshow_static_frames` static images edited as video · `screencast_tutorial` screen recording with cursor or taps, tutorial style · `talking_head_produced` a person on camera, professionally lit and directed · `animated_explainer` fully animated characters or scenes.

**`video_subject`** (the primary narrative subject across the video): `presenter_talking_head` faces camera throughout, direct address · `presenter_with_product` holds or demonstrates the product · `presenter_lifestyle_scene` in context, product integrated naturally · `hands_only_POV` hands throughout, no face · `app_screen_walkthrough` app UI is the main subject · `product_hero_rotating` the product alone, often moving or rotating · `before_after_sequence` two states in time order, not a split frame · `transformation_reveal` gradual reveal, payoff held late · `animated_character_scene` an illustrated or synthetic character drives it · `voiceover_with_broll` no dominant subject, VO over supporting footage · `infographic_sequence` designed full-screen slides · `social_feed_scroll` a simulated feed, comments or reactions · `multi_person_compilation` different people across scenes · `environment_establishing` a place is the subject · `text_kinetic_sequence` typography animation throughout · `reaction_overlay_scene` a person reacts to content shown at the same time.

**`format`** (duration bucket): `video_under_6s` bumper or loop · `video_6_15s` short, hook-only or awareness · `video_15_30s` standard short performance · `video_30_60s` room for demo or narrative · `video_over_60s` long story or deep demo.

**`offer_framing`**: `price_anchor` a high reference price makes the real one feel cheap · `free_trial` leads with a no-cost trial · `percentage_discount` · `dollar_discount` (a currency amount) · `BOGO` buy one get one · `limited_time_urgency` a restricted time window · `scarcity` limited quantity · `value_stack` many inclusions make the value feel large · `money_back_guarantee` · `free_shipping` · `bundle_deal` · `subscription_savings` recurring billing framed as cheaper · `no_offer_brand_only` no economic proposition · `comparison_pricing` a competitor's price next to own · `pay_what_you_want`.

**`cta_type`**: `learn_more` · `shop_now` · `try_free` · `get_started` (onboarding, apps, SaaS) · `download` · `sign_up` · `subscribe` · `buy_now` · `book_now` · `get_offer` · `claim_deal` · `see_more` · `send_message` · `watch_more` · `swipe_up` · `custom` any other CTA, its exact text in `cta_custom_text`.

**`cta_source`**: `on_screen_text` · `transcript` · `title` · `caption` · `body` · `description` · `inferred` (no explicit CTA, inferred from the landing intent).

**`emotional_tone`** (dominant register): `aspirational` an idealized future state · `fear_based` anxiety, threat, loss · `humorous_playful` · `educational_informative` calm, factual · `urgent_FOMO` act now or miss out · `calm_trust` measured, reassuring · `provocative_edgy` · `empathetic_relatable` mirrors the viewer's feelings without judgment · `luxurious_premium` · `nostalgic` · `inspirational_motivational` · `casual_conversational` a friendly message from a peer.

**`copy_structure`** (spoken and on-screen text across the video): `headline_only` one dominant message · `headline_plus_subtext` · `long_form_story` an extended narrative or monologue · `minimal_no_text` only a logo and brand mark · `bullet_benefits` features or benefits one after another · `story_arc_narrative` a mini story with beginning, middle, resolution · `question_answer` · `listicle_numbered` · `social_proof_quote` a user, expert or third-party quote as the main copy · `data_driven_stats` statistics as the main copy.

**`video_pacing`**: `single_shot` one take, no cuts · `slow_cinematic` long takes, few cuts · `medium` cuts every 3 to 5 s · `fast_cuts` cuts every 1 to 2 s · `rapid_montage` sub-second cuts.

**`audio_style`**: `dialogue` the person on screen speaks, lip sync · `voiceover` an off-camera voice, no lip sync · `music_only` · `silent` · `mixed` dialogue or VO with music under it.

**`social_proof_type`** (even as a secondary element): `none` · `user_quote` a quote from a real or simulated user, spoken or on screen · `star_rating` · `user_count` users, downloads, customers or reviews · `award` an award, badge, certification, App of the Year signal · `celebrity` a known figure, influencer or verified creator.

**`text_to_visual_ratio`**: `text_heavy` text dominates most frames · `balanced` · `visual_dominant` text is minimal (logo, short CTA or captions only) · `no_text`.

Plus: **`color_palette`** 2 to 3 dominant hex colors, most dominant first · **`has_human_face`** true if a face is visible in any frame · **`key_claims`** 2 to 5 items in the claim format · **`cta_custom_text`** required when `cta_type` is `custom`.

### Schema

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Video Ad Creative Analysis",
  "type": "object",
  "properties": {
    "visual_summary": { "type": "string" },
    "hook_type": { "type": "string", "enum": ["problem_solution","before_after","social_proof","UGC_testimonial","curiosity_gap","fear_urgency","question","statistic_claim","POV_first_person","tutorial_how_to","unboxing_reveal","comparison_vs","transformation","day_in_life","GRWM_get_ready","reaction","myth_busting","listicle","controversy_hot_take","authority_expert","emotional_story","product_demo","challenge"] },
    "hook_text": { "type": "string" },
    "hook_source": { "type": "string", "enum": ["on_screen_text","transcript","title","caption","body","description","inferred"] },
    "narrative_arc": { "type": "string", "enum": ["talking_head_direct","hook_demo_cta","hook_loop","problem_agitate_solve","listicle_sequential","multi_segment_compiled","transformation_reveal","testimonial_monologue","social_proof_compilation","unboxing_reveal","tutorial_step_by_step","comparison_walkthrough","educational_explainer","single_shot_loop","GRWM_routine","reaction_to_content"] },
    "presenter_type": { "type": "string", "enum": ["real_person_UGC","real_person_expert","real_person_lifestyle","celebrity_influencer","AI_avatar","animated_character","voiceover_only","hands_only_POV","none"] },
    "scene_structure": { "type": "string", "enum": ["single_continuous","two_scene_ab","hook_plus_demo","multi_segment_complex","looping_hook","rapid_montage","screen_only"] },
    "on_screen_text_style": { "type": "string", "enum": ["subtitle_captions","headline_overlays","kinetic_typography","app_ui_labels","infographic_labels","mixed_overlays","emoji_text_hybrid","none"] },
    "video_production": { "type": "string", "enum": ["UGC_handheld","studio_directed","screen_recording_live","app_mockup_animated","graphic_animation_only","mixed_live_and_graphic","mixed_UGC_and_screen","stock_footage_produced","AI_generated_video","documentary_cinematic","slideshow_static_frames","screencast_tutorial","talking_head_produced","animated_explainer"] },
    "video_subject": { "type": "string", "enum": ["presenter_talking_head","presenter_with_product","presenter_lifestyle_scene","hands_only_POV","app_screen_walkthrough","product_hero_rotating","before_after_sequence","transformation_reveal","animated_character_scene","voiceover_with_broll","infographic_sequence","social_feed_scroll","multi_person_compilation","environment_establishing","text_kinetic_sequence","reaction_overlay_scene"] },
    "format": { "type": "string", "enum": ["video_under_6s","video_6_15s","video_15_30s","video_30_60s","video_over_60s"] },
    "emotional_tone": { "type": "string", "enum": ["aspirational","fear_based","humorous_playful","educational_informative","urgent_FOMO","calm_trust","provocative_edgy","empathetic_relatable","luxurious_premium","nostalgic","inspirational_motivational","casual_conversational"] },
    "copy_structure": { "type": "string", "enum": ["headline_only","headline_plus_subtext","long_form_story","minimal_no_text","bullet_benefits","story_arc_narrative","question_answer","listicle_numbered","social_proof_quote","data_driven_stats"] },
    "offer_framing": { "type": "string", "enum": ["price_anchor","free_trial","percentage_discount","dollar_discount","BOGO","limited_time_urgency","scarcity","value_stack","money_back_guarantee","free_shipping","bundle_deal","subscription_savings","no_offer_brand_only","comparison_pricing","pay_what_you_want"] },
    "cta_type": { "type": "string", "enum": ["learn_more","shop_now","try_free","get_started","download","sign_up","subscribe","buy_now","book_now","get_offer","claim_deal","see_more","send_message","watch_more","swipe_up","custom"] },
    "cta_custom_text": { "type": "string" },
    "cta_source": { "type": "string", "enum": ["on_screen_text","transcript","title","caption","body","description","inferred"] },
    "key_claims": { "type": "array", "items": { "type": "string" }, "minItems": 2, "maxItems": 5 },
    "social_proof_type": { "type": "string", "enum": ["none","user_quote","star_rating","user_count","award","celebrity"] },
    "color_palette": { "type": "array", "items": { "type": "string", "pattern": "^#[0-9A-Fa-f]{6}$" }, "minItems": 2, "maxItems": 3 },
    "has_human_face": { "type": "boolean" },
    "text_to_visual_ratio": { "type": "string", "enum": ["text_heavy","balanced","visual_dominant","no_text"] },
    "video_pacing": { "type": "string", "enum": ["single_shot","slow_cinematic","medium","fast_cuts","rapid_montage"] },
    "audio_style": { "type": "string", "enum": ["dialogue","voiceover","music_only","silent","mixed"] }
  },
  "required": ["visual_summary","hook_type","hook_text","hook_source","narrative_arc","presenter_type","scene_structure","on_screen_text_style","video_production","video_subject","format","emotional_tone","copy_structure","offer_framing","cta_type","cta_source","key_claims","social_proof_type","has_human_face","text_to_visual_ratio","video_pacing","audio_style"],
  "if": { "properties": { "cta_type": { "const": "custom" } }, "required": ["cta_type"] },
  "then": { "required": ["cta_custom_text"] },
  "additionalProperties": false
}
```

(Full field descriptions are in the taxonomy above; the team's original spec also carries a worked example for a coin-scanner app: hands-only POV, curiosity gap hook "Can I buy a house? 🏠🤔", multi-segment compiled arc, mixed live and graphic production.)

---

## Reference L. Static ad creative analysis standard

Moved to `lyra-copy-competitor-static` (Reference L there, the team's full static standard with field descriptions and the worked example).
