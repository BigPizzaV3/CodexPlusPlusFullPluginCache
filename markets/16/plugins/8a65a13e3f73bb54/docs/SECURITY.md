# Scope and trust

Dispro is intended for a private local workspace and its original reviewed
recipe. It is not a security boundary for hostile code or malicious same-user
processes. Caller-chosen command strings, arbitrary file reads, SDKs, hooks and
modified source are rejected. Native validation runs in a child process with
timeout/cancellation, not an OS sandbox.

Only dedicated workspace files are read/written by workflow operations.
Symlink paths and multi-linked inputs are rejected. Source bytes are verified
and snapshotted before compilation. Private credentials and compiler override
variables are not forwarded; raw subprocess output is neither saved nor sent
to the model. Receipts contain project identifiers, machine/OS version, hashes,
exit codes, check names and statuses. CLI paths remain local and the operator
controls sharing. No telemetry, network client, account, purchase flow or
credential storage is implemented.

The parent host still controls its conversation and file handling; this is not
a statement about ChatGPT retention. Public policies must describe actual host
and publisher practices and be approved/published before directory submission.

No signing or publishing endpoint exists. Future such operations must require
explicit artifact-bound authority, preserve receipts, and use existing secure
credential mechanisms without revealing values to a model.
