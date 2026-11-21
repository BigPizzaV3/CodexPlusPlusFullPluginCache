# Worksheet header text and position

Privacy boundary: this public plugin is for adult educators and creators. Never
transmit personal information about children under 13 to OpenAI. Use anonymous
or synthetic inputs only; do not request, send or retrieve pupil names, pupil
ids, rosters, photographs, scripts, individual answers or individual results.
Apply this boundary whenever ages or identifiability are uncertain. Do not
open, screenshot, upload or read back private pupil records through a browser
or another connector. Give the exact native link and hand the sensitive step
to the adult user to complete independently. Do not read a record first merely
to decide whether it contains personal information.

Use `get_sheet_header` with `settings:read` for the connected teacher's current
header. It returns only `name`, `class_name`, `school`, `position` and
`has_logo`, plus the exact native settings link. It does not expose the logo
address, profile, email or payment information. Request these explicit scopes
only for a requested header task; they are not default free-tool permissions.

`update_sheet_header_text` needs `settings:write` and all four text/position
fields: `name` (up to 60 characters), `class_name` (40), `school` (80) and
`position` (`bottom` or `top-right`). Read the current header first, apply the
teacher's requested change and send the other fields unchanged. A request to
change a class label is not permission to erase the teacher or school name.
An empty string explicitly clears that text field. Do not put pupil names in
the class label. If read access is unavailable, obtain all four current or
requested values rather than inventing or clearing them.

The native writer preserves the existing logo. It does not remove watermarks,
grant paid header features or change any download/export eligibility. These
settings use no model calls or credits. Logo uploads, profile/security
settings, subscription changes and billing use their native interfaces;
this operation accepts no arbitrary settings path or upload URL.

Read the actual saved result before reporting completion. After an ambiguous
failure, read the current header before retrying. Return the exact settings
link and the fields actually changed, without subscription offers.
