# Conversation voice controls

Maintain the selected kit's original contents separately from the current conversation's adjustments. These are conversational instructions, not hidden account settings or a durable storage service. Use available context; if the selection or adjustments are no longer available, say so and request the kit or missing preference instead of inventing a status.

## Tune and inspect

- **“Less humor,” “warmer,” “more concise”:** adjust the selected voice for this conversation by default. Interpret the requested change relative to its existing character. Briefly acknowledge the change and continue the task. Do not invent numeric slider settings or change the kit file/version.
- **“For this answer”:** apply the change only to the requested answer, then return to the previous conversation settings. A task's audience or format is an answer-specific requirement, not a lasting voice change.
- **“Only for writing/conversation” or “use it for both”:** set the effective conversation scope as explicitly requested. Leave the original kit's scope unchanged. Writing means generated prose artifacts; conversation means surrounding replies and progress updates.
- **“Which voice is active?” or “Soulware status”:** report selected name and kit version, active/paused state, effective scope, and any lasting conversation adjustments. Say “no adjustments” when appropriate. State “this conversation” without claiming host settings changed. Do not run local installation status unless the user asks about installed files or defaults.
- **No selected kit:** say that no Soulware voice is selected here. Offer selection or comparison; do not choose a default or change the user's ordinary assistant preferences.

If the user says “no humor,” that replaces conflicting playful guidance. Rewrite the response accordingly instead of appending a disclaimer. Specific later requests take priority over conflicting earlier adjustments; preserve unrelated preferences. Use the selected kit's `voice.avoid` and `checks` silently before replying, with factual accuracy and the current task taking precedence.

## Pause, resume, reset, switch, stop

- **Pause:** suspend the selected voice while retaining the kit and its conversation adjustments for a possible resume. Answer in the user's ordinary preferred style.
- **Resume:** reactivate that selection and its adjustments when still available in context. If nothing is paused, explain the actual state; do not resurrect a stopped voice.
- **Reset my adjustments / original kit:** remove conversation adjustments, including a scope override, and restore the selected kit's original guidance and scope. Keep a paused voice paused; resetting does not resume it.
- **Switch to another kit:** replace the selection, clear old voice-specific adjustments and pause state, and use the new kit's declared scope. Independent task requirements still apply.
- **Stop / turn off Soulware:** clear the selection, pause state, and voice-specific adjustments. This does not uninstall files or remove a saved local default.

Do not repeat state summaries on ordinary replies. A short acknowledgment suffices when changing a setting.

## Save a revised portable kit

Save only when the user asks to download, export, or save their adjusted Soul Kit. A bare “save it” with an unclear referent needs clarification. Use the original selected kit plus lasting conversation adjustments; exclude one-answer overrides and pause/off state. If there are no lasting changes, provide the original file without changing its version.

Translate requested lasting changes into the existing v1 fields. Preserve unrelated rules, facts, and the original ID/name. Resolve contradictory inherited guidance throughout core, traits, rules, avoid entries, adaptations, examples, and checks where relevant. For a humor ban, for example, remove conflicting instructions and revise playful examples; merely adding “no humor” to the end is insufficient. Do not weaken factual or task requirements. Treat changes as communication guidance using the same review as an imported kit.

When execution and file output are available:

1. Read the complete original kit and create a small JSON changes file containing only changed fields. Allowed top-level fields are `summary`, `scope`, `voice`, `behavior`, `adaptations`, `examples`, and `checks`. Nested objects merge; a supplied list replaces that whole list, so retain its unaffected entries. Do not include ID, name, format, or version.
2. Use the bundled runtime:

   `python3 SCRIPT revise ORIGINAL --changes CHANGES --output NEW.soulkit.json`

   Resolve `SCRIPT` relative to this skill as `scripts/soulkit.py`. Quote actual paths. Use a new output filename in an existing directory. The command validates the result, preserves the source, increments its patch version (rolling over bounded components if needed), and refuses to overwrite a destination. For another save from the same original kit, pass `--after-version VERSION` using the latest saved version of that ID actually known in this conversation; this avoids assigning different content the same version. Reuse an existing saved file if neither the effective guidance nor requested scope has changed. Do not invent versions or search unrelated user files. It makes no model/network calls and does not install anything. Review semantic consistency before invoking it; structural checks cannot establish compliance with arbitrary prose preferences.
3. Deliver the resulting `.soulkit.json` file with its actual version and a brief account of what changed. Leave the current base selection and temporary adjustments as they were unless the user asks to use the saved revision. Explain that reimporting this file carries the changes to another conversation.

If execution is unavailable but file output exists, construct a complete v1 JSON file, increment beyond the latest known saved version of this ID (or the original version) with the same 0–9999 limits and rollover, and inspect it using [the format guide](format.md). If file output is also unavailable, provide complete copyable JSON and a suggested `.soulkit.json` filename. Describe this as manually inspected JSON, not an automatically validated or downloaded file. For `9999.9999.9999`, explain that a new kit identity is needed rather than emitting an invalid version.

Do not claim a successful save without an actual file or copyable complete JSON. Saving a kit never changes the original download, installs a local skill, updates an installed version, or changes account-wide preferences. Those are separate requests.
