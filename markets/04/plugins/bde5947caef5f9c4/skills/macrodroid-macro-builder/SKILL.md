---
name: macrodroid-macro-builder
description: Build an import-ready MacroDroid macro (Android automation) from a plain-language description using the MacroDroid feature catalog, schema and validator tools. Use whenever the user asks for a MacroDroid macro, automation, trigger, action or constraint, or to change a macro you produced earlier.
---

A MacroDroid macro is TRIGGERS (events that start it) + ACTIONS (what it does when it runs) + CONSTRAINTS (conditions that must be true for it to run). The user describes what they want; you produce complete macro JSON.

Never write macro JSON from memory. Feature names and field layouts must come from the tools, in this order:

1. `list_macrodroid_features` - read the full catalog and follow its selection rules to pick the triggers, actions and constraints the macro needs. Use exact catalog names only. Include a state-checking constraint whenever the trigger could fire when the action makes no sense (already in a call, screen off, not at home...).
2. `get_macrodroid_schema` - pass the selected names. It returns the JSON layout for those features and the rules for writing the macro. If it warns that a name does not exist, call it again with the suggested name. Read the schema before writing anything.
3. Write the complete macro JSON following the schema and rules exactly. Keep it compact: omit optional fields that hold default values.
4. `validate_macrodroid_macro` - pass the whole JSON as a string. Fix every reported problem and validate again. Never show the user a macro that has not passed validation.

Reply format:

- ONE ```json code block with the complete, validated JSON. Nothing may be cut off; if the macro would be huge, simplify it instead.
- Then a short plain-language summary of what the macro does and any assumptions made (a WiFi name, a time, a contact). Ask at most one clarifying question and only when the request is truly ambiguous; otherwise assume and say so.
- Keep user-visible text inside the macro (notification titles, messages, spoken text) in the language the user wrote in.
- Explain how to import: save the JSON as a file ending in `.macro` and use Import on the Macros tab in MacroDroid, or paste it into the AI Macro Builder at https://remote.macrodroid.com which sends it to the phone.
- If the reply is cut off and the user says continue, resume exactly where you stopped without repeating anything.

For changes to a macro already produced, skip `list_macrodroid_features` unless new features are needed, but call `get_macrodroid_schema` for any new feature and `validate_macrodroid_macro` on the changed JSON.
