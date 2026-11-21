---
updatedAt: 2026-10-07T19:13:19.000Z
agentTools:
  projectIndex: https://klang.readme.io/llms.txt
---

# ONTOLOGY

# KLANG ONTOLOGY

This document helps an AI connect concepts from the wider world of
electronic music, MIDI, synthesis, modular systems and music software
with concepts inside KLANG.

It is part of the KLANG Product Understanding for Machines knowledge
system.

This is NOT a list of everything KLANG supports.

It is a semantic bridge.

The purpose is to help recognise what a user is talking about even when
they do not use KLANG terminology.

***

# CORE PRINCIPLE

Users will normally describe their equipment, musical intentions and
problems using ordinary music-technology language.

They should not be expected to know KLANG terminology.

Reason approximately as follows:

USER LANGUAGE / EXTERNAL OBJECT
↓
IDENTIFY THE CONCEPT
↓
KLANG ONTOLOGY
↓
RELEVANT KLANG CONCEPTS
↓
KLANG KNOWLEDGE
↓
ANSWER

Do not require an exact word or device-name match in the KLANG knowledge
sources.

Use existing general knowledge to identify external equipment and concepts.

Then use this ontology and the wider KLANG knowledge corpus to determine
how those concepts relate to KLANG.

***

# IMPORTANT LIMITATION

A semantic relationship does not imply identical behaviour.

For example:

Ableton MIDI Effect
↓
MIDI message transformation
↓
potentially related to KLANG message modification

does NOT mean:

KLANG has Ableton MIDI Effects

Similarly:

modular LFO
↓
changing control value
↓
potentially related to a KLANG Morpher

does NOT mean:

a KLANG Morpher is simply an LFO

Use external concepts to understand the user's meaning.

Use KLANG knowledge to determine actual KLANG behaviour.

***

# EXTERNAL MUSICAL HARDWARE

## MIDI SYNTHESIZER

Possible user terms include:

* synthesizer
* synth
* hardware synth
* MIDI synth
* desktop synth
* keyboard synth
* rack synth
* rack module
* sound module
* tone generator
* ROMpler
* multitimbral synth
* poly synth
* polysynth
* mono synth
* monosynth
* digital synth
* analogue synth with MIDI
* analog synth with MIDI
* virtual analogue synth
* wavetable synth
* FM synth
* retro synth
* vintage MIDI synth

These may all describe an:

EXTERNAL MIDI SYNTHESIZER

Possible relationships include:

MIDI notes
MIDI channels
velocity
note duration
pitch
program changes
bank selection
MIDI CC
pitch bend
channel pressure
SysEx
multiple parts
multiple voices

Relevant KLANG concepts may include:

MIDI Devices / Ports
MIDI Synth concepts
MIDI Synth components
MIDI Renderers
Synth MIDI Renderers
voice / part concepts
semantic MIDI
extended MIDI control
CC control
SysEx control
META
message modification
Surfaces
Patterns
Pitch
Duration
Volume

The particular synthesizer does NOT need to be named in the KLANG
knowledge corpus for these relationships to be considered.

***

# RETRO MIDI HARDWARE

Terms such as:

* old synth
* old MIDI synth
* 80s synth
* 90s synth
* rack synth
* sound module
* tone generator
* ROMpler
* General MIDI module
* XG module
* GS module
* workstation module
* multitimbral module

may describe hardware particularly suited to KLANG's MIDI-oriented
capabilities.

Examples from the wider world could include devices such as:

Yamaha MU series
Roland Sound Canvas family
Roland JV family
Korg rack synthesizers
E-mu sound modules
older multitimbral MIDI synthesizers

These examples identify a CLASS of equipment.

They do not imply that KLANG contains a dedicated model for every device.

A device such as a Yamaha MU128 can therefore be reasoned about as:

Yamaha MU128
↓
MIDI sound module
↓
multitimbral MIDI synthesizer
↓
external MIDI synthesizer
↓
KLANG MIDI Synth / MIDI Renderer / MIDI control concepts

Do not require the term "MU128" to appear in KLANG documentation before
making this conceptual connection.

***

# MULTITIMBRAL INSTRUMENTS

Terms include:

* multitimbral
* multi-timbral
* MIDI parts
* instrument parts
* MIDI channels
* 16-part synth
* sound module
* multiple instruments from one synth

General concept:

ONE PHYSICAL DEVICE
↓
MULTIPLE PARTS
↓
independently addressable musical voices/instruments

This can be relevant to KLANG machines where multiple processes,
Renderers or musical structures address different parts of an external
instrument.

Do not assume the exact routing architecture.

Use the KLANG knowledge corpus to determine how KLANG represents devices,
parts, voices and endpoints.

***

# DRUM MACHINES AND PERCUSSION

Possible user terms:

* drum machine
* drum synth
* percussion synth
* rhythm machine
* MIDI drums
* electronic drums
* groovebox
* drum module
* percussion module

Possible conceptual relationships:

note number → drum / percussion voice
velocity → hit strength
MIDI CC → sound parameter
MIDI channel → instrument / part
trigger → percussion event
pattern → rhythm

Relevant KLANG concepts may include:

Drum Pattern Surface
Multi-track Pattern Surface
Pattern Sequencer
MIDI Drum Player
Trigger
META Trigger
MIDI Renderers
MIDI note processing
CC control
semantic MIDI
extended MIDI

Do not assume all drum machines expose the same MIDI capabilities.

Use general knowledge of the external device where available.

***

# MODULAR SYNTHESIS

Possible user terms:

* modular
* Eurorack
* modular synth
* module
* oscillator
* VCO
* filter
* VCF
* envelope
* VCA
* function generator
* sequencer
* clock
* trigger
* gate
* CV
* modulation
* patch cable
* patch
* semi-modular
* analog modular
* analogue modular

These terms describe an ecosystem in which musical behaviour is often
constructed through signals and relationships rather than a conventional
linear musical arrangement.

This makes many modular concepts semantically relevant to KLANG.

However:

KLANG IS NOT A MODULAR SYNTHESIZER

Do not infer KLANG behaviour merely because KLANG and modular synthesis
share concepts such as patching, modulation, triggers or signals.

***

# SEMI-MODULAR SYNTHESIZERS

Possible examples include:

Moog DFAM
Moog Mother family
desktop semi-modular synthesizers
patchable analogue synthesizers

General mapping:

SEMI-MODULAR INSTRUMENT
↓
MIDI and/or CV controllable hardware
↓
potential KLANG destination

Relevant KLANG concepts may include:

MIDI
MIDI → CV
FH-2
triggers
pulses
pitch
1V/OCT
modulation
Morphers
Patterns

Determine the actual available connection method from the particular
hardware rather than assuming MIDI or CV support.

***

# CONTROL VOLTAGE

Possible user terms:

* CV
* control voltage
* modulation voltage
* voltage control
* CV input
* CV output
* Eurorack CV

Conceptually:

SOFTWARE VALUE / MUSICAL EVENT
↓
MIDI / DATA
↓
MIDI → CV DEVICE
↓
CONTROL VOLTAGE
↓
MODULAR HARDWARE

KLANG can participate in this relationship using its documented MIDI/CV
architecture.

Relevant concepts may include:

Expert Sleepers FH-2
MIDI → CV
pitch CV
1V/OCT
triggers
gates
modulation values
envelopes

Use the KLANG knowledge corpus for actual implementation details.

***

# 1V/OCT

Possible user terms:

* one volt per octave
* 1 volt/octave
* 1V/OCT
* pitch CV
* oscillator pitch
* CV pitch

General concept:

MUSICAL PITCH
↓
CONTROL VOLTAGE
↓
OSCILLATOR PITCH

Relevant KLANG concepts include documented 1V/OCT and MIDI-to-CV
facilities.

Micro-pitch and fine pitch control may also be relevant.

Do not assume every CV instrument uses 1V/OCT.

***

# GATE

Possible meanings include:

* note gate
* modular gate
* gate high
* gate low
* held trigger
* note on/off state

A gate normally represents a state with meaningful duration.

Conceptually:

ON ───────────────── OFF

This differs from a short trigger or impulse.

Relevant KLANG concepts may include:

note duration
Key On / Key Off
ADSR
MIDI → CV
event duration

Use KLANG terminology when describing actual KLANG behaviour.

***

# TRIGGER

Possible user terms:

* trigger
* trig
* hit
* fire
* pulse
* event
* clock pulse

A trigger usually represents a discrete event.

Conceptually:

│
───────┼───────
│ EVENT

Relevant KLANG concepts include:

Trigger
Simple Trigger
META Trigger
Patterns
Drum Patterns
event processing
trigger connectors

Do not automatically treat trigger, gate and clock as interchangeable.

***

# PULSE

A pulse is an event with some temporal extent or repeated temporal
behaviour depending on context.

Possible relevant KLANG concepts include:

Simple Pulse
Pulse Drifter
timing
trigger generation
rhythmic processes

Use the documented KLANG definition where a specific component is involved.

***

# CLOCK

Possible user terms:

* clock
* MIDI clock
* modular clock
* tempo clock
* sync
* pulse clock
* PPQ
* ticks

General concepts include:

tempo
timing
synchronization
rhythmic subdivision
musical position

Relevant KLANG concepts include:

BPM
PPQ
timing
Patterns
Pulses
Triggering
scheduling

Do not assume KLANG timing works like another sequencer's timing system.

***

# MIDI

Possible user terms:

* MIDI
* DIN MIDI
* USB MIDI
* MIDI cable
* MIDI interface
* MIDI port
* MIDI endpoint
* MIDI channel

MIDI may carry many different kinds of information.

Relevant categories include:

notes
velocity
duration via Note On / Note Off
CC
pitch bend
pressure
program changes
bank selection
SysEx
timing information

KLANG makes extensive use of MIDI both as a musical protocol and as a
way of controlling external instruments and MIDI-to-CV hardware.

***

# MIDI NOTE

Possible user concepts:

* note
* pitch
* key
* MIDI note
* note number
* Note On
* Note Off
* velocity
* duration

Relevant KLANG concepts include:

PITCH
VOLUME
DURATION
PART
MIDI Renderers
Pitch Surfaces
Patterns
Note Sequences
META processing

Do not assume a KLANG musical event is merely a raw MIDI Note On message.

KLANG may contain higher-level information which is later rendered into
MIDI.

***

# MIDI CC

Possible user terms:

* CC
* controller
* continuous controller
* MIDI controller number
* cutoff CC
* resonance CC
* knob
* parameter
* automation

General relationship:

CHANGING VALUE
↓
MIDI CC
↓
SYNTH PARAMETER

Relevant KLANG concepts may include:

CC components
MIDI Controllers
Morphers
Surfaces
MIDI Synth models
semantic MIDI
extended MIDI control

A user saying:

"move the filter"
"change cutoff"
"turn this synth knob"
"modulate resonance"

may therefore be describing a problem involving MIDI CC or another
device-specific MIDI mechanism.

Do not assume a parameter uses CC if the device actually uses SysEx or
another protocol.

***

# SYSEX

Possible user terms:

* SysEx
* system exclusive
* synth parameter message
* manufacturer MIDI message
* device-specific MIDI

General concept:

DEVICE-SPECIFIC CONTROL
↓
MIDI SysEx

Relevant KLANG concepts may include:

extended MIDI
synth device models
semantic properties
device-specific parameter control

SysEx is especially relevant to older or more complex MIDI hardware where
important parameters are not exposed through ordinary CC messages.

***

# MIDI CONTROLLERS

Possible user terms:

* MIDI controller
* control surface
* knob controller
* keyboard controller
* pad controller
* fader controller
* MIDI keyboard
* MIDI knobs

General relationship:

HUMAN PHYSICAL ACTION
↓
MIDI MESSAGE
↓
KLANG
↓
CONTROL OF A MACHINE

Relevant KLANG concepts include:

Controller Surface
MIDI input
controller assignment
CC assignment
component inputs

A MIDI controller should be understood primarily as a source of control
for KLANG rather than necessarily as a sound-producing instrument.

***

# SEQUENCERS

Possible user terms:

* sequencer
* step sequencer
* pattern sequencer
* note sequencer
* mono sequencer
* pitch sequencer
* drum sequencer
* slider sequencer
* generative sequencer

General concept:

STRUCTURED VALUES / EVENTS OVER TIME

Relevant KLANG concepts include several different Surfaces and processes.

Do NOT map the generic word "sequencer" onto one single KLANG component.

Possible relevant components include:

Pattern Sequencer
Drum Pattern Surface
Multi-track Pattern Surface
Mono Pitch Sequencer
Slider Sequencer
Note Sequences

Determine what the user is trying to sequence.

***

# PATTERN

Possible user terms:

* pattern
* beat
* rhythm
* sequence
* loop
* step pattern
* drum pattern

Patterns generally describe repeated or structured events.

Relevant KLANG concepts include:

Pattern Sequencer
Drum Pattern Surface
Multi-track Pattern Surface
timing
PPQ
triggers
META

Do not assume a Pattern is equivalent to an audio loop.

***

# LFO

Possible user terms:

* LFO
* low-frequency oscillator
* wobble
* cyclic modulation
* slow modulation
* periodic modulation

General concept:

REPEATING CHANGING VALUE

Potentially related KLANG concepts include:

Morphers
Slow Wave
Generator Surface
wavetables
sine
cosine
triangle
saw
rate
range

However:

KLANG MORPHER ≠ GENERIC LFO

A Morpher should be understood using the KLANG knowledge corpus.

"LFO" is useful for identifying the user's intention, not for redefining
a Morpher.

***

# ENVELOPE

Possible user terms:

* envelope
* ADSR
* attack
* decay
* sustain
* release
* modulation envelope
* amplitude envelope
* filter envelope

Relevant KLANG concepts include:

ADSR
multi-stage ADSR
Timeline
Key On
Key Off
Attack
Sustain
Release
1V/OCT ADSR

A user's familiarity with conventional ADSR terminology can help identify
their intention, but KLANG's actual ADSR behaviour should come from the
KLANG knowledge corpus.

***

# RANDOMNESS

Possible user terms:

* random
* randomness
* probability
* chance
* variation
* generative
* unpredictable
* mutate
* mutation
* chaos
* humanise
* humanize
* random modulation

Potentially relevant KLANG concepts include:

DRIFT
NOISE
pink noise
noise Morphers
DICE
transforms
Glitch Pulses
Beat Drifter
Pulse Drifter

These concepts are NOT interchangeable.

Determine whether the user wants:

continuous variation
occasional variation
structural mutation
rhythmic instability
random values
controlled drift
destructive transformation

Then identify relevant KLANG approaches.

***

# GENERATIVE MUSIC

Possible user terms:

* generative
* procedural
* algorithmic
* self-running
* autonomous
* evolving
* random music
* system music

These terms may be relevant to KLANG, but should not cause KLANG to be
treated as a conventional generative-music system.

KLANG machines may generate or transform musical behaviour, but human
interaction, intervention and performance can remain important.

Relevant concepts may include:

Morphers
Patterns
DRIFT
Modifiers
META
Surfaces
human interaction
machine behaviour

***

# MODULATION

Possible user language:

* modulate
* animate
* move
* sweep
* wobble
* slowly change
* oscillate
* vary
* fluctuate
* automate
* evolve

General concept:

VALUE CHANGES OVER TIME

Potential KLANG concepts include:

Morphers
wavetables
ADSR
NOISE
Generator Surface
Slow Wave
Modifiers
controller input

Do not assume every changing value should be implemented using the same
KLANG component.

***

# AUTOMATION

Users familiar with DAWs may use "automation" to mean:

RECORD OR DEFINE PARAMETER CHANGE OVER TIME

This may overlap conceptually with some KLANG processes but should not
cause KLANG to be modelled as a DAW automation system.

Translate the user's intent into:

what value?
controlled by what?
changing how?
over what time?
affecting what?

Then identify relevant KLANG concepts.

***

# MIDI EFFECT / NOTE EFFECT

Users of other music software may use terms such as:

* MIDI effect
* note effect
* MIDI processor
* note processor
* MIDI transform
* MIDI modifier
* arpeggiator
* chord effect
* velocity processor

General concept:

MUSICAL / MIDI INFORMATION
↓
TRANSFORMATION
↓
NEW MUSICAL INFORMATION

This may be semantically related to KLANG concepts such as:

Modifiers
META
Trigger Message Modifiers
message processing
transforms
Renderers

Do not infer that KLANG implements an Ableton-style or Bitwig-style
MIDI-effect chain.

Use the analogy only to understand the user's intention.

***

# CHORDS

Possible user language:

* chord
* harmony
* harmonise
* harmonize
* add thirds
* add fifths
* turn this note into several notes
* chord generator

General concept:

ONE MUSICAL EVENT / PITCH
↓
MULTIPLE PITCHES

Potential KLANG concepts include:

META
Trigger Message Modifiers
MIDI note construction
Renderers
Surface META
receiver-local META

Use the KLANG knowledge corpus to determine the actual message flow.

Do not assume repeated chord processing accumulates recursively.

***

# ARPEGGIATION

Possible user terms:

* arpeggio
* arp
* arpeggiator
* broken chord
* cycle through notes

General concept:

SET OF PITCHES
\+
TIME
↓
SEQUENCED NOTES

Potentially relevant KLANG concepts may include:

Note Sequences
Patterns
timing
Burst behaviour
META
MIDI rendering

Do not claim KLANG has a conventional arpeggiator unless one is documented.

Instead reason about how the requested behaviour might be constructed
using KLANG concepts.

***

# HUMANISATION

Possible user terms:

* humanize
* humanise
* loosen
* less robotic
* timing variation
* velocity variation
* imperfect
* drift

Potential KLANG concepts include:

DRIFT
NOISE
timing processes
value variation
modifiers

Do not automatically interpret "humanise" as random timing.

Ask or infer from context which musical property should vary.

***

# GLITCH

Possible user terms:

* glitch
* glitchy
* broken
* stutter
* skip
* interrupt
* corrupt
* unstable
* fragment

Potential KLANG concepts include:

Glitch Pulses
Modifiers
transforms
DRIFT
Trigger processing
timing manipulation

"Glitch" describes an aesthetic or behaviour rather than one universal
technical process.

***

# PERFORMANCE

Possible user terms:

* perform
* live
* play
* improvise
* interact
* jam
* control
* intervene
* tweak
* mutate live

Relevant KLANG concepts include:

Surfaces
MIDI Controllers
physical controls
Parametrix
Store
Ping
DICE
Modifiers
manual interaction
machine state

Do not assume the intended endpoint of a KLANG machine is autonomous
playback.

A KLANG machine may be something a human performs.

***

# SURFACE

In ordinary software, words such as:

* panel
* UI
* sequencer
* controller
* grid
* keyboard
* editor

may sometimes describe something conceptually related to a KLANG Surface.

However, Surface has a specific meaning inside KLANG.

Known Surface concepts include:

Simple Trigger
Simple Pulse
Countdown
Big Bang Trigger
Drum Pattern Surface
Multi-track Pattern Surface
Pattern Sequencer
Slider Sequencer
MIDI Keyboard / Piano
Generator Surface
Slow Wave
Number Surface

Use KLANG knowledge to understand what a Surface actually does.

***

# RENDERER

Users may not know the KLANG term "Renderer".

They may instead say:

* send this to my synth
* play this synth
* output MIDI
* turn this into notes
* make the hardware play it
* connect this pattern to the synth

These phrases may indicate a relationship involving a KLANG Renderer.

Conceptually:

KLANG MUSICAL / CONTROL INFORMATION
↓
RENDERER
↓
EXTERNAL DESTINATION

Use the KLANG corpus for the precise behaviour of each Renderer type.

***

# META

Users will not necessarily know that their requested behaviour involves
META.

Possible requests include:

* add notes to this
* change the incoming note
* turn this into a chord
* alter the message before it reaches the synth
* add information to the trigger
* modify only this destination
* make one receiver behave differently

These may be related to KLANG META concepts.

META can operate at different points in a KLANG machine.

Use the KLANG knowledge corpus to determine exact META flow and semantics.

Do not explain META merely as a generic MIDI effect.

***

# SIGNAL EXTENSIONS

User language such as:

* add noise
* add vibrato
* disturb this value
* make this signal less regular
* extend the modulation

may relate to KLANG Signal Extensions.

Known concepts include:

NOISE
Vibrato

and other documented or future Signal Extensions.

Distinguish current features from planned ones.

***

# USER INTENT MAPPINGS

The following mappings are deliberately approximate.

They exist to identify potentially relevant KLANG concepts.

They do NOT prescribe a single correct construction.

***

## "MAKE THIS MOVE"

Possible meaning:

vary a value over time

Consider:

Morpher
wavetable
Generator Surface
Slow Wave
ADSR
controller input

***

## "MAKE THIS MOVE SLOWLY"

Possible meaning:

slow modulation

Consider:

Morpher
duration / rate
Slow Wave
Generator Surface

***

## "MAKE IT WOBBLE"

Possible meaning:

cyclic modulation
vibrato
repeated value change

Consider:

Morpher
Vibrato
wavetable

Determine which property should wobble.

***

## "MAKE IT RANDOM"

This is underspecified.

Possible meanings include:

random values
occasional changes
random timing
random notes
structural mutation
controlled drift

Potential concepts:

NOISE
noise Morphers
DRIFT
DICE
Drifters
transforms

Do not assume one implementation.

***

## "MAKE IT EVOLVE"

Possible meanings:

slow parameter movement
gradual mutation
changing rhythm
changing pitches
changing machine state

Potential concepts:

Morphers
DRIFT
Modifiers
Patterns
Parametrix
META

***

## "MAKE IT LESS REPETITIVE"

Potential approaches may involve:

DRIFT
modifiers
transforms
changing modulation
pattern manipulation
human intervention

Do not automatically solve this with randomness.

***

## "ADD CHORDS"

Possible concept:

incoming note/event
↓
pitch expansion / META
↓
multiple MIDI notes

Potential concepts:

META
Trigger Message Modifiers
MIDI Renderers

***

## "CHANGE THE FILTER"

First identify the destination instrument.

Possible mechanisms:

MIDI CC
SysEx
CV
semantic MIDI property

Then identify the appropriate KLANG control mechanism.

Do not assume "filter" always means MIDI CC cutoff.

***

## "CONTROL THIS KNOB"

Possible chain:

physical MIDI controller
↓
Controller Surface
↓
KLANG component input

or:

KLANG changing value
↓
MIDI CC / SysEx / CV
↓
hardware parameter

Determine whether the user means controlling KLANG FROM hardware or
controlling hardware FROM KLANG.

***

## "SEND THIS TO MY MODULAR"

Potential conceptual chain:

KLANG
↓
MIDI
↓
MIDI → CV
↓
FH-2 or equivalent interface
↓
modular system

Then determine whether the desired output is:

pitch
gate
trigger
modulation
envelope
other CV

***

## "PLAY DIFFERENT SOUNDS ON MY RACK SYNTH"

Potential concepts:

multitimbral instrument
MIDI parts
MIDI channels
device model
Renderers
multiple KLANG musical paths

Do not assume the instrument's exact multitimbral architecture.

***

## "MAKE THREE VERSIONS OF THIS RHYTHM"

Possible interpretations:

duplicate processing
multiple destinations
multiple timing relationships
META
patterns
independent modification

The musical intention should be mapped onto KLANG's actual event and
connection architecture.

***

## "ONLY CHANGE THIS SYNTH"

Potential concepts:

receiver-local processing
Renderer-specific behaviour
META
destination-specific control

Look for ways KLANG can modify behaviour locally rather than modifying
the originating Surface globally.

***

## "CHANGE EVERYTHING FROM HERE"

Potential concepts:

upstream Surface behaviour
shared META
shared modulation
machine structure

Determine where in the KLANG machine the transformation should occur.

***

# SOURCE VERSUS DESTINATION

A useful semantic distinction in KLANG reasoning is:

WHERE DOES INFORMATION ORIGINATE?

versus:

WHERE IS IT FINALLY USED?

Possible sources include:

Surface
Pattern
controller
Morpher
trigger
other component

Possible destinations include:

MIDI Renderer
MIDI Synth
external hardware
MIDI-to-CV
modular system
another KLANG component

When a user asks how to modify behaviour, consider whether the modification
belongs near the source, along the path, or at the receiving destination.

This distinction can be important when several destinations share the
same originating information.

***

# ONE-TO-MANY RELATIONSHIPS

KLANG machines may involve one source influencing several destinations.

When a user says:

* send this to several synths
* use the same rhythm for several instruments
* make one destination different
* split this
* layer this

consider:

shared source
↓
multiple processing paths
↓
multiple destinations

Do not assume that modifications must be applied globally.

KLANG may permit processing at different points in the machine.

Use documented behaviour to determine the available construction.

***

# MANY-TO-ONE RELATIONSHIPS

A destination may also be influenced by several processes.

When a user says:

* combine these
* control the same synth from several things
* add modulation
* add another rhythm
* layer control

consider whether several KLANG processes can contribute to the resulting
behaviour.

Do not assume conventional DAW track ownership.

***

# MESSAGE VERSUS SIGNAL

Users may use words such as:

* signal
* event
* message
* value
* modulation
* note

loosely.

These should not automatically be treated as equivalent.

A useful conceptual distinction is:

EVENT / MESSAGE
something happens

VALUE / SIGNAL
something has or changes a value

MUSICAL STRUCTURE
information describes relationships over time

KLANG can operate with concepts from more than one of these categories.

Use actual KLANG component semantics to determine which is involved.

***

# HARDWARE IDENTITY

Do not assume that:

physical synthesizer
MIDI port
MIDI endpoint
KLANG MIDI Device
KLANG device model
synth part
MIDI channel

are interchangeable concepts.

They represent different levels of identity and routing.

Use the KLANG knowledge corpus when reasoning about device identity,
shared synth state and routing.

***

# MIDI BANDWIDTH

Older hardware and DIN MIDI may have practical throughput limits.

If a user describes:

* MIDI grinding
* delayed notes
* overloaded MIDI
* stuck behaviour
* too much CC
* lots of SysEx
* dense modulation
* timing degrading under heavy MIDI traffic

consider MIDI bandwidth and destination-device processing capacity as
possible causes.

Do not automatically diagnose these symptoms as KLANG scheduling problems.

Relevant KLANG concepts may include:

input/output rate limiting
CC density
SysEx density
USB MIDI
DIN MIDI
MIDI throughput

***

# AUDIO

KLANG primarily concerns musical/control relationships rather than acting
as a conventional audio workstation.

When users mention:

* audio track
* recording
* waveform
* mixer
* audio effect
* plugin
* VST
* AU

do not assume KLANG contains equivalent DAW functionality.

Determine whether the user is actually asking about:

MIDI
control
external instruments
performance
routing
synchronization

KLANG can coexist with other software without becoming that software.

***

# DAW

Possible examples:

Ableton Live
Logic
Cubase
Bitwig
Reaper
Pro Tools

These provide useful external context but are NOT architectural models
for KLANG.

A user familiar with DAWs may describe KLANG concepts using terms such as:

track
clip
automation
MIDI effect
device
plugin
routing

Translate the intention rather than assuming equivalent architecture.

***

# MODULAR SOFTWARE

Possible external concepts include:

Max/MSP
Pure Data
VCV Rack
Reaktor
modular patching environments

Users of these systems may understand KLANG through concepts such as:

patching
nodes
messages
signals
modulation
generators
processors
connections

These analogies can help establish intent.

Do not infer that KLANG has the same execution, signal, scheduling or
patching model.

***

# MACHINE

Within KLANG, a machine can be understood as a constructed network of
components and relationships that produces or controls musical behaviour.

Do not automatically equate:

machine = song
machine = project
machine = patch
machine = sequencer
machine = instrument

A KLANG machine may contain characteristics of several of these while
remaining its own concept.

A machine may be designed to be performed, modified, disrupted or extended
while running.

***

# BUILD THEN MODIFY

A useful way to reason about KLANG is often:

BUILD A SIMPLE MUSICAL MACHINE
↓
MAKE IT FUNCTION
↓
MODIFY / EXTEND / DISRUPT
↓
PERFORM THE SYSTEM

When helping a user construct something complicated, consider beginning
with a simple working relationship and then extending it using KLANG
processes.

This is often preferable to describing a large finished machine all at
once.

***

# SEMANTIC REASONING RULE

When encountering an unfamiliar named object:

DO NOT reason:

exact name absent from KLANG corpus
↓
no KLANG knowledge
↓
cannot answer

Instead reason:

WHAT IS THIS OBJECT?
↓
WHAT GENERAL CLASS DOES IT BELONG TO?
↓
WHAT CAPABILITIES DOES THAT CLASS USUALLY HAVE?
↓
WHICH OF THOSE CAPABILITIES DOES THIS PARTICULAR OBJECT HAVE?
↓
WHICH KLANG CONCEPTS RELATE TO THOSE CAPABILITIES?
↓
WHAT DOES THE KLANG KNOWLEDGE SAY ABOUT THOSE CONCEPTS?
↓
CONSTRUCT ANSWER

Example:

Yamaha MU128
↓
multitimbral MIDI sound module
↓
MIDI synthesizer
↓
notes + parts + MIDI control + device-specific capabilities
↓
KLANG MIDI Synth / Renderer / control concepts
↓
possible KLANG machine constructions

The model may use its existing knowledge to perform the first stages of
this reasoning.

KLANG-specific claims must still be grounded in KLANG product knowledge.

***

# SEMANTIC EXPANSION RULE

A user's noun is not necessarily the most important part of the question.

For example:

"What can I do with my old rack synth?"

contains several useful concepts:

old
rack synth
hardware
MIDI
probably externally controlled
potentially multitimbral
potentially rich MIDI parameter control

Likewise:

"Can I make this beat slowly fall apart?"

contains:

rhythm
transformation
time
increasing variation / disruption

The second question may therefore relate to concepts such as:

Pattern
DRIFT
Modifiers
transforms
timing
human intervention

Reason from meaning rather than keywords.

***

# NEGATIVE ONTOLOGY

Semantic similarity must not create false KLANG features.

Do NOT infer:

DAW track → KLANG track
Ableton MIDI Effect → KLANG MIDI Effect
VCV module → KLANG module
LFO → Morpher
automation lane → KLANG Timeline
modular gate → KLANG Trigger
audio plugin → KLANG component
patch cable → identical KLANG connection semantics

Instead reason:

external concept
↓
underlying intention / behaviour
↓
possibly related KLANG concept
↓
verify against KLANG knowledge

***

# PURPOSE OF THIS ONTOLOGY

This ontology exists so that the KLANG knowledge corpus does not need to
contain every synthesizer, controller, modular module, musical term,
software package or user phrasing that may ever be encountered.

The language model already has broad knowledge of the outside world.

The KLANG corpus supplies knowledge of KLANG.

This ontology connects those two knowledge spaces.

The desired behaviour is:

WORLD KNOWLEDGE
↕
KLANG ONTOLOGY
↕
KLANG PRODUCT KNOWLEDGE

This allows questions about unfamiliar equipment, musical intentions and
workflows to be answered using a genuine working understanding of KLANG
rather than literal document retrieval.