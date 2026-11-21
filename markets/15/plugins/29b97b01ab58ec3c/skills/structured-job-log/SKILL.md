---
name: structured-job-log
description: "Use when a FlatRate Pro technician wants to find repair jobs, log explicitly described work, update job hours or vehicle details, or change a specific job's status."
---

# Structured job log

Work only with the connected technician's jobs. A request to search or estimate
is not permission to create or update records. Follow the user's explicit scope
and preserve every unspecified field.

1. For retrieval, call `listRecentJobs` with a limit of 1-20 or
   `searchJobsByVehicle` with the user's title/vehicle query and supplied
   `date`, `startDate`, or `endDate`. Summarize actual matches and returned IDs.
2. For creation, collect a job name or description and explicit relevant
   category, hours, vehicle, and date. Ask for missing or ambiguous details.
   Do not infer book time, actual time, or a category from vague repair notes.
3. If the user requests a labor estimate, call `estimateJob` for the repair.
   Present it as an estimate and ask whether to use it before creating a record.
4. Call `createJob` only for an explicitly requested structured entry. Use
   `updateJob` for requested partial edits or `updateJobStatus` for a status
   change (`pending`, `in_progress`, or `complete`). Resolve a real job ID first;
   clarify multiple matches rather than selecting one arbitrarily.
5. Respect client confirmations before writes. Locked or verified jobs cannot
   be changed. Never bypass a denial or alter a different record to work around it.
6. Report only server-confirmed changes, including the actual ID and fields.
   Surface errors and uncertain responses; check existing records before retrying
   a create. Do not claim success from a timeout.
7. Do not perform bulk fuzzy edits, organization verification, billing, or file
   uploads through this workflow. If authentication is needed, direct the user
   to the client's OAuth connection flow. Never ask for credentials in chat.

Examples: "Find my brake jobs from February 10, 2025" is read-only;
"Log the repair I finished" requires clarification; "Mark that job complete"
requires a uniquely identified editable job.
