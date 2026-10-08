# Connected tools

The user may have Remote Desktop Commander or another computer/terminal connector attached. Discover its actual callable tools and read their schemas. This package neither installs nor authenticates that connector.

| Need | Suitable existing capability | If absent |
| --- | --- | --- |
| Read program rules | Browser, document reader, or user-supplied text | Request the relevant rules before dependent live tests |
| Inspect source | File reader and local search with line numbers | Analyze supplied snippets and disclose limited coverage |
| Inspect web/API behavior | Authorized browser, HTTP client, or existing proxy | Work from supplied request/response evidence |
| Run local analysis | Terminal on the verified Windows/Linux host | Use available read-only analysis capabilities |
| Save evidence and reports | File writer in an authorized output folder | Return a draft in chat |

Use read-only capability checks first: current host, working directory, shell, available executable paths, and permitted output location. Do not enumerate credential stores or unrelated private files as a setup check. Prefer already installed utilities. Do not install packages or launch broad scanners merely because Kali is available.

For commands, quote paths and user-controlled values correctly for the actual shell. Set explicit targets, output paths, timeout, and request limits where applicable. Read the chosen tool's help when its flags or defaults are unknown. Avoid shell interpolation of untrusted HTTP data. Inspect the real exit status and output before claiming success.

For browser work, select the user-authorized tab/profile and inspect current state. Use observed controls rather than guessed selectors. Track account identity and role so an authorization test is not accidentally performed under an administrator session.

For HTTP work, record method, destination, account role, relevant inputs, response status, and the observed security effect. Handle cookies and tokens as secrets. Redact shareable copies while preserving enough structure for reproduction. Check redirect destinations before following them outside the permitted scope.

If the host exposes approvals, honor them. Installation of this skill does not grant blanket tool authorization. Never disable a sandbox or bypass a connector denial to continue testing.
