---
name: crack-width-calculation
description: Use for calculating and verifying flexural surface crack widths in reinforced concrete beams and slabs in accordance with Indian Standard IS 456:2000 Annex F and exposure serviceability limits.
---

# Crack Width Calculation (IS 456:2000 Annex F)

Use the registered StructEngine MCP tool `calculate_crack_width` as the calculation and structural verification authority for flexural crack widths in reinforced concrete members.

## Downloadable report

The end product is the tool-generated **Download PDF**, alongside a brief summary. Present its actual link, filename and expiry immediately; do not ask a second export question. If the tool returns a native OAuth linking challenge, let ChatGPT connect the user's StructEngine account and retry the same arguments. Reuse valid authorization without repeated sign-in prompts; never request passwords, tokens or authorization codes in chat. Preserve failed design checks and warnings in the summary. If export fails or the deployed tool lacks PDF support, say no PDF was delivered; never invent a link or silently substitute a model-written report.

## When to Use

Use this skill whenever a user:
- Requests crack width checks for RC beams or slabs per IS 456:2000 Annex F.
- Asks whether a given beam reinforcement layout satisfies serviceability crack width limits under a service moment.
- Inquires about permissible crack width limits under various environmental exposures per IS 456 Cl. 35.3.2 (0.3 mm for mild, 0.2 mm for moderate/severe, 0.1 mm for very severe/extreme or water-retaining structures).
- Asks for cracked elastic neutral axis depth `x`, average tension strain `eps_m`, or distance to nearest reinforcing bar `a_cr`.
- Designs singly or doubly reinforced beams with optional top compression reinforcement.

## Input & Execution Guidelines

1. **Tool Invocation**: Call `calculate_crack_width` with the geometric dimensions, materials, and service loading. Never attempt to guess or hallucinate Annex F formula results manually.
   - `element_type`: `"beam"` or `"slab"`.
   - `fck`: Concrete grade in MPa (e.g., 20, 25, 30, 35, 40).
   - `fy`: Steel yield strength in MPa (e.g., 415, 500, 550).
   - `clear_cover`: Clear cover in mm (typical 25 to 50 mm).
   - `overall_depth`: Total depth `D` in mm.
   - For Beams (Tension Steel): `width` (`b`), `num_bars_layer1`, `bar_dia_layer1`, optional layer 2 bars (`num_bars_layer2`, `bar_dia_layer2`), and unfactored `service_moment` in kN-m.
   - For Beams (Compression Steel, Optional): `num_comp_layer1`, `bar_dia_comp_layer1`, optional layer 2 compression bars (`num_comp_layer2`, `bar_dia_comp_layer2`). If provided, the tool performs doubly reinforced transformed cracked-section analysis.
   - For Slabs: `spacing` (c/c bar spacing in mm), `bar_dia_slab`, and `service_moment_slab` in kN-m/m.
   - `exposure`: `"mild"`, `"moderate"`, `"severe"`, `"very_severe"`, `"extreme"`.

## Presentation Guidelines

1. **Verdict & Summary**: State whether the member passes serviceability criteria (`PASS (SAFE)` or `FAIL (EXCEEDS LIMIT)`), showing calculated `w_cr` vs the allowable limit `w_lim`.
2. **Governing Location**: Display the governing critical check location (e.g. `Beam Corner` or `Midpoint between bars`) and distance `a_cr`.
3. **Key Strains & Depths**: Tabulate the neutral axis depth `x`, average tensile strain `eps_m`, and reinforcement type (singly or doubly reinforced).
4. **Exposure Compatibility**: List all environmental exposure classes for which the section is safe.
5. **Engineering Notes**: Note that Annex F assesses flexural cracking under service loads; early thermal contraction and shrinkage cracking must be addressed through adequate distribution steel and proper curing.
