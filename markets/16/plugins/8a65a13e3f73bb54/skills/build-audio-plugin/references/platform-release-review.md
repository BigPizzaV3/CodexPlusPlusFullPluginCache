# Platform and delivery review

Use this reference when preparing assets, installers or platform support claims.
It is a review procedure, not a new packaging/signing endpoint. Dispro still
builds only its fixed LV2 example. Product receipts establish only their named
artifact and environment; do not transfer a pass to a new build or another product.

## Asset staging is part of the artifact

Freeze the exact binary, asset version and intended package layout together.
List required resources and relative destinations, then compare the staged and
extracted package inventories and hashes. A working developer tree does not
prove that an installer contains or locates the right assets.

Check whether the binary expects external assets or contains an embedded fallback.
Keep that configuration with the evidence. A diagnostic that succeeds using a
fallback cannot qualify a customer build that requires external files. Likewise,
signing a diagnostic or removing a visible marker does not change the configuration
compiled into it. A customer build with changed inputs needs its own evidence.

For Windows staging, verify the actual target-native paths, expected directory
structure and destination contract. Do not assume a Mac-oriented release check
proves Windows package correctness. Treat missing or ambiguous required resources
as a failed stage; never silently use unrelated installed assets to make a test pass.
Use isolated staging/extraction directories and retain the owner-approved source
assets unchanged. A fresh installation/upgrade must separately prove resolution
of the staged assets in the installed environment.

## Minimum macOS version is specific to each architecture

Record the architectures actually present in every declared executable payload
and relevant dependency. Inspect the deployment information for each slice;
the SDK used to build a binary is not its minimum deployment version. A universal
container does not establish a single OS floor or demonstrate both hardware paths.

Keep three facts separate:

| Fact | Evidence |
|---|---|
| Encoded binary/dependency requirement | Exact file hash and per-architecture load-command/dependency inspection |
| Installer admission rule | Versioned preflight logic and supported/unsupported input cases |
| Supported user environment | Actual install/load/audio receipts on the named OS, architecture and host |

Reconcile binary requirements, dependent libraries, installer checks and published
support text before release. A preflight should reject unsupported combinations
before making installation changes. A mocked preflight case is not an old-OS
installation test. Running Intel code under translation is not physical Intel
hardware acceptance. Do not lower a published floor based only on one main binary
or one successful local run.

## AAX validation and Windows publisher signing are separate

Keep the product-specific AAX/PACE signing/verification receipt separate from
Windows Authenticode evidence. A valid AAX signature does not establish the
publisher signature or timestamp of the Windows payload/installer. Conversely,
an Authenticode pass is not proof that a retail Pro Tools host accepts the AAX
plugin. Record both when the declared release requires both; never reuse another
product's configuration or infer one result from the other.

For an authorized Windows signature review, record the exact file, verification
policy, expected publisher identity, timestamp evidence and tool result. A generic
"valid" label without its policy/identity scope is incomplete. Microsoft documents
SignTool's separate verification policies and timestamp operations; Avid documents
the separate AAX developer/signing process. Consult current official requirements
for the chosen target instead of copying an old signing command or promising
certificate reputation. [Microsoft SignTool](https://learn.microsoft.com/en-us/windows/win32/seccrypto/signtool),
[Avid AAX SDK](https://developer.avid.com/aax/).

On macOS, signature validity, notarization acceptance, stapling, Gatekeeper,
installation and host acceptance also remain separate. Preserve each declared
format. If a required signer or format is unavailable, identify the affected
stage as unrun/failed; do not silently omit it or label an unsigned-private output
a customer release. Dispro does not obtain credentials, create accounts, configure
secret storage or call signers as part of this procedure.

## Report the narrow result and the next gate

Use the artifact/format/OS/architecture/host worksheet in `release-checklist.md`.
Keep source inspection, synthetic fixtures, native compilation, native offline
loading, installed-host behavior and public delivery as separate evidence.
Report `passed`, `failed` or `unrun` and preserve cancelled/timed-out outcomes.

For a skills-only ChatGPT/Codex plugin, distinguish loading the installed skill,
executing its scripts in an authorized local runtime, and invoking it in a
particular hosted client. Reading a package alone is not execution evidence.
A local native run is not proof that ChatGPT web/mobile can reach that machine,
or that a DAW has loaded the generated audio plugin.

Before changing a saved plugin or public submission, identify the current version,
release/submission ID, audience and exact approval scope. Private plugin approval
does not approve a public-directory replacement or website archive change. If
current review/publication state cannot be checked, preserve the submission and
record the gap; do not infer approval from a previously uploaded draft.

Existing Windows GUI/DLL-unload and known Logic AU transition gaps remain open
until their own exact native acceptance succeeds. None of the staging, floor or
signature checks above supplies those missing passes.
