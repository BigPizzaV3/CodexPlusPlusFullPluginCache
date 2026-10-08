# Choose, share, or move your memory location

Use a local Codex task or a supported ChatGPT Work task with Python 3.10+,
local command execution, and access to your chosen folder. An ordinary web
ChatGPT chat cannot reach a computer's database just by installing this plugin.

You can ask BetterContext in plain language:

- "Show where this edition stores my memory."
- "Move this edition's existing memory to [absolute folder], preserving my
  memories, registered chats, message counters, and relays."
- "Connect this computer to my existing shared BetterContext database at
  [database file], using the permanent registry at [registry file] and the
  shared mount at [root]. Do not create a second database."

For a fresh store, explicitly ask to create one. Creating an empty store and
moving your existing memories are different operations. The plugin previews
the change, backs up and verifies migrations, and retains the original.

To share between a server and a computer, mount the same shared filesystem on
both and enroll each installation once in the same edition's registry. Windows
and Linux can use different paths to that same share. Keep public and private
editions in different databases and registries.

Keep the small registry file in a permanent shared location OUTSIDE the folder
being moved. Every enrolled updated instance checks it before opening memory;
offline instances follow the new location when they reconnect. Moving across
different shares requires a destination path for every enrolled computer. The
original registry must remain reachable. A chat relay is not needed to announce
the location. Never move memory.db manually or use a file-sync folder as a
substitute for shared storage with working SQLite file locks.

## Local commands when named tools are unavailable

The Directory release does not register BetterContext MCP tools. It includes
the action program below so the assistant can perform the same operations
through its existing local command-execution capability. This does not create
a remote connection or add MCP tool registration to ChatGPT.

`ACTION` means Python plus the absolute plugin-root `scripts/actions.py` path:

```text
ACTION list
ACTION memory_storage
ACTION memory_configure_storage --arguments-file /absolute/path/change.json
```

For a move, write a JSON object with `mode: "migrate"`, `directory` set to the
new absolute folder, and `check_only: true`. Inspect the result, then apply the
already authorized move with `check_only: false`. If no registry is configured,
first use `mode: "connect"` with the CURRENT database directory, a permanent
`registry_path`, and `shared_root`; do not create a replacement store.

For initial enrollment, use `mode: "connect"` with `directory`, `registry_path`,
`shared_root`, and `check_only: true`, then false. Use `mode: "create"` only for
an explicitly requested new empty store. `ACTION list` provides exact schemas.
For an interrupted migration, inspect `memory_storage`, then use
`memory_recover_storage` with the user's chosen `action` (`finish` or `cancel`),
previewing with `check_only: true`. See shared-storage.md for details.

## Feature limits

- Local memory, tasks, notes, available-history MEM counters, and mailbox relay
  require access to the persistent database from the executing host.
- A MEM counter is a message label, not an automatic archive of every message.
  Cross-chat recall covers saved/imported content and available local history;
  it cannot read arbitrary or unavailable ChatGPT conversations.
- Prefix display depends on the assistant following the skill. Hidden reasoning
  and tool calls are not counted as visible assistant messages.
- Relay queues a message. Automatic wake needs a separately enabled helper and
  a compatible local Codex CLI on the destination host. It does not wake a
  sleeping computer or a hosted ChatGPT web chat.
- The helper's Windows lifecycle is tested. The new Linux/macOS installers and
  reboot behavior are not yet validated; the maintained Code-Engine Linux bridge
  was tested separately. Do not promise supported automatic wake on every OS.
- Chat token savings have not been established by a controlled comparison.
