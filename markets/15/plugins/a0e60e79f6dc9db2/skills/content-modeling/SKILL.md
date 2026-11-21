---
name: content-modeling
description: Explain, design or change the structure of an Agility CMS instance - content models, component models, page models, fields and containers. Use when a developer or architect asks how content is structured, wants to add or change a field, create a new model or container, or plan a content architecture.
---

# Content models, components and containers

## How Agility structures content

- A **content model** defines the fields of a type of content, such as Blog Post.
- A **container** is a list of items that use one content model, such as
  BlogPosts. Content items are saved into containers. One model can back several
  containers.
- A **component model** defines a module that editors place in a page zone.
- A **page model** defines a page template and its zones.

To explain an instance, call `get_content_models`, `get_component_models`,
`get_page_models` and `get_containers`, then `get_content_model_details` or
`get_component_model_details` for the ones that matter. Describe how they connect:
which containers use which model, and which fields link to other content.

## Changing a model: read, modify, save the whole thing

1. Read the model with `get_content_model_details` (or
   `get_component_model_details`).
2. Change only what the user asked for.
3. Save the **complete** model: every field, with every setting it had. A save
   replaces each field's settings, so a setting you leave out is removed.
4. Read the model again and confirm the change and that the other fields are
   unchanged.

Use `save_component_model` for components and `save_content_model` for content
models. They take the same shape, but are not interchangeable: saving a component
through `save_content_model` converts it and orphans its content.

Changing or removing a field on a model that already has content affects every
item using it. Say this before saving, and say which containers use the model.

## Creating new models and containers

- Check the existing models (`get_content_models`, `get_component_models`) and
  containers (`get_containers`) first. Reuse or extend before creating.
- There is no tool to delete a model. A model created by mistake stays in the
  instance. Confirm the name, reference name and fields with the user before the
  first save.
- After creating a content model, create a container for it with `save_container`
  so editors can add items.

## Field rules

- Linked-content fields (fields that point at other content) do not have
  `required`, `unique` or "copy across all languages" settings in Agility. Do not
  add them.
- Field reference names must be unique within the model. Keep the casing
  consistent; developers' code reads these names.
- Prefer clear, stable reference names. Renaming a field later breaks the code
  that reads it. Avoid all-caps abbreviations: the Fetch API lowercases only the
  first letter, so `URL` arrives as `uRL`. Use `Url` and `Cta` instead.
- Reference names can be normalized when a container or model is created. After
  saving, take the name from the save result or from `get_containers`, not from
  what you asked for.
- Hide-when (conditional visibility) formulas support only `[eq]`, `[ne]`,
  `[lt]` and `[gt]`. Anything else fails silently.
- Single-item containers cannot be created with these tools. Create them in the
  Agility app, or use a one-item list.
- Saving a page model with a zone left out removes that zone and the components
  placed in it. Send every zone.

## Look up the platform docs

For exact field-type names and settings, search Agility's documentation (the
Agility Knowledgebase MCP's `search_docs` and `fetch_doc`, if connected, or
https://agilitycms.com/docs) rather than guessing.

## When the user asks for code

These tools change the CMS, not a codebase. For front-end code, explain the model
structure the code will receive, and point developers to the Agility CMS
documentation at https://agilitycms.com/docs for SDK details.
