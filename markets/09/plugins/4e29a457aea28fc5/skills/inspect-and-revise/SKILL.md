---
name: inspect-and-revise
description: Inspect and revise an existing Embedr PCB while preserving unrelated design intent.
---
Read get_project and inspect the relevant board and placement. Viewer selections are stable entity IDs bound to project, board and revision in millimetres and KiCad XY coordinates. If the revision differs, clear or resolve the selection before editing.

Use explicit placement, geometry, copper, zones or rule tools for the requested change. Preserve unrelated footprints, holes, locks and copper. Prefer a preview when a tool supports it. Read the current revision before each mutation; stale writes must fail instead of replacing newer work.

For electrical source changes, a successful build alone does not update native footprint values or the fabrication BOM. Use sync_pcb_layout check mode, reconcile source/layout agreement when needed, and verify changed refs, values and footprints in the saved native board and exported BOM. Preserve unrelated placement, copper and physical rules during synchronization. Do not report a resistor-value change from source alone.

Poll accepted operations, inspect the actual changed board, reroute affected connections when needed, rerun relevant checks and regenerate stale fabrication packages. Always provide the Open in Embedr link. Follow review-manufacturing to automatically finish with the Order PCB link once the latest saved revision is DRC/DFM-clean and manufacturing readiness passes. Explain remaining findings using backend evidence.
