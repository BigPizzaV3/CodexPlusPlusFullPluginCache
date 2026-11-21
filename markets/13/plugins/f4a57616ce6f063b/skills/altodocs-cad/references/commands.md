# CAD command groups

Generated from the native catalog and checked by `catalog-workspace-tools.mjs`.
These are tool names, not substitute schemas. Use the live schema for arguments,
units, bounds and returned IDs. All mutate a saved native file except the read
and audit commands marked read-only by the host.

## Read and audit

`cad_read_drawing`, `cad_read_entities`, `cad_read_layouts`, `cad_check_text_fit`, `cad_check_paper_fit`.

## Geometry and shapes

`cad_add_line`, `cad_add_circle`, `cad_add_arc`, `cad_add_rectangle`, `cad_add_polyline`, `cad_add_plate`, `cad_add_spline`, `cad_add_ellipse`, `cad_add_point`, `cad_add_construction_line`, `cad_add_polygon`, `cad_add_donut`, `cad_add_wipeout`.

## Text and annotations

`cad_add_text`, `cad_add_table`, `cad_update_table`, `cad_add_note_block`, `cad_update_note_block`, `cad_merge_text_into_note_block`, `cad_add_hatch`, `cad_add_dimension`, `cad_add_leader`, `cad_update_leader`, `cad_add_revision_cloud`, `cad_set_dimension_style`, `cad_space_text`.

## Edit and transform

`cad_break_entity`, `cad_join_entities`, `cad_explode_entities`, `cad_group_entities`, `cad_ungroup_entities`, `cad_divide_entity`, `cad_lengthen_entity`, `cad_stretch_entities`, `cad_align_entities`, `cad_move`, `cad_duplicate`, `cad_rotate`, `cad_scale_entities`, `cad_mirror`, `cad_mirror_copy`, `cad_offset`, `cad_array`, `cad_trim`, `cad_extend`, `cad_fillet`, `cad_chamfer`, `cad_update_style`, `cad_edit_geometry`, `cad_delete_entities`, `cad_clear_drawing`.

## Blocks and layers

`cad_set_block_attributes`, `cad_insert_block`, `cad_make_block`, `cad_explode_block`, `cad_rename_block`, `cad_create_layer`, `cad_set_active_layer`, `cad_set_layer_props`, `cad_delete_layer`.

## Paper and presentation

`cad_set_branding`, `cad_create_layout`, `cad_rename_layout`, `cad_delete_layout`, `cad_set_layout_properties`, `cad_add_viewport`, `cad_update_viewport`, `cad_delete_viewport`, `cad_set_title_block`, `cad_add_revision`, `cad_set_layout_annex`.
