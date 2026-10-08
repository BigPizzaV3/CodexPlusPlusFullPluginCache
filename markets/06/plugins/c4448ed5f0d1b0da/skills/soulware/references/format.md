# Soul Kit exchange format, version 1

A Soul Kit is a UTF-8 JSON object, normally downloaded as `<id>.soulkit.json`. Maximum encoded size is 262144 bytes. The website generates content; the plugin renders installation files. There are no executable fields.

The [machine schema](soul-kit.schema.json) is bundled alongside this guide as an unchanged copy of the plugin's canonical schema. For local validation use the bundled importer. A manual inspection in ChatGPT should check the following shape and reject inconsistent or missing fields; it is not a substitute for the automated importer when installing files.

| Field | Expected value |
| --- | --- |
| format | Exactly `soulware.soul-kit` |
| format_version | Integer `1` |
| id | 1–48 characters; lowercase letters/digits separated by single hyphens |
| name | Nonempty string, at most 80 characters |
| version | Numeric `X.Y.Z`; 1–4 digits per component |
| summary | Nonempty string, at most 400 characters |
| scope | `conversation`, `writing`, or `both` |
| voice | Object containing core, traits, style_rules, avoid |
| behavior | Object with explain, disagree, uncertainty, mistakes, progress |
| adaptations | Object with everyday, focused, sensitive, writing |
| examples | 3–8 objects with situation, user, assistant, note |
| checks | 3–8 nonempty strings, each at most 240 characters |

`voice.core` is at most 800 characters. `traits` has 3–6 entries of at most 240 characters; `style_rules` has 3–12 entries of at most 400; `avoid` has 0–8 entries of at most 240. Each behavior and adaptation is a nonempty string of at most 600 characters.

For each example, situation is at most 160 characters; user 800; assistant 1800; note 400. All four are required. An example's assistant reply illustrates the voice; it does not become a response to the current user.

All objects are closed: unknown properties and duplicate keys are invalid. Strings must contain visible content, may use newline or tab, and may not contain other ASCII control characters or `SOULWARE:DEFAULT` or `soulware-kit:` marker text in any letter case. The importer reserves that marker for managing a user's default instructions.

Only the fixed envelope and native output layout are machine contracts. Personality content remains editable guidance subject to the current task and platform instructions.
