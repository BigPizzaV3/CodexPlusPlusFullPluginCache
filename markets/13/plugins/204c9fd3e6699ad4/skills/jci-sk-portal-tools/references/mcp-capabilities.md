# JCI SK Portal — MCP tool/capability registry (literal reference)

Pulled directly from `database/seeders/McpCapabilitySeeder.php` and
`App\Mcp\Servers\PortalServer::CAPABILITY_TOOL_MAP` in the jcisk-portal
repo (not summarized/approximated) — this is a snapshot taken 2026-10-23;
`required_permission` is admin-manageable live data, so the exact set a
given caller can use may differ from this table. When in doubt, call your
own MCP client's `tools/list` (the live, current, PER-CALLER-FILTERED
answer) or this server's own `my-permissions` tool, rather than trusting
this file.

| tool name | capability key | type | required_permission | input |
|---|---|---|---|---|
| `list-content` | `content.list` | query | — | `folder?`, `type?` ("file"\|"text"), `tag?`, `limit?` (default 20, max 100) |
| `get-content` | `content.get` | query | — | `id` (uuid, required) |
| `search-content` | `content.search` | query | — | `q` (required), `limit?` (default 20, max 100) |
| `create-content-note` | `content.create_note` | action | `content.create` | `title` (required), `body` (required), `folder?`, `tags?` (array) |
| `list-corpus` | `corpus.list` | query | — | `path?` (default `/`) |
| `glob-corpus` | `corpus.glob` | query | — | `pattern` (required) |
| `read-corpus` | `corpus.read` | query | — | `path` (required), `offset?` (default 1), `limit?` (default 400, max 1000) |
| `grep-corpus` | `corpus.grep` | query | — | `pattern` (regex, required), `path?` (glob, default `/**`), `context?` (0-5, default 0), `case_sensitive?` (default false), `max_results?` (default 200, max 500) |
| `remember-note` | `memory.remember` | action | — | `note` (required) |
| `forget-note` | `memory.forget` | action | — | `note_id` (integer, required) — destructiveHint: true, the one genuinely irreversible tool here |
| `submit-feedback` | `feedback.submit` | action | — | `query_ref?`, `rating?` (1-5), `comment?` |
| `my-permissions` | — (introspection, no underlying capability row) | query | — | none |

**"type" above maps directly to each tool's `readOnlyHint` annotation**
(query → `readOnlyHint: true`, action → `readOnlyHint: false`) — there is no
longer a 3rd "list" category; before 2026-10-23 `content.list` was seeded
under a now-unused legacy `list` tool_type value that existed only for a
single bespoke discovery meta-tool, since replaced by the native MCP
`tools/list` call plus the `my-permissions` introspection tool above.

Every call is logged server-side to `mcp_invocation_logs`
(platform/user/capability/status/duration) — this is for the portal admin's
own visibility, not something the calling AI client needs to act on.
