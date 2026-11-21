---
name: lyra-ugc-video
description: "Use when the user wants a UGC-style video ad for an app, e.g. \"a UGC video\", \"UGC ad for my app\", \"creator / influencer style\", \"talking head\", \"testimonial\", \"storytime\", \"car vlog\", \"a skit\", \"street interview\", \"day in my life\", \"honest review\", or a Lyra UGC template. A realistic person talks to the phone camera about the audience's pain, built in Lyra."
---

# lyra-ugc-video

This skill makes UGC style video ads for mobile apps; their goal is installs, trials and subscriptions. It casts a believable person from the Brand Kit's audience, puts them where the pain actually happens, gives them a voice that fits, and writes what they say from the audience's real problem. Then builds and runs the video in Lyra.

**Canvas layout → `lyra-workflow-layout`.** Every workflow this skill builds or changes is laid out by `lyra-workflow-layout`: sections in reading order with a STEP note above each one, the team's color code, clear node labels and the final check. The layout lines in this file only say which sections this creative needs.

**App ads first.** Every decision in this skill serves one goal: the right person installs the app and keeps using it. UGC here is not brand content, a creator portfolio or product UGC for a physical item; it is a performance ad for an app, judged by installs, trials and payers. When a general UGC habit (unboxing, "shop now", a product held up to the camera, an aesthetic mood film) doesn't move an app install, drop it or translate it into its app version (see "UGC for app ads").

**This is a way of thinking, not a script.** The rules below are defaults and good practice. Use judgment: when a different person, place, format or order serves the idea better, do it and say why in one line. Only a few things are fixed: truth (no invented claims, reviews or numbers; an AI person is never a real customer), the Brand Kit's facts, Lyra's technical limits, and the user's explicit choices.

**Base skill first.** Everything not written here follows `lyra-video-ad-generation`: the 8 steps, instruction order, app card, plan table and stages, run options with credits, run and report, prompt rules, models (Reference A), audio (C), app UI (D), consistency (E), prompt craft (F), errors (G), de-slop (H), Brand Kit (I), Meta app ads (J). This file only adds what is specific to UGC. If the two disagree, the user wins, then this file, then the base skill.

**Hooks come from `lyra-video-hooks`, and often.** UGC lives or dies in the first 1 to 3 s, so most UGC ads open with a hook built by the hook skill (its pain map, hook kinds, hook base, writing rules). Use it by default, skip it only for the cases in "Hooks in UGC" below. This skill owns the person, the place, the voice, the speech and the body of the video; the hook skill owns the opening.

**Everything comes from the Brand Kit.** The person, the pain, the speech, the feature, the offer, the tone and the look of every UGC video are built from the app's Brand Kit, never from imagination. Source order (base Reference I): the user's words in this chat → the Brand Kit given in the chat → the Brand Kit connected to the workspace or workflow (`list_brand_kits`; one kit → "Make this for {kit name}?", several → ask which) → none: ask once to send it or to connect one of the workspace's kits. The user's request always wins; the Brand Kit fills everything they didn't say; a conflict is named in one line. Missing facts are asked for or written as hypotheses to confirm, never invented. See "What UGC takes from the Brand Kit" in Step 1.

**Model.** UGC and real people talking: **always Seedance 2.5**, references only, 720p by default (1080p on the user's choice), sound on. Never Kling or Veo for UGC; if the user wants cheaper, say faces and speech will lose quality and let them decide (base Reference A).

---

## How to think about UGC

**What it is.** A video that looks like a real person filmed it on their phone and posted it, not like an ad. The viewer should feel they are watching someone like them, or someone they trust, talk about a problem they know. It works because it does not trigger the skip reflex: native, phone-real, personal.

**Four pillars, all built from the audience's pain:**

| Pillar | Question it answers | Comes from |
|---|---|---|
| **Person** (persona) | Who is talking, and why would this viewer listen to them? | the audience segment in the Brand Kit |
| **Place** (setting) | Where and when does the pain happen? | the daily moment in the pain map |
| **Voice** | How does this person sound? | the persona, the market, the tone of voice |
| **Speech** | What do they say, in what words? | the pain, the customer's own words, one real feature |

All four must tell one story. A tired student at 2 am in bed, speaking quietly and a bit hoarse, saying the thing every night owl thinks: that is one idea. A glossy model in a studio saying "this app changed my life" is four mismatched ideas.

**Final test for every UGC concept:** would a real person from this audience post this? Would the right viewer recognise their own problem in 3 s? Is everything the person says true for this app?

**Principles:**

- Problem first, by default. Usually the person starts from the pain, in the audience's words, and the app arrives as the thing that fixed it. This is a default, not a hard rule: naming or showing the app early (app first) is a valid choice when it fits the concept, the audience or the test (see Speech).
- Mirror the viewer. The person looks, lives and talks like the audience (or like the person they trust). Casting is targeting.
- One person, one problem, one feature, one result. No feature lists.
- Talk, don't pitch. Contractions, short sentences, a pause, a half laugh. Copywriting voice kills UGC.
- Specific beats vague: an exact moment ("2 am", "the 15th of the month"), an exact thing ("I opened my banking app and just closed it again").
- Natural beats perfect: casual framing, real rooms, real skin, small imperfections convert better than polish.
- Show, if you talk about it: the pain on the face or in the place; the app only from real screenshots.

**What feels stale in 2026 (avoid unless twisted):** ring-light testimonial · "I've been using this app for a few weeks and…" · forced enthusiasm ("obsessed", "game changer", "life changing") · scripted influencer read · walkthrough with a fake smile · model-perfect actor · a logo intro · "Hey guys". Testimonial-style UGC still takes a big share of budgets but has weakened on cost per trial; tutorial, review and story formats tend to do better for apps.

---

## UGC for app ads: what's different

An app is invisible software on a phone. Product UGC sells something you can hold, open and apply; app UGC has to make an invisible product felt and believed in a few seconds. That changes the job of every pillar.

**Make the app visible, in this order of strength:**

1. **The change on the person.** Stressed → relieved, lost → in control, bored → hooked. The emotional shift is the demo when no screen is shown (the Lyra "Talking head with phone" template works only on this contrast).
2. **The result in life.** What is different after using the app: she sleeps, the fridge is planned, the money is left on the 25th, he speaks to the waiter in Spanish. Show it in the place.
3. **The phone moment.** A thumb taps, she turns the phone a little, she looks at it and reacts; the screen faces her, not us.
4. **One real screen.** The "aha" screen from the user's screenshot, as a short UI insert (base Reference D). Never invented UI, never the full walkthrough.

**App translations of general UGC moves:**

| General UGC | App ad version |
|---|---|
| Unboxing, first impression | **First try:** "I downloaded it last night, ok let's see", the first session, her honest reaction |
| Product demonstration | **One feature, one screen moment**, or the result it gives; ~4 s of real UI at most |
| Before and after (body, skin) | **Before and after of the situation** (the chaos, the bill, the night); never the body for health apps |
| Testimonial | **Creative first-person scene** (never presented as a real user) or real reviews as text |
| "Shop now", "link in bio" | **Install / trial CTA** with the real offer: "it's free for seven days", said like a tip |
| Product held to camera | **The phone held a little toward camera**, screen hidden or a real screenshot |
| Aesthetic product video | Only for premium positioning, and still with a person and a pain |

**The one feature.** Each video sells one job the app does for this person, tied to one pain. A second feature is a second video.

**The ad promise matches the store page.** What the person says and shows (the feature, the offer, the look of the screen) must be what the viewer finds on the App Store or Google Play page and in the first session. Overpromising raises installs and kills trial-to-paid and retention.

**Psychological triggers (pick 2 to 3 per video, not all):**

| Trigger | In an app UGC ad |
|---|---|
| Recognition | the pain moment the viewer lives (2 am, the 15th, the empty fridge) |
| Relief / emotion | the visible shift on the person's face |
| Curiosity | the hook opens a question the body answers |
| Simplicity | "five minutes", "one tap", one feature explained in one sentence |
| Demonstration | one real screen or the result in life, not claims |
| Identity | "someone who has money left", "someone who actually sleeps" |
| Trust | natural delivery, one honest drawback, specific and true details |
| Social proof | only real: real ratings, real review lines as text, real numbers from the Brand Kit |
| Urgency | only a real offer or deadline |

**Positioning sets the polish level.** Read the Brand Kit's positioning and pick one look per video, said in the plan: **raw UGC** (default: handheld, home, casual; most cold traffic) · **elevated UGC** (premium or wellness apps: cleaner rooms, nicer light, still a real person on a phone, still natural skin) · **stylized UGC** (a hook-led or format-hook ad: object POV, surreal fourth wall, from the hook skill). A strong test set for one concept is often the same idea in two of these looks.

**Category guide (starting points, not rules):**

| App category | Typical pain moment | Persona | Formats that fit | Careful with |
|---|---|---|---|---|
| Sleep, meditation, calm | night in bed, racing thoughts | Mirror, tired, quiet voice | storytime, ASMR, selfie in bed | health claims; no "cures insomnia" |
| Fitness, steps, workouts | skipped workout, no time, gym nerves | Mirror or friend a step ahead | walk and talk, mirror, routine, first try | no body before/after; no promised weight loss |
| Budgeting, banking, saving | end of month, a bill, the banking app closed again | Mirror, converted skeptic | car, honest review, storytime | no invented amounts or returns; finance rules |
| Language learning | a trip, a waiter, a work call | Mirror, traveller | walk and talk abroad, skit, street interview | no fluency promises in days |
| Dating, social | a bad date, ghosting, small talk | friends, two people | skit, podcast, interview | no real people or fake matches |
| Productivity, planning | chaos, missed deadline, 47 tabs | Mirror, busy parent, student | desk tripod, routine, hidden cam | no invented time saved |
| Photo, video, AI tools | an edit that took hours, a bad photo | creator-type friend | first try, reaction, tutorial | the output shown only from real results |
| Utilities (cleaner, VPN, caller ID, scanner) | a full phone, a spam call, a moment of risk | Mirror, parent | reaction, honest review, car | no fear-mongering, no fake alerts or system UI |
| Kids, family, education | homework fight, screen time, bedtime | parent | storytime, couch tripod, dialogue | no claims about children's results; no minors as the speaker |
| Health tracking, period, nutrition | an unclear symptom, a doctor visit, meal chaos | Mirror | storytime, routine | health claims only from the Brand Kit; no diagnosis talk |

---

## Step 1 additions: audience, pain and persona first

1. **Brand Kit and pain map.** Find and read the Brand Kit (base Reference I). Build the **pain map** exactly as in `lyra-video-hooks` Step 1 (audience, pains in their words, desires, objections, product truth). If a hook round already made one for this app, reuse it. Pains missing or vague → 3 to 5 pain hypotheses in the audience's words, ask to confirm, and keep moving in the same message.
   **What UGC takes from the Brand Kit:**

   | Brand Kit field | Used for in UGC |
   |---|---|
   | Audience, segments, their daily life | the persona (archetype, age, look, market), the pain moment, the place |
   | Pains, problems, customer words, reviews | the hook line, the speech, the "old way" beat |
   | Desires, outcomes | the result beat, the identity trigger |
   | Objections | the converted skeptic, honest review, objection-first spines |
   | Product, features, value proposition | the one feature, the discovery and demonstration beats |
   | Approved claims, proof, numbers | the only claims and proof the person may say or a caption may show |
   | Offer, CTA | the soft CTA and its caption |
   | Tone of voice | how the persona talks (word choice, humour, energy) and the voice anchor |
   | Positioning (mass, premium, wellness, playful) | the polish level: raw, elevated or stylized UGC |
   | Brand colors | subtle accents only (a mug, a hoodie, the room's light); UGC never looks branded |
   | Markets, languages | the persona's market, the spoken language and accent |
   | Must include / must exclude, forbidden claims | hard rules for every prompt and line |
   | Assets (logo, screenshots) | logo on the end card; screenshots for the phone image and UI insert |

2. **The pain moment.** For the pain you lead with, write one line: who, where, when, what they do, what they feel. Example: "Student, 21, in bed at 2 am, scrolling, can't switch off, annoyed at herself." This line picks the place and the format.
3. **Customer words.** Store page, reviews, comments, support messages (hooks skill Step 1a). Short phrases only. They feed the speech, never as a copied review.
4. **Intake quiz** (base Step 1: one message, multiple choice, options from the Brand Kit, the recommended option first, 4–8 questions; skip what the task or the kit already answers), with these questions plus the base quiz questions that apply:
   - Which pain or segment to lead with (offer your recommendation).
   - Format, or "you decide" (default: you decide from the pain moment, see the format library).
   - Persona preferences: age, gender, look, market; one persona or two for an A/B test.
   - Language and market (the person speaks this language natively in the clip).
   - Screenshots, if the app should be seen (screenshots only, never a screen recording).
   - The store link (to match the ad promise and read the reviews), if not in the Brand Kit.
   - Approved and forbidden claims, mandatory disclaimers or phrases, if the Brand Kit doesn't say (health, finance, kids apps above all).
   - Raw or elevated look, if the Brand Kit's positioning isn't clear.
   - Is AI-generated content allowed for this brand, and does the client have a disclosure rule.
   - How many videos (default 1 concept; 2 personas if they want a test).

**Defaults (state, don't ask):** cold traffic · Reels / TikTok · 9:16 · **15 s** (10 to 30) · English · one persona · native speech in the clip (no separate voiceover) · no music for talking head formats, light instrumental music for vlog and POV (always its own node in the Video Editor, never inside the clip) · captions: ask the user in the approval message (if yes: all speech, added in the Video Editor; size 80, at 75% of the height, under the face: `lyra-video-editor` → Captions) · phone screen hidden unless there are screenshots · Seedance 2.5, 720p (1080p on the user's choice), sound on, duration adaptive · Nano Banana Pro for every image, 9:16, 2K (4K for close-up selfies), character count 2 · CTA spoken + caption, logo end card optional.

**Recommended first run:** A. Character images (the person decides the whole video; images are cheap).

## Step 2 addition: the UGC concept

The concept the user approves (base Step 2) has, per video: **pain moment** (one line) · **persona** (character card, or 2 to 3 persona options to pick from) · **place** · **camera setup** (handheld selfie, walk and talk, car, propped, tripod, mirror, someone else films) · **format** (and the template, if one fits) · **hook** (3 to 5 options from `lyra-video-hooks` with one recommended, or "no hook skill: why") · **spine** with the spoken lines and word count · **clip plan** (one clip or several, B-roll, UI insert) · **music** yes/no.

> C1 · storytime · Mia, 21, student (Mirror) · bed at 2 am, phone light · handheld selfie lying on her side · hook H3 (combined): the phone slips and taps her nose, she winces, says "Two a.m. and my brain won't shut up." · spine: pain → tea, podcasts, counting sheep → Calmly five-minute wind-down → out before it ended → free, try tonight · 35 words, one clip ~15 s adaptive, one jump cut · no music, room tone · screen hidden (no screenshots yet).

**Persona options.** When the audience is broad or the user has no preference, write 2 to 3 short character cards (different archetype, age or look) and recommend one; the picked one, or two for an A/B, go into the build.

---

## Person: casting from the audience

**Who talks.** Pick the archetype from the audience and the pain, then make it specific:

| Archetype | The viewer thinks | Works best for |
|---|---|---|
| **Mirror** (default for cold traffic) | "that's me" | most apps; same age, life stage, situation, problem |
| **Friend who figured it out** | "she's like me, a few steps ahead" | habits, productivity, money, learning |
| **Converted skeptic** | "she doubted it too" | categories with trust issues, objection-led ads |
| **Insider** (works in the field, no claimed credentials) | "she knows how this works" | finance, learning, career; never a fake doctor, lawyer or advisor, no white coat or titles |
| **Two people** (friends, couple, coworkers, interviewer + stranger) | "that's a real conversation" | skits, street interview, social and dating apps |
| **Parent / partner / roommate** | "that's my house" | family, home, health habits, shared money |

**Character card.** Write it once, in the script text node, and repeat it word for word in every image and video prompt (it is the character anchor, base Reference E):

> Character: Mia · 21 · student · light brown skin, freckles, dark curly hair in a loose bun, a few strands falling · no makeup, slight dark circles · oversized grey hoodie, thin silver hoop earrings · energy: tired, dry humour, speaks quietly · voice: young woman, early 20s, soft American accent, slightly husky, relaxed pace, a little sleepy

**Realism rules for the person:**

- Real, not pretty: natural skin texture, visible pores, small asymmetries, real hair, everyday clothes from the audience's life. Attractive is fine; model-perfect reads as an ad.
- Age, look and style match the segment and the market (a Lisbon student, a Texas mom, a Tokyo office worker look and dress differently). Diverse casting across variants, never stereotypes.
- Expression fits the moment of the pain (tired, annoyed, embarrassed, relieved), not a constant smile.
- One person in focus; a second person only in two-person formats.
- Never a real person, celebrity, known creator or a lookalike; never a real creator's voice; no third-party brand clothing logos.
- An AI person is never presented as a real customer, a verified user or a real review. First-person stories are creative scenes.

**Images: Nano Banana Pro, high quality, phone-real.** Every UGC person, keyframe and moment image is made with **Nano Banana Pro** (`google/nano-banana-pro`), the finals model of the base skill (Reference A): it holds faces, skin, hands and real rooms best. Nano Banana 2 only for quick drafts, then the winner is rerun on Pro.

- **Settings:** aspect ratio **9:16** (the video's ratio, base Reference E) · resolution **2K** by default, **4K** for close-up selfies where skin and eyes fill the frame · count **2** for the character image (the user picks one), 1 for the rest. Read the values from `list_node_configs`.
- **High quality is not polish.** High resolution is there so the details survive into the video: visible pores, fine hair, fabric texture, the small objects of the room. The look stays phone-real (natural light, deep focus, no beauty filter, no editorial styling). Seedance 2.5 copies what the reference shows, so a plastic or blurry image becomes a plastic or blurry video.
- **Skin:** "natural skin texture, visible pores, fine lines, subtle redness, slight unevenness, a few blemishes, no makeup airbrushing, no beauty filter", sized to the persona (a tired student, a busy mom). Never "flawless", "perfect", "porcelain", "glowing".
- **Setting:** the real place of the pain moment with 2 to 3 lived-in details, motivated light, sharp readable background (see Place). Never an empty, minimalist or showroom room.
- **Check before any video** (stage 1 gate): does the skin look like a real person filmed on a phone, and does the room look lived in? If not, rerun the image (cheap) with a stronger realism line; never spend video credits on a plastic image.

**Two personas for an A/B test.** One script, two character cards (different age, look or archetype), same place, same speech; two character images, two clips, two videos. The persona is the hypothesis ("students trust a peer more than an older sister type").

---

## Place: where the pain happens

The setting is the pain moment from Step 1, not a nice location. The viewer should recognise their own room, car or desk.

- **Lived-in, specific:** 2 to 3 concrete details that tell the story (a half-drunk energy drink and a charger cable on the duvet; parking ticket on the dashboard; a sticky note wall). Not a showroom, not piles of decor.
- **Motivated light:** the light that is really there (phone light at night, window light in the morning, car daylight, office fluorescent, bathroom mirror light). No studio light, no ring light catchlight unless the format is a podcast.
- **Time of day matches the pain** (night for sleep, morning rush for habits, end of month for money).
- **Sound of the place:** room tone, traffic, fridge hum, street noise; Seedance makes it with sound on. It sells the realism.
- **The phone is the camera.** Every UGC prompt says who holds the phone and how (see "Camera setups" below). Framing for speech: medium close-up, face and mouth clearly visible, eye level or slightly above, subject in the central 65% of 9:16.
- **Phone optics, not cinema optics:** wide phone lens ("shot on a 24mm smartphone front camera"), **deep depth of field with a sharp, readable background** (portrait blur and creamy bokeh read as a camera, not a phone), small handheld micro-jitters and drift instead of gimbal moves, a little autoexposure shift when the light changes, a little noise in low light, no heavy grading.
- **Variety without losing the person:** the same face can appear in several UGC spots (selfie in bed, on the couch, in the car) for different videos; keep the character card and change only the place.
- **One place per video by default.** A second place only when the story needs it (problem at night → result in the morning), with the same person anchor.

---

## Camera setups: how the person films themselves

In real UGC the person films themselves: the phone is in their hand, or they put it down somewhere and talk to it. This is what makes a video read as a post, not an ad. Pick one setup per clip, write it into the image and the video prompt, and keep it through the clip.

| Setup | What it looks like | Feels like | Best for | Prompt cues | Watch out |
|---|---|---|---|---|---|
| **Handheld selfie, spontaneous** (a strong default) | phone in one hand at arm's length, front camera, slightly above eye level; she grabbed the phone because she had to tell you something right now | urgent, honest, "I need to tell you this" | pain callouts, confessions, "wait, why did no one tell me", reactions | "she holds the phone in one hand at arm's length and films herself with the front camera, handheld micro-jitters, the frame drifts a little as she talks, her arm and shoulder edge visible at the side" | the free hand does one simple gesture at most; the arm doesn't change length mid-clip |
| **Walk and talk** (very native) | handheld selfie while walking: street, park, office corridor, supermarket, campus; the background passes behind her | on the go, real life, a thought she had on the way | routines, commute, productivity, money, "on my way to…" moments | "she walks toward camera while filming herself, the phone bobbing slightly with each step, the street passing behind her, natural walking rhythm" | steady pace, one direction, no crowds crossing in front; one short sentence per beat |
| **Car** | phone in a dashboard or vent mount, or in her hand while **parked**; driver's seat, seatbelt, window light | "talking to you in my car", private, casual | commute pains, busy people, parents, money and planning apps | "phone in a dashboard mount facing her" or "parked, she holds the phone and films herself from the driver's seat, daylight through the side window" | never a phone held in hand while driving (unsafe and it reads badly); moving car = phone in a mount |
| **Propped phone** | she set the phone down herself and leaned it on something: a shelf, a stack of books, a cup, the kitchen counter, the bathroom sink; static frame, she steps or sits back into it | settled, honest, "let me explain" | storytime, honest review, routines, GRWM, cooking | "the phone is propped against a mug on the kitchen counter, static frame slightly below eye level, she leans in and talks to it, a bit off-center" | a static frame needs life in the person: small moves, leaning in, looking away and back |
| **Tripod / clamp by the bed, desk, floor** | phone on a small tripod or a clamp, she sits on the bed, the floor, at the desk; wider frame, more of the room | longer talk, "sit down, story time", a creator setup | storytime, tutorials, day in my life, podcast-lite | "filmed on a phone on a small tripod at the foot of the bed, static wide-ish frame, she sits cross-legged on the bed facing it" | wider frame = smaller face; keep the mouth readable (medium shot, not full body) for speech |
| **Mirror selfie** | she films her reflection, phone in hand in front of her chest or face; bedroom mirror, bathroom, gym, elevator | outfit, body, routine, "look at this" | GRWM, fitness, fashion, beauty, routines; short lines or no speech | "mirror selfie: she holds the phone in front of her chest, the phone's back visible in the reflection, we see her and the room in the mirror" | the phone must not cover the mouth when she talks; mirror logic (reversed text, a second reflection) breaks easily; keep the background simple; better for short lines or a visual hook than a long monologue |
| **Set-up moment** (an opening beat) | the clip starts as she places or props the phone, adjusts it, sits back and starts talking | real, "I'm just recording this quickly" | the first beat of a propped or tripod clip; a combined hook | "the video opens as she leans the phone against the books, adjusts it once, sits back and starts talking" | keep it under 1 s, then speech; it is the visual beat, not a scene |
| **Someone else films** | a friend, a partner, an interviewer, a hidden camera; she is filmed, not filming | social proof of a moment, "caught on camera" | skits, street interview, hidden cam, couples | "filmed handheld by a friend standing in front of her, the friend asks from behind the camera…" | the filmer is off-camera with their own voice (see Voice) |

**How to choose.** The setup follows the pain moment and the energy of the speech: a sudden thought → handheld selfie; a thought on the go → walk and talk or car; a calm story or review → propped phone or tripod; something to show on the body or the outfit → mirror; a social moment → someone else films. Different setups for different videos of the same persona are a cheap way to make variety (same face, same voice, a new setup and place).

**Rules for every setup:**

- Write the setup in the image prompt too, so the character image already shows it (arm at the edge of the frame, the angle from the mug, the mirror).
- The camera moves only as the setup allows: handheld = small jitters and drift, walking = a gentle bob, propped and tripod = static (the person moves, the camera doesn't), car mount = small road vibration.
- The phone screen faces her, not us, unless there is a real screenshot (base Reference D).
- One setup per clip. A change of setup is a cut, written as a new shot ("cut to: she has propped the phone on the shelf…").

---

## Voice: how the person sounds

Default: **native speech in Seedance 2.5.** The spoken lines go in the video prompt in quotes, the model makes the voice and the lip-sync together. No separate voiceover node.

- **Voice anchor.** Describe the voice once in the character card and repeat it word for word in every clip: gender, age, accent, pace, energy, texture ("young woman, early 20s, soft American accent, slightly husky, relaxed pace, a little sleepy"). It must fit the face, the age and the moment.
- **Language and accent explicit** for every market ("speaks in natural European Portuguese, Lisbon accent"). One language per clip. For another market: new clip with the line written in that language (and a persona from that market if the user wants), not dubbing.
- **Delivery through words and action, not adjectives:** a pause written as a comma or an ellipsis, a breath before the key line, a half laugh, looking away then back. Never stage directions in the quoted line.
- **Lines Lyra's own producers put in UGC video prompts** (keep them, they fix common failures): "She starts speaking from the very first second of the video." · "She speaks calmly with natural pauses between sentences. No rushed speech." · "No voiceover narration, no off-screen voice, no dubbed audio. Only her live in-camera speech is heard." (drop the middle part when the format has an off-camera voice, like an interviewer or the person filming) · roughly **three short sentences per 10 s**.
- **Off-camera voice.** Interview, hidden cam and "friend filming" formats have a second voice behind the phone. Give it its own short voice description and tie its line to it ("the person filming asks from behind the camera: '…'"); the on-screen person answers.
- **Same voice across clips.** Native voices can drift between clips. Prevent: one longer clip instead of several where possible (Seedance 2.5 goes to 30 s), same voice anchor, same model. If it drifts anyway, offer: regenerate the weaker clip, merge into one clip, or switch to an ElevenLabs voiceover as audio reference (base Reference C; the video is fitted to the track).
- **Fallback when exact wording or a fixed brand voice matters** (or the user brings a recording): ElevenLabs VO, then the voiceover as audio reference in Seedance 2.5. Say once what changes: steady voice and exact words, a little less natural acting.

---

## Speech: what the person says

Write the speech from the pain map and the customer's words. It goes into a user text node "UGC script" (base Part 2), with the lines per clip.

**Default spine (problem first), 15 s:**

| Beat | Time | What the person does | Example (fictional app Calmly) |
|---|---|---|---|
| **Hook: the pain** | 0 to 3 s | names the pain in the audience's words, already mid-thought; built with `lyra-video-hooks` (see Hooks in UGC) | "Two a.m. and my brain won't shut up." |
| **The old way** | 3 to 6 s | what they tried, why it failed, a feeling the viewer knows | "Tea, podcasts, counting sheep… nothing." |
| **Discovery** | 6 to 10 s | how they found the app, the one feature, what it does for them | "Then I found Calmly. Five minutes, lights off, timer on." |
| **Result** | 10 to 13 s | a specific, believable change | "I was out before it ended." |
| **Soft CTA** | 13 to 15 s | casual, like a tip to a friend; offer from the Brand Kit | "It's free. Try it tonight." |

(35 words: fits 15 s at a calm pace, ending about 1 s early.)

**30 s app ad spine** (when the user wants 30 s, or the feature needs showing): hook (0 to 3 s) → pain and context (3 to 8 s) → discovery, the app named (8 to 12 s) → **demonstration**: one feature, one phone moment or real screen (12 to 18 s) → **benefit**, the specific reason it helps (18 to 23 s) → **payoff**, the result in life on the person (23 to 27 s) → CTA (27 to 30 s). About 70 words; usually one Seedance 2.5 clip of up to 30 s plus a UI insert.

Other spines when they fit better (say why in the plan): **first try** (she opens the app for the first time on camera and reacts honestly; the app version of unboxing) · **old way vs app** (a comparison: what she used to do vs what she does now) · **app first** (the person names or shows the app by second 2 to 3, then the pain it solved; a good A/B against problem first, often more clicks for utility apps) · **honest review** (what I expected, one small real drawback, why I still keep it; strong for warm traffic and skeptical audiences) · **storytime** (a short story with a turn, the app is the turn) · **objection first** ("I thought budgeting apps were pointless") · **tutorial / how I do it** (method first, the app named later; often higher intent) · **day in my life** (the app appears naturally in the routine) · **interview** (question → answer with the pain → the app) · **skit** (one person has the pain, the other has the fix).

**Speech rules:**

- **First person, spoken, simple.** Contractions, short sentences, everyday words, about a 5th grade reading level. Read it aloud: if it sounds like an ad, rewrite.
- **Start on the pain or the key word.** No "So", "Okay", "Hey guys". **When the app is named is a choice of the concept, not a rule:** problem first by default; app first (the app in the first seconds) when the hook is the app itself, the audience already knows the category, the user asks for it, or it is the A/B test. Say in the plan which one and why.
- **One idea per sentence, one short sentence per 3 to 5 s of clip.** Long, multi-clause lines break lip-sync.
- **Word budget:** about 2.5 words per second for a calm talker, 3.0 for energetic, 2.0 for slow and emotional, and the speech ends about 1 s before the clip ends. 15 s ≈ 30 to 35 words. Count them.
- **Numbers and abbreviations as spoken** ("two a.m.", "fifty euros"); spell the app name as it's pronounced if it's unusual, and check it in the result.
- **Natural imperfections, sparingly:** one pause, one self-correction or half laugh per video. Not a stack of "um".
- **Claims only from the Brand Kit or the user.** No invented numbers, durations of use, ratings or results. "Three nights in a row" only if it's a plausible creative scene, never as proof; no health, money or body results the app can't stand behind; no body before/after for health apps.
- **The CTA is soft and concrete:** the real offer ("it's free for seven days"), said like a tip. Same words as the CTA caption.
- **Echo, don't contradict:** captions and on-screen text repeat the spoken words.

**Checks for every script:** tied to one pain from the pain map · sounds like this persona, not a copywriter · specific to this app and moment (if it could sell a hundred apps, rewrite) · true · counted and fits the clip minus 1 s · the hook works muted with its caption.

---

## Hooks in UGC (use `lyra-video-hooks` often)

The hook beat of the spine (0 to 3 s) is where UGC ads win or lose. A selfie of someone starting to talk is the most common opening in the feed, so it needs a reason to stop: a sharper pain line, a physical beat, an unusual first frame. That is what the hook skill is for. **Read `lyra-video-hooks` and use it for the opening in most UGC ads.** It is a strong default, not a rule.

**Use the hook skill when** (most cases):

- cold traffic, or the user didn't say;
- the video is for a test (almost every paid ad);
- the format opens on a person just talking (selfie, honest review, car vlog, podcast): it needs a visual beat or a sharper line;
- the user asks for variants, a stronger start, or the hook rate is low;
- a UGC winner is fatiguing: keep the body, new hooks (hook multiplier, mode A of the hook skill).

**Skip it, or keep it light, when:**

- the user gives their own opening line or first scene (use it as is, check it against the hook skill's line checks once);
- the format's calm opening is the concept (ASMR, storytime whisper, calm contrast) and a hard interrupt would break it;
- a Lyra template already has its hook built in (Fridge Camera, Blinds, Hook door, Balcony, Trunk POV): adapt that hook, don't add a second one;
- warm retargeting where the offer opens the ad;
- one quick video for a look, not a test.

Say in the plan which way you went and why, in one line.

**How the two skills work together:**

1. **One pain map.** Build it once (hook skill Step 1) and use it for both the hook and the speech.
2. **Hook options in the concept.** For one UGC video, write 3 to 5 hook options from the hook base (not the full bank of 12 to 15) in the concept step, each one line with its kind and the persona's spoken line; recommend one. For a test, or when the user asks, write the full hook bank and build N hooks on one UGC body (hook skill, mode A or B).
3. **Hook kinds that fit UGC best:** **combined** (a small physical beat at frame 0, then the persona says the pain line: a clap, a phone flipped toward the lens, a sigh into the pillow, a door opened) · **verbal** (pain callout, POV, confession, storytime cold open, objection first, mistake, "people talking about the prospect") · **format hooks** (comment reply, hidden cam, street interview question, object POV) · **visual** only when the pain can be seen at once. The awareness table of the hook skill picks the kind for the audience.
4. **Same person, same voice, same place.** The hook is played by the UGC persona with the same character card and voice anchor, so the hook and the body cut together. A hook in a different spot (fridge, trunk, balcony) still uses the same persona reference; the body follows right after.
5. **Where the hook lives in the graph.** Spoken or combined hook in the same place → the first beat of the main clip (the opening action and the line first in the prompt; "starts speaking from the very first second"). Visual or format hook in another spot, or N hooks for a test → its own 4 to 5 s clip, trimmed to 1.5 to 3 s, cut into the shared body in the Video Editor (hook skill: cut point, end state).
6. **The speech continues the hook.** The second line answers or deepens the hook, never repeats it; if the hook opens a loop or promises something, the body pays it off.
7. **Caption on frame 1.** 2 to 6 words echoing the hook line, marked for post (hook skill rules).

**Hook naming:** add the hook code to the final's name: `B2-A:CantSwitchOff-F:UGC-Storytime-P1-C1H3`.

---

## Format library

A reference, not a menu. Pick from the pain moment; combine and adapt.

| Format | What it looks like | Pick it when | Lyra templates |
|---|---|---|---|
| **Selfie talking head** | front camera, arm's length, talking like on FaceTime with a friend | the pain is a feeling or a thought; the default | Talking head with phone, Mini Girl on Phone (stylized) |
| **Vlog in motion** | walk and talk selfie, car (phone in a mount, or in hand while parked), skating, commuting (see Camera setups) | the pain lives in a routine or on the go | Car Vlog, Skateboarding App Discovery Vlog, Female Street Promotion |
| **Storytime / confession** | lying in bed, on the couch, on the floor; quiet, honest, personal | the pain is private or a bit embarrassing (sleep, money, loneliness, habits) | Life Transformation, Sofa |
| **GRWM / routine** | getting ready, cooking, tidying, talking over the shoulder | the app fits a daily routine (habits, wellness, planning) | none (build from scratch) |
| **Day in my life POV** | short handheld moments of a day, the app in one natural moment | lowest ad feel; the app is part of life | none (build from scratch) |
| **Honest review / reaction** | sitting at a desk or in the car, "ok, real review", one small drawback | skeptical audience, warm traffic, competitive category | none (build from scratch) |
| **Street interview** | handheld, a mic in frame, a quick question, a stranger answers with the pain and the app | broad consumer apps; recognisable question | Interview, Interview POV |
| **Skit / dialogue** | two people: a friend catches the other, a coworker asks "what are you doing?" | social, dating, productivity, shared pain | Hidden Cam, Stream, Podcast App Discovery |
| **Podcast / insider clip** | two mics or one host, studio-ish room, a confident opinion | trust-heavy apps (finance, learning, career) | Podcast, App Presentation |
| **First try / first open** | "ok, I just downloaded this, let's see", first session on camera, honest reaction | new or surprising apps, AI tools, games-like apps; the app version of unboxing | none (build from scratch) |
| **Old way vs app** | she shows how she used to do it (notes, ten alarms, spreadsheets), then how she does it now | utilities, productivity, finance, learning | none (build from scratch) |
| **VO over UGC moments** | silent handheld moments of her day, her own voice telling the story over them | when lip-sync is hard (walking fast, mirror) or for a calm diary feel | none (VO as audio reference or composed in the Video Editor) |
| **ASMR / whisper** | close mic, soft voice, calm room | calm, sleep, meditation, self-care apps | ASMR, Microphone UGC |
| **Hook-led UGC** | object POV, door, blinds, balcony, fridge, trunk, then the person talks | the first second needs a visual stop | Fridge Camera, Trunk POV, Blinds, Hook door, Balcony (see lyra-video-hooks) |

**Pain → format, in short:** a feeling → selfie or storytime · a moment in the day → vlog, routine or POV in that place · a doubt → honest review or objection first · a social pain → skit or interview · a trust problem → insider or podcast · a calm category → ASMR.

**Lyra UGC templates.** `list_templates` with tags ["UGC", "Talking Head"]; offer up to 3 that fit (title + one line why + preview link); always re-check the list. Picked → `get_template`, `use_template`, then adapt as in `lyra-video-hooks` Step 1b, plus for UGC:

- The video model becomes **Seedance 2.5**, references only, 720p by default (1080p on the user's choice), sound on (several templates use Kling 3.0 or Seedance 2.0 at other settings); say it once and follow the user's choice.
- Rewrite the script node with this skill's speech (problem first, the persona's words), replace every "[App Name]" and "[main benefit]".
- Replace the template's persona with a character card from the audience; remove "flawless skin", "Vogue editorial", "4K" style tags (UGC is phone-real).
- Remove on-screen text, stickers and "link in bio" from prompts; captions go in the Video Editor.
- The image and character nodes keep their prompts' idea; switch to Nano Banana Pro for finals unless the user wants the template's model.

---

## Best way to build it

The user's explicit choices override any row. Models and prices: base Reference A.

| If the video is | Best approach (graph) | Models |
|---|---|---|
| **One person, one place, ≤15 s** (default) | UGC script (text) → character image in the setting (count 2, user picks) → **one clip**, adaptive duration, the speech in quotes, 1 to 2 jump cuts written as "cut to" inside the clip → Video Editor (captions, optional end card) | nano-banana-pro · seedance-2.5 |
| One person, 15 to 30 s | as default, one clip up to 30 s adaptive; or 2 clips cut on a natural pause, same references, same voice anchor | seedance-2.5 |
| Two places or several moments (problem → result, day in my life) | character image → one image per moment made **from the character image** ("Change the setup and her pose: she is now… Keep the same woman, face, hair") with the character as input, so identity carries over → one clip per moment, or one multi-shot clip with all moment images as references ([Image1] scene 1, [Image2] scene 2…) → Video Editor | nano-banana-pro · seedance-2.5 |
| Hidden cam, interview, friend filming | character image (the person on screen; the filmer stays off-camera) → clip with the off-camera question and the on-screen answer, each tied to its voice | nano-banana-pro · seedance-2.5 |
| The user already has an app packshot or app video | as default; their file appended in the Video Editor as the last 2 to 4 s (don't ask for a screen recording; use it only if they bring one) | video_composer |
| Shows the app | as default + phone image (character holds the phone, the user's screenshot) → short UI insert clip laid over in the Video Editor, or the phone image as a reference in the main clip (base Reference D) | nano-banana-pro · seedance-2.5 (UI insert: seedance-2.0, frame) |
| B-roll moments (hands, the pain object, the room) | 1 to 2 short clips (4 to 5 s, trimmed to 1 to 2 s) from keyframes with the same anchors, cut over the talking head in the Video Editor while the voice continues | seedance-2.5 |
| Two people (skit, interview, couple) | two character images → one shared keyframe of both in the place → clip with each line tied to its speaker by [ImageN] and the other person still; if the wrong person talks, one clip per line joined in the Video Editor | nano-banana-pro · seedance-2.5 |
| Two personas for A/B | one script → two character images → two clips → two Video Editors, everything else identical | nano-banana-pro · seedance-2.5 |
| Several openings on one body | build the body here, hooks from `lyra-video-hooks` (mode A) | as the hooks skill |
| Another language or market | same structure; the speech rewritten in that language (not translated word by word), the voice anchor with that accent; new clip | seedance-2.5 |
| Exact words or a fixed voice needed, or the user's own recording | VO (ElevenLabs, or the user's file uploaded) → audio reference in the Seedance 2.5 clip | elevenlabs/v3 · seedance-2.5 |
| Lyra UGC template picked | use_template → adapt (Format library) → upgraded settings | as the template, upgraded |
| Many personas or formats, tight budget | character images for all, clips only for the 1 to 2 the user picks | seedance-2.5 |

**Clip plan.** UGC lives on jump cuts: they hide small drift, keep the rhythm and look native. Write them in the script (where the cut is, what changes: framing slightly closer, a new sentence). A new stimulus every 2 to 4 s (a cut, a B-roll, a gesture). Seedance's minimum is 4 s: short beats are trimmed in the Video Editor.

**Music.** **Never inside the clip:** every UGC clip prompt says "Only her live in-camera speech and the room's natural sounds; no music, no background music, no soundtrack, no score", because music baked under the live voice can't be removed (base Reference C). Talking head, storytime, honest review, ASMR: usually no music at all, the room tone carries it. Vlog, POV, routine: light instrumental (lo-fi, soft pop beat), barely under the live voice (Lyra's UGC templates sit at about 0.05 to 0.1 track volume under in-camera speech; up to about 0.25 only under a clean studio voiceover), length = video + ~5 s, instrumental only (base Reference C).

**Video Editor.** One `video_composer` per final: hook clip (if separate) → main clip(s) → B-roll and UI inserts on a layer above → optional packshot or end card (logo, 1 to 1.5 s, or none: many UGC ads end on the person). Captions only if the user said yes (asked in the approval message): all speech, word by word, in one place, by the base rule (`lyra-video-editor` → Captions): size 80, at 75% of the height (y = 1440 on 1080×1920), never over the face. The editor makes them from the speech (caption track): set the size and position yourself once the track exists; the user checks the words and the app name; tell the user what to check. Keep the clip's own sound (it is the voice); mute only clashing B-roll sound.

**Layout.** Section "Script" (UGC script, character card), Section per persona (character image, keyframes, clips), Section "Final" (Video Editor). Labels: "Character: Mia", "Mia: bed 2 am (clip)", "B-roll: phone on duvet", "Final: P1 Mia · storytime sleep".

## Run options for UGC

**Run order, not a menu** (base Step 6): after the user's yes, run all of it in this order without offering options. Stop between stages (the look first, then the rest) only when the user asked for it, or when the plan is expensive and that was said in the approval message.

As in the base skill, credits read from the nodes, per option. **A. Character images (recommended):** every persona image (count 2) and keyframes · **B. Clips** for the persona the user picked · **C. Everything** → the Video Editor. When a character image has several results, the user selects one in Lyra before the clips (references pin to the selected result).

---

## Prompt rules (UGC)

| Node | Write | Avoid |
|---|---|---|
| UGC script (text node) | character card (with voice anchor), pain moment, place, format, spine with the lines per clip, word count per clip, cuts, B-roll, captions marked for post, CTA | ad copy; claims not in the Brand Kit |
| Character image | "UGC phone photo" → the character card word for word → in the place, mid-moment (the expression of the pain) → phone framing ("shot on a 24mm smartphone front camera", selfie at arm's length, off-center, candid) → motivated light → deep depth of field, sharp background → 2 to 3 lived-in details → "natural skin texture, visible pores, subtle asymmetry, flyaway hair, no beauty filter, no makeup airbrushing, casual, unpolished" → exclusions | "flawless", "perfect skin", "Vogue", "editorial", "luxury", "8K", "HDR", studio light, portrait bokeh, minimalist or empty background; text; logos; a visible phone screen without a screenshot |
| Keyframe (second place, two people) | the same card word for word, the new place, who is where, the moment it starts | re-inventing the person; different light logic |
| Video clip with speech | roles first ("[Image1] is Mia: face, hair, hoodie, her bedroom at night") → format and camera ("UGC selfie video, phone front camera at arm's length, handheld micro-jitters") → "starts speaking from the very first second" → action before each line → the lines in quotes, tied to the speaker → natural pauses, no rushed speech → voice anchor and language → "only her live in-camera speech" → cuts as "cut to" → room sound and action sounds, then "no music, no background music, no soundtrack, no score" → end state → short "Avoid" line | the full look re-described (the reference carries it; a short identity line is enough); stage directions inside quotes; more than one sentence per 3 to 5 s; on-screen text |
| Dialogue clip | each line after "[Image1] (Mia) says:" or "[Image2] (Leo) says:", the listener's reaction without speaking ("Leo listens, only Mia's mouth moves") | two people talking over each other; lines without a speaker |
| B-roll clip | one concrete action of hands or an object, same anchors, no speech, 4 to 5 s | faces (drift); a second person |

**Pattern: video clip with speech (Seedance 2.5, references).**

> [Image1] is Mia: her face, curly hair in a loose bun, grey hoodie, and her dark bedroom at night. UGC selfie video, shot on a 24mm phone front camera held at arm's length, handheld micro-jitters, deep focus, phone light on her face, warm lamp in the background. She starts speaking from the very first second. Mia lies on her side in bed, the phone slips and taps her nose, she winces, looks straight into the lens, tired but amused, and says: "Two a.m. and my brain won't shut up." She rolls onto her back, sighs, and says: "Tea, podcasts, counting sheep… nothing." Cut to: a little closer, she lifts the phone, and says: "Then I found Calmly. Five minutes, lights off, timer on." She smiles softly and says: "I was out before it ended. It's free. Try it tonight." Natural pauses between sentences, no rushed speech. Voice: young woman, early 20s, soft American accent, slightly husky, relaxed pace, a little sleepy. Only her live in-camera speech is heard, no voiceover. Quiet room tone, faint street noise, no music, no background music, no soundtrack, no score. Ends on her holding eye contact, a small smile. Avoid: background music, text, captions, beauty filter, studio lighting, identity drift, warped hands, visible phone screen.

(Hook H3 from the concept as the first beat: the phone tap is the physical interrupt, the line is the pain. 35 spoken words, about 14 s at a calm pace, in an adaptive clip that should land near 15 s; check the real length and trim only the silence after the last word. The app's real screen is shown, if at all, as a UI insert.)

**UGC prompt checklist** (what every image and video prompt specifies, when it matters for the shot): objective (app ad, which beat) · the app's role (hidden phone, phone moment, real screenshot) · person (the character card) · action (one clear action, the phone interaction) · setting (the pain moment, 2 to 3 details) · camera setup (who holds the phone, how it moves) · shot size and framing · light (motivated source) · texture (skin, fabric, room) · mood (the emotion at this beat) · format (9:16, duration in the node settings, not in prose) · constraints (what must not change, the artifacts to avoid).

## De-slop for UGC

Base Reference H, plus what breaks UGC in particular:

- **Too polished:** studio light, perfect teeth and skin, beauty filter, cinematic shallow depth of field, color grading, a camera that floats. UGC = phone camera: autoexposure, slight wobble, a little noise in low light, imperfect framing.
- **Overacting:** big hand gestures, constant smile, "excited" eyebrows, nodding on every word. Ask for small, real reactions: a look away, a pause, a half laugh.
- **Lip-sync slop:** mouth out of sync, the wrong person speaking, garbled app name. Prevent: face frontal or three-quarter, mouth visible, short lines, one speaker at a time.
- **Voice slop:** voice too old or too polished for the face, a radio announcer tone, voice changing between clips, rushing to fit the words.
- **Fake proof:** fake star ratings, fake comments on screen, "verified user", a doctor's coat.
- **App fidelity:** the phone looks the same in every shot (model, color, case); the screen matches the user's screenshot exactly or stays hidden; the app icon, logo and store badges are never generated (the uploaded logo goes on the end card); the thumb really presses the glass and the screen reacts in the right place.

---

## Truth and disclosure

- An AI person is a creative performance, never a real customer. No fake testimonials, reviews, ratings, "verified" badges or durations of use as proof. Real reviews can be quoted as proof only as text (caption, card), attributed as reviews, never put in an AI person's mouth as if they wrote it.
- No real people, creators, celebrities or lookalikes; no cloned voices of real people.
- No credentials the persona doesn't have (doctor, financial advisor, therapist); no health, money or body results beyond the Brand Kit's approved claims.
- Platforms label AI content: Meta and TikTok expect a visible AI label on photorealistic synthetic people, and auto-detect content credentials. In the US the FTC treats an undisclosed synthetic endorsement as a deceptive testimonial and expects both "ad" and "AI" disclosure. Tell the user once, in the final report, to turn on the AI-generated label when they set up the campaign. Not legal advice; they check current platform rules.
- **Brand safety** (Lyra's System Preamble, base Reference B): no profanity, no political statements, no unsubstantiated health claims, no competitor disparagement. The Brand Kit's **forbidden claims are enforced absolutely**, in every spoken line, caption, visual and VO; if the user asks for one, say once that it is on the kit's forbidden list and leave it out unless the user confirms the kit is outdated.

---

## Deliverable and naming

1. A "UGC script" text node: pain moment, character card, place, format, speech per clip, cuts, captions marked for post.
2. Character image(s), clip(s), B-roll and UI inserts as planned.
3. One finished video per persona (or per format), each in its own Video Editor.

Name every final with a code the media buyer can paste into Ads Manager: `B{batch}-A:{angle}-F:UGC-{format}-P{persona}-C{concept}H{hook}`, e.g. `B2-A:CantSwitchOff-F:UGC-Storytime-P1-C1H3` (drop `H` when no hook skill was used). Node label: "Final: P1 Mia · C1H3 storytime sleep".

---

## Common mistakes (UGC)

| Mistake | Prevention |
|---|---|
| Persona invented without reading the Brand Kit's audience | Pain map and pain moment first; casting from the audience |
| UGC opens on someone just starting to talk, no hook | Hook from `lyra-video-hooks` by default (Hooks in UGC) |
| Hook played by a different person or voice than the body | Same character card and voice anchor in the hook |
| Second line repeats the hook instead of moving on | The speech continues the hook |
| Portrait blur, gimbal moves, graded "cinematic" phone video | Phone optics: 24mm, deep focus, micro-jitters |
| Nobody holds the camera (a floating, smooth "film" camera) | A camera setup in every prompt: handheld, walking, car mount, propped, tripod, mirror, someone else films |
| Phone held in hand while driving | Phone in a mount, or the car is parked |
| Model-perfect person, studio light, editorial look | Realism rules; phone-real light and framing |
| Setting chosen because it looks nice, not where the pain happens | The pain moment picks the place |
| Speech written as ad copy | Spoken words, read aloud; the app named where the concept planned it |
| Fake testimonial ("I've used it for 3 months", 5 stars) | Creative scene only; proof only from real reviews, as text |
| Too many words, rushed voice, broken lip-sync | Word budget, one short sentence per 3 to 5 s, clip minus 1 s |
| Voice doesn't fit the face or changes between clips | Voice anchor word for word; one longer clip; fallback VO as audio reference |
| The wrong person speaks in a dialogue | Lines tied to [ImageN]; listener still; one clip per line if needed |
| Kling or Veo for UGC, sound off | Seedance 2.5, sound on (720p by default, 1080p on the user's choice) |
| First / last frame on Seedance 2.5 | References only |
| Invented app screen in the person's hand | Screen hidden, or the user's screenshot as UI insert |
| Captions added without asking, or forgotten after a yes | Ask in the approval message; if yes, captions for all speech in the Video Editor |
| Seedance adds its own background music under the live voice | No-music sound line in every clip + "background music" in Avoid; our music only in the Video Editor; rerun a clip that still has music |
| Music under a talking head drowning the voice | No music by default for talking formats; otherwise about 0.05 to 0.1 under live speech |
| Template run as it came (Kling, "flawless", text in prompts) | Adapt per Format library |
| Two personas differ in script or place too | Only the persona changes in an A/B |
| AI label not mentioned | One line in the final report |

## Quality gates (UGC)

- **Stage 0 (script, Claude checks before sending):** tied to one pain? Hook built with the hook skill (or a stated reason why not), and it passes its line checks? Persona, place, voice and speech tell one idea? Words counted, fit the clip minus 1 s? Spoken, simple, specific, true? No fake proof?
- **Stage 1 (character images):** looks like a real person from this audience, not a model? Phone-real, not editorial? Place matches the pain moment? Expression fits? Hands and phone natural, screen hidden or right?
- **Stage 2 (clips):** lip-sync matches the words? The app name pronounced right? Voice fits the face and stays the same across clips? Not rushed, natural pauses? Small real gestures, no overacting? Same face and outfit through the cuts? Camera feels like a phone, and it moves as the setup allows (handheld jitters, walking bob, static when propped)?
- **Stage 3 (final), app ad check:** is it clear in one watch what the app does for this person? Does the app fit the scene naturally, not glued on? Does the promise match the store page and the real first session? Is the CTA an install or trial step with the real offer?
- **Stage 3 (final):** pain recognisable in 1.5 to 3 s? Spine in order, CTA at the end, same words as the caption? Captions (if the user said yes) on all speech, size 80, at 75% of the height, not over the face? Music (if any) under the voice? 9:16, planned resolution (720p by default), planned length? Named with its code? AI label reminder given?

## After the test

Read the test as in `lyra-video-hooks` (After the test): hook rate, hold rate, then the numbers that matter for apps: installs per 1,000 impressions, cost per trial, trial to paid, day-7 retention. UGC formats differ downstream: skits and method-first videos often get fewer but better clicks, so judge by trials and payers, not CTR alone. The persona, the pain and the format are each a hypothesis: say which one won. Then offer: a new persona on the winning script, the winning persona in a new format, new hooks on the winner (`lyra-video-hooks`, mode A), other sizes or languages.
