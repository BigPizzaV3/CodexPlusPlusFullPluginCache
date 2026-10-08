---
name: harbormaster
description: Diagnose local port collisions, identify the project or process holding a port, reserve ports, inspect service history, or safely free exactly one explicitly authorized local listener. Use for localhost conflicts, vanished dev servers, port ownership, reservations, and anti-killall process control.
---

# Harbormaster

Harbormaster is the anti-killall. It inspects local listeners, attributes them to projects, records service appearances and disappearances, and can free exactly one explicitly selected port.

## Surface gate

Before running any bundled command, confirm that this is a **local Codex task running on the computer whose ports the user wants to inspect**.

- In a supported local Codex task, say that Harbormaster will inspect the current computer, then begin with the smallest read-only command that answers the request.
- In ChatGPT, Codex cloud, or any other hosted or remote sandbox, do **not** run the bundled engine and do not describe sandbox listeners as the user's local ports.
- On an unsupported surface, explain: "Harbormaster inspects ports through a local Codex task on the computer you want to inspect. Hosted ChatGPT cannot see that computer's process table. Open Harbormaster in Codex on that machine and repeat your request."
- If the execution surface is ambiguous, state the requirement and ask the user to open the request in local Codex. Never infer that zero sandbox listeners means the user's computer has no listening ports.

## Locate the bundled engine

Use the plugin's bundled `../../scripts/harbormaster.py` relative to this skill directory. Resolve it to an absolute path before running it. Do not assume a separately installed `ports` command exists.

## Read first

Start with the smallest read-only command that answers the request:

- Harbor overview: `python3 <script> list`
- Development listeners only: `python3 <script> list --dev`
- Exact owner, agent-safe output: `python3 <script> who <port> --json --safe`
- Reservations and collisions: `python3 <script> reservations`
- Flight recorder: `python3 <script> history [port]`
- Setup diagnosis: `python3 <script> doctor`

Prefer `who <port> --json --safe` for Codex reasoning. Do not reveal full command lines or filesystem paths unless the user explicitly requests those details and they are necessary.

## Mutations are explicit

- Reserve only when the user asks: `python3 <script> reserve <port> <project> [--note ...]`.
- Remove a reservation only when the user asks: `python3 <script> unreserve <port>`.
- Before freeing a port, always run `who <port> --json --safe` and verify there is exactly one attributable holder.
- Explain which project and process will stop, then require explicit authorization to free it.
- Use interactive `free <port>` by default. Never add `-y` or `--force` unless the user explicitly asks for that exact override after seeing the owner evidence.
- If ownership is unknown, multiple holders exist, or the target looks like a system service, stop. Never guess.
- Never use `killall`, broad process-name termination, recursive cleanup, or unrelated service restarts.

## Dashboard

Launch `serve` only when the user asks for the dashboard. Keep it loopback-only (`127.0.0.1`) and report the local URL. Do not expose it to the network.

## Safety and privacy

- Treat command arguments and filesystem paths as potentially sensitive.
- Keep history and reservations local in `~/.harbormaster`.
- Do not copy or publish local process inventories.
- A vanished-service event is evidence that a listener disappeared, not proof of a crash.
- Report observation, inference, and recommended action separately.
