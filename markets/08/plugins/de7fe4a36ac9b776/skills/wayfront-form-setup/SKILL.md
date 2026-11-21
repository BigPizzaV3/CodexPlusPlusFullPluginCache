---
name: wayfront-form-setup
description: Choose, design, create, or improve Wayfront order, contact, intake, and onboarding forms and connect them to the right services. Use when deciding which form type to use, planning fields, reducing checkout friction, or configuring a customer information flow.
---

# Wayfront Form Setup

Design forms around when the information is needed. Do not put every question into one form.

## Choose the form type

- **Order form:** self-service signup or checkout. It lets clients choose services and can collect payment. Keep it short. It must contain an email field and at least one service-bearing field.
- **Contact form:** a general inquiry, quote, or support request that is not attached to an existing project. A submission creates a ticket. It must contain an email field and may redirect after submission.
- **Intake form:** information needed for one purchased service or project. Attach one intake form to the relevant service so checkout stays focused on conversion.
- **Onboarding form:** information that is reusable across the client relationship, such as brand details or account access. Attach it to the services that require it instead of asking for the same information on every project.

Use more than one form when information belongs at different moments. If the user's process is unclear, ask what starts the relationship, when payment happens, what changes per project, and what should be collected only once.

## Inspect before designing

Use `workspace-info` if form access is unavailable or the user is unsure which workspace is connected. Use `search-wayfront-docs` when the choice depends on current Wayfront behavior that is not present in the live form schema or records.

List existing services and forms first. Show an existing form before editing it, and inspect its attached services. Reuse or refine a suitable form instead of creating a duplicate. Use folders only when they make a larger form library easier to navigate; folders can contain only forms of their own type.

Use `form-read`, `service-read`, and `form-folder-read` for inspection. Changes use `form-write`, `service-write`, and `form-folder-write` respectively. A read tool cannot accept a write action.

Before writing, present the proposed form as an ordered field plan with each field's label, type, required state, purpose, and relevant services. Make fields required only when the workflow genuinely cannot continue without them. Use help text where the requested answer or acceptable format would otherwise be ambiguous.

For order-form service selection, use one of the service-bearing field types supported by the tool: `dropdown` or `optgroup` for a single choice, and `multiselect` or `checkgroup` for multiple choices. Reference verified service IDs. Payment processors must already be connected manually before their payment options can work.

## Create or update safely

Fields can be added, edited, reordered, and removed later through MCP. The important constraint is how updates work: form creation requires the complete initial field list, and an update that includes `fields` performs full field synchronization.

Immediately before a field update, show the form and construct the complete desired list. Include every retained field with its existing `id` and intended `sort_order`; omit `id` only for a new field. Translate the read response into the write schema rather than sending it back verbatim: map `services[].id` to `service_ids`, and map services whose `pivot.default` is true to `default_service_ids`. Include only fields accepted by the update schema.

Every existing field omitted from the list is deleted, and rules involving deleted fields are cleaned up. There is no MCP dry run or version restore. Present a concise before/after field diff and obtain confirmation before invoking the update.

Omit `fields` entirely when changing only form-level settings. Preserve service attachments, option values, default services, help text, required state, and rules unless the user asked to change them. If the form has any white-labeled service, all field updates are blocked.

Prefer separate calls for form-level changes and field synchronization so each result is easy to verify. Re-read the form after any update error before deciding whether to retry.

After creating an intake form, attach it with the service's `intake_form_id`. After creating an onboarding form, update each service's complete `onboarding_form_ids` list while preserving existing associations. Order forms connect services through the form's service-bearing fields. Contact forms do not attach to an order.

After a write, inspect the returned form and summarize its type, fields, service connections, and edit URL. If sharing, embedding, payment connection, or visual preview still requires the Wayfront interface, identify that as a separate manual step rather than claiming the form is fully launched.

When the user wants examples or an interface walkthrough, search the current Wayfront documentation, retrieve the relevant result with `get-wayfront-doc`, and share its canonical source URL.
