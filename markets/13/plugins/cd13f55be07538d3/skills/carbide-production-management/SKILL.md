---
name: carbide-production-management
description: Manage Carbide production jobs, scope, teams, blocks, crews, constraints, colors, checklists, and project check-ins. Use for job planning and execution after a request reaches production.
---

# Carbide production management

1. Resolve the job, blocks, crews, crew members, constraints, equipment, and coordination items with `search_operational_records` and the production list tools.
   When promoting a request, omit `blocks` to create one default block containing every active trade, or supply `blocks` to create exactly that initial plan instead. Every job plans with its blocks: the job's scope hours and value are its estimate and never change a block, so set hours, crew size and duration on the blocks themselves.
2. For schedule changes, call `simulate_production_plan` with the proposed changes and locks. Explain conflicts, shortages, and non-applicable scenarios.
3. Call `apply_plan_scenario` only for a valid scenario that matches the user's requested change. Never use it to acknowledge unresolved conflicts.
4. Use the typed job, block, team, color, constraint, checklist, and check-in tools for the smallest change. Re-read the affected records afterward.
   A block's `days` list each productive day (numbered from 0) with its effective crew size, trades, named people and notes. To change a single day, use `update_block_day`, `assign_block_day_members` or `reset_block_day` instead of editing the whole block; a day with more or fewer people changes how many days the block takes.
5. Treat job archival, completion, final check-in submission, and removals as consequential; identify the exact record and effect before acting.
6. To place an unscheduled job automatically, call `auto_schedule_job` with the job id. Any member with `mcp.operate` may; the job needs a work block with labor hours, a production value or a duration. The job is `analyzing` for a few seconds, then `get_job` shows it `tentatively_scheduled` on the crew the crew routing rules ranked first with room, or back to `unscheduled` with the reason in its activity. Offer the job start email after a placement.

These tools appear only for organizations with production scheduling enabled. Job execution mutations require `mcp.operate`; archiving a job, changing its team, extending an appointment, and requesting a project check-in are shown only to owners and administrators. Production catalogue and crew roster or capability setup requires `mcp.write` and an administrator role. The user's ordinary Carbide authorization remains authoritative.

Equipment is selected by quantity per work block with `set_job_block_equipment`; zero removes an assignment. `get_equipment_availability` reports owned and reserved units on a date. Reservations cover full block spans, including weekends and pauses, for Scheduled, In progress, and Paused jobs. `extra_quantity` adds stock shared across all jobs (default 0). Availability uses owned plus extra stock. `set_job_equipment_acquisition` can only reduce or remove previously saved job-only supply; new stock belongs in the shared equipment catalog.

Use `list_coordination_items` for job Coordination selections. The former project-requirement tools and job field are retired. Every selected Coordination item appears in the job’s checklist at every status. There are no separate checklist, required-notes, or required-date catalog options; completion needs no notes or date. Removing a selection archives its checklist item and preserves history.
