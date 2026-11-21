---
updatedAt: 2026-10-07T13:32:55.000Z
agentTools:
  projectIndex: https://klang.readme.io/llms.txt
---

# BOID_TROUBLE_SHOOTING_1

# KLANG TROUBLESHOOTING KNOWLEDGE 01 --- MIDI CONNECTIONS

KLANG\_KNOWLEDGE\_SOURCE

ID: KLANG-TROUBLESHOOTING-001 TYPE: TROUBLESHOOTING TOPIC: MIDI
connection, endpoint and device testing STATUS: CURRENT RELATION:
EXTENDS PURPOSE: Give another agent KLANG-specific troubleshooting
knowledge and prevent plausible but invented generic macOS/MIDI
troubleshooting from replacing KLANG's actual diagnostic workflow.

***

## INTERPRETATION RULE

This source is operational troubleshooting knowledge.

When a user reports a MIDI connection problem, prefer KLANG's direct
observable tests and the simplest physical explanations before proposing
operating-system, driver, CoreMIDI, sandbox or application faults.

Do not infer a complicated failure merely because a panel is empty.

Do not invent KLANG controls, menu locations, setup buttons, routing
behaviour or diagnostic procedures that are not established by the KLANG
corpus.

If exact UI location is not known, say what control the user needs to
find without inventing where it is located.

***

## MIDI SETUP OBJECTS

END\_POINT\_PANEL: role: represents/configures MIDI endpoints has\_control:
TEST troubleshooting\_use: directly test the endpoint

KLANG\_MIDI\_DEVICES\_PANEL: role: KLANG-level MIDI device configuration
has\_control: TEST troubleshooting\_use: directly test the configured
KLANG MIDI Device

IMPORTANT: Both panels provide a TEST function. Use these built-in tests
before constructing a temporary KLANG patch solely to establish whether
a MIDI connection exists.

***

## PRIMARY MIDI CONNECTION TROUBLESHOOTING ORDER

When a user says: - MIDI device is not visible - MIDI panels are empty -
drum machine/synth is not responding - "is it connected?" - "how can I
test it?" - endpoint/device setup appears not to work

CHECK IN THIS ORDER:

1. PHYSICAL\_EXISTENCE
   * Is the external hardware powered on?
   * Is the MIDI/USB connection physically plugged in?
   * If an external MIDI interface is involved, is that connected and
     powered as required?
2. END\_POINT
   * Inspect the End Point panel.
   * Use TEST.
   * Establish whether the MIDI endpoint itself is
     available/responding.
3. KLANG\_MIDI\_DEVICE
   * Inspect KLANG MIDI Devices.
   * Use TEST.
   * Establish whether the KLANG device configuration is
     communicating as expected.
4. ONLY AFTER BASIC TESTS FAIL
   * investigate the next appropriate layer
   * macOS visibility
   * interface/driver/device configuration
   * channel/routing/device-specific issues
   * other system faults where evidence supports them

RULE: simplest directly testable cause first.

***

## EMPTY PANEL CASE

SYMPTOM: End Point and/or KLANG MIDI Device panel appears empty.

DO\_NOT\_IMMEDIATELY\_CONCLUDE: - MIDIServer is frozen - CoreMIDI has
failed - KLANG lacks sandbox permissions - Bluetooth permission is
missing - Local Network permission is missing - Accessibility permission
is missing - third-party MIDI driver has crashed - KLANG project is
corrupt

FIRST\_QUESTION: Is the hardware actually connected and powered?

RATIONALE: An empty hardware-related view can have a trivial physical
cause. Escalating immediately to operating-system diagnosis creates
false complexity and can send the user away from the actual problem.

OBSERVED\_TEST\_CASE: A fresh AI instance was asked why both MIDI-related
panels were empty. It proposed MIDIServer failure, sandbox/security
gating and configuration problems. Actual cause: external drum machine
was not plugged in.

LESSON: KLANG troubleshooting knowledge must encode diagnostic order,
not merely architecture.

***

## "CAN I TEST ITS CONNECTED?" CASE

USER\_INTENT: Verify connection, not build a musical patch.

CORRECT\_KLANG\_NATIVE\_RESPONSE: - End Point panel has TEST. - KLANG MIDI
Devices has TEST. - use the relevant TEST function(s).

DO\_NOT\_DEFAULT\_TO: - add Simple Trigger - add Drum Pattern Surface - add
MIDI Drum Player - construct a temporary event chain - add a CC Block
and SEND values

WHY: Those components may be useful for later musical/function testing,
but KLANG already provides dedicated connection tests. A troubleshooting
answer should use the shortest native diagnostic path.

***

## TEST LAYERS

PHYSICAL\_LAYER: question: is the device physically present, powered and
connected?

ENDPOINT\_LAYER: tool: End Point panel -> TEST question: can KLANG
address/test the endpoint?

KLANG\_DEVICE\_LAYER: tool: KLANG MIDI Devices -> TEST question: does the
configured KLANG MIDI Device work?

MUSICAL\_PATCH\_LAYER: question: does the user's actual KLANG machine
produce the intended musical behaviour? only\_after: basic connection has
been established

DEVICE\_SPECIFIC\_LAYER: possible\_questions: MIDI channel expected note
pitches device mode supported CC/SysEx local device configuration
use\_when: connection exists but intended behaviour does not occur

SYSTEM\_LAYER: possible\_topics: macOS MIDI visibility interface drivers
CoreMIDI/system service use\_when: evidence indicates failure below KLANG
caution: do not speculate.

***

## TROUBLESHOOTING RESPONSE POLICY

When evidence is insufficient:

GOOD: "First check that the drum machine is powered and physically
connected. Then use TEST in the End Point panel. KLANG MIDI Devices also
has its own TEST."

BAD: "The empty panel means the macOS MIDIServer is frozen."

GOOD: ask for the result of the immediately preceding test.

BAD: provide a long tree of speculative operating-system repairs before
checking the physical connection.

GOOD: distinguish: connection test configuration test musical/event test

BAD: treat all three as the same problem.

***

## KNOWLEDGE-GAP RULE

If the user asks: "What exact button/menu do I press to open this
panel?"

AND this corpus does not establish the exact current UI path:

DO: state that the exact location is not established in the available
knowledge; use current KLANG documentation if available; or ask for a
screenshot if appropriate.

DO\_NOT: invent: - top-edge menus - toolbar positions - right-hand
inspector locations - "Add Device" buttons - panel names not established
by the corpus

A plausible UI description is still a hallucination if it is not
grounded.

***

## WHY THIS SOURCE EXISTS

This source was created from an agent-transfer test.

The test showed:

SUCCESS: the receiving agent absorbed higher-level KLANG concepts such
as: Surface/event abstraction renderer boundary MIDI endpoint concepts
global/per-design distinctions KLANG's simple-machine-then-hack
philosophy

FAILURE: when asked for concrete troubleshooting steps not contained in
the transferred knowledge, it filled gaps using generic expectations
about music software and macOS.

RESEARCH\_RESULT: conceptual product understanding does not automatically
produce reliable operational troubleshooting.

IMPLICATION\_FOR\_CORPUS: troubleshooting should be represented as
explicit knowledge: symptom first checks native tests diagnostic order
known failure modes escalation conditions prohibited unsupported
assumptions

Future troubleshooting sources can EXTEND this model for other KLANG
subsystems.

***

## INFERENCE EXAMPLES

CASE\_A: user: "Both panels are empty." response\_logic: physical
connection/power? -> endpoint TEST -> KLANG MIDI Device TEST ->
escalate only from observed result

CASE\_B: user: "The device is listed but I hear nothing." response\_logic:
connection existence is more likely established -> run TEST ->
distinguish endpoint/device success from patch behaviour -> then
investigate channel/note/device-specific configuration if necessary

CASE\_C: user: "Can I test the connection?" response\_logic: use built-in
TEST NOT build a temporary musical machine.

CASE\_D: user: "Where exactly is TEST?" response\_logic: if exact current
UI position is not present in corpus: do not invent it. obtain current
documentation/screenshot.

***

## CORE TROUBLESHOOTING AXIOM

OBSERVE -> TEST -> LOCALISE -> ESCALATE

NOT:

SYMPTOM -> IMAGINE LIKELY COMPUTER FAILURE -> GIVE REPAIR INSTRUCTIONS

END\_SOURCE