---
name: display-editing
description: Use when someone wants to find, change, rebuild, export or delete a saved WallKiwi display.
---

Privacy boundary: this public plugin is for adult educators and creators. Never
transmit personal information about children under 13 to OpenAI. Use anonymous
or synthetic inputs only; do not request, send or retrieve pupil names, pupil
ids, rosters, photographs, scripts, individual answers or individual results.
Apply this boundary whenever ages or identifiability are uncertain. Do not
open, screenshot, upload or read back private pupil records through a browser
or another connector. Give the exact native link and hand the sensitive step
to the adult user to complete independently. Do not read a record first merely
to decide whether it contains personal information.
Use only existing records confirmed to contain anonymous or synthetic teaching
content. If privacy is uncertain, return the exact native link without reading
the record, opening its private screen or obtaining its contents through an
export or another connector. Do not ask the adult to paste pupil records.


# Display editing

Call list_my_displays and get_display to identify the exact owned pack; never guess ids. Read its current manifest and updatedAt before an edit. Send only requested native fields in edit_display_manifest.changes and use expectedUpdatedAt. Preserve unrelated text and options verbatim. A stale-version refusal requires rereading, not overwriting another edit.

The manifest edit itself makes no AI call but invalidates printed files. Rebuilding can generate changed pieces and spends existing credits at the native changed-piece price; read get_display_access and obtain agreement before build_display. Stop on INSUFFICIENT_CREDITS and report the restriction neutrally without purchases or unrequested retries. Poll until confirmed ready. Use export_display with the actual preset, allowed file kind and real sheet id when needed. For a published example, pass its exact example_slug from list_display_examples; the gateway verifies that slug, pack id and preset agree. Return its real embedded PDF/ZIP; if the host cannot attach it or the file exceeds 10 MiB, return that result’s exact native editor or published example page and explain the native download control. Never invent a download URL or bypass account policy.

Delete only after explicit confirmation for the exact named pack, then pass confirmed:true to delete_display. Do not retry deletion or spending calls after an ambiguous result; reread the pack/status first. No subscriptions, token sales or checkout flows.
