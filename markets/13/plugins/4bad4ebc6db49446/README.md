# Eye.Photo

The official owner and staff assistant for Eye.Photo. Seven skills support public
product help and authorized studio workflows at https://eye.photo/mcp/plugin.
Access follows the selected account, current studio membership, plan, permissions
and approved studios. No credentials or executable hooks are packaged.

Account linking uses the registered App and the host's saved connected accounts.
Public help and installation do not trigger login. For a requested private task,
request its required scopes together, preserve existing grants, and let the host
show OAuth consent. Continue the same task after verification. See
[supported account workflow](scripts/AUTHENTICATION.md). Sending, publishing,
deleting and applying changes retain their separate preview/approval requirements.

The public ZIP declares mixed OAuth/CIMD configuration in mcp.json. The local
registered package uses the same production endpoint, skills, version and existing
local plugin identity. Installation checks availability before changing files:
it prefers the publisher registration once accessible, and otherwise uses the
existing private Eye.Photo test registration. An unavailable publisher draft must
not make the test installation unusable. Public uploads exclude .app.json and
registered App declarations; the publisher draft identity stays unchanged.

Verification explicitly reports whether native calls use the private test
registration or publisher registration. Private tests establish that installation's
behavior; they cannot establish public release availability. Raw MCP credentials
and unrelated administrative connections never count as native account verification.

From the application repository:

```sh
script/eye_photo_plugin release
script/eye_photo_plugin install
script/eye_photo_plugin verify
script/eye_photo_plugin verify --scope templates:write
# After publisher availability, require the publisher identity explicitly:
script/eye_photo_plugin install --publisher
script/eye_photo_plugin verify --publisher
```

Verification checks package identity, version, enabled skills, file hashes,
regular App availability and native tools tagged with that App/account identity.
It makes harmless public and protected reads only; it never starts OAuth or
approves consent. Exit 0 means account calls passed; exit 2 means host availability
or account authorization remains pending; exit 1 means a package/runtime error.
A draft upload or successful scan alone is not proof of the connected-account UX.
The regular draft must remain unsubmitted and unpublished during this work.
