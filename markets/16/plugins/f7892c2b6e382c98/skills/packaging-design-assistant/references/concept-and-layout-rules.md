# Concept Development and Panel Layout

## Packaging Concept Schema
```json
{
  "concept_id": "P1",
  "concept_name": "string",
  "design_direction": "string",
  "main_visual_idea": "string",
  "front_panel": "string",
  "back_panel": "string",
  "side_panels": "string|NOT_APPLICABLE",
  "top_panel": "string|NOT_APPLICABLE",
  "bottom_panel": "string|NOT_APPLICABLE",
  "primary_focal_element": "string",
  "secondary_elements": "array",
  "product_name_treatment": "string",
  "variant_treatment": "string",
  "typography_direction": "string",
  "graphic_style": "string",
  "photography_or_illustration": "string",
  "finish_suggestions": "array",
  "material_direction": "array",
  "shelf_behavior": "string",
  "ecommerce_behavior": "string",
  "production_notes": "array",
  "unknown_requirements": "array",
  "mockup_prompt": "string"
}
```

## Concept Generation Rules
```json
[
  "Create visually different directions rather than minor variations.",
  "Change hierarchy, composition, visual language, image use, typography direction, and structural presentation between concepts.",
  "Do not add decorative features that interfere with mandatory information.",
  "Do not rely on tiny details for product recognition.",
  "Give the product name and product type enough visual priority.",
  "Make the package understandable from the expected viewing distance.",
  "Consider physical handling when relevant.",
  "Consider online thumbnail visibility when ecommerce is relevant."
]
```

## Visual Hierarchy
```json
{
  "typical_priority": [
    "Brand or product identity",
    "Product type",
    "Variant or flavor",
    "Main verified product benefit",
    "Net quantity when required",
    "Secondary details"
  ],
  "rules": [
    "Do not force this order when applicable regulations or product needs require another hierarchy.",
    "Avoid giving equal visual weight to every element.",
    "Keep critical product identification visible.",
    "Avoid overloading the principal display panel."
  ]
}
```

## Front Panel Planner
```json
{
  "possible_elements": [
    "brand name",
    "product name",
    "product type",
    "variant",
    "flavor",
    "verified benefit statement",
    "product image",
    "illustration",
    "net quantity",
    "verified certification mark",
    "category cue"
  ],
  "rule": "Only include factual claims or certifications supplied or verified by the user."
}
```

## Back Panel Planner
```json
{
  "possible_elements": [
    "product description",
    "usage instructions",
    "ingredients",
    "nutrition panel",
    "warnings",
    "storage information",
    "manufacturer information",
    "contact information",
    "website",
    "barcode",
    "QR code",
    "recycling instructions",
    "certification information",
    "batch information",
    "expiry information"
  ],
  "rule": "Do not generate mandatory legal content as factual unless the user provides it or current jurisdiction-specific requirements are verified."
}
```

## Side Panel Planner
```json
{
  "possible_elements": [
    "product story",
    "feature icons",
    "instructions",
    "ingredients",
    "nutrition information",
    "social links",
    "QR code",
    "warnings",
    "brand story",
    "variant indicator"
  ]
}
```

## Variant System
```json
{
  "use_cases": [
    "flavors",
    "scents",
    "sizes",
    "strengths",
    "formulas",
    "models",
    "collections"
  ],
  "rules": [
    "Keep core brand elements consistent across variants.",
    "Change one or two easy-to-recognize cues for each variant.",
    "Do not rely on color alone when accessibility or retail clarity would suffer.",
    "Keep product name placement consistent when possible.",
    "Give variant names enough distinction to avoid customer confusion.",
    "Ensure similar variants remain distinguishable in small ecommerce images."
  ],
  "possible_variant_cues": [
    "color family",
    "illustration",
    "ingredient image",
    "pattern",
    "variant badge",
    "secondary typography",
    "icon",
    "photography"
  ]
}
```

## Structural Packaging
```json
{
  "evaluation_dimensions": [
    "product protection",
    "product size",
    "product weight",
    "liquid or solid state",
    "shelf life considerations",
    "shipping requirements",
    "tamper evidence",
    "opening experience",
    "reclosure",
    "display requirements",
    "print area",
    "cost sensitivity",
    "storage efficiency"
  ],
  "rule": "Structural recommendations are conceptual unless engineering and manufacturer specifications are available."
}
```

## Panel Mapping Schema
```json
{
  "panel_id": "string",
  "panel_name": "FRONT|BACK|LEFT|RIGHT|TOP|BOTTOM|FLAP|OTHER",
  "dimensions": "string|UNKNOWN",
  "primary_content": "array",
  "secondary_content": "array",
  "production_restrictions": "array",
  "notes": "array"
}
```
