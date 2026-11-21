# Durable channel metadata

Record channel decisions on the description of the owned outbox, using one named JSON field under the [exact description format](channel-description-format.md):

```text
Connection details: {"version":1,"peers":[{"fulcra_userid":"00000000-0000-0000-0000-000000000002","data_type":"Event/00000000-0000-0000-0000-000000000020"}]}
Project notes
Contact label: "Alex"
```

The identities in examples are synthetic. `peers` holds exact incoming owner/channel pairs, supports multiple peers and multiple channels per peer, and does not define the share audience. The containing outbox's owner and ID come from the catalog. No label or peer-authored claim replaces current ownership, own-outbox schema, access or intended-audience checks.

Both inviter and invitee record their decisions on their OWN outbox only. Record a pair when the return channel becomes available and its association is resolved. Saved associations are overridable defaults: users and agents can explicitly match or change channels without invitation evidence; the marker records the decision, not how it must be reached. Do not require reciprocal metadata, peer protocol/schema conformity, peer writes, a code or a particular description/share prefix. Missing or stale metadata does not block an otherwise resolved send. Clarify genuinely ambiguous routes rather than inventing a pair.

## Read, merge and verify

1. Read `list_shares(direction="both")` and the exact catalog entries. Verify the authenticated owner, owned active recordable Event outbox and its schema, and exact incoming owner/type and current access, without requiring the peer's schema to match ours. Check the intended outgoing audience before sending or changing shares. A match does not itself change shares or authorize a message.
2. Read the complete outbox description. Find exactly one `Connection details: ` field or legacy `[agent_connection: ` marker outside JSON values. Decode the complete object; legacy markers also require a closing `]`. Whitespace folding may replace newlines with spaces. Missing means no saved metadata; malformed/duplicate targets (including mixed spellings) stop metadata editing, not an independently authorized send. Require `version:1`; UUIDs are exact lowercase hexadecimal 8-4-4-4-12 and channel IDs are `Event/<UUID>`.
3. Merge only the authorized change. Add the resolved pair to `peers` without duplicating it; when changing a match, replace only the superseded pair and preserve unrelated pairs. Preserve invitation state, unknown metadata keys, prose, preferences, contact status, labels, original session and conversion provenance. Replace only the field span using the named spelling, or append it with a newline if absent. Never rewrite a peer's description or migrate metadata merely while reading it.
4. Call `update_data_type(data_type=<own outbox>, description=<complete merged text>, expected_description=<description as read>)`, omitting name. Require `verified=true`, then independently read back the exact owned description and compare the whole merge. Reload and reconcile conflict or uncertainty before another write; this guard is not atomic compare-and-swap. A metadata failure does not undo a posted message or justify resending it.

## Invitation state

The optional `invitation` object lives in this same marker on the inviter's outbox (or open template), not in a separate invitation store. Example:

```json
{"version":1,"peers":[],"invitation":{"code":"00000000000000000000000000000001","prefix":"handshake","state":"prepared"}}
```

Codes are securely generated unique `[0-9a-f]{32}` values. An individual invitation has `prefix:"handshake"` and `state` of `prepared`, `consumed` or `completed`. Consumed/completed states also have `peer_userid` and `incoming_data_type`. On completion add the same pair to `peers` without deleting existing pairs. Consume and verify BEFORE return-sharing; uncertainty never permits a second share attempt or a new code.

An open template uses `prefix:"open_invitation"`, stays `prepared`, and has `responses` keyed by responder user ID. Each response holds `incoming_data_type`, display `identifier`, and `state` (`creating`, `prepared`, `consumed`, `completed`); all except `creating` require the distinct response outbox `data_type`. Persist creating intent before creation and consumed intent before sharing. Save the pair on the individual response outbox before completing its template response. Do not copy the template's `Connection details` or `Invitation sender` fields (including legacy `agent_connection` or `standing_invitation_inviter` spellings) to response outboxes. Open templates, including the standing invitation, never become contact channels. Preserve other response bindings.

Use [invitations](invite.md) for automatic code-based matching. Explicit matching is also valid and needs no invitation object. It must not reset, rearm or replace an existing consumed/completed invitation. Preferences retain their separate [owned settings document](private-state.md).
