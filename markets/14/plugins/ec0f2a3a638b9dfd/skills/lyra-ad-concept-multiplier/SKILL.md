---
name: lyra-ad-concept-multiplier
description: "Use when the user wants more ads from a winning concept, e.g. \"more ads like this winner\", \"same concept, new angles\", \"multiply this concept\", a concept name like \"Authority figure\", \"1 concept, 4 angles, 20 hooks\", \"same format, different pain / story\", \"the angle is tired, keep the format\", \"iterate on the winner\". Builds each angle as a Lyra variation. New openings only go to lyra-video-hooks, another person or market to lyra-audience-variations."
---

# lyra-ad-concept-multiplier

Mini skill. Takes a concept that works (or one the team wants to explore) and makes **new ads on it with new angles**. There are two ways to do it, and they mean different things by "angle", so the user picks one (or both, as two separate rounds):

**Canvas layout → `lyra-workflow-layout`.** Every workflow this skill builds or changes is laid out by `lyra-workflow-layout`: sections in reading order with a STEP note above each one, the team's color code, clear node labels and the final check. The layout lines in this file only say which sections this creative needs.

- **A. Perspectives** (the team framework: concept → angles → hooks). The concept is a creative mechanism in 3 to 4 words ("Authority figure"). Each angle is a new perspective inside it, often a new voice with its own argument (the doctor, the teacher, the trainer, the mom), and each angle gets its own hooks. One concept → 3 to 4 angles → about 5 hooks each.
- **B. Reasons** (the proven wrapper). A winning ad keeps everything that made it work (format, beats, timing, hook mechanism, camera, person, look, music, CTA), and only the reason to care changes: another pain, desire, objection, moment or feature from the Brand Kit, in the situation where it happens. One winner → 3 new angles + the original as control.

One new angle = one Lyra **variation** of the original workflow.

**Why it works.** A concept is the expensive thing to find; angles are where the next wins usually are. Mode A expands a concept into the space around it and finds which perspective carries it best. Mode B keeps a proven wrapper and finds which reason to care sells inside it, as a clean test of one thing. Both give ads that are new to the viewer and to the platform (new words, new people or places, a new story), which Meta's delivery needs: it groups near-identical creatives as one (check the current behaviour).

**This is a way of thinking, not a script.** The rules below are defaults and good practice. Use judgment: when a different angle, situation or build serves the concept better, do it and say why in one line. Only a few things are fixed: truth (no invented claims, reviews, numbers or credentials; an AI person is never a real customer or a real expert), the Brand Kit's facts (every angle is a real pain or desire answered by a real feature), the locked part of the mode the user picked, the product and its real UI, Lyra's technical limits, and the user's explicit choices.

**Method.** The team framework (concept → angle → hook, each level tested separately), GBP (Gut, Brain, Pocket) and More, Better, New. `lyra-video-hooks` is MORE on the Gut (new openings, same body). `lyra-audience-variations` keeps the Brain and changes the world it is shown in. This skill is **MORE on the Brain**: new angles on a concept. The Pocket (CTA, offer, end card) stays.

**Base skill first.** Everything not written here follows `lyra-video-ad-generation`: the 8 steps, instruction order, app card, plan table and stages, run options with credits, run and report, prompt rules, models (Reference A), brief and scenes (B), audio (C), app UI (D), consistency (E), prompt craft (F), errors (G), de-slop (H), Brand Kit (I), Meta app ads (J). This file only adds what is specific to multiplying a concept. If the two disagree, the user wins, then this file, then the base skill.

**Other skills for their parts.**
- Person, place, voice, speech, camera setups, formats, realism, casting → `lyra-ugc-video`.
- Hooks: the ~5 hooks per angle in mode A, the hook line of every angle in mode B (same mechanism, new words), new openings on a winning angle → `lyra-video-hooks`.
- A new feature screen, a UI moment or the end card → `lyra-ui-motion-video` (only the user's screenshots, checked word by word).
- The same script for another person, segment or market → `lyra-audience-variations`.
- A competitor's ad as the source → `lyra-copy-competitor-ad` first; the multiplier works on our own version once it exists.

---

## The words: concept, angle, hook

The team uses the three levels from the framework ("a zoom-in effect"):

| Level | What it is | Size | Example (fitness app) |
|---|---|---|---|
| **Concept** | the basic creative mechanism, the big idea or format | 3 to 4 words | Authority figure · Before/After · Social proof · Challenge · Myth-busting · POV · Warning · Negative emotion |
| **Angle** | a specific perspective inside the concept: who says it, from which lens, with which persuasive point | 6 to 7 words | "A trainer tells clients about protein timing" |
| **Hook** | the execution that earns attention in the first seconds | 1 sentence | "Stop doing crunches." |

Other sources order these words differently (some put the angle, as the argument, above the concept). In Lyra skills the team order is used: concept → angle → hook. Two more terms:
- **The built concept** is one specific ad made on a concept (code `C1` in names); it may have been built with any of our skills.
- **The wrapper** of a built ad is everything about how it is told: format, beat structure and timing, hook mechanism, camera, person, look, audio role, CTA. Mode B keeps it; mode A keeps only the concept mechanism and the Pocket.

**The same words inside Lyra.** Lyra's own nodes use these words a little differently; know which one you are reading:

| Where | "Angle" or "concept" there means | How this skill reads it |
|---|---|---|
| The team framework (this skill, mode A) | angle = a perspective inside a concept, 6 to 7 words | as is |
| This skill, mode B | angle = a reason to care: a pain, desire, objection, moment or feature | as is |
| Lyra's **Ad Brief** node, field "Concept angle" | the whole creative idea being tested, up to 100 characters ("UGC before/after with dermatologist endorsement and urgency offer") | the brief line of one angle: concept + angle + proof + offer in one phrase |
| Lyra's **Ad Brief**, field "Hook mechanism" | question, statistic, before after, social proof, curiosity gap, direct benefit, pain point, FOMO, shock value, trend riding, relatability, authority claim | the same words can be concepts in the team framework (Before/After, Social proof, Authority figure); a hook mechanism is only the opening |
| Lyra's **Creative Hypotheses** node | `new_angle` = a new argument for the same people · `new_persona` = new people with their own problem · `new_concept` = a new format and story · `improve` = one weak element of a winner; tags in the `angle` namespace shape the whole ad, not one funnel stage | see the borders below; its own MODE A / MODE B (whole account / one video) has nothing to do with this skill's modes |
| Lyra's **Ad Variation** node | single-variable mode (one dimension changes, every other one listed as held constant) or multi-variable mode | mode B is single-variable (the angle); mode A is multi-variable |

**The speaker is not the persona.** Lyra keeps two things apart: the **persona** is who the ad is for (their situation and goal), the **presenter** is who is on screen. In mode A the presenter changes with the angle (the doctor, the teacher); the persona stays the account's people unless the angle is meant for new people. People are the same when they share the situation and the goal the ad speaks to, not when they look alike: a male beginner runner and a woman training for a half-marathon are different people, although both run.

---

## Two ways to multiply: pick with the user

| | **A. Perspectives** (team framework) | **B. Reasons** (proven wrapper) |
|---|---|---|
| The question | Who else could tell this, and how would they argue it? | What else can this same ad say? |
| An angle is | a perspective inside the concept: a speaker, a role, a lens, each with its own point | a reason to care for a segment: another pain, desire, objection, moment or feature (a "motivation layer": a fear, a frustration, a desire) |
| Stays | the concept mechanism, the brand, the Pocket (CTA, offer, end card); the format family if the user wants | the whole wrapper: format, beat jobs and timing, hook mechanism, camera, cut rhythm, the person, look, audio role, music, the Pocket |
| Changes | the person or role, the place, the script, the argument, the hooks (about 5 per angle) | the reason, the situation where it happens, the script, the hook line (same mechanism) |
| Source | a concept name, a brief or a built ad | a built ad: a winner (a Lyra workflow or a finished video) |
| Scale | 1 concept → 3 to 4 angles → about 5 hooks each (up to 20 videos) | 3 angles + the original as control, one ad each |
| The test reads | which perspective makes this concept work, then which hook | which reason to care sells in this wrapper |
| Best when | exploring a concept's territory; early in a campaign; the user thinks in the framework's tree; a concept that lives on its speaker (Authority figure, Social proof, POV) | a validated winner; its angle fatigues but the format still holds; clean tests one variable at a time |
| Watch out | several things change at once, so a winner says "this perspective works", not "this word works" | narrow: the wrapper itself is never tested |

Both modes can run on one concept, as two separately named rounds (`A`-round and `B`-round), so the media buyer can compare the methods too.

### How to ask the user (plain words, exaggerated on purpose)

Ask once, early (Step 1), in the user's language, built on their app and their concept, with a recommendation. The examples are deliberately simple so the difference is obvious. Template (fictional fitness app, the winner is a doctor warning about sitting too long):

> There are two ways to make more ads from this concept. Which do you want?
> **A. Other people, other arguments** (concept → angles → hooks). The idea "an authority tells you to move" stays, but other people say it, each in their own way: a doctor ("Prescription: 10 minutes a day"), a teacher ("Homework: 10 squats"), a trainer ("Stop doing crunches"), a mom ("Have you moved today?"). About 5 hooks for each. Good for finding which voice works best.
> **B. Same ad, new reason** (proven wrapper). The same doctor, the same format, the same rhythm and ending, but each new ad is about a different problem: back pain at the desk, bad sleep, "no time for the gym". Good for a clean test of which problem sells.
> I'd recommend B, because your doctor ad already wins and B keeps everything that made it win. We can also do both, as two separate rounds.

Recommend by the source: a validated winner whose format holds → B · a concept name or an early concept, or a concept that lives on its speaker → A · the user already thinks in "1 concept, 4 angles, 20 hooks" → A.

### Borders with the other skills

- Only the first 3 s change → `lyra-video-hooks`.
- **The same script** said by another person or in another world (a nurse saying the same lines, the bedroom in São Paulo), words change only where tied to the person or place → `lyra-audience-variations`.
- **Another person with their own argument** (the teacher with "homework: 10 squats" instead of the doctor's prescription) → this skill, mode A.
- **A new reason to care** or a new situation where another pain happens (bed at 2 am → desk in exam week), the same wrapper → this skill, mode B.
- **Another concept** (Authority figure → Challenge) → a new concept (base skill).
- **A hypothesis card from Lyra's Creative Hypotheses** (`what_to_do`, `why`, `what_to_change`): `improve` is one element on a winner's weak step → `lyra-video-hooks` when the weak step is the opening, otherwise a one-element edit of that workflow (a variation, everything else held constant) · `new_angle`, `new_persona`, `new_concept` are new videos invented from a moment, not assembled from the account's videos → build each with the base or format skill exactly as the card says, then multiply it here once it wins. A card whose idea is "the same wrapper, a new reason" is mode B; one that is "another speaker with their own argument" is mode A.

**The ladder of iterations:** hooks (the first 3 s) → audience variations (who and where, same words) → concept multiplier (new angles) → a new concept.

**Every angle is a hypothesis**, written as one line: "We think [segment] installs more when [concept] is told [through this perspective / about this reason], because [evidence from the Brand Kit or research]."

**Different enough to count.** Angles must differ in the perspective or the reason, not in wording: "can't fall asleep" and "lying awake at night" are one angle; "a trainer" and "a gym coach" are one angle. Each new ad must read as a different ad in the first 3 s (a new person or place, a new hook line) and in the transcript.

---

## Mode A: Perspectives (concept → angles → hooks)

### The concept card

One note, "Concept card": the concept name (3 to 4 words) · its mechanism in one line (what makes it persuade: "an authority gives a simple order the viewer can follow today") · why it works for this app (from the original ad's numbers or the research) · what stays across all angles (the Pocket, the brand look, the format family if the user wants one, the length).

If the source is a built ad, also note what the original angle is: it is angle 1 of the tree, the control.

### Angles: perspectives inside the concept

An angle in mode A answers "who tells it, from which lens, with which point?". It is written in 6 to 7 words and expands the space around the concept. Where perspectives come from:

| Concept | Ways to find perspectives | Example angles (fitness and nutrition apps) |
|---|---|---|
| Authority figure | different roles the audience listens to | doctor · teacher · trainer · mom · a coach: "why tracking alone doesn't change habits" |
| Before / After | different "befores" | my day of eating before vs after · my questions before: 10 browser tabs, after: one answer · my hit-rate before vs after a week of reminders |
| Social proof | different sources of proof | "my gym friends keep asking what app I use" · replying to a real comment · first-week wins (only real ones) |
| Challenge | different challenges and their stakes | a 7-day protein challenge · "I asked the app every food question for a week" · making it past day 14 |
| Myth-busting | which belief is broken | "skipping meals isn't discipline" · "counting calories isn't the hard part" |
| POV | which moment the viewer lives | POV: your coach texts you right before you get hungry · POV: you finally know what to order |
| Warning | which mistake | "stop guessing your protein" · "don't download another calorie app until you see this" |
| Negative emotion | which feeling | fed up of tracking and still not knowing what to eat · crying because the language is hard |

Every angle is tied to **a segment** from the Brand Kit and to **evidence** (the Brand Kit, reviews, the research agent, past results). No evidence → the angle is marked **Explore**; evidence → **Adapt**. A good tree mixes both (mostly Adapt, one or two Explore).

**The person is part of the angle.** In mode A the speaker often *is* the perspective, so the person changes with the angle: a new character card per angle (`lyra-ugc-video`, casting from the audience). Keep the place, light and look consistent only where the concept needs it.

**The audience check, per angle** (Lyra's Hypothesis Audience Check). A new speaker must not quietly change who the ad is for. For every angle write: who the angle is for · who the original was for · same people: **yes** (the same situation and goal, even if the person on screen looks different) / **no** (another stage, goal, need or identity: the speaker brings their own situation with them) / **unclear** (say what is missing) · one plain sentence why. "No" is fine only when the angle is meant for new people: then name it as a new-persona angle with its own problem, in its own segment row. A mom telling *other moms* to move is still the fitness app's audience only if the account speaks to moms.

**Professionals and authority.** An AI person is never presented as a real expert. No white coat with "as a doctor I recommend", no titles, no medical, financial or legal advice. Authority angles work as: a clearly playful role in a skit ("Prescription: 10 minutes of walking", the teacher's "homework"), an **insider** without claimed credentials (`lyra-ugc-video` archetypes), a parent or a friend, or a **real** expert the brand works with (their consent, their words). Health claims only from the Brand Kit.

### Hooks per angle

Approve the angles first; write hooks only after ("do not ask for detailed hooks right away"). Then about **5 hooks per angle** by `lyra-video-hooks` (pain map, kinds, writing rules), each a different idea, all in that angle's voice. Within one angle the hooks share one body (hooks skill, mode A: same body, music and CTA), so the hook test inside an angle stays clean.

The tree is shown to the user before anything is built:

> **Concept** C01 Authority figure (1 idea)
> **Angles** A1 doctor · A2 teacher · A3 trainer · A4 mom (4 perspectives)
> **Hooks** A1: posture warning · X-ray reveal · bed-rotting diagnosis · prescription: 10 minutes · heart rate check / A2: blackboard drawing · you now vs in a month · homework: 10 squats · failing grade · calorie math / … (20 videos)

**Budget.** 20 finished videos is a lot of credits. Default first round: **2 to 3 angles × 3 hooks**, angle bodies on images first; more hooks for the angles that show promise.

---

## Mode B: Reasons (the proven wrapper, a new reason to care)

### Concept DNA: the mechanism, not the content

Every element of the original ad is either **mechanism** (why it works; reusable with any pain) or **content** (what it happens to be about this time). The test for each element: **would it still work if the pain were different?** Yes → mechanism, locked. No → content, it changes with the angle.

Example: the "Calmly" concept C1, a 15 s UGC storytime for a sleep app (fictional).

| Element | Mechanism (locked) | Content (changes with the angle) |
|---|---|---|
| Format | storytime confession, selfie at arm's length, quiet honest voice | where she is and why |
| Hook | combined: a physical drop at frame 0 + a confession line in the shape "I tried every…" | what she drops onto, the words |
| Structure | hook → old way (three failed tries in fast cuts, closer each time) → the app as the last try → result on the person → soft spoken CTA | the three tries, the feature, the result |
| Timing and pacing | beats 0 to 2.5 / 2.5 to 6 / 6 to 10 / 10 to 13 / 13 to 15 s; a cut about every 2.5 s | none |
| Camera | handheld front camera at arm's length; one B-roll shot for the result | the place it's filmed in |
| Person | Mia, 21 (the same face in every angle) | her outfit and state follow the situation |
| Look | raw UGC, motivated practical light, brand palette | the light source of the new place |
| Audio role | native speech, no music, room tone | the room tone of the new place |
| App moment | screen turned toward her, then the result shown on the person | which feature, which screen |
| CTA and end card | soft spoken tip + store-style end card | none (the Pocket stays) |
| Emotional tone | tired, honest, a bit ironic | none |

Write the DNA from the original's own evidence (the workflow's prompts and Video Editor timings, the video's frames and transcript), never from a memory of what the ad was "about". If `lyra-copy-competitor-ad` Reference K is filled for the original, its `hook_type` and `narrative_arc` usually name the team-level concept (Authority figure, POV, Before/After).

**From Lyra's Creative Analysis (Pattern Import) output.** When the original was run through the node, its Creative Anatomy fills most of the DNA; sort its fields like this:

| Creative Anatomy field | In the DNA |
|---|---|
| Format · Layout · Text placement · Narrative structure · Hook mechanism · Motion · Pacing · Image style · Emotional register · Typography | mechanism (locked) |
| Key elements · Hook text · Objection handling | content (changes with the angle); the person in Key elements stays in mode B |
| Value proposition · Offer · CTA | the Pocket (stays), unless the angle is another feature |
| Dominant colors | the look (stays) |
| Concept summary | the original's one-line idea: rewrite it per angle for its brief |
| Notable techniques | the first candidates for "why it works" |
| Additional observations | flags for review (compliance, claims) |

The node works from frames about every second plus the transcript; anything it didn't see is a gap to fill from the workflow's prompts or to ask about, never to guess.

**Why it works** in 2 to 3 lines: what every angle must keep alive ("the pain lands in 2 s in her own words; the three failed tries are the viewer's own history; the result is shown on the person, no screen needed"). If nobody can say why it works, ask the user for the numbers and what they think won.

### The angle: a new reason to care

An angle in mode B is the reason this viewer should care now. One angle per ad. Every angle comes from the Brand Kit (the pain map, `lyra-video-hooks` Step 1), best organised per segment as **motivation layers**: what they fear, what frustrates them, what they want. A real feature answers it.

| Angle type | What it answers | Example (Calmly, students) | Watch out |
|---|---|---|---|
| **Another pain** | another problem the app solves | exam week, the brain won't stop | one pain per ad |
| **Another moment** | the same need at a new trigger moment that makes a new story | Sunday night, dreading Monday | a new story, not the old one re-dressed (that is audience variations) |
| **Outcome / desire** | the result they want | waking up before the alarm, actually rested | the result shown on the person; no invented numbers |
| **Identity / future self** | who they want to be | "the friend who's fun at brunch because she slept" | aspiration, never shame |
| **Through other people** | a partner, roommate, kids or boss notice | the roommate: "you stopped scrolling at 3 am?" | others never mock |
| **Objection** | why they hesitate | "I thought sleep apps were just rain sounds" | the body answers the doubt with the real feature |
| **Old way / alternative** | what they do now and why it fails | the third coffee, ten alarms, a podcast that keeps her awake | generic objects only; never a competitor or a brand |
| **Another feature** | a second real feature and the pain it answers | sleep sounds for a loud dorm | a new screenshot; one feature per ad |
| **Cost of the problem** | what it costs to keep the pain | "third coffee by noon and still useless" | real stakes, no fear-mongering |
| **Occasion / season** | a calendar moment that sharpens the pain | exams, jet lag after a trip, the New Year reset | fits the launch window; dated angles expire |
| **A belief to break** | a belief that keeps them stuck | "counting sheep keeps you awake" | true, no pseudo-science (in team terms this is close to the Myth-busting concept: in mode B it only changes the reason, not the wrapper) |
| **Awareness shift** | the same wrapper for another awareness level | unaware: a relatable 2 am moment with no pitch; product aware: objection first | the awareness table in `lyra-video-hooks` |

### The situation: where the new angle happens

A new angle usually needs a new situation: the place and moment where **that** pain happens (`lyra-ugc-video`, Place). Derive it from the angle, never pick a place because it looks good. The situation fills the concept's slots: the hook's physical beat happens in the new place (she drops onto the pillow → she drops her head onto the open textbook), the old-way beat gets the new angle's own tries (tea, earbuds, counting → the third coffee, an energy drink, flashcards in bed), the result happens in the new place.

| Distance | What changes | What reruns | Use when |
|---|---|---|---|
| **1. Re-angle** | the words and the app moment; the same place and person | clip(s) + VO; usually no new images | the cheapest test; the original place also fits the new angle |
| **2. Re-situate** (default) | the angle + its situation: new place, moment, props, light; the same person | scene image(s) + clip(s) + VO | the new pain lives somewhere else |
| **3. Re-story** | the angle + a new plot inside the same structure (another cause, another turning point, a second person in a skit) | as 2, plus a second character if needed | story formats: skit, micro-drama, interview, talking object series |

**Distance 1 is the riskiest for delivery.** The same person, place, shots and rhythm with new words can read to the platform as the same ad (Meta groups near-identical creatives), and Lyra's own rule for new videos is that "a talking head about fees after five talking heads about fees is not new". Use distance 1 to test the message itself; for a round that must also refresh delivery, prefer distance 2 or 3, so the first frames look different.

### The same person, by default

In mode B the person stays: the face is part of the proven wrapper, and changing it too would mix two tests (angle and person). Their outfit, state and props follow the new situation (the one-story test). Change the person only when the new angle really belongs to another segment's life; then name it an angle + audience version, or run the angle with the same person first and the person later with `lyra-audience-variations`. A recurring face across angles also turns the concept into a series the audience recognises. (When the new person *is* the point, that is mode A.)

**The sibling test (mode B):** muted, with the faces blurred, is it obviously the same concept as the original (same rhythm, same shot types, same format)? Read as transcripts, are they obviously two different ads? Is every word true for the app?

---

## Step 1 additions: the source, the mode, the angle bank

1. **The source.**
   - **A Lyra workflow** (built with our skills, or the user's own): `list_variations` and `get_workflow` on the original. Read every prompt: the script note, the character, scene images and keyframes, phone shots, clips (camera, cuts, sound line, voice anchor, avoid line), VO, music, and the Video Editor's composition (the beat timings from `startMs` and `durationMs`).
   - **A finished video, the user's own ad** (a file or a public direct link): `create_upload` → `attach_upload`. Analyse it as in `lyra-copy-competitor-ad` Path 2 (frames every 3 s and at each cut, transcript with timestamps) and write its layer 2 production breakdown; layer 1 (Reference K there) is optional but names the mechanism in the team's terms. It is the user's footage, so a still of the person can be the identity reference.
   - **A concept name or a brief only** (mode A) → no source ad needed; angle 1 is built with the matching skill (base, UGC, UI), the next angles as variations of it.
   - **A competitor's ad** → `lyra-copy-competitor-ad`.
   Check `list_uploads` first.
2. **The proof.** Ask in the same message: is it a validated winner? Its numbers, if known (hook rate, hold rate, CTR, cost per trial, how long it ran)? What does the user think won? If the account has Lyra's analytics, use its labels as they are: **winner** or **near winner** (close to the best) can be a mode B base; **middle** or **loser** is not a base to patch but a starting point for mode A or a new concept; **early read**, **under-tested** or **not judged** prove nothing yet. Mode B on an unproven ad multiplies a guess: say it once and offer mode A, hooks first or a smaller round. Compare only ads of the same optimisation goal (installs with installs, purchases with purchases).
3. **The mode** (the question above, plain words, with a recommendation). Nothing in Steps 4 to 6 is written for both modes unless the user wants both rounds.
4. **Brand Kit and the pain map** (base Reference I; `lyra-video-hooks` Step 1; several kits → ask which; never mix two). Read: audience and segments, pains in their words (fears, frustrations, desires per segment), objections, features, approved claims and proof, forbidden claims, offer, tone, must include / must exclude. Mark the angle the original already uses. No pains in the kit → 3 to 5 pain hypotheses to confirm, and keep moving in the same message.
5. **The angle bank** (user text node "Angle bank"), in the team's angle sheet format, one row per angle:

   | Angle ID | Concept | Angle (6 to 7 words) | Segment | Benefit · register | Bucket | Evidence | Closest ads · what's different | Flag for review | Mode A: who / lens · audience check · hooks planned | Mode B: situation · distance · hook line (words) |
   |---|---|---|---|---|---|---|---|---|---|---|

   - **Angle ID** `C01-A1`, `C01-A2`… (the concept number and the angle number; A1 is the original's angle).
   - **Benefit:** the one benefit of the app this angle sells, a different one for every angle until each is used ("simple checkout" is one benefit, however it is filmed). **Register:** emotional (how it makes them feel), practical (what it does for them), identity (who it makes them) or critical (what is wrong with what they do now); a round spreads across registers.
   - **Bucket:** **Adapt** (backed by evidence: the Brand Kit, reviews, research, past results) or **Explore** (no direct evidence yet, a bet).
   - **Evidence:** the source in a few words ("KB: day-14 drop-off", "Research 2026-10-18: r/loseit 'fed up of tracking'", "reviews: 'my roommate noticed'"); with Lyra's analytics, how many of the account's ads already back it ("3 ads, one a winner") and Lyra's tag verdict if there is one (ads with it get results for less, in the same goal).
   - **Closest ads · what's different:** up to 3 ads the account already ran that are most like this angle, and what makes this one different. Nothing → drop the angle. A similar ad that lost → say what is different this time.
   - **Flag for review:** what a person must check (a claim, a stat to cite, a sensitive topic, a real review needed).
   - Never repeat an angle already proposed or already run for this account (check the project's creative repository and earlier angle banks), in any wording.

   Mode A, examples:
   > C01-A2 · Authority figure · A teacher gives movement as homework · students and parents · Explore · no direct evidence · flag: playful role, no claims · who: a teacher in a classroom skit · 5 hooks
   > C01-A3 · Authority figure · A trainer shares what clients get wrong · goal-driven gym-goers · Adapt · KB: gym-goer pains · flag: none · who: a trainer, insider, no titles · 5 hooks

   Mode B, examples:
   > C01-A2 · Storytime confession · Exam week, the brain won't stop · students · Adapt · KB: exam stress in reviews · situation: her desk at 1 am, notes and highlighters, only the desk lamp · distance 2 · hook: "I tried every way to sleep in exam week." (9)
   > C01-A3 · Storytime confession · Sleep apps are just rain sounds · students who tried apps · Adapt · reviews: "finally not just rain sounds" · situation: the same bed at 2 am · distance 1 · hook: "I tried every sleep app that's just rain sounds." (9)
   > C01-A4 · Storytime confession · The roommate notices she sleeps now · students in shared rooms · Explore · no direct evidence · situation: dorm room in the morning, the roommate at the door with two coffees · distance 3

   8 to 12 rows. Recommend: mode A, 3 to 4 angles (2 to 3 for a first round); mode B, 3 (2 to 4). One line why; at least one Adapt close to the original (safer) and one Explore further away (more learning).
6. **Intake quiz** (base Step 1 format: one message, multiple choice, options from the Brand Kit, the recommended option first): the mode · which angles (with your recommendation) · how many (and in mode A, hooks per angle) · in mode B, the same person (default yes) · screenshots of any new feature · language · anything the brand doesn't want to say or show.

**Defaults (state, don't ask):** mode B for a validated winner, mode A for a concept name or an early concept · mode A: 3 angles × 3 hooks for a first round · mode B: 3 angles + the original as control, distance 2, the same person · **one variation per angle**, copied from the original, which stays Main and untouched · the same length, ratio, platform and models as the original · same music, CTA, offer and end card · real people: Seedance 2.5, references only, the original's resolution (720p by default), sound on · Nano Banana Pro for every image, 9:16, 2K.

**Recommended first run:** A. Images (mode A: each angle's person and scene; mode B: each angle's new situation). Images are cheap, and they show whether each angle reads in one glance.

---

## Step 2 addition: the multiplier sheet

Before building, a user text node "Multiplier sheet", part of the concept the user approves.

**Mode A:**
1. **The concept card** (above) and the **lock list**: the Pocket (CTA, offer, end card), the brand look and palette, the length and ratio, the format family if the user wants one.
2. **One angle card per angle:** the perspective in 6 to 7 words · the person (character card, `lyra-ugc-video`) · the place and moment · the argument in one line (what this perspective says that the others don't) · the spine with times (hook → the point → the app → CTA, by the base skill or the format's skill) · the feature it shows · the 3 to 5 hook ideas (one line each, approved before writing them out).
3. **The tree** (concept → angles → hooks) with codes, as above.
4. **Hypotheses:** one line per angle.

**Mode B:**
1. **Lock list:** what stays identical in every angle, from the DNA: format, beat jobs and timing (about ±0.5 s per beat), hook mechanism, camera setup and moves, cut rhythm, the person, look and palette, audio role, voice anchor, music, CTA, offer, end card, length.
2. **Situation card** per angle: the angle · the moment (time, day) · the place with 2 to 3 lived-in details · the light source · props · the person's state and outfit · the feature and its screen. Name the place, props and actions concretely, the way Lyra's tag mapper reads them: a **scene** ("living room", "street"), **objects** with an attribute ("wooden box", "pink nail polish"), **actions** ("scanning a coin with a phone"). Mood words ("serene", "cosy") are not tags and count for nothing; they belong in the prompt's light and tone, not in the card's list of what changed.
3. **Beat sheet, side by side:**

   | Beat | Time | Job (locked) | Mechanism (locked) | A1 (control) | A2 exam week | A3 objection |
   |---|---|---|---|---|---|---|
   | Hook | 0 to 2.5 s | stop, name the pain | a physical drop + "I tried every…" | drops onto the pillow: "I tried every sleep hack on TikTok." (8) | drops her head onto the textbook: "I tried every way to sleep in exam week." (9) | drops onto the pillow, phone up: "I tried every sleep app that's just rain sounds." (9) |
   | Old way | 2.5 to 6 s | the viewer's own failed tries | three tries, fast cuts, closer each time | tea, earbuds, counting on her fingers | a third coffee, an energy drink, flashcards in bed | rain, whale sounds, a meditation |
   | App | 6 to 10 s | the last try | screen turned toward her, one line | "This one does a 5-minute wind-down." | same | "This one actually talks you down. Five minutes." |
   | Result | 10 to 13 s | result on the person | B-roll, eyes closed | asleep, phone face down on the duvet | asleep, notes stacked on the chair, alarm set for 7 | asleep, headphones off |
   | CTA | 13 to 15 s | soft tip | back to the selfie, smile | "It's free. Try it tonight." | same | same |

   Word counts per line within about ±10% of the original (never past ±20%, Lyra's Ad Variation limit); the same level of claims.
4. **Hypotheses:** one line per angle.

**Both modes, per angle: Changed fields, Held constant, and a brief in Lyra's format.**
- **Label** the angle by its strategic idea ("Exam-week pain", "Teacher's homework"), never "Variant A".
- **Changed fields:** every dimension that changes, from → to, concretely (Person: Mia, 21 → Ana, 29, a nurse · Place: bedroom at 2 am → desk at 1 am · Hook line: "…" → "…").
- **Held constant:** every dimension that does not change, listed one by one, not "everything else". In mode B this is the lock list; in mode A at least the Pocket, the brand look and the length.
- **Brief** (a user text node "Brief: C1A2"), in the exact format of Lyra's Ad Brief node, so it reads like every other brief in the workspace: `aspect_ratio` (9:16, 16:9 or 1:1) · `elements_to_include` (the production blocks: voiceover, music, brand video asset… only what the angle needs) · then three sections with their labels written exactly: **Concept Hypothesis** (Statement · Concept angle, up to 100 characters: the whole idea in one phrase · Format type) · **Creative Direction** (Concept summary, 200 · Hook mechanism · Hook suggested text, 80 · Value proposition, 150 · Proof point, only a real one · Tone · Offer text · CTA text, 30) · **Visual Direction** (Format · Layout Description, 200 · Image Style · Color Palette Primary · Duration seconds · Must include elements · Must exclude elements). A field with nothing real for it is left out, never "N/A".

---

## Writing the new script

**Both modes:**
- **One angle, one feature, one result** per ad. The CTA and offer stay identical (the Pocket); an angle-specific CTA only when the offer is part of the angle, named in the plan.
- **Hooks** follow `lyra-video-hooks` (6 to 10 words, key word first, text on frame 1 of 2 to 6 words, marked for post).
- **Captions** are written to the new words, marked for post (Video Editor only, never in a prompt).
- Base pace about 2.5 words per second; speech ends about 1 s before the clip ends.

**Mode A:** each angle gets its own script on the concept's spine, in its speaker's voice, with its own argument. Within an angle, all hooks share one body; the body is written once and the hooks are cut onto it (hooks skill, mode A). Across angles, keep the length and the Pocket the same so the angles compare fairly.

**Mode B:**
- Beat by beat, from the beat sheet. Each line keeps its **job** and, where the shape is part of the mechanism ("I tried every…", "POV: …", a list of three), its **shape**; the words are new, built from the Brand Kit and customer words.
- **Timing contract:** the same beats in the same order, each within about ±0.5 s of the original, the same total length.
- **A beat that doesn't fit the angle** (an outcome angle has no "three failed tries"): give the beat new content with the same job and the same length (three moments of the tired morning before, three alarms snoozed), or drop that angle. Never break the timing contract or the beat order to force an angle in: that is mode A or a new concept.

---

## Best way to build it

The user's explicit choices override any row. Models and prices: base Reference A.

| If | Best approach (graph) | Models |
|---|---|---|
| **Mode B, a Lyra workflow with a finished creative** (default for B) | **one variation per angle** (below): `create_variation` → `switch_variation` → the character node keeps its copied result (the identity) → the scene image(s) rewritten for the new situation, with the character connected as reference → the clip prompt: content lines replaced, locked lines word for word → new VO text if the VO is separate → rerun only the changed nodes → Video Editor with the same timings | as the original |
| Mode B, **distance 1** (re-angle, same place) | variation → `update_node` on the clip's speech and app moment, and the VO; the images stay | as the original |
| **Mode A, a built ad as angle 1** (default for A) | one variation per angle: a new character node or prompt (the angle's person, count 2) → the angle's scene image(s) with that character as reference → the body clip on the concept's spine with the angle's script → the angle's hooks by `lyra-video-hooks` mode A (one Section per hook inside the variation, each with its own Video Editor) | nano-banana-pro · seedance-2.5 |
| Mode A, **a concept name only** | `create_workflow` → angle 1 built with the matching skill (UGC, base, UI) → then one variation per further angle, as the row above | as the matching skill |
| The angle shows **another feature** | + `create_upload` of the new screenshot → phone shot by `lyra-ui-motion-video` (screenshot + character) → reference for the clip, or a short UI insert in the Video Editor | nano-banana-pro · seedance-2.5 / 2.0 |
| A workflow on **frame models** (Seedance 2.0, Kling) | a new keyframe per shot (character as reference; mode B: the old keyframe's framing written in words) → the frame linked right after the image has a result and the user selected one | nano-banana-pro · seedance-2.0 / kling-v3-video |
| **A finished video** (the user's own), no workflow | DNA or concept card from the breakdown → mode B: a still of the person as the identity reference; mode A: a new character per angle → per angle: scene image → **one Seedance 2.5 clip** with the shot plan as "cut to" with lengths → optional in mode B: the original as **[Video1], editing reference only**, when the timing must match closely; check that the old place and words don't leak → VO and music → Video Editor | nano-banana-pro · seedance-2.5 |
| **Story formats** (skit, micro-drama, interview, talking object series) | mode B distance 3: the same characters and roles, one new episode per angle, the same episode structure and length · mode A: a new character or role per angle in the same format | seedance-2.5 (people) · seedance-2.0 (stylized) |
| **A visual hook concept** (object POV, fourth wall, visual metaphor) | the mechanism stays, the object moves into the new situation (the fridge camera → the gym bag camera; the giant heavy head → a giant stack of flashcards) | as the original |
| **A UI motion concept** | the style, motion vocabulary, layout and end card stay; the angle changes the headline and the screen (another feature, another benefit), by `lyra-ui-motion-video` | as the original |
| An angle that needs its own workflow (another client, shared separately) | workflow menu (⋮ next to the name) → **Save as a new workflow**; no MCP tool does this, so ask the user to click it (or do it in their browser if they allow), then work there | as the original |
| Many angles, tight budget | mode B distance 1 angles first; mode A 2 angles × 3 hooks; images for all, clips only for the 1 to 2 the user picks; or drafts on a fast model and the winner on the recommended one | seedance-2.0-fast for drafts |

### Variations: the way to make an angle

In Lyra every version of a creative is a **variation** of its workflow: the **Create variation** button above the canvas (the `create_variation` tool) copies the whole space (every node, prompt, connection and result). The original stays **Main** and untouched as the control (angle A1); the new angle is written into the copy.

**Step by step:**
1. `list_variations` → find the original (the main one, unless the user names another). Rename it if needed: `rename_variation` "C1 · A1 · storytime · can't sleep (control)".
2. Put the notes ("Concept card" or "Concept DNA", "Angle bank", "Multiplier sheet") in the original's Sources Section before copying, so every variation carries them (notes don't feed generation).
3. `create_variation` with `copy_from_variation_uuid` = the original and `title` = code, angle, person or situation, language: "C1 · A2 · teacher · EN", "C1 · A2 · exam week · desk · EN". The copy carries the original's results, so what doesn't change (music, end card, screenshots, and in mode B the character) never reruns.
4. `switch_variation` to it (Lyra renames the workflow after the main variation; tell the user which one is open), then `get_workflow`.
5. Write the angle in with `update_node`, by the node map below. New nodes if needed (a character in mode A, a scene image, a new screenshot upload, a phone shot, hook clips and their Video Editors), connected at build time with `connect_nodes`; `disconnect_nodes` an image of the old place or old person from the clip if it would pull them in.
6. `get_workflow` on the variation and search every prompt for the old angle: the old pain words, the old place, old props, old lines, and in mode A the old person. One forgotten line puts two ads in one.
7. Read the price on the nodes that will rerun and put it in the approval message (base Step 6: one question, then run everything). Unchanged nodes keep the copied results.
8. Repeat from step 3 for the next angle (always copy from the original, never from another angle).
9. When done, `switch_variation` back to the original if the user wants it shown first, and say which variation holds which angle.

### The node map: what to update, what reruns

| Node | Mode A (new perspective) | Mode B distance 1 (re-angle) | Mode B distance 2 (re-situate) | Mode B distance 3 (re-story) |
|---|---|---|---|---|
| Character (identity) | new person for the angle: rewrite and rerun (count 2) | stays, result copied | stays as the identity reference; the new outfit and state go into the scene image prompt | stays; a second character added if the plot needs one |
| Scene images, keyframes | the angle's place, with the new character as reference → rerun | stay | new situation: `update_node` (or a new node with the character as reference) → rerun | as distance 2 |
| Screenshot, phone shot | new if the feature changes; a phone shot with a new person reruns | stay, unless the feature changes | same | same |
| Clip(s) | the angle's body: identity, place, action, speech, voice anchor rewritten; camera and length from the concept's spine | content lines: speech, app moment | content lines: environment, props, light, the action's content, speech, app moment | + plot lines, who says what |
| Hook clips | about 5 new per angle (hooks skill) | — (the hook line is in the main clip) | — | — |
| VO (if separate) | new text and a voice that fits the new person | new text, same voice and length | same | same |
| Music | stays (new only if the perspective's emotion really differs; say why) | stays | stays | stays |
| End card, logo | stay | stay | stay | stay |
| Video Editor | one per hook inside the angle | reruns with the same timings; captions changed in the editor UI | same | same |

**Mode B: never rerun the character node** to "refresh" it: a new run is a new face, and the series loses its person. Keep the copied result and pass it as a reference.

**Mode B locked lines in a clip prompt** (copied word for word from the original): the roles of the references, the camera setup and moves, the cut structure and lengths ("cut to" with times), the sound line (if someone speaks and the original's lets music in, add "no music, no background music, no soundtrack, no score": base Reference C), the voice anchor, the end state of each shot (only its place details adjusted), the avoid line. **Content lines** (rewritten): the environment, props, light source, the content of the action, the spoken lines in quotes, the app moment.

**Connections.** A variation copies the original's connections, so the graph already runs end to end. Only new nodes need links (base Step 4): a new character → every image and clip that shows the person; a new scene image → the clip as a reference; a new screenshot → the phone shot → the clip; hook clips → their Video Editors; on frame models, the new keyframe right after it has a result. The text notes don't feed generation; consistency comes from the images connected as references plus the anchors written into every prompt.

**Layout and labels.** Each variation keeps the original's layout, Sections and order, so the user can flip between angles and see the same canvas. Mode A adds one Section per hook. Relabel the nodes that changed with the angle code: "A2 teacher: character", "A2: classroom (scene)", "A2: body clip", "A2H3: homework squats (hook clip)", "Final: C1A2H3 · teacher homework", "A2 exam week: desk (scene)", "Final: C1A2 · exam week".

---

## Prompt rules (concept multiplier)

| Node | Write | Avoid |
|---|---|---|
| Concept card / Concept DNA (text) | mode A: the concept in 3 to 4 words, its mechanism, why it works, the lock list · mode B: element by element, mechanism (locked) and content, why it works, beat slots with times and jobs | what the ad is "about" without naming the mechanism |
| Angle bank (text) | the team's angle sheet: ID, concept, angle in 6 to 7 words, segment, bucket, evidence, flag; plus the mode's columns | one angle reworded several times; an angle without a real feature or a segment |
| Multiplier sheet (text) | mode A: angle cards and the tree · mode B: lock list, situation cards, beat sheet with word counts; hypotheses | "a different vibe" without naming the angle |
| Character (mode A) | the angle's person in the structure of Lyra's Character Prompt node (a note per angle): **Character** (age range, gender, ethnicity) · **Appearance** (build; hair: colour, length, style; face details with small imperfections; distinctive features) · **Style** (outfit, style vibe, accessories) · **Behavior** (expression, natural and subtle; pose, selfie or direct to camera; action tied to the app) · **Environment** (a specific real location, context, natural imperfect lighting, camera feel: front camera, handheld) · then the image prompt: up to about 500 characters, subject first, camera angle, environment, action, light, with the words "natural", "realistic", "UGC style", "not polished" · and the negative prompt, always with "studio lighting, overproduced, perfect skin, model look, cinematic, 3d render, illustration, text overlays, watermark, blur, distortion". A role is shown by the situation and props, not by titles | a white coat with a stethoscope as proof; "Dr." or job titles in text; a lookalike; a stereotype or caricature of the role |
| Scene image (mode B, same person, new situation) | "UGC phone photo" → "[Image1] is [name]: keep the face, hair, skin and build exactly" → the new situation in full: place, moment, 2 to 3 lived-in details, light source, props → outfit and state that fit it → the original shot's framing and camera setup, in words → realism line → no text | "the same scene, but in a library" (keeps the old room); details of the old place; text, logos, brands |
| Clip | mode A: the concept's spine and camera told in words, the angle's identity, place and speech · mode B: the original prompt with content lines replaced, locked lines word for word; roles of references first | mode B: another camera, cut structure or timing; the old place, person or words left anywhere |
| VO | the new text, sized to the original's length | a VO longer than the clip minus 1 s |
| Music | unchanged by default | a new track "for variety" (it breaks the comparison) |

**Pattern: scene image, same person in the new situation (mode B, Nano Banana Pro, distance 2).**

> UGC phone photo, same person in a new place. [Image1] is Mia: keep her face, hair, skin texture and build exactly. She sits at a cluttered desk in her student room at 1 am, her head resting on an open textbook, highlighters and three empty coffee cups around her laptop, flashcards spilling onto the floor; the only light is a warm desk lamp and the glow of the laptop. Grey hoodie, hair in a loose bun, tired eyes. Shot on a phone front camera at arm's length, slightly above eye level, the selfie framing of a storytime video, deep focus, natural skin texture, visible pores, slight dark circles, no beauty filter. No text, no captions, no watermark, no logos, no visible phone screen.

**Pattern: what changes in a clip prompt (mode B, Seedance 2.5).**

> Locked, word for word: "[Image1] is Mia: her face, hair and grey hoodie. [Image2] is the scene. Handheld selfie at arm's length, front camera, slight natural wobble… cut to (2.5 s)… cut to (3.5 s)… Sound: only natural room tone and action sounds, no music, no soundtrack, no score. Voice: young woman, soft American accent, sleepy, unhurried. Avoid: morphing faces, identity drift, outfit change, warped hands, text on screen."
>
> Content, new: "She drops her head onto the open textbook, looks up into the camera and says: 'I tried every way to sleep in exam week.' Cut to: a third coffee, closer. Cut to: an energy drink, closer. Cut to: flashcards in bed, closest…"

**Pattern: a mode A angle character (Authority figure → the teacher, Nano Banana Pro, in the Character Prompt node's format).**

> Prompt: Woman in her early 40s, a teacher, warm brown skin, short natural hair, reading glasses pushed up, cardigan over a plain blouse, front-facing selfie at arm's length in an empty classroom after school, whiteboard behind her with a stick-figure doing squats, she raises her eyebrows about to give homework, late afternoon window light, natural, realistic, UGC style, not polished, visible skin texture.
>
> Negative prompt: studio lighting, overproduced, perfect skin, model look, cinematic, 3d render, illustration, text overlays, watermark, blur, distortion, readable text, logos, name badge.

---

## Run options (concept multiplier)

**Run order, not a menu** (base Step 6): after the user's yes, run all of it in this order without offering options. Stop between stages (the look first, then the rest) only when the user asked for it, or when the plan is expensive and that was said in the approval message.

As in the base skill, credits read from the nodes, per option. **Mode A:** **A. Angle images (recommended):** each angle's person (count 2) and scene · **B. Angle bodies** for the picked people · **C. Hook clips and Video Editors** (about 5 per angle, or the 3 the user picks) · or **D. Everything** at once (count 1; no pause to pick). **Mode B:** **A. New scene images (recommended):** every angle's situation · **B. Clips, VO and Video Editors** for the picked images · or **C. Everything** (count 1). Mode B distance 1 angles skip A and cost only the clip and the VO. When an image has several results, the user selects one in Lyra before the next stage (references pin to the selected result).

---

## Truth and brand safety

- **Every angle is real.** A pain or desire from the Brand Kit (or a confirmed hypothesis), answered by a feature the app really has. An angle the app can't truthfully answer is dropped, however good it sounds. Explore angles are bets, not claims.
- **No new claims.** A new angle never brings a new result, number or promise ("I passed my exams thanks to Calmly"); claims stay at the original's level, from the Brand Kit only. The promise matches the store page and the first session.
- **No fake experts.** An AI person is never a real doctor, coach, advisor or reviewer: no titles, credentials, white-coat proof or professional advice (health, money, law). Authority angles are playful roles, insiders without credentials, parents and friends, or a real expert the brand works with, with consent. Remind the user once to turn on the AI-generated label (`lyra-ugc-video`, Truth and disclosure).
- Sensitive categories: health, sleep, fitness, finance angles promise no cure, weight loss, diagnosis or returns; no body before/after.
- No personal-attribute callouts to the viewer (Meta's personal attributes policy): the person speaks about their own life ("I'm on nights this week"), never "Are you anxious?". Check the current platform rules; this is not legal advice.
- Stakes, warning and fear angles use real stakes, no fear-mongering; myth and belief angles are true.
- No third-party brands: the old-way beat shows generic objects (a coffee cup, an energy drink can without a brand, "a sounds app"), never a competitor, a named product, a logo or readable packaging; no "if ChatGPT is your coach" style callouts of other products unless the brand's team approves. Occasions are generic (exams, a trip, the New Year), never a trademarked event.
- **Brand safety** (Lyra's System Preamble, base Reference B): no profanity and no political statements in any angle (health claims and competitors are covered above). The Brand Kit's **forbidden claims are enforced absolutely**, in every angle's line, caption, visual and VO; if the user asks for one, say once that it is on the kit's forbidden list and leave it out unless the user confirms the kit is outdated.

---

## Deliverable and naming

1. The notes in the original's Sources Section: "Concept card" (mode A) or "Concept DNA" (mode B), "Angle bank", "Multiplier sheet".
2. One variation per angle (titled with its code, angle, person or situation and language), with its changed images, clips, VO and Video Editor(s); the original untouched as Main, the control (A1).

Codes follow the tree: concept `C`, angle `A`, hook `H`. The angle sheet uses the team's ID `C01-A2`; the ad name uses the short form `C1A2` (+ `H3` for a hook). Each angle puts its own angle in `A:`: control `B6-A:CantSleep-F:UGC-Storytime-C1A1` → mode B `B7-A:ExamWeek-F:UGC-Storytime-C1A2`, `B7-A:JustRainSounds-F:UGC-Storytime-C1A3` · mode A `B7-A:TeacherHomework-F:UGC-Skit-C1A2H3`. Add `V{n}` for audience variations of an angle: `…-C1A2-V4Bundle-Nurses`. Mark the round when both modes run: `…-C1A2-ModeA`, `…-C1A2-ModeB`. Node label: "Final: C1A2H3 · teacher homework".

---

## Common mistakes (concept multiplier)

| Mistake | Prevention |
|---|---|
| The mode not asked, or asked in abstract words | The plain-words question with the user's app and an exaggerated example of both modes |
| "Angle" means one thing to the user and another in the build | Say the mode's meaning in one line in the plan |
| Mode A: a new speaker quietly changes who the ad is for | The audience check per angle: same situation and goal, or a named new-persona angle |
| Mode B on a middle or losing ad | Bases are winners or near winners; the rest start mode A or a new concept |
| A round of distance 1 angles only, read by the platform as the same ad | Distance 2 or 3 when the round must refresh delivery |
| Angles that share a benefit, or all in one register | One benefit per angle; spread across emotional, practical, identity, critical |
| No "closest ads" checked, so the angle repeats what already ran | Closest ads and what's different in every row |
| A Lyra hypothesis card for a new video built as a variation of an old one | `new_angle`, `new_persona`, `new_concept` are invented videos (base skill); multiply them once they win |
| "Variant A", or "everything else stays" without the list | A strategic label; Changed fields and Held constant listed one by one |
| An angle judged on click rate, install rate or CPM | Cost per result of its goal; click rate alone is clickbait, install rate is the store page, CPM is delivery |
| Mode A: hooks written before the angles are approved | Angles first, hooks after |
| Mode A: 20 videos built in one go, the budget gone | 2 to 3 angles × 3 hooks first; more for the promising angles |
| Mode A: an AI "doctor" with titles giving advice | Playful role, insider, parent or a real expert; no credentials, no advice |
| Mode A: the new person says the old script (that's audience variations) | Each angle has its own argument and script |
| Mode B: the DNA describes the topic, not the mechanism | The element table: mechanism vs content, the "would it work with another pain?" test |
| Mode B: the format, beat order or hook mechanism changed "so the angle fits" | That's mode A or a new concept; pick an angle that fits the wrapper |
| Mode B: the person changed with the angle (two tests in one) | The same person; audience variations later |
| Mode B: the character node rerun, so the face changed | Keep the copied result; pass it as a reference |
| Nobody knows why the original works | Ask for numbers and the user's view; say once that an unproven ad multiplies a guess |
| Angles invented without reading the Brand Kit, or with no segment and evidence | The angle sheet: segment, bucket, evidence for every row |
| Only Adapt (safe) or only Explore (bets) | Mostly Adapt, one or two Explore |
| Three angles that are one angle reworded | Different perspectives or reasons, different situations |
| An angle the app can't truthfully answer, or a borrowed feature | One real feature per angle; no fit → drop the angle |
| The place chosen because it looks good | The angle's pain moment picks the place |
| "Same scene, but in a library" in the prompt, so the old room stays | Describe the new place in full; the character image is only for identity |
| An old place, person, prop or line left in a node | `get_workflow` on the variation; search every prompt for the old angle |
| Timing drifts, or the new VO is longer | Mode B timing contract (±0.5 s per beat, words ±10%); VO ≤ clip − 1 s |
| A new claim arrives with the angle | Claims identical across angles, from the Brand Kit only |
| Music, CTA, offer or end card changed "for variety" | The Pocket and the music stay |
| The original edited instead of a variation | Original untouched as Main; `create_variation` per angle |
| A variation copied from another angle | Always copy from the original |
| A competitor or brand named in the old-way beat | Generic objects only |
| "Are you exhausted?" in the hook | First person about their own life; situation callouts only |
| A competitor's ad used as the source | `lyra-copy-competitor-ad` first |

## Quality gates (concept multiplier)

- **Stage 0 (notes; Claude checks before sending):** the mode asked in plain words and picked by the user? Every angle in the angle sheet with a segment, bucket, evidence and a one-line hypothesis, answered by a real feature? Angles really different? **Mode A:** concept card with its mechanism; angles in 6 to 7 words; each with its own person, place and argument; hooks only after the angles are approved; no fake experts; budget sized (angles × hooks)? **Mode B:** DNA element by element with why it works; situations derived from each angle's pain moment; lock list; beat sheet with the same jobs, order and timing, word counts about ±10%; the same hook kind and mechanism? Both: no new claims, no personal-attribute callouts, no brands?
- **Stage 1 (images):** mode A: each angle's person reads as that perspective in one glance, natural, no titles or logos? Mode B: the same person as the original, the new situation reads at thumbnail size, the original's framing kept, no trace of the old place? Both: hands, phone and screen right (the screen identical to the screenshot)? No readable text? As phone-real as the original?
- **Stage 2 (clips):** mode A: each angle's body tells its own argument; the hooks of one angle cut cleanly into its body? Mode B: the beats and timing match the original, the same camera and cut rhythm, the same voice? Both: lines said right, the app name pronounced right, the person stable through the cuts? If [Video1] was used: nothing of the old place or words leaked in?
- **Stage 3 (finals):** mode A: the angles clearly different perspectives on one concept, the same Pocket and length? Mode B, side by side with the original: muted, the same concept; read, a different ad? Both: captions match the new words, the same music, CTA, offer and end card, 9:16, the original's resolution, planned length, named with its `C·A·H` code, AI label reminder given?

## After the test

- Launch the control and the angles the same day, with the same setup and budget.
- Tag every ad with its concept, angle and hook (the codes), so results can be read **per level**: a good hook rate with a poor ROAS is a hook that works on an angle that doesn't convert, not a dead concept. Example: Authority figure × financial expert: hook rate ok, CTR decent, ROAS poor → the hook gets people in; this concept-angle pair doesn't convert them.
- Sort every ad into four groups: **Winners · Losers · Needs attention** (fatiguing, clickbait or borderline) · **Requires more data**. With Lyra's analytics, its labels and its pass mark decide: a changed video passes at least 20% below its base's cost per result, a new one 20% below the goal's usual cost (or below the video it started from, when that one is cheaper), read after 30 results in its first 14 days. Without them, judge each ad at 5,000+ impressions and by CPA / ROAS, as in `lyra-video-hooks` (After the test).
- **Judge an angle on the cost per result of its goal**, never on one rate: an angle shapes the whole ad, not one step. The steps say where it works: opening (hook rate), hold (hold rate), click (CTR). Click rate alone never makes an angle good: high clicks with dear results is clickbait. Click-to-install depends on the store page, the same for every ad, so it says little about the angle. CPM is delivery, never the angle's fault. Compare only within one optimisation goal.
- **Mode A learning:** which perspective carries the concept → more hooks on it, the winning perspective in mode B (new reasons in its wrapper), audience variations of it. **Mode B learning:** which reason sells → add it to the Brand Kit's pain map as proven; a losing angle in a winning wrapper is a clean "no" on that angle; every angle losing against the control → the original may have won for its angle, not its wrapper: go back to it with hooks.
- Expect few winners: about 1 concept in 10 becomes one, and a winner fatigues in about 4 to 8 weeks (Singular benchmark, quoted by the team). A wrapper carries several rounds of angles; when two rounds in a row stop beating the control, it is tired: time for a new concept.
- Save to the project's creative repository: concept, angle, mode, hook, segment, bucket, evidence, hypothesis, result, so the next round (and the research agent) starts from what was learned.
