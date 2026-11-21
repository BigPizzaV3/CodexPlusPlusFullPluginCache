---
name: lyra-video-hooks
description: "Use when the user wants hooks or new openings for an app video ad, e.g. \"hooks for my app\", \"4 hook variants\", \"a hook bank\", \"hook multiplier\", \"a visual / brainrot hook\", \"the hook is weak\", \"hook rate dropped\", \"a stronger first 3 seconds\", or a Lyra Hook template. Writes hooks from the audience's pains and turns them into videos in Lyra for an A/B test."
---

# lyra-video-hooks

Mini skill. Finds the audience's pains in the Brand Kit, writes a bank of hook ideas, then turns the best 4 (3 to 6) into finished videos in Lyra.

**Canvas layout → `lyra-workflow-layout`.** Every workflow this skill builds or changes is laid out by `lyra-workflow-layout`: sections in reading order with a STEP note above each one, the team's color code, clear node labels and the final check. The layout lines in this file only say which sections this creative needs.

**This is a way of thinking, not a script.** The rules below are defaults and good practice. Use judgment: when a different hook, order or combination serves the idea better, do it and say why in one line. Only a few things are fixed: truth (no invented claims, reviews or numbers), the Brand Kit's facts, Lyra's technical limits, and the user's explicit choices.

**Base skill first.** Everything not written here follows `lyra-video-ad-generation`: the 8 steps, instruction order, app card, plan table and stages, run options with credits, run and report, prompt rules, models (Reference A), audio (C), app UI (D), consistency (E), prompt craft (F), errors (G), de-slop (H), Brand Kit (I), Meta app ads (J). This file only adds what is specific to hooks. If the two disagree, the user wins, then this file, then the base skill.

**Method.** GBP (Gut, Brain, Pocket) and the More, Better, New iteration framework. This skill is **MORE**: new Guts on the same Brain and Pocket. Hook writing follows direct response practice: audience awareness, voice of customer, one idea per hook, every claim true.

---

## How to think about a hook

**What it is.** The hook is the **Gut** of the ad: the first 1 to 3 s. It has up to four layers that fire together: **visual** (the first frame and the first movement), **verbal** (the first spoken line), **text** (the caption on frame 1), **sound** (SFX, music hit, silence). Its job: stop the scroll in about 1 s and, by 3 s, tell the right viewer "this is about your problem". Meta reads early retention from the first second, so frame 1 already has to move.

**Three kinds of hook.** Decide this first, for every idea:

| Kind | What happens in 0 to 3 s | Works best when |
|---|---|---|
| **Visual hook** | the picture does the work: an action, a surprise, a strange situation, a transformation; no one needs to speak (music, SFX, a caption) | the pain or the result can be *seen*; music-led or ASMR videos; one video for many languages; cinematic or surreal concepts |
| **Verbal hook** | a person speaks first: a pain line, a question, a confession, a callout; the picture is a face already mid-sentence | UGC and talking head; the pain is a feeling or a thought that is hard to show; the audience needs to be named |
| **Combined hook (stack)** | a short visual beat first (0 to 1 s), then the spoken line right on top of it (1 to 3 s); example: a clap in front of the camera, then the girl says the pain in the audience's words | most UGC app ads: the visual stops the thumb, the line tells the right person "this is you" |

**How to choose.** Think about the idea of the whole video, not the hook alone:

- What is the strongest thing to show or say in the first second? Lead with it.
- Can the pain be seen? Lean visual. Is it a thought or a feeling? Lean verbal, maybe with a small visual beat.
- UGC and talking head: a combined hook is usually strongest (a physical beat + a pain line). Cinematic, surreal or music-led: a visual hook alone is often enough. Reels moves fastest: keep visual tricks short and get to the person quickly.
- Two layers must tell **one** idea. A visual beat and a line that say different things fight each other; then pick one.
- One strong hook beats two weak ones stacked. Stack only when each layer adds something: the visual catches, the line qualifies. A **double hook** (a second hook at 3 to 6 s) is a separate test (Better), not the default.
- Sometimes the pain itself is the hook; sometimes the hook is a surprise and the pain comes right after. Decide per idea.

**The story the hook opens (default spine).** Hook (0 to 3 s) → **the pain**, shown on a person so the viewer recognises themselves (3 to ~6 s) → **how the app solved it**, one real feature, the change visible (~6 to 12 s) → CTA. This is the default for app ads (problem-led hooks take most app video spend). Other spines are fine when they fit: outcome first then how, demo first, old way vs new way, a story cold open. Choose what presents the idea best and say why in the plan.

**Final test for every hook:** relevance + curiosity + a reason to care. Would the right person understand it at once, recognise something from their life, and want the next seconds?

**Main character of the first seconds (3P):** **Problem** (the pain, on a person living it) · **Product** (the app in use, real screens) · **Persona** (someone the viewer sees as themselves). A strong hook also uses at least two of: visual interrupt · relevance signal (the viewer's situation, or the audience named) · promised outcome · open loop (always closed later).

**Principles:** sell the outcome, not the feature; identity and future-state lines ("What if you woke up actually rested?") usually beat feature lines ("Track your sleep with AI") · clear beats clever · if you talk about it, show it · specific beats vague (a real number, a named audience, an exact moment) · negative and contrarian framings often stop more people, but never shame the viewer · the ad must not look like an ad (native, phone-real) · humour and edge when the brand allows · don't open on the logo or the app name · no price in the hook for cold traffic (a free trial can open the ad when it's the real offer).

---

## Step 1 additions: Brand Kit and the audience's pains first

Hooks are built on the **Brand Kit** and on the **real pains of the audience**. Before any idea:

1. **Find the Brand Kit:** the one in the chat, the one assigned to the workflow, or `list_brand_kits` (one kit → use it and say so; several → ask which). No kit → ask the user to send it or connect one (base Reference I).
2. **Read it fully** and pull out a short **pain map**:
   - **Audience:** who, which segments, their situation and daily moments where the problem shows up.
   - **Pains:** what hurts, in their words if the kit has them; what they already tried and why it failed.
   - **Desires:** the outcome they want, the identity they want ("someone who sleeps", "someone who has money left").
   - **Objections:** why they hesitate.
   - **Product truth:** real features, claims, offer, proof, tone of voice, must include / must exclude, forbidden claims.
3. **If the pains are missing, vague or too generic**, don't block: write 3 to 5 **pain hypotheses** from the app card (each one line, in the audience's words) and ask the user to confirm, pick or correct them. Still propose hook ideas in the same message so work moves.
4. **Intake quiz** (base Step 1: one message, multiple choice, options from the Brand Kit, the recommended option first, 4–8 questions; skip what the task or the kit already answers), with these questions plus the base quiz questions that apply:
   - Body already (mode A, hook multiplier) or not (mode B)? Where does the old hook end? Is it a validated winner? Its hook rate, hold rate, CTR if known.
   - Which pain or segment to lead with, if the kit has several (offer your recommendation).
   - Hook preference: visual, verbal, combined, or "you decide" (default: you decide and explain).
   - Cold or warm traffic; the store link for research; reviews, past winning hooks, viral videos the audience loves.
   - How many hooks (default 4)? Tone, types or claims to avoid?
5. **Propose ideas straight away.** Don't wait for perfect input: the first reply already carries the pain map (or hypotheses) and the first hook ideas.

**Defaults (state, don't ask):** cold traffic · bank of 12 to 15 · N = 4 · 9:16 · Reels / TikTok · English · final 10 to 15 s in mode B, body length + hook in mode A · Seedance 2.5 for people, 2.0 for stylized or UI · 720p (1080p on the user's choice) · sound on · voiceover on in mode B.

**Debug path from the numbers:**

| Signal | Diagnosis | What to do |
|---|---|---|
| Low hook rate | The hook doesn't stop people | Stronger visual beat in frame 1, or a sharper pain; if the angle isn't validated, the angle may be the problem (tell the user) |
| High hook rate, low hold rate or CTR, high CPM | Stops the wrong people, or the body doesn't keep the hook's promise | Name the audience in the line, show what they recognise, align the hook with what the body delivers |
| Good hook rate, low hold rate | The body is weak | Not a hook problem: Better (double hook, social proof after the hook, reorder blocks) |
| Good CTR, weak conversion | Offer, store page or expectations | Not a hook problem; check the hook doesn't promise more than the app gives |

## Step 1a: hook research (voice of customer)

When there is a store link, website or reviews; it takes minutes and makes every hook more specific.

1. **Store page / website:** title, subtitle, description, screenshot captions, ratings. Note the brand voice and the real features and claims.
2. **Reviews and comments:** sort into four kinds of language. **Pain** (the frustration before the app) · **Outcome** (what they wanted, the relief) · **Objection** (why they hesitated) · **Discovery** (what surprised them). Keep repeating patterns, drop one-offs.
3. **Alternatives** (when useful): what the audience uses now and what annoys them about it; claims every app in the category repeats (avoid them); what this app does differently that matters.
4. **Add to the pain map** in the app card: main pain · desired outcome · strongest real benefit · differentiator · objections · customer words worth quoting.

Couldn't browse or found nothing → say so and work from the Brand Kit. Never invent reviews, ratings, user numbers, press or awards.

## Step 1b: Lyra Hook templates

1. `list_templates` with tags ["Hook"] (add "UGC" or "Talking Head" for a person to camera).
2. Offer up to 3 that fit the audience, tone and the hook ideas: title + one line why + preview link. The user may pick one, several or none.
3. Picked → `get_template`, `use_template`, then adapt: rewrite the Video Script for the app card and the chosen pain with `update_node`, replace every placeholder ("[App Name]", "[main benefit]"), upload the logo, packshot or screenshots it needs.
4. Templates are fast demos: some use Seedance 2.0 Fast at 720p, some draw UI or a "DOWNLOAD" button. Say once: Seedance 2.5 (people) or 2.0, 720p by default, real screenshots (base Reference D). Follow the user's choice.

Hook templates in Lyra (Oct 2026); always re-check `list_templates`:
**Visual stop, object POV:** Knock, Blinds, Hook door, Camera is in a bag, Fridge Camera, Trunk POV, Empty Cup Hook, Library Shelf Hook, Morning Girl, Pogo Stick Fall.
**Fourth wall / surreal reveal:** Screen Pull, Balcony, Billboard App Reveal, Las Vegas Sphere, Office-core girl.
**Visual metaphor of the pain:** Clear Your Head, Swipe Away the Chaos, Sofa.
**Format hijack:** Breaking news, Interview POV, Stand-Up Comedy, Angry Boss, Hidden Cam, Subway Surfers Switch.
**Product reveal:** Phone Screen Reveal.

---

## Hook base: what you can draw from

A reference, not a menu to tick off. Combine, adapt and invent; always start from the Brand Kit's pain. The ad concept is in brackets where it fits.

### Visual hooks (the picture does the work)

| Type | What it looks like | Watch out |
|---|---|---|
| Physical interrupt | a clap in front of the lens, a knock on the lens from inside, a hand covering then uncovering the lens, an object tossed at the camera, blinds or a door snapping open | must lead into the pain within 3 s; one beat, not a show |
| Mid-action open | start at the peak moment: the phone already flying onto the bed, the mess already everywhere, the reaction already happening | no setup before it |
| Before state | the problem on screen: 47 unread notifications, a chaotic calendar, an empty fridge at 11 pm, the tired face in phone light (Problem) | show it on a person, not only an object |
| Incomplete visual | a strange situation without explanation that the next seconds answer | answer it by 3 to 5 s |
| Transformation cut | hard cut before → after on a beat, same framing and light (Transformation) | specific, believable; no body before/after for health apps |
| Demo first | a thumb already using the core feature on a real screen (Demonstration) | real screenshots only; keep it short |
| Unusual POV | camera inside a bag, fridge, trunk, bookshelf; the person opens it and looks in | the reveal leads to a person who talks or shows the pain |
| Fourth wall | the character looks into, reaches out of or pulls the viewer into the screen | one clear gesture |
| Visual metaphor / hyperbole | the pain made physical: a huge heavy head, notifications flooding the room, a to-do list unrolling to the floor | exact cause and effect order in the prompt |
| Reaction / micro-expression | a genuine face reacting: the pause, the eyebrow, the laugh | not a forced "wow" |
| Sensory / ASMR close-up | tactile macro detail, satisfying motion, 1 to 2 s with no voice | needs a link to the app (a satisfying "done" tick, an inbox going to zero) |
| Format hijack visual | a news studio, a street interview mic, a stand-up stage, an office meeting (Platform Trends) | only formats this audience follows; no real channels or brands |
| Text-first frame | a bold claim or question as the caption on frame 1, over a moving shot | full text at once, no letter-by-letter fades |

### Verbal hooks (a person says it)

| Type | Example line | Watch out |
|---|---|---|
| Pain callout | "Still scrolling at 2 am? This one's for you." | specific pain from the pain map, not generic |
| Audience callout | "Night owls who hate mornings, listen." | the fix when the hook stops the wrong people |
| Diagnosis | "Here's why your to-do list never gets shorter." | the body must give the reason |
| Mistake / contrarian / negative | "Stop setting ten alarms. It's making mornings worse." | challenge the habit, never insult or scare |
| Question with a stake | "Why is your budget gone by the 15th?" | no yes/no questions |
| Confession / low expectation | "I didn't expect a sleep app to actually work." | a creative scene, not a fake review |
| First person | "I used to lose two hours every night scrolling." | never presented as a verified real user |
| Story cold open | "Lying in bed at 3 am. Again." | close the loop in the body |
| POV | "POV: you finally fell asleep before midnight." | must match the audience's real life |
| Identity / future state | "What if you woke up actually rested?" | tied to what the app really does |
| Specific outcome / direct benefit | "I saved my first 200 euros in a month." | numbers only from the Brand Kit or real reviews |
| Objection first | "I thought budgeting apps were a waste of time." | the body answers the doubt |
| Third-person proof | "My sister hasn't missed a deadline since March." | creative scene; real proof only as proof |
| Dialogue | "Wait, you went to bed before midnight?" "Yeah, since…" | short lines, clear roles |
| People talking about the prospect | "She's been 'going to sleep' for two hours." | recognition, never humiliation |
| Compliment | "How are you always on time now?" | shows a real benefit; usually not about looks |
| List / formula | "Two mistakes everyone makes with their savings." | deliver exactly what was promised |
| Insider / what's new | "Nobody tells you this about morning routines." / "This app just changed one thing." | true and specific |
| Unique feature | "It reads every label, so you shop twice as fast." | feature → benefit → why it matters to you |
| Social proof / authority / statistic | a real rating, a real user count, a real expert, a real number | verified only; none available → demo instead |
| Stakes / FOMO | "Every month you wait costs you another 50 euros." | real stakes only, no fear-mongering |
| Offer first | "Seven days free. Here's why I kept it." | warm traffic or real risk reversal; no price |

### Sound (the fourth layer)

An SFX on frame 1 (click, zip, knock, slurp, notification ping), a music hit on the cut, a sudden silence, or a trending sound the audience knows. Sound-led hooks are weak with sound off, so the picture or caption must still carry the idea.

### Catchy and brainrot hooks (app-native, attention-first)

Feed-native formats that win attention by being weird, chaotic, funny or "not an ad". They borrow the language of the feed (memes, AI characters, chats, split screens) and then turn to the app fast. Strongest with Gen Z and Gen Alpha and for casual, social, entertainment, study, productivity and habit apps. For trust-heavy categories (finance, health, premium) borrow the logic (surprise, speed, humour), not the full chaotic look.

| Format | What it looks like | How it turns to the app |
|---|---|---|
| Brainrot absurd | an original absurd AI character or situation, deliberately lo-fi, a confident dramatic voice saying near-nonsense, bass-heavy sound, fast jump cuts | the absurd thing *is* the pain in disguise (a screaming alarm-clock creature = mornings), then a hard cut to a real person and the app |
| Talking object / pet | the phone, the alarm clock, the to-do list, the brain or a pet talks to camera like a colleague | the object complains about the user's habit (the pain) and "recommends" the app |
| AI micro-drama | an episodic mini-series with original characters (fruit, objects, habits as characters), reality-show tropes, a twist each episode | the app is the plot twist or the solution of the episode; a series gives several ads |
| Split screen | top: a person talking or a story; bottom: a satisfying loop (kinetic sand, slime, marble run, an original game-like run) | the story on top is the pain and the app; the loop only holds the eye |
| Story with TTS | a short first-person story read by a synthetic voice over a satisfying or POV background, captions word by word | the story's turn is how the app helped |
| Chat thread | stylised message bubbles appear one by one: "wait, did you actually try it?" | the reply resolves into the app; based on real customer conversations, lightly fictionalised |
| Comment reply | the video opens on a comment bubble: "does this app actually work?" and the creator answers | the answer is the demo; only real comments or clearly hypothetical ones |
| Trend remix | an AI trend mechanic the audience knows right now (action figure in a box, earth zoom out, bullet time, 80s camcorder diary, a dance), with the user's character | cut to the app within 2 to 3 s; the trend has nothing to sell on its own |
| Absurd scale or physics | something impossibly big, tiny or heavy (a giant notification crushing the room, a tiny person drowning in emails) | the app restores normal scale |
| Calm contrast | a slow, quiet, hand-painted or soft scene with gentle music in a loud feed | stands out by contrast, then the app appears as the calm |

**How to use them well:**

- Entertain first, but the link to the pain or the app must land within about 3 s; a weird opener that never connects brings cheap views and weak users.
- One absurd idea per hook, instantly readable; no inside jokes the audience has to research.
- Invent **original** characters and situations. Never use known meme characters (Skibidi, Italian brainrot creatures and the like), real games (Subway Surfers…), shows or brands unless the user owns the rights; the Lyra "Subway Surfers Switch" template needs an original background.
- Deliberately lo-fi is a style; accidentally uncanny is slop. Faces and hands of real-looking people still follow de-slop; brands that ran sloppy AI ads (Valentino, McDonald's NL) had to pull them.
- Chats, notifications and comments are stylised, not copies of iOS, WhatsApp, TikTok or system UI (platforms restrict ads that imitate organic interface elements); no fake read receipts or fake contact photos; a fictional chat is never presented as a real customer conversation.
- Keep the rhythm: a new stimulus every 2 to 3 s (cut, zoom, sound hit).
- Trends move fast: the brainrot peak was late 2025 to early 2026 and some audiences already call it cringe. Use the mechanic, keep it fresh, check what is trending now (TikTok Creative Center, the user's own feed) before building.
- Sound matters most here: a dramatic narrator, sped-up voice, bass hit, a strange jingle. Music is generated from a description (no artist names, no copied tracks).

### What feels stale in 2026 (avoid unless twisted)

Ring-light testimonial that reads as an ad in half a second · forced enthusiasm ("this changed my life", "obsessed") · opening with a feature list · vague before/after · "Hey guys, today I'm…" · logo or app name first · a slow fade in.

---

## Audience awareness: which hooks for whom

App install ads on cold traffic are mostly levels 1 to 3; retargeting 4 to 5. Unknown → mostly cold plus one or two warm.

| Level | The viewer | What usually works |
|---|---|---|
| 1. Unaware | doesn't see the problem as a problem | a relatable moment, a visual metaphor, humour, mid-action, POV, catchy and brainrot formats (talking object, micro-drama, trend remix, split screen); no hard pitch |
| 2. Problem aware | knows the pain, not the fix | pain callout, diagnosis, mistake, before state, first person, people talking about the prospect |
| 3. Solution aware | knows fixes exist, not which | old way vs new way, question with a stake, list, outcome first, transformation cut |
| 4. Product aware | knows the app, not why it's worth it | demo first, unique feature, objection first, compliment, proof |
| 5. Most aware | close to installing | offer first, real proof, a reason to act now (real urgency only) |

## Where hook ideas come from (in this order)

1. **The Brand Kit's pains and desires** (the pain map). Every hook ties to one of them.
2. **Customer words:** lines from real reviews, comments, support messages (the user, the Brand Kit, store research). Short phrases, never long copied reviews; an AI person saying the line is never presented as the real reviewer.
3. **Past winning hooks** of this app (ask for the hook repository), above all when the current winner has a low hook rate.
4. **Modelled viral TikTok / Reels hooks** the audience loves: copy the mechanism (first frame, twist, line structure), never the video, its people or its sound.
5. **The hook base above**, to widen the set.

## Step 2 addition: the hook bank

Before the plan, write the bank in the chat; it is part of the concept the user approves.

- **12 to 15 ideas** by default (30 on request), each a different idea: a different pain, outcome, situation, perspective or format, not one idea reworded. Mix visual, verbal and combined hooks; mix direct (names the app or feature) and indirect (starts with a situation) openers; cover the audience's awareness levels; a few with humour or edge; when the audience and brand fit, one or two catchy or brainrot ideas.
- One line per idea, with tags:
  > H07 · combined · problem aware · Problem · pain: "can't fall asleep" · visual: clap in front of the lens, she's in bed in phone light · line: "If your brain starts talking at 2 am, listen." (9 words) · text: "2 am again?" · hypothesis: night-scrollers stop for a sleep pain said in their words
- **Recommend N** for production (default 4) with one line why. A good set of 4 usually has different kinds (at least one visual-led and one verbal-led or combined), different pains or angles from the pain map, different main characters, and one idea from the user's own sources if they have any. Guidance, not a quota: explain your choice.
- After approval, save the whole bank in a user text node "Hook bank" in the workflow (picked ones marked) for the next MORE round.

## Writing one hook

Write the muted version first: the first frame plus text must work with sound off.

- **First frame:** the hook moment at frame 0, already moving. It is also the thumbnail, so it must read on its own.
- **Spoken line** (verbal and combined hooks): aim for about **6 to 10 words**, said within ~3 s; count the words. Start on the key word; no "So", "Okay", "Hey guys". A longer line is fine only if it still lands by second 3.
- **Text on screen:** 2 to 6 words, echoes the line (doesn't contradict it), on frame 1 in full, marked for post (added in the Video Editor, never in a prompt), inside the safe zone.
- **Sound:** what is heard in the first second. Sound stays on at generation. When someone speaks in the clip: no music under the voice ("no music, no background music, no soundtrack, no score" in that clip's prompt, base Reference C). Clips without speech may keep their music hits.
- **Visual beat** (combined hooks): 0.5 to 1 s, then the line starts on top of it or right after; both tell one idea.

**Checks for every line:** one idea · simple (about a 5th grade reading level, no corporate or "AI" marketing words) · sounds natural said aloud · specific to this app, audience and moment (if it could sell a hundred apps, rewrite) · true (nothing outside the Brand Kit, app card or verified research) · different from the other hooks.

Concept line per picked hook (goes into the plan):
> C1H2 · combined · problem aware · Problem · Visual: a clap in front of the lens, she's sitting in bed in phone light at 2 am. Line: "If your brain starts talking at 2 am, listen." Text (post): "2 am again?" Sound: the clap, then silence. Then: her pain (3 to 6 s), the app's wind-down timer (real screenshot), she falls asleep, CTA.

---

## Deliverable and modes

1. A **hook bank** (12 to 15 ideas) saved in a "Hook bank" text node.
2. N hook clips and **N finished videos**, one per picked hook, each in its own Video Editor. All variants share the same body (Brain), CTA (Pocket), music and end card, so the test isolates the hook.

Name every final with a code the media buyer can paste into Ads Manager: `B{batch}-A:{angle}-F:{formula}-C{concept}H{hook}-Iteration`, e.g. `B3-A:SleepIn5min-F:PAS-C1H2-Iteration`. Node label: "Final: C1H2 · combined clap + pain line".

**When MORE is the right move:** right after an ad is validated · hook rate low while hold rate and CTR are fine · a winner fatiguing after 2 to 6 weeks (keep audience and angle, replace only the hook) · a losing streak (new hooks on a past winner). Not this skill: weak body or high CPC → Better; dead angle → new concept or angle (base skill). Only hook texts wanted → stop after the bank.

| Mode | When | What gets built |
|---|---|---|
| **A. Hook multiplier** (true MORE; default when a body exists) | The user has a body: an existing or winning ad, a Lyra workflow, a video to upload | the original ad as control + N new hooks, each a hypothesis; only the first 2 to 3 s change → N Video Editors (hook N + same body, music, CTA) |
| **B. Hook-led short ads** (default when there is no body) | Nothing exists yet | N ads of 10 to 15 s on the default spine: hook → pain → app solves it → CTA; pain, solution and CTA as identical across variants as the hooks allow |

Mode A body sources: the user's own Lyra workflow (build the hooks inside it, in a new Section) or a finished video (create_upload + attach_upload). Results can't be connected across workflows.

### Hook multiplier: testing hypotheses with the same body

Only the first 2 to 3 s change; everything after the cut point stays exactly as it is. That makes each new hook a clean test of one **hypothesis**, and the cheapest way to learn what stops this audience.

**1. Hypothesis per hook.** Every hook in the bank carries one line: "We think [segment] stops for [pain / angle / hook kind / format]." Decide what the round is testing and vary that, keeping the rest close:

- **Which pain or desire** hits hardest (same kind of hook, different pain from the pain map).
- **Which kind** works: visual vs verbal vs combined (same pain, different kind).
- **Which segment** responds: a callout per segment (students vs parents vs freelancers).
- **Which framing:** negative vs positive, question vs statement, identity vs feature.
- **Which format:** UGC person vs catchy or brainrot vs demo.
- **Finer tests** for a winner: same line with a different first frame, or same first frame with a different line.

A round can mix hypotheses, but say which hook tests what, so the result teaches something.

**2. Control.** Keep the original ad with its own hook in the test as the control (champion). New hooks are challengers; a hook wins only if it beats the control on the user's KPI.

**3. The cut point.** Find where the old hook ends (usually 2 to 3 s; ask the user or read the composition in the Video Editor). Trim the body from that point (`trim.sourceStartMs`). Check that the body still makes sense without the old hook: the voiceover doesn't start mid-sentence, no line refers back to the old opening, the first body frame follows the new hook naturally. If the old hook was spoken over the body, trim the VO too and keep the rest identical. The new hook ends on an end state that cuts cleanly into the body's first frame (cut on action, match cut, or a deliberate hard cut).

**4. Scale.** 4 to 6 new hooks per round is a good default; more (up to 10 to 20) when the budget allows, built in rounds from the bank. Each round's winners and losers go to the hook repository with the hypothesis they tested.

**5. Reading the result.** The winning hypothesis is the learning, not only the winning video: a winning pain or segment feeds the next ads, angles and Brand Kit notes; a winning kind or framing becomes the default for the next round.

**Double hook (optional, mode A):** a second proven hook right after the first (0 to 3 s, then 3 to 6 s). Offer as one extra variant when hold rate is low or CPC is high; it is a Better test.

## Best way to build it

The user's explicit choices override any row. Models and prices: base Reference A.

| If the hook is | Best approach (graph) | Models |
|---|---|---|
| **Combined, UGC person** (common default) | character image → hook keyframe (the visual beat at frame 0) → one clip with the beat, then the spoken line in quotes, then the pain; or the hook as its own 4 to 5 s clip trimmed to 1.5 to 3 s | nano-banana-pro · seedance-2.5 |
| **Verbal, talking head** | character image → clip starting mid-sentence, the line in quotes, natural gestures | nano-banana-pro · seedance-2.5 |
| **Visual, no speech** (object POV, metaphor, transformation, ASMR) | hook keyframe → clip 4 to 5 s with exact action order; music or SFX; caption in post | seedance-2.0 (frame) or seedance-2.5 (refs) |
| Dialogue or "people talking about the prospect" | two character images as references → one clip, who says what by [ImageN] | seedance-2.5 |
| Shows the app (demo, feature) | user screenshots → phone image → short clip or UI insert (base Reference D) | seedance-2.0 (frames) or 2.5 (refs) |
| Mode A, same person as the body | a still of that person from the body as reference; no still → a faceless hook | seedance-2.5 |
| Mode B, full short ad | per hook: character → one multi-shot clip 10 to 15 s with "cut to" between hook, pain and solution, or separate clips joined in the Video Editor; VO + music; logo end card | seedance-2.5 · nano-banana-pro |
| Lyra Hook template picked | use_template → adapt (Step 1b) → one Section per hook | as the template, upgraded |
| Double hook variant | hook clip A + hook clip B + body → one extra Video Editor | as above |
| Only hook texts | stop after the bank | none |
| Catchy: talking object, AI character, micro-drama | original character image (nano-banana-pro, the style chosen: lo-fi, cartoon, 3D) → clip with the line in quotes; one character reference for the whole series | nano-banana-pro · seedance-2.0 (stylized) or 2.5 (realistic) |
| Catchy: split screen | top clip (person or story) + bottom clip (original satisfying loop) → Video Editor with two video layers positioned top and bottom (position x/y/width/height), captions in the editor | seedance-2.5 + seedance-2.0 |
| Catchy: chat thread, comment reply | message or comment images designed with exact text in quotes (stylised, not a copy of a real messenger) → laid over the video in the Video Editor, one by one | nano-banana-pro + video_composer |
| Catchy: trend remix | the trend mechanic as an image or clip with the user's character → hard cut to the app part | per trend: seedance-2.5 or kling (frames) |
| Many hooks, tight budget | hook clips on a draft model, rerun winners on the recommended one | seedance-2.0-fast |

**Hook clip length.** Seedance's minimum is 4 s: generate 4 to 5 s, put the hook beat in the first 1.5 to 3 s, plan a clean cut point (end state) into the next shot, trim in the Video Editor.

**Layout.** Section "Hook bank" (text node), one Section per hook (its nodes + its Video Editor), one Section for the shared body, music and VO. Labels: "C1H1: clap + pain (frame)", "C1H1: clap + pain (clip)", "Final: C1H1 · clap + pain".

## Video Editor per hook

One `video_composer` per hook, in playback order: hook clip → body clip(s) → end card, then VO and music. Everything except the hook is identical across variants: same body trims, same music (starting at 0 so the hit lands on every hook), same body VO and CTA, same end card. Keep the hook's own sound or line; lower the body clip's sound if it clashes. Hook text and captions are added in the editor UI: tell the user what to add and where. Captions, if the user wants them (asked in the approval message), follow the base rule (`lyra-video-editor` → Captions: size 80, at 75% of the height, under the face); the hook text on frame 1 is a headline, placed in the safe zone. If the hook opens a loop or promises a list, check the body delivers it.

## Run options for hooks

**Run order, not a menu** (base Step 6): after the user's yes, run all of it in this order without offering options. Stop between stages (the look first, then the rest) only when the user asked for it, or when the plan is expensive and that was said in the approval message.

As in the base skill, credits read from the nodes and multiplied by N; the hook bank costs nothing. **A. Hook images (recommended):** all N keyframes and characters · **B. Hook clips** for the frames the user picked · **C. Everything** → N Video Editors.

---

## Prompt rules (hooks)

| Node | Write | Avoid |
|---|---|---|
| Hook bank (text node) | each idea with number, kind (visual / verbal / combined), awareness level, main character, pain, visual, line, text, word count; picked ones marked | long explanations |
| Hook keyframe | the hook moment itself at frame 0: the visual beat mid-action or the person mid-sentence, the pain visible, phone-real for UGC, 9:16 | an establishing shot; text; drawn UI or logos |
| Hook clip | action from frame 1; for combined hooks, the exact order ("she claps once in front of the lens, lowers her hands, looks into the camera and says: '…'"); the surprise readable in ≤1.5 s; spoken line in quotes; who says what in dialogue; cause and effect; the end state at the cut point | slow build up; two surprises; the caption text in the prompt; a polished "ad" look |
| Hook VO (if separate) | the exact hook line as its own short VO node; body VO shared | filler openers; price; claims not in the Brand Kit |

No third-party brands, games, channels, landmarks used as brands, or famous people in prompts unless the user owns the rights.

## Truth and brand safety

- **Brand safety** (Lyra's System Preamble, base Reference B): no profanity, no political statements, no unsubstantiated health claims, no competitor disparagement. The Brand Kit's **forbidden claims are enforced absolutely**, in every hook line, caption, first frame and VO; if the user asks for one, say once that it is on the kit's forbidden list and leave it out unless the user confirms the kit is outdated.
- Hooks never carry a claim, number or offer that isn't in the Brand Kit or the user's message; a provocative or negative hook challenges a habit, never the viewer, a group or a competitor.

## Common mistakes (hooks)

| Mistake | Prevention |
|---|---|
| A hook clip where someone speaks comes with music under the voice | No-music sound line in every clip with speech; our music in the Video Editor |
| Hooks written without reading the Brand Kit | Pain map first; every hook tied to a real pain or desire |
| Waiting for perfect input before proposing anything | Pain hypotheses + first ideas in the first reply |
| Visual beat and line say two different things | One idea per hook across all layers |
| A visual trick with no link to the pain | The trick leads into the pain by second 3 |
| Two weak hooks stacked instead of one strong | Stack only when each layer adds something |
| Video credits spent on untested ideas | Hook bank first; the user picks |
| N hooks that are one idea reworded | Different pains, kinds, mechanisms, main characters |
| Generic line that could sell any app | Specific to this app, audience, moment |
| Hook type doesn't match the audience | Awareness table |
| Body, music or CTA differ between variants | Lock the body; only the hook changes |
| Logo intro, fade in, "Hey guys", feature list first | Frame 1 already moving; pain or outcome by second 3 |
| Hook promises what the app or body doesn't deliver | Promise only what the app card supports |
| Invented reviews, ratings, numbers, press, testimonials | Verified sources only; no proof → demo |
| Viral video copied instead of modelled | Mechanism only |
| Hook clip set to 1.5 s (rejected) | Generate 4 to 5 s, trim |
| Different face in hook and body | Body still as reference, or faceless hook |
| Template run as it came | Adapt per Step 1b |
| Hook multiplier without a control or without a stated hypothesis | Original ad as control; one hypothesis line per hook |
| Remnants of the old hook in the body (VO mid-sentence, a line about the old opening) | Cut point checked; body and VO trimmed cleanly |
| Brainrot opener that never connects to the app | Pain or app by about second 3 |
| Known meme characters, real games or a copied trend video | Original characters and backgrounds; the mechanic only |
| Chat or notification that copies iOS / WhatsApp / system UI, or a fake chat sold as real | Stylised bubbles, real or clearly fictional content |
| Chaotic brainrot look on a trust-heavy brand | Borrow the logic, not the look |

## Quality gates (hooks)

- **Stage 0 (bank, Claude checks before sending):** every idea tied to a pain or desire from the pain map? Different ideas, kinds and awareness levels? Layers of each hook tell one idea? Lines simple, specific, true, sayable, counted? No invented proof?
- **Stage 1 (images):** each hook moment reads in one glance, muted, even as a thumbnail? The N hooks clearly different? Same person as the body where needed?
- **Stage 2 (clips):** action from frame 1? Visual beat and line in the planned order? Surprise lands in ≤1.5 s? Line clear? Clean cut point? Native, not an ad?
- **Stage 3 (finals):** every final opens on its hook? Pain recognisable right after it? The app's role clear? Body, music and CTA identical across variants? Loops and lists paid off? Text 2 to 6 words in the safe zone? Each final named with its code? In hook multiplier: control included, old hook fully removed, hypothesis written for each variant?

## After the test

Hooks are hypotheses. Tell the user how to read the test in one short block:

- Launch all variants the same day, one ad set per concept in an ABO campaign.
- First signals at 2,000 to 4,000 impressions; judge each ad at 5,000+ impressions, never on day one.
- **Hook rate** (3 s views ÷ impressions): target above 40%; 2026 medians are about 28% on Meta and 33% on TikTok, top 10% about 45% and 55%; below 20% is weak. **Hold rate** (ThruPlays ÷ 3 s views): target above 30%. Compare with the account's own averages.
- Sales and profit → winner · no sales → not a winner, but an outstanding hook rate earns one more test · sales without profit → worth another test. No winner → next ideas from the bank, or a different pain or angle.
- Judge winners by CPA / ROAS (cost per install, trials, payers), not hook rate alone.

Then offer: save winning and losing hooks (hypothesis, kind, pain, line, visual, hook rate) to a **hook repository** doc in the project; the next round from the unused bank; the winning hook on other ads of the same angle; Better on the winner; other sizes or languages (matching skills). A winner lives about 2 to 6 weeks: start the next round before it fatigues.
