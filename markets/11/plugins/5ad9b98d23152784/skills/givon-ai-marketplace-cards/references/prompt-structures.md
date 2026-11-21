# Marketplace Prompt Structures

Build a focused visual brief for each requested asset, then adapt it to the selected model's
current family guidance and schema.

## Base brief

```text
Asset role: <main / angle / detail / lifestyle / included items / infographic / page module>
Marketplace or placement: <when it changes the visual requirements>
Product identity: <relevant visible details>
Reference role: <product identity / style / composition / none>
Buyer information: <facts or message needed in this asset>
Composition: <product scale, angle, crop, text hierarchy>
Exact text: <quoted wording and placement, when requested>
Preserve: <product details that stay stable>
```

Keep only relevant lines.

## Composition by role

- **Main image:** product-first composition, clear scale, material and silhouette.
- **Angle/detail:** one specific buyer question, feature or material in focus.
- **Lifestyle:** a context that explains use while keeping the product legible.
- **Included items:** a clear separated layout of the supplied contents.
- **Infographic:** short exact facts with readable hierarchy and mobile-scale text.
- **Page module:** one message per module with a shared visual system across the page.

Use supplied facts exactly when the asset represents a real listing. For a user-requested concept
or mock, retain the stated hypothetical context. Count, aspect, resolution, reference slots and
other typed controls come from the selected model schema.
