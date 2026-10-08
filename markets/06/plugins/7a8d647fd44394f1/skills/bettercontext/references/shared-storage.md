# Shared storage

The plugin installation is local; the permanent registry is a small shared JSON
file outside the folder containing memory.db. It records the active location,
edition, revision, enrolled hosts and any pending migration. It contains paths
and host names, not saved facts. Give it the same filesystem protections as the
memory database. No publisher server or broadcast service is involved.

Each host stores storage_registry_path, shared_root and instance_id in its local
plugin-config.json outside the plugin cache. Connect each installation once with
memory_configure_storage: mode connect, directory (containing memory.db),
registry_path, shared_root and check_only. The registry and database should be
within that shared root. Use each host's own mount path. For example a Windows
share root and a Linux mount root can refer to the same directory tree.

The CLI equivalent is plugin-root/scripts/configure_host.py --database <file>
--registry <permanent-json> --shared-root <mount-root>. --check previews enrollment.
The private runtime is bundled; no separate source checkout is required.

For a move inside the shared root, use mode migrate and the new directory.
Relative paths update all enrolled installations without changing their local
settings. To move outside that root, supply destination_paths: a list of objects
with instance_id and absolute database_path for EVERY enrolled host. Those paths
must refer to the same destination file; the migration host cannot verify another
host's mount. Confirm access from each host first. Future hosts joining such a
location supply their local database path when enrolling; the tool adds their mapping. Shared storage must support
SQLite DELETE-journal locking and file locks; a sync folder is not a substitute.

Migration takes the registry lock, publishes a pending state, locks source writes,
freezes source writes, copies and verifies every table, schema, row/ID and
counter, saves a verified backup, then publishes the new path. New calls pause during
the move. The backup and original are retained. It never overwrites or merges a
destination. The registry stays in its permanent location. Do not delete it or
disconnect that original registry share when moving the database elsewhere.

An interrupted move stays pending. memory_storage shows the transaction.
memory_recover_storage with action finish can activate a fully verified unchanged
copy. Action cancel reactivates the original and retains the candidate copy for
inspection; it does not merge data. Preview using check_only true before applying
the user's chosen recovery. Both operations use the same inter-host lock.

Updated MCP processes and wake helpers re-resolve on every connection. Existing
tasks running PRE-registry plugin code need one restart/new task to load this
upgrade. They cannot receive new executable code through a relay. The maintained
legacy CLI follows a small sidecar pointer at the original database location;
raw SQLite clients ignore the registry, but frozen-source triggers reject writes
after migration. Installations that were never enrolled cannot be discovered or
configured automatically. Host aliases are not authentication.

Linux connections use SQLite unix-excl locks, including CIFS mounts. Cross-host
Windows/Linux migration and lock exclusion were tested on a shared SMB volume.
