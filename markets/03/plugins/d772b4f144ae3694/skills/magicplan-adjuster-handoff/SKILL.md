---
name: magicplan-adjuster-handoff
description: >-
  Prepare a neutral, carrier-ready adjuster handoff package from a magicplan restoration project —
  project geometry and affected areas, the documentation inventory, the estimate posture, and a clean
  list of open questions — following the built-in restoration adjuster-handoff playbook plus adjuster
  communication best practices. Use this whenever someone is getting a job in front of an insurer:
  "prepare the adjuster handoff", "put together the carrier package for this loss", "I need to hand this
  off to the adjuster", "write the adjuster narrative", "get this file ready for the insurance company",
  or "summarize this project for the carrier". Trigger it even when the person only says they're sending
  a project to an adjuster or carrier and wants it packaged properly.
compatibility: Requires the magicplan connector (MCP tools) for project and workspace data.
metadata:
  author: magicplan
  version: "1.0"
---

# magicplan Adjuster Handoff

Assemble a concise, factual package a restoration professional can hand to an insurance adjuster or
carrier representative. The tone is measured and neutral throughout — present conditions observed and
what the documentation shows, not advocacy for scope. A clean, honest handoff builds carrier trust; an
overreaching one invites pushback.

This skill reads from magicplan only and does not change workspace data. It documents the project state;
it does not decide coverage — that is the carrier's and adjuster's call.

## Step 1 — Load the built-in playbook

If restoration resources are available, read the **`restoration://playbooks/adjuster-handoff`** resource
and follow its review sequence — it is the authoritative structure for this task. The
`restoration://playbooks/fnol-to-scope` playbook is a useful companion when the handoff also needs to
frame first-scope reasoning. Combine the playbook's sequence with the template and best practices in
`references/handoff-guide.md`. If resources are not available, use the reference file alone.

## Step 2 — Ask about carrier-specific requirements

Before building, ask the user whether they have **carrier-specific requirements** for this handoff, for
example:

- The **carrier / program** and any house format or portal it must fit.
- **Required forms or attachments** the carrier expects (specific documentation, authorizations).
- **Reference numbers** — claim number, adjuster name/contact, policyholder details.
- Any **house rules** on tone, itemization, or what to include/exclude.

If they have a spec, follow it. If not, tell them you'll use standard best practices from the playbook
and reference file, and proceed. Also ask once for the **company name and contact details** for the
header — never assume branding.

## Step 3 — Gather the project documentation

Following the playbook sequence, read:

- `get_project_snapshot` — property type, floors, affected rooms, estimates, `plan_id`, `cloud_url`.
- `get_plan_statistics` — approximate square footage and per-room measurements.
- `get_project_plan` — affected-area annotations, loss type/category/class if set, equipment placed.
- `get_plan_forms` — completed workspace custom forms.
- `get_moisture_readings` — instrument drying history (empty series = a gap to name).
- `list_project_photos` — photo evidence (counts, captions, URLs); page through `page_info`.
- `list_project_files` — reports, third-party assessments, other documents.
- `list_estimates` / `get_estimate` — estimate posture and, if needed, coverage of line items.

## Step 4 — Build the package

Produce the handoff using the structure in `references/handoff-guide.md`: project & affected-area
summary, documentation inventory (forms, photos, files, readings — with gaps named), estimate posture
(what it covers, no opinion on whether it is high or low), and a clean list of open questions sorted into
field / adjuster / customer / third-party items, each phrased as a neutral question rather than a demand.

Deliver a polished file (a clean written document; HTML or Word both print well) plus a one-line summary
in chat. Keep the document neutral and free of magicplan-specific jargon the adjuster would not use.

### Report-gap recommendation

A strong handoff often needs an estimate or report that lives in magicplan and cannot be generated here.
When the package would be materially stronger with something missing — no estimate on file, no formal
report, thin photo or moisture documentation — name the gap, give the user the project `cloud_url` so
they can generate or capture it in magicplan, and offer to fold it into the package once it exists.
Handing a carrier a package with visible, acknowledged gaps beats padding it with assumptions.

## Principles

- Neutral and factual. Present conditions observed; do not argue scope or coverage.
- Separate documented facts from assumptions; label assumptions.
- Name documentation gaps as neutral open items, not failures.
- Never fabricate readings, measurements, dates, or claim details.
