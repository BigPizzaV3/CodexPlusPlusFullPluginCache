---
name: voltformer-sld-engineering
description: Create, edit, analyze, revise, and export member-owned electrical single-line diagrams with Voltformer. Use when a user asks for SLD drafting, diagram changes, studies, revisions, catalog links, or project-equipment synchronization.
---

# Voltformer SLD engineering

Maintain editable, version-safe diagrams in the connected member's Voltformer workspace and clearly separate calculations from engineering approval.

## Workflow

1. Confirm the user is connected and identify the owned project. Use `getSldCapabilities` before drafting when symbols, templates, studies, or the editing contract are needed.
2. Create a diagram with `createSldDocument`, or list and retrieve an existing diagram with `listSldDocuments` and `getSldDocument`.
3. Before editing, read the complete current snapshot. Preserve unedited sheets, elements, terminals, busbars, connections, junctions, annotations, metadata, and study settings.
4. Apply requested editor changes to the snapshot and call `saveSldDocument` with its current storage version. If a conflict occurs, reread, reconcile, and ask the user when intent is ambiguous.
5. Use `linkSldCatalogProduct` for catalog-backed component properties and `syncSldProjectEquipment` only when the user wants diagram equipment merged into the project.
6. Use `analyzeSldDocument` or `runSldStudy` only when inputs are sufficient; otherwise report missing inputs. Use `exportSldDocument` for the requested supported formats.
7. Create an immutable revision only when requested. Treat approval-status changes, snapshot replacement, synchronization, and deletion as consequential actions.

## Invariants

- Never invent terminals, ratings, study results, catalog links, or approval status.
- Do not overwrite on stale versions or discard fields the user did not ask to change.
- Obtain explicit confirmation immediately before deletion, replacing a saved snapshot, creating an approval revision, linking properties that overwrite element data, or synchronizing project equipment.
- Describe engineering studies as preliminary and requiring qualified review.

