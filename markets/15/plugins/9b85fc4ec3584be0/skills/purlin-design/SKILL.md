---
name: purlin-design
description: Use for designing and verifying cold-formed steel purlins (Z-sections and C-channels) according to Indian Standard IS 801:1975, including biaxial bending, web shear, combined web interaction, web crippling, deflection limits, and sag rod bracing.
---

# Cold-Formed Steel Purlin Design (IS 801:1975)

Use the registered StructEngine MCP tool `design_purlin` as the calculation and structural verification authority for cold-formed steel roof purlins.

## Downloadable report

The end product is the tool-generated **Download PDF**, alongside a brief summary. Present its actual link, filename and expiry immediately; do not ask a second export question. If the tool returns a native OAuth linking challenge, let ChatGPT connect the user's StructEngine account and retry the same arguments. Reuse valid authorization without repeated sign-in prompts; never request passwords, tokens or authorization codes in chat. Preserve failed design checks and warnings in the summary. If export fails or the deployed tool lacks PDF support, say no PDF was delivered; never invent a link or silently substitute a model-written report.

## When to Use

Use this skill whenever a user:
- Requests design, sizing, or verification of cold-formed steel purlins for industrial buildings, warehouses, pre-engineered buildings (PEBs), or roof trusses per IS 801:1975.
- Asks whether a specific cold-formed profile (e.g., `Z20020`, `Z20015`, `Z25020`, `C20020`) is structurally safe for a given roof bay span, purlin spacing, and roof pitch/slope.
- Needs to check combined biaxial bending stresses, lateral-torsional buckling, web shear stress, combined web bending and shear interaction, web crippling at supports, or deflection under dead, live, and wind uplift loads.
- Asks for sag rod recommendations (e.g., 0, 1 mid-span, or 2 third-point sag rods) to brace the minor axis.
- Supplies custom or non-standard cold-formed profile dimensions (depth, flange widths, thickness, lip depth, and sectional properties).

## Input & Execution Guidelines

1. **Tool Invocation**: Call `design_purlin` with the geometric, loading, and support parameters. Always use the deterministic remote calculator; never perform manual or hallucinated stress and capacity calculations. Check the registered tool schema first: if support options or shear/interaction results described below are absent, report an outdated server interface and request its update. Do not silently discard requested options or claim the current complete verification is available.
2. **Profile Selection**:
   - Provide standard profile designation via `profile_name` (e.g., `Z20020`, `Z20015`, `Z20024`, `Z25020`, `C20020`, `C15015`).
   - Profile types: `Z45` (standard Z-section with 45° lips), `Z90` (Z-section with 90° lips), or `C` (lipped channel). If omitted, inferred automatically from the profile name prefix.
   - For custom sections, provide `manual_section` with `thickness`, `depth`, `flange_width_tp`, `flange_width_bt`, `lip_depth`, `Ixx`, `Iyy`, `Zxx_tp`, `Zxx_bt`, `Zyy`, `area`, etc.
3. **Geometry & Bracing**:
   - `span`: Bay length / purlin span in meters (1.0 to 12.0 m).
   - `spacing`: Purlin spacing along the roof slope in meters (0.5 to 3.0 m).
   - `inclination`: Roof slope in degrees from horizontal (0° to 45°). Default is 0°.
   - `sag_rods`: Number of sag rod rows along span (0 for unbraced, 1 for mid-span sag rod, 2 for third-point sag rods). Default is 1.
     * **Sag Rods & Wind Uplift Physics**: Under gravity loads ($DL + LL$), the top flange is restrained by roof sheeting. Under wind uplift ($DL + WL < 0$), the moment reverses and the **bottom flange is in compression**.
     * **Actual Calculator Assumption**: The remote calculator checks uplift bending by assuming the bottom-flange unbraced buckling length is $L_y = \text{span} / (\text{sag\_rods} + 1)$ (using sag rod spacing as compression flange unbraced length). The tool has no separate bottom-flange bracing input.
     * **Physical Detailing & Engineering Reality**: Standard sag rods alone threaded through the web or connected near the top flange provide minor-axis sag restraint, but do **not** physically prove bottom-flange lateral restraint against buckling under wind uplift unless detailed with effective diagonal fly-bracing or bottom-flange struts to the roof rafters.
     * **Bracing Confirmation & Conditional Results**: Always prompt the user to confirm whether effective bottom-flange bracing is detailed in the actual structure, and explicitly label wind uplift bending results as **conditional** upon this physical restraint. Do not promise or state that providing bracing guarantees the section will pass.
4. **Support & Restraint Assumptions (Request & Disclose)**:
   - `bearing_length`: Bearing length at support in mm (10 to 500 mm, default 100 mm; typical 75 to 150 mm on PEB rafters). Disclose this assumption to the user.
   - `top_flange_restrained`: Whether the top flange is continuously restrained against lateral buckling by roof sheeting/decking (default True). If unrestrained, unbraced lateral buckling governs. Disclose this assumption.
   - `web_reinforced_at_supports`: Whether transverse web stiffeners or reinforcement are provided at support locations (default False). Disclose this assumption.
   - `cladding_type`: Cladding type determining deflection limits: `elastic` (span/150, default) or `brittle` (span/180).
5. **Loads & Material**:
   - `dead_load_roof`: Roof sheeting dead load in kN/m² (default 0.15 kN/m²).
   - `dead_load_purlin`: Self-weight in kN/m (default 0.06 kN/m).
   - `live_load`: Imposed roof live load in kN/m² per IS 875 Part 2 (default 0.75 kN/m²).
   - `wind_load`: Design wind pressure in kN/m² (negative values indicate uplift/suction, e.g. -1.2 kN/m²; positive values indicate downward pressure). Default is -1.2 kN/m².
   - `Fy`: Steel yield strength in MPa (default 350 MPa).
6. **No Hallucinated Calculations**:
   - Do not attempt to compute effective section modulus, lateral buckling allowable stresses, web shear, or web crippling capacity manually. Always use the deterministic values returned by `design_purlin`.

## Presentation Guidelines

1. **Overall Status**: Clearly display whether the design is **SAFE** or **UNSAFE**, along with the profile used, governing check, and maximum utilization ratio. Ensure overall status agrees with detailed check outcomes.
2. **Verification Table**: Present a markdown table covering all governing IS 801 checks:
   - Combined Biaxial Bending (Major & Minor bending with lateral buckling per Cl. 6.1 / 6.3)
   - Web Shear Stress (per Cl. 6.4.1)
   - Combined Web Bending & Shear Interaction (per Cl. 6.4.3)
   - Web Crippling at support / end reaction (per Cl. 6.5)
   - Major Axis Deflection (Total load)
   - Minor Axis Deflection (Total load)
   - Live Load Deflection (Major axis)
   - Stiffener & Lip Adequacy (per Cl. 5.2.2)
3. **Engineering Assumptions Disclosure**: Always state the support bearing length, top flange restraint condition, and web reinforcement assumption alongside the results.
4. **Wind Uplift & Restraint Interpretation**:
   - Explain uplift bending using the returned checks and the calculator's assumed unbraced length: full span with zero sag rods, otherwise sag-rod spacing. Do not claim it automatically uses full span whenever fly bracing is unspecified.
   - Confirm effective bottom-flange restraint before relying on the reduced length. If unconfirmed, label uplift results conditional and request engineering review; the tool cannot independently model bottom-flange bracing.
   - Distinguish `bearing_reaction_kn` (compressive support demand) from `uplift_reaction_kn` (tension demand on connections). Report available values; null means unavailable, not zero. Web crippling does not verify uplift connection capacity.
5. **Recommendations**: Highlight any failure modes and practical engineering guidance (e.g., adding sag rods, adding fly braces to the bottom flange under uplift, increasing section depth or thickness, providing support stiffeners, or verifying connection cleats).
6. **No Standards Compliance Proof**: State explicitly that calculation results are deterministic engineering checks from the remote tool and do not constitute formal standards certification, structural sign-off, or compliance proof. Connection detailing, fastener pull-out, and site erection tolerances require independent professional engineering verification.
