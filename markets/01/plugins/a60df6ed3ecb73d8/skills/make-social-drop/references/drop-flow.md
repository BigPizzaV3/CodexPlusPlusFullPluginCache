# Social drop flow

Lifecycle: Draft → Processing → Ready (or Failed). Export only when Ready.

Source types commonly supported by `create_drop`:

- exercise
- workout
- program
- (and related team source variants accepted by the MCP tool schema)

Variants:

- Aspects: 9:16 / 1:1 / 16:9
- Durations: 15 / 30 / 60 seconds

Tools:

| Step | Tool |
|------|------|
| Create | `create_drop` |
| List | `list_team_drops` |
| Regen copy | `regenerate_drop_copy` |
| Regen cover | `regenerate_drop_cover` |
| Update meta | `update_drop` |
| Export | `export_drop` |

Automate scheduled publishing lives in Teams (`/automate`), not in these MCP tools.
