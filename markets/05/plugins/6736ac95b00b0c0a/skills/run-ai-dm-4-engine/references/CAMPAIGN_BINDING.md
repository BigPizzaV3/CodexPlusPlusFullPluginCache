# Campaign binding

Bind only the Campaign directory or ZIP explicitly supplied or selected by the
user. The package must expose exactly one `CAMPAIGN_MANIFEST.json`.

## Directory Campaign

- Read and validate in place.
- Substantive turns update the directory only after all database validations
  pass.
- Use `--output` when the user also wants an exported ZIP.

## ZIP Campaign

- Extract to a private disposable directory.
- Reject path traversal and packages with zero or multiple manifests.
- Read-only commands require no output.
- Every mutation requires `--output <changed-campaign.zip>`.
- Refuse to overwrite the only supplied ZIP.

## Authority

The manifest selects the current state head and transaction hash. Filenames,
modification times, search rank, file size, and labels such as `CURRENT`,
`MASTER`, `FINAL`, or `COMPLETE` carry no current-authority weight.

If several Campaign packages are visible, stop and ask the user to bind one.

## Persistence claim

A turn is durable only when the changed Campaign directory remains available or
the changed Campaign/checkpoint ZIP is returned to the user. Conversation memory
is never Campaign persistence.
