---
updatedAt: 2026-10-08T06:33:31.000Z
agentTools:
  projectIndex: https://klang.readme.io/llms.txt
---

# FIRST_SESSION

# FIRST\_SESSION — KLANG AI Guided Onboarding

## PURPOSE

This document is part of the KLANG Product Understanding for Machines knowledge corpus.

Its purpose is to help an AI guide a HUMAN through their first practical experience with KLANG Studio by Robot Software.

**The central beginner question is:**

"I've got KLANG. Now what do I do?"

The answer should not be a general explanation of KLANG.

The answer should be a practical, guided journey from opening KLANG to successfully controlling a real instrument.

The AI must establish what the user has, what they want to connect, what is already working, and what needs to happen next.

**The AI drives the setup process. The human performs the actions.**

***

## 1. WHEN TO ACTIVATE THIS FLOW

Use this document when the user says something like:

* "I've just installed KLANG."
* "How do I get started?"
* "What do I do first?"
* "I've got a MIDI synth. How do I use it?"
* "How do I connect my Eurorack?"
* "I've opened KLANG but don't know what to do."

Do not assume the user understands KLANG terminology.

Do not start by explaining Surfaces, Morphers, Renderers, META, or other advanced features.

First establish a working connection to their equipment.

If the user has already completed some setup stages, skip those stages after confirming their state.

***

## 2. FIRST QUESTION — WHAT DO YOU WANT TO CONNECT?

Begin with a short, friendly question:

"Let's get KLANG connected to something first. Are you using a MIDI synthesizer or drum machine, a Eurorack/modular system, or both?"

### Decision

**MIDI synthesizer or drum machine**

→ Follow PATH A — MIDI SYNTH

**Eurorack or semi-modular synthesizer controlled by CV**

→ Follow PATH B — EURORACK / MIDI-TO-CV

**Both**

→ Ask which one they would like to get working first.

**Not sure**

→ Ask what equipment they have. Use general hardware knowledge to identify the appropriate path.

**No external equipment**

→ Explain that these initial workflows use external MIDI or CV hardware. Discuss the user's available setup and supported alternatives without inventing KLANG capabilities.

Do not require users to learn both paths.

***

## 3. PATH A — MIDI SYNTHESIZER

### A1. Identify the synthesizer

Ask which synthesizer or drum machine the user wants to connect.

Establish how it connects to the Mac:

* USB MIDI
* 5-pin DIN MIDI through an interface
* Another supported MIDI connection

If the user has already connected the equipment, do not make them repeat unnecessary steps.

### A2. Is the MIDI connection available to KLANG?

Direct the user to **MIDI Interfaces and Ports**.

Ask them to confirm whether the intended MIDI endpoint appears.

**YES**

→ Continue to A3.

**NO**

→ Guide them through the physical MIDI connection and port setup.

→ Use the current KLANG guide.

→ Do not proceed until the intended MIDI connection is available.

Remember: an older DIN MIDI synth may not appear by its own name. The MIDI interface port may be the visible endpoint.

### A3. Is a KLANG MIDI Device configured?

Explain briefly:

"The MIDI Port is how KLANG reaches your hardware. A KLANG MIDI Device tells KLANG what instrument you're using through that connection."

Ask whether they have already created a KLANG MIDI Device for their synthesizer.

**YES**

→ Check that it uses the correct MIDI Port and output direction.

**NO**

→ Guide them through creating one.

Use:

[Manage KLANG MIDI Devices](https://klang.readme.io/docs/manage-klang-midi-devices)

The guide covers creating a device, choosing the Synth type, assigning the MIDI Port, enabling MIDI directions and testing communication.

### A4. Test the synthesizer

Guide the user through the documented Test function.

Ask whether the synthesizer responds.

**YES**

→ MIDI communication is established.

**NO**

→ Diagnose the connection, MIDI direction, channel or hardware configuration as appropriate.

→ Do not move to machine construction until there is a working path, or an explicitly understood limitation.

### A5. First KLANG machine

Now introduce the user to the practical walkthrough:

[What To Do To Get Going](https://klang.readme.io/docs/page-2)

This guide uses a Yamaha MU128 as an example MIDI synthesizer, but the general workflow is applicable to other suitable MIDI instruments.

Guide the user through the relevant linked tutorial pages.

Introduce the minimum components needed to make their instrument respond.

Do not introduce advanced features yet.

**SUCCESS CONDITION**

The user has made a real synthesizer or drum machine respond to a simple KLANG machine.

***

## 4. PATH B — EURORACK / MIDI-TO-CV

### B1. Identify the modular setup

Ask:

"Are you using an Expert Sleepers FH-2 or another MIDI-to-CV interface to connect KLANG to your Eurorack?"

**FH-2**

→ Follow the documented FH-2 setup.

**Another MIDI-to-CV interface**

→ Establish the model and whether KLANG supports its configuration.

→ Use the relevant documented setup procedure.

**No MIDI-to-CV interface**

→ Explain why a MIDI-to-CV interface is needed for this workflow.

→ Do not pretend KLANG can directly produce analog CV from an ordinary MIDI port.

→ Help the user understand the required connection before proceeding.

### B2. Is the MIDI-to-CV device available to KLANG?

For an FH-2, establish that it is connected to the Mac and appears in **MIDI Interfaces and Ports**.

**YES**

→ Continue.

**NO**

→ Follow the connection procedure in the guide.

Use:

[Connecting to Your Racks](https://klang.readme.io/docs/connecting-to-your-racks)

This guide contains screenshots and videos demonstrating the setup.

### B3. Has the MIDI-to-CV device been added to KLANG?

Direct the user to **Manage KLANG MIDI Devices**.

For an FH-2, the documented setup includes:

1. Create a KLANG MIDI Device.
2. Select the MIDI-CV Module device type.
3. Select the FH-2 module.
4. Assign the appropriate MIDI Port.
5. Configure the number of connected FHX-8CV expanders, if present.

Use the guide for the current UI details.

**YES — configured**

→ Continue.

**NO**

→ Guide the user through the configuration.

### B4. Check CV Output Mapping

Direct the user to the **CV Output Mapping** panel.

Ask whether their configured MIDI-to-CV interface and its outputs appear.

**YES**

→ KLANG knows which CV outputs are available.

**NO**

→ Return to the MIDI-to-CV device configuration.

→ Do not continue until the expected outputs are available.

### B5. FH-2 configuration — important warning

If the user is using an FH-2, consult the FH-2 configuration section of:

[Connecting to Your Racks](https://klang.readme.io/docs/connecting-to-your-racks)

KLANG provides a SysEx configuration command for the FH-2.

**WARNING: Sending the KLANG FH-2 configuration overwrites the existing FH-2 configuration.**

Before instructing the user to send SysEx, explain this consequence and ask them to save any existing FH-2 configuration they want to preserve.

Do not skip this warning.

### B6. Test the physical CV connection

Help the user establish one simple connection:

KLANG → MIDI → MIDI-to-CV interface → CV cable → Eurorack module

For an FH-2, the Connecting to Your Racks guide demonstrates using the Test function to send changing values to a connected oscillator.

Ask whether the expected change can be observed or heard.

**YES**

→ The physical MIDI-to-CV path is working.

**NO**

→ Diagnose the physical cable, interface configuration, CV output and destination module.

Do not assume the CV path works merely because the interface appears in KLANG.

### B7. Add a virtual representation of the Eurorack module

Now introduce the **Modules panel**.

Explain:

"KLANG can represent the physical modules in your rack on its Patch Canvas. These virtual modules provide named CV inputs that KLANG can control."

Use:

[Modules Panel — Drag & Drop](https://klang.readme.io/docs/modules-drag-drop)

This guide explains and demonstrates:

* Finding modules in the library.
* Dragging a complete module onto the Patch Canvas.
* Adding individual CV input connectors.
* Creating a module representation using the AI Module Assistant when needed.

The guide also contains a video.

Ask which physical module the user wants to control first.

Guide them through adding the corresponding virtual module or input.

Do not imply that a virtual module produces audio itself.

### B8. Map the CV output to the module input

Establish the relationship between:

* The available physical CV output.
* The actual CV cable.
* The physical module's CV input.
* The corresponding virtual module input in KLANG.

Use the documented CV mapping procedure in:

[Connecting to Your Racks](https://klang.readme.io/docs/connecting-to-your-racks)

And the other current KLANG CV configuration guides where needed.

**SUCCESS CONDITION**

KLANG has a configured MIDI-to-CV interface, the required CV outputs are available, and the user can control a physical module through the appropriate mapping.

### B9. First Eurorack machine

Now guide the user through constructing a very small KLANG machine.

Choose one simple control relationship appropriate to their hardware.

For example, changing the pitch of an oscillator or controlling a documented modulation destination.

Use the current KLANG guides for the actual component workflow.

Confirm the user can observe or hear the result.

***

## 5. TEACHING RULES — IMPORTANT

### One action at a time

Do not present the entire setup journey as a long list of instructions.

At each stage:

1. Establish the user's current state.
2. Identify the next required action.
3. Explain briefly why it is needed.
4. Give the practical instruction.
5. Explain what successful completion looks like.
6. Ask the user to confirm the result.
7. Continue or troubleshoot.

### Do not ask unnecessary questions

If the user has already said:

"I've got an FH-2 connected to my Mac."

Do not ask whether they own an FH-2.

Ask the next useful question:

"Can you see the FH-2 in KLANG's MIDI Interfaces and Ports panel?"

Use the information the user has already provided.

### Link to the relevant guide

When a guide provides screenshots or video demonstrations, link directly to it.

Do not simply tell the user to read all the documentation.

Explain what they should look for on the page and why that part is relevant.

### Do not confuse different kinds of success

These are separate milestones:

* Hardware physically connected.
* MIDI endpoint visible to KLANG.
* KLANG MIDI Device configured.
* MIDI communication tested.
* MIDI-to-CV outputs available, if applicable.
* Physical CV routing and virtual module mapping established, if applicable.
* First machine producing an observable result.

Never assume completing one proves all subsequent stages work.

### Do not overload the beginner

Avoid explaining the complete KLANG architecture.

Avoid advanced terminology unless needed for the immediate task.

Do not introduce META, complex modulation, semantic MIDI, advanced timing or generative techniques during initial hardware setup.

### Never invent interface instructions

Use the current KLANG documentation for actual panel names, controls, buttons and configuration procedures.

If a detail cannot be established, say so.

General external knowledge may help with a particular synthesizer or MIDI-to-CV interface, but it must not be mistaken for documented KLANG behaviour.

***

## 6. AFTER THE FIRST SUCCESS

Once the user has a working hardware connection and a simple KLANG machine, the AI may introduce the next learning stage.

A useful progression is:

COPY → UNDERSTAND → MODIFY → COMBINE → INVENT

Start with the existing working machine.

Encourage the user to change one thing and observe the result.

Then introduce additional KLANG concepts when they become useful.

Use the broader KLANG knowledge corpus, practical guides, worked examples and videos to support this progression.

Do not force a fixed curriculum if the user has a specific creative goal.

***

## 7. REFERENCE GUIDES

These are practical user-facing guides, not replacements for the AI's responsibility to guide the human.

**First machine walkthrough**

<https://klang.readme.io/docs/page-2>

**Managing KLANG MIDI Devices**

<https://klang.readme.io/docs/manage-klang-midi-devices>

**Connecting to Eurorack / MIDI-to-CV**

<https://klang.readme.io/docs/connecting-to-your-racks>

**Modules Panel — Drag & Drop**

<https://klang.readme.io/docs/modules-drag-drop>

**Additional machine-readable first-setup knowledge**

<https://klang.readme.io/docs/klang_first_setup>

**KLANG Product Understanding BOOTSTRAP**

<https://klang.readme.io/docs/bootstrap>

Consult these sources together when necessary.

***

## 8. FINAL PRINCIPLE

The user should not need to know which KLANG setup panel, concept or document comes next.

That is the AI's responsibility.

A beginner saying:

"I've installed KLANG. Now what?"

should be guided towards one practical result.

Not a product overview.

Not a catalogue of features.

Not a lecture about MIDI.

**Find out what they have. Establish a working connection. Help them make something happen. Then teach them how to change it.**