---
name: rea-native-and-managed-artifacts
description: Plan authorized analysis of native binaries, libraries, package contents, managed .NET assemblies, Linux ELF layouts, or supplied crash cores using available REA providers.
---

# Native and managed artifacts

Use only user-supplied artifacts the user owns or is authorized to analyze. Before opening a target, state the format and question, check provider availability, and warn that the provider parses untrusted input with the user's permissions; it is not a sandbox.

## Route and scope

- For a native executable/library/database: open the exact path with `open_binary`; inspect the selected provider and active target before focused calls.
- For package member inventories, open only the supplied ZIP/APK/IPA/MSIX/AppX/DMG. Use artifact graph/findings only when they answer a named question.
- For managed PE/CLI assemblies, use static inspection and preserve metadata/CIL coverage and unresolved native boundaries.
- For offline Linux ELF layout, use `inspect_binary_layout` only when available and the target is an explicit ELF; preserve section/symbol/relocation evidence and static mitigation candidates.
- For an explicitly supplied Linux x86-64 core, use `inspect_recorded_crash`; read recorded notes/threads and raw evidence. Historical PIDs must never be used to select live processes.

## Avoid overreach

- Do not disable, bypass, patch, or remove licensing, access controls, anti-cheat, DRM, or integrity checks.
- Do not extract or disclose secrets, private keys, credentials, tokens, personal data, or proprietary information.
- Do not execute a binary merely to see what it does. If runtime evidence is necessary, explain target effects and request the exact target/lifecycle within a controlled, authorized environment.
- Do not save to or modify user-owned analysis databases or projects unless specifically requested and the tool's action is understood. Verify provider save semantics first.
- If output is partial, say so. Never report pseudocode as source or static mitigation hints as a full security verdict.

Report artifact identity, provider/version if available, evidence IDs, methods used, coverage, and the difference between observations and hypotheses.
