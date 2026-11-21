# Class summaries and the school workspace

Privacy boundary: this public plugin is for adult educators and creators. Never
transmit personal information about children under 13 to OpenAI. Use anonymous
or synthetic inputs only; do not request, send or retrieve pupil names, pupil
ids, rosters, photographs, scripts, individual answers or individual results.
Apply this boundary whenever ages or identifiability are uncertain. Do not
open, screenshot, upload or read back private pupil records through a browser
or another connector. Give the exact native link and hand the sensitive step
to the adult user to complete independently. Do not read a record first merely
to decide whether it contains personal information.

Check each operation in the connected tool list. Class reads use `classes:read`,
metadata changes use `classes:write`, school reads use `schools:read` and owner-
confirmed school identity changes use `schools:write`. Request only the relevant
explicit consent; a public/free-tool connection does not imply these grants.

## Class-level summaries only

`list_my_classes` returns owned class-level metadata and pupil counts, following
`nextOffset` as needed. `get_class` accepts an exact returned `class_id` and
returns a summary without pupil names, ids, roster entries or pupil attributes.
There is no `include_pupils` expansion. Never send that field, request a roster,
or use another saved resource/export/browser as a workaround.

`create_class` and `update_class` accept only their disclosed class metadata
such as class label, year group and subject. Use anonymous labels rather than
pupil identities in text. Pupil arrays and roster replacement are not public
plugin inputs. Native capacity, uniqueness and ownership remain authoritative.
Read the safe summary before a requested metadata change, preserve unrelated
fields and do not repeat a successful creation after a timeout.

`delete_class` requires the exact owned `class_id` and `confirmed:true` for the
teacher's explicit deletion. The native service removes the class record,
detaches seating links and notifies linked marking sessions; saved seating
files are not deleted. Explain that consequence before confirmation.

For an owned-class deterministic seating plan, follow [class-seating.md](class-seating.md).
The backend uses the roster internally; it never returns identities or named
positions to ChatGPT. Give the adult the exact native link for independent
roster management, named placement or individual pupil records. Do not open,
capture or read back that private page.

## School summaries and owner-confirmed identity

`get_my_school` returns current membership/role, school identity and seat usage,
without billing or invitations. `list_school_members` provides bounded active-
colleague summaries without emails or invitation tokens. Follow pagination
only for the requested task. No membership means a neutral access explanation,
not an offer to subscribe or invite anyone.

`list_school_library` takes the disclosed `type`, `page` and `limit` to list
explicitly shared resource summaries. These are not permission to read another
teacher's private body or edit/re-share their work. `list_school_activity`
returns bounded shared-activity summaries, not private records. If the native
library page could contain pupil material, hand the link to the adult without
opening or reading it back.

`update_school_identity` is owner-only and accepts the selected `school_id`,
`confirmed:true` and at least one requested `name` or `brand_colours`. Read the
identity with separate `schools:read` consent before/after saving. Omit unchanged
fields; the trimmed name is 2–120 characters and colours are a complete list
of zero to five native hexadecimal values. An empty list explicitly clears
colours. Confirm the exact replacement list. Native updates have no revision
lock, so do not promise atomic conflict protection.

These operations cannot create a school, upload a logo, invite/message anyone,
change roles/members/security or purchase anything. Explain refusals neutrally.
All personal pupil workflows remain an independent adult native handoff.
