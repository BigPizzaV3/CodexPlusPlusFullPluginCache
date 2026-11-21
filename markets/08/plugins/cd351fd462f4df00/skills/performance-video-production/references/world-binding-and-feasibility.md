# World binding and feasibility

## Exact authority is not a 2D overlay rule

Keep final authority for Japanese, UI, reports, claims, price, logo, and CTA deterministic. Choose the visual realization that lets the exact surface inhabit the approved world:

- `screen_native`: the viewer is looking at the actual UI or editorial surface;
- `planar_track` or `corner_pin`: bind exact content to a stable plane in generated footage;
- `uv_texture_3d`: map exact content onto deterministic 3D geometry and share camera, depth, light, and occlusion;
- `final_frame_repair`: use generation for motion, then restore only declared readable anchors;
- `motion_scaffold_v2v`: define camera and object geometry deterministically, then let generation supply finish and atmosphere.

Do not treat fixed screen coordinates as a valid binding mode for an object that is supposed to float, turn, pass behind a subject, or share a moving camera.

## `PREPRODUCTION_FEASIBILITY`

Accept an approved Animatic plus selected `visual-treatment-contract.json` before the immutable production handoff exists. This mode is local and non-paid.

1. Confirm the selected Treatment and input hashes.
2. Build the smallest final-fidelity proof that can falsify the binding route.
3. For screen-native surfaces, prove hierarchy, readability, and look match.
4. For world-bound surfaces, prove relative motion, perspective, occlusion, look match, and readable anchors. Prove trackability when the route depends on tracking.
5. Record evidence refs for every machine check. Derive the gate status from those checks; never accept a typed `PASS` without evidence.
6. Require human Taste only for a new grammar, a primary world-bound exact semantic surface, or high world-binding risk. Do not force moving proof for a known static screen-native End Card.
7. Return `PASS`, `FAIL`, or the smallest Treatment/binding decision needed. Do not choose a paid model in this mode.

The proof can be a local 3D/2.5D composite, tracked mock, or other non-paid artifact. It is not required to be a provider-generated clip.

## Production use

After handoff v4, preserve the approved object ownership and binding mode. If a generated Raw cannot support the approved binding, reject the Raw or return a blocker. Do not rescue it by placing a second screen-space object over the same semantic object.
