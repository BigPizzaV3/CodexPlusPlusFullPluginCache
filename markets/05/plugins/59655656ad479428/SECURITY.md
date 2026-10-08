# Security policy

## Supported version

Security fixes currently target the latest `0.1.x` private-beta release.

## Report a vulnerability

Do not open a public issue for credential exposure, path escape, secret leakage, provider spoofing, budget bypass, or unauthorized repository mutation. Email **team@empirellm.com** with a concise description and non-sensitive reproduction steps.

Do not send API keys, keyring exports, real private source code, or raw provider responses. Revoke any credential that may have been exposed before reporting it.

## Credential handling

- Enter provider credentials only through `$empire-settings` or the router's hidden setup prompt.
- Never paste credentials into Codex chat, repository files, issues, pull requests, or logs.
- Use provider-side spending limits and a dedicated key for Empire.
- `doctor` reports presence and credential source only; it never prints values.
- `logout` removes stored Empire credentials from the native system keyring.

The project intentionally contains no production credentials. Offline tests use synthetic fixtures.

## Implemented safeguards

- Outbound tasks, evidence, and media prompts are length-bounded and rejected when credential patterns or high-entropy secret material are detected.
- Provider traffic is HTTPS-only, rejects embedded URL credentials and non-public targets, verifies TLS certificates, and refuses redirects so authorization headers cannot cross origins.
- External-model output is treated as untrusted: only documented structured fields are retained, size and count limits are enforced, and secret-looking responses are rejected.
- Provider output and handoff artifacts cannot write into the repository. Private state uses owner-only directories and atomic, mode-`0600` files.
- Release ZIPs are built from an explicit allowlist with deterministic contents; private state, caches, key material, traversal paths, active SVG content, and dangerous Python execution constructs are checked before submission.

See [SECURITY_TESTING.md](SECURITY_TESTING.md) for reproducible commands, results, benchmark mappings, and the limits of these tests.
