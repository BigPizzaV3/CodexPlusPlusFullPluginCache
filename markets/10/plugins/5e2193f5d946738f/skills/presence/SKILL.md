---
name: presence
description: Answer questions about PositionGuard groups, named areas, member presence, and area counts while respecting independent member consent and presence freshness.
---

# PositionGuard presence

Use the connected PositionGuard MCP tools for area-level presence questions.
The production server enforces privacy before returning information. This skill
does not grant access or replace those controls.

## Connection

Use the host's supported remote MCP OAuth connection to
https://mcp.positionguardai.com/mcp. The user approves the assistant through the
PositionGuard mobile app using the provider's displayed QR code or code.
Preserve the existing PositionGuard and Firebase identity flow. Do not request
API keys, extract tokens, invent OAuth scopes or endpoints, create accounts on
the user's behalf, or introduce alternate authentication. If access fails or is
revoked, report the failure and direct the user to the supported connection flow.
Never interpret an authentication failure as empty groups or absent members.

## Tools

- list_groups: discover available groups and IDs.
- list_areas: discover named areas and IDs, optionally within a group.
- where_is_member: look up an established member nickname, optionally in a group.
- who_is_at_area: obtain consenting members' confirmed and last-known presence.
- count_members_at_area: obtain the server-provided count without identities.

Prefer returned IDs to ambiguous names. Clarify group or area ambiguity when
needed. For "Where am I?", use an already established PositionGuard nickname;
otherwise ask for it. No self-identity tool is established by this package.

## Interpret results

- Each member independently authorizes AI sharing. The requesting user's consent
  does not authorize access to other members. Respect group and area visibility.
- unknown means unknown, never absent or away. Do not guess hidden presence.
- A missing area in inside_areas is not evidence that the member is outside it.
- Keep confirmed and last_known lists separate. Report last-known information
  with last_confirmed_seconds_ago as an age, never as current presence.
- since indicates entry time, not freshness. Do not invent duration when absent.
- Relay count_note, undisclosed_note, and freshness notes. Do not present partial
  names as everyone, infer undisclosed identities, or reconstruct hidden presence.
- When stale_count or undisclosed_count is nonzero, report member_count as
  "at least N" with the server's qualifications and how many counted members
  are not recently confirmed. Do not label stale members as currently there.
- count_unavailable is unknown, never zero. no_such_area or no_such_member does
  not establish anyone's absence.
- not_at_area supports only the scope explicitly stated by the server; do not
  extrapolate it to hidden areas or an exact location.

Do not provide coordinates, routes, location history, continuous monitoring,
or privacy bypasses. These tools cannot change settings or send messages.
Sharing and individual assistant revocation are managed in PositionGuard.
