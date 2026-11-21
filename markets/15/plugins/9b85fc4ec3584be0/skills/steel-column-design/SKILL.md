---
name: steel-column-design
description: Use for designing and structurally verifying steel columns and beam-columns according to Indian Standard IS 800:2007, including axial compressive strength, buckling classes, slenderness limits, and biaxial bending interaction.
---

# Steel Column Design (IS 800:2007)

Use the registered StructEngine MCP tool `design_steel_column` as the calculation and structural verification authority for steel columns and beam-columns.

## Downloadable report

The end product is the tool-generated **Download PDF**, alongside a brief summary. Present its actual link, filename and expiry immediately; do not ask a second export question. If the tool returns a native OAuth linking challenge, let ChatGPT connect the user's StructEngine account and retry the same arguments. Reuse valid authorization without repeated sign-in prompts; never request passwords, tokens or authorization codes in chat. Preserve failed design checks and warnings in the summary. If export fails or the deployed tool lacks PDF support, say no PDF was delivered; never invent a link or silently substitute a model-written report.

## When to Use

Use this skill whenever a user:
- Requests design, capacity checks, or sizing for structural steel columns per IS 800:2007.
- Asks whether a specific steel section (e.g. `ISMB 350`, `ISMB 400`, `UC 203x203x46`, `WPB 300x300`) can carry a given factored axial load and bending moments for a given column height/length.
- Inquires about column slenderness ratio ($\lambda = KL/r$) against IS 800:2007 Table 3 limits ($\le 180$).
- Asks for design compressive stress $f_{cd}$ or buckling class curves (curves a, b, c, d per Cl. 7.1.2).
- Needs combined axial compression plus biaxial bending interaction check per IS 800:2007 Section 9.3.

## Input & Execution Guidelines

1. **Tool Invocation**: Call `design_steel_column` with the geometry, loading, and boundary condition parameters. Always use the deterministic remote calculator; never compute buckling capacities or interaction equations manually.
   - `section_name`: Standard Indian steel section designation (e.g., `ISMB 350`, `ISMB 400`, `UC 203x203x46`). The tool automatically queries the section database.
   - `axial_load`: Factored axial compression in kN.
   - `length` (or `length_major` / `length_minor`): Unsupported column length in meters (0.5 to 20 m).
   - `moment_major` ($M_y$) and `moment_minor` ($M_z$): Factored moments in kN-m (if applicable).
   - `end_condition_major` / `end_condition_minor`: Boundary condition (`pinned_pinned` for K=1.0, `fixed_pinned` for K=0.8, `fixed_fixed` for K=0.65, `fixed_free` for K=2.0).
   - `steel_grade`: `E250` (default, $f_y=250\text{ MPa}$), `E300`, `E350`, etc.
2. **Custom Sections**:
   - If a built-up or non-catalog profile is specified, pass geometric properties (`area`, `depth`, `width`, `thickness_web`, `thickness_flange`, `radius_gyration_major`, `radius_gyration_minor`).

## Presentation Guidelines

1. **Safety Verdict**: Clearly display overall status (`SAFE` or `UNSAFE`) and governing demand-to-capacity utilization ratio.
2. **Capacities Table**: Tabulate axial compression ($P_u$ vs $P_d$), slenderness ratio ($KL/r$ vs limit), and Section 9.3 interaction ratio.
3. **Buckling & Stresses**: Show the governing buckling axis (major or minor), buckling curve classification (a, b, c, d), and design compressive stress $f_{cd}$.
4. **Engineering Notes**: Remind the engineer that effective length factors assume ideal joint restraints and base plate conditions that must be detailed accordingly.
