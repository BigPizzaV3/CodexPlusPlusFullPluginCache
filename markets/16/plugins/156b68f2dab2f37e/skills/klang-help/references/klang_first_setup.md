---
updatedAt: 2026-10-07T19:51:56.000Z
agentTools:
  projectIndex: https://klang.readme.io/llms.txt
---

# KLANG_FIRST_SETUP

# KLANG FIRST SETUP

## FUNDAMENTAL SETUP BEFORE BUILDING A KLANG MACHINE

This document is part of the **KLANG Product Understanding for Machines**
knowledge system.

It describes fundamental setup concepts that a new KLANG user should
understand before attempting to build more substantial machines.

This is not merely troubleshooting information.

For many users, these concepts form the bridge between:

THEIR PHYSICAL STUDIO
↓
KLANG
↓
THE MACHINE THEY WILL BUILD

The three important setup areas are:

1. MIDI PORTS
2. KLANG MIDI DEVICES
3. MIDI → CV OUTPUTS

For modular systems, MIDI → CV setup also connects with KLANG's
representation of MODULES and the associated drag-and-drop workflow.

These concepts should be treated as fundamental orientation.

Do not assume a new user already understands them.

<br />

<br />

# NEW USER — SETUP COMES FIRST

When a user says or strongly implies that they are new to KLANG,
do not immediately begin constructing a machine on the canvas.

First determine what hardware they want to use.

If they already tell you what hardware they have, use that information
immediately.

For example:

"I'm new to KLANG. I've got an old MIDI synth. What do I do?"

This should trigger a guided First Setup journey.

Do NOT respond primarily with a list of things KLANG can do with an old
synth.

Do NOT immediately tell the user to add sequencers, Renderers, Morphers
or other machine components.

The user's first problem is:

KLANG DOES NOT YET KNOW ABOUT
THE HARDWARE THEY WANT TO USE

Guide them through establishing that relationship first.

***

# NEW MIDI USER JOURNEY

If a new user has a MIDI synthesizer, begin approximately from this
conceptual position:

> "Since you've got a MIDI synth, the first thing we'll do is get KLANG
> set up to use it. There are two things to establish before we build
> anything: the MIDI connection to the synth, and the KLANG MIDI Device
> that represents the synth."

Then walk through the stages.

Do not merely name them.

Explain why each stage exists, what the user needs to do, and what
success looks like.

The journey is:

USER HAS MIDI SYNTH
↓
HOW IS IT CONNECTED TO THE COMPUTER?
↓
MIDI PORTS
↓
KLANG MIDI DEVICE
↓
VERIFY THE SETUP
↓
RETURN TO THE CANVAS
↓
BUILD FIRST SIMPLE MACHINE
↓
MAKE SYNTH RESPOND
↓
MODIFY / EXTEND

***

# STAGE 1 — UNDERSTAND THE CONNECTION

First establish how the synthesizer is connected.

For an older MIDI synthesizer this may be:

OLD MIDI SYNTH
↓
5-PIN DIN MIDI
↓
MIDI INTERFACE
↓
MAC
↓
KLANG

Use general knowledge to understand the user's hardware.

If the exact synthesizer is known, general external knowledge may help
determine whether it uses DIN MIDI, USB MIDI, multiple MIDI ports,
multitimbral operation or other relevant hardware capabilities.

Do not invent KLANG behaviour from this external knowledge.

If enough information is already known, do not interrogate the user
unnecessarily.

***

# STAGE 2 — MIDI PORTS

Once the physical connection is understood, introduce MIDI Ports.

Explain WHY before giving instructions.

For example:

> "Your synth is physically connected to the Mac, but KLANG first needs
> access to the MIDI connection that leads to it. That's what the MIDI
> Ports setup is for."

Then use the current KLANG user guide to walk the user through the
actual MIDI Ports procedure.

Explain what they should see and how they will know this stage has
worked.

Do not simply say:

> "Configure MIDI Ports."

A new user needs the actual guided procedure.

***

# STAGE 3 — KLANG MIDI DEVICES

Once the required MIDI Port is available, introduce KLANG MIDI Devices.

Connect this explicitly to the previous step:

> "We've now established the MIDI path. Next we'll tell KLANG what
> musical device we're using through that path."

Then walk through the current documented KLANG MIDI Device procedure.

Explain the distinction:

# MIDI PORT

HOW MIDI GETS THERE

# KLANG MIDI DEVICE

THE MUSICAL DEVICE KLANG WILL USE THROUGH THAT CONNECTION

For a beginner, this distinction is more important than memorising the
names of the setup screens.

***

# STAGE 4 — VERIFY BEFORE BUILDING

Before moving into more complicated KLANG construction, establish that
the basic setup makes sense.

The user should understand:

MY SYNTH
↓
MIDI CONNECTION
↓
MIDI PORT
↓
KLANG MIDI DEVICE

If there is an appropriate simple documented way to verify this setup,
guide the user through it.

Do not add unnecessary configuration.

The purpose is to establish one known working path.

***

# STAGE 5 — NOW RETURN TO THE CANVAS

Only after the fundamental setup is established should the beginner
journey become:

> "Good — KLANG now knows how to reach your synth. Now let's make it do
> something."

At this point use the KLANG Getting Started / Blank Canvas knowledge.

Build the smallest useful machine that demonstrates the relationship.

The user is now learning machine construction rather than hardware
configuration.

***

# WALK THE USER THROUGH IT

For a first-time user, do not compress the complete setup journey into:

1. Configure MIDI.
2. Add device.
3. Add component.
4. Press Play.

The user does not yet possess the mental model that makes those
instructions meaningful.

Instead, guide them through the causal sequence.

For example:

> "Since you're using an older MIDI synth, let's get that connected to
> KLANG before worrying about the canvas.
>
> First, how is the synth connected to your Mac? If it's using the
> traditional 5-pin MIDI sockets, you'll normally have a MIDI interface
> between the Mac and the synth.
>
> Once that's physically connected, the first KLANG setup we'll look at
> is MIDI Ports..."

Continue from there using documented KLANG procedures.

At each stage:

EXPLAIN WHY
↓
GIVE THE ACTION
↓
SAY WHAT SUCCESS LOOKS LIKE
↓
CONTINUE TO NEXT STAGE

***

# DO NOT MAKE THE BEGINNER DRIVE THE DOCUMENTATION

A new user does not know that they should ask:

> "What's a MIDI Port?"

then:

> "What's a KLANG MIDI Device?"

then:

> "What do I put on the canvas?"

AI Help should know this progression.

When the user's situation makes the next prerequisite clear, introduce
it proactively.

The user should be able to say:

> "I'm new to KLANG. I've got an old MIDI synth."

and be guided through the appropriate KLANG setup journey without
already knowing KLANG terminology.

***

# ADAPT THE JOURNEY TO THE HARDWARE

The same principle applies to different studios.

For a new user with a MIDI synth:

MIDI PORTS
↓
KLANG MIDI DEVICE
↓
FIRST MACHINE

For a new user with modular hardware:

MIDI → CV SETUP
↓
CV OUTPUTS / MODULE RELATIONSHIPS
↓
FIRST MACHINE

For a user with both:

ESTABLISH THE SIMPLEST REQUIRED PATH FIRST
↓
GET ONE THING WORKING
↓
ADD THE SECOND HARDWARE PATH

Do not force every new user through every KLANG setup area.

The user's actual studio determines the route.

***

# 1. BEFORE THE BLANK CANVAS

A new user may reasonably think:

> "I've opened KLANG. What do I put on the canvas?"

But there is an earlier question:

> "How does KLANG know what equipment I have?"

Before a machine can meaningfully control external hardware, KLANG needs
an appropriate relationship with the user's physical studio.

Conceptually:

PHYSICAL STUDIO
↓
KLANG SETUP
↓
KLANG MACHINE
↓
PHYSICAL STUDIO

The canvas is where the user constructs behaviour.

The setup areas establish important relationships between that behaviour
and the external world.

***

# 2. THE THREE FUNDAMENTAL SETUP CONCEPTS

Do not collapse the three setup areas into one generic concept called
"MIDI Setup".

They have different roles.

A useful first approximation is:

MIDI PORTS
"What MIDI connections are available?"

↓

KLANG MIDI DEVICES
"What musical devices am I using through those connections?"

↓

MIDI → CV OUTPUTS
"How can KLANG reach my CV/modular system?"

These answer different questions.

When helping a beginner, use the actual KLANG terminology established by
the current KLANG documentation.

Do not invent generic panels or settings merely because similar music
software uses them.

***

# 3. MIDI PORTS

## THE BEGINNER QUESTION

A new user may ask:

> "How does KLANG see my MIDI interface?"

or:

> "How do I get MIDI out of KLANG?"

or simply:

> "Why isn't my synth showing up?"

The underlying concept is the relationship between KLANG and the MIDI
connections made available by the computer.

Think:

COMPUTER
↓
MIDI CONNECTION / ENDPOINT
↓
KLANG MIDI PORTS
↓
AVAILABLE TO KLANG

MIDI Ports concern the communication paths available to KLANG.

They are not the same thing as a musical instrument.

***

# 4. PORT IS NOT DEVICE

This distinction is fundamental.

A MIDI port answers something like:

> "Where can MIDI data travel?"

A KLANG MIDI Device answers something more like:

> "What musical device am I intending to communicate with through that
> connection?"

Do not treat these as interchangeable concepts.

Conceptually:

# MIDI PORT

COMMUNICATION PATH

while:

# KLANG MIDI DEVICE

MUSICAL / HARDWARE DESTINATION CONFIGURATION

A physical MIDI interface may expose one or more MIDI ports.

A synthesizer may be reached through one of those ports.

These are related, but they are not the same object.

***

# 5. WHY MIDI PORTS COME FIRST

Before KLANG can meaningfully send information toward an external MIDI
instrument, there must be an appropriate MIDI path.

Therefore a beginner setup sequence commonly begins with MIDI Ports.

The user should establish:

IS THE MIDI CONNECTION AVAILABLE?
↓
CAN KLANG USE THE REQUIRED PORT?
↓
NOW DEFINE / USE THE MUSICAL DEVICE

Do not immediately teach Patterns, Renderers, Morphers or META if the
basic external MIDI path required by the user's intended machine has not
yet been established.

***

# 6. EXAMPLE — MIDI INTERFACE AND SYNTH

Suppose the user's studio contains:

MAC
↓
USB MIDI INTERFACE
↓
MIDI DIN
↓
YAMAHA MU128

The MU128 is the synthesizer.

The MIDI interface provides the physical MIDI communication path.

KLANG needs to work with the appropriate MIDI port exposed by that
interface.

The user can then establish an appropriate KLANG MIDI Device representing
how KLANG will address the synthesizer.

Do not confuse:

"KLANG can see the MIDI interface"

with:

"KLANG is correctly configured to use the MU128."

The first is necessary infrastructure.

The second adds musical/device meaning.

***

# 7. KLANG MIDI DEVICES

## THE BEGINNER QUESTION

Once MIDI communication is available, the next conceptual question is:

> "What is actually connected to that MIDI path?"

This is where KLANG MIDI Devices become important.

A KLANG MIDI Device gives KLANG a configured representation of an
external MIDI destination.

Examples of external destinations might include:

* synthesizers
* rack synthesizers
* sound modules
* drum machines
* desktop synthesizers
* other MIDI-controllable musical hardware

Use external world knowledge to understand what the user's hardware is.

Use KLANG product knowledge to explain how KLANG represents and uses it.

***

# 8. EXTERNAL HARDWARE KNOWLEDGE + KLANG DEVICE KNOWLEDGE

Suppose the user says:

> "I've got an MU128."

General knowledge can establish:

Yamaha MU128
↓
hardware MIDI tone generator
↓
multitimbral MIDI synthesizer

KLANG knowledge can then establish how an external MIDI synthesizer fits
into KLANG.

Conceptually:

REAL MU128
↓
MIDI CONNECTION
↓
KLANG MIDI DEVICE
↓
KLANG MACHINE

Do not require the KLANG documentation to contain a dedicated MU128 page
before making the semantic connection.

However, do not invent KLANG-specific configuration behaviour that is
not supported by the KLANG knowledge corpus.

***

# 9. A KLANG MIDI DEVICE IS NOT THE PHYSICAL SYNTH

Keep the layers distinct:

PHYSICAL SYNTH
≠
MIDI PORT
≠
KLANG MIDI DEVICE
≠
KLANG COMPONENT USING THAT DEVICE

These objects may participate in one working relationship, but they have
different roles.

This distinction becomes increasingly important in larger studios.

***

# 10. WHY THIS MATTERS LATER

A beginner may initially wonder why KLANG needs a device concept at all.

The answer becomes clearer as machines grow.

KLANG needs to know not merely that MIDI can leave the computer, but
which configured musical destination is involved.

Later KLANG concepts may depend upon this device relationship.

Therefore do not teach KLANG MIDI Devices as arbitrary administrative
setup.

Explain their role in connecting the abstract KLANG machine to the
user's actual musical equipment.

***

# 11. MIDI SYNTH DEVICE MODELS

Some external synthesizers may have richer KLANG support through
synth/device models.

Where documented, these can allow KLANG to understand more about the
structure and controllable properties of the instrument.

This may include concepts such as:

* parts
* voices
* MIDI CC properties
* device-specific properties
* semantic control
* extended MIDI behaviour
* SysEx-based properties

Do not assume every MIDI device has a dedicated KLANG synth model.

Do not assume a generic MIDI Device and a supported synthesizer model are
the same thing.

If a particular synthesizer is not represented by a dedicated model,
use the capabilities that KLANG actually documents for that situation.

***

# 12. MIDI CHANNELS, PARTS AND DEVICES ARE DIFFERENT CONCEPTS

A beginner using a multitimbral instrument can easily confuse:

* physical instrument
* MIDI connection
* KLANG MIDI Device
* MIDI channel
* synthesizer part
* KLANG Renderer
* KLANG synth/device model

Keep these concepts separate.

For example, a single physical multitimbral synthesizer may contain many
musical parts.

That does not make each part a separate physical MIDI device.

Likewise, a MIDI channel is not itself a hardware device.

Explain these distinctions when they become relevant rather than
front-loading all of them.

***

# 13. FIRST MIDI SETUP GOAL

For a new MIDI user, the initial goal should be modest:

KLANG CAN ACCESS MIDI CONNECTION
↓
KLANG HAS APPROPRIATE DEVICE CONFIGURATION
↓
SIMPLE KLANG MACHINE
↓
EXTERNAL SYNTH RESPONDS

Do not configure an entire studio before demonstrating one working
relationship unless the user specifically wants to do so.

***

# 14. MIDI → CV OUTPUTS

## THE BEGINNER QUESTION

A modular user has a different problem.

Their equipment may not be controlled primarily as a conventional MIDI
synthesizer.

They may need:

* pitch CV
* trigger
* gate
* modulation CV
* envelopes
* other voltage control

KLANG therefore needs a route from its software/MIDI world into control
voltage.

Conceptually:

KLANG
↓
MIDI
↓
MIDI → CV
↓
CONTROL VOLTAGE
↓
MODULAR HARDWARE

MIDI → CV Outputs describe this important boundary.

***

# 15. MIDI → CV IS A BRIDGE

Do not explain MIDI → CV merely as another MIDI destination.

Its important conceptual role is:

> translating KLANG's control into physical voltage relationships that
> can participate in a modular patch.

For example:

KLANG PITCH
↓
MIDI → CV OUTPUT
↓
1V/OCT
↓
OSCILLATOR

or:

KLANG TRIGGER
↓
MIDI → CV OUTPUT
↓
TRIGGER VOLTAGE
↓
MODULAR PERCUSSION

or:

KLANG CHANGING VALUE
↓
MIDI → CV OUTPUT
↓
CONTROL VOLTAGE
↓
MODULATION DESTINATION

The exact supported setup and behaviour must come from current KLANG
documentation.

***

# 16. EXPERT SLEEPERS FH-2

KLANG workflows may use the Expert Sleepers FH-2 as a MIDI-to-CV bridge.

Treat the FH-2 as external hardware.

General knowledge may help explain what an FH-2 is.

KLANG documentation establishes how KLANG uses/configures it.

Do not assume generic FH-2 configuration procedures are identical to
KLANG's workflow.

The important beginner concept is:

KLANG DOES NOT DIRECTLY CREATE AN ANALOG PATCH CABLE

Instead:

KLANG BEHAVIOUR
↓
MIDI / CONFIGURED OUTPUT
↓
FH-2 OR APPROPRIATE MIDI→CV HARDWARE
↓
PHYSICAL CV OUTPUT
↓
PATCH CABLE
↓
MODULE

***

# 17. MIDI → CV OUTPUTS AND MODULES

This relationship is especially important for understanding KLANG.

The MIDI → CV configuration establishes available physical CV outputs.

KLANG's module representation gives those outputs meaning in relation to
the user's modular system.

The beginner should eventually understand both sides:

AVAILABLE PHYSICAL CV OUTPUT
\+
WHAT THAT OUTPUT IS CONNECTED TO
↓
MEANINGFUL MODULAR DESTINATION

This is more useful than thinking only in terms of anonymous numbered
outputs.

***

# 18. MODULES ARE PART OF THE PHYSICAL-STUDIO MODEL

A modular synthesizer is not simply one MIDI instrument.

It may consist of many individual modules with different inputs and
functions.

For example:

OSCILLATOR
FILTER
ENVELOPE
VCA
DRUM MODULE
FUNCTION GENERATOR
MODULATION PROCESSOR
SEMI-MODULAR VOICE

KLANG can therefore benefit from understanding the relationship between
configured CV outputs and the physical modular system they control.

Do not assume every module behaves the same way.

***

# 19. MODULE DRAG AND DROP

Module drag-and-drop is important because it helps bridge:

ABSTRACT CV OUTPUT

and:

PHYSICAL THING IN THE USER'S RACK

A beginner should not experience this merely as an unexplained UI
gesture.

Explain the purpose before the mechanics.

Conceptually:

AVAILABLE MODULE
↓
DRAG INTO SETUP
↓
REPRESENT PART OF PHYSICAL MODULAR SYSTEM
↓
ASSOCIATE / WORK WITH CONFIGURED CV OUTPUTS
↓
KLANG CAN REASON ABOUT THAT MODULAR DESTINATION

Use the current user guide for the exact drag-and-drop procedure and
configuration details.

Do not invent steps.

***

# 20. WHY MODULE DRAG AND DROP MATTERS

The important idea is not:

> "KLANG has a draggable picture of a module."

The important idea is:

> "KLANG is being told something about the physical modular system that
> exists outside the computer."

This turns configuration into a model of the studio.

Conceptually:

SOFTWARE REPRESENTATION
↕
PHYSICAL MODULAR HARDWARE

That relationship later makes constructing meaningful KLANG → CV
behaviour easier to understand.

***

# 21. THE FUNDAMENTAL STUDIO MODEL

The three setup systems together allow a useful high-level mental model:

PHYSICAL STUDIO

MIDI SYNTHS                  MODULAR
│                           │
│                           │
MIDI PORTS                  CV OUTPUTS
│                           │
KLANG MIDI DEVICES               MODULES
\                           /
\                         /
└──────── KLANG ────────┘
│
│
KLANG MACHINE

This is conceptual.

It is not intended to specify implementation details.

***

# 22. SETUP IS NOT THE MACHINE

This distinction is fundamental.

The setup systems describe important relationships with external
equipment.

The canvas is where the user constructs musical/control behaviour.

Therefore:

SETUP
≠
MACHINE

Instead:

SETUP
↓
MAKES EXTERNAL DESTINATIONS AVAILABLE / MEANINGFUL
↓
MACHINE USES THOSE RELATIONSHIPS

A user can correctly configure hardware and still have an empty canvas.

Pressing PLAY at that point may still do nothing interesting.

The next stage is machine construction.

***

# 23. SETUP BEFORE BLANK CANVAS

For a completely new user with external hardware, a useful onboarding
sequence is:

WHAT HARDWARE DO YOU HAVE?
↓
MIDI OR CV?
↓
ESTABLISH APPROPRIATE KLANG SETUP
↓
VERIFY BASIC CONNECTION
↓
RETURN TO CANVAS
↓
BUILD MINIMUM VIABLE MACHINE
↓
HEAR / OBSERVE RESULT
↓
MODIFY MACHINE

This connects KLANG FIRST SETUP with the KLANG GETTING STARTED / BLANK
CANVAS knowledge.

***

# 24. DO NOT CONFIGURE THINGS THE USER DOES NOT NEED

A user with only MIDI synthesizers may not need MIDI → CV setup.

A user working only with a modular system may not need to configure a
collection of MIDI synthesizers.

A user with both may need both.

Determine the studio first.

Then introduce the relevant setup.

Do not turn onboarding into a tour of every setup screen.

***

# 25. ASK ABOUT THE USER'S HARDWARE

For a genuinely new user, useful questions include:

> "What are you connecting to KLANG?"

If necessary:

> "Is it a MIDI synth/drum machine, a modular system, or both?"

Then guide accordingly.

Examples:

MIDI SYNTH
↓
MIDI PORTS
↓
KLANG MIDI DEVICE

MODULAR
↓
MIDI → CV
↓
CV OUTPUTS
↓
MODULE RELATIONSHIP

BOTH
↓
CONFIGURE EACH RELEVANT PATH

***

# 26. DO NOT ASSUME "MIDI SYNTH" MEANS MODERN USB MIDI

The user's equipment may include:

* USB MIDI instruments
* DIN MIDI instruments
* older rack modules
* MIDI interfaces
* multitimbral hardware
* drum machines
* synthesizers with device-specific MIDI behaviour

Use general hardware knowledge where useful.

For example, an older rack module may require a MIDI interface and DIN
connection rather than appearing as a direct USB MIDI device.

This is external hardware knowledge.

Combine it with KLANG setup knowledge.

***

# 27. DO NOT ASSUME "MODULAR" MEANS MIDI

A modular system may receive control through CV rather than MIDI.

If the user says:

> "I've got a Eurorack system."

do not immediately treat it as a MIDI synthesizer.

Determine the control route.

If they have appropriate MIDI-to-CV hardware, explain the KLANG → MIDI →
CV relationship.

***

# 28. EXPLAIN THE REASON FOR EACH SETUP STEP

Avoid:

> "Go to MIDI Ports and do X."

Prefer:

> "First we need to make the physical MIDI connection available to
> KLANG. That's what the MIDI Ports setup is establishing."

Avoid:

> "Now create a KLANG MIDI Device."

Prefer:

> "The port gives us a communication path. Now KLANG needs to know what
> musical device we're using through that path."

Avoid:

> "Drag the module here."

Prefer:

> "The CV output exists, but now we're giving that output meaning by
> relating it to the module in your physical rack."

The exact UI operation can then follow.

***

# 29. TEACH THE DIFFERENCE BETWEEN LAYERS

A useful beginner model is:

## LAYER 1 — PHYSICAL CONNECTION

What is physically connected to the Mac?

## LAYER 2 — KLANG SETUP

How does KLANG represent/access those connections and devices?

## LAYER 3 — MACHINE

What behaviour has the user constructed?

## LAYER 4 — MUSICAL RESULT

What happens in the external hardware?

Conceptually:

PHYSICAL
↓
CONFIGURATION
↓
CONSTRUCTION
↓
BEHAVIOUR

When something does not work, identify which layer is failing.

***

# 30. FIRST-TIME SETUP QUESTIONS

A beginner may ask:

* Where is my synth?
* Why can't KLANG see my synth?
* What's a MIDI Port?
* What's a KLANG MIDI Device?
* What's the difference between a port and a device?
* Do I need to add every synth?
* How do I add my MIDI interface?
* My synth only has DIN MIDI. Can I use it?
* What if my synth isn't in KLANG's supported synth list?
* How do I connect my modular?
* What is MIDI-to-CV doing?
* What is an FH-2 doing?
* What do the CV outputs represent?
* Why am I dragging modules into KLANG?
* Does KLANG know what is physically patched?
* Do I need to configure this every time?
* I've configured everything. Why does PLAY still do nothing?

Answer the underlying conceptual question as well as the UI question.

***

# 31. "I SET IT UP BUT PLAY DOES NOTHING"

This is an important transition.

Correct setup does not itself generate musical behaviour.

Explain:

> "Good — KLANG now knows about the route to your hardware. We haven't
> built the machine that uses that route yet."

Then move into Blank Canvas onboarding.

Conceptually:

HARDWARE CONFIGURED
↓
CANVAS STILL EMPTY
↓
ADD SOURCE
↓
CONNECT / PROCESS
↓
RENDER TO DESTINATION
↓
PRESS PLAY / INTERACT
↓
HARDWARE RESPONDS

This is not a setup failure.

It is the transition from configuration to construction.

***

# 32. "MY DEVICE ISN'T IN THE SYNTH LIST"

Do not automatically conclude that the hardware cannot be used.

Distinguish:

CAN KLANG SEND APPROPRIATE MIDI TO IT?

from:

DOES KLANG HAVE A DEDICATED MODEL FOR IT?

A dedicated device model may provide richer device-specific or semantic
behaviour.

Its absence does not necessarily imply that ordinary MIDI communication
is impossible.

Use current KLANG documentation to establish the exact supported
workflow.

Do not invent device support.

***

# 33. MULTIPLE SYNTHS

If a user has several MIDI instruments, establish the simple case first.

For example:

MIDI PORT
↓
DEVICE A
↓
SIMPLE MACHINE

Verify.

Then add:

DEVICE B

This makes routing problems easier to identify.

Do not require the beginner to configure their entire studio before
getting one instrument working.

***

# 34. MULTIPLE CV OUTPUTS

Likewise, a MIDI-to-CV system may expose many outputs.

Do not begin by teaching all possible assignments.

Start with one understandable physical relationship.

For example:

OUTPUT
↓
TRIGGER INPUT
↓
MODULE RESPONDS

Then another:

OUTPUT
↓
PITCH INPUT
↓
OSCILLATOR RESPONDS

The user learns what an output represents through physical consequence.

***

# 35. SETUP AS A MAP OF THE STUDIO

A useful deeper mental model is:

> KLANG setup creates a software-side understanding of important routes
> into the user's physical studio.

This may include:

MIDI CONNECTIONS
MUSICAL DEVICES
MIDI → CV OUTPUTS
MODULAR MODULE RELATIONSHIPS

The machine constructed on the canvas can then operate through those
routes.

This is why setup is fundamental rather than administrative.

***

# 36. SETUP SHOULD BE TAUGHT ONCE, THEN BECOME BACKGROUND

Once a user has successfully configured their studio, do not repeatedly
send them back through first-time setup unless there is evidence that the
configuration is relevant to the problem.

For example:

User has already successfully played their synth from KLANG.

Later asks:

> "How do I add chords?"

Do not begin again with MIDI Ports.

The working MIDI connection is already established.

Continue from the current machine.

***

# 37. PRESERVE ESTABLISHED FACTS

If the user reports:

> "The synth is receiving notes."

then several facts are already established:

* some MIDI path works
* some destination configuration works
* some KLANG output path works
* the hardware can receive KLANG-generated MIDI

Do not troubleshoot those layers again without evidence.

Move forward.

***

# 38. TROUBLESHOOT SETUP FROM OUTSIDE IN

If a new user's hardware does not respond, reason through layers.

For MIDI:

IS HARDWARE PHYSICALLY CONNECTED?
↓
IS THE EXPECTED MIDI PORT AVAILABLE?
↓
IS KLANG USING THE CORRECT PORT?
↓
IS THE KLANG MIDI DEVICE CONFIGURED APPROPRIATELY?
↓
IS THE MACHINE SENDING SOMETHING?
↓
IS THE EXTERNAL DEVICE EXPECTING IT?

For CV:

IS MIDI→CV HARDWARE CONNECTED?
↓
IS THE REQUIRED OUTPUT CONFIGURED?
↓
IS THE KLANG RELATIONSHIP CORRECT?
↓
IS THE PHYSICAL CV OUTPUT PATCHED?
↓
IS THE DESTINATION MODULE INPUT APPROPRIATE?
↓
IS KLANG GENERATING THE EXPECTED BEHAVIOUR?

Use current KLANG troubleshooting knowledge for exact procedures.

***

# 39. DO NOT INVENT GENERIC "MIDI SETUP PANELS"

Use actual KLANG terminology.

If KLANG documentation distinguishes:

MIDI PORTS

KLANG MIDI DEVICES

MIDI → CV OUTPUTS

preserve those distinctions.

Do not collapse them into invented terminology such as:

"the MIDI Setup Panels"

unless that is itself an official KLANG term documented elsewhere.

Similarly, do not invent:

* central MIDI patch bays
* automatic hardware scanning behaviour
* enable/disable requirements
* routing rules
* timing behaviour
* persistence behaviour

simply because other music software behaves that way.

KLANG-specific claims must come from KLANG knowledge.

***

# 40. EXTERNAL HARDWARE FACTS ARE ALLOWED

It is appropriate to use reliable general knowledge about the user's
external equipment.

For example:

MU128 is multitimbral
FH-2 is MIDI-to-CV hardware
a particular synth supports DIN MIDI
a particular device uses certain MIDI CCs

This can help construct a useful KLANG answer.

But maintain the boundary:

EXTERNAL DEVICE FACT
\+
DOCUMENTED KLANG CAPABILITY
↓
REASONED USE WITH KLANG

Do not turn an external hardware fact into an undocumented KLANG feature.

***

# 41. FIRST SETUP AND THE ONTOLOGY

Use the KLANG ONTOLOGY to identify unfamiliar hardware.

For example:

"old Yamaha rack thing"
↓
rack sound module
↓
MIDI synthesizer
↓
MIDI PORT + KLANG MIDI DEVICE path

or:

"Eurorack drum module"
↓
CV-controlled modular hardware
↓
MIDI→CV path
↓
MODULE / CV relationship

The user does not need to know the KLANG category first.

Translate their hardware into KLANG concepts.

***

# 42. FIRST SETUP AND BLANK CANVAS

These two knowledge areas are complementary.

KLANG FIRST SETUP asks:

> "How does KLANG connect conceptually and technically with my studio?"

KLANG GETTING STARTED / BLANK CANVAS asks:

> "Now that the environment is ready, what should I build?"

The transition is:

STUDIO
↓
FIRST SETUP
↓
BLANK CANVAS
↓
MINIMUM VIABLE MACHINE
↓
FIRST RESULT
↓
HACK / EXTEND
↓
PERFORMANCE

***

# 43. RECOMMENDED BEGINNER CONVERSATION

For an apparently new user:

> "What are you connecting to KLANG?"

Suppose:

> "An old Yamaha MU128."

Reason:

MU128
↓
MIDI SYNTH
↓
MIDI PATH REQUIRED

Then guide:

MIDI PORT
↓
KLANG MIDI DEVICE
↓
SIMPLE MACHINE
↓
MU128 RESPONDS

Once successful:

> "Good. The setup part is working. Now let's build something more
> interesting with it."

Do not continue treating the user as being in setup mode.

***

# 44. RECOMMENDED MODULAR BEGINNER CONVERSATION

User:

> "I've got an FH-2 going into my Eurorack."

Reason:

MIDI→CV ALREADY IDENTIFIED
↓
UNDERSTAND AVAILABLE CV OUTPUTS
↓
RELATE OUTPUT TO MODULE
↓
TEST ONE PHYSICAL CONTROL PATH

Begin with one result.

For example:

> "Let's get one trigger from KLANG to one module first."

Once that works, introduce more CV relationships.

***

# 45. SUCCESS CRITERIA

First Setup is successful when the user understands enough to say:

## MIDI

> "KLANG has access to the MIDI connection and knows which external
> musical device I'm trying to use."

or:

## MODULAR

> "KLANG has a configured route through MIDI-to-CV into a known part of
> my modular system."

At that point, stop expanding setup unnecessarily.

Move to machine construction.

***

# 46. THE FUNDAMENTAL DISTINCTION

Teach this distinction early:

SETUP ANSWERS:

"WHAT IS OUT THERE AND HOW CAN KLANG REACH IT?"

↓

THE CANVAS ANSWERS:

"WHAT SHOULD KLANG DO WITH IT?"

This is one of the most useful mental models for a new KLANG user.

***

# 47. PRIMARY AI BEHAVIOUR

When helping a new KLANG user:

1. Determine what external equipment they want to use.
2. Classify it using general knowledge and the KLANG ONTOLOGY.
3. Identify whether MIDI, MIDI→CV, or another documented path is relevant.
4. Introduce only the setup areas required for that path.
5. Explain what each setup concept means before giving mechanical steps.
6. Use actual KLANG terminology.
7. Do not invent generic setup behaviour.
8. Verify one working external relationship.
9. Recognise when setup is complete.
10. Move the user onto the canvas.
11. Build the smallest useful machine.
12. Do not return to setup unless evidence suggests a setup problem.

***

# 48. CORE MENTAL MODEL

For MIDI hardware:

PHYSICAL MIDI CONNECTION
↓
MIDI PORT
↓
KLANG MIDI DEVICE
↓
KLANG MACHINE
↓
MUSICAL INFORMATION
↓
PHYSICAL INSTRUMENT

For modular hardware:

KLANG MACHINE
↓
MIDI / CONTROL
↓
MIDI → CV OUTPUT
↓
PHYSICAL VOLTAGE
↓
PHYSICAL MODULE INPUT
↓
MODULAR BEHAVIOUR

The setup systems make these relationships understandable and usable.

***

# 49. WHAT COMES NEXT

Once First Setup is established, continue with the KLANG Getting Started
knowledge.

The next question becomes:

> "My hardware is ready. What do I put on the blank canvas?"

At that point:

DO NOT TEACH MORE SETUP

unless it is needed.

Instead:

BUILD SOMETHING SIMPLE
↓
MAKE SOMETHING HAPPEN
↓
UNDERSTAND WHY
↓
CHANGE SOMETHING
↓
ADD SOMETHING
↓
HACK THE MACHINE
↓
PERFORM THE RESULT

***

# 50. PURPOSE OF THIS DOCUMENT

The purpose of KLANG FIRST SETUP is not to make the AI recite setup
screens.

It is to ensure that the AI understands the fundamental relationship
between:

THE USER'S PHYSICAL STUDIO

KLANG'S HARDWARE / OUTPUT CONFIGURATION

THE MACHINE CONSTRUCTED ON THE CANVAS

A beginner should leave First Setup understanding:

> "KLANG now knows how to reach the things I want to work with."

They can then approach the blank canvas with a much simpler question:

> "What do I want KLANG to make those things do?"