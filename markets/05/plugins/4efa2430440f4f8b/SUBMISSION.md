# Submission notes

## Proposed listing

**Display name:** Human Prose Editor

**Short description:** Remove AI-writing habits without flattening voice.

**Long description:** Human Prose Editor edits, audits, and drafts prose using a strict anti-slop workflow. It composes narrative in coherent units of thought and movement, repairs weak scene and paragraph architecture, and runs structural and cadence checks before returning fiction. It also targets canned significance, generic abstraction, repetitive rhetorical templates, promotional puffery, weak attribution, dialogue without grounding, and recurring LLM cadence while preserving the writer's facts, voice, pacing, and genre.

**Category:** Productivity

## Publisher fields still required

The public submission form requires real publisher information. Fill these with the verified identity and public URLs you actually control:

- Developer identity
- Website
- Support URL
- Privacy policy URL
- Terms URL
- Production-ready logo

Do not invent these fields. They need to match the verified publisher identity.

## Starter prompts

1. De-AI this draft without flattening my voice.
2. Audit this passage for AI-writing patterns.
3. Rewrite this scene with grounded dialogue.

## Positive trigger tests

### Positive 1

**Prompt:** `De-AI this paragraph, but keep my profanity and sentence rhythm.`

**Expected behavior:** Activate the skill, identify the draft's existing voice, and make only changes needed to remove relevant AI-pattern habits.

**Expected result shape:** Full revised paragraph with no process commentary unless requested.

**Fixture data:** Any 150 to 300 word paragraph containing at least two covered patterns.

### Positive 2

**Prompt:** `Audit this chapter for AI-slop. Do not rewrite it.`

**Expected behavior:** Activate in audit mode, report concrete recurring patterns, and avoid guessing whether AI authored the chapter.

**Expected result shape:** Findings grouped by pattern, each with a short excerpt and a specific fix. No full rewrite.

**Fixture data:** A 700 to 1,500 word prose sample containing repeated significance inflation, superficial analysis, or templated rhetoric.

### Positive 3

**Prompt:** `Rewrite this argument so it stops doing the "not X, but Y" thing every paragraph.`

**Expected behavior:** Activate and remove repetitive corrective parallelism while preserving genuine contrasts required by the argument.

**Expected result shape:** Full revised passage.

**Fixture data:** A 300 to 700 word argument with several negative-parallelism constructions.

### Positive 4

**Prompt:** `Fix the floating dialogue in this scene, but don't add a gesture after every line.`

**Expected behavior:** Activate the fiction rules, ground sustained dialogue through scene movement, POV, action, and character behavior, and avoid mechanical beat insertion.

**Expected result shape:** Full revised scene with dialogue embedded in normal prose paragraphs.

**Fixture data:** A 500 to 1,000 word scene containing several stretches of bare back-and-forth dialogue.

### Positive 5

**Prompt:** `Draft this scene from my outline and apply the Human Prose rules before you show it to me.`

**Expected behavior:** Activate in draft mode, follow the supplied story constraints first, draft the scene, and internally apply the prose and continuity checks.

**Expected result shape:** Finished scene only unless the prompt asks for notes.

**Fixture data:** A short scene outline including POV, setting, characters, and at least one continuity constraint.

### Positive 6

**Prompt:** `Rewrite this passage using the Human Prose rules. Fix the staccato cadence without losing the scene's facts: Peter stayed there long enough to be sure. The ache never started. His shoulders sagged. He turned toward the sink and reached out, expecting his hand to hit porcelain. It did. What bothered him was that he had known where it would be. Peter drew his hand back and stood without touching anything.`

**Expected behavior:** Activate the skill and diagnose semantic beat stacking even though the passage mixes short and medium-length sentences. Treat the sequence as waiting, result, reaction, action, result, interpretation, and reaction, then rebuild the paragraph around the relationships among those beats instead of polishing each sentence separately.

**Expected result shape:** A natural paragraph of rhythmically varied sentences that preserves the missing ache, easing shoulders, sink, porcelain, accurate expectation, disturbed reaction, and withdrawal. The rewrite should not retain the original one-beat-per-sentence architecture or mechanically join every sentence with conjunctions.

**Generalization requirement:** Peter is only a regression fixture. The same diagnosis and structural repair must apply to other characters and narrators, every POV and tense, and narrative modes such as action, introspection, description, memory, memoir, and narrative nonfiction.

### Positive 7

**Prompt:** `Fix the semantic beat stacking in this first-person passage while preserving its voice: I kept my hand on the letter. The paper had gone warm beneath my palm. I knew what the signature meant. I did not open it. Instead, I listened to the refrigerator hum in the next room. The sound made the apartment feel emptier. I folded the letter once and put it in my pocket.`

**Expected behavior:** Activate the skill and identify one-beat-per-sentence architecture in first-person introspection even though the passage is not an action chain and does not resemble the Peter fixture. Rebuild the movement among touch, recognition, refusal, displaced attention, loneliness, and decision without flattening the narrator's restraint.

**Expected result shape:** A cohesive paragraph with varied cadence and clear relationships among the thoughts, sensations, and actions. It should preserve the letter, its warmth, the meaningful signature, the unopened state, the refrigerator hum, the apartment's emptiness, and the final fold and pocketing without retaining the original sentence map.

**Fixture data:** The complete passage is included directly in the prompt. No external context is required.

### Positive 8

**Prompt:** `Edit this scene without adding new actions or dialogue: Mara noticed how quickly he had crossed the room, but she did not ask about it. There were more important problems to deal with first. Blood ran down his sleeve. She opened the first-aid kit and reached for the gauze.`

**Expected behavior:** Identify the first two sentences as authorial-management leakage if their only function is explaining why Mara obeys a discovery constraint. Remove that management layer and let the supported first-aid action carry the scene.

**Expected result shape:** A concise passage centered on the bleeding arm and first-aid kit. It must not invent a command, motive, new action, or explanation for Mara's silence.

**Fixture data:** The complete passage is included directly in the prompt. No external context is required.

### Positive 9

**Prompt:** `Repair the scene architecture, not just the sentences: The lettering on the bottle sharpened until he could see flaws in the ink. The wood grain on the desk separated into tiny fibers. When he looked at the curtain, individual threads became visible too. That was impossible. He opened the cabinet. He moved two jars aside. He found the painkillers behind them. He took down the bottle and opened it.`

**Expected behavior:** Detect repeated proof of one perceptual condition, a redundant micro-verdict, and procedural bookkeeping. Preserve the established perception and retrieval of painkillers while compressing demonstrations and intermediate movements.

**Expected result shape:** A structurally rebuilt passage, not a sentence-by-sentence polish. It should retain no more sensory proof than the moment needs, omit or earn the interpretation, and compress the cabinet procedure around its intention without inventing consequences.

**Fixture data:** The complete passage is included directly in the prompt. No external context is required.

### Positive 10

**Prompt:** `Fix the dialogue architecture while preserving the medical facts: "Does your head hurt?" "Yes." "Are you dizzy?" "A little." "Did you eat?" "No." "Do your eyes hurt too?" "Yes." She picked up the car keys.`

**Expected behavior:** Recognize that the character has enough information to act before completing an orderly symptom checklist. Move the exchange toward the established decision represented by the keys, without narrating that she has heard enough.

**Expected result shape:** Grounded dialogue or narration that preserves headache, dizziness, lack of food, eye pain, and the keys while avoiding mechanical interview rhythm. It must not invent a diagnosis, destination, relationship, or additional action.

**Fixture data:** The complete passage is included directly in the prompt. No external context is required.

### Positive 11

**Prompt:** `Write this scene as finished fiction: Lena hears a window break behind her. Glass scatters across the floor. A man climbs through the frame with a knife. She backs toward the kitchen before he gets both feet inside.`

**Expected behavior:** Compose the first visible response in coherent units of movement rather than drafting each outline beat as a separate sentence or paragraph. Express the relationships among sound, turn, broken glass, intrusion, knife, and retreat through syntactic hierarchy and POV attention, then run the structural and cadence checks before returning the scene.

**Expected result shape:** Finished narrative prose whose developed paragraphs connect simultaneous and causal events. It must preserve every supplied fact, avoid inventing motives or consequences, and contain no visible raw shot-list pass or process commentary.

**Fixture data:** The complete scene outline is included directly in the prompt. No external context is required.

### Positive 12

**Prompt:** `Rewrite this action beat without losing the impact of the first sentence: The gun went off. Lena ducked. The bullet hit the wall. Plaster burst beside her. She covered her head.`

**Expected behavior:** Preserve `The gun went off` as an earned short impact sentence, then detect the remaining action, result, sensory consequence, and reaction as a flat semantic chain. Resume connected prose through simultaneity and causality instead of waiving the cadence check because the scene is fast or dangerous.

**Expected result shape:** A compact action paragraph with the gunshot emphasized and the subsequent beats hierarchically connected. It must preserve Lena ducking and covering her head, the bullet striking the wall, and the burst plaster without adding injuries, locations, or motives.

**Fixture data:** The complete passage is included directly in the prompt. No external context is required.

### Positive 13

**Prompt:** `Fix the syntactic hierarchy without turning this into one overloaded sentence: Jonah opened the envelope. His hands were shaking. He saw the hospital logo. He stopped.`

**Expected behavior:** Distinguish primary actions from supporting circumstance and triggering perception. Combine related information through natural hierarchy while preserving a useful boundary if the emphasis needs one.

**Expected result shape:** Clear prose that preserves the envelope, shaking hands, hospital logo, and Jonah stopping. It should not keep every fact at equal sentence weight, invent the letter's contents, or produce an unwieldy clause chain.

**Fixture data:** The complete passage is included directly in the prompt. No external context is required.

## Negative trigger tests

### Negative 1

**Prompt:** `Translate this paragraph into Spanish.`

**Expected behavior:** Do not activate solely because the input is prose.

**Expected fallback:** Perform an ordinary translation without anti-AI rewriting.

**Why the plugin should stay out:** The user requested language conversion, not style editing.

### Negative 2

**Prompt:** `Summarize this article in 200 words.`

**Expected behavior:** Do not activate solely because the source contains prose.

**Expected fallback:** Produce an ordinary faithful summary.

**Why the plugin should stay out:** The task is content compression, not de-AI editing.

### Negative 3

**Prompt:** `Check only spelling and punctuation. Do not change my style.`

**Expected behavior:** Respect the explicit narrow scope and do not apply the broader anti-AI rewrite.

**Expected fallback:** Correct only spelling and punctuation.

**Why the plugin should stay out:** Broader prose changes would conflict with the user's explicit constraint.

## Boundary tests

**Prompt:** `What is negative parallelism in writing?`

Ordinary explanation is sufficient. If the plugin is explicitly selected, it may explain the concept but should not invent a rewrite task.

**Prompt:** `Make this clearer.`

Activation is optional. If it activates, make the minimum effective edit and do not assume the user wants an aggressive de-AI rewrite.

**Prompt:** `Give me only raw beat notes for this scene, one fragment per line.`

If the plugin is active, respect the requested working format. Do not force developed narrative paragraphs or run the ordinary visible-fiction quality gate on material the user explicitly requested as fragments or beat notes.

## Initial release notes

Initial submission of Human Prose Editor, a skills-only prose editing workflow. It supports edit, audit, and drafting modes; includes a detailed AI-writing pattern reference and a fiction/dialogue final check; makes no external network calls; and requires no connected app or MCP server.

## Version 0.1.1 release notes

Adds aggressive detection and repair of accidental staccato beat stacking. The editor now flags clusters of short declarative sentences, repeated subject-verb openings, one-detail-per-sentence fragmentation, and screenplay-like action/perception chains, then recombines them into natural paragraphs while preserving intentional fragments used for panic, impact, interruption, shock, comic timing, or established voice. A required final cadence pass prevents longer scenes from slipping back into clipped beat-by-beat narration.

## Version 0.1.2 release notes

Expands staccato detection from sentence-length counting to semantic beat analysis. The editor now catches mixed-length passages in which related actions, results, reactions, perceptions, and interpretations are isolated into separate sentences, even when a longer sentence interrupts the run. Paragraphs are audited by narrative function, including across adjacent one-sentence paragraphs, and structurally rebuilt through causality, simultaneity, subordination, POV attention, grouping, and deletion of unnecessary beats. The rule applies across fiction, memoir, narrative nonfiction, genres, POVs, tenses, voices, and scene types; examples are regression fixtures rather than templates. When cadence itself is defective, this structural rewrite takes priority over preserving the original sentence boundaries or making only sentence-level edits.

## Version 0.1.3 release notes

Promotes scene architecture above surface cleanup. The editor now removes authorial-management leakage and prompt-compliance narration, compresses repeated demonstrations and mundane procedural bookkeeping, groups sensory evidence by narrative purpose, cuts redundant post-event micro-verdicts, and moves dialogue beyond mechanical fact gathering once characters have enough information to take a position. These patterns are structural defects alongside semantic beat stacking, so the editor may rebuild or delete supported material instead of polishing every original sentence. Guardrails preserve meaningful absence, escalation, procedure, sensory accumulation, interpretation, and structured questioning when they perform real narrative work, and forbid invented replacement actions, motives, dialogue, decisions, or sensory facts.

## Version 0.1.4 release notes

Adds composition-first paragraph architecture and a mandatory pre-return fiction quality gate. Fiction is now composed in coherent units of thought, attention, conversation, action, and physical movement instead of being drafted as isolated semantic beats for later repair. The editor prefers syntactic hierarchy when causality, simultaneity, perception, and qualification connect events; treats developed multi-sentence paragraphs as the ordinary default without imposing a sentence quota; and audits adjacent one-sentence paragraphs and action-perception chains before the first visible response. Tense, visual, emotional, or action-heavy scenes do not receive an automatic cadence exemption. Short impact sentences, speaker changes, requested forms, and intentionally fragmented voices remain valid, while guardrails prevent overlong clause chains, dangling modifiers, participial clutter, arbitrary paragraph merging, and invented story material.
