# Evidence-backed release gates

Keep these separate for each exact artifact, format, OS and architecture:

1. Source identity and dependency rights.
2. Native build and offline contract/DSP validation.
3. Package extraction and exact payload/hash agreement.
4. Real host discovery, audio, parameters/automation and session recall.
5. Applicable signature, notarization, installer and rollback acceptance.
6. Publisher-approved immutable delivery and truthful support claims.

Dispro v0.1 automates only the first three for its original LV2 recipe. The
remaining gates stay unrun. Never infer Windows from Mac, physical Intel from
emulation, DAW playback from offline processing, or signing from a compile pass.
Retain failed evidence; a newer receipt does not erase it. Signing and publishing
are explicit later operations with separately authorized tools and exact hashes.
Dispro has no such endpoints and does not retrieve or provision credentials.

Use `release-checklist.md` for a per-candidate worksheet and
`engineering-lessons.md` for applicable lifecycle, state, latency, provenance,
licensing and fulfilment checks. Historical, source/syntax, mock, offline and
native-host evidence have different scopes. A unit-test count is not a GUI
teardown pass; a successful API-bypass fixture does not close a failing Logic
AU transition. The reviewed `JUCE_DIRECT2D=0` define was not consumed by the
pinned JUCE inputs and must not be presented as a proven D3D11 fix.

These references add guidance only. They do not add proprietary product code,
JUCE, platform implementations, browser runtimes, signing systems or licence
servers to the original LV2 recipe. Preserve the original notices and obtain
source-owner plus dependency-rights clearance before copying any implementation.

## SDK rights

The bundled LV2 core header is from LV2 v1.18.10 under ISC; retain its original
notices and the included `LV2-COPYING`. First-party Dispro toolkit code is proprietary and free to use under LICENSE. Users may modify, distribute and sell audio plugins containing the reference template and generated metadata under OUTPUT-LICENSE.txt, including closed-source commercial binaries. This does not permit redistribution of the reusable toolkit. Independently authored user materials retain their existing rights.
The reference bundle includes the generated-output licence and upstream ISC notices. No JUCE, AAX or ASIO code is bundled.

JUCE's applicable licence must be selected and satisfied before redistribution;
do not assume its commercial or AGPL option licenses proprietary products for
free. AAX SDK access, redistribution terms and signing/distribution requirements
need the developer's own Avid/PACE authorization. ASIO SDK versions/options have
their own terms; check the exact release and do not infer permission from an
installed SDK or another product's licence. ASIO is a driver interface, not a
plugin format. Dispro neither provides nor accepts those SDKs in v0.1.

Consult primary terms for the selected SDK/version before expanding the recipe:
- https://juce.com/legal/juce-8-licence/
- https://developer.avid.com/aax/
- https://www.steinberg.net/developers/
- https://github.com/lv2/lv2/tree/v1.18.10

The plugin-directory publication workflow is separate from releasing an audio
binary. A valid ChatGPT plugin ZIP still requires publisher verification,
published support/policy pages and applicable directory review/attestations.
