# Soul Kit generator contract

Version 1, September 22, 2026.

The website creates original personalities from a short questionnaire. The plugin imports the finished result. Customer writing samples are not required.

## Boundary

Return one JSON object matching `schemas/soul-kit.schema.json`. The same approved object supplies the final preview and the customer download, named `<id>.soulkit.json` with media type `application/json`. Keep previews, inputs, and drafts in browser memory; the download is an explicit user action. The plugin does not require a saved account, database, or retrieval API.

Use `examples/moss.soulkit.json` as a valid example of the format, not a template for every voice's personality.

## Generation

Capture scope, collaborator relationship, directness/detail, warmth/humor, and disagreement preferences. Generate the core character, concrete speaking habits, interaction behaviors, adaptations, original demonstrations, and a short quality check. Resolve conflicting preferences rather than copying all answers into a list of rules.

Offer two candidate demonstrations using the same situation. They can come from two complete candidate kits; each kit must contain at least three examples. Include disagreement or uncertainty. The selected kit is the final artifact; do not display one voice and download a separately regenerated one.

The generator may refine content but may not invent permissions, tool availability, source evidence, personal history, or accounts. User instructions and task requirements remain authoritative over voice preferences.

## Validation and revisions

Validate server responses before preview or export. In addition to JSON Schema validation, reject duplicate JSON keys, invalid UTF-8 or unpaired Unicode surrogates, payloads above 262144 bytes, whitespace-only strings, and case-insensitive `SOULWARE:DEFAULT` or `soulware-kit:` marker strings. These extra rules are required by the importer. Decoded field strings may contain tab and newline, but no other ASCII control characters. JSON formatting whitespace may use either LF or CRLF line endings.

`id` is a stable lowercase slug with at most 48 characters. `version` is numeric `X.Y.Z`, with 1–4 digits per component. Keep the ID stable across refinements. When content changes after export, increment the patch version. The importer refuses a different payload with the same version or a numeric downgrade. Whitespace and JSON property order do not change kit identity.

The plugin does not accept arbitrary executable files, URLs to instructions, raw skill folders, or generated shell scripts. The deterministic compiler creates native skill files from the JSON. This keeps the website independent from client-specific installation layouts.

## Local integration check

Run:

```text
python3 skills/soulware/scripts/soulkit.py validate examples/moss.soulkit.json
python3 skills/soulware/scripts/soulkit.py export examples/moss.soulkit.json --output /new/output/directory
```

The command exits nonzero on invalid content and reports a structured error. The website can validate with its own JSON Schema library and the additional checks above; the shared Python importer is the compatibility reference.

## Scope and setup

`conversation` changes assistant replies; `writing` changes prose artifacts; `both` covers both. Artifact audience, format, explicit instructions, and factual accuracy continue to govern the task. The website should communicate this choice in ordinary language.

The plugin can apply a kit in a conversation. On local Codex it can install a reusable skill and optionally set a saved default. A generic ChatGPT conversation cannot be assumed to write a user's local files or change account preferences. Keep client-specific claims out of the kit itself.

The canonical schema is maintained by the plugin task. The Website task can vendor a byte-identical copy and record its hash. Coordinate changes to the contract before altering field names or validation rules.
