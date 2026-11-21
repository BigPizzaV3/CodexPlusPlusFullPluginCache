# Common game server problems and their fixes

Each entry: what the console or `diagnose_server` shows, the cause, the fix.

## Starts, then stops or crashes

- **`OutOfMemoryError`, the server stops with no error, or memory at 95% or more of the plan**: the game needs more memory than the plan has. Lower `view-distance` / `simulation-distance` in `server.properties`, remove heavy mods or plugins, or pre-generate fewer chunks.
- **`You need to agree to the EULA`**: set `eula=true` in `/eula.txt` (only after the user agrees to Mojang's EULA), then start.
- **`Unsupported class file major version` / `UnsupportedClassVersionError`**: the Java version doesn't match the Minecraft version. The Java version is set by the server's Docker image (`get_startup`). Changing it is a GravelHost support matter if no matching image is offered.
- **`Failed to bind to port` / `Address already in use`**: the configured port isn't the server's own. Set `server-port` in `server.properties` to the primary port from `get_network`.
- **A plugin or mod stack trace right before the stop** (`Could not load`, `Error occurred while enabling`, `Mixin apply failed`): that add-on is broken or built for another version or loader. Disable or remove it with `remove_content` (it goes to the recycle bin), then start.
- **Errors reading `level.dat`, region files, or "chunk" errors**: the world may be corrupted, often after a crash or a full disk. Restoring the last good backup is the safe fix; ask first, because it replaces the current world.

## Lag

- **`Can't keep up! Is the server overloaded?`**: CPU at the plan limit. Common causes: high `view-distance`, many entities (mob farms), heavy plugins, chunk generation. Lower distances first.
- **CPU fine, players still lag**: usually the network between the player and the server's location; compare with `get_server` (location).

## Players can't join

- Check the server is running (`get_server_status`) and give the exact address from `get_network` (the primary port).
- **`Outdated client` / `Outdated server`**: the game versions differ. Change one side.
- **`You are not whitelisted`**: `whitelist add <name>` in the console, with the user's go-ahead.
- **Bedrock players on a Java server**: they need Geyser (a plugin or mod) and its own port.
- **`Failed to verify username`**: the player isn't signed in with a paid account, or `online-mode` doesn't match the setup.

## Disk

- **Disk at 90% or more**: old backups, logs, crash reports and unused worlds are the usual space. A full disk corrupts worlds, so free space before restarting.
