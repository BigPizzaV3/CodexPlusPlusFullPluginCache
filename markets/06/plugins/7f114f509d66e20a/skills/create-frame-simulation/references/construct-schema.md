# Frame simulation schema

Use one structure for the teaching illustration, worksheet and 3D simulator. List support levels proximal to distal.

```json
{
  "laterality": "left",
  "fracture_level": 46,
  "segmental_pattern": true,
  "bone_defect": false,
  "defect_height_cm": 11,
  "construct_text": "Exact educational construct description",
  "simulation_title": "Segmental tibia teaching example",
  "learning_objective": "Compare fixation geometry across support types",
  "teaching_notes": "Observations and circular-fixation principles",
  "construct_checks": "CHECK ...",
  "workspace": "three-d",
  "rings": [
    {
      "level": 92,
      "ring_type": "two-thirds",
      "rotation_degrees": 315,
      "wire_count": 2,
      "half_pin_count": 1,
      "half_pin_mount": "rancho-post",
      "connector_to_proximal": "rods",
      "connector_count": 4
    }
  ]
}
```

## Field rules

- `laterality`: `left` or `right` for orientation teaching.
- `fracture_level`: schematic tibial level, where 0 is distal and 100 is proximal.
- `rings`: one to eight supports, ordered proximal to distal.
- `level`: 0–100 for tibial supports; foot plates use `-8`.
- `ring_type`: `full`, `two-thirds`, or `foot`.
- `rotation_degrees`: independent 0–360° axial rotation for a 2/3 ring. Attached wires, half-pins and Rancho posts rotate with it.
- `wire_count`: 0–6 fine wires at that support.
- `half_pin_count`: 0–6 half-pins at that same support. A support may contain both types.
- `half_pin_mount`: `direct` or `rancho-post`.
- `connector_to_proximal`: `rods`, `trauma`, or `hexapod`. These values never represent Rancho posts.
- `connector_count`: 3 or 4 for longitudinal Ilizarov rods. A hexapod interval always uses six struts.
- Legacy fixation fields remain accepted for older links, but new simulations should use independent counts.
- Put unresolved educational questions in `construct_checks` with a `CHECK` prefix.

## Verification

Call `apply_frame_construct`, then `get_frame_construct`. Compare laterality, support order, 2/3-ring rotations, wire and half-pin counts, half-pin mounting, rod count and every connector interval.

## Fallback link

The fallback URL carries hardware geometry only. Do not put identifying details or free text in it.

```text
https://trauma-frame-planner.nicholasnoye.chatgpt.site/?side=left&fracture=46&segmental=1&defect=0&defectHeight=11&mode=three-d&ring=92,two-thirds,2,1,rancho-post,rods,4,315&ring=48,full,0,3,direct,trauma,4,0&ring=13,full,2,0,direct,hexapod,4,0
```

Each repeated `ring` value is:

```text
level,ring_type,wire_count,half_pin_count,half_pin_mount,connector_to_proximal,connector_count,rotation_degrees
```
