# Web & Mobile App Builder

A portable **skills-driven** OpenAI plugin for building and improving web, PWA, SwiftUI iOS/macOS, native Android and cross-platform apps.

## What it is
21 focused skills, 15 curated architecture/design/security references and 5 reusable templates. Natural-language requests route to platform-specific engineering workflows. The design references are curated starting points—not automatically installed packages or copied assets. Roles may delegate to *actual* subagents when a supported host exposes them.

## What it is not
This version has no hosted coding service, MCP endpoint or bundled App connection. It cannot guarantee local file access, Xcode, simulators, browser automation, subagents, live deployments or app-store approval. It tells the assistant to check capabilities and report real evidence. Packaging checks do not constitute product runtime tests.

## Example prompts
- "Build a polished PWA for organizing recipes. It should work offline and let me add recipes."
- "Build this iOS app in SwiftUI from my sketch; do not make it look like a web page."
- "Improve the dashboard UI in my existing React app without changing the APIs."
- "Review the accessibility and mobile UI of this site and fix the confirmed issues."
- "Create an Android-first habit tracker with Compose and meaningful empty/error states."

## Source tree
- `plugin.json`: public package metadata, onboarding skill and assets
- `skills/*/SKILL.md`: focused activation goals and procedures
- `references/`: platform guidance and user-supplied inspiration catalog
- `templates/`: specification, UI inventory, agent and verification reports
- `benchmarks/cases.json`: prompt/expectation cases, **not executed runtime tests**
- `scripts/validate_package.py`: deterministic integrity/quality checks

## Validation
Run `python3 scripts/validate_package.py` in this source directory. Review the output; this validates package structure and policy assertions only.

## Release status
Version 1.0.3 is a skills-only package; directory submission is a separate process. Submission to the public directory is a separate reviewed process and may be subject to skills-only listing eligibility.
