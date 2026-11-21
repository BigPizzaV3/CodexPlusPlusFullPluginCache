# ScriptNib MCP tool map

Use this map for routing. Live tool descriptions and schemas are authoritative.

## Discovery and house workflow

- `list_projects`, `get_project`: screenplay discovery, metadata, ordered scenes, pages.
- `list_manuscripts`, `get_manuscript`: Novel workspace discovery and chapter structure.
- `get_instructions`: required first call for `format`, `breakdown`, `loglines`, `story_analysis`, and `fill_development` requests.

## Screenplays and notes

- Read/find: `read_scene`, `read_range`, `search_script`, `read_script_notes`, `get_revisions`.
- Edit: `apply_edit` replaces screenplay elements after review and approval; `rename_character_or_location` updates the script and linked production/development data globally.
- Notes: `write_script_note` adds or replies to notes; deletion requires care because replies are removed too.
- Settings/art: `edit_project_settings`, `set_title_logo`.
- Legacy only: `list_suggestions`, `withdraw_suggestion` do not create modern edits.

Screenplay elements are `slug`, `action`, `char`, `paren`, `dial`, `trans`, `center`, and `fadein`. Read the exact range before editing. Version History entries are created by the author pressing Save, not by `apply_edit`.

## Development

- `get_development`: story fields, beat template/notes, characters, outline cards, drafts, script-scene links.
- `update_development`: merges story/beats/characters; a supplied scene-card array replaces the entire outline, so retain every card and id.
- `insert_scene_draft`: inserts or, when explicitly requested, replaces a linked screenplay scene.

## Novels

- Read/find: `read_chapter`, `search_manuscript`, `read_notes`.
- Targeted edits: `replace_text`, `replace_section`, `write_note`, `write_notes`.
- Structural edits: `insert_chapter`, `move_chapter`, `split_chapter`, `merge_chapters`, `rename_chapter`, `renumber_chapters`, `delete_chapter`.
- Full replacement: `edit_chapter` requires the complete current chapter text.
- Typography/recovery: `smart_quotes` defaults to preview and snapshots before apply; `restore_snapshot` lists or restores Novel snapshots.

No MCP tool creates or exports a manuscript.

## Breakdown, locations, and visual planning

- `get_locations`: script-derived locations, scenes, and cast.
- `list_breakdown`, `add_breakdown_tags`, `update_breakdown_tags`, `remove_breakdown_tags`: inspect before tagging; keep names consistent with words in the scene and confirm changes.
- `get_moodboard`, `edit_moodboard`: boards, frames, notes, swatches, and layout. Image upload is not exposed through MCP.
- `list_shots`, `add_shots`, `update_shot`, `remove_shots`: inspect the scene and existing board first; confirm mutations.
- `set_shot_image`, `set_shot_images`, `get_shot_image`: use original-resolution files for board drawings; confirm replacement.

## Schedule, plan, contacts, and call sheets

- `get_schedule`: shoot days, dates, scenes, breaks, unscheduled scenes, Day Out of Days.
- `set_schedule_settings`, `edit_shoot_days`, `schedule_scenes`: confirm date changes, auto-scheduling, and scene moves; read the current schedule first.
- `get_plan`: five-stage timeline, jobs, dependencies, milestones, contacts, call-sheet state, and delivery items.
- Jobs: `add_work`, `update_work`, `remove_work`.
- Milestones: `add_milestones`, `update_milestone`, `remove_milestones`.
- Contacts: `add_contacts`, `update_contact`, `remove_contacts`. Script-linked locations and cast must match ScriptNib names exactly.
- Call sheets: `get_call_sheet`, `set_call_sheet`. ScriptNib derives scenes, pages, sets, and cast; write only confirmed times, unit details, notes, actor calls, and exceptional crew calls.

Report dependency-driven date changes returned by timeline tools. Removal tools have no undo and require explicit approval.

## Budget

- `start_budget`: creates the standard industry chart once; never overwrites an existing budget. Confirm first.
- `get_budget`: read topsheet or a specific account; permissions are enforced by ScriptNib.
- `edit_budget`: read first, use sub-account numbers and existing line ids, preserve auto-derived globals, mark equipment/rentals/purchases/allowances as non-labor, and confirm the proposed total effect.

## Delivery

- `edit_deliverables`: add/change/remove Picture, Sound, Text, Legal, or Publicity items after reading `get_plan`.
- `export_document`: supported kinds are screenplay PDF, tagged PDF, Final Draft, Word, sides, call sheet, stripboard, one-liner, Day Out of Days, breakdown PDF/CSV, budget PDF/CSV, storyboard, and delivery schedule.

Default export is a private one-hour link. Email can go only to the user's account address. Text output is only for breakdown and budget CSV. Sides and call sheets require a `shoot_day_id` from `get_schedule`.

## Important boundaries

- Revision colors can be read with `get_revisions` but issued only in Production → Revisions.
- A new screenplay can be created with `create_project`; there is no corresponding manuscript-creation tool.
- Never infer permissions for budgets or documents; call the tool and relay an access refusal.
- Never claim a write, export, email, or schedule change succeeded unless its tool result confirms it.
