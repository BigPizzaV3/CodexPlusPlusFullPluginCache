---
name: rea-target-routing
description: Select the appropriate REA workflow and prerequisites for a supplied binary, archive, JavaScript/Electron app, web target, capture, Android package, firmware image, managed assembly, ELF, EVM bytecode, or process trace.
---

# REA target routing

Use the user's actual target and question. This is a routing guide, not a claim that REA tools are connected. Verify the installed REA version and live tool availability because main-branch documentation can exceed an older package.

| Target and question | Initial route | Important boundary |
| --- | --- | --- |
| Native executable/library/database | `open_binary`, then focused analysis; use `binary_overview` if advertised and useful | Select a supported provider; do not infer runtime behavior from static output |
| ZIP/APK/IPA/MSIX/AppX/DMG member inventory | `open_binary`; then `inspect_artifact` only if graph/findings answer the question | Inventory is not proof of behavior |
| JavaScript/Electron tree or ASAR | `analyze_javascript_application` | Static analysis needs Node.js/npm but no native disassembler; source completeness matters |
| Existing user-owned browser page | `list_browser_targets` | Do not open guessed URLs or access third-party systems without scope |
| Existing user-owned Electron runtime | `list_electron_targets` | Observe only the selected running app and requested flow |
| Retained HAR/mitmproxy capture | `inspect_web_network_capture` | Historical capture only; do not fetch captured URLs or claim live attribution |
| .NET managed PE/CLI assembly | `inspect_managed_artifact` | Static metadata/CIL is not runtime evidence |
| Android APK/classes/methods | `inspect_android_package`, then focused advertised Android tools | Requires host-specific JADX/JDK prerequisites; use only authorized APKs |
| Firmware image | `inspect_firmware_regions`; `extract_firmware` only if asked | Caller-supplied Binwalk/Unblob on supported Linux; output directory must be user-selected |
| Linux ELF section/symbol/relocation/static mitigation layout | `inspect_binary_layout` | Caller-supplied pwntools; offline operation, not a disassembler database |
| Linux x86-64 core dump | `inspect_recorded_crash` | Historical PIDs do not select live processes; parse recorded threads only |
| EVM bytecode in explicit raw/hex carrier | `inspect_evm_interface` | Select encoding; selectors/arguments/mutability are inferred; no chain lookup or execution |
| Process capture/run comparison | Use the process-capture workflow advertised by connected REA | Runtime commands have effects; restrict command, cwd, env, timeout, and expected lifecycle |

Do not call unavailable or unadvertised commands. If a tool reports a capability constraint, relay its exact reason and prerequisite rather than retrying a different target or silently installing software. For a target-free session, bind a caller-supplied target first when the tool requires it.
