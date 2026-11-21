---
name: formulare
description: Build, publish and embed Formkurier forms and read their answers in the connected workspace.
---

Use the Formkurier tools for the connected workspace only. Before creating a form, ask only for what is missing to
build a sensible first version; prefer the short YAML form (`fields` with key, type, label, required, options).
Show the user the fields you are about to create. After creating, offer to publish; publishing is a separate step.

Answers contain personal data. Read them only when the user asks, return only the fields needed, and do not repeat
them outside the conversation. Deleting answers, archiving forms, switching the storage mode and changing the
webhook need the user's explicit confirmation of that exact action.

In pass-through mode Formkurier keeps no answers: say so instead of searching for them, and point to the deliveries
list for status. If a tool reports that the subscription is required, explain that and link the subscription page.
