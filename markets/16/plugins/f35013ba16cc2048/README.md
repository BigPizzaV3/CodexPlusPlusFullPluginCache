# reverse engineering anything

An independent, skills-only companion for planning and interpreting authorized work with [REA: Reverse Engineer Anything](https://github.com/morluto/rea).

This package does **not** contain REA's implementation, binaries, MCP server, or analysis engines. It cannot inspect a target by itself. A host must already expose the relevant REA tools, or the user must run the documented REA CLI locally. The upstream project is independently maintained; this companion is not affiliated with or endorsed by its maintainers.

## Included skills

- `rea-analysis-companion`: route and coordinate an investigation.
- `rea-readiness-and-setup`: diagnose tools and prerequisites without silently changing configuration.
- `rea-evidence-and-reporting`: keep observations, inferences, and unknowns distinct and traceable.
- `rea-native-and-managed-artifacts`: scope native binary, package, .NET, and crash investigations.
- `rea-javascript-electron`: inspect static JavaScript/Electron artifacts and trace features.
- `rea-browser-and-network`: plan passive browser/Electron observation and interpret retained captures carefully.
- `rea-mobile-and-firmware`: route Android and firmware work to the proper prerequisites and safe boundaries.
- `rea-specialized-formats`: handle ELF layouts, EVM bytecode, process captures, and other specialized inputs.
- `rea-runtime-safety`: gate target execution, interaction, and handling of untrusted files.

## Upstream source and license

Workflow architecture was adapted from the public `morluto/rea` project and its `skill-src/reverse-engineer-anything/SKILL.md`, README, documentation, and security policy, observed on 2026-10-09. The upstream repository declares MIT licensing. Its copyright and license notice are included in `LICENSE`; see `THIRD_PARTY_NOTICES.md` for attribution and scope. This companion is a separate integration guide, not a copy of the REA software distribution.

## Safety and limitations

- Work only on targets for which the user has authorization.
- Do not help bypass access controls, defeat DRM/licensing, steal credentials or secrets, deploy malware, evade detection, or exploit third-party systems.
- Opening an untrusted binary delegates parsing to the selected local analysis provider. REA is not a sandbox; same-user processes are outside its security boundary.
- Runtime tasks may execute or interact with the selected target using the user's permissions. Keep the target and requested lifecycle narrow; do not infer consent to install dependencies or change configuration.
- REA analyzes locally, but resulting tool output is sent to the model provider under that provider's data policy. Avoid uploading proprietary artifacts or sensitive findings unless allowed.
- Static evidence does not prove runtime behavior. Every report must identify evidence, inference, coverage boundary, and unresolved unknowns.

## Public-directory state

This source package is not a public listing or an OpenAI approval. A public submission also needs verified listing URLs, publisher identity, dashboard scans and attestations, and review approval. A skills-only plugin has no demo or MCP test cases. See `docs/publication-readiness.md` for the current preparation ledger.
