---
name: model-target-check
description: Check that every 3D part and object that a Simplio3D configurator's options, rules and animations target really exists in the model files, and explain the 3D scene. Use when the user asks whether their Simplio3D options point at the right parts, why a material or option changes nothing on the 3D model, what parts or meshes a Simplio3D model contains, or where a part sits in the scene.
---

# Check 3D targets in a Simplio3D project

Read-only. Resolve the project by name first (workspace-navigation skill). The user's explicit instructions take priority over this guidance, within what this read-only version can do.

Simplio3D targets 3D parts **by mesh name**. A name that isn't in the model file silently does nothing: the option saves, the page loads, and nothing changes on the model. That is what this check finds.

## Steps

1. `validate_project` with `deep: true`. It opens the project's model files (the first few) and cross-checks every part name options, rules and animations use. Look for `part-target-unknown`, `rule-part-unknown`, `rule-3d-object-unresolved`, `variant-target-model-missing`, `animation-part-unknown` and `texture-target-missing`.
2. For each missing name, find what the model really contains:
   - `list_model_parts` for a model's mesh names (flat list with paths),
   - `find_scene_objects` to search parts by name,
   - `get_scene_hierarchy` for the nested groups.
3. Suggest the closest real name for each missing one, and say which option or rule uses it. Don't claim a match you haven't seen in the tool results.

## Explain the scene

- `get_scene_hierarchy`: the model's groups and parts, addressed by slash-separated paths.
- `get_object_details`: one part's position, rotation, scale and bounds, and which options or rules reference it.
- `get_object_spatial_context`: where a part sits relative to others (regions, neighbours, relative size), computed from the geometry. Use it instead of guessing positions.
- `get_model_pivots`: each model's Edit Axis pivot. Number inputs that resize parts do not use it: a part grows around its own origin in the 3D file, so a part that grows the wrong way needs its origin moved in the 3D modelling tool.

## Things to know

- Material options and part visibility work on meshes. A name that is a **group** in the file matches nothing for them; conditional rules can hide whole groups.
- Two meshes with the same name in different groups are both targeted by that name.
- After a model is replaced with a new version, parts that were renamed or merged stop matching. `validate_project` flags them.
- A material option that changes nothing on the model can also be pointing at a 3D object that is no longer in the scene (finding: variant-target-model-missing). Retargeting the option fixes it.

## Fixing targets

This version doesn't change projects. Tell the user which option or rule to retarget and to which part; they pick the parts in the option's target list in the Simplio3D editor.
