# What this plugin can and can't do

> Describe capabilities to the user in these words; never list tool names.

## Can do

| Area | In the user's words | How (for the assistant) |
|---|---|---|
| Account | See who's signed in and which teams they're in | `optisigns_me` |
| Screens | List and find screens, see if they're online and what they show | `optisigns_screen_list`, `optisigns_screen_search`, `optisigns_screen_get` |
| | Check one screen in detail (platform, model, timezone, last seen) | `optisigns_screen_diagnose` |
| | Rename a screen, change its orientation | `optisigns_screen_update` |
| | Pair a new screen with its on-screen pairing code; unpair one | `optisigns_screen_pair`, `optisigns_screen_unpair` |
| Content | Upload images, video, audio, PDFs and Office files (incl. PowerPoint) | `optisigns_asset_upload_from_url`, or `optisigns_asset_upload_begin` → upload → `optisigns_asset_upload_finish` |
| | Add a website, a dashboard page or an OptiDev project | `optisigns_asset_create` with a URL |
| | Add a built-in app (weather, feeds, Google Slides, Power BI…) | `optisigns_app_manifest` → `optisigns_asset_create` |
| | Find, rename, update or delete content | `optisigns_asset_list/search/get/update/delete` |
| Playlists | Create, edit, reorder, set durations, duplicate, delete; see where one is used | `optisigns_playlist_*` |
| Schedules | Show content on certain days and hours, one-off or repeating | `optisigns_schedule_*`, `optisigns_schedule_repeat_presets` |
| On screen | Put content, a playlist or a schedule on one or many screens; cancel a scheduled push | `optisigns_screen_assign_content`, `optisigns_screen_cancel_scheduled` |
| Organize | Folders for content, playlists, schedules and screens | `optisigns_folder_*` |
| Design | Make the content itself (slides, images, pages) in the assistant's own workspace | `signage-design` skill |
| Advice | Setup, devices, plans, best practices, rollout | `optisigns-expert` skill |
| Ideas | What to show next: upcoming holidays and events for their location, time changes, content that has expired on their screens, ideas that fit their industry; each as a ready-to-send request, reads only | `optisigns-suggest` skill |

Every change that alters what a screen shows, or deletes something, asks for the user's confirmation
first. Deletes move items to Trash, restorable in the portal for 30 days.

## Needs the OptiSigns portal or support

Say so plainly and link the right place; don't improvise a workaround.

- Billing, plan changes, invoices, payment methods → the portal's billing page or support.
- Users, roles, permissions, inviting teammates, creating teams → the portal.
- Account settings and turning features on (including the AI connector toggle) → the portal, by an
  account owner or admin.
- Physical setup: buying players, mounting, network, installing the player app → Help Center
  ([getting-started.md](getting-started.md)), pairing is then possible here with the code on screen.
- Engage / kiosk hardware, video walls, MDM device management → `optisigns-expert` for guidance, then the
  portal.
- Restoring from Trash, and deleting operational (power/CEC) schedules → the portal.
- Deleting the account → support.
