# Capability honesty and execution policy

This plugin is packaged skills, templates and references; **it does not run a hosted build backend or provision local Xcode, Android SDK, browser automation, simulator, subagents or remote credentials**.

- Before promising files/code/tests/deployments, inspect actual host tools, repository access and user authorization.
- If coding tools exist, implement real files and run available checks; do not stop at pseudocode when user asked to build.
- If environment lacks filesystem/terminal, give complete editable code or actionable file tree where supported, with precise disclosure about inability to build/run.
- If browser/simulator is unavailable, provide static design review only and mark visual/device verification NOT RUN.
- Real subagents only when host exposes them; otherwise follow orchestrator steps serially.
- Never assume a user's personal GitHub/Figma/Vercel access is connected. Ask for missing integration only when needed; do not simulate it.
- Preserve existing repo and user data, especially uncommitted changes. Do not commit, push, publish, deploy or spend without user approval.
