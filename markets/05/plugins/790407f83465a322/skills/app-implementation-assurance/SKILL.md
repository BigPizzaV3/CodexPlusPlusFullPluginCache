---
name: app-implementation-assurance
description: Ensures an implemented Dataverse app matches its approved blueprint by running export-based verification, producing repair actions, generating role/UAT/ALM evidence, and keeping test-data cleanup explicitly approved.
---

## Architect edition scope

This edition produces local plans, checks and review artifacts only. Instructions below describing provisioning, deployment, API calls, runtime tests or publishing are plans for an authorized operator, not actions to execute. Never connect to or modify an environment through this edition. No runtime test or deployment may be claimed from generated checklists.


# App Implementation Assurance

Use after any real Dataverse app build or change, especially when Copilot, a maker portal wizard, or an automation tool created components.

## Mandatory closed loop

1. Run the blueprint linter before change:
   `python scripts/validate_app_blueprint.py <blueprint>`
2. Build only in the confirmed unmanaged Dev solution.
3. Export and unpack with PAC. Never hand-write solution XML to manufacture components.
4. Compare the export to the approved blueprint:
   `python scripts/validate_solution_against_blueprint.py <blueprint> <unpacked-solution> --json`
5. If the report has `repairRequired: true`, do **not** call the build complete. Create only the missing components in Dataverse, then export and compare again.
6. Generate a reviewable delivery pack:
   `python scripts/generate_delivery_pack.py <blueprint> --output delivery-pack.md`

## Copilot and portal generator guard

Treat generated content as a draft. Check specifically for:

- all requested columns, their actual logical names and types;
- all Choice values, relationships, form placement, views and sitemap entries;
- technical/auto-generated labels such as `New Group` or schema names in user navigation;
- unrequested sample data. Keep it only in an explicit test-data scope.

Do not claim a generated response is correct merely because the portal reports success. The exported solution is the evidence.

## Order-entry accelerator

Start from `assets/order-entry.blueprint.json` for a test implementation. It requires:

- `gbl2026_auftrag` and `gbl2026_auftragsposition`;
- all listed columns and the position-to-order relationship;
- an app group named **Auftragserfassung**, not an auto-generated group;
- role/UAT checklist and explicit test-data cleanup confirmation.

## Direct implementation boundary

Where the current session has Dataverse SDK/MCP capability, use supported metadata operations for tables, columns and relationships. Use maker-portal UI for modern app composition or business rules when no supported API surface exists. Always pass the confirmed solution name, publish after validation, and export/unpack the result.

## Completion standard

Report: environment, solution version, actual logical names, verified components, validation result, role smoke tests, accessibility status, remaining known gaps, source-folder path and rollback path.
