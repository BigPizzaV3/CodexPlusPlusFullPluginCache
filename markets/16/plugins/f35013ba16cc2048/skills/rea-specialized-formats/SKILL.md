---
name: rea-specialized-formats
description: Handle focused REA workflows for ELF layout, recorded crashes, EVM bytecode, process runs, and other nonstandard carriers while preserving raw evidence and inference boundaries.
---

# Specialized formats

- **Offline ELF layout:** on a caller-supplied Linux ELF, use `inspect_binary_layout` only if advertised. It relies on caller-supplied pwntools, does not open a disassembler database, and may list static mitigation candidates. Preserve raw offsets, symbols, relocations, and coverage.
- **Recorded Linux x86-64 core:** use `inspect_recorded_crash` for the explicitly supplied core. Keep every recorded thread and raw note as evidence; historical PIDs are not live-process selectors. Optional mapping/debugger context requires an explicit relevant question.
- **EVM bytecode:** use `inspect_evm_interface` only on an explicit raw/hex carrier with caller-selected encoding. Preserve carrier and decoded digests. Selectors, inferred arguments, and mutability are candidates—not verified ABI or chain state. Do not perform chain lookups or execute transactions.
- **Process capture or run comparison:** inspect the live tool schema before use. It may execute a command and observe output, interactions, filesystem changes, or exit state with the user's permissions. Confirm the exact command, target, cwd, environment, limits, and intended effects first.
- **Other formats:** do not force a target into the closest route. Ask for the exact format and question, then consult current upstream documentation and live capabilities.

Never treat malformed input, missing dependencies, timeouts, or partial coverage as successful analysis. Explain the returned status and safest next step.
