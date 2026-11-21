# Platform scope and documented limits

Checked October 2, 2026. This is original workflow guidance with official source links, not a compatibility certification or catalog of MIDI Monsters products. Recheck the installed version and exact device before operational advice.

## Traktor: the core workflow

Use Controller Manager for mapping diagnosis, input/output assignments and reversible changes. Keep the exact product's installation instructions authoritative for import choices. A mapping can involve multiple devices intentionally, so distinguish accidental duplicate imports from a documented multi-device design. Choose the actual controller ports and verify input and feedback independently. The official [generic controller setup](https://support.native-instruments.com/support/solutions/articles/69000879394-how-to-set-up-a-generic-midi-controller-in-traktor) and [Controller Manager overview](https://support.native-instruments.com/support/solutions/articles/69000879471-how-to-use-the-controller-manager-in-traktor) support this workflow. Confirm the installed Traktor release and controller firmware before naming a command or certifying a result.

## rekordbox: documented MIDI Learn help

The [rekordbox 7 MIDI LEARN Operation Guide, file edition 7.0.5](https://cdn.rekordbox.com/files/20241203210623/rekordbox7.0.5_midi_learn_operation_guide_EN.pdf), printed pages 1–7, documents Performance-mode mapping for USB-connected MIDI equipment. Select the intended device, export its existing settings, then add and learn one available function. Check deck and control type. Imports overwrite the selected device's current settings; closing the window saves edits. Indicator output needs its own MIDI OUT code. The guide says AlphaTheta does not provide configuration support for third-party products. Do not promise that every controller function can be mapped or that Traktor modifier logic transfers.

Check the current [plans](https://rekordbox.com/en/plan/), [Hardware Unlock list](https://rekordbox.com/en/support/hardware-unlock/) and exact feature documentation. General MIDI Learn availability does not unlock every paid feature. For example, the [version 7 STEMS FAQ](https://rekordbox.com/en/support/faq/stems-7/#faq-72377) conditions hardware assignment on a supported plan or Hardware Unlock device. If the UI or entitlement is unclear, ask for the relevant settings screenshot rather than recommending a purchase by guesswork.

## Serato: DJ Pro guidance, with hardware limits

MIDI Assign is a [DJ Pro feature, absent from the Lite comparison](https://serato.com/upgrade). Establish the exact software edition and supported primary hardware first. A secondary controller does not by itself establish a usable, licensed DJ setup.

Use [MIDI mapping with Serato DJ Pro](https://support.serato.com/hc/en-us/articles/209377487-MIDI-mapping-with-Serato-DJ-Pro), especially “Remapping your primary Serato DJ hardware,” “Save your preset,” and “Current limitations.” Preserve the current preset before editing. Supported primary hardware requires its per-device remapping option; secondary devices and accessories have their own eligibility. Create a new preset before making the intended mapping, not after unsaved work, because New clears the current settings. Test one assignment and save it. Restore Defaults affects every device in that preset, so it is not a first troubleshooting step. Jogwheels/platters, input switches, Shift and Performance Pad Mode buttons are excluded from the documented remapping controls. Some accessories cannot be remapped at all.

The separate [MIDI Platters reference](https://support.serato.com/hc/en-us/articles/225065788-MIDI-Platters) confirms that arbitrary user mapping cannot drive the virtual deck platter. Use supported native hardware or a documented alternative; do not offer a hidden mapping workaround. Do not imply a Traktor TSI becomes a Serato preset by conversion or renaming.

## Engine DJ: compatibility triage only

First distinguish Engine DJ Desktop, Engine OS standalone operation, and a Denon/Numark unit controlling laptop software. These are different targets. The [Desktop 5.1.0 guide](https://cdn.inmusicbrands.com/engine/51/Engine%20DJ%20-%20User%20Guide%20-%20v5.1.0.pdf), “About Engine DJ,” describes preparing a library for Engine OS hardware. The reviewed guide does not document a general MIDI Learn editor. The [downloads page](https://enginedj.com/downloads) separates Desktop and OS releases.

Therefore this release does not offer Engine custom mapping procedures or claim arbitrary MIDI-controller support. That is an evidence boundary, not a claim that no future version or supported accessory can work. Denon's [LC6000 FAQ](https://support.denondj.com/en/support/solutions/articles/69000809994-denon-dj-lc6000-prime-frequently-asked-questions) documents specific standalone pairings and separate computer-software support. Retrieve the current device manual and compatibility list for the user's exact pairing. A MIDI specification or a successful Traktor mapping for Denon hardware does not establish that Engine OS can import that map.

## Practical answer format

Give the verified scope, one reversible next step, the expected observation and the source section. Label hardware-tested results only when actual test evidence exists. If official sources cannot answer the exact pairing or control, say what remains unknown and provide the relevant manufacturer support route. Do not invent a MIDI Monsters product to fill that gap.
