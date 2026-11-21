---
name: lyra-short-drama
description: "Use when the user wants a story ad for an app, e.g. \"a short drama ad\", \"a mini-series / story ad\", \"a cartoon story for my app\", \"a realistic story ad\", \"a 1-2 minute story video\", \"drama like ReelShort but for my app\", \"an animated story where the app saves the day\", \"episodes with a cliffhanger\". A 60-120 s animated or realistic story where the app is the turning point, built in Lyra."
---

# lyra-short-drama

This skill makes short drama video ads for mobile apps; their goal is installs, trials and subscriptions. A short drama is a 60 to 120 s story that plays like a clip from a mini-series: a hero the viewer roots for, a chain of everyday disasters caused by the pain the app solves, a turning point where the app comes in, and a payoff the viewer can see. It can be stylized (3D animation, 2D, stop-motion), so it reads as AI and as fiction and is still worth watching, or realistic (a live-action sitcom scene, a vertical mini-series, a confession). The skill offers story concepts for the app, writes the chosen story, casts and designs the characters, then builds and runs the whole film in Lyra.

**Canvas layout → `lyra-workflow-layout`.** Every workflow this skill builds or changes is laid out by `lyra-workflow-layout`: sections in reading order with a STEP note above each one, the team's color code, clear node labels and the final check. The layout lines in this file only say which sections this creative needs.

**App ads first.** Every decision serves one goal: the right person installs the app and keeps using it. A short drama is not a brand film or a cartoon for its own sake; it is a performance ad judged by installs, trials and payers. The story exists to make the audience's pain felt and the app's role believable. If a beat is fun but doesn't move the hero toward the app or show what the app changes, cut it.

**This is a way of thinking, not a script.** The rules below are defaults and good practice. Use judgment: when a different structure, style, length or order serves the story better, do it and say why in one line. Only a few things are fixed: truth (no invented claims, reviews or numbers; the story is fiction and never presented as a real customer), the Brand Kit's facts, Lyra's technical limits, and the user's explicit choices.

**Base skill first.** Everything not written here follows `lyra-video-ad-generation`: the 8 steps, instruction order, app card, plan table and stages, run options with credits, run and report, prompt rules, models (Reference A), audio (C), app UI (D), consistency (E), prompt craft (F), errors (G), de-slop (H), Brand Kit (I), Meta app ads (J). This file only adds what is specific to short drama. If the two disagree, the user wins, then this file, then the base skill.

**Other skills it uses.** Openings and opening tests: `lyra-video-hooks` (pain map, hook kinds, hook multiplier). Realistic people, voice anchors and spoken lines: `lyra-ugc-video` (casting, realism, voice, speech rules), with cinematic light instead of phone-real. End card with install button: `lyra-ui-motion-video`. Same story for another audience or market: `lyra-audience-variations`. New pain chain or new angle on a winning drama: `lyra-ad-concept-multiplier`. Remaking a competitor's drama: `lyra-copy-competitor-ad` for the analysis, then this skill for the build.

**Everything comes from the Brand Kit.** The hero, the pain chain, the turning point, the feature, the payoff, the offer, the tone and the look are built from the app's Brand Kit, never from imagination. Source order (base Reference I): the user's words in this chat → the Brand Kit given in the chat → the Brand Kit connected to the workspace or workflow (`list_brand_kits`; one kit → "Make this for {kit name}?", several → ask which) → none: ask once to send it or to connect one of the workspace's kits. Missing facts are asked for or written as hypotheses to confirm, never invented.

**Model.** Characters who talk on screen (3D animation, realistic drama): **Seedance 2.5**, references only, 720p by default (1080p on the user's choice), sound on, up to 30 s per clip. Flat 2D styles (anime, storybook, kawaii, doodle) and stop-motion looks: **Seedance 2.0** (references, or frames when the exact composition matters), 720p by default (1080p on the user's choice), up to 15 s per clip, as in Lyra's own animated story templates. Images: **Nano Banana Pro** for every character sheet and keyframe. Always confirm with `list_node_configs` and ask the user's preference in the plan (base Reference A).

---

## How to think about short drama

**What it is.** A short film in the language of vertical mini-series (ReelShort, DramaBox style), adapted for an app: conflict in the first seconds, quick escalation, a turn, an emotional payoff, a CTA. It works because the viewer starts watching a story, not an ad: the skip reflex doesn't fire, curiosity and empathy carry them past the point where a normal ad loses them, and by the time the app appears they already want the hero to win. The app is the hero's tool, not the hero.

**Animated or realistic.** Animation tells the viewer at once "this is a story", so nobody mistakes it for a testimonial; it hides the small imperfections that make AI people uncanny; it keeps characters consistent more easily across 60 to 120 s; and exaggerated acting reads with the sound off. Realistic drama feels closer to the viewer's own life and to the drama apps' own ads; it needs more care on faces, a clear fiction frame and the AI label (see Realistic drama). Choose by audience and category (see Category guide), and test both on the same script when unsure.

**Four pillars, all built from the audience's pain:**

| Pillar | Question it answers | Comes from |
|---|---|---|
| **Hero** | Who do we root for, and why do they deserve a win? | the audience segment in the Brand Kit, as an underdog |
| **Pain chain** | How does the pain ruin the hero's day, week, relationships? | the pain map, turned into 3 to 6 concrete scenes |
| **Turn** | Who or what brings the app into the story, and what exactly does it do? | one real feature, one messenger or plot device, an honest time to result |
| **Payoff** | What is visibly different now, and who notices? | desires and outcomes from the Brand Kit, mirrored on the pain scenes |

All four tell one story. A dog owner whose untrained puppy ruins her morning, her job, her neighbour's patience and her dinner party; a friend with a calm dog shows her the training app; "Day 14"; the same places, the same people, now going right; a stranger says "yours is so calm". That is one idea. A generic "sad person, downloads app, happy person" is not a story, it's a slide.

**Final test for every concept:** can the logline be said in one sentence with a hero, a pain, a turn and a payoff? Would the right viewer recognise their own life in the pain chain? Does the payoff show what the app really does, at a believable speed? Would a viewer who leaves after 10 s still know which app this was about? Would you watch the next scene even if it weren't an ad?

**Principles:**

- **Conflict in 3 s.** Open at the peak of a disaster, mid-scene, never on an establishing shot or a logo.
- **Every scene escalates.** Each disaster costs more than the last: time → money → face → a relationship. Same pain, new arena.
- **Every disaster has a witness.** The boss, the neighbour, the partner, the guests: their one line is the social cost, and the person the hero wants to win back.
- **Most viewers never reach the end, so the app can't wait for it.** Plant a light brand thread early, bring the turn at about 35 to 55% of the runtime (up to ~60% in a 2 min film), never in the last third (see The app in the story).
- **The app moves the plot.** It arrives through a person who shows their own result, or it causes the next event. A forced insert ("and now a word about our app") breaks the story and the trust.
- **Time is honest.** A title card ("Day 14", "Three weeks later") matches the Brand Kit's real time to result. No instant magic.
- **The payoff mirrors the pain.** The same places and people from the pain chain, now going right; the witness who complained now compliments. This is the satisfying click, and it reuses the sets (cheaper and more consistent).
- **One hero, one pain, one feature.** A second feature is a second episode.
- **Show, don't tell.** Expressions and actions carry the story; dialogue is short; it all reads muted with captions.
- **Warmth and a little humour.** Dramas for apps win on relatable comedy and sympathy, not on misery.
- **Modular scenes.** Every scene stands on its own, so the same film cuts down to 59 s, 30 s and a teaser without new generation.

---

## Why it works, and why it should work for us

**What research and platform data say** (numbers are from the named studies; vendor and platform data marked):

- **Being carried into a story changes minds.** A meta-analysis of 76 studies (van Laer et al., Journal of Consumer Research, 2014) found that narrative transportation goes with stronger emotions (ρ ≈ .57), attitudes (≈ .44) and intentions (≈ .31). Transportation grows with a plot that's easy to picture, realism, and a hero the viewer identifies with. → Concrete scenes from the audience's life, a hero from the audience.
- **Underdogs sell.** Underdog stories (a disadvantage plus passion and determination) raised purchase intent and choice through identification (Paharia et al., JCR, 2011). → The hero is losing but trying, never pathetic.
- **Arcs that end high get engagement.** In an MIT Media Lab × McKinsey study of ~1,500 short films, arcs that end on a big positive spike, especially after ups and downs, drew the most engagement. → Pain chain, rock bottom, payoff.
- **Brand inside the story pays.** Kantar × Meta × CreativeX (57k Meta assets, 2024): integrating the brand into the story added ~46% effectiveness, but only ~36% of campaigns did it well; fast storytelling (4 scenes in 6 s) +73%; people and eye contact +81% [platform research]. → Integration levels, fast cold opens, faces.
- **Storytelling beats tactical.** TikTok × Dentsu (MMM, 15 Nordic brands, 2025): storytelling UGC had ~70% higher ROI than tactical UGC [platform data].
- **It looks like content.** Drama-style ads don't look like ads, so they get past banner blindness; actors overplay so the plot reads muted (Palai Media).

**What to be careful about:**

- **Long ads are watched briefly by most.** In an agency analysis of 421 Meta ads (Biddy Co, 2026), cost per result was about the same at every length, 60 s+ included, but average watch time was ~3 s and only ~0.2% of impressions reached the end [agency data]. The full film works for the minority who get hooked (they are the high-intent ones); everyone else must get the hook, the app and the promise early. This is why the skill puts a brand thread early, the turn before the last third, and always makes cutdowns.
- **Cliffhangers are not magic.** A lab study (Wirz et al., 2023) found cliffhangers raise arousal but not the intention to keep watching. Every episode must sell on its own.
- **Fatigue is fast.** The format burns out quickly; one Chinese brand that pioneered brand dramas saw results fall sharply once everyone copied it. Plan variants from the start.
- **ROI is not proven for every category.** Public performance data for non-drama apps is scarce; treat each drama as a test against your best UGC.

**Why it should work for us (Lyra and its clients):**

- **Live action is the barrier.** A live-action vertical series costs about $130k to 300k and a drama ad set $1.5k to 3k [industry reports]; AI production is reported at 1/5 to 1/10 of that [vendor data]. Most app marketers can't shoot dramas; they can build them in Lyra.
- **The format needs volume.** Drama advertisers ran ~1,900 creatives per app in H1 2026, more than any other category [vendor data]. The winners run a system, not one film: Woofz runs many 3D dramas of 84 to 244 s with different heroes, dogs and languages. Lyra makes the system cheap: one cast and world, many pain chains, heroes, languages and cutdowns as variations.
- **Consistency is the hard part, and it's what the graph solves.** Character sheets as references, keyframes chained from them, Seedance 2.5 clips up to 30 s with dialogue, one canvas per film with variations.
- **It's still fresh outside drama and games.** In our scan most non-drama apps still run 10 to 60 s skits; long story ads are a way to stand out in the feed (an observation, not a guarantee).

---

## What the market shows

Examples seen in Meta Ad Library (Oct 2026) and public sources. Timings approximate.

| Advertiser | Category | Style, length | Story | How the app comes in | Lesson |
|---|---|---|---|---|---|
| **Woofz** (the reference) | dog training | 3D, ~126 s | a heroine's day of disasters with clock chapters (7:15 → 20:15) | a friend with a calm dog names the app and a named course at ~55%; "Day 14"; witness reversal | the full template (teardown below) |
| **Woofz** (second film) | dog training | 3D, ~141 s | a young man and his rottweiler puppy: "I've watched a bunch of YouTube videos" → "Maybe getting him was a mistake" → "I can't afford K9 training" → a family BBQ he's told not to come to | an older pet-shop expert shows the app on a tablet: the same method at home, no trainer needed; payoff: accepted at the BBQ | an expert messenger; the price objection answered inside the drama |
| **Woofz** (the system) | dog training | 3D, 84 to 244 s | many heroes (men, women, older owners), breeds, settings; English, Spanish, Portuguese, German; karaoke captions | the same turn mechanics | one world, many heroes and pains: a drama system |
| **Praktika** | language learning | realistic, 100 to 140 s, Brazilian Portuguese | on a plane with a foreign passenger; at home cooking while talking with the AI tutor on a tablet | a flight attendant asks "Já ouviu falar do Praktika?" at ~30%; then the app is used inside the scenes | an early messenger; the app as a plot device; two ads share one opener and test different bodies |
| **BetterMe: Mental Health** | mental health | photoreal AI, 74 s, "Generative AI used" in frame | a woman on a panel: "It took me getting divorced at 35 to realize I wasn't hard to love, I was hard to stay with" | late, as the way she understood her patterns | the confession format; the twist is the first line; in-frame AI disclosure |
| **Finch** | self-care | text-post story, 91 s | "I can't tell my wife the real reason I've been cleaning the house" → his daughter put a cartoon-bird app on his phone | the app is the secret | the "secret" structure; a story without video generation (careful: see Truth and safety) |
| **Calm** | mental health | illustrated, ~51 s | a stressed mother, a crying child; "nervous systems, not bad parenting" | the app never on screen, only headphones and the CTA | soft framing for delicate topics |
| **Rocket Money** | finance | live skit, 37 to 60 s | guess your subscriptions → the reveal | the app is the twist | the reveal mechanic |
| **Duolingo** | education | anime series, 5 × 60 s; the "Duo is dead" arc | a mascot world | the product mechanic is the plot (earn XP to bring Duo back) | a mascot as a character; a plot people take part in |
| **Brand dramas in China and India** (Meituan, Pupu, Taobao, Zomato, Myntra) | delivery, e-commerce | live-action series | the app saves a family dinner, a party, a job | from prop placement to a fully custom plot | the integration ladder; forced inserts and overuse kill results |

**Take the mechanism, never the material:** no competitor's characters, lines, sets, look or music in our films (base Reference B); these examples teach structure only.

**What to take from it:** dramas for apps run as systems (many heroes, pains, languages), the app comes earlier than the drama apps' own cliffhangers would suggest (30 to 60%), the messenger is either a peer with visible proof or an expert who removes an objection, realistic and animated both work, and disclosure travels with realistic AI people.

## Reference teardown: the dog training app drama

The reference the team started from (Meta Ad Library, Woofz, active from 22 Sep 2026, ~126 s). Timings approximate, from frames.

| Time | Beat | What happens | Why it works |
|---|---|---|---|
| 0 to 3 s | **Cold open, chapter "7:15"** | The heroine (red hair, glasses, mustard shirt) stands soaked in the bathroom; the poodle runs out | conflict at frame 1; a clock as chapter marker promises "a day" story |
| ~4 to 8 s | **"7:25"** | A puddle in the hallway, the poodle sits "innocently", she enters frame | escalation, comedy, the pain is the dog's behaviour, not the dog |
| ~9 to 14 s | **"8:47" office** | Late, dishevelled; a coworker looks; she: "Is it that obvious?" | the pain leaks into work; a witness |
| ~20 to 26 s | **"18:30" stairwell** | The dog pulls on the leash; the elderly neighbour: "...have to complain" | social cost rises |
| ~32 to 38 s | **"19:05" dinner** | Her partner: "They're all like that" | the home witness gives up on the problem |
| ~45 to 52 s | **"19:40" guests** | The dog jumps on guests; she: "He's just excited" | public embarrassment, the peak |
| ~59 s | **"20:15" rock bottom** | On the sofa, hugging the dog, sad; the partner looks at her | a quiet beat, empathy |
| ~66 to 73 s | **The turn** | In the park, a friend with a calm dog: "I downloaded [app] and started [named course]" | the messenger's calm dog is the proof; the app named with a real course |
| ~80 s | **"Day 14"** | Black title card | honest time jump |
| ~87 to 100 s | **Payoff** | The poodle sits calmly, brings the leash; a calm walk out of the same hallway | mirror of the 7:25 hallway |
| ~106 s | **Witness reversal** | Another owner (whose dog misbehaves) says: "Yours is so calm" | the heroine is now the friend with the calm dog |
| ~112 s | **Button** | She holds the phone (app icon screen) to camera: "Best thing that ever happened to us" | the app's identity, one warm line |
| ~113 to 126 s | **End card** | "TRY NOW" button on a paw pattern | CTA; held ~13 s, longer than needed |

Style: soft stylized 3D animation, big expressive eyes, warm interior light, detailed lived-in sets, one signature outfit for the heroine the whole film. Dialogue spoken in the clips; captions burnt in post; the clock and "Day 14" as text in post. The ad's post copy above the video names the app and lists its features from second 0. What to keep: chapter markers, witnesses, the messenger, the honest time jump, the mirror payoff, the witness reversal. What to improve: an earlier brand thread, the app's real feature visible once, a tighter Act 1, a 2 to 4 s end card.

---

## Step 1 additions: from the Brand Kit to the pain chain

1. **Brand Kit and pain map.** Read the Brand Kit (base Reference I). Build the pain map as in `lyra-video-hooks` Step 1 (audience, pains in their words, desires, objections, product truth); reuse it if one exists for this app. Find the app's row in the Category guide.
2. **The hero.** One person from the audience segment, made specific and lovable: name, age, job or life stage, one quirk, one want ("Mia, 29, junior designer, first dog, wants to be the calm, together person she pretends to be"). The hero is an underdog: likeable, trying, losing, never stupid or pathetic.
3. **The pain chain.** 3 to 6 concrete situations where the pain costs the hero something, in rising order, each with a place, a time marker and a witness. Example (fictional sleep app Calmly): 02:47 awake, scrolling, partner sighs · 07:58 oversleeps, coffee on her shirt · 10:30 falls asleep in the client meeting, boss stares · 18:40 snaps at her sister on the phone · 23:55 awake again, crying quietly.
4. **The old way.** What the hero already tried and why it failed (YouTube videos, willpower, a spreadsheet, an expensive trainer): it makes the app's difference concrete and can carry an objection ("I can't afford a trainer").
5. **The turn.** Who or what brings the app (a peer with visible proof, an expert, a stranger, the plot itself), what they say, the one feature by its real Brand Kit name, the integration level (see The app in the story), and the honest time to result.
6. **The payoff.** The same situations, now going right, and the witness reversal (the person who sighed, stared or complained notices). Only results the Brand Kit can stand behind.
7. **Intake quiz** (base Step 1: one message, multiple choice, options from the Brand Kit, the recommended option first, 4–8 questions; skip what the task or the kit already answers), with these questions plus the base quiz questions that apply:
   - Visual style: animated or realistic (offer 2 to 3 from the Style library with a recommendation), or "you decide".
   - Length: 60 to 90 s (default) or 2 min; one film or a series of episodes.
   - Voice: dialogue spoken in the clips, a narrator, or both (see Dialogue and narration).
   - Language and market.
   - The app logo and 1 to 3 screenshots (the turn and the button show the app; screenshots only, never a screen recording).
   - Approved claims, forbidden claims, the honest time to result (above all for health, money, kids and pet apps).
   - The hero: any preference on age, gender, family, pet, job; or "you decide" from the audience.

**Defaults (state, don't ask):** cold traffic · Instagram Reels / TikTok · 9:16 · **75 s** (60 to 90; 2 min on request) · always a **59 s cut** too (per Meta's specs at the time of writing, videos over 60 s lose Facebook Reels ads and in-stream placements, and over 2 min Facebook and Messenger Stories; Instagram Reels and TikTok take long videos; the media buyer checks in Ads Manager) · one complete story (series on request) · **3D animation** style · dialogue spoken in the clips, captions added in the Video Editor · English · one score for the whole film with an emotional arc, instrumental · chapter markers on screen (added in post) · app logo screen on the phone at the turn and the button · end card 2 to 4 s · Seedance 2.5, references, 720p (1080p on the user's choice), sound on · Nano Banana Pro 2K, 9:16 for every image.

**Recommended first run:** A1. Cast (the characters and the look decide everything; images are cheap), then A2. Keyframes after the user selects the sheets, then B. a pilot clip before the rest.

## Step 2 addition: concepts, then the drama concept card

**Offer three different concepts first.** Unless the user brought a fixed story, write **3 short concept options** that differ in structure, style and how the app comes in (e.g. A: a 3D day of disasters with a friend as messenger · B: a realistic comeback where the app is used inside the scenes · C: a storybook fable with a narrator), 3 lines each (logline · style · how the app comes in), with one recommended and why for this audience. The picked one becomes the concept card. Two concepts can be built for a test.

The concept the user approves (base Step 2) is a drama concept card per film:

> **D1 · "Running on Empty" · 3D animation · 75 s (+59 s, 30 s cuts) · dialogue + captions**
> Logline: a sleepless junior designer wrecks her own week until a coworker shows her the five-minute wind-down that finally lets her sleep.
> Hero: Mia, 29, junior designer, dark curly hair in a low ponytail, sage-green overshirt over a white tee · Cast: Leo (partner), Dana (boss), Jess (coworker, the messenger).
> Hook: cold open at 10:30, Mia asleep on the client's slides, Dana: "Are we… boring you?" Then a card "8 hours earlier" and the chain runs forward.
> Brand thread: in the cold open, Jess's phone lies face-up on the meeting table showing the Calmly logo screen (from the user's logo) for under a second; nobody comments.
> Pain chain: 02:47 awake, Leo sighs · 07:58 coffee on her shirt · back to 10:30, Dana's stare · 23:55 crying quietly in the kitchen.
> Turn (~45%): Jess at the coffee machine, fresh and calm: "Five minutes of Calmly's wind-down. Every night. That's it." (L2, peer messenger)
> Time jump: "Night 7" card.
> Payoff: 23:00 asleep with the timer on · 07:00 awake before the alarm · 10:30 Mia presents, Dana nods: "Great work." Leo: "You're… humming?"
> Button: Mia to camera, phone with the Calmly icon: "Turns out I just needed to switch off." End card: logo + "Free for 7 days".
> Clips: 5 × Seedance 2.5 · cold open (~9 s, the pilot) · night and morning (~20 s) · turn (~10 s) · payoff (~22 s) · button (~6 s) · music: tense-comic → quiet → warm → bright · ~110 spoken words · ad copy for Ads Manager in the script node.

The hook gets 3 to 5 options (see Openings); the plan recommends one. For a series, one card per episode and a series line (see Series option).

---

## Category guide

Starting points, not rules; the Brand Kit decides. "Seen" = we saw this category run story ads; "judgment" = our recommendation without a market example yet.

| Category | Hero and pain chain | Turn and integration | Style | Careful with | Evidence |
|---|---|---|---|---|---|
| **Pets, training** | first-time owner; mess, chewed things, pulling leash, neighbour, guests, landlord | peer with a calm pet or an ex-trainer; the price objection ("can't afford a trainer"); L2 | 3D (warm, comic) | never hurt or scare the animal; no guaranteed behaviour in N days | seen: Woofz |
| **Language learning** | traveller, expat, professional; freezes with a foreigner, a job interview, the partner's parents, a waiter | a stranger or colleague asks "heard of…?"; then the hero practises inside the scenes (AI tutor, lesson on the commute); L2 + L3 | realistic sitcom, or 3D | no fluency in days; real accents, no mockery of accents | seen: Praktika |
| **Mental health, self-care, journaling** | overwhelmed adult; bed rot, snapping at people, the same relationship pattern again | a friend, a partner, the hero's own discovery; the app as the quiet secret; L2 soft, L4 if the brand has a mascot | storybook, kawaii, knitted; or a realistic confession | no clinical crisis, self-harm or diagnosis talk; no "cures"; soft framing | seen: BetterMe Mental Health, Finch, Calm |
| **Sleep, meditation** | tired worker or parent; night scrolling, oversleeping, falling asleep in the meeting | peer with visible rest; L2 | storybook, 3D | no insomnia cure | judgment |
| **Fitness, workouts, steps** | busy parent, gym newbie; out of breath on the stairs with kids, skipped workouts, can't keep up on a hike | friend a step ahead, a coach character; L2 / L3 (a 10-minute session in the living room) | 3D, realistic | the payoff is energy and confidence, not the body; no body shaming, no kg by a date, no body before / after | judgment (most fitness apps run short skits) |
| **Finance, budgeting, saving** | young professional; card declined on a date, surprise subscriptions, rent panic, money gone by the 15th | the app reveals the leak (twist, L3) or a peer with money left (L2) | realistic, 3D | no guaranteed savings or returns; staged numbers clearly fictional; no mocking debt | seen: Rocket Money (skits) |
| **Dating** | serial bad dates, ghosting, the friend's wedding alone | the app is how they meet (L3) | realistic, 3D, anime | non-sexual; no humiliation of a gender; no guaranteed love; no fake matches | seen: Hinge skits, Tinder's interactive series |
| **Books, self-growth, brain training** | stuck professional; doomscrolling, silent in the meeting, passed over for promotion | 15 minutes a day; the bad habit personified as a villain; L2 / L4 | 3D, 2D | no income or career promises | seen: Headway's "Mr. Procrastinator" (2023) |
| **Productivity, planning, to-do** | parent or student; missed deadlines, the forgotten pick-up, 47 tabs | the app plans the day inside the scenes; L3 | 3D, realistic sitcom | no invented time saved | judgment |
| **Parenting, kids, family** | parent; homework fights, screen-time battles, bedtime chaos | another parent; L2 | storybook, 3D | kids never endangered or in distress for the plot; no blaming parents; no claims about children's results | judgment |
| **AI photo, video, creative tools** | small business owner, creator; bad photos, lost sales, hours of editing | the app's output changes the next scene (L3) | realistic, 3D | the output shown only from real results | judgment |
| **Health tracking, women's health, nutrition** | an unclear pattern, a doctor visit, meal chaos | peer or the hero's own discovery; L2 | storybook, 3D | claims only from the Brand Kit; no diagnosis | judgment |
| **E-commerce, delivery, grocery** | the party, the gift, the family dinner about to fail | the app saves the day (L3), or placement through the story (L1) | realistic, 3D | real prices and delivery times only | seen: brand dramas in China and India, Temu skits |
| **Utilities (VPN, cleaner, caller ID, scanner)** | full phone at the kid's recital, a scam call, the lost document | the app as the fix in the moment (L3) | realistic, 3D comic | no fear-mongering, no fake system alerts or OS UI | judgment |

---

## Story structures

A reference, not a menu. Pick from the pain and the audience; combine.

| Structure | Shape | Best for | Example |
|---|---|---|---|
| **A day (or week) of disasters** (default) | clock or day chapters → rock bottom → messenger → "Day N" → mirror payoff | daily-habit pains: pets, sleep, productivity, kids, money | the dog training reference |
| **Underdog comeback** | humiliation in front of someone → app → triumphant return to the same place | learning, fitness, career, language, confidence | laughed at for bad Spanish at a dinner → app → orders for everyone in Madrid |
| **Expert mentor** | the hero tries the old way and fails → an expert (trainer, teacher, coach character) sees it → the app as the affordable, at-home version of the expert | categories with a paid human alternative | the pet-shop expert in Woofz's second film |
| **Two timelines** | split or alternating "without the app / with the app" days | utilities, planning, finance | same Monday, two versions |
| **The secret** | the hero has changed and hides why, or notices someone who has it together and investigates; the app is the reveal | habits, self-care, money, beauty | Finch: "the real reason I've been cleaning the house" |
| **Confession** | one person tells their story to an audience (a panel, a podcast, a friend), the twist in the first line, cutaways to the past | mental health, relationships, money; realistic style | BetterMe: "It took me getting divorced at 35…" |
| **Relationship drama** | the pain strains a relationship (partner, parent, boss, roommate) → the app removes the friction → reconciliation | family, couples, shared money, home, health habits | the fight about the bills, settled |
| **Fail and rewind** | the hero makes the wrong move, disaster, the scene rewinds, the app path shows what goes right (borrowed from game "fail ads") | utilities, finance, learning | the scam call, rewound |
| **Rival** | a rival seems to win; the hero turns it around with the app (light, never cruel) | competitive categories, fitness | the gym "mirror guy" |
| **Fable** | animals, mascots or objects live the human pain in a small world | kawaii, storybook, knitted styles; broad or young audiences; delicate topics | the kitten who spent everything on skincare (Lyra template) |
| **Cliffhanger episode** | stops after the turn, before the payoff; the next episode resolves | series option, retargeting | "…and then Jess showed me her phone." |

**Short drama tropes, made app-safe.** Drama apps sell betrayal, revenge, hidden identity and the big comeback (betrayal, revenge, forbidden romance skew to women; hidden identity and comebacks to men, per trend reports). Use their energy, not their content: betrayal → "my own habits betrayed me" or a friend who kept the secret; revenge → the comeback in front of whoever doubted; hidden identity → "nobody knew I was the one who…"; romance → the date that went wrong because of the pain. No cheating, violence, abuse, humiliation of a group or anything the brand wouldn't put its name on (brand safety, base Reference B).

## Beat sheet

**75 s default (60 to 90 s):**

| Beat | Time | What happens | Rule |
|---|---|---|---|
| **Cold open** | 0 to 3 s | the most painful or funny moment of the chain, mid-action, first line or sound | conflict at frame 1; built with `lyra-video-hooks` |
| **Pain chain** | 3 to 28 s | 3 scenes, 6 to 8 s each, a chapter marker on each, each ends on a witness reaction; a light brand thread in one of them | escalate; one location per scene; no dead air |
| **Rock bottom** | 28 to 33 s | one quiet beat: alone, the cost lands | the only slow beat before the turn; music drops |
| **Turn** | 33 to 42 s | the messenger and their proof (or the plot device), the app named once, the one feature in one line, the phone shown | 35 to 55% of the runtime |
| **Time jump** | 42 to 44 s | title card "Day 14" / "Night 7" / "Three weeks later" | honest, from the Brand Kit |
| **Payoff** | 44 to 64 s | 2 to 3 mirror scenes in the same places, the witness reversal | show the result in life, not on a screen |
| **Button** | 64 to 72 s | the hero to camera (or to the witness), phone with the app icon, one warm line | not ad copy |
| **End card** | 72 to 75 s | logo, the real offer, install button | 2 to 4 s |

**A cold open taken from the middle of the chain** (the meeting at 10:30) is followed by a time card ("8 hours earlier") and the chain runs forward from there, or the chain simply continues forward from the cold open. Never jump back without a card.

**2 min:** the same shape, longer: pain chain of 5 to 6 scenes (an old-way attempt and an objection among them), a short subplot (the partner's patience running out), a payoff of 3 to 4 mirror scenes, the turn at ~45 to 70 s (never past ~60%).

**59 to 60 s:** pain chain of 2 to 3 scenes, payoff of 2, the turn at ~22 to 28 s.

**Cutdowns.** One drama gives four ads: the full film, a **59 s cut** (drop one pain scene and one mirror scene, end card 2 s), a **30 s cut** (cold open, 1 pain scene, turn, 1 payoff, end card ≈ 3 + 7 + 9 + 7 + 3 s) and a **10 to 15 s teaser** (the cold open, one beat of the turn, the end card). Cut only at scene boundaries: write each scene's start and end second inside each clip in the script. Each cut is its own Video Editor (no credits) with its own short music node (cheap) or the score trimmed with a fade; captions follow the clips.

---

## The app in the story

**Integration levels.** Pick one main level (L2 or L3 in most films) and add an L1 brand thread.

| Level | What it is | Use when | Example |
|---|---|---|---|
| **L1 Brand thread** | the app appears in passing before the turn, under 1 s, only as the real logo screen or a real screenshot: the messenger's phone face-up on a table, a tablet in the background | almost always; it plants recall for viewers who leave early | Jess's phone on the meeting table in the cold open |
| **L2 Messenger turn** (default) | a person shows their own result and names the app with one feature | most categories | the friend with the calm dog; the pet-shop expert |
| **L3 Plot device** | the app causes the next event or is used on screen in life | language, dating, finance, AI tools, delivery, productivity | they meet on the app; he talks with the AI tutor while cooking; the subscriptions reveal |
| **L4 The app as a character** | the brand's mascot lives in the story | only when the Brand Kit has a mascot; never invent one without the user | Finch's bird, Duolingo's owl |
| **L5 End card only** | pure story, the app only at the end | teasers and brand content; weakest for performance | — |

**Rules:**

- **On Meta and TikTok the advertiser name and the post copy sit above the video from second 0.** The film can stay story-first; the post copy carries the app name and the offer (see Ad copy).
- **The messenger shows proof.** Their result is visible in the scene (the calm dog, the fresh face, the money left) before they name the app. An expert messenger removes an objection (price, time, "I tried videos").
- **The app moves the plot.** If the scene would play the same without the app, it is a forced insert: rewrite it.
- **The phone moment.** At the brand thread, the turn and the button, the phone screen shows the **app icon / logo screen** (the user's logo on the brand color) or the user's real screenshot, made as a phone image with the logo or screenshot connected as reference, in the film's style (base Reference D). **One phone image per phone that appears** (the messenger's, the hero's), each connected as a reference to the clip where it appears. No notifications, lock screens or OS UI. Check every screen letter by letter; if it breaks, turn the screen away in the clip and lay a short UI insert or the logo screen over it in the Video Editor.
- **No logo and no screenshots:** the screen stays turned away, the app is named in the line and in the caption, and the end card waits for the logo (ask for it before the final run).
- **Never invented UI,** never a full walkthrough; one screen or the logo is enough in a drama. An AI tutor or chat on a screen is shown only from real screenshots, or as a voice the hero answers with the screen turned away.
- **The feature is a line, the result is a scene.** "She started the small dog course" (line) → "the dog brings her the leash" (scene).
- **The end card** is the app's real identity: logo, the real offer ("Free for 7 days"), an install button; made with `lyra-ui-motion-video` or uploaded by the user; 2 to 4 s.

---

## Style library

Pick one style per film and hold it to the last frame. The style is written once as a **style anchor** in the script and repeated word for word in every image and clip prompt.

| Style | Style anchor (write the look, not a studio name) | Best for | Video model | Watch out |
|---|---|---|---|---|
| **3D animation** (default) | "stylized 3D animated feature film look, soft rounded character design, big expressive eyes, subtle subsurface skin, warm global illumination, detailed lived-in sets, gentle depth of field, rich but soft colors" | most apps; wide audiences; dialogue | Seedance 2.5 refs | drift toward photoreal faces; plastic toy look; too dark interiors |
| **2D anime** | "2D anime style, clean thin lineart, cel shading with two-tone shadows, expressive eyes, painted backgrounds, soft light bloom" | Gen Z, learning, dating, games-adjacent, wellness | Seedance 2.0 refs (frames for exact shots) | lip-sync weak in flat 2D: short lines or narrator; line wobble |
| **Storybook watercolor** | "children's picture book illustration, delicate hand-drawn linework, watercolor and colored pencil textures, muted pastel palette, cozy light" | calm, learning, kids and family, wellness | Seedance 2.0 refs | stays static; narrator works best; keep scenes simple |
| **Kawaii doodle** | "ultra-simple Korean kawaii doodle, thick clean black outlines, rounded blob shapes, flat pastel colors, almost no shading, sticker style" | fables with animals or mascots; finance, beauty and habit apps for young audiences | Seedance 2.0 refs | very simple faces: emotion through posture, tears, props; music + narrator |
| **Stop-motion / knitted / clay / felt** | "fully knitted miniature world, visible stitches, tactile yarn, macro photography, shallow depth of field, warm 35mm look, subtle stop-motion feel" (or clay / felt) | emotional and wellness apps, premium feel, delicate topics | Seedance 2.0 (frames or refs) or 2.5 refs | scale errors (a giant phone); the material changes between shots |
| **Realistic: sitcom / real life** | "naturalistic real-life scene, handheld or locked-off camera, available light, real lived-in locations, natural skin texture, unpolished, natural comic timing" | language, utilities, productivity, delivery; audiences that skip polished ads | Seedance 2.5 refs | uncanny faces; overacting; see Realistic drama |
| **Realistic: vertical mini-series** | "vertical mini-series look, cinematic soft key light, motivated practical lights, shallow but readable depth, faces filling the frame, natural skin texture" | money, career, relationships, dating; audiences that live in drama apps | Seedance 2.5 refs | identity drift; melodrama tipping into parody; AI label |
| **Realistic: confession** | "one person telling their story to an audience, stage or studio light, intimate close-ups, cutaways to the past" | mental health, relationships, money | Seedance 2.5 refs | must stay clearly a dramatization; AI label |
| **Motion comic** (budget) | the chosen 2D style as illustrated panels, camera moves across each image, narrator | tight budget, a story test before a full build | Seedance 2.0 Fast or 2.0 (frames), slow push-ins | feels cheap if the story is weak; for story tests |

**Style rules:**

- **No studio, franchise or artist names** in prompts and never a known character or a lookalike. Describe the look (shapes, lines, shading, light, palette, textures). It keeps the style ours, keeps the models from refusing, and keeps the brand safe.
- **The Brand Kit's palette sets the world.** One dominant color family from the brand, kept in sets and the hero's outfit; the payoff can be a little brighter and warmer than the pain chain (the light change is part of the story).
- **Style drift is the main risk in a long film.** The style anchor goes first in every prompt, the character sheet is a reference in every image and clip, one image model and one video model for the whole film.
- **Choose with the user.** Offer 2 to 3 styles with one line each and a recommendation tied to the audience and category. A strong test set for one story is the same script in an animated and a realistic style.

## Realistic drama

Three flavours, all on Seedance 2.5 with references, all built with the realism rules of `lyra-ugc-video` (real skin, lived-in places, casting from the audience, never "flawless") but with motivated cinematic light instead of phone-real.

| Flavour | Looks like | Writing | Camera and acting |
|---|---|---|---|
| **Sitcom / real life** (Praktika-like) | an overheard real situation: a plane, a kitchen, an office | situational comedy; a stranger or colleague starts the turn early; the app used inside later scenes | handheld or locked-off, eye level; natural acting with comic timing; real ambience |
| **Vertical mini-series** (ReelShort-like) | a heightened soap: faces fill the frame, reaction close-ups, a big reveal | high-concept first line, a reveal, a reversal; the comeback | close-ups and reaction beats written into the script; rack focus; end each scene on the most surprised face, not on the reveal itself; acting heightened but not parody |
| **Confession** (BetterMe-like) | one person telling an audience what changed their life | the twist in the first line; short past flashes; the app as the moment they understood | a stage, a podcast set or a sofa; close-ups and listeners' reactions; one speaker |

**Craft rules for realistic AI drama** (practitioner tips):

- 1 to 2 short sentences per shot; on a longer line, cut away from the mouth to a listener or a detail.
- One camera axis per dialogue exchange: reverse angles make backgrounds drift; a new location is safer than a new angle.
- Frame above the hands when you can; hands are the most visible AI tell.
- Layer room tone and ambience under every line; silence exposes AI voices.
- Same signature wardrobe through the film; a change of outfit only with a new character image.
- **Fiction frame:** the characters never claim to be real customers. Confession-style lines ("I used this app and…") are a dramatization: say so (see Truth and safety). The AI label goes on; for the EU, a small in-frame "AI-generated" note is the safe default for realistic people (the BetterMe ad does this).

---

## Cast: characters and consistency

A 60 to 120 s film is 3 to 8 clips on Seedance 2.5, 6 to 15 on Seedance 2.0; holding the same faces through all of them is the hardest technical part. Consistency comes only from images connected as references and anchors repeated in prompts (base Reference E), never from a text node.

**Character card.** For every character, written once in the script node and repeated word for word in every prompt where they appear:

> Mia (hero) · 29 · junior designer · warm olive skin, a few freckles, dark curly hair in a low ponytail, small gold hoop earrings · sage-green overshirt over a white tee, dark jeans, white sneakers · expressive, clumsy, kind · voice: young woman, late 20s, warm American accent, a little breathless when stressed

**Signature outfit.** One outfit per character for the whole film (cartoon logic, and it helps the model hold identity). Change it only when the story needs it (pyjamas at night), and then make a second character image from the first.

**Cast size.** The hero plus 2 to 4 side characters (the witnesses and the messenger). Pets and mascots count as characters and get their own sheet. A witness who appears once can stay unnamed but still gets a one-line card ("the neighbour: woman, 70s, grey bob, lilac cardigan, slippers").

**Character sheet images (stage 1):** one Nano Banana Pro image per character, 9:16, 2K, count 2 (the user picks one): full body, front three-quarter view, neutral pose, plain soft background, the style anchor and the card word for word. For the hero of a long film, a second sheet with a close-up of the face (and, for realistic drama, a profile) helps hold identity across angles. These are the references for every keyframe and clip.

**Location keyframes:** one image per scene, made **with the character sheets as input images** ("Use the exact characters from the reference images… new scene: …"), so face, outfit and style carry over (as Lyra's own story templates chain their scene images). One keyframe per place is enough when several scenes happen there; mirror scenes in the payoff reuse the pain chain's keyframe, changed by light and props ("the same hallway, morning sun, the puddle gone, the dog sitting calmly").

**References per clip:** a small, purposeful set: the characters in the clip + the location keyframe(s), usually 2 to 4. Assign each in the prompt: "[Image1] is Mia… [Image2] is Leo… [Image3] is the kitchen at night". Never connect the whole cast to every clip.

**Voices:** one voice anchor per character in the card, word for word in every clip where they speak; one narrator voice for the whole film.

**What hides drift between clips:** chapter cards and title cards between scenes, cuts on action, a cut to a reaction or a detail (the dog's paws, the coffee stain), and the stylized look itself. Plan these cuts in the script.

---

## Dialogue and narration

Three modes; pick in the plan, by style and by what the user prefers. **No mode ever generates text in the clip:** every clip prompt says "no subtitles, no captions, no on-screen text"; captions, chapter markers and title cards are added in the Video Editor.

| Mode | How | Best for | Watch out |
|---|---|---|---|
| **A. Dialogue in the clip** (default for 3D and realistic) | the lines in quotes in the clip prompt, each tied to its speaker by [ImageN]; Seedance makes voice and lip-sync | the series feel; 3D, realistic | wrong speaker; voices drift between clips; the model adds its own subtitles |
| **B. Narrator** | an ElevenLabs voiceover (the hero's diary voice "I used to…" or a third-person storyteller) over clips with ambience and action sound only | 2D, kawaii, storybook, stop-motion; exact wording; cheap localization | less "series" feel; VO must match the cuts |
| **C. Mixed** | dialogue in the key scenes (witness lines, the turn, the button), the hero's inner voice over the montage (the pain chain fast-cut, the "Day 14" payoff) | longer films; montage-heavy stories; confessions | two voice sources must sound like the same person: the inner voice uses the hero's voice anchor |

**Writing the lines:**

- **Short and in character.** One line per 3 to 5 s of screen; most lines under 8 words. A witness line is a reaction ("Are we… boring you?"), not an explanation.
- **Subtext over exposition.** "He's just excited" tells us she's embarrassed; "My dog is untrained and it's ruining my life" tells us nothing we feel.
- **The objection can be a line.** "I can't afford a trainer", "I've watched a hundred YouTube videos": the messenger's answer is the app's value.
- **The app is named once** by the messenger (or appears through the plot), with the one feature by its real Brand Kit name. The hero's button line can name it again or just show the phone.
- **Word budget:** a drama breathes. Plan about 1.5 to 2 spoken words per second across the film (75 s ≈ 110 to 150 words), up to 2.5 inside a dialogue scene; the narrator at 2.0 to 2.5. Count them per clip.
- **Spoken numbers and names** as pronounced; check the app name in every result.
- **Language:** write natively for the market, not translated word for word. In mode A another language means new clips (or mode B for that market); in mode B only the VO changes, the clips stay (`lyra-audience-variations` for the rest).

**Voice consistency across clips (mode A).** Same voice anchor, same model, one speaker per line. If a voice drifts, offer: regenerate the clip; or **voice lock**: record each character's lines as a voiceover node (the ElevenLabs model `list_node_configs` lists first; one saved voice per character), then give Seedance 2.5 that audio as reference for lip-sync (up to 30 s of audio per clip). In a two-speaker clip, [Audio1] is one character's lines and [Audio2] the other's, each tied to its speaker in the prompt; if the wrong mouth moves, one clip per speaker. Exact words and the same voices in every clip, a little less natural acting (base Reference C).

**Music.** One score for the whole film (`elevenlabs/music`, instrumental, length = film + ~5 s) with an arc written in the brief: light comic tension in the pain chain → it drops out or goes soft at rock bottom → a warm lift at the turn → bright and resolved at the payoff → a short button for the end card. Or two tracks (before / after) crossfaded at the time jump. Under dialogue about 0.1 to 0.2 track volume; up to ~0.3 under a narrator; louder in the title cards only if the music track is split there (otherwise keep one level). The times in the music brief are approximate; align by trimming in the editor. Clip prompts: "Sound: dialogue and natural ambience only, no music, no score."

**Captions.** Asked first in the approval message (base rule). If yes: all speech, added in the Video Editor, by the base rule (`lyra-video-editor` → Captions): size 80, at 75% of the height (y = 1440 on 1080×1920), never over a face, high-contrast, one place. Series look: white with a dark outline or shadow; karaoke style (the editor's active-word highlight in a brand color, used in Lyra's own story templates) also works well in this format. The user checks the words and the app name.

**Chapter markers and title cards.** Clock times ("7:15"), days ("Day 14"), places ("Monday"): text added in the Video Editor over the first second of each scene; a full title card is a plain black or brand-color 9:16 image (uploaded, or a plain Nano Banana Pro image without text) held 1 to 1.5 s with the text added in the editor. Text and captions are added in the editor's interface: in the final report, list for the user exactly which captions, chapter markers and title cards to add and where.

---

## Openings (use `lyra-video-hooks`)

The cold open decides whether anyone sees the story; most viewers decide in the first 3 s. Read `lyra-video-hooks` and write 3 to 5 opening options in the concept, one recommended:

- **Peak disaster, mid-action** (default): the worst or funniest moment of the pain chain, already happening ("soaked in the bathroom, the dog bolting").
- **Conflict line:** a witness says the sharpest line at frame 1 ("You have to do something about that dog.").
- **Twist first line** (confession, realistic): "It took me getting divorced at 35 to realize…".
- **Fast chaos montage:** 4 quick shots of the pain chain in the first 6 s, then the story starts.
- **Flash-forward:** a glimpse of the payoff, then "3 weeks earlier…" (good when the payoff is visual and surprising).
- **Fourth-wall aside:** the hero looks at us: "This is me. Day one of being a dog mom." Then chaos.
- **Chapter clock on chaos:** "7:15" over a crash sound and the aftermath.

For a test, keep one body and build N openings (hook skill, mode A): only the first 3 to 6 s change (Praktika runs one opener on several bodies; the reverse also works). Caption on frame 1, 2 to 6 words. Hook code in the final's name.

## Ad copy around the video

Write it into the script node as "Ad copy (for Ads Manager)", for the user or media buyer to paste:

- **Primary text:** line 1 continues the story's hook in a few words ("She almost gave him back."), then the app name and 3 to 5 real features as short lines (the Woofz pattern), the offer, the CTA. Only Brand Kit facts.
- **Headline:** the promise or the offer in 5 to 8 words.
- **One per language**, written natively.

---

## Series option

On request, or when the story is long and the user wants retargeting:

- **2 to 3 episodes, 60 to 90 s each,** one workflow with a shared **Cast** section (character sheets, location keyframes) and one Section per episode, each with its own clips and Video Editor.
- **Each episode is a complete ad:** it opens on conflict, has its own mini arc, names the app and ends with the end card (cliffhangers alone don't make people come back). Episode 1 includes the turn and stops before the payoff ("…tomorrow I'll find out if it works."); episode 2 opens with a 2 to 3 s "previously" flash and pays off; episode 3 can be another pain or the comeback.
- **Episode markers** in post: "Episode 1", "Part 2" on frame 1 or the end card.
- **Media plan line for the report:** run episode 1 to cold audiences; retarget people who watched 50%+ of it with episode 2 (a video-viewer audience or ad sequencing, where the campaign type allows it; app campaigns can limit this); exclude installers. The user's media buyer decides; this is a suggestion.
- Naming adds the episode: `…-E1`, `…-E2`.

---

## Best way to build it

The user's explicit choices override any row. Models and prices: base Reference A.

| If the drama is | Best approach (graph) | Models |
|---|---|---|
| **60 to 90 s, 3D or realistic, dialogue** (default) | Story script (text) → character sheets (count 2, user picks) → location keyframes from the sheets → phone image (hero + logo or screenshot) → **pilot clip** (the cold open scene) → after the user's OK, the remaining **3 to 4 clips of 15 to 30 s**, grouped by place and cast, each with "cut to" shots inside → music → Video Editors (the film, the 59 s cut, the 30 s cut, the teaser) | nano-banana-pro · seedance-2.5 · elevenlabs/music |
| 2 min | as default, 5 to 6 clips | same |
| 2D anime, storybook, kawaii | as default, but clips of 8 to 15 s on Seedance 2.0 (6 to 9 clips for 75 s); narrator (mode B) by default; multi-shot clips take the character sheets and keyframes as references (as Lyra's Bunny and Kitten story templates do); a single-shot clip that must match its keyframe exactly takes it as first frame instead; never frames and references in one node; frame links are made right after the keyframe has a result (base Step 4) | nano-banana-pro · seedance-2.0 · elevenlabs VO + music |
| Stop-motion, knitted, clay, felt | keyframe per scene; one video model for the whole film: Seedance 2.0 with the keyframe as first frame (as Lyra's Knitted Doll template) when the film is narrated, Seedance 2.5 refs when characters speak; "subtle stop-motion feel" in every clip | nano-banana-pro · seedance-2.0 or 2.5 |
| Realistic confession | one speaker sheet (face close-up + full body) → the set keyframe → 2 to 3 clips of the talk with listener cutaways → past flashes as short clips → mode C | nano-banana-pro · seedance-2.5 |
| Exact words or fixed voices (mode A, voice lock) | each character's lines as ElevenLabs VO → audio reference in the Seedance 2.5 clip | elevenlabs (v4 / v3 as listed) · seedance-2.5 |
| Series of 2 to 3 episodes | one workflow: shared Cast section, a Section and a Video Editor per episode | as default |
| A drama system (many heroes for one app) | build the first film; each new hero, pain chain or language as a Lyra variation of it (`lyra-audience-variations`, `lyra-ad-concept-multiplier`) | as default |
| Several openings on one film | the film here, openings from `lyra-video-hooks` mode A, each its own short clip cut onto the shared body | as the hooks skill |
| Another market | mode B: new VO only; mode A: new clips with lines written in that language (or voice lock); `lyra-audience-variations` for the rest | as default |
| Tight budget or story test | motion comic (keyframes + slow camera moves) or drafts on Seedance 2.0 Fast at 720p; rerun the winning story on the full models | seedance-2.0-fast · seedance-2.0 |
| A competitor's drama to adapt | `lyra-copy-competitor-ad` analysis (beats, timing, mechanism) → this skill's build with our hero, pain chain and app | as default |

**Clip plan.** A clip holds the scenes that share a place and a cast (Seedance 2.5 up to 30 s, Seedance 2.0 up to 15 s), with "cut to" shots inside; a new place usually means a new clip. The cold open is its own clip (the pilot, and the piece replaced in hook tests). The turn gets its own clip (the most important scene for the ad). Write the end state of every clip; the next clip starts from it. Clips are trimmed in the Video Editor, never stretched.

**Pilot clip gate.** Before spending on 4 to 8 clips, run one: the cold open with the hero and a witness. The user checks style, faces, voices, lip-sync and the pace. Fix the prompt, the references or the model on the pilot; only then run the rest. Say this in the plan; it saves the most credits in this format.

**Video Editor.** One `video_composer` per film and per cutdown: clips in playback order → title cards and chapter markers on the layer above → the phone or logo insert if needed → the end card → music on its own track (no clip with dialogue carries music), the clips' own sound kept for dialogue and ambience, the VO track in mode B or C. Captions for all speech, if the user said yes. Check the order and set `startMs` after the clips have results.

**Layout.** Section "Story" (story script, cast cards, ad copy) → Section "Cast" (character sheets, uploads: logo, screenshots) → Section "Keyframes" (locations, phone image) → Section per act or episode ("Act 1: the bad day", "Act 2: the turn", "Act 3: the payoff") with its clips → Section "Audio" → Section "Final" (Video Editors: film and cutdowns). Labels: "Cast: Mia", "Place: kitchen night", "Clip 2: office disasters (24 s)", "Final: D1 75 s", "Cut: D1 59 s", "Cut: D1 30 s".

## Run options for short drama

**Run order, not a menu** (base Step 6): after the user's yes, run all of it in this order without offering options. Stop between stages (the look first, then the rest) only when the user asked for it, or when the plan is expensive and that was said in the approval message.

As in the base skill, credits are read from the nodes, never guessed. This is the most expensive format in the set: in the plan, say so and give the clip count × seconds per clip; in Run options, read every node's price and show each option's credits plus the whole-film total, before anything runs.

| Option | Runs | Results | Credits | Time |
|---|---|---|---|---|
| **A1. Cast (recommended first)** | character sheets (count 2) | the faces and the look; the user selects one sheet per character in Lyra | {x} | ~1 min |
| **A2. Keyframes** | location keyframes + phone images (from the selected sheets) | every scene's look | {x} | ~1 to 2 min |
| **B. Pilot clip** | the cold open clip | style, faces, voices checked on one clip | {x} | ~3 min |
| **C. The rest of the film** | remaining clips + music (+ VO in modes B and C) | all pieces | {x} | ~5 to 10 min |
| **D. Final** | Video Editors (no credits) | the film and the cutdowns | 0 | ~1 min |

Whole film: {x} credits · balance {X}. Run A1, then A2 after the user's selection (references pin to the selected result), then B, then C.

---

## Prompt rules (short drama)

| Node | Write | Avoid |
|---|---|---|
| Story script (text node) | logline · style anchor · cast cards with voice anchors · the beat sheet with times, chapter markers, places, witnesses, the brand thread · every line per clip with its speaker and word count · title cards · captions marked for post · music arc · end card · cutdowns · ad copy | ad copy inside the film's lines; claims not in the Brand Kit; a single block of prose without timings |
| Character sheet | style anchor → the card word for word → full body, front three-quarter, neutral pose, plain soft background → "single character, one image, no text" | studio or artist names; text; several poses in one image (unless a turnaround is wanted) |
| Location keyframe | "Use the exact characters and style from the reference images" → the scene: who, where, doing what, the emotion at the start of the scene → the set with 2 to 3 story details (the puddle, the coffee stain) → light and time of day → framing for 9:16 → "single illustration, one scene, no comic panels, no speech bubbles, no text" (for realistic: "single photograph, one scene, no text") | re-describing the faces (the reference holds them); comic panels; captions |
| Phone image | the hero holding the phone toward the camera in the style, the screen showing the logo or screenshot from the reference "exactly as in the reference, every letter" | an invented UI; a placeholder app name |
| Clip (Seedance 2.5, references) | style anchor first → roles: "[Image1] is Mia… [Image2] is the kitchen at night" → the scene and its shots with "cut to" → the action before each line → each line in quotes after its speaker, the listener silent → acting through actions (she freezes, he blinks slowly) → camera per shot → "Sound: dialogue and natural ambience only (the scene's own sounds: a door, steps, cups); no music, no background music, no soundtrack, no score" → the end state → "No subtitles, no captions, no on-screen text" → short Avoid line | stage directions inside quotes; more than one line per 3 s; music in the clip; the full look re-described |
| Clip (Seedance 2.0, 2D) | style anchor → roles → one simple action per shot, expressive poses → slow camera moves → sound line (no speech in mode B) → end state → no text | complex choreography; long dialogue in flat 2D |
| Narrator VO | the exact words only, one continuous text, sized to the film minus ~1 s, the hero's voice or a storyteller | labels, brackets, "(sad)", scene names |
| Music brief | genre, tempo, instruments, the arc with times (comic tension 0 to 28 s → soft 28 to 33 s → warm lift 33 s → bright 44 s → resolve on the end card), instrumental only, length = film + 5 s | artist or film names; vocals |

**Pattern: clip with dialogue (Seedance 2.5, references, 3D animation).**

> Style: stylized 3D animated feature film look, soft rounded character design, big expressive eyes, warm global illumination, detailed lived-in sets. [Image1] is Mia: dark curly hair in a low ponytail, small gold hoops, sage-green overshirt, white tee. [Image2] is Dana, her boss: sharp grey bob, black blazer, red reading glasses. [Image3] is the glass meeting room at 10:30, morning light, a client presentation on the screen. Shot 1, medium shot: Mia is asleep upright at the table, her cheek sliding slowly down her hand. Dana stops mid-sentence, lowers her glasses and says flatly: "Are we… boring you?" Cut to: close-up, Mia jolts awake, a sticky note stuck to her cheek, eyes wide. She says: "No! No. I was… visualising." Cut to: Dana's slow blink, she says nothing. Dialogue and natural office ambience only, no music, no background music, no soundtrack, no score. Each line spoken by its speaker only, the listener silent. Ends on Mia peeling the sticky note off, mortified. No subtitles, no captions, no on-screen text. Avoid: photoreal faces, identity drift, outfit change, extra fingers, flicker.

(9 spoken words in a ~9 s clip: the 3 s cold open plus the first beat after it; this clip is also the pilot. When the brand thread is planned here, connect the messenger's phone image as [Image4] and add one line: "on the table, Jess's phone lies face-up showing the screen from [Image4]".)

**Pattern: location keyframe from the character sheets.**

> Use the exact characters, faces, outfits and style from the reference images. Stylized 3D animated feature film look, soft rounded character design, warm global illumination. New scene: a small kitchen at 23:55, Mia sits on the floor against the fridge, still in her overshirt, hair down, with a mug, the phone's light on her face, tired and teary; a sink of dishes, a half-eaten cereal bowl, her work badge on the counter. Cool blue night light from the window, a warm stove lamp. Vertical 9:16, Mia in the lower middle third. Single illustration, one scene, no comic panels, no speech bubbles, no text.

**Pattern: realistic sitcom clip (Seedance 2.5, references).**

> Naturalistic real-life scene, handheld camera at eye level, available daylight, natural skin texture, unpolished. [Image1] is Rafael: early 30s, short dark hair, light stubble, rust-colored t-shirt, a backpack. [Image2] is the barista: late 40s, grey beard, rolled-up sleeves, a canvas apron. [Image3] is a small café abroad, a counter with pastries, a queue behind Rafael, morning light from the street. Rafael tries to order, the barista answers fast in the local language, Rafael freezes and points at a pastry. Cut to: the woman behind him in the queue, hiding a smile. Cut to: the barista slides the coffee over and says kindly, slowly: "Next time, you order in full sentences, okay?" Rafael laughs at himself: "Deal." Dialogue and café ambience only, cups and street noise, no music, no background music, no soundtrack, no score. Each line spoken by its speaker only. Ends on Rafael stepping outside and taking out his phone. No subtitles, no captions, no on-screen text. Avoid: identity drift, plastic skin, warped hands, people turning to camera.

(The cold open and first pain beat of a fictional language app's comeback story; in a real build the app, the lines and the market come from the user's Brand Kit.)

**Drama prompt checklist:** style anchor · who is who ([ImageN]) · where and when (time marker) · one action per shot · the line and its speaker · the emotion at this beat · camera per shot · light (pain chain cooler, payoff warmer) · sound line · end state · no text.

## De-slop for short drama

Base Reference H, plus what breaks long stories:

- **Style drift:** 3D turns photoreal in close-ups, 2D gains 3D shading, the knitted world turns plastic, realistic skin turns waxy. Prevent: the style anchor first in every prompt, the sheets as references, one model per film; "Avoid: photoreal faces" in stylized clips.
- **Character drift between clips:** hair, glasses, outfit color, the dog's breed change. Prevent: signature outfits, cards word for word, 2 to 4 references per clip, cuts on chapter cards.
- **Generated text:** the model adds subtitles to dialogue scenes, writes on screens, signs and phones. Prevent: "No subtitles, no captions, no on-screen text" in every clip; real logo only through the phone image.
- **Dialogue slop:** the wrong character speaks, both talk, mouth moves with no words, voice too old or too young for the face, the app name garbled, silence under AI voices.
- **Story slop:** the viewer can't tell who the hero is in 3 s; scenes that don't escalate; the app arriving in the last third, or as a forced insert; an instant magic fix; a payoff that doesn't mirror the pain; a "happy montage" with no witness.
- **Acting slop:** constant smiling, floaty gestures, everyone overacting at once. Big acting is fine, but one clear emotion per beat; in realistic drama, heightened but never parody.
- **Edit slop:** dead air between lines, cuts that jump the axis, the music fighting the dialogue, the end card held 10+ s, chapter markers outside the safe zone.

---

## Truth and safety

- **The drama is fiction.** Characters are invented, the story is a creative scene, never presented as a real customer's story. A witness or messenger line is dialogue, not a review. Real reviews and ratings appear only as text on the end card, attributed.
- **Dramatizations stay dramatizations.** In the US, people presented as actual customers must be real or clearly disclosed as not (FTC Endorsement Guides; the FTC rule on fake and AI reviews bans AI testimonials that misrepresent the speaker). A confession or a first-person "I used this app" scene with an AI person gets a visible "Dramatization" / "AI-generated story" note.
- **AI labels.** Meta labels and detects AI content (C2PA); TikTok requires the "AI-generated content" box on fully AI ads. Under the EU AI Act (Article 50, applying from 2 Aug 2026 per legal analyses at the time of writing) realistic synthetic people are expected to carry a visible label at first exposure, and the platform's label alone may not cover the advertiser; clearly stylized animation is less likely to count, but keep the platform label on. Tell the user once in the final report. Not legal advice; they check current rules.
- **Only Brand Kit claims.** The feature, the program names, the time to result ("Day 14" only if the Brand Kit supports two weeks), the offer, prices. No health, money, weight, pet behaviour or child results the app can't stand behind; no body before / after.
- **No real people, celebrities, creators, studio characters or lookalikes;** no studio or franchise names in prompts; no cloned voices.
- **Story formats that imitate platforms** (a forum post, a chat, comments): never copy a real platform's interface, logo or name, and never fake user comments as social proof. Write a neutral, clearly fictional post or chat, or use the film instead.
- **Brand-safe drama** (base Reference B): no violence, abuse, cheating, humiliation of a group, profanity, politics or competitor digs; minors only as side characters in family scenes, never in distress for the plot; pets are never hurt; mental health without crisis, self-harm or cure claims; the Brand Kit's forbidden claims enforced absolutely.

---

## Deliverable and naming

1. A "Story script" text node: logline, style anchor, cast cards, beat sheet, lines per clip, title cards, captions marked for post, music arc, cutdowns, ad copy.
2. Character sheets, location keyframes, the phone image, clips, music (and VO).
3. The finished film in its Video Editor plus the cutdowns (59 s, 30 s, teaser), and one Video Editor per episode in a series.

Name every final with a code the media buyer can paste into Ads Manager: `B{batch}-A:{angle}-F:Drama-{style}-{length}-C{concept}H{hook}[-E{episode}]`, e.g. `B3-A:SleepWrecksWeek-F:Drama-3D-75s-C1H2`, `B3-A:SleepWrecksWeek-F:Drama-3D-59cut-C1H2`, `…-Real-…`, `…-E2`. Node label: "Final: D1 · 3D · 75 s · H2".

---

## Common mistakes (short drama)

| Mistake | Prevention |
|---|---|
| Different background music inside the clips, fighting the score under the dialogue | Every clip: dialogue and scene sounds only, "no music, no background music, no soundtrack, no score"; the score only in the Video Editor; rerun a clip that still has music (base Reference C) |
| One concept offered when the user asked for ideas | Three different concepts (structure, style, integration), one recommended |
| Story without a pain map: a generic sad person, a generic happy person | Pain map → hero → pain chain from the Brand Kit; the Category guide |
| Opens on an establishing shot, a sunrise or a logo | Cold open at the peak of a disaster; `lyra-video-hooks` |
| Pain scenes that repeat instead of escalating | Each scene costs more: time → money → face → a relationship |
| The app only in the last third, so most viewers never see it | Brand thread early; the turn at 35 to 55% (up to ~60% in 2 min) |
| The app as a forced insert | The app moves the plot (L2 or L3) |
| The app fixes everything instantly | An honest time card from the Brand Kit |
| Payoff in new places with new people | Mirror scenes, the witness reversal |
| A studio or franchise name in prompts, a known character's look | Describe the look; original characters only |
| Style or faces drift across clips | Style anchor first, character sheets as references, signature outfits, one model |
| The whole cast connected to every clip | 2 to 4 purposeful references per clip |
| Subtitles or text generated in the clip | "No subtitles, no captions, no on-screen text"; captions in the editor |
| Lines too long, rushed voices, the wrong speaker | One line per 3 to 5 s, speaker by [ImageN], listener silent; voice lock if needed |
| Realistic AI people presented as real customers | Fiction frame; "Dramatization" / AI note; AI label |
| Invented app UI on the phone | Logo screen or real screenshot through the phone image; else screen away |
| All clips run at once, the style fails on clip 5 | Pilot clip gate |
| One score with vocals or a track that ends early | Instrumental, film + 5 s, an arc, trimmed with a fade |
| Only a 75 s+ version | The 59 s cut for all Meta placements, plus 30 s and a teaser |
| End card held 10+ s | 2 to 4 s |
| One drama and done | A drama system: new heroes, pains and languages as variations |
| Melodrama tropes that hurt the brand | App-safe versions; brand safety |
| Forgetting the AI label | One line in the final report |

## Quality gates (short drama)

- **Stage 0 (story, Claude checks before sending):** three concepts offered (unless the story was given)? The logline has a hero, a pain, a turn, a payoff? The hero is likeable and from the audience? Conflict in the first 3 s? Every pain scene escalates and has a witness? A brand thread early, the turn at 35 to 55% (up to ~60% in 2 min), through a messenger or the plot, with one real feature? An honest time jump? The payoff mirrors the pain, with a witness reversal? Lines counted per clip? No claims outside the Brand Kit? No studio names? Cutdowns and ad copy planned?
- **Stage 1 (cast and keyframes):** each character looks the same in every keyframe? The style is the same everywhere? The emotion at the start of each scene reads at a glance? The phone shows the logo or screenshot exactly, or is turned away? No text in images?
- **Stage 2 (pilot, then all clips):** faces, outfits and style hold within and across clips? The right person speaks, the lip-sync fits, the voices fit the faces and stay the same? Acting reads muted? No generated subtitles or text? Each clip ends on its planned end state?
- **Stage 3 (final), app ad check:** does a viewer who leaves at 10 s know the app and the promise? Does a muted viewer understand the story with captions? Is it clear what the app does for the hero, and is that what the store page and the first session give? Is the CTA an install or trial step with the real offer?
- **Stage 3 (final):** hook in 1.5 to 3 s? Beats in order, the turn at 35 to 55% (up to ~60% in 2 min)? Chapter markers inside the safe zone, captions (if the user said yes) size 80, at 75% of the height, not over a face? Music under the dialogue, the arc landing at the turn and the payoff? End card 2 to 4 s? 9:16, planned resolution (720p by default), the planned length? 59 s, 30 s and teaser cuts made? Dramatization note where needed? Named with its code? AI label reminder given?

## After the test

Read the drama by where people leave, not only by CTR:

- **Hook rate** (3 s plays ÷ impressions; above 30% good, under 20% weak, base Reference J), **hold rate** (ThruPlays ÷ 3 s plays; about 40 to 50%; a ThruPlay counts at 15 s, so for long ads also read the retention curve), plays at 25 / 50 / 75 / 100%, the share who reach the turn; on TikTok, 2 s and 6 s views and quartiles.
- Then installs per 1,000 impressions, cost per trial, trial to paid and day-7 retention. Dramas can bring fewer but better clicks; judge them by trials and payers, against your best UGC.

**Diagnose:** drop in the first 3 s → new cold opens (`lyra-video-hooks`); drop in the pain chain → shorter Act 1, the 59 s or 30 s cut; viewers reach the turn but don't install → the turn or the offer (a clearer feature line, stronger messenger proof, an objection answered); good results on the full film only → keep it, but put budget behind the cut that wins on cost per trial.

**Then build the system:** new openings on the winner; a new hero on the same story (`lyra-audience-variations`); a new pain chain or messenger on the same cast (`lyra-ad-concept-multiplier`, mode B); the same script in the other style (animated ↔ realistic); other languages; the next episode. The format fatigues fast, so plan 2 to 3 new variants for every winner.
