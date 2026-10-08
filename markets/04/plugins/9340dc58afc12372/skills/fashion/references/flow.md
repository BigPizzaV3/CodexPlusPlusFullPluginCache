# Fashion picker sequence

One call per turn. Wait for the user's choice before the next.

1. `select_folder` — where the work lands
2. `select_fashion_project` — takes the folder from step 1
3. `select_fashion_models` — who wears it
4. `select_fashion_wardrobe` — **optional**; skip when no specific garment is named
5. `select_fashion_background` — where the shoot happens
6. `select_fashion_pose` — how they stand
7. `generate_fashion_photoshoot` — run it
8. `show_fashion_generations` — display results (`org_id` + `fashion_project_id`)

## Entity management

These exist so a brand builds a reusable library. Offer them when the user is setting up,
not mid-shoot.

| Purpose | Tools |
|---|---|
| Models | `create_fashion_model`, `list_fashion_models`, `update_fashion_model`, `restyle_fashion_model`, `generate_fashion_model_image` |
| Outfits | `create_fashion_outfit`, `list_fashion_outfits`, `update_fashion_outfit` |
| Shot settings | `create_fashion_shot_setting`, `list_fashion_shot_settings`, `update_fashion_shot_setting` |
| Projects | `create_fashion_project`, `list_fashion_projects`, `update_fashion_project` |
| Styling | `list_fashion_styling` |

Deletes (`delete_fashion_model`, `delete_fashion_outfit`, `delete_fashion_project`,
`delete_fashion_shot_setting`, `delete_fashion_asset`) are destructive — confirm first.

## Viewing results

- `show_fashion_generations` — visual grid; takes `org_id` and `fashion_project_id`
- `list_fashion_generations` — rows, when you need to reason over them
