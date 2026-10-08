# Unicycle maintenance

Read CONTEXT.md. Keep the plugin reusable: no user names, task IDs, private paths, credentials, history, or runtime state in package sources. State belongs under the user's chosen private directory. Use Python standard library. Native Codex tools remain host-owned and are capability checked each run. Preserve error and approval boundaries; no remote sends from the helper. Test behavior with `python3 -m unittest discover -s tests -v`. Do not claim visible delivery from file creation or queued tab placement.
