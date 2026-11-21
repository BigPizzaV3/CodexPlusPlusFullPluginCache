# Tool workflows

Use the live tool schemas. The catalog contains 25 named tools; command variants
below are a closed set, not a general REST executor.

| Work | Tools |
|---|---|
| Project discovery and saved script reads | `list_projects`, `get_project`, `get_script_project` |
| Create, update, promote, and comment | `create_project`, `update_project`, `promote_idea`, `add_project_comment` |
| Assigned work and notifications | `list_my_work`, `mark_project_notifications_read` |
| Public YouTube research | `search_youtube_channels`, `search_youtube_videos`, `get_youtube_channel`, `get_youtube_video` |
| Idea generation and operation status | `generate_ideas`, `get_operation` |
| Channel overview and template retrieval | `get_channel_workspace` |
| Research library and bookmarks | `list_research_videos`, `get_research_video`, `list_research_bookmarks`, `save_bookmark` |
| Custom templates and writing voices | `save_template`, `validate_voice_profile`, `commit_voice_profile` |
| Thumbnail Studio | `get_thumbnail_board`, `edit_thumbnail_board` |

## Channel and Project details

`get_channel_workspace` commands: `overview`, `list_channels`, `get_channel`,
`get_template`. Read template summaries before fetching a specific full prompt;
do not request every template's prompt by default.

`update_project` commands: `edit_fields`, `move`, `archive`, `restore`. Read the
current Project and revision first. Stages come from the tool schema; do not
invent stages. `save_template` supports `create`, `update`, `archive`, `restore`
for custom templates only. `mark_project_notifications_read` supports `one`,
`many`, `all`; use only the scope the user requests.

Voice changes require a complete Voice Profile v2 document. Validate it first,
show the normalized profile and diff, then commit only the explicitly approved
receipt-bound version. Do not guess missing fields or silently migrate a legacy
voice profile.

## Thumbnail commands

Every command uses the resolved `channel_id`.

| Command | Main arguments and result |
|---|---|
| `add_images` | `source` is `my_recent`, `my_top_viewed`, `my_top_outlier`, or `urls`; public HTTPS `urls` apply only to `urls`. Optional `usage` identifies creator face, style, product, background, or screenshot references. |
| `generate_variations` | `prompt`, optional `reference_item_ids` and `variations`; explicit credit approval and `confirm` required. Returns work in progress. |
| `edit_image` | One ready `item_id` and `instruction`; optional fractional `region` and `preserve_layers`. Creates a new image, preserving the original. Requires credit approval and `confirm`. |
| `set_text` | Creates or updates text overlays using `content`, positioning, and supported styling. Read item IDs before updating an existing overlay. |
| `export_image` | One ready `item_id`; flattens that image and overlaid text into a finished 1280×720 PNG. |
| `assign_image` | One ready `item_id` plus `script_id` on the same Channel; replaces the selected Script thumbnail without generation. Follow preview/confirmation. |
| `add_person_photo` | `name` and a team-owned Studio upload `url`. Arbitrary third-party photo URLs are rejected. A new upload needs the separately authenticated website/API; this MCP tool does not accept binary uploads. |
| `rename_person` | Read `asset_id` first, then supply the approved `name`. Renames grouped photos for that person. |
| `set_default_person` | Use a returned `asset_id` to select the person used by default. |

`get_thumbnail_board` returns saved people and photo asset IDs. Do not confuse
person asset IDs, thumbnail board item IDs, Script IDs, and typed Project IDs.
Use the field corresponding to each tool schema.
