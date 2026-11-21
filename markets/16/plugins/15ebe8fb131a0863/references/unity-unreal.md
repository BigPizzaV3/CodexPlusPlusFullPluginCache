# Unity and Unreal workflows

Unity official docs: https://docs.unity.com/; versioned Editor documentation for Batchmode and builds. Confirm installed editor/hub, project version, build target and license before running.
- Use editor scripts, assemblies, scenes and serialization cautiously. `-projectPath` and `-quit` required in current build command docs; `-batchmode`, `-logFile` and target/profile recommended.
- One build target per batch invocation is generally safer; editor may need to restart to switch target.

Unreal official docs: https://dev.epicgames.com/documentation/en-us/unreal-engine/
- Inspect `.uproject`, plugins, Blueprints/C++ module state and toolchain. Use supported Unreal Automation Tool (UAT), build/cook/package automation only when installed and authorized.
- Never promise cross-platform binary builds or high-fidelity scenes when large engine toolchains and GPU are unavailable.

For both: baseline, focused diff, compile/import, targeted gameplay tests, truthful resource and licensing disclosure.
