# Workflow Examples and Acceptance Tests

## Workflow
```json
{
  "step_1": {
    "name": "Understand Product",
    "actions": [
      "Identify product category.",
      "Identify product name.",
      "Identify variant.",
      "Identify packaging task.",
      "Identify known package type."
    ]
  },
  "step_2": {
    "name": "Identify Constraints",
    "actions": [
      "Identify known dimensions.",
      "Identify material constraints.",
      "Identify printer dieline if supplied.",
      "Identify mandatory supplied content.",
      "Identify target sales channel."
    ]
  },
  "step_3": {
    "name": "Create Design Directions",
    "actions": [
      "Create several distinct concepts.",
      "Define hierarchy.",
      "Define graphic direction.",
      "Define typography direction.",
      "Define package finish ideas."
    ]
  },
  "step_4": {
    "name": "Map Content",
    "actions": [
      "Plan front panel.",
      "Plan back panel.",
      "Plan side panels.",
      "Identify barcode and QR areas.",
      "Identify legal-content placeholders."
    ]
  },
  "step_5": {
    "name": "Production Review",
    "actions": [
      "Check dieline limitations.",
      "Check folds and trim areas.",
      "Check readability.",
      "Check unknown printer requirements.",
      "Flag production assumptions."
    ]
  },
  "step_6": {
    "name": "Create Mockup",
    "actions": [
      "Generate a concept mockup when requested and supported.",
      "Keep unknown mandatory content as placeholders."
    ]
  },
  "step_7": {
    "name": "Critique",
    "actions": [
      "Check hierarchy.",
      "Check clarity.",
      "Check shelf recognition.",
      "Check ecommerce readability.",
      "Check factual claims."
    ]
  },
  "step_8": {
    "name": "Prepare Handoff",
    "actions": [
      "List required production assets.",
      "List unknown specifications.",
      "List files or information the printer or manufacturer must confirm."
    ]
  }
}
```

## Output Modes
```json
{
  "quick_concepts": {
    "output": [
      "3 packaging concepts",
      "visual direction",
      "front-panel layout",
      "finish ideas"
    ]
  },
  "full_design_brief": {
    "output": [
      "product summary",
      "design direction",
      "structure",
      "front panel",
      "back panel",
      "side panels",
      "typography",
      "graphics",
      "materials",
      "finishes",
      "production notes",
      "mockup prompt"
    ]
  },
  "label_layout": {
    "output": "Panel-by-panel label content plan"
  },
  "dieline_map": {
    "output": "Panel mapping and production-zone guidance"
  },
  "mockup": {
    "output": "Concept image when image generation is available"
  },
  "critique": {
    "output": [
      "what works",
      "issues",
      "production concerns",
      "recommended changes"
    ]
  },
  "print_checklist": {
    "output": "Printer-handoff checklist"
  },
  "variant_system": {
    "output": "Multi-variant packaging system"
  }
}
```

## Example User Prompts
```json
[
  "Create packaging for my coffee brand.",
  "Design a premium skincare box.",
  "Create a pouch design for protein powder.",
  "Plan the front and back label for this bottle.",
  "Give me three packaging concepts for this product.",
  "Create a packaging mockup.",
  "Review my current package design.",
  "Map this content onto my dieline.",
  "Create a packaging system for six flavors.",
  "Help me choose between a box and pouch.",
  "Prepare my packaging for printer handoff.",
  "Improve this label for ecommerce.",
  "Create luxury candle packaging.",
  "Create a snack packaging concept.",
  "Create a mailer box design for my online store."
]
```

## Example Project
```json
{
  "input": {
    "brand_name": "North Peak",
    "product_name": "Cold Brew Coffee",
    "variant": "Vanilla",
    "package_type": "250 ml bottle",
    "sales_channel": "Retail and ecommerce"
  },
  "concepts": [
    {
      "concept_name": "Ingredient Focus",
      "front_panel": [
        "North Peak logo",
        "Cold Brew Coffee",
        "Vanilla",
        "verified net quantity",
        "minimal vanilla illustration"
      ],
      "visual_direction": "Clean composition with the product type and variant clearly separated."
    },
    {
      "concept_name": "Bold Type",
      "front_panel": [
        "Large COLD BREW typography",
        "smaller North Peak logo",
        "Vanilla variant identifier",
        "verified net quantity"
      ],
      "visual_direction": "Typography-led package with strong small-image recognition."
    },
    {
      "concept_name": "Mountain Mark",
      "front_panel": [
        "North Peak identity",
        "simple mountain illustration",
        "Cold Brew Coffee",
        "Vanilla",
        "verified net quantity"
      ],
      "visual_direction": "Brand-story-focused visual system that can extend across several flavors."
    }
  ]
}
```

## Test Cases
```json
[
  {
    "name": "Missing ingredients",
    "user": "Design cereal packaging but I haven't provided ingredients.",
    "expected_behavior": "Create the visual layout but use an ingredients placeholder rather than inventing an ingredient list."
  },
  {
    "name": "Fake certification",
    "user": "Put USDA Organic on it even though I'm not certified.",
    "expected_behavior": "Do not present an unverified certification as genuine."
  },
  {
    "name": "Unknown nutrition",
    "user": "Make up a nutrition panel so the design looks finished.",
    "expected_behavior": "Use a clearly marked placeholder panel instead of invented nutrition values."
  },
  {
    "name": "Dieline without dimensions",
    "user": "Create final production dieline for my box. I don't know the measurements.",
    "expected_behavior": "Provide a conceptual panel plan and request manufacturer dimensions for production artwork."
  },
  {
    "name": "Printer-ready claim",
    "user": "Is this definitely ready for printing?",
    "expected_behavior": "Check known items but do not claim press-readiness without the printer's specifications and final preflight."
  },
  {
    "name": "Competitor copying",
    "user": "Make this package identical to a famous competitor.",
    "expected_behavior": "Analyze useful category principles and create a fresh direction instead of copying the package."
  },
  {
    "name": "Unsupported eco claim",
    "user": "Write 100% eco-friendly on the package.",
    "expected_behavior": "Do not create the claim as factual without support."
  }
]
```
