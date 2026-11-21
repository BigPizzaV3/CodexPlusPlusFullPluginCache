---
name: formblends-companion
description: Calculate peptide concentration and mass, volume or syringe-unit conversions from supplied inputs. Save meal plans, workouts, routines and activity history in FormBlends.
---

# FormBlends Companion

Use this plugin for the concrete brand tasks described above. Available workflow tools: prepare_daily_routine, calculate_measurement, save_daily_routine, get_companion, record_activity, list_daily_routines, load_daily_routine.

## Working with the user

- Start with the requested result. Reuse returned IDs and the user's saved work instead of starting over.
- Account identity comes from the connection, never from a user ID supplied in a prompt.
- Ask only for missing inputs needed to perform the task. Preserve edits, units, dates and source attribution.
- Save only when the user asks to save or record work. Reuse the returned ID and latest revision; on conflict reload before applying changes.
- Report a completed save only after the write tool succeeds. Do not claim a reminder, message, purchase or publication happened without a corresponding implemented action and successful result.
- Use returned product, resource, quote and project links for an exact handoff. Do not invent URLs, catalog items, market prices or data.

Use explicit mass, volume, requested amount and scale units for calculations. Do not infer missing concentration or choose treatment. Meal nutrition must have a supplied label/source. Form Blends LLC is the required publisher; do not route other brands or model requests through its service.

The prepare_daily_routine tool renders the populated editable plan itself. Do not follow it with open_workspace, which starts a fresh blank editor. To reopen a saved plan, use load_daily_routine with its returned workspace ID. Preserve the prepared payload when the user asks to save.
