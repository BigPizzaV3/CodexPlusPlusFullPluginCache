---
name: design-pcb
description: Design a circuit and a placed, routed PCB from a specification using Embedr tools.
---
1. Create or read the real project. Save the original requirements and material assumptions. Keep its canonical Open in Embedr link visible.
2. Load get_design_guidance for zener-language and the relevant PCB workflow. Read exact referenced resources through read_design_guidance_resource. Learn the deployed syntax; do not invent source language features or assume a local shell.
3. Search components and inspect grounded records and raw component evidence. Install suitable dependencies, or author project-local source/dependencies when catalog coverage is incomplete. Missing catalog coverage does not forbid a circuit.
4. Write source with apply_project_patch, using the latest baseRevisionId and a fresh idempotencyKey. Every engineering mutation also requires those guards. A retry of the same request uses the same key; changed inputs use a new key.
5. Poll every accepted operation with get_operation until terminal. Each call waits up to 20 seconds for the job, so call it again straight away while it is still running; do not narrate each poll. queued/running means work is accepted, not that the PCB is ready. Interpret the actual result, preserve useful partial files, repair diagnostics and retry through explicit tools.
6. Build, inspect the netlist and synchronize the layout. Define a real outline and board rules. For a first pass on a supported rectangular, unconstrained board, use auto_place_pcb. It reads native locks and fingerprint, rejects unsupported geometry/copper/keepouts and incomplete placements before writing, and preserves fixed refs. Use preview when hand placement is worth keeping; preview does not save. Keep manual place_pcb available for exact x/y/rotation/locked changes and unsupported or constrained boards.
   - Await placement terminal success. Then call render_pcb with projectId, layoutPath and width:1600; poll get_operation until its image is returned. Inspect the actual MCP image content and result.revisionId, not only a widget or text report.
   - Inspect current placement with inspect_pcb_placement and await its result. Check the project, layout, revision and fingerprint. If a newer edit intervened, re-inspect and re-render. An older image is not evidence of the new revision.
   - Adjust selected refs through place_pcb with current baseRevisionId, expectedSha256 and a fresh idempotencyKey for changed inputs. Await success, render again and inspect the new image/revision. Repeat as needed. Render shows the saved board; after an unsaved preview it does not show the candidate.
   - The image is a simplified raster and placement uses rendered envelopes and estimated connectivity. Neither proves full geometry, routability or manufacturing readiness. Keep actual validation authoritative, preserve locks and critical geometry, and report unsupported constraints honestly.
   - Run the selected self-hosted router for the accepted placement. Report actual routing coverage and unconnected nets.
7. Run revision-specific checks, inspect findings and make repairs. Compiled, copper present, routed and manufacturing ready are different states. Never infer readiness from a preview alone.
8. Show the real project using show_project. Export the requested native/fabrication/BOM outputs for the accepted revision, then follow review-manufacturing to verify the final saved revision and automatically output its Order PCB link when DRC and DFM are clean. Do not wait for a separate order request or direct the user to a viewer Order button.

If a browser edit causes REVISION_CONFLICT, read the latest project, compare snapshots where needed and rebase the requested change. Do not blindly restore or overwrite newer web work. A preserved candidate can be downloaded for recovery.

Do not use a hidden Embedr generative loop. Further design decisions belong to this conversation. Accepted deterministic jobs can finish after disconnect; use get_operation to resume.
