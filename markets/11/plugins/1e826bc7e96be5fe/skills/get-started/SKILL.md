---
name: ExaMedix Reach setup
description: Help users securely connect an ExaMedix Reach account and an authorized Windows computer.
---

# ExaMedix Reach setup

Use Reach only with Windows computers that the user owns or is expressly authorized to administer.

1. Ask the user to connect their ExaMedix Reach account using the normal ChatGPT OAuth flow, then call `list_devices`.
2. If an authorized computer is online, proceed with the requested workstation task using the least privileges necessary.
3. If no computer is online, direct the user to the official setup guide at https://reach.examedix.ch/. The user completes the local Windows setup and device pairing themselves. Do not install software, invoke package managers, fetch executable scripts, or run setup code through ChatGPT tools.
4. Once the user confirms pairing and that the Windows Reach agent is running, call `list_devices` again to verify the intended computer is online.
5. Reach asks for local consent before enabling optional Power Mode. Power Mode is off by default. Never assume permission to enable command execution; the user manages this decision locally and must understand the consequences.
6. Reach supports authorized file and folder operations and blocks known credential stores, private keys, and common authentication secrets. Respect its local directory boundaries. Never suggest workarounds for a denied or blocked path.

Prefer read-only inspection before editing data. Obtain the user's permission for destructive changes or process termination when required. Do not provide or execute remote installer commands from this skill. For connection problems, direct the user to https://examedix.ch/reach/support/ or the product documentation.
