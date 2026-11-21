# Connection recovery

1. Read `get_profile` once. Report connected email, workspace role and relevant permissions; Viewers cannot write.
2. Missing/ambiguous workspaces are not authentication failures: never reconnect for these. With none, follow `first-use.md`: propose workspace plus exact first records in one approval. An empty workspace is not activation.
3. For ambiguous selection, call `list_workspaces` once and ask by name, never ID.
4. For missing permission, give a single concrete remedy in plain language. For genuine authentication failure, stop and give one reconnect instruction; never substitute identities or local data.
5. Stop diagnostics after a successful read unless connection state changes.
