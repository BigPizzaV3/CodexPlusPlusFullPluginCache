---
name: bosl2-cheatsheet
description: Use the pinned BOSL2 library in Print Ready for chamfers, rounding, anchors, attachments, sweeps, screw threads, gears, hinges and snap joints. Consult its linked reference when choosing includes or debugging BOSL2 geometry.
---

# BOSL2 modeling reference

Read the [practical BOSL2 reference](references/bosl2-basics.md). It covers the library included in Print Ready, required include files, positioning, boolean tags, mechanical examples and upstream documentation links.

Call `get_capabilities` to confirm the installed version. Print Ready currently pins BOSL2 2.0.766 at commit `e173fa0ae45f9e2082e0d8c0382dae98621b7c20`. The upstream wiki changes independently, so check the pinned implementation when a newer example uses unfamiliar arguments. Prefer named arguments. Compile and inspect real geometry before claiming a mechanism works; physical fit still requires the user's printer and measurements.

MCP-only clients can call `get_bosl2_cheatsheet` for this skill and its reference. This read does not render a model or open the welcome guide.

For custom FDM mating threads, use `trapezoidal_threaded_rod(thread_angle=90)` for 45 degree flanks and the identical profile with `internal=true` for the female cutter. The reference gives the 8 mm diameter, 2 mm pitch, 0.60 mm radial depth starting profile, 0.40 mm flat lands and one-time female `$slop=0.15` clearance. Use chamfered entries, blunt lead-ins and vertical print axes. Physical testing determines the final clearance.
