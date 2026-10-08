# Ad picker sequence

One call per turn. Wait for the choice before the next.

1. `select_product` — what is advertised
2. `select_avatar` — who presents it
3. **Format** — if the user named one, `list_formats` resolves it to a numeric `format_id`.
   If they named none, `select_format` renders a picker.
4. `select_hook` — the opening beat
5. `select_setting` — where it takes place
6. `select_folder`, then `select_market_project` (which takes that folder)
7. `generate_ad`

## Required arguments on generate_ad

`duration` and `resolution` are **required**, not optional. Resolve them first:
- `list_durations` — ad lengths with cost notes
- `list_resolutions` — quality tiers with cost notes

Match a user-named value; otherwise present the options and let them choose.

## Product management

`create_product`, `update_product`, `list_*`, `upload_market_image`,
`fetch_product_status`. `delete_product` is destructive — confirm.

## Not available

`generate_product_ad` and `generate_ugc_tryon` exist in the server source but are **not
registered as MCP tools** — they are not callable. For a polished product clip without a
presenter, use Product Studio. For try-on, use the Try-On skill's `composite_shoot` path.
