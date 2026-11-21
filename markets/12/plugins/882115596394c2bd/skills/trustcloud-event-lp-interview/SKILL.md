---
name: trustcloud-event-lp-interview
description: "Use when an external MCP client helps a Homin Cloud user create or update an event and its LP from supplied facts, files, or focused questions."
---

# External event and LP interview

Shared references provide business knowledge. Runtime, UI, tool, or save examples
inside them describe the internal surface and must not be executed as written.
Follow this external workflow, the current live contract, and its confirmation
requirements.

Collect only the facts needed for the requested outcome: organization and branch,
event name, dates and times, location, reservation calendar and rules, intended
visitors, source-backed highlights, and any explicit image or publication choices.
Use supplied materials and current Homin Cloud records first. Ask one focused
question when a required fact is missing or ambiguous. Do not invent offers,
prices, testimonials, performance claims, access facts, or booking availability.

The MCP client must author the event copy and LP JSON from the user's facts and the
loaded Homin Cloud guidance. Do not delegate copywriting to an internal Homin Cloud
text-generation operation.

For native MCP, discover and inspect the current `events.*` contracts. Obtain the
canonical LP schema with `events.lp.schema.get` and current editable facts with
`events.lp.context.get`. Preview and apply the event or draft operation separately,
retain one idempotency key for the same retry, then read back the event/LP context
and run `events.lp.draft.review`. Use returned block IDs and `expected_updated_at`
for partial patches. Publication is a separate requested operation.

For ChatGPT Apps, use the individually exposed organization, branch, location,
calendar and event read tools for setup. Use `homin.get_event_lp_update_context`
for an update, author the
workflow payload, call `homin.prepare_event_lp_proposal`, render
`homin.show_event_lp_review`, and wait for the user's review action before
the widget saves the reviewed changes. The widget owns
`homin.apply_event_lp_proposal` and `homin.get_event_lp_proposal_status`; these
app-only callbacks must not be called by the model. For an uncertain result,
keep the original confirmation reference and use the widget's recovery action;
do not prepare a second proposal merely because a response timed out. Preview
the saved LP through the dedicated preview tools. A proposal or saved draft does
not publish the event.

For a host attachment, use the surface's Homin image-import tool and only the file
handle supplied by the host. For a native HTTPS source, use the registered media
import operation with a stable idempotency key. Never expose temporary URLs,
authorization headers, or file bytes in the conversation.

For a fictional or materially altered scene that could be mistaken for a real
venue, building, product, or event, add a short visible `イメージ` label near the
image. Do not add generic AI-production disclosures the user did not request.

## Selective references

Open only the references needed for the current task. In an installed package, use the relative links below. With an MCP-only client, fetch the exact document ID shown for the reference.

- [references/event-creation-playbook.md](references/event-creation-playbook.md) — MCP doc ID: `skill/trustcloud-event-lp-interview/v1/references/event-creation-playbook.md`
- [references/interview-flow.json](references/interview-flow.json) — MCP doc ID: `skill/trustcloud-event-lp-interview/v1/references/interview-flow.json`
- [references/interview-flow.md](references/interview-flow.md) — MCP doc ID: `skill/trustcloud-event-lp-interview/v1/references/interview-flow.md`
