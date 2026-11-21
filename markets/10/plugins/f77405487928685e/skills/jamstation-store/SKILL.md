---
name: jamstation-store
description: Manage the OAuth-linked JamStation store's music playlists, voice advertisements, schedules, volume, and profile through the JamStation MCP. Use for store audio operations, not on-demand song playback or general music research.
---

# JamStation store operations

Use the connected JamStation MCP and its current tool schemas to operate only the currently linked store. Obtain IDs from the corresponding list/get tools; never invent store data, IDs, campaign details, or tool results. If authentication or linking is required, direct the user to the connection or linking flow supplied by the service. Do not collect passwords, PINs, or tokens in chat. LINE account rebinding and password changes are not MCP capabilities.

Respond in the user's language and honor their language preferences; default to Traditional Chinese when no language can be determined. Report useful names, IDs, times, and enabled status from actual results rather than dumping raw JSON. The MCP cannot start individual songs, report live device playback telemetry, or proactively push ad preview audio.

## Changes and side effects

- Writes take effect immediately; MCP has no LINE confirmation buttons. Present the concrete parameters and effects and obtain explicit consent before each write. Explain irreversible asset/schedule deletion and cross-store distribution when applicable. Removing a favorite is reversible by adding it again.
- Use `readOnlyHint` rather than tool names or HTTP methods to identify writes. `generate_ad_script`, `get_current_ad`, and `select_external_ad_for_store` also change state. The latter two may overwrite selection history and increase play counts; use `get_ad_queue` for read-only schedule queries.
- Read current state before updates unless the user supplies every necessary field. Preserve unchanged required profile fields using `get_profile`; `update_alerts` replaces the complete alert-code array.
- Do not blindly retry `idempotentHint=false` tools after an unknown outcome. Inspect the corresponding lists or generation status first. Explain additional quota/count effects before repeating generation or selection.

## Dates and schedule conflicts

Call `get_current_time` to resolve relative dates in Asia/Taipei. Use `HHmm` values and comma-separated weekdays `1` (Monday) through `7` (Sunday). Start times cannot be `2400`; an end time of `2400` means the end of the day. Use the argument types in the live tool schemas.

Before playlist writes, use `check_schedule_conflict`; before volume schedule writes, use `check_volume_schedule_conflict`. For updates, exclude the current schedule from conflict checks. `jobType=daily` uses weekdays; `jobType=event` uses dates, and these are separate conflict pools.

For playlist/volume conflict resolutions, `replacements` describes retained intervals after shortening or splitting existing schedules; an empty array deletes the affected schedule. Show all affected intervals and obtain consent. Do not shift existing slots forward or backward on your own.

Only enabled, fixed-time (`type=2`) in-store ad schedules conflict. Before creating, changing type, or enabling one, use `check_instore_schedule_conflict`, passing `excludeScheduleId` on updates/enabling. Frequency-based (`type=1`) schedules do not conflict. In-store ads do not support replacements: propose other times/days/dates or disabling conflicting schedules. A write returning `{ blocked: true }` did not complete; explain the conflict and do not retry identical arguments.

## Playlists and volume

Browse with `list_catalog_playlists` and inspect choices with `get_playlist_detail`. Catalog playlists can be scheduled directly with `playlistSource=category`, without favoriting. Use `list_playlists` for favorites and `playlistSource=collect`; use `playlistSource=smart` with an empty `playlists` array for automatic recommendations. Favorite changes also require consent.

Read `get_current_volume` or `get_volume_schedules` for volume questions. When the user has not specified levels, propose BGM `volume=60`, `adVolume=90`, and `bgmVolumeDuringAd=30` as adjustable defaults, then obtain consent before applying them.

## Voice advertisements

1. Inspect `get_ad_edit_limits` and `list_voice_sources` for available quota, valid voice IDs, language, and content limits. Obtain existing ad IDs with `list_advertisements` or `get_advertisement`.
2. For AI copy, confirm business style and promotion content without inventing prices, discounts, or deadlines. Explain that `generate_ad_script` sends these details to JamStation's AI copy service, consumes daily quota, and logs usage; `type=2` also includes the existing store name and city/district. Obtain consent before generation.
3. Let the user select a generated candidate. Propose the title, voice, and final copy, and obtain consent before `create_advertisement`. Use `contentCreatedSource=AI_GENERATED` for generated copy, `HUMAN_CREATED` for fully user-written copy, or a schema-supported assisted value for user-edited AI copy. Never use reserved system provenance values.
4. Check `get_advertisement` after creation to report actual TTS status. Do not describe pending generation as ready. Before updating an ad, inspect it and obtain consent to disable any enabled schedules/broadcasts that block editing. Never re-enable those automatically.

## In-store ads and external broadcasts

Use `list_instore_schedules` to identify existing in-store schedules. For `create_instore_schedule`, supply an integer `type`: `1` plays every `frequency` minutes (commonly 30); `2` plays at a fixed time with `startTime=endTime`. Daily weekdays are `1,2,3,4,5,6,7`. `campaignType=PERMANENT` omits dates; `DATE_RANGE` requires both dates in ascending order. Check applicable conflicts before requesting write consent.

Use `list_external_ad_broadcasts` to obtain broadcast IDs. Verify the advertisement's TTS completion before creating or enabling a broadcast. Explain that an enabled external broadcast distributes to other stores and obtain explicit consent for that effect. Do not substitute realtime external-ad selection for creating a broadcast.
