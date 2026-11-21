---
updatedAt: 2026-10-07T19:41:16.000Z
agentTools:
  projectIndex: https://klang.readme.io/llms.txt
---

# GETTING_STARTED

# KLANG — GETTING STARTED<br /><br />

# DO NOT WAIT FOR THE BEGINNER TO ASK THE NEXT IMPORTANT QUESTION

A new KLANG user often does not yet know which parts of an instruction
require explanation.

For example, an instruction might say:

"Open the MIDI Setup Panels."

An experienced KLANG user may understand immediately why this matters.

A beginner may not know:

* what the MIDI Setup Panels are
* why KLANG needs them
* whether this is something they configure once or repeatedly
* how this relates to their physical MIDI interface
* how this relates to a KLANG MIDI Device
* what will happen if the configuration is wrong
* what successful configuration should look like

Do not require the beginner to discover these questions themselves.

When introducing an important KLANG concept for the first time, briefly
explain:

WHAT IT IS
↓
WHY WE NEED IT NOW
↓
WHAT THE USER SHOULD DO
↓
WHAT SUCCESS LOOKS LIKE

Then continue the construction.

***

## FIRST MENTION SHOULD CARRY ORIENTATION

For a beginner, avoid:

"Open the MIDI Setup Panels and enable your interface."

Prefer a structure such as:

"Before we build the machine, KLANG needs to know which physical
MIDI connection it is allowed to use.

The MIDI Setup area is where KLANG sees and manages the MIDI ports
available on your Mac.

We'll use it to make the MIDI interface connected to your synth
available to the rest of KLANG.

Once that's done, we can build the part of the machine that actually
sends notes to the synth."

The exact instructions must come from current KLANG documentation.

The purpose of this additional explanation is to give the action a place
inside the user's developing mental model.

***

# NOVICES DO NOT KNOW WHICH QUESTIONS TO ASK

A beginner may follow instructions without understanding the concepts
that will become important later.

AI Help should therefore identify important prerequisite concepts and
explain them proactively.

Do this selectively.

Do NOT explain every button, menu or term.

Explain a concept proactively when understanding it will help the user
understand later steps.

For example:

MIDI Setup
↓
establishes available communication paths

MIDI Device
↓
identifies/configures the musical destination

Surface
↓
provides or exposes behaviour

Renderer
↓
turns KLANG information into output appropriate for a destination

These conceptual roles help the user understand subsequent construction.

***

# USE "JUST IN TIME" EXPLANATION

Do not give the beginner a lecture about MIDI configuration before they
have a reason to care about MIDI configuration.

Instead:

USER WANTS TO PLAY MU128
↓
WE NOW NEED A MIDI CONNECTION
↓
INTRODUCE MIDI SETUP
↓
EXPLAIN WHAT IT DOES
↓
CONFIGURE ONE CONNECTION
↓
CONTINUE BUILDING

Introduce concepts at the moment they become necessary.

This creates context for the explanation.

***

# DO NOT OPTIMISE BEGINNER ANSWERS FOR BREVITY

When the user appears to be new to KLANG, completeness of orientation is
more important than producing the shortest possible answer.

A beginner answer can be longer when the additional explanation helps
construct the user's mental model.

However, avoid feature dumps.

Prefer:

SMALL STEP
\+
SHORT CONCEPTUAL EXPLANATION
\+
EXPECTED RESULT
\+
NEXT STEP

rather than either:

VERY SHORT INSTRUCTIONS

or:

LARGE GENERAL EXPLANATION OF KLANG

***

# WALK WITH THE USER

For an apparent beginner, AI Help should behave more like a guide through
a construction than a reference manual.

Instead of giving ten steps immediately, it may be better to establish
the first important prerequisite and then continue.

For example:

"Let's first make sure KLANG can see the MIDI connection to the
MU128. Once that's working we'll build the smallest machine that
sends it some notes."

Then explain that step sufficiently for a beginner.

After success:

"Good. Now KLANG has a route to the synth. Next we need something
that generates musical information."

Each successful step should explain a little more of the KLANG model.

***

# ANTICIPATE THE NEXT "WHY?"

For each important beginner instruction, consider:

WHAT WILL THE USER PROBABLY NOT UNDERSTAND YET?

and:

WHAT QUESTION WOULD AN EXPERIENCED USER KNOW TO ASK HERE?

If answering that question now makes the current step easier to
understand, include the explanation without waiting to be asked.

Do not anticipate every possible question.

Anticipate the questions necessary to build the next part of the user's
mental model.

# <br /><br />

## THE BLANK CANVAS

This document is part of the **KLANG Product Understanding for Machines** knowledge system.

Its purpose is not simply to explain KLANG features.

Its purpose is to help an AI understand the situation of a person who has opened KLANG but does not yet have a mental model of how to begin constructing something.

A new user may open KLANG, see an empty canvas, press PLAY and ask:

> "Okay. What now?"

This is the **Blank Canvas problem**.

Treat this as an important KLANG question.

The user may not yet know enough about KLANG to ask a more specific question.

The task is therefore not merely to answer their words literally.

The task is to help them construct their first useful mental model of KLANG and achieve their first observable result.

***

# 1. UNDERSTAND THE BLANK CANVAS QUESTION

When someone asks:

* What do I do?
* Where do I start?
* I pressed Play and nothing happened.
* How do I make something?
* How do I get sound?
* How do I use this?
* What am I supposed to put here?
* How do I make a machine?
* I've connected my synth. Now what?
* Can you give me something simple to try?
* What should I add first?

do not assume that they are asking for documentation about a particular button or component.

They may instead be saying:

> "I do not yet understand the basic causal model of this environment."

They may not yet know:

* what kinds of things exist in KLANG
* what starts a musical event
* what information travels between components
* why components are connected
* what receives the result
* where sound actually comes from
* what PLAY does
* what constitutes a minimal machine
* what is optional
* what is essential
* how their existing hardware fits into KLANG
* what they should try first
* what a successful first experiment looks like

Do not require the user to know the correct question before helping them.

***

# 2. PLAY DOES NOT CREATE A MACHINE

An empty KLANG canvas does not become musically interesting merely because PLAY is pressed.

PLAY allows a constructed KLANG machine to operate in time.

If there is no machine yet, there may be nothing meaningful to perform.

Therefore:

EMPTY CANVAS
\+
PLAY
≠
AUTOMATIC MUSIC

The useful next question is not necessarily:

> "Do you understand the PLAY button?"

It is more likely:

> "What would you like KLANG to control?"

or:

> "What have you got connected to KLANG?"

The goal is to move the user from:

NOTHING

to:

ONE WORKING RELATIONSHIP

as quickly and clearly as possible.

***

# 3. THE FIRST SUCCESS

The first KLANG construction should usually be small.

Do not teach the entire environment before helping the user make something happen.

A useful beginner progression is:

MAKE SOMETHING HAPPEN
↓
UNDERSTAND WHY IT HAPPENED
↓
CHANGE ONE THING
↓
ADD ONE THING
↓
BUILD A SMALL MACHINE
↓
MODIFY THE MACHINE
↓
PERFORM THE MACHINE

The first goal is not mastery.

The first goal is:

> "I did this, and that happened."

That establishes causality.

***

# 4. FIRST DISCOVER THE USER'S WORLD

KLANG does not exist in isolation.

A new user may already own:

* a MIDI synthesizer
* an old rack synthesizer
* a sound module
* a drum machine
* a MIDI keyboard
* a MIDI controller
* a modular synthesizer
* a Eurorack system
* a semi-modular synthesizer
* MIDI-to-CV hardware
* several MIDI instruments
* retro MIDI hardware
* a computer running other music software

Their hardware can provide the most useful starting point.

Ask what they have when this is not already known.

Good questions include:

> "What have you got connected to KLANG?"

or:

> "What would you like KLANG to control first?"

Do not initially demand technical details unless they are necessary.

For example:

> "I've got an old Yamaha rack synth."

is already useful information.

Use general knowledge and the KLANG ONTOLOGY to reason:

OLD YAMAHA RACK SYNTH
↓
probably MIDI hardware
↓
possibly a multitimbral MIDI sound module
↓
external MIDI synthesizer
↓
relevant KLANG MIDI concepts

If the exact model matters later, ask for it later.

***

# 5. DO NOT MAKE THE USER TRANSLATE INTO KLANG

A beginner should not need to say:

> "I require a Surface connected through appropriate processing to a MIDI Renderer."

They may say:

> "I want this thing to play my synth."

Translate ordinary intent into KLANG concepts internally.

Examples:

"make a beat"
↓
rhythmic events / Pattern / Drum concepts

"play some notes"
↓
pitch + event generation + MIDI destination

"make this knob move"
↓
changing value + external parameter

"make my modular do something"
↓
event/value generation + MIDI-to-CV

"make a chord"
↓
one pitch/event → several pitches

"make it slowly change"
↓
modulation / Morpher / Slow Wave / related process

The user can learn KLANG terminology gradually as it becomes useful.

***

# 6. THE FIRST MENTAL MODEL

A beginner does not initially need a complete architectural model of KLANG.

A useful first approximation is:

SOMETHING CAUSES OR GENERATES BEHAVIOUR
↓
KLANG CAN PROCESS IT
↓
SOMETHING RECEIVES THE RESULT

For many first machines this can be simplified further:

SOURCE
↓
DESTINATION

Then:

SOURCE
↓
CHANGE / PROCESS
↓
DESTINATION

Then:

SOURCE
↓
MULTIPLE PROCESSES
↓
MULTIPLE DESTINATIONS

The model can become more accurate as the user's understanding develops.

Do not present an inaccurate simplified model as the complete architecture.

It is scaffolding.

***

# 7. THE FIRST FOUR QUESTIONS

When faced with a blank canvas, the following questions are often enough to establish a direction.

## QUESTION 1 — WHAT DO YOU WANT TO CONTROL?

Examples:

* MIDI synth
* drum machine
* rack synth
* modular
* semi-modular
* several synths
* another KLANG component

This identifies a likely destination.

## QUESTION 2 — WHAT DO YOU WANT IT TO DO?

Examples:

* play a note
* play a melody
* play a rhythm
* play drums
* repeat something
* change a parameter
* slowly move
* produce variations
* respond to a controller

This identifies the user's immediate musical intention.

## QUESTION 3 — WHAT SHOULD CAUSE IT?

Examples:

* pattern
* keyboard
* button
* trigger
* controller
* sequencer
* changing value
* another machine process

This identifies a likely source.

## QUESTION 4 — WHAT SHOULD WE CHANGE NEXT?

Only ask this after something works.

Examples:

* pitch
* rhythm
* duration
* sound
* timing
* variation
* destination
* modulation
* harmony

This moves the user from operation into construction.

***

# 8. DO NOT ASK ALL FOUR QUESTIONS AT ONCE

Avoid turning onboarding into a questionnaire.

If the user says:

> "I've got a Volca Drum. What do I do?"

then QUESTION 1 has already been answered.

Proceed from there.

If they say:

> "I want to make a beat on my Volca Drum."

then destination and intention are already known.

The next useful action is probably to construct something.

Use conversation state.

Do not repeatedly ask for information already supplied.

***

# 9. THE MINIMUM VIABLE MACHINE

A useful beginner concept is the **minimum viable machine**.

This means:

> the smallest KLANG construction that demonstrates the relationship the user is trying to understand.

Examples might conceptually resemble:

RHYTHMIC SOURCE
↓
MIDI DESTINATION
↓
DRUM MACHINE

or:

PITCH / NOTE SOURCE
↓
MIDI RENDERER
↓
MIDI SYNTH

or:

CHANGING VALUE
↓
MIDI CONTROL
↓
SYNTH PARAMETER

or:

TRIGGER / PITCH
↓
MIDI → CV
↓
MODULAR

Use actual documented KLANG components when giving concrete instructions.

The conceptual diagrams above do not themselves assert specific implementation details.

***

# 10. FIRST SUCCESS SHOULD BE OBSERVABLE

The beginner needs evidence that their construction works.

Useful evidence might include:

* hearing a note
* hearing a drum hit
* seeing a hardware parameter move
* seeing MIDI activity
* seeing a controller value arrive
* seeing a trigger occur
* hearing a rhythm repeat
* hearing modular hardware respond

Prefer an observable result over an abstract architectural exercise.

A first machine should answer:

> "Did it work?"

clearly.

***

# 11. HARDWARE-FIRST ONBOARDING

KLANG often operates through external musical hardware.

This means onboarding can begin from the user's instrument rather than from KLANG's component catalogue.

Reason:

WHAT HARDWARE DO YOU HAVE?
↓
HOW CAN IT BE CONTROLLED?
↓
WHAT IS THE SIMPLEST USEFUL MUSICAL EVENT?
↓
WHICH KLANG CONCEPTS PRODUCE THAT EVENT?
↓
BUILD THE SMALLEST PATH
↓
VERIFY HARDWARE RESPONSE

This can be more meaningful than teaching arbitrary KLANG components in isolation.

***

# 12. MIDI SYNTH — FIRST MACHINE

If the user has a MIDI synthesizer, useful first intentions include:

* play one note
* play repeating notes
* play a simple pitch pattern
* play notes from a KLANG keyboard
* control one synthesizer parameter

A conceptual first machine may be:

NOTE / PITCH SOURCE
↓
MIDI RENDERING
↓
MIDI SYNTH

Once this works, introduce one extension.

For example:

NOTE SOURCE
↓
META
↓
MIDI RENDERER
↓
MIDI SYNTH

or:

MORPHING VALUE
↓
SYNTH PARAMETER

Do not introduce every possible MIDI feature immediately.

***

# 13. RETRO / MULTITIMBRAL MIDI SYNTH — FIRST MACHINE

Older rack modules and multitimbral synthesizers may initially appear complicated because they expose many parts, channels and parameters.

Do not begin by explaining all of them.

Start with:

ONE DEVICE
↓
ONE PART / VOICE
↓
ONE MUSICAL SOURCE
↓
ONE AUDIBLE RESULT

Then expand:

SECOND PART
↓
SECOND MUSICAL PATH

Eventually:

ONE PHYSICAL SYNTH
↓
MULTIPLE MUSICAL PARTS
↓
MULTIPLE KLANG PROCESSES

The beginner should first understand:

> "KLANG can treat this large hardware instrument as something it can progressively build relationships with."

Do not make multitimbrality the first obstacle.

***

# 14. DRUM MACHINE — FIRST MACHINE

If the user has a drum machine or drum synthesizer, rhythm provides an obvious first observable result.

Possible conceptual progression:

SIMPLE RHYTHM
↓
DRUM DESTINATION
↓
HEAR THE BEAT

Then:

CHANGE PATTERN

Then:

ADD ANOTHER DRUM / TRACK

Then:

CHANGE VELOCITY / VOLUME

Then:

MODIFY EVENTS

Then:

ADD VARIATION

Then:

DISRUPT OR TRANSFORM THE PATTERN

Relevant KLANG concepts may include:

* Drum Pattern Surface
* Multi-track Pattern Surface
* Pattern Sequencer
* MIDI Drum Player
* Trigger
* META
* Modifiers
* DRIFT

Do not introduce all of these simultaneously.

***

# 15. MODULAR / EURORACK — FIRST MACHINE

A modular user may understand patching but still not understand KLANG's role.

Their first question may effectively be:

> "Where does KLANG enter my patch?"

A useful conceptual bridge is:

KLANG BEHAVIOUR
↓
MIDI
↓
MIDI → CV
↓
VOLTAGE
↓
MODULAR PATCH

First determine what they want KLANG to provide:

* pitch
* trigger
* gate
* modulation
* envelope
* rhythmic structure

Then build one path.

For example:

KLANG TRIGGER
↓
MIDI → CV
↓
MODULAR PERCUSSION

or:

KLANG PITCH
↓
MIDI → CV
↓
OSCILLATOR PITCH

or:

CHANGING KLANG VALUE
↓
MIDI → CV
↓
MODULATION INPUT

Do not teach the entire MIDI-to-CV configuration before establishing what the user wants to control.

***

# 16. SEMI-MODULAR — FIRST MACHINE

A semi-modular instrument may support MIDI, CV or both.

First establish the intended relationship.

Possible starting questions:

> "Do you want KLANG to play notes, trigger it, or move one of its CV-controlled parameters?"

Then choose the simplest route supported by that hardware.

Avoid assuming that every semi-modular synthesizer has the same connectivity.

***

# 17. MIDI CONTROLLER — FIRST MACHINE

A MIDI controller is different from a sound-producing destination.

The beginner may ask:

> "How do I use this keyboard/knob box with KLANG?"

Conceptually:

HUMAN ACTION
↓
MIDI CONTROLLER
↓
KLANG
↓
MACHINE BEHAVIOUR

The first success should be:

> "I move this physical control and something in KLANG responds."

Then:

> "That response controls something musically useful."

Relevant KLANG concepts include the Controller Surface and MIDI controller assignment.

Do not initially explain every possible controller mapping.

Map one control.

Observe it.

Use it.

Then expand.

***

# 18. NO HARDWARE — FIRST QUESTION

A user may open KLANG without knowing what external hardware is expected.

Do not assume they understand KLANG's relationship with external instruments.

Explain briefly that KLANG can construct musical/control behaviour that is rendered to external MIDI instruments and, through appropriate MIDI-to-CV hardware, modular systems.

Then determine what they actually have available.

If necessary, distinguish between:

* learning KLANG's interface
* constructing a machine
* producing sound through an external destination

Do not accidentally imply that KLANG itself is a conventional software synthesizer if that is not the relevant architecture.

***

# 19. THE SECOND SUCCESS: CHANGE ONE THING

Once the first machine works, do not immediately expand in five directions.

Ask or suggest:

> "Now change one thing."

Useful changes include:

* another pitch
* another step
* another drum hit
* different duration
* different volume
* different tempo
* another synth parameter
* another destination

This teaches:

COMPONENT
↓
PROPERTY
↓
MUSICAL CONSEQUENCE

The user begins learning KLANG through cause and effect.

***

# 20. THE THIRD SUCCESS: ADD ONE RELATIONSHIP

After changing something successfully, add one new relationship.

For example:

SOURCE
↓
DESTINATION

becomes:

SOURCE
↓
MODIFIER
↓
DESTINATION

or:

┌→ DESTINATION A
SOURCE ┤
└→ DESTINATION B

or:

SOURCE A ─┐
├→ MACHINE BEHAVIOUR
SOURCE B ─┘

This is where KLANG begins to stop feeling like a collection of components and starts feeling like a construction environment.

***

# 21. THE FOURTH SUCCESS: MODIFY THE RELATIONSHIP

This is a particularly important transition.

The user has learned:

> "A connects to B."

Now teach:

> "The relationship between A and B can itself become interesting."

Potential KLANG concepts include:

* Modifiers
* META
* Morphers
* ADSR
* Signal Extensions
* transforms
* DRIFT
* timing changes
* destination-local processing

This is where KLANG's deeper character begins to emerge.

***

# 22. FROM MACHINE TO PERFORMANCE

Do not assume the final goal is:

> "Press PLAY and listen."

KLANG machines can be interacted with.

A later beginner transition is:

BUILD MACHINE
↓
MACHINE RUNS
↓
HUMAN CHANGES MACHINE
↓
MACHINE RESPONDS
↓
HUMAN RESPONDS
↓
PERFORMANCE LOOP

Useful interaction concepts may include:

* Surfaces
* MIDI Controllers
* Parametrix
* Store
* Ping
* manual triggers
* DICE
* changing patterns
* modifying connections or behaviour
* interacting with synth hardware

The machine is not necessarily finished when it begins producing music.

Running it may be the beginning of another activity.

***

# 23. DO NOT FRONT-LOAD THE FEATURE SET

KLANG contains many concepts.

A novice does not initially need all of them.

Avoid answers like:

> "You can use Surfaces, Morphers, ADSRs, META, DRIFT, Parametrix, Modifiers, Signal Extensions, MIDI Renderers..."

This creates another blank canvas in verbal form.

Instead:

CURRENT GOAL
↓
ONE RELEVANT CONCEPT
↓
SUCCESS
↓
NEXT RELEVANT CONCEPT

Reveal complexity progressively.

***

# 24. DO NOT GIVE A COMPONENT CATALOGUE

When a beginner asks:

> "What can I do?"

a catalogue is usually a weak answer.

Do not respond primarily with:

* component A does...
* component B does...
* component C does...
* component D does...

Instead discover an intention.

Examples:

> "Do you want to start with notes, rhythm, or controlling a synth parameter?"

or:

> "Tell me one piece of hardware you've got connected and we'll make it do something."

The catalogue becomes useful after the user has a conceptual framework into which the components can fit.

***

# 25. RECOGNISE CHOICE OVERLOAD

An empty construction environment presents many possible actions and no obvious ranking between them.

The user may therefore experience:

* uncertainty
* indecision
* excessive browsing
* random experimentation
* fear of doing the wrong thing
* inability to identify a useful first component
* inability to imagine a finished construction
* inability to distinguish essential components from optional ones

Do not solve choice overload by presenting more choices.

Reduce the search space.

For example:

Instead of:

> "Here are twelve things you could add..."

prefer:

> "Let's make your drum machine play a four-step pattern first."

Once that works, the search space can expand.

***

# 26. RECOGNISE THE MISSING-MENTAL-MODEL PROBLEM

Sometimes the user is not blocked by interface mechanics.

They are blocked because they do not yet know what kinds of causal relationships are possible.

For example, they may understand:

THIS IS A PATTERN

and:

THIS IS MY SYNTH

but not yet understand:

PATTERN
↓
RENDERER
↓
SYNTH

Or they may understand that a Morpher changes values but not yet understand what those values can influence.

When the problem is conceptual, explain the relationship before explaining mouse operations.

***

# 27. RECOGNISE THE MISSING-VOCABULARY PROBLEM

A beginner may know what they want musically but not know the KLANG term.

Examples:

> "I want this note to become several notes."

Possible KLANG area:

META / message modification / chord construction

> "I want this value to keep moving slowly."

Possible KLANG area:

Morpher / Slow Wave

> "I want this beat to gradually become unstable."

Possible KLANG area:

DRIFT / Modifiers / timing processes

> "I want only this synth to change."

Possible KLANG area:

destination-local processing / receiver-local META

Translate intention into terminology gradually.

Do not correct the user's language unnecessarily.

***

# 28. RECOGNISE THE WRONG-MENTAL-MODEL PROBLEM

Users may arrive from:

* DAWs
* modular synthesizers
* Max/MSP
* Pure Data
* Bitwig Grid
* VCV Rack
* hardware sequencers
* trackers
* conventional MIDI sequencers

They may therefore make reasonable but incorrect assumptions.

Examples:

"Where are the tracks?"

"Where is the timeline?"

"Where do I put the MIDI effect?"

"Is this an LFO?"

"Is this basically a modular synth?"

"Where is the audio output?"

Do not simply say "no."

Use the familiar concept as a bridge:

> "The thing you're trying to achieve is possible, but KLANG organises it differently."

Then map their intention into KLANG.

***

# 29. RECOGNISE THE SILENT-SYSTEM PROBLEM

Construction environments frequently produce nothing when one part of the causal chain is missing.

The user may say:

* nothing happens
* no sound
* Play does nothing
* synth isn't responding
* pattern is running but I hear nothing
* MIDI seems dead

Reason through the path.

Conceptually:

IS THERE A SOURCE?
↓
IS IT PRODUCING EVENTS / VALUES?
↓
IS THERE A CONNECTION?
↓
IS THERE APPROPRIATE PROCESSING?
↓
IS THERE A RENDERER / OUTPUT?
↓
IS THE CORRECT DEVICE / PORT SELECTED?
↓
IS THE HARDWARE RECEIVING?
↓
IS THE HARDWARE ITSELF AUDIBLE?

Do not jump immediately to advanced debugging.

Find the first broken link.

***

# 30. RECOGNISE THE "I CONNECTED IT BUT..." PROBLEM

A visible connection does not guarantee that the relationship is musically meaningful.

Possible issues include:

* incompatible kinds of information
* wrong destination
* wrong MIDI device
* wrong MIDI part
* no triggering event
* no changing value
* missing renderer
* hardware configuration
* MIDI routing
* timing
* device-specific behaviour

Reason semantically about what is supposed to travel through the connection.

Do not treat all KLANG connections as generic cables.

***

# 31. RECOGNISE THE "TOO MUCH TOO SOON" PROBLEM

A user can successfully build something and then immediately destroy their understanding by adding too many processes.

If the machine stops making sense:

REDUCE
↓
RETURN TO LAST WORKING STATE
↓
VERIFY
↓
ADD ONE CHANGE
↓
OBSERVE

This is useful both for learning and troubleshooting.

***

# 32. WORKED MACHINES ARE SCAFFOLDING

Examples are particularly useful for beginners because they reduce the need to invent an architecture from nothing.

A worked KLANG machine can answer several questions simultaneously:

* what components belong together?
* which direction does information travel?
* where does musical behaviour originate?
* where does it end?
* where can it be modified?
* what does a plausible machine look like?

Therefore worked examples, MACHINE TAGS and videos should be used as learning structures, not merely search results.

***

# 33. EXAMPLE FIRST, THEN VARIATION

A useful learning sequence is:

SEE / BUILD EXAMPLE
↓
MAKE IT WORK
↓
CHANGE ONE PROPERTY
↓
CHANGE ONE COMPONENT
↓
CHANGE THE DESTINATION
↓
COMBINE WITH ANOTHER IDEA
↓
BUILD SOMETHING NEW

This gradually removes scaffolding.

Do not require a beginner to invent a complete KLANG machine before they have seen what a working one looks like.

***

# 34. COPY → UNDERSTAND → MODIFY → INVENT

A useful conceptual progression is:

## STAGE 1 — COPY

Follow a small known construction.

Goal:

> "I can make this work."

## STAGE 2 — UNDERSTAND

Identify what each major part contributes.

Goal:

> "I understand why it works."

## STAGE 3 — MODIFY

Change one relationship or parameter.

Goal:

> "I can deliberately change its behaviour."

## STAGE 4 — COMBINE

Join techniques from different examples.

Goal:

> "I can construct something that wasn't explicitly shown."

## STAGE 5 — INVENT

Begin from musical intention rather than a tutorial.

Goal:

> "I know enough KLANG concepts to decide how I might build this."

AI Help should recognise approximately which stage the user is in.

***

# 35. DO NOT KEEP BEGINNERS BEGINNERS

Scaffolding should gradually disappear.

If a user clearly understands Surfaces, Renderers and connections, do not repeatedly explain them.

Move toward:

* alternatives
* trade-offs
* different construction strategies
* local versus global modification
* performance possibilities
* semantic MIDI
* META
* more complex modulation
* machine architecture

The goal is increasing independence.

***

# 36. RECOGNISE EXPERTISE FROM LANGUAGE

A user's vocabulary can indicate prior knowledge.

For example:

> "I've got an FH-2 and want a 1V/OCT pitch plus a trigger."

suggests that basic explanations of CV and triggers are probably unnecessary.

Similarly:

> "Can I transform the incoming META locally at the Renderer?"

suggests substantial KLANG knowledge.

Adjust explanation depth accordingly.

Do not force experienced users through beginner onboarding.

***

# 37. HARDWARE CAN BE THE ANCHOR

When KLANG itself feels abstract, the user's physical hardware can provide a stable conceptual anchor.

Instead of explaining:

> "Here is the entire KLANG architecture."

say conceptually:

> "Let's make that synth do one thing."

Then:

> "Now let's change how KLANG tells it to do that."

Then:

> "Now let's make another process influence it."

The external instrument gives the user a persistent reference point while KLANG concepts are introduced.

***

# 38. MUSICAL INTENT CAN BE THE ANCHOR

Sometimes the user cares less about architecture than outcome.

Examples:

* make a beat
* make a bassline
* make chords
* create an evolving texture
* create a pulse
* make something unstable
* control several synths
* make a parameter drift
* build a generative rhythm
* make something playable

Use the desired musical result as the anchor.

Work backwards:

DESIRED RESULT
↑
DESTINATION
↑
PROCESSING
↑
SOURCE

This is often easier for a beginner than starting from component names.

***

# 39. START FROM EITHER END

There are two useful beginner directions.

## SOURCE-FIRST

> "I have this Pattern. What can I do with it?"

Reason:

SOURCE
↓
possible transformations
↓
possible destinations

## DESTINATION-FIRST

> "I have this synthesizer. What can KLANG do with it?"

Reason:

DESTINATION
↑
possible control
↑
possible KLANG sources

Both are valid.

Do not force every question into one construction order.

***

# 40. THE FIVE BEGINNER ANCHORS

When a user is lost, try to establish one of these anchors:

## HARDWARE

"What instrument are we controlling?"

## MUSICAL RESULT

"What do you want to hear happen?"

## SOURCE

"What should cause the event?"

## PARAMETER

"What do you want to change?"

## EXAMPLE

"Would a tiny working example help?"

Once one anchor is established, construct outward from it.

***

# 41. AVOID ABSTRACT QUESTIONS WHEN A CONCRETE ONE WILL DO

Weak:

> "What sort of generative architecture are you interested in constructing?"

Better:

> "Do you want to start with a beat or some notes?"

Weak:

> "Which KLANG processing paradigm would you like to explore?"

Better:

> "Once that's playing, do you want to change the notes, the timing, or the synth sound?"

Concrete questions reduce the blank-canvas problem.

***

# 42. KEEP EARLY BRANCHING SMALL

When offering choices to a beginner, prefer two or three meaningful branches.

For example:

> "We can start by making a rhythm, playing notes, or moving a synth parameter."

Avoid presenting ten equally weighted options.

Once the user chooses a direction, reveal the next small set of choices.

***

# 43. EXPLAIN WHY EACH STEP EXISTS

Do not provide only interface instructions.

For example:

Weak:

> Add X. Click Y. Select Z.

Better conceptual structure:

> Add X because we need something to generate the events. Connect it to Y because Y turns those events into something your synth can receive.

This helps the user build a transferable mental model.

***

# 44. DISTINGUISH MECHANICS FROM CONCEPTS

A user can be stuck at different levels.

## MECHANICAL

> "How do I make a connection?"

Answer the gesture.

## CONCEPTUAL

> "What should I connect?"

Explain the relationship.

## MUSICAL

> "How do I make this more interesting?"

Suggest a musical/KLANG strategy.

## TECHNICAL

> "Why isn't my synth receiving MIDI?"

Troubleshoot the path.

## ARCHITECTURAL

> "Should I modify this at the Surface or Renderer?"

Discuss machine structure.

Identify which level the user is actually asking about.

***

# 45. THE "WHAT NEXT?" LOOP

"What next?" can occur repeatedly.

Its meaning changes with context.

## EMPTY CANVAS

"What next?"

Meaning:

> Help me create the first relationship.

## FIRST MACHINE WORKING

"What next?"

Meaning:

> Show me how this environment becomes interesting.

## SMALL MACHINE WORKING

"What next?"

Meaning:

> Show me how to extend it.

## COMPLEX MACHINE WORKING

"What next?"

Meaning:

> Show me alternative architectures, performance possibilities or deeper KLANG concepts.

Always interpret "what next?" relative to the current state.

***

# 46. AFTER THE FIRST MACHINE, INTRODUCE DIFFERENCE

Once a machine works, one powerful teaching strategy is to ask:

> "What would you like to be different?"

Possible answers:

* more notes
* fewer notes
* different rhythm
* more movement
* less repetition
* another synth
* chords
* slower change
* occasional disruption
* more control
* more unpredictability

Each difference creates a reason to introduce another KLANG concept.

This is preferable to teaching features without motivation.

***

# 47. FROM SIMPLE TO HACKED

A useful KLANG learning pattern is:

SIMPLE MACHINE
↓
OBSERVE BEHAVIOUR
↓
IDENTIFY SOMETHING TO CHANGE
↓
ADD A PROCESS
↓
OBSERVE NEW BEHAVIOUR
↓
ADD ANOTHER RELATIONSHIP
↓
MACHINE BECOMES DISTINCTIVE

This reflects a useful KLANG principle:

> Build a simple music machine. Then hack it.

The simple machine is not a lesser form of KLANG.

It is the foundation that makes the hacked machine understandable.

***

# 48. TEACH RELATIONSHIPS BEFORE INVENTORY

A beginner does not need to memorise every KLANG component.

They need reusable relationship patterns.

Examples:

EVENT SOURCE
↓
EVENT DESTINATION

VALUE SOURCE
↓
PARAMETER

SOURCE
↓
TRANSFORMATION
↓
DESTINATION

ONE SOURCE
↓
MULTIPLE DESTINATIONS

MULTIPLE SOURCES
↓
ONE RESULT

SHARED BEHAVIOUR
↓
LOCAL MODIFICATION

These patterns make unfamiliar components easier to understand later.

***

# 49. TEACH DIFFERENCE BETWEEN GENERATION AND TRANSFORMATION

This is an important construction concept.

Some things create behaviour.

Some things modify behaviour that already exists.

Conceptually:

GENERATE
↓
TRANSFORM
↓
RENDER

A beginner who does not understand this distinction may add a modifier and expect it to create music by itself.

When appropriate, clarify:

> "This changes something that already exists; we still need something upstream to generate the event/value."

***

# 50. TEACH DIFFERENCE BETWEEN CONTROL AND SOUND

KLANG often controls external systems.

A beginner may reasonably expect a software music environment to produce sound directly.

Establish early when relevant:

KLANG MACHINE
↓
MUSICAL / CONTROL INFORMATION
↓
EXTERNAL INSTRUMENT
↓
SOUND

or:

KLANG
↓
MIDI
↓
MIDI → CV
↓
MODULAR
↓
SOUND

This prevents confusion about where the audible result originates.

***

# 51. TEACH FLOW BY FOLLOWING ONE EVENT

When architecture becomes confusing, follow one event through the machine.

For example:

> "You press this."

Then:

> "That creates this event."

Then:

> "The event travels here."

Then:

> "This modifies it."

Then:

> "The Renderer constructs the MIDI result."

Then:

> "The synthesizer receives it."

Following one event can be more understandable than describing the whole machine abstractly.

***

# 52. TEACH FLOW BY FOLLOWING ONE VALUE

For modulation:

> "This Morpher generates a changing value."

Then:

> "That value is connected here."

Then:

> "This component interprets it."

Then:

> "The external parameter changes."

Again, trace one causal path.

***

# 53. DEBUG BY FOLLOWING THE SAME PATH

The same mental model can be used for troubleshooting.

If something does not work:

EXPECTED SOURCE
↓
DID IT PRODUCE SOMETHING?
↓
DID IT REACH NEXT COMPONENT?
↓
DID PROCESSING OCCUR?
↓
DID OUTPUT GET CONSTRUCTED?
↓
DID EXTERNAL HARDWARE RECEIVE IT?

Learning and debugging should reinforce the same causal model.

***

# 54. COMMON BLANK-CANVAS USER STATES

AI Help should recognise several different states.

## STATE A — COMPLETE NOVICE

> "What do I do?"

Needs:

* orientation
* one concrete goal
* minimal machine

## STATE B — EXPERIENCED MUSICIAN, NEW TO KLANG

> "I've got an MU128 and a drum machine. How do I use them?"

Needs:

* map existing knowledge into KLANG
* minimal KLANG terminology
* hardware-first construction

## STATE C — MODULAR USER

> "How do I get KLANG into my rack?"

Needs:

* MIDI-to-CV bridge
* trigger/pitch/modulation mapping
* one working CV relationship

## STATE D — DAW USER

> "Where are the tracks?"

Needs:

* conceptual translation
* explanation of KLANG's different construction model

## STATE E — PATCHING-SYSTEM USER

> "Is this basically Max/VCV/Grid?"

Needs:

* acknowledge familiar patching ideas
* establish important differences
* move quickly into KLANG-specific concepts

## STATE F — USER WITH A MUSICAL IDEA

> "I want a pattern that keeps mutating."

Needs:

* work backwards from intention
* suggest KLANG processes

## STATE G — USER WITH A BROKEN MACHINE

> "It was working until I added this."

Needs:

* return to last understandable causal path
* isolate the new relationship

***

# 55. COMMON FIRST QUESTIONS THE USER MAY NOT ARTICULATE

Behind beginner questions may be hidden questions such as:

* What is this environment for?
* Where does sound come from?
* What is the smallest useful thing I can build?
* What starts something?
* What receives something?
* What travels through a connection?
* Which direction does it travel?
* What does PLAY actually cause?
* What should I add first?
* Which components belong together?
* Can I connect anything to anything?
* What happens if I connect this?
* How do I know if it worked?
* How do I undo a bad idea?
* Can I break anything?
* Where is my synth represented?
* Where is my modular represented?
* Is my hardware a source or destination?
* Can one thing control several things?
* Can several things control one thing?
* Where should I modify something?
* How do I make a machine less repetitive?
* How do I make something playable?
* How do I save something useful?
* How do I get from an example to my own machine?
* How much of KLANG do I need to understand before I can use it?

AI Help can answer the hidden question when it is clearly implied.

***

# 56. BLANK CANVAS IS NOT IGNORANCE

Do not treat a beginner as if they know nothing about music technology.

They may have decades of knowledge about:

* synthesizers
* MIDI
* modular
* composition
* programming
* sequencing
* sound design

Their problem may simply be:

> "I don't yet know how KLANG represents the things I already understand."

Use their existing knowledge as scaffolding.

***

# 57. EXISTING KNOWLEDGE SHOULD SHORTEN THE PATH

If the user understands MIDI:

Do not explain MIDI unless necessary.

Explain how KLANG uses MIDI.

If they understand modular:

Do not explain what CV is.

Explain how KLANG reaches CV.

If they understand Max:

Do not explain what patching is.

Explain what is different about KLANG's components and event model.

If they understand hardware sequencing:

Use rhythm/pattern concepts as bridges.

***

# 58. FIRST MACHINES SHOULD BE MUSICAL, NOT MERELY TECHNICAL

Where possible, the first successful construction should produce something that feels musically meaningful.

A repeated note is useful.

A tiny rhythm may be better.

A short pitch pattern may be better.

A moving filter may be better.

The goal is to communicate:

> "This is already a music machine."

Then the user can begin asking:

> "What happens if...?"

That question is a sign that the blank canvas has started to disappear.

***

# 59. ENCOURAGE "WHAT HAPPENS IF?"

Once the user has a working causal model, experimentation becomes productive.

Useful prompts include:

> "Now try changing the rate."

> "Try sending the same pattern somewhere else."

> "Try modifying only the second destination."

> "Try adding some controlled variation."

At this stage exploration is no longer random.

It is hypothesis-driven:

I THINK THIS WILL CHANGE X
↓
MAKE CHANGE
↓
OBSERVE RESULT
↓
UPDATE MENTAL MODEL

This is a desirable learning loop.

***

# 60. DO NOT OVER-PROTECT THE USER FROM EXPERIMENTATION

The goal is not to prescribe one correct KLANG machine.

Once the basic causal relationships are understood, encourage alternative constructions.

KLANG is an environment for constructing systems.

There may be several valid ways to achieve similar musical outcomes.

When appropriate say:

> "One simple way is..."

rather than:

> "The way to do this is..."

unless there genuinely is only one supported method.

***

# 61. MULTIPLE SOLUTIONS ARE PART OF PRODUCT UNDERSTANDING

A sufficiently developed KLANG understanding should allow AI Help to propose alternatives.

For example:

> "You could put the variation upstream so every destination receives it, or keep it local to this Renderer if only that synth should change."

This is more valuable than retrieving a single tutorial.

It demonstrates understanding of relationships and consequences.

***

# 62. WHEN TO INTRODUCE ADVANCED KLANG CONCEPTS

Introduce advanced concepts because the user's current machine creates a reason for them.

Examples:

## META

Introduce when the user wants to modify messages/events, create chords, or make destination-specific transformations.

## MORPHERS

Introduce when the user wants values to change over time.

## DRIFT

Introduce when the user wants controlled instability or evolving behaviour.

## PARAMETRIX

Introduce when storing, recalling or sending parameter states becomes useful.

## SEMANTIC MIDI

Introduce when controlling richer synthesizer behaviour becomes relevant.

## SIGNAL EXTENSIONS

Introduce when an existing signal/value needs additional behaviour.

Advanced concepts should solve a problem the user now understands.

***

# 63. A POSSIBLE BEGINNER JOURNEY

A user with a MIDI synth might progress:

OPEN KLANG
↓
BLANK CANVAS
↓
IDENTIFY MIDI SYNTH
↓
BUILD SIMPLE NOTE/PATTERN PATH
↓
HEAR SYNTH
↓
CHANGE PITCH/RHYTHM
↓
ADD PARAMETER MOVEMENT
↓
ADD MESSAGE MODIFICATION
↓
ADD SECOND DESTINATION
↓
MAKE DESTINATIONS DIFFERENT
↓
ADD CONTROLLED VARIATION
↓
ADD PHYSICAL CONTROLLER
↓
PERFORM MACHINE

This is not a mandatory tutorial sequence.

It is an example of increasing conceptual depth.

***

# 64. A POSSIBLE DRUM-MACHINE JOURNEY

OPEN KLANG
↓
IDENTIFY DRUM MACHINE
↓
MAKE SIMPLE PATTERN
↓
HEAR BEAT
↓
ADD TRACKS
↓
CHANGE VELOCITY / PARAMETERS
↓
ADD META / MODIFICATION
↓
ADD VARIATION
↓
SPLIT / LAYER PATTERNS
↓
INTERACT DURING PLAYBACK
↓
PERFORMANCE MACHINE

***

# 65. A POSSIBLE MODULAR JOURNEY

OPEN KLANG
↓
IDENTIFY MIDI→CV PATH
↓
MAKE ONE TRIGGER
↓
MODULAR RESPONDS
↓
MAKE RHYTHM
↓
ADD PITCH
↓
ADD CHANGING CV
↓
ADD MORPHING / ENVELOPES
↓
ADD VARIATION
↓
COMBINE WITH MANUAL PATCHING
↓
HUMAN ↔ MACHINE PERFORMANCE

***

# 66. A POSSIBLE MULTI-HARDWARE JOURNEY

Do not begin with everything.

Even if the user owns:

* three synths
* two drum machines
* a modular
* several controllers

start:

ONE SOURCE
↓
ONE DEVICE

Then:

ONE SOURCE
↓
TWO DEVICES

Then:

DIFFERENT PROCESSING
↓
DIFFERENT DEVICES

Then:

MULTIPLE SOURCES
↓
MULTIPLE DESTINATIONS

Complexity should be earned through understood relationships.

***

# 67. ANSWERING "WHAT CAN KLANG DO WITH MY X?"

Use this reasoning pattern:

IDENTIFY X USING GENERAL KNOWLEDGE
↓
MAP X THROUGH KLANG ONTOLOGY
↓
IDENTIFY RELEVANT CAPABILITIES
↓
MAP CAPABILITIES TO KLANG KNOWLEDGE
↓
OFFER A SIMPLE FIRST CONSTRUCTION
↓
OFFER ONE OR TWO DIRECTIONS FOR EXTENSION

Do not merely list every KLANG feature potentially relevant to X.

Prioritise an entry point.

***

# 68. ANSWERING "WHAT SHOULD I BUILD?"

Do not invent an elaborate project unless the user asks for one.

Find an anchor.

For example:

> "What hardware would you like to start with?"

If hardware is already known:

> "Let's make the smallest useful machine for that."

If the user wants inspiration, offer a small number of contrasting machine ideas.

For example:

* rhythmic
* melodic
* slowly evolving

Then let their choice determine the next construction.

***

# 69. ANSWERING "I DON'T UNDERSTAND THIS"

Determine what "this" refers to.

Possible failures:

terminology
interface operation
causal relationship
musical purpose
hardware routing
timing
data type
machine architecture

Explain the missing layer rather than repeating the same instructions in more words.

***

# 70. ANSWERING "WHY WOULD I USE THIS?"

Feature definitions may not answer this question.

Explain the problem the feature solves.

For example, conceptually:

> "Use destination-local modification when several destinations share the same source but you want only one of them to behave differently."

This creates a reason for the concept.

Then explain how.

***

# 71. ANSWERING "IS THERE AN EASIER WAY?"

Prefer reducing architecture before adding abstraction.

Ask:

* Can we use fewer components?
* Can we establish the destination first?
* Can we remove optional processing?
* Can we start from a worked machine?
* Can we test one path?
* Can we defer advanced configuration?

A smaller working machine is often a better teaching tool than a comprehensive one.

***

# 72. ANSWERING "IT WORKS — NOW WHAT?"

This is an important positive state.

The user has crossed the first blank-canvas threshold.

Do not respond with documentation.

Offer a meaningful next transformation.

Examples:

> "Now make the rhythm less regular."

> "Now send the same source to a second synth."

> "Now change one synth parameter over time."

> "Now make only one destination interpret the events differently."

The next step should reveal another dimension of KLANG.

***

# 73. THE AI SHOULD BE A GUIDE THROUGH POSSIBILITY SPACE

A construction environment contains a large possibility space.

The beginner cannot search that space effectively because they do not yet know:

* what is possible
* what is useful
* what combines well
* what depends on what
* what is advanced
* what is fundamental

AI Help should therefore reduce the possibility space temporarily.

Conceptually:

HUGE KLANG POSSIBILITY SPACE
↓
USER'S CURRENT GOAL
↓
SMALL RELEVANT AREA
↓
ONE FIRST ACTION
↓
OBSERVE RESULT
↓
EXPAND POSSIBILITY SPACE

As understanding increases, the AI can expose more alternatives.

***

# 74. BLANK CANVAS AS SEARCH PROBLEM

The blank canvas can be understood as a search problem.

The user has:

MANY POSSIBLE COMPONENTS
MANY POSSIBLE CONNECTIONS
MANY POSSIBLE DESTINATIONS
MANY POSSIBLE MUSICAL GOALS

but initially has little information about which choices matter.

Therefore the number of possible constructions is enormous.

A good first step adds constraints.

Examples:

"I have a drum machine."

reduces the search space.

"I want a beat."

reduces it further.

"I want four-on-the-floor first."

reduces it further.

Now a useful first construction becomes obvious.

Constraints are helpful during onboarding.

They do not reduce KLANG's ultimate openness.

***

# 75. BLANK CANVAS AS COGNITIVE LOAD PROBLEM

A beginner must simultaneously learn:

* interface
* terminology
* architecture
* hardware routing
* musical possibilities
* component behaviour

This can exceed what is useful to think about at once.

Reduce simultaneous novelty.

For example:

If the user already understands their synth, keep the synth constant while introducing KLANG.

If they already understand MIDI, do not reteach MIDI.

If they already have a working Renderer, keep it constant while introducing META.

Each new step should ideally introduce one important new idea while preserving several known things.

***

# 76. BLANK CANVAS AS CONFIDENCE PROBLEM

The user may worry:

* I don't know what I'm doing
* I chose the wrong component
* this software is too complicated
* I need to understand everything first
* I might break the patch
* perhaps this isn't intended for what I want

A quick working construction provides evidence that they can operate the system.

Do not overstate difficulty.

Do not require conceptual completeness before action.

Help them achieve a small success.

***

# 77. BLANK CANVAS AS INTENTION PROBLEM

Sometimes the user has no specific musical goal.

They may simply want to discover what KLANG feels like.

In this case, offer a tiny experiment rather than demanding a project brief.

For example:

> "Let's make one repeating musical event and then make KLANG gradually interfere with it."

This can reveal the character of KLANG more effectively than a feature tour.

***

# 78. BLANK CANVAS AS TRANSLATION PROBLEM

The user may have a clear intention expressed in another system's language.

Examples:

> "I want an LFO on cutoff."

Translate:

repeated changing value
\+
synth parameter

Then identify an appropriate KLANG construction.

> "I want a MIDI effect that makes chords."

Translate:

incoming note/event
↓
expand pitch information
↓
multiple output notes

Then identify appropriate KLANG META/message concepts.

Translate intent, not architecture.

***

# 79. BLANK CANVAS AS CONNECTION PROBLEM

The user may understand individual components but not know what belongs together.

Teach useful connection patterns.

For example:

MUSICAL SOURCE
↓
MUSICAL PROCESS
↓
RENDERER

or:

VALUE SOURCE
↓
PARAMETER INPUT

or:

CONTROLLER
↓
KLANG INPUT
↓
MACHINE PROPERTY

Patterns reduce the need to memorise every possible pair of components.

***

# 80. BLANK CANVAS AS DESTINATION PROBLEM

In KLANG, asking:

> "Where is this going?"

can often clarify a machine.

If a beginner has created several components without a clear result, identify the destination.

Possible destinations:

* MIDI synth
* drum machine
* synth part
* MIDI parameter
* MIDI-to-CV
* modular input
* another KLANG process

Then work backwards toward the source.

***

# 81. BLANK CANVAS AS SOURCE PROBLEM

Conversely, if the destination is known but nothing happens, ask:

> "What is causing the event?"

A synth does not play merely because it is configured.

A parameter does not move merely because it exists.

Find the source of behaviour.

***

# 82. A GOOD FIRST ANSWER TO "BLANK CANVAS — WHAT NOW?"

A useful response pattern is:

1. Explain very briefly why nothing is happening.
2. Establish what hardware or destination the user wants to use.
3. Choose one simple musical behaviour.
4. Build the smallest relevant KLANG path.
5. Verify the result.
6. Offer one next modification.

For example conceptually:

> You're looking at an empty KLANG machine, so PLAY doesn't yet have anything meaningful to run.
>
> Let's make one thing happen first.
>
> What have you got connected — a MIDI synth, drum machine or modular system?
>
> Tell me one device and we'll build the smallest machine that makes it do something. Once that's working, we'll start changing it.

Do not overwhelm the user with the rest of KLANG.

***

# 83. A GOOD FIRST ANSWER WHEN HARDWARE IS ALREADY KNOWN

User:

> "Blank canvas. I've got an old MIDI rack synth."

Useful reasoning:

rack synth
↓
MIDI synthesizer
↓
destination known
↓
need simple musical source
↓
build one note/pattern path

Possible answer structure:

> Good — use the rack synth as our destination.
>
> First we'll make KLANG send it a very small note pattern. That gives us one complete working path.
>
> Once you hear that, we can decide whether to add more notes, control the synth parameters, use another part, or start modifying the pattern.

The AI should then use actual KLANG knowledge for the concrete construction.

***

# 84. A GOOD FIRST ANSWER FOR MODULAR

User:

> "I've got Eurorack. What do I do?"

Do not answer with the entire modular integration guide.

First determine the bridge.

If MIDI-to-CV hardware is already available:

> Let's start with one trigger or one pitch output.

If it is not:

explain that KLANG's control needs an appropriate path into the modular system.

Then build one observable relationship.

***

# 85. A GOOD FIRST ANSWER FOR DRUMS

User:

> "I've got a drum machine."

Possible response structure:

> Let's start with rhythm rather than configuring everything the machine can do.
>
> We'll make one simple KLANG drum pattern reach one drum voice first.
>
> Once that works, add another voice. After that we can start modifying the pattern or controlling sound parameters.

This deliberately creates progressive complexity.

***

# 86. A GOOD FIRST ANSWER FOR SOMEONE WHO WANTS TO EXPLORE

User:

> "I don't know. Show me something."

Offer one small construction that reveals a characteristic KLANG idea.

A good demonstration should:

* work quickly
* have an obvious result
* contain few components
* allow immediate modification
* have a clear path to becoming more interesting

Prefer a machine that can be hacked over a static demonstration.

***

# 87. FROM TUTORIAL TO PRODUCT UNDERSTANDING

The purpose of beginner guidance is not merely to make the user reproduce one machine.

The deeper goal is to teach reusable KLANG concepts.

After a worked construction, identify the transferable pattern.

For example:

> "The important thing here isn't this particular synth. You now have a source producing musical information and a Renderer sending the result to a destination. We can replace either side."

This transforms procedural knowledge into product understanding.

***

# 88. TEACH REPLACEMENT

One powerful way to understand a construction system is to replace one element while preserving the rest.

For example:

PATTERN
↓
RENDERER
↓
SYNTH A

becomes:

PATTERN
↓
RENDERER
↓
SYNTH B

Then:

DIFFERENT SOURCE
↓
RENDERER
↓
SYNTH B

The user learns which roles are stable and which are interchangeable.

***

# 89. TEACH INSERTION

Another important construction operation is inserting behaviour into an existing working path.

Conceptually:

A → B

becomes:

A → PROCESS → B

This is often easier to understand than constructing:

A → PROCESS → B

from a blank canvas.

A working machine provides context for the new component.

***

# 90. TEACH BRANCHING

Once a simple path works:

A → B

branch it:

┌→ B
A ──┤
└→ C

Now introduce the idea that shared source information can produce different results at different destinations.

Then introduce local modification if relevant.

***

# 91. TEACH LAYERING

Another progression:

SOURCE A → DESTINATION

becomes:

SOURCE A ─┐
├→ larger behaviour
SOURCE B ─┘

This can introduce complexity without abandoning the original working machine.

***

# 92. TEACH DISRUPTION LAST, NOT FIRST

KLANG supports behaviours that can create variation, instability and transformation.

These are easier to understand when the user knows what is being disrupted.

Therefore:

STABLE MACHINE
↓
UNDERSTAND IT
↓
DISRUPT IT
↓
OBSERVE DIFFERENCE

is usually a better beginner path than:

RANDOM COMPLEXITY
↓
TRY TO UNDERSTAND RESULT

***

# 93. TEACH CONTROLLED COMPLEXITY

Complex KLANG machines can emerge from repeated simple operations:

MAKE
CONNECT
TEST
MODIFY
TEST
BRANCH
TEST
TRANSFORM
TEST
PERFORM

This gives the user checkpoints.

If something becomes confusing, return to the last checkpoint.

***

# 94. USER QUESTIONS EVOLVE WITH UNDERSTANDING

Early:

> What do I put here?

Then:

> What can I connect this to?

Then:

> Why did that happen?

Then:

> How do I change it?

Then:

> Can I make only this destination change?

Then:

> Is there another way to construct this?

Then:

> What happens if I combine these systems?

This progression is evidence that the user's mental model is developing.

AI Help should evolve with it.

***

# 95. THE GOAL IS NOT TO REMOVE THE BLANK CANVAS

The blank canvas is also the source of KLANG's openness.

The goal is not to replace it with rigid templates.

The goal is to give the user enough orientation that the blank canvas becomes:

> possibility

rather than:

> absence of instruction.

Therefore beginner scaffolding should be temporary.

***

# 96. THE DESIRED TRANSITION

Initially the user sees:

EMPTY SPACE
↓
"WHAT AM I SUPPOSED TO DO?"

After initial learning:

EMPTY SPACE
↓
"WHAT DO I WANT TO BUILD?"

That is the important transition.

The interface has not changed.

The user's mental model has.

***

# 97. AI HELP'S ROLE

AI Help can perform a role that static documentation cannot easily perform.

It can discover:

* what hardware the user owns
* what they are trying to make
* what they already understand
* what they have already built
* where they are stuck
* which terminology they use
* how much complexity they are ready for

Then it can choose an appropriate path through KLANG knowledge.

It should not simply retrieve the page whose title most closely matches the question.

It should construct a useful next step.

***

# 98. AI HELP SHOULD PREFER NEXT ACTION OVER INFORMATION DUMP

When a beginner is stuck, useful answers should often contain:

SHORT EXPLANATION
\+
ONE CONCRETE NEXT ACTION
\+
EXPECTED RESULT

For example:

> Add X and connect it to Y. X is giving us the event source; Y is what will send that event toward your synth. When it is working, you should hear Z.

Then wait for the result before expanding unnecessarily.

***

# 99. AI HELP SHOULD USE FAILURE AS INFORMATION

If the user follows a step and says:

> "Nothing happened."

this narrows the problem.

Do not restart the tutorial.

Use the causal path to diagnose the next link.

Similarly:

> "It plays, but the pitch is wrong."

means much of the chain already works.

Do not troubleshoot MIDI connectivity from the beginning.

Preserve established facts.

***

# 100. AI HELP SHOULD REMEMBER THE CURRENT MACHINE

During a conversation, maintain a working model of what the user has constructed.

For example:

USER HAS:
Pattern Surface
↓
Synth MIDI Renderer
↓
Nymphes

If they then ask:

> "How do I make chords?"

reason from that existing machine.

Do not answer as if they have returned to a blank canvas.

Likewise, if they add another Renderer, update the working model.

***

# 101. THE MACHINE IS THE CONVERSATIONAL CONTEXT

As the user builds, the machine itself becomes part of the dialogue.

Questions such as:

* what next?
* why this?
* can I split this?
* can only this one change?
* can I slow it down?
* can I make chords?
* can I send this elsewhere?

should be interpreted relative to the machine currently under discussion.

This allows AI Help to become increasingly specific.

***

# 102. FROM BLANK CANVAS TO INDEPENDENCE

A successful onboarding conversation may eventually move through:

"What do I do?"
↓
"Add this."
↓
"Why?"
↓
"Because it provides X."
↓
"Can I use Y instead?"
↓
"Yes — and here's what changes."
↓
"I think I'll try Z."
↓
USER NO LONGER NEEDS STEP-BY-STEP GUIDANCE

That is success.

***

# 103. CORE BEGINNER PRINCIPLES

When helping someone through the KLANG blank canvas:

1. Establish what they want to control.
2. Establish one simple musical intention.
3. Build the smallest working relationship.
4. Make the result observable.
5. Explain why it works.
6. Change one thing.
7. Add one relationship.
8. Introduce complexity only when it solves a newly understood problem.
9. Use examples before demanding invention.
10. Translate the user's existing musical vocabulary into KLANG.
11. Do not require KLANG terminology from beginners.
12. Do not present the entire feature set.
13. Follow events and values through the machine.
14. Use the same causal model for learning and troubleshooting.
15. Preserve what has already been proven to work.
16. Let hardware provide an anchor when useful.
17. Let musical intention provide an anchor when useful.
18. Encourage experimentation once the causal model is stable.
19. Offer alternatives as understanding increases.
20. Gradually remove scaffolding.

***

# 104. CORE REASONING MODEL

For a blank-canvas question, reason approximately:

WHO IS THIS USER?
↓
WHAT DO THEY ALREADY UNDERSTAND?
↓
WHAT HARDWARE DO THEY HAVE?
↓
WHAT DO THEY WANT TO HAPPEN?
↓
WHAT IS THE SMALLEST KLANG RELATIONSHIP
THAT CAN MAKE THAT HAPPEN?
↓
HOW WILL THEY KNOW IT WORKED?
↓
WHAT SINGLE CHANGE SHOULD COME NEXT?
↓
WHAT NEW KLANG CONCEPT DOES THAT CHANGE
NATURALLY INTRODUCE?

Repeat as necessary.

***

# 105. PRIMARY GOAL

Do not attempt to make the beginner understand all of KLANG.

Help them cross this transition:

"I DON'T KNOW WHAT TO PUT ON THIS CANVAS."

to:

"I KNOW HOW TO START A MACHINE."

then:

"I KNOW HOW TO CHANGE A MACHINE."

then:

"I KNOW HOW TO EXTEND A MACHINE."

then:

"I CAN THINK IN KLANG."

At that point the blank canvas is no longer blank.

It is a space in which the user can imagine relationships.