---
name: crisphive-roster-sync
description: Manage a field-operations team in Crisphive — create, update, and remove technicians and keep their skills, service areas, crew relations (leads/buddies), and vehicles in sync, e.g. when onboarding staff or syncing from an HR system. Use when the user wants to add or remove a technician, change someone's skills or coverage area, or set up who works with whom.
---

# Manage the technician roster with Crisphive

The technician roster feeds the scheduling engine directly: skills, service
areas, start locations and crew relations all change who gets matched to
which job. Keep them accurate.

## Environments: sandbox vs production

This skill works identically in BOTH environments — same tools, same fields,
same responses. The credential decides which one you are in:

- **Sandbox** — API key `chsk_test_…`, or an OAuth connection authorized from
  a sandbox dashboard session. The sandbox has its OWN isolated roster: test
  technicians here never appear in the live team and receive no
  notifications. One extra rule applies: Owner/Administrator role groups
  cannot be created in sandbox (operational roles like Technician work
  everywhere).
- **Production** — API key `chsk_live_…`, or an OAuth connection authorized
  from a live session. Creating a member with an email/phone sends them a
  real "you've been added" notification, and roster changes immediately
  affect real job matching. Create real people only, and confirm removals
  with the user before calling `deleteTechnician`.

You cannot switch environments with a parameter; reconnect with the other
credential.

## Creating a technician

`createTechnician` — required fields:

- `business_group_id` — the role group (Technician, Supervisor, …).
  **Group IDs are not discoverable through this API**; the business copies
  them from the Crisphive dashboard (Settings → Permissions). Ask the user
  for it if you don't have one from an earlier call in this conversation.
- `full_name`.
- At least one of `email` / `phone`. Phone numbers are validated as REAL
  E.164 numbers (libphonenumber: real dial code + per-country pattern) —
  placeholder numbers are rejected with `PHONE_INVALID`. If neither contact
  is valid you get `TECHNICIAN_CONTACT_REQUIRED`.

Strongly recommended at create time:

- `assignment_tier` — how the crew matcher treats them: `lead` (can head a
  job), `buddy` (crew helper), `float` (excluded from auto crew-assign).
- `start_location_type` (`home` | `office`) **plus explicit
  `start_location_lat` / `start_location_long`** — the engine computes travel
  times from this point. Note: choosing `office` snapshots the business
  location at creation time; set the coordinates explicitly to be safe.
- `service_area_ids` — which geographic areas they cover (discover via
  `listServiceAreas`). A technician with no service area is never matched.
- `buddy_ids` (when creating a lead) or `lead_ids` (when creating a buddy) —
  see crew relations below.

No invite email is sent; sign-in is passwordless and handled by the platform
later.

## Keeping attributes in sync

- Skills: `replaceTechnicianSkills` (PATCH, replace-semantics — send the FULL
  list; `[]` clears). Discover skill IDs via `listSkills` /
  `listSkillCategories`. Skills matter twice: as a hard filter when a job
  demands them and as a soft ranking signal.
- Service areas: `replaceTechnicianServiceAreas` (replace-semantics).
- Vehicles: `replaceTechnicianVehicles` — the vehicles this technician can
  use (discover via `listVehicles`). Vehicle-to-tech links are edited only
  from the technician side.
- Profile fields: `updateTechnician` is a FULL replace — read the current
  record with `getTechnician` first and send every field back, changing only
  what the user asked for.

## Crew relations (leads & buddies)

- The relation is DIRECTIONAL and owned by the lead: a lead's `buddy_ids`
  lists who can crew under them. `replaceTechnicianBuddies` edits a lead's
  list (replace-semantics; self-buddy is rejected).
- `replaceTechnicianLeads` is the buddy-side write of the SAME relation — it
  adds/removes this technician in the named leads' buddy lists.
- Buddies matter for multi-person jobs: the matcher prefers a lead's own
  buddies when building a crew.

## Removing a technician

- `deleteTechnician` removes them from the active roster and automatically
  scrubs references (buddy lists, vehicle ownership). It is a soft delete
  server-side, but treat it as destructive: confirm with the user first.
- Suspending rather than removing (status changes) is a dashboard operation,
  not available through this API.

## Verifying

`listTechnicians` / `getTechnician` embed the synced state: skills, service
areas, buddies/leads, vehicles, tier, start location. After a batch of
changes, read back and summarize what changed.

