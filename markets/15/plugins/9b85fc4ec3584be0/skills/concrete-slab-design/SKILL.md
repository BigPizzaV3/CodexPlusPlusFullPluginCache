---
name: concrete-slab-design
description: Use for designing and detailing reinforced concrete one-way and two-way slabs according to Indian Standard IS 456:2000, including moment coefficients, reinforcement schedule, one-way shear, and deflection control.
---

# Concrete Slab Design (IS 456:2000)

Use the registered StructEngine MCP tool `design_concrete_slab` as the calculation and structural verification authority for reinforced concrete slabs.

## Downloadable report

The end product is the tool-generated **Download PDF**, alongside a brief summary. Present its actual link, filename and expiry immediately; do not ask a second export question. If the tool returns a native OAuth linking challenge, let ChatGPT connect the user's StructEngine account and retry the same arguments. Reuse valid authorization without repeated sign-in prompts; never request passwords, tokens or authorization codes in chat. Preserve failed design checks and warnings in the summary. If export fails or the deployed tool lacks PDF support, say no PDF was delivered; never invent a link or silently substitute a model-written report.

## When to Use

Use this skill whenever a user:
- Requests limit state design for one-way or two-way reinforced concrete floor or roof slabs to IS 456:2000.
- Asks to determine bending moments, required reinforcement area ($A_{st}$), bar diameter, and c/c spacing for a slab panel.
- Needs to check slabs with various boundary/support conditions (e.g. simply supported, interior panel, one edge discontinuous, cantilever).
- Inquires about slab shear capacity ($\tau_v$ vs $\tau_c$) or span-to-effective-depth ratio for deflection control per IS 456 Cl. 23.2.1.
- Inquires about distribution steel requirements per IS 456 Cl. 26.5.2.1.

## Input & Execution Guidelines

1. **Tool Invocation**: Call `design_concrete_slab` with geometric, material, and loading parameters:
   - `clear_shorter_span` ($L_x$): Clear short span in meters (1.0 to 10.0 m).
   - `clear_longer_span` ($L_y$): Clear long span in meters (1.0 to 12.0 m).
   - `slab_depth` ($D$): Overall slab thickness in mm (typically 125 to 200 mm).
   - `support_condition`: Standard boundary condition (`"Simply Supported"`, `"Interior Panel"`, `"One short edge discontinuous"`, `"One long edge discontinuous"`, `"Two adjacent edges discontinuous"`, `"Two short edges discontinuous"`, `"Two long edges discontinuous"`, `"One long edge continuous"`, `"One short edge continuous"`, or `"Four edges discontinuous"`).
   - `fck`: Concrete grade in MPa (20, 25, 30, 35, 40, etc.).
   - `fy`: Steel grade in MPa (415, 500, or 550).
   - `dead_load`: Superimposed dead load in kN/m² (finishes, partitions; self-weight is computed automatically).
   - `live_load`: Imposed live load in kN/m² per IS 875 Part 2.
   - `db_short` & `db_long`: Main and transverse bar diameters in mm (default 10 mm and 8 mm).
   - `clear_cover`: Clear cover in mm (default 20 mm).

## Presentation Guidelines

1. **Classification & Verdict**: Clearly state whether the slab acts as a One-way or Two-way slab ($L_y/L_x$ ratio) and whether the overall design is `SAFE`.
2. **Reinforcement Schedule Table**:
   - Short span midspan bottom steel (bar diameter, c/c spacing, provided $A_{st}$ vs required).
   - Short-span support top steel, if returned. Label `minimum_detailing` as minimum detailing steel and `support_moment` as reinforcement for a calculated support moment.
   - Long span / distribution transverse steel.
3. **Safety Checks**: Tabulate one-way shear stress ($\tau_v$ vs $\tau_c$) and span-to-depth deflection control (actual $L/d$ vs allowable $L/d$).
4. **Detailing Requirements**: Advise on corner torsional reinforcement for restrained slabs per IS 456 Annex D and curtailment rules.
