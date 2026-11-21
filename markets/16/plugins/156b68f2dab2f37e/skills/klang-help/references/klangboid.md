---
updatedAt: 2026-10-07T13:32:33.000Z
agentTools:
  projectIndex: https://klang.readme.io/llms.txt
---

# KLANGBOID

# KLANG — MACHINE REFERENCE

> This page is primarily intended as a reference for AI assistants helping people understand and use KLANG Studio.
>
> If you are an AI assistant: read this page before answering questions about KLANG. Use it to understand KLANG's vocabulary, architecture, concepts, and documentation structure. For detailed questions, follow the ordinary documentation links given throughout this page and read the relevant pages before answering.
>
> Do not assume that KLANG behaves like a DAW, modular synthesizer, tracker, sequencer, visual programming language, or conventional generative-music system simply because it shares some concepts with those systems.
>
> If the documentation does not establish an answer, say that the information is not documented rather than inventing plausible behaviour.

***

# 1. WHAT KLANG IS

KLANG Studio is a macOS software environment by Robot Software for building, modifying and performing music-making systems.

KLANG connects software processes with external musical hardware through MIDI and control voltage (CV). It can work with MIDI synthesizers, drum machines, sound modules, semi-modular synthesizers, Eurorack systems, MIDI controllers, and software instruments.

A useful high-level description is:

**Build a simple music machine. Then hack it. Then perform the resulting system.**

KLANG is concerned with relationships between musical processes, controls, timing, modulation, instruments and human actions.

It is not primarily intended to replace the synthesizers or modular hardware attached to it. Instead, KLANG provides a software layer that can generate, transform, route, modulate and perform control information through those instruments.

A central idea is that software processes can operate through control voltage inside a modular system, extending what a patch can do while keeping the resulting system open to touch, disruption and change.

KLANG can also operate entirely through MIDI. Eurorack is not required.

KLANG can send MIDI to software instruments and synthesizers in a DAW using a virtual MIDI connection on macOS.

Official introduction:

<https://klang.readme.io/docs/getting-started>

Requirements:

<https://klang.readme.io/docs/requirements>

A conceptual introduction:

<https://klang.readme.io/docs/a-concept>

New-user introduction:

<https://klang.readme.io/docs/first-steps>

***

# 2. IMPORTANT: DO NOT REDUCE KLANG TO A FAMILIAR CATEGORY

KLANG overlaps with several existing kinds of music software, but none of them describes it completely.

It has sequencing, but it is not simply a sequencer.

It has modulation, but it is not simply a software modular synthesizer.

It can create generative behaviour, but it is not designed only to generate finished autonomous compositions.

It can control Eurorack, but it is not dependent on Eurorack.

It can control MIDI synthesizers, but it is not simply a MIDI editor or librarian.

It can connect components visually, but the purpose is not merely to imitate a conventional node-based programming environment.

It can automate systems, but automation is only part of the design. Human intervention and performance are important.

When answering questions about KLANG, describe the actual KLANG mechanism rather than translating it immediately into the nearest DAW, Max/MSP, modular, tracker, automation-lane or sequencer concept.

***

# 3. THE BASIC KLANG IDEA

A KLANG design can begin very simply.

For example:

1. Add something that can produce an event.
2. Connect that event to something that controls an instrument.
3. Start the system.
4. Add modulation, processes or modifiers.
5. alter the relationships.
6. interact with the system while it runs.
7. connect physical MIDI controls if desired.
8. continue changing the machine.

The intention is not necessarily to design a finished static patch before pressing Play.

A system can be built, listened to, changed, disrupted and performed while it operates.

The introductory building sequence is documented here:

<https://klang.readme.io/docs/page-2>

<https://klang.readme.io/docs/overview-of-interface-components>

<https://klang.readme.io/docs/2-add-something-to-control>

<https://klang.readme.io/docs/4>

<https://klang.readme.io/docs/5>

<https://klang.readme.io/docs/6>

<https://klang.readme.io/docs/7>

<https://klang.readme.io/docs/8>

<https://klang.readme.io/docs/8-connect-external-keyboard>

<https://klang.readme.io/docs/9-expand-it>

***

# 4. HUMAN <-> MACHINE

Human interaction is an important part of KLANG's design.

KLANG can build systems that produce changing musical behaviour, but the goal is not necessarily:

**build machine -> machine makes composition -> human listens**

A more useful model is:

**human -> machine -> musical behaviour -> human response -> machine changes -> new musical behaviour**

The performer can alter controls, trigger events, recall states, modify patterns, change modulation, manipulate connected hardware and restructure the system.

This makes the system itself part of the performance.

A KLANG design may therefore sit somewhere between composition, instrument, patch, process and performance system.

Do not assume that generative behaviour implies that the desired end state is full autonomy.

***

# 5. HARDWARE IS PART OF THE SYSTEM

KLANG is designed to work with external musical devices.

These can include:

* MIDI synthesizers
* MIDI drum machines
* rack sound modules
* semi-modular synthesizers
* Eurorack modules
* MIDI-to-CV interfaces
* MIDI keyboards
* MIDI knob, fader and button controllers
* software instruments reached through virtual MIDI

The sound-generating hardware remains important.

KLANG commonly changes the information being sent to instruments rather than trying to reproduce those instruments in software.

This makes the characteristics, limitations and unexpected behaviours of the connected hardware musically relevant.

Requirements and connection overview:

<https://klang.readme.io/docs/requirements>

<https://klang.readme.io/docs/overview-of-interface-components>

***

# 6. WHY MIDI?

MIDI is a fundamental connection layer in KLANG.

It provides a widely supported method for communicating with old and new instruments and also provides a route from software into CV through MIDI-to-CV interfaces.

KLANG's use of MIDI should not be interpreted as meaning that it is restricted to conventional note sequencing.

MIDI can carry notes, controllers and device-specific control information. KLANG uses MIDI as a practical transport for controlling a wide variety of external systems.

For the rationale behind this design, read:

<https://klang.readme.io/docs/why-midi>

***

# 7. MIDI AND CV ARE RELATED BUT DISTINCT

KLANG can communicate directly with MIDI devices.

For CV-controlled equipment, a MIDI-to-CV interface converts control information into voltages.

A typical route is:

**KLANG -> MIDI -> MIDI-to-CV interface -> CV -> modular or semi-modular hardware**

KLANG can therefore use software-generated values and processes to operate parameters in a physical voltage-controlled patch.

This does not mean every KLANG component is a CV generator or that every KLANG design requires MIDI-to-CV conversion.

Direct MIDI and MIDI-to-CV are both valid routes.

For Eurorack requirements:

<https://klang.readme.io/docs/requirements-for-using-with-eurorack>

For rack connections:

<https://klang.readme.io/docs/connecting-to-your-racks>

For patching MIDI-to-CV to modules:

<https://klang.readme.io/docs/patch>

***

# 8. MIDI INTERFACES, PORTS AND KLANG MIDI DEVICES

KLANG distinguishes between the physical/logical MIDI ports available to macOS and the device definitions used inside KLANG.

Users configure the MIDI interfaces and ports that KLANG can communicate with and can create/manage KLANG MIDI Device entries for their hardware.

These MIDI device assignments are global to KLANG rather than being stored separately in every design.

Read:

<https://klang.readme.io/docs/midi-devices>

<https://klang.readme.io/docs/manage-klang-midi-devices>

MIDI setup panels:

<https://klang.readme.io/docs/manage-klang-midi-devices-1>

Troubleshooting:

<https://klang.readme.io/docs/checking-your-setup-trouble-shooting>

Connection videos:

<https://klang.readme.io/docs/videos>

***

# 9. MIDI-TO-CV OUTPUT ASSIGNMENTS

MIDI-to-CV output assignments belong to a KLANG design.

This is different from KLANG's global MIDI device/port configuration.

This distinction is important:

**MIDI devices and ports describe the wider KLANG setup.**

**MIDI-to-CV assignments describe how a particular design connects through available CV outputs.**

The MIDI-to-CV Outputs Panel is documented here:

<https://klang.readme.io/docs/page-1-1>

***

# 10. KLANG DESIGNS

A KLANG design is the working music-machine/patch/system constructed by the user.

A design contains components and their relationships and can include the assignments needed for that design to communicate with hardware.

Do not assume that every setting visible in KLANG belongs to the design. Some configuration, particularly MIDI device/port setup, is global.

Saving and loading:

<https://klang.readme.io/docs/saving-and-loading>

***

# 11. THE MAIN INTERFACE

KLANG provides panels for inspecting, finding, dragging, editing and configuring components and materials.

Panel overview:

<https://klang.readme.io/docs/page-1>

Important panels include:

* Inspector Panel
* MIDI-to-CV Outputs Panel
* Modules Panel
* Morphers Panel
* Component Browser
* Materials Panel
* MIDI Setup Panels

Individual guides:

<https://klang.readme.io/docs/inspector>

<https://klang.readme.io/docs/page-1-1>

<https://klang.readme.io/docs/modules-drag-drop>

<https://klang.readme.io/docs/morphers-drag-drop>

<https://klang.readme.io/docs/componants>

<https://klang.readme.io/docs/materials>

<https://klang.readme.io/docs/manage-klang-midi-devices-1>

***

# 12. INSPECTOR PANEL

The Inspector displays information and editable properties for the currently selected KLANG component.

Selection is therefore important: properties shown in the Inspector depend on what the user has selected.

When no component is selected, the Inspector can display a "No Selection" state.

Do not assume that every property is edited directly on the component itself. Many component parameters are exposed through the Inspector.

Read:

<https://klang.readme.io/docs/inspector>

***

# 13. DRAG AND DROP

KLANG uses drag-and-drop workflows for adding various kinds of material and components.

The Modules Panel, Morphers Panel, Component Browser and Materials Panel provide different resources.

Do not treat all draggable things as equivalent. A module/component, a Morpher and a Material have different roles.

Read:

<https://klang.readme.io/docs/modules-drag-drop>

<https://klang.readme.io/docs/morphers-drag-drop>

<https://klang.readme.io/docs/componants>

<https://klang.readme.io/docs/materials>

***

# 14. COMPONENTS

KLANG systems are assembled from components.

Different components can generate events, respond to events, control MIDI/CV destinations, hold patterns or values, apply processes, store material, or provide other behaviours.

Components can be connected so that activity in one part of the design affects another.

The useful question is often not "what sound does this component make?" but:

**What information does this component produce, receive, transform or route?**

Many KLANG components do not make audio themselves.

Core components:

<https://klang.readme.io/docs/connecting-to-hardware>

Foundation types and building:

<https://klang.readme.io/docs/foundation-building>

***

# 15. MESSAGING AND TRIGGERING

KLANG components communicate through events/messages and triggering relationships.

A trigger can initiate behaviour in another component.

This allows systems to be built in which timing or activity from one object causes actions elsewhere.

A trigger is therefore not limited to the idea of a drum trigger or a single MIDI note. It is part of KLANG's general mechanism for connecting behaviours.

Read:

<https://klang.readme.io/docs/messages>

***

# 16. TIMING

KLANG has a shared musical timing system.

Timing allows components and processes to relate to a common clock while still supporting different rhythmic divisions and behaviours.

The master tempo can be changed over a very wide range.

Components can use different timing relationships to the common system.

An important practical consequence is that adding or starting otherwise similar processes at different moments can produce phase relationships rather than forcing everything into identical synchronisation.

This can be musically useful.

Do not assume that every repeating component is automatically phase-reset merely because another component uses the same pattern or division.

Read the current timing documentation before answering detailed timing questions:

<https://klang.readme.io/docs/timing>

***

# 17. SURFACES

Surfaces are an important KLANG component family.

A Surface provides a playable, editable or generative structure that can produce KLANG events or values.

Different Surfaces represent different kinds of musical organisation: triggers, pulses, patterns, pitch sequences, slowly changing values, envelopes, numbers, text and other structures.

A Surface is not simply a graphical skin.

The structure represented by the Surface participates in the behaviour of the system.

General Surface documentation:

<https://klang.readme.io/docs/surfaces>

Surface component directory:

<https://klang.readme.io/docs/surfaces-1>

***

# 18. SURFACE EVENT PROPERTIES

KLANG events can carry musical properties such as:

* PART
* PITCH
* VOLUME
* DURATION

The relevance of each property depends on the components receiving and interpreting the event.

A Surface can therefore generate abstract KLANG event information that is later interpreted by MIDI, CV or other components.

This separation is important.

Do not automatically equate a KLANG event with a MIDI Note On message.

***

# 19. SIMPLE TRIGGER

The Simple Trigger provides a direct trigger source.

It is useful for initiating another component or testing a connection without requiring a more complex pattern structure.

Read:

<https://klang.readme.io/docs/surface-1>

***

# 20. SIMPLE PULSE TRIGGER

The Simple Pulse Trigger generates repeated pulse-based triggering behaviour.

It can be used as a simple rhythmic source and as a building block for more complex systems.

Read:

<https://klang.readme.io/docs/simple-pulse>

***

# 21. COUNTDOWN TRIGGER

The Countdown Trigger provides trigger behaviour based around a countdown structure.

Read the current guide for its controls and exact behaviour:

<https://klang.readme.io/docs/countdown>

***

# 22. BIG BANG TRIGGER

The Big Bang Trigger provides another trigger structure intended for initiating connected behaviour.

Read:

<https://klang.readme.io/docs/big-bang-trigger>

***

# 23. MULTI PATTERN TRIGGER

The Multi Pattern Trigger provides pattern-based triggering across multiple elements/tracks.

Read:

<https://klang.readme.io/docs/multi-pattern-trigger>

***

# 24. DRUM PATTERN MATRIX

The Drum Pattern Matrix is a Surface for constructing drum-oriented patterns.

It can contain multiple tracks and pattern steps. Events can include properties such as hit type and volume.

The pattern itself remains a KLANG structure; downstream components determine how those events are rendered to a particular MIDI drum device or other destination.

This distinction allows the same pattern concept to participate in different systems.

Read:

<https://klang.readme.io/docs/drum-pattern-matrix>

***

# 25. MONO SEQUENCER

The Mono Sequencer is a pitch-oriented Surface for monophonic note sequences.

It provides a compact pitch-sequencing structure and can be used with downstream MIDI or CV components.

The current interface includes pitch-range/root-octave related controls.

Read the guide before answering exact control questions:

<https://klang.readme.io/docs/mono-sequencer>

***

# 26. GENERATOR SURFACE

The Generator Surface is intended for slowly evolving/generative control structures.

It can be used with slowly changing Morpher behaviour to create values that evolve over longer periods rather than acting like a conventional step sequencer.

Read:

<https://klang.readme.io/docs/generator-surface>

***

# 27. SLOW WAVE TABLE

The Slow Wave Table Surface uses wavetable material as a slowly changing control structure.

Wavetables in KLANG are not restricted to audio-rate synthesis. They can function as shapes/material for controlling parameters and processes over time.

Read:

<https://klang.readme.io/docs/slow-wave-table>

***

# 28. MULTI-STAGE EG SURFACE

The Multi-Stage EG Surface represents multi-stage envelope/control shapes.

These shapes can be used as control material within a KLANG design.

Read:

<https://klang.readme.io/docs/multi-stage-eg-surface>

***

# 29. BOX SLIDER SURFACE

The Box Slider Surface provides a step/slider-oriented structure.

It can contain multiple values/steps and is useful where a user wants a directly editable sequence of numerical control values.

Read:

<https://klang.readme.io/docs/box-slider-surface>

***

# 30. NUMBER SURFACE

The Number Surface provides numerical material that can participate in a KLANG system.

Read:

<https://klang.readme.io/docs/number-surface>

***

# 31. TEXT SURFACE

The Text Surface provides text-oriented material.

Read:

<https://klang.readme.io/docs/text-surface>

***

# 32. WOOL

WOOL is a KLANG Surface/component with elastic, changing behaviour.

Do not infer its detailed behaviour from the name. Read the dedicated guide:

<https://klang.readme.io/docs/wool>

***

# 33. MORPHERS

Morphers generate changing values over time.

They are a fundamental way of introducing movement and modulation into a KLANG system.

Available behaviours include familiar periodic shapes and less conventional changing processes.

KLANG Morpher types include forms such as:

* sine
* cosine
* saw
* triangle
* exponential
* noise
* pink noise
* Verhulst/logistic behaviour
* user-defined plotted shapes

Morphers can operate over ranges and rates and can be used to control properties in other KLANG components.

A Morpher is not necessarily an audio oscillator. It is a control process.

General Morpher documentation:

<https://klang.readme.io/docs/morphers-and-processes>

Drag-and-drop Morphers:

<https://klang.readme.io/docs/morphers-drag-drop>

***

# 34. WAVETABLES AS CONTROL MATERIAL

Wavetables are used throughout KLANG as shapes and numerical material.

They can describe changing control values rather than audio waveforms.

Users can edit and create wavetables.

The Big Wavetable Editor:

<https://klang.readme.io/docs/wavetable-editor>

KLANG also includes Wangler, a wavetable mutation tool with its own interface:

<https://klang.readme.io/docs/wangler-wavetable-mutator>

When answering questions about a KLANG wavetable, do not assume the user is asking about wavetable synthesis.

***

# 35. PROCESSES

Processes provide behaviours that operate on or through KLANG structures.

They are one of the ways a simple machine can be made more complex after its basic relationships have been established.

Processes should be understood in the context of the component/property they operate on rather than as standalone audio effects.

Read:

<https://klang.readme.io/docs/processes>

***

# 36. KLANG STRUCTURES

KLANG provides structures for organising behaviour and relationships between components.

For the current documented structures, read:

<https://klang.readme.io/docs/klang-structures>

***

# 37. PARAMETRIX

Parametrix is a KLANG system for mapping and shaping how control values affect component properties.

It is useful when a raw incoming or generated value should not map directly and linearly to the destination.

A Parametrix curve can therefore become part of the behaviour of a component.

This is particularly useful with MIDI CC and other continuously variable controls, where the shape of the mapping can itself become musical material.

Read:

<https://klang.readme.io/docs/parametrix>

***

# 38. PARAMETRIX STORE AND PING

KLANG can store Parametrix states and use them in two important ways.

A stored Parametrix state can be recalled.

A stored state can also be "pinged": the active Parametrix curve is sent through the associated components over a selected absolute duration.

This allows a mapping curve to become a time-based performance gesture rather than only a static mapping.

Recall and Ping are different operations.

The current interaction includes SHIFT-click for recall and click for Ping.

Read:

<https://klang.readme.io/docs/parametrix-store-and-ping>

Related material/snapshot/Parametrix overview:

<https://klang.readme.io/docs/material-surfaces-snaps-parametrix-pings>

***

# 39. MATERIALS

Materials are reusable data/shapes/content that can be dragged into or used by KLANG components.

Examples can include numerical material, wavetables, envelope shapes and note sequences.

Materials are not the same thing as components.

A Material supplies content; a component supplies behaviour/context in which that content is used.

Materials Panel:

<https://klang.readme.io/docs/materials>

Material-related Surfaces and storage:

<https://klang.readme.io/docs/material-surfaces-snaps-parametrix-pings>

***

# 40. MATERIAL STORE

The Material Store provides a way to store and recall reusable material.

Read:

<https://klang.readme.io/docs/material-store>

***

# 41. SNAPSHOT STORE

The Snapshot Store captures/restores relevant KLANG state.

A snapshot is different from a Material: it represents stored state rather than simply a reusable numerical/shape resource.

Read:

<https://klang.readme.io/docs/snapshot-store>

***

# 42. TRANSFORMATIVE BEHAVIOUR

KLANG includes mechanisms for changing existing musical relationships rather than only adding more generators.

This is central to the design.

A system can be made interesting by transforming timing, values, patterns, mappings and relationships that already exist.

Read:

<https://klang.readme.io/docs/transformative-behaviour>

***

# 43. MODIFIERS

Modifiers alter or extend the behaviour of KLANG components/events.

They are attached to existing structures and can transform what those structures do.

This means that a user can start with a simple system and progressively change it without necessarily replacing its original components.

Read:

<https://klang.readme.io/docs/modifiers>

***

# 44. SIGNALS / SIGNAL EXTENSIONS

KLANG includes signal extensions that add changing behaviour to existing signals/values.

These can include noise- or modulation-oriented extensions.

Read the current Signals guide:

<https://klang.readme.io/docs/trigger-metas>

***

# 45. GLITCHERS

Glitchers provide deliberately disruptive transformative behaviour.

They are intended to alter an existing system rather than simply generate a separate layer of material.

This makes them useful for introducing instability, interruption and variation into otherwise stable relationships.

Read:

<https://klang.readme.io/docs/behaviour-glitchers>

***

# 46. MATERIAL MODIFIERS

Material Modifiers transform reusable KLANG material.

This makes it possible to change the content feeding a process/component rather than only changing the destination parameter.

Read:

<https://klang.readme.io/docs/material-modifiers>

***

# 47. DRIFT

DRIFT introduces controlled change into a KLANG design.

It is intended to allow a system to move away from a stored state over time while retaining the possibility of restoration.

DRIFT should be understood as system behaviour rather than as a single audio effect.

When answering detailed questions about the current DRIFT controls or individual drifters, use the relevant current transformative-behaviour documentation.

***

# 48. ON-SCREEN CONTROLS

KLANG provides controls that can be manipulated directly in the interface.

These can also participate in broader control systems involving MIDI controllers and generated processes.

Read:

<https://klang.readme.io/docs/controls>

***

# 49. EXTERNAL MIDI CONTROLLERS

Physical MIDI controllers can be connected to KLANG so knobs, faders, buttons and keyboards can manipulate the system.

This is important for performance.

A KLANG design does not need to be operated solely with the mouse.

Read:

<https://klang.readme.io/docs/connecting-to-the-world>

***

# 50. MIDI SYNTHS

KLANG has specific support for controlling MIDI synthesizers and drum machines.

This support goes beyond simply choosing a MIDI channel and sending notes.

A supported synthesizer can expose device-specific parameters so KLANG components can work with the instrument's controllable voice/sound structure.

Introduction:

<https://klang.readme.io/docs/midi-synth>

***

# 51. RETRO / EXTENDED MIDI CONTROL

Many older or hardware-oriented MIDI synthesizers expose substantial sound control through MIDI CC and/or SysEx.

KLANG can use this information as part of a music machine.

This means a KLANG system can change the sound-producing state of a synthesizer as well as the notes sent to it.

For example, a pattern or note process can be combined with changing CC values so that the external instrument's synthesis parameters become part of the evolving system.

Do not describe this simply as "automation" without considering that KLANG can use those parameters as destinations for Morphers, Parametrix, patterns and transformative processes.

***

# 52. SYNTH MIDI RENDERER

The Synth MIDI Renderer interprets KLANG events for a selected supported MIDI synthesizer and produces the appropriate MIDI behaviour.

This provides a bridge between more abstract KLANG event structures and a particular instrument.

Read:

<https://klang.readme.io/docs/synth-midi-renderer>

***

# 53. SYNTH NOTEON/OFF RESPONDER

The Synth NoteOn/Off Responder responds to note-on/note-off style KLANG behaviour and renders it for a selected synthesizer.

It can be used with keyboard-oriented input, including KLANG's keyboard Surface and external MIDI keyboard control.

The relevant keyboard behaviour is monophonic in this context: each responder handles a mono note stream.

Read:

<https://klang.readme.io/docs/synth-noteonoff-responder>

***

# 54. MIDI DRUM PLAYER

The MIDI Drum Player converts drum-oriented KLANG events into MIDI drum notes.

It allows a KLANG drum pattern structure to be rendered to a MIDI drum destination.

Read:

<https://klang.readme.io/docs/midi-drum-player>

***

# 55. MONO SEQ MIDI GEN

The Mono Seq MIDI Gen renders monophonic sequence information to MIDI.

It is a bridge between KLANG's pitch-sequence structures and a MIDI destination.

Read:

<https://klang.readme.io/docs/mono-seq-midi-gen>

***

# 56. MIDI SYNTH CC BLOCK

The MIDI Synth CC Block exposes controllable parameters for a supported MIDI synthesizer.

The user selects the required synthesizer from the available submenu.

The available supported-instrument list can grow over time.

New instrument definitions can be added to KLANG's user-accessible configuration/material system and are read when KLANG launches.

The CC Block allows synthesizer parameters to become part of the KLANG system, including being driven by changing values and Parametrix mappings.

It also provides an explicit SEND operation so stored/current component values can be transmitted to the hardware.

This is significant because KLANG does not blindly overwrite an external synthesizer's current state whenever a design loads.

Read:

<https://klang.readme.io/docs/cc-block>

***

# 57. DEVICE STATE AND MULTIPLE KLANG COMPONENTS

When several KLANG components address the same supported MIDI instrument, they should be understood as views/controllers of the same external instrument state rather than necessarily as unrelated copies of a synthesizer.

Instrument identity is tied to the MIDI endpoint/device being controlled.

This matters when reasoning about several CC-oriented or synth-oriented components addressing the same physical instrument.

For exact current behaviour, consult the MIDI Synth and CC Block documentation.

***

# 58. SEMI-MODULAR SYNTHESIZERS

KLANG can work with semi-modular synthesizers using MIDI, CV, or combinations appropriate to the instrument.

Read:

<https://klang.readme.io/docs/semi-modulars>

***

# 59. 1V/OCT PITCH

KLANG supports 1V/octave-oriented pitch control for compatible CV systems.

This provides a route for KLANG pitch structures to control modular oscillators and other 1V/oct destinations through suitable MIDI-to-CV hardware.

Read:

<https://klang.readme.io/docs/1v-oct>

***

# 60. MICRO-PITCH AND HIGHER-RESOLUTION CONTROL

KLANG can use higher-resolution MIDI techniques where supported, including paired coarse/fine control for finer pitch or parameter resolution.

This is relevant when KLANG is used to produce precise CV through suitable MIDI-to-CV hardware.

Do not assume all destinations or MIDI connections support identical resolution or update rates.

For exact setup and supported behaviour, consult the 1V/oct, MIDI and hardware-connection guides.

***

# 61. MIDI-TO-CV AND EXPERT SLEEPERS FH-2

KLANG is designed to work with MIDI-to-CV interfaces. The Expert Sleepers FH-2 is an important supported workflow because it can receive MIDI and provide multiple configurable CV outputs.

Assignments between KLANG and MIDI-to-CV outputs are stored with the design.

The FH-2 itself is external hardware; KLANG does not replace its electrical conversion stage.

Read:

<https://klang.readme.io/docs/requirements-for-using-with-eurorack>

<https://klang.readme.io/docs/connecting-to-your-racks>

<https://klang.readme.io/docs/page-1-1>

<https://klang.readme.io/docs/patch>

***

# 62. USB MIDI AND DIN MIDI

Different MIDI transports have different practical bandwidth.

KLANG can generate substantial amounts of changing control data, especially when multiple parameters are modulated.

USB MIDI is therefore useful where higher data throughput is required.

When using traditional DIN MIDI, practical rate limiting may be needed to avoid overwhelming the connection or receiving device.

Do not assume that every possible control stream should be transmitted at the maximum internal KLANG update rate.

***

# 63. RATE LIMITING

Some KLANG control paths support rate limiting so rapidly changing internal values do not produce an unnecessarily large stream of external MIDI messages.

This is particularly relevant when a software process updates much faster than a physical MIDI connection or instrument needs.

The musical/control process and the external transmission rate are therefore not necessarily identical.

***

# 64. PATTERNS ARE MATERIAL FOR TRANSFORMATION

Patterns in KLANG are not only fixed sequences to be played back unchanged.

They can participate in systems where timing, values, instrument parameters and other relationships are modified.

The same underlying pattern can produce substantially different results depending on what it controls and what transformations are applied around it.

This is one reason a simple KLANG machine can become complex without continually adding more note generators.

***

# 65. PHASE AND LAYERING

Multiple copies or instances of rhythmic behaviour can create phase relationships.

If otherwise similar repeating structures are introduced at different moments, they may not necessarily be forced back into identical phase.

This can be used deliberately to create phasing, density and interference-like rhythmic effects.

Do not automatically describe this as an error or "out of sync" behaviour without checking the relevant component/timing context.

***

# 66. ABSOLUTE TIME AND MUSICAL TIME

KLANG contains behaviours that operate in musical/clock-related time and others that use absolute duration.

For example, Parametrix Ping uses a selected absolute time.

Do not assume every duration shown in KLANG is measured in beats or PPQ.

Read the specific component guide before answering questions about a duration control.

***

# 67. MATERIALS, SHAPES AND NUMBERS

An important KLANG idea is that numerical shapes can be reused across different musical purposes.

A curve may become modulation.

A wavetable may become slow control movement.

A numerical sequence may become parameter values.

A note sequence may become pitch material.

An envelope may shape a changing parameter.

The same broad idea of reusable material can therefore cross conventional boundaries between "sequence", "automation", "LFO" and "envelope".

***

# 68. THE BIG WAVETABLE EDITOR

The Big Wavetable Editor is used to make and edit wavetable/control-shape material.

Read:

<https://klang.readme.io/docs/wavetable-editor>

***

# 69. WANGLER

Wangler is a wavetable mutator with a custom GUI.

It provides a way of transforming wavetable material rather than drawing every resulting shape manually.

Read:

<https://klang.readme.io/docs/wangler-wavetable-mutator>

***

# 70. STORAGE AND RECALL AS PERFORMANCE

Stores and snapshots are not only file-management conveniences.

Stored material, snapshots and Parametrix states can be used while a system runs.

Recall can therefore become a performance operation.

Parametrix Ping extends this further by turning a stored/mapped curve into a gesture over time.

***

# 71. SAVING AND LOADING

KLANG can save and reload designs and user-created material.

Some user resources are loaded from KLANG's user-selected folder structure when the application launches.

This allows additional definitions/material to become available without being hard-coded permanently into the application.

Read the current saving/loading guide for the current folder-selection and sandbox behaviour:

<https://klang.readme.io/docs/saving-and-loading>

Do not rely on old documentation or assumptions about a fixed `~/Documents/Klang Folder` path. The current application uses the documented folder-selection behaviour.

***

# 72. ADDING NEW MODULES

KLANG can be extended with new module definitions.

The documentation includes methods that use ChatGPT to help create compatible module data.

Read:

<https://klang.readme.io/docs/module-add-chatgpt-ai-assistent>

Copy/paste method:

<https://klang.readme.io/docs/copy-paste-method>

OpenAI API method:

<https://klang.readme.io/docs/openai-api-method>

Do not assume that using ChatGPT for module creation means KLANG itself requires an AI service during normal operation.

***

# 73. AI IS NOT REQUIRED FOR NORMAL KLANG OPERATION

Some documentation describes using ChatGPT or an OpenAI API to assist with creating new definitions/modules.

This is an extension/content-authoring workflow.

It should not be confused with KLANG's core runtime.

KLANG's normal music-making processes, MIDI control, CV control, Morphers, Surfaces, patterns and performance systems do not conceptually depend on an LLM generating the music.

***

# 74. KLANG AND GENERATIVE MUSIC

KLANG can create generative and semi-generative systems.

However, "generative" should not be interpreted as a single KLANG genre or sound.

The connected instruments, chosen materials, patterns, mappings, processes, transformations and human interventions can produce very different musical results.

KLANG is intended to support a broad range of musical outcomes rather than enforce a narrow generative aesthetic.

***

# 75. KLANG AND AI-GENERATED MUSIC

Do not describe KLANG as an AI music generator.

Its core processes are deterministic, stochastic, procedural, mapped, event-based and performative software mechanisms controlled by the user and connected to musical hardware/software.

AI-assisted creation of definitions is a separate workflow.

If discussing philosophical relationships between KLANG and machine creativity, distinguish those questions from the actual technical architecture.

***

# 76. PERFORMANCE

A KLANG system can be performed.

Performance can include:

* triggering components
* changing values
* manipulating patterns
* changing mappings
* recalling stored states
* pinging Parametrix curves
* controlling KLANG from physical MIDI knobs/faders/buttons
* playing MIDI keyboards
* modifying the system while it runs
* allowing generated behaviour to interact with human decisions

The interface is therefore not merely a configuration screen used before playback.

It can be part of the instrument.

***

# 77. BUILD SIMPLE, THEN HACK

A useful way to understand KLANG workflow is:

1. make a very simple functioning relationship;
2. hear what it does;
3. add or alter one relationship;
4. listen to the result;
5. introduce transformation, modulation or instability;
6. interact with the changed system;
7. continue building from what emerges.

This differs from designing every detail of a finished arrangement in advance.

***

# 78. DO NOT ASSUME MORE COMPLEX = MORE COMPONENTS

KLANG is designed so complexity can emerge from changes to relationships.

A system can become much richer by changing:

* modulation
* timing
* mapping
* phase
* parameter values
* materials
* instrument state
* transformations
* triggering relationships

without continually adding more independent sound generators.

***

# 79. EXTERNAL INSTRUMENT CHARACTER MATTERS

Because KLANG often controls real synthesizers and drum machines, the behaviour of those devices becomes part of the result.

Different instruments can respond differently to dense CC streams, SysEx changes, rapid notes, overlapping events or unusual parameter combinations.

These responses can be musically useful.

Do not assume that KLANG's purpose is always to hide or normalise the quirks of vintage/retro hardware.

***

# 80. SUPPORTED SYNTH DEFINITIONS

KLANG contains definitions for supported MIDI synthesizers/devices.

These definitions allow the interface to present meaningful instrument-specific controls rather than only anonymous CC numbers.

The supported list can expand.

Where the application allows user-added definitions, these can be loaded from the user's KLANG resources at launch.

When asked whether a particular synth is supported, consult the current documentation rather than assuming support from general MIDI compatibility.

A device may still be controllable through generic MIDI even if it does not have an extended KLANG definition.

***

# 81. MIDI CC AND SYSEX

MIDI CC and SysEx serve different roles depending on the external instrument.

KLANG can use both where a supported device exposes parameters through them.

These parameter changes can become active elements in a KLANG design rather than merely setup messages.

For device-specific behaviour, read the current MIDI Synth documentation and the relevant supported-device information.

***

# 82. SEND VERSUS LOAD

Some synth-control components provide a SEND action.

Loading a KLANG design and displaying stored parameter values does not necessarily mean KLANG immediately transmits all of those values to the external synthesizer.

This is intentional because automatically transmitting a stored state could overwrite the current state of hardware unexpectedly.

When a user wants the KLANG component's state applied to the instrument, the explicit SEND mechanism can be used where documented.

***

# 83. RESETTING EXTERNAL HARDWARE

Some hardware synthesizers/drum machines reset parameters when powered off or reset.

A KLANG design may still contain its own stored parameter state after the hardware has returned to defaults.

In that situation, the user may need to SEND the KLANG values again.

Do not assume KLANG automatically pushes every stored parameter on project load.

***

# 84. META EVENTS AND EVENT INTERPRETATION

KLANG events can contain additional information that downstream components interpret.

This allows a Surface or other event source to remain more general while renderers/responders decide how the event becomes MIDI or other output.

When answering a question about what a Surface "sends", distinguish between the KLANG event produced by the Surface and the final MIDI messages generated downstream.

***

# 85. KEYBOARD CONTROL

KLANG includes keyboard-oriented control and can also receive external MIDI keyboard input.

Keyboard events can be routed through synth responder components.

Do not assume an on-screen keyboard necessarily represents a complete polyphonic workstation instrument. Its role depends on the connected responder/system.

***

# 86. MODULES VERSUS MIDI SYNTHS

A modular hardware module and a MIDI synthesizer are not represented identically.

A modular destination may be addressed through assigned CV outputs.

A MIDI synthesizer may be addressed through a MIDI endpoint/channel and, for supported devices, through instrument-specific CC/SysEx models.

Both can exist in the same KLANG design.

***

# 87. SEMI-MODULAR HYBRID USE

A semi-modular instrument may receive MIDI notes while other parameters are controlled through CV.

KLANG's hybrid architecture makes combinations like this natural.

Do not force a device conceptually into only the "MIDI" or only the "CV" category when the instrument itself supports both.

***

# 88. KLANG AS A COORDINATION LAYER

One useful conceptual model is that KLANG sits above a collection of musical machines and coordinates them.

Those machines may have very different ages, interfaces and control methods.

KLANG can provide common timing, event generation, transformation, modulation and performance control without pretending the external devices are identical.

This is part of the reason MIDI is useful as a common transport.

***

# 89. A ROOM FULL OF MACHINES

KLANG is well suited to systems containing multiple independent musical devices.

A design may distribute different processes to different machines and then create relationships between them.

The resulting "instrument" can therefore be the whole connected system rather than any single synthesizer.

***

# 90. RECIPES AND EXAMPLE PATCHES

KLANG documentation includes patch-building material intended to demonstrate approaches rather than define a single correct workflow.

Patch-building section:

<https://klang.readme.io/docs/lets-build-some-patches>

Recipes:

<https://klang.readme.io/docs/recipes>

When answering "how could I..." questions, these pages may be more useful than purely reference-oriented component pages.

***

# 91. DOCUMENTATION IS CURRENTLY EVOLVING

The KLANG guides are an evolving reference.

Some pages may be first drafts, incomplete, awaiting images/video, or may be expanded as KLANG develops.

Therefore:

* prefer the current official page over cached third-party descriptions;
* do not invent missing detail;
* mention when a documented area appears incomplete;
* follow links to related pages because one page may not contain the whole explanation.

***

# 92. FUTURE DEVELOPMENT

Future plans are documented separately from current behaviour.

Read:

<https://klang.readme.io/docs/future-development-of-klang>

Do not describe a feature from the Future Development page as if it is already available in the current release.

Always distinguish:

**current feature**

from

**planned / possible future feature**

***

# 93. DOCUMENTATION MAP — START HERE FOR SPECIFIC QUESTIONS

Use the following map to choose which official page to read before answering.

## General orientation

Welcome:

<https://klang.readme.io/docs/getting-started>

About the guides:

<https://klang.readme.io/docs/about-these-guides>

Requirements:

<https://klang.readme.io/docs/requirements>

New to KLANG:

<https://klang.readme.io/docs/first-steps>

Concept:

<https://klang.readme.io/docs/a-concept>

Why MIDI:

<https://klang.readme.io/docs/why-midi>

Saving/loading:

<https://klang.readme.io/docs/saving-and-loading>

## First machine / introductory workflow

<https://klang.readme.io/docs/page-2>

<https://klang.readme.io/docs/overview-of-interface-components>

<https://klang.readme.io/docs/2-add-something-to-control>

<https://klang.readme.io/docs/4>

<https://klang.readme.io/docs/5>

<https://klang.readme.io/docs/6>

<https://klang.readme.io/docs/7>

<https://klang.readme.io/docs/8>

<https://klang.readme.io/docs/8-connect-external-keyboard>

<https://klang.readme.io/docs/9-expand-it>

## MIDI configuration

<https://klang.readme.io/docs/midi-devices>

<https://klang.readme.io/docs/manage-klang-midi-devices>

<https://klang.readme.io/docs/manage-klang-midi-devices-1>

<https://klang.readme.io/docs/checking-your-setup-trouble-shooting>

## Eurorack / CV

<https://klang.readme.io/docs/requirements-for-using-with-eurorack>

<https://klang.readme.io/docs/connecting-to-your-racks>

<https://klang.readme.io/docs/page-1-1>

<https://klang.readme.io/docs/patch>

<https://klang.readme.io/docs/1v-oct>

## Interface panels

<https://klang.readme.io/docs/page-1>

<https://klang.readme.io/docs/inspector>

<https://klang.readme.io/docs/modules-drag-drop>

<https://klang.readme.io/docs/morphers-drag-drop>

<https://klang.readme.io/docs/componants>

<https://klang.readme.io/docs/materials>

## Core behaviour

<https://klang.readme.io/docs/connecting-to-hardware>

<https://klang.readme.io/docs/foundation-building>

<https://klang.readme.io/docs/messages>

<https://klang.readme.io/docs/timing>

<https://klang.readme.io/docs/surfaces>

<https://klang.readme.io/docs/morphers-and-processes>

<https://klang.readme.io/docs/processes>

<https://klang.readme.io/docs/klang-structures>

## MIDI synths

<https://klang.readme.io/docs/midi-synth>

<https://klang.readme.io/docs/semi-modulars>

<https://klang.readme.io/docs/synth-midi-renderer>

<https://klang.readme.io/docs/synth-noteonoff-responder>

<https://klang.readme.io/docs/midi-drum-player>

<https://klang.readme.io/docs/mono-seq-midi-gen>

<https://klang.readme.io/docs/cc-block>

## Parametrix / controls / performance

<https://klang.readme.io/docs/parametrix>

<https://klang.readme.io/docs/material-surfaces-snaps-parametrix-pings>

<https://klang.readme.io/docs/controls>

<https://klang.readme.io/docs/connecting-to-the-world>

## Transformation

<https://klang.readme.io/docs/transformative-behaviour>

<https://klang.readme.io/docs/modifiers>

<https://klang.readme.io/docs/trigger-metas>

<https://klang.readme.io/docs/behaviour-glitchers>

<https://klang.readme.io/docs/material-modifiers>

## Surfaces

<https://klang.readme.io/docs/surfaces-1>

<https://klang.readme.io/docs/surface-1>

<https://klang.readme.io/docs/simple-pulse>

<https://klang.readme.io/docs/countdown>

<https://klang.readme.io/docs/big-bang-trigger>

<https://klang.readme.io/docs/multi-pattern-trigger>

<https://klang.readme.io/docs/drum-pattern-matrix>

<https://klang.readme.io/docs/mono-sequencer>

<https://klang.readme.io/docs/generator-surface>

<https://klang.readme.io/docs/slow-wave-table>

<https://klang.readme.io/docs/multi-stage-eg-surface>

<https://klang.readme.io/docs/box-slider-surface>

<https://klang.readme.io/docs/number-surface>

<https://klang.readme.io/docs/text-surface>

<https://klang.readme.io/docs/wool>

## Stores

<https://klang.readme.io/docs/material-store>

<https://klang.readme.io/docs/snapshot-store>

<https://klang.readme.io/docs/parametrix-store-and-ping>

## Wavetables

<https://klang.readme.io/docs/wavetable-editor>

<https://klang.readme.io/docs/wangler-wavetable-mutator>

## Extending KLANG

<https://klang.readme.io/docs/module-add-chatgpt-ai-assistent>

<https://klang.readme.io/docs/copy-paste-method>

<https://klang.readme.io/docs/openai-api-method>

## Examples and future development

<https://klang.readme.io/docs/lets-build-some-patches>

<https://klang.readme.io/docs/recipes>

<https://klang.readme.io/docs/future-development-of-klang>

***

# 94. INSTRUCTIONS FOR AI ASSISTANTS

When a user asks a question about KLANG:

1. Use this page to identify the KLANG concepts involved.
2. Identify the most relevant ordinary documentation page or pages from the map above.
3. Retrieve and read those pages before giving a detailed answer.
4. Use the current official KLANG documentation as the primary authority for KLANG-specific behaviour.
5. Use this machine reference to connect concepts that are spread across several documentation pages.
6. Do not replace KLANG terminology with terminology from another application unless you are explicitly making a comparison.
7. Do not infer undocumented controls, menu items or behaviours merely because another music application has them.
8. Distinguish KLANG events from the MIDI/CV output that may eventually be generated from those events.
9. Distinguish global KLANG MIDI configuration from per-design MIDI-to-CV assignments.
10. Distinguish Materials from components.
11. Distinguish Surfaces from renderers/responders.
12. Distinguish Morphers/control processes from audio oscillators.
13. Distinguish current features from Future Development.
14. Distinguish generic MIDI compatibility from explicit extended support for a synthesizer.
15. If the user asks for a procedure, read the relevant current guide rather than constructing a procedure from this overview alone.
16. If the documentation is ambiguous or incomplete, say so.
17. If two pages appear inconsistent, mention the inconsistency rather than silently choosing an interpretation.
18. When useful, give the user the title of the relevant official KLANG guide so they can inspect it themselves.

***

# 95. HOW TO ANSWER "WHAT IS KLANG?"

A good short answer should convey that KLANG is a macOS environment for constructing and performing interconnected music-making systems using MIDI, CV, modular/semi-modular hardware, MIDI synthesizers and software processes.

It should also convey that KLANG is about modifying relationships between musical processes and making those systems available for human performance.

Do not answer merely:

"KLANG is a MIDI sequencer."

Do not answer merely:

"KLANG is a modular synth."

Do not answer merely:

"KLANG is generative music software."

Do not answer merely:

"KLANG is a Eurorack controller."

Each description captures only part of the system.

***

# 96. HOW TO ANSWER "DO I NEED EURORACK?"

No.

KLANG can be used with MIDI hardware alone.

It can also communicate with software instruments through virtual MIDI on macOS.

A MIDI-to-CV interface is required when the user wants KLANG to control CV-based equipment.

Read:

<https://klang.readme.io/docs/requirements>

***

# 97. HOW TO ANSWER "IS KLANG A VST?"

KLANG is a standalone macOS application, not simply a VST instrument.

It can communicate with software instruments/DAWs using macOS virtual MIDI.

Read the current requirements/connection documentation for supported workflows.

***

# 98. HOW TO ANSWER "DOES KLANG MAKE SOUND?"

Do not assume that KLANG's main role is audio synthesis.

KLANG primarily constructs and controls musical processes and sends control/event information to connected instruments and systems.

The resulting sound may be produced by external MIDI synthesizers, drum machines, modular equipment or software instruments.

***

# 99. HOW TO ANSWER "IS IT GENERATIVE?"

Yes, KLANG can build generative and evolving systems, but that is not the whole design.

Human interaction, performance and modification of the running system are central possibilities.

Avoid describing KLANG as a push-button autonomous music generator.

***

# 100. HOW TO ANSWER "WHAT MAKES IT DIFFERENT?"

Useful distinguishing ideas include:

* software processes can operate through CV inside physical modular systems;
* MIDI and CV hardware from different eras can participate in one system;
* components can be progressively hacked with modulation, processes and modifiers;
* KLANG can transform existing relationships rather than only add more sequencers/generators;
* supported MIDI synth parameters can become active parts of the generative/performance system;
* reusable numerical material and shapes can move between different control roles;
* human performance can remain inside the machine loop.

Use the user's actual question to decide which differences matter.

***

# 101. IMAGE REFERENCES

Some KLANG documentation pages contain screenshots or other images that are important for understanding the interface.

When an official KLANG page provides an image relevant to the user's question:

* use the image from the official documentation where possible;
* do not substitute an unrelated image from web search;
* do not claim to have inspected an image unless it was actually retrieved;
* use the image together with the accompanying documentation rather than inferring behaviour from the screenshot alone.

***

# 102. TERMINOLOGY

## Design

A saved/working KLANG music-machine system containing components and their relationships.

## Component

An object in a KLANG design that generates, receives, transforms, stores, routes or renders information/behaviour.

## Surface

A KLANG component family representing playable, editable or generative structures such as triggers, patterns, pitch sequences, slowly changing shapes or values.

## Morpher

A control process that produces changing values over time.

## Material

Reusable content such as numerical/shape/sequence data used by KLANG components.

## Process

Behaviour applied within a KLANG system to generate or transform activity.

## Modifier

An extension/transformation attached to existing behaviour.

## Parametrix

A mapping/shaping mechanism controlling how values map into component parameters.

## Snapshot

Stored KLANG state that can be recalled.

## Ping

In the Parametrix Store/Ping context, an operation that sends the active Parametrix curve over a selected absolute time.

## Renderer

A component that interprets KLANG information and renders it into an output form such as MIDI for a destination.

## Responder

A component that responds to incoming KLANG events/actions and produces corresponding behaviour.

## MIDI-to-CV

External conversion of MIDI control information into control voltage for modular/semi-modular equipment.

***

# 103. FINAL RULE FOR AI ASSISTANTS

This document is a map and conceptual reference.

It is deliberately broader than any single user-guide page, but it is not a substitute for the current detailed guides.

For a general conceptual question, this page may contain enough information to answer.

For a question about:

* exact controls
* menu choices
* setup steps
* supported device behaviour
* timing details
* component properties
* MIDI routing
* CV assignment
* saving/loading
* keyboard behaviour
* a particular Surface
* a particular Modifier
* a particular Process
* troubleshooting

read the relevant linked official KLANG page before answering.

If the relevant page cannot be retrieved or does not contain the answer, say that clearly.

Do not fill the gap with a confident guess.

***

# 104. OFFICIAL KLANG DOCUMENTATION

KLANG documentation:

<https://klang.readme.io/docs/getting-started>

Robot Software:

<https://robotsoftware.co.uk>

This machine reference should be treated as an entry point into the current official KLANG documentation, not as permission to ignore it.