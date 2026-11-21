---
name: orbit
description: Start, view, or stop the Orbit desktop usage tracker; compare the signed-in Codex account's remaining allowance with its full-period target and review recorded history. Requires local desktop execution. Not API billing or phone/cloud synchronization.
---

# Orbit

Resolve `../../scripts/pace.mjs` relative to this skill folder. It is the plugin's bundled controller; run it with Node.js 22+ and one argument: `start`, `status`, `stop`, `enable-startup`, or `disable-startup`. Use a properly quoted absolute path. The script locates the user's Codex CLI and reads its signed-in ChatGPT account. Do not read credential files or ask for tokens.

For “start Orbit”, setup, or opening the dashboard, run `start`. This starts a background local tracker that reads usage every minute until stopped or the computer shuts down. Explain that behavior briefly, then open its returned loopback URL in the available browser. If browser opening isn't available, provide the URL. Never substitute the publisher's private Orbit website.

For a pacing or usage question, run `status` once. If stopped, say so; do not start ongoing tracking merely to answer a one-time question. If running with a fresh reading, use returned bucket values and reset time. Target remaining is `100 × clamp((reset − now)/(windowMinutes × 60000), 0, 1)`. Target used is 100 minus target remaining. Compare actual remaining minus target remaining in percentage points. The target always runs from 100% at the window's start to 0% at reset, independent of the current balance or optional reserve. Separate measured values from calculated targets. State source time and any stale/error status.

For “stop Orbit”, run `stop`; this preserves recorded history. Do not remove histories unless the user asks. Updates record actual observations only, account-separated on the user's computer. Missing time is not reconstructed. History and preferences are not synchronized to phones or other computers.

If Node.js or Codex CLI is missing, explain the missing prerequisite. Follow the host's installation rules; do not silently install or sign in. If no ChatGPT account is signed in, ask the user to sign in through the normal Codex CLI flow, then try again. Never run a prompt, consume reset credits, change accounts, publish data, or alter the user's hosted website as part of this skill.

This is a local companion for personal account usage. Do not claim commercial integration approval or hosted access. On hosts without local execution, explain that the desktop plugin is required.

## Optional Windows startup
Only when the user explicitly asks to start Orbit automatically after restart/sign-in, run `enable-startup`. Explain that this installs a per-user Windows Startup launcher and copies the runtime into the PacePlugin data folder. It checks usage with the dashboard closed and recovers when the tracker exits. No administrator access is required. Startup is off by default. Do not enable it merely for a normal Start Orbit request.

Run `disable-startup` when asked to remove automatic startup. This removes the launcher; it does not delete history or stop an already running tracker. Use `stop` too when the user asks to stop tracking. Stop pauses tracking until Start Orbit or the next Windows sign-in if startup remains enabled. No startup support is claimed for macOS/Linux.

Day shows consecutive 24-hour blocks anchored to the usage reset. Week shows the full period. Dotted blue connectors show the change between real readings across gaps, not measured usage timing. Never describe interpolated lines as actual historical observations.
