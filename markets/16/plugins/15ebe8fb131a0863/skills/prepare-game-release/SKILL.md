---
name: prepare-game-release
description: Package an editable game and verified builds for browser, desktop, mobile or game marketplaces with licensing and submission checks.
---

# Prepare Game Release


1. Confirm intended destination: source archive, browser demo, itch.io, Steam, app store, desktop executable, or private collaboration; no deployment/publishing without approval.
2. Read `../../references/release-and-compliance.md`; inventory source, engine and exact version, third-party assets/licenses, controls, rating/content obligations and dependencies.
3. Produce build/export only with verified engine, required templates/signing profiles and permission. For browser: include entrypoint and assets, check base paths, mobile browser constraints and server MIME behavior.
4. Verify launching the packaged artifact (not only the development server). Run applicable platform smoke tests, update licensing notices and give a README with controls.
5. Include `../../templates/evidence-report.md` with passed/failed/not run checks, environments and blockers. Never describe an unbuilt ZIP as an installed app or a hosted game.
6. Include production warnings for credentials, network services, analytics, store rules and underage audiences when relevant.

## Execution truth and safeguards
- A skill is an instruction workflow, not a remotely running game engine or a separately running AI agent. Inspect tools and repo state before claiming execution.
- Preserve existing projects, names, dependencies, save formats, and user work unless a change is explicitly requested. Obtain approval for deployment, payments, destructive edits, publication, and major third-party connections.
- Avoid reproducing protected commercial characters, levels, dialogue, soundtracks, logos, or copyrighted assets unless authorized. For assets, record origin and license. Read `../../references/security-and-rights.md`.
- Report what was implemented, what was actually run, what failed, and what remains unverified; never describe proposed tests as passed.
