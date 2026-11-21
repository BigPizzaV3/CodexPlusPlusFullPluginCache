# Fixed-recipe workflow

For new DSP, first complete the brief/mockup approval gate in `../SKILL.md`.
This runner remains limited to its unchanged gain example. The engineering
checklists do not add JUCE, browser UI, licensing servers or new build recipes.

The pipeline verifies original source bytes, snapshots them into a fresh run,
compiles one tiny C file with a fixed compiler command, loads the exact output
in a separate timeout-controlled offline host, then round-trips an allowlisted
ZIP. No downloads or model calls occur. Build output is not installed anywhere.

The offline host checks descriptor identity, instantiation, 0/64/257 sample
blocks, three sample rates, gain changes including clamping/nonfinite controls,
finite output and in-place operation. The reference input is synthetic and low
level. It opens no audio device. A successful run is not listening or DAW proof.

Each attempt writes `PROJECT/runs/RUN_ID/receipt.json`. Receipts identify source,
binary, bundle and archive hashes plus platform and unrun gates. Build receipts
are never overwritten by a later attempt. Reuse existing evidence; rerun only
for changed inputs or a concrete unresolved check. ZIP timestamps are fixed;
byte-identical native binaries across compiler versions are not promised.

The runtime accepts only a startup workspace and constrained project/run IDs.
It rejects symlinks, multi-linked input files, traversal, modified fixed recipes,
unknown tool arguments and overlapping MCP jobs. Child processes receive a
minimal environment, bounded output and a 1–60 second overall execution budget.
Only owned child process groups are cancelled. No raw compiler output or
environment is returned to the model; failure reports are deliberately coarse.

This is a local trusted-code tool, not a sandbox for adversarial native code.
Keep the workspace private to its operator. A malicious same-user process can
race filesystem checks; OS-level isolation would be a separate future feature.
No untrusted arbitrary source, hooks, build scripts, flags or compiler overrides
are accepted by v0.1. Do not loosen that boundary to make a modified project pass.

Native C compilers and operating systems can use their own system caches;
Dispro itself writes only under the dedicated workspace. It does not inspect
or terminate unrelated processes or use CI. Toolchain installation is separate.
