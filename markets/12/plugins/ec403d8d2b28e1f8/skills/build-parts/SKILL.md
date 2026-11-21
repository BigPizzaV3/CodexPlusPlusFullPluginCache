---
name: build-parts
description: Design mechanical parts and simple mechanisms in WebCAD and deliver STEP files. Use when the user asks to design, model or change a part, bracket, plate, enclosure, gear, hinge, arm or linkage, wants pictures of a design, a first stress check, or a STEP file for CAD, machining or 3D printing.
---

# Build parts with WebCAD

WebCAD builds models written in ArchScript, its text modelling language, and reports the result. Work in this loop:

1. **Look up.** Read `get_archscript_reference` once. For a feature you have not used, call `lookup_archscript_capabilities` with the topic. Start from the closest example (`list_archscript_examples`, then `get_archscript_example`).
2. **Write the whole script** and call `validate_archscript`. Fix every error and validate again. Validation is free and builds nothing.
3. **Build** with `execute_archscript`. It returns PASS, or FAIL with each problem to fix, such as a missing part, parts that collide, or a joint that cannot move through its range. Fix the script and build again. Never call a design done before a PASS.
4. **Show it** when the user wants to see it: `viewport_capture` with one to three named views.
5. **Deliver** with `export_step`, only after a PASS. Give the user the download link and say that it works for 24 hours.

Good practice:

- Ask for the dimensions that matter (overall size, hole sizes, material) when the user has not given them; otherwise choose sensible values and say which ones you chose.
- Build an assembly one moving group at a time, and build again after each step.
- Give every part a colour, keep at least 0.25 mm between parts that should not touch, and make each moving part a single body.
- Every tool is free (no WebCAD credits); builds are limited to one at a time and 100 a day. Validate before every build so that builds do not fail on syntax.
- A PASS means the model builds in WebCAD. Fit, strength, safety and manufacturability still need a person's review; say so with stress results.
- Thermal and CFD studies do not always run here. When a build result says it left a study out, tell the user in its words.
- If WebCAD turns a request down, for example a script over its size limit, tell the user and offer a simpler version. Do not present code in another CAD language as ArchScript.
