---
name: properties-list-property-types
description: List PropBot parent and child property types before creating a listing.
---

Use this skill when a person asks which property types PropBot supports, or before creating a listing.

Permission: none. This is a public read.

1. Call properties_public_property_type_list with no parent id to list parent types.
2. Call properties_public_property_type_list with one parentTypeId to list the child types for that parent.
3. Use the returned ids. Do not invent a type name or a numeric id.

Shared stops:

- A parent id and a child id are both required before properties_private_listing_create.
- The child must belong to the chosen parent.
- Do not open another company's private records.
- Follow the person's explicit instruction when it is within these tools.
