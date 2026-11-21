---
name: rtlca-map-material
description: >-
  Use when a user asks to map, remap, assign, link, or connect RTLCA project
  inventory materials to EPDs. Guides safe manual mapping: resolving project
  materials, checking lifetimes and quantities, finding relevant EPDs, handling
  compatible declared units including mass-volume density conversion between
  kg/g/t and m3, confirming writes with the user, mapping via
  rtlca_map_materials, and verifying the final mapping and lifetime.
---

# RTLCA Map Material

Use this skill for manual, user-approved mapping of RTLCA project inventory materials to EPDs.

Do not call automapping tools from this skill. Every mapping or remapping must be deliberate, specific, and verified afterward.

## Core Rules

1. Never call `rtlca_map_materials` unless the user has explicitly approved the exact project material to EPD mapping.

2. Treat remapping differently from mapping.
   - Mapping an unmapped material may increase mapping coverage.
   - Remapping an already mapped material usually changes GWP but not coverage.
   - Always report whether the target was previously mapped.

3. Check quantity and lifetime before mapping.
   - The target inventory material must have a non-zero quantity in a compatible unit.
   - The material must have a non-zero `lifeTime`.
   - If lifetime is missing, look up the BR18 value with `rtlca_get_reference_data` (`type: "lifetime-table"`), confirm it with the user, and set it with `rtlca_update_material_properties` (`updates: [{ materialId, lifetime }]`) before mapping.

4. Declared-unit compatibility.
   - Mass and volume are cross-compatible: `G`, `KG`, `T` and `M3`.
   - This works because RTLCA can normalize through EPD density/mass metadata.
   - Strict units: `M2` maps only to `M2`, `M` maps only to `M`, and `PCS` maps only to `PCS`.
   - Do not reject a kg EPD for an m3 inventory material, or an m3 EPD for a kg inventory material, if the EPD has density/mass metadata.
   - If a mass-volume mapping fails, check whether the EPD is missing density/mass metadata before assuming incompatibility.

## Workflow

1. Resolve the project.
   - Use `rtlca_list_projects` if the project ID is unknown.
   - Confirm ambiguous project matches.

2. Resolve target inventory materials.
   - Prefer `rtlca_get_inventory_materials` with `detail: "detailed"` for flat material lookup. The default compact rows lack `typeIdentifier`, `lifeTime` and `includeMapping`.
   - Search by material name, type identifier, or category.
   - Collect `materialId`, `identifier`, `typeIdentifier`, `branchName`, `category`, quantities and preferred unit, `lifeTime`, current `mappedEpd`, and `includeMapping`.

3. Resolve declared unit labels.
   - Call `rtlca_get_reference_data` with `type: "declared-units"`.
   - Do not hard-code enum labels.
   - Determine whether the material has a non-zero quantity in the exact strict unit or in the mass-volume compatibility group.

4. Find candidate EPDs.
   - Start with `rtlca_find_relevant_epd_materials`.
   - Build the search description from `identifier`, `typeIdentifier`, `category`, `branchName`, and useful synonyms.
   - Pass the material's preferred unit as `declaredUnits` (an array of declared-unit int enums).
   - For mass/volume materials, one relevance-finder call is enough because the tool expands across the mass-volume group.
   - For strict `rtlca_search_materials` searches, remember declared-unit filtering is exact.

5. Present shortlist.
   - Show 3-8 candidates.
   - Include EPD name, owner, declared unit, density/mass metadata when relevant, and EPD id.
   - Prefer locally appropriate EPDs, but do not hide better user-requested manufacturer EPDs.

6. Confirm before writing.
   - State the inventory material, current mapping if any, target EPD, whether this is mapping or remapping, lifetime, and unit conversion if any.
   - Wait for explicit approval unless the user's message already clearly says to map this exact material to this exact EPD.

7. Map.
   - Call `rtlca_map_materials` with `projectId` and `mappings: [{ materialId, mappedMaterialId, includeMapping: true }]` unless the user says otherwise.
   - Check each result's `status`: `mapped` is confirmed stored, `not_applied` means the project still shows another mapping, `not_found` means the materialId is wrong.
   - Do not set `isAutoMapping`.

8. Verify.
   - Re-fetch the mapped inventory row with `rtlca_get_inventory_materials` (`materialIds: [materialId]`, `detail: "detailed"`).
   - Confirm `isMapped: true`, `mappedEpd.id`, `mappedEpd.name`, `lifeTime`, and `includeMapping`.
   - If possible, report whether mapping coverage changed. For remaps, say coverage likely did not change.

9. Handle errors.
   - If the error says incompatible units or lifespan not set, first check `lifeTime`.
   - Then check unit compatibility.
   - Remember mass-volume is allowed if density/mass metadata exists.
   - If kg-to-m3 or m3-to-kg fails despite density metadata, flag it as a possible backend or tool regression.

## Output

After mapping, respond with the mapped material row, previous EPD if any, new EPD, lifetime after mapping, whether it was a map or remap, and verification result.

Keep it short unless the user asks for full details.
