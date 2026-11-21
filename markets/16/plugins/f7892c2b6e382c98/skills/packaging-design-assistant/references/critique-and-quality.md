# Critique, Reference Use, and Quality Control

## Packaging Critique
```json
{
  "dimensions": [
    "Product identification",
    "Brand recognition",
    "Visual hierarchy",
    "Text readability",
    "Information density",
    "Variant clarity",
    "Front-panel clarity",
    "Back-panel organization",
    "Print practicality",
    "Dieline placement",
    "Material fit",
    "Finish practicality",
    "Shelf recognition",
    "Ecommerce readability",
    "Claim accuracy"
  ],
  "output_schema": {
    "what_works": "array",
    "problems": "array",
    "production_concerns": "array",
    "missing_information": "array",
    "recommended_changes": "array",
    "revised_direction": "string"
  },
  "rule": "Use descriptive feedback rather than arbitrary numeric scoring unless the user specifically requests scores."
}
```

## Competitor Reference Rules
```json
{
  "allowed": [
    "Analyze category conventions",
    "Analyze visual hierarchy",
    "Analyze common package structures",
    "Analyze shelf color patterns",
    "Analyze front-panel information patterns",
    "Identify opportunities for visual distinction"
  ],
  "not_allowed": [
    "Copy another brand's package exactly",
    "Reproduce protected illustrations",
    "Use another brand's logo",
    "Create confusingly similar trade dress"
  ],
  "rule": "Use category observations to create a fresh design direction."
}
```

## Quality Control
```json
{
  "checks_before_output": [
    "Product facts match user-supplied information.",
    "No invented ingredients.",
    "No invented nutrition data.",
    "No invented certifications.",
    "No unsupported health claims.",
    "No unsupported environmental claims.",
    "No invented dimensions.",
    "No invented barcode.",
    "Unknown mandatory information is marked as placeholder.",
    "Visual hierarchy is clear.",
    "Product type is identifiable.",
    "Variant is identifiable.",
    "Critical elements avoid known trim or fold areas.",
    "Production assumptions are clearly labeled.",
    "Concept mockup is not presented as final production artwork."
  ]
}
```
