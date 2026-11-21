# Dispro 0.1.0-rc.8

**Release candidate. Public directory release is pending.**

Build a small audio-plugin scaffold and distinguish working evidence from
unrun release gates. Free by Kaizen Strategic AI Inc.

Use the `build-audio-plugin` skill to scope an effect, generate the original
mono LV2 gain example, or review release evidence. The portable scripts need
Python 3.10+; native builds also require macOS/Linux with `/usr/bin/cc`.

New plugin/DSP work starts with a visual mockup and explicit visual approval
before implementation. The unchanged gain example can still be exercised
directly. Delivery repairs preserve approved sound/UI. The skill now includes
18 general engineering lessons and a release worksheet covering lifecycle,
state, latency, provenance, signing, entitlements and fulfilment. These are
descriptive checklists, not additional DSP/runtime or platform implementations.

For an easier first brief, follow `references/guided-setup.md` inside the skill.
It asks only missing sound/control/target choices and makes assumptions visible.
The companion parameter/state, realtime safety and audio-comparison references
provide focused worksheets when needed. They are original general guidance;
no third-party skill code, product algorithm or universal performance promise
is included. The available runtime remains the fixed gain example.

From `skills/build-audio-plugin/scripts`, substitute an actual new output path:

```sh
python3 -m dispro --workspace /absolute/new/dispro-work init
python3 -m dispro --workspace /absolute/new/dispro-work scaffold first-gain
python3 -m dispro --workspace /absolute/new/dispro-work run first-gain --timeout 30
```

Use a dedicated directory with no symlink ancestors. The pipeline verifies its
fixed recipe, builds one C file, validates the exact binary offline and creates
an LV2 bundle ZIP with a stage/hash receipt. Generated bundles are never
installed. Native testing in this release was macOS arm64 only. Linux is
implemented but unverified; Windows native compilation is unsupported.

The original gain example has one mono input/output and a linear 0–2 gain
control, with no UI, MIDI, smoothing or state extension. It is a teaching
example; sudden gain changes can click. Modified recipes are refused by the
trusted runner and require a separate reviewed implementation path.

ChatGPT web/mobile can use the skill and provide source/commands or a local
handoff. The package does not grant access to the user's local computer. A
sandbox offered by the host is a separate runtime. Do not give anyone keys or
account credentials to use Dispro.

If this package contains `mcp.json`, it is the optional **Dispro Local** variant
for a host supporting stdio MCP, `${PLUGIN_ROOT}` and `${PLUGIN_DATA}`. It adds
five narrow tools: scaffold, start, status, cancel, receipt. Installing or
configuring it is an explicit operator action; unpacking creates no persistent
access. One job runs at a time, with a 1–60 second limit. Ctrl-C or `cancel_job`
cancels owned work. The public skills variant has no MCP connection.

DAW playback, automation, recall, signing, notarization and publishing remain
separate gates. No automatic release or credential handling is implemented.
See the skill's `references/release-gates.md` and `docs/SECURITY.md`.
Use `references/engineering-lessons.md` and `references/release-checklist.md`
inside the skill for applicable checks and evidence limits. Historical Windows
teardown reports and source/mock checks do not establish current GUI/unload
acceptance; an unconsumed `JUCE_DIRECT2D` define is not a fix. The known Logic AU
bypass-transition case remains unresolved. No proprietary product code or
internal source-evidence files are included.

First-party toolkit code is free to use under its proprietary LICENSE. Generated audio plugins may be modified, distributed and sold under OUTPUT-LICENSE.txt. No toolkit modification or redistribution grant is provided. The LV2 core header remains ISC licensed with
preserved notices; see `docs/vendor-provenance.json`. JUCE/AAX/ASIO are not
included. `PACKAGE-SHA256.json` inventories every other file in this archive.
This package does not itself prove public-directory approval or publication.

Support: support@kaizendsp.com. You may modify, distribute and sell generated audio plugins under OUTPUT-LICENSE.txt, including commercial closed-source plugins. The reusable Dispro toolkit stays proprietary under LICENSE; independently authored user materials keep their existing rights.

The original fixed runtime has also been exercised through the installed skill
and an authorized Codex local runtime: real C compilation, native offline LV2
loading/audio checks and exact package verification passed on macOS arm64. This
is distinct from DAW/GUI acceptance, web/mobile invocation and persistent MCP
installation. No additional platform support is inferred. The skill's
`references/platform-release-review.md` covers asset staging, per-architecture
floors/preflight, separate signature systems and exact publication approval scope.
