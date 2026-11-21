# Owned settings and state

Used by [preferences](contact-preferences.md). Preference documents live in a dedicated owned Event description, not contact channels. Invitation state and durable channel pairs instead use [channel metadata](channel-metadata.md) on the owned outbox.

## Read and merge

1. Get authenticated `own_fulcra_userid` from `list_shares(direction="both")`. Discover owned v1 Event entries named exactly `Fulcra Contact Preferences`, then use `get_data_catalog(data_type=<exact ID>)` and parse its `description`. Require exact owner and a v1 Event. Select the lexicographically lowest exact ID if duplicates exist, as the app does. Never create a replacement for an unreadable existing entry.
2. Before using state and again before each write, inspect outgoing shares. Stop if any grant has `share_all_data=false` and `data_types=[<storage ID>]`, with no `file_paths` or `file_history_paths`, regardless of its name. Parse strict JSON (no duplicate keys), validate the entire known schema below, and retain all other scopes and preference values. Unknown keys/version, malformed state or unsupported schema stops writes; never repair or discard it. An absent entry means the empty version-1 document, but a failed lookup does not mean absent.
3. Before each write reload account, description and operation evidence. If any changed, stop and reassess against fresh state; never replay a stale document. Merge only the authorized change. For an existing entry call `update_data_type(data_type=<storage ID>, description=<complete serialized JSON>, expected_description=<description as read>)`, omitting name. For a genuinely absent entry use `create_data_type(base_type="event", name="Fulcra Contact Preferences", description=<JSON>)` without channel fields. Require success and independently rediscover/read the same owned document. No automatic creation retry on uncertainty.
4. `expected_description` is a stale-read guard, not compare-and-swap or a transaction. Other workers/UI can race. Verify the complete merged document after every write, including unchanged entries. On conflict or uncertain readback stop dependent writes, reload and reconcile; do not overwrite competing state or claim atomic/exactly-once behavior.

## Preference schema

Root keys: `version` (integer 1), `global_preferences` (object), `overrides` (object keyed by `<own Event ID>|<peer UUID>`, lowercase canonical UUIDs). Values are partial objects containing only the fields in [contact preferences](contact-preferences.md). Boolean fields require actual booleans, `unanswered_days` an integer 1..365 (not a boolean), `notifications` one of `attention`, `all_messages`, `none`, and `checking_preferences` a string of at most 2000 characters. Empty overrides restore globals; remove that scope rather than replacing unrelated scopes.

```json
{"version":1,"global_preferences":{"pause_autonomous_replies":true,"notifications":"attention"},"overrides":{"Event/00000000-0000-0000-0000-000000000011|00000000-0000-0000-0000-000000000002":{"pause_autonomous_replies":false,"unanswered_days":3,"checking_preferences":"Summarize decisions."}}}
```
