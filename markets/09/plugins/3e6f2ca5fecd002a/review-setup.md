# Reviewer fixtures and recording walkthrough

## Provided recording

The demo URL is <https://www.loom.com/share/bdfb3ef1293b43708d5f313b5ca34a5e>
and is included in `review.demo_recording_url` in the manifest. The Loom page
is titled “Circa MCP Connection for Place Recommendations” and displays a
5-minute-28-second video. Public playback without login was verified on
October 1, 2026. Full case coverage and a complete sensitive-content check
have not been verified. The walkthrough below remains the coverage checklist.

## Account and data setup

Use two dedicated non-admin accounts with usernames and only sample activity.
Keep their passwords and sign-in instructions in secure portal fields, outside
this package. Sign-in uses `https://cerca.me/sign_in`; verify that exact URL and
the accounts before supplying access. Complete username setup and onboarding
so the reviewer can reach OAuth consent without assistance.

Connect the primary account in ChatGPT development mode to
`https://cerca.me/mcp` using OAuth, including read and write permission.
Verify both `list_my_places` and discovery of `save_place`. The development
connection is separate from the submission portal's eventual connection.

These baseline fixtures were provisioned on October 1, 2026 using the guarded
PluginReview::Seed service. Both accounts are private, non-admin, onboarded,
and have unique usernames. Passwords and the friend username are stored outside
this package and supplied through the secure review fields. No personal account
was used. Five places were reused from the production catalogue; Praça do
Comércio was resolved using its real Google Places record.

| Place in Lisbon | Primary reviewer | Controlled friend |
|---|---|---|
| Pastéis de Belém | loved | liked |
| Castelo de São Jorge | want-to-go, private note: Review fixture: visit together | want-to-go, private note: Friend private fixture |
| Time Out Market (Lisboa) | absent initially | loved |
| Jerónimos Monastery | absent initially | liked |
| LX Factory | absent initially | want-to-go |
| Praça do Comércio | disliked | loved |

City metadata may say Lisboa rather than Lisbon. Use the Lisbon center
coordinates (38.7223, -9.1393) with destination/near filtering so both localities
are covered. Search Time Out Market without appending Lisboa to its name.
Select exact provider matches; resolve ambiguity before saving. Follow the
controlled friend from the primary account and accept the request if private.
The friend must share their full list (`all`) for shared want-to-go comparisons.
Record the actual username in secure reviewer instructions. Do not put a
personal friend's handle or notes into public review evidence.

The friend fixture puts the three initially absent places in Cerca's catalogue.
Use returned `place_ref` values during cases, never sample numeric IDs.
Place-category and taste affinities depend on actual catalogue data; expected
answers must reflect tool results, not invented exact scores.

Run P1–P3 first, then P4 and P5. Reset primary-account changes from P4/P5
through confirmed removal before rerunning. Preserve the baseline loved,
want-to-go and disliked places. Never reset a personal account.

## Record a real ChatGPT walkthrough

Rehearse the cases before recording. Use the actual packaged plugin/server
version, readable text size, and the dedicated reviewer account. Keep passwords,
tokens, unrelated chats and personal activity off screen. Screenshots and this
script are not a recording. A website product-tour video alone does not show
the ChatGPT tool workflow.

Use a screen recorder such as Loom, or start your recorder before having
Computer assist with the visible walkthrough. Capture the following:

1. Show the Cerca development connection in ChatGPT, OAuth consent, and the
   connected state. Hide credential entry.
2. Run P1: “Plan two days in Lisbon around my want-to-go places and places my
   friends recommend. Explain how my Cerca taste profile affects your picks.”
   Show real results, prioritization and separate attribution of friends and
   editorial picks; Praça do Comércio must not be recommended.
3. Run P2: show the loved-place filter, first-place detail and catalogue search.
4. Run P3: list follows, select the controlled friend, and show shared
   want-to-go results. The friend's private note must not appear.
5. Run P4 and its scripted follow-ups from `plugin.json`: save LX Factory,
   replace the private note, explicitly authorize a public rating note, read
   back the rating, confirm removal, and verify it is gone.
6. Run P5: record two places with different statuses. Show both actual item
   outcomes and read them back. If a candidate requires confirmation, capture
   clarification; do not claim an unresolved item was imported.
7. Run N1–N3: show that booking/payment, unauthorized private access and private
   Google account synchronization are unsupported without Cerca tool calls.

Optional additional coverage: supply a real shared Google Maps fixture list
containing only test destinations. Ask “Import this shared Google Maps list
into my want-to-go places,” including its actual link. Show `started` and the
returned import ID, then check progress with `get_import_status` until a terminal
status. Do not invent a fixture URL or treat background start as completion.

Play back the saved recording to verify readable prompts/results, complete
coverage, successful playback and no exposed secrets. Host it at a destination
reviewers can view without requesting access. Verify that actual recording URL
before replacing `extensions.com.openai.review.demo_recording_url` in `plugin.json`
and rebuilding the archive. The supplied URL is already included; recheck access
and coverage if the recording is changed.
