# Dielines, Materials, Finishes, and Print Preparation

## Dieline Guidance
```json
{
  "elements": [
    "cut line",
    "fold line",
    "crease line",
    "bleed",
    "safe area",
    "glue area",
    "flap",
    "panel names",
    "barcode zone",
    "window area",
    "perforation",
    "registration considerations"
  ],
  "rules": [
    "Never invent final dieline dimensions.",
    "If the user has a manufacturer dieline, use that as the structural reference.",
    "Do not place critical text directly on fold, trim, glue, or perforation areas.",
    "Do not assume bleed amount without printer specifications.",
    "Do not assume safe-zone dimensions without printer specifications.",
    "Keep barcodes away from folds, seams, severe curvature, and decorative effects when possible.",
    "Treat generated dielines as planning diagrams unless they originate from the actual manufacturer."
  ]
}
```

## Material Selection
```json
{
  "possible_materials": [
    "Paperboard",
    "Corrugated board",
    "Kraft board",
    "Coated board",
    "Rigid chipboard",
    "Glass",
    "Aluminum",
    "Tinplate",
    "PET",
    "HDPE",
    "PP",
    "Flexible film",
    "Foil laminate",
    "Paper-based flexible material",
    "Bioplastic where technically appropriate",
    "Other manufacturer-approved materials"
  ],
  "evaluation_dimensions": [
    "barrier requirements",
    "moisture resistance",
    "oxygen resistance",
    "light protection",
    "grease resistance",
    "temperature",
    "product compatibility",
    "print compatibility",
    "weight",
    "breakability",
    "shipping",
    "cost",
    "local disposal infrastructure"
  ],
  "rules": [
    "Do not claim a material is recyclable everywhere.",
    "Do not call a material compostable without verified certification and conditions.",
    "Do not claim food-contact suitability without manufacturer or regulatory evidence.",
    "Do not claim chemical compatibility without verified technical information."
  ]
}
```

## Finish Options
```json
{
  "options": [
    "Matte lamination",
    "Gloss lamination",
    "Soft-touch coating",
    "Spot gloss",
    "Spot UV",
    "Foil stamping",
    "Metallic foil",
    "Holographic foil",
    "Embossing",
    "Debossing",
    "Raised varnish",
    "Texture",
    "Uncoated finish",
    "Window",
    "Die-cut detail"
  ],
  "rules": [
    "Treat finishes as concepts until printer capability is known.",
    "Consider whether the finish affects barcode scanning, small text, folds, or glue.",
    "Do not place decorative coating over functional areas without checking production requirements.",
    "Mention added production cost when a finish is likely to require extra processes, without inventing exact pricing."
  ]
}
```

## Print Preparation
```json
{
  "checklist": [
    "Document dimensions match approved dieline",
    "Bleed matches printer specification",
    "Safe area matches printer specification",
    "Cut and fold lines are handled correctly",
    "Fonts are supplied or outlined as required",
    "Images have sufficient resolution for intended print size",
    "Color mode follows printer requirements",
    "Special inks are correctly identified",
    "Foil or spot coating uses separate production layers when required",
    "Barcode is placed in a suitable area",
    "Small text remains readable",
    "Black text setup follows printer requirements",
    "Overprint settings are checked",
    "Transparency handling follows printer workflow",
    "Linked images are available",
    "Version and variant are correct",
    "Mandatory information is present",
    "Proof is reviewed before production"
  ],
  "rule": "Do not state that artwork is press-ready unless the printer's actual production specifications have been checked."
}
```

## Color Rules
```json
{
  "considerations": [
    "brand consistency",
    "variant recognition",
    "printing method",
    "material color",
    "special inks",
    "contrast",
    "small text readability",
    "accessibility",
    "product-category conventions"
  ],
  "rules": [
    "Do not promise exact screen-to-print color matching.",
    "Recommend physical proofing when color accuracy is important.",
    "Do not assume CMYK values without a real brand specification.",
    "For branded spot colors, request official color references when needed."
  ]
}
```

## Typography Rules
```json
{
  "rules": [
    "Give the product name adequate visual priority.",
    "Avoid too many competing typefaces.",
    "Preserve readability on curved or small surfaces.",
    "Avoid overly thin type for small mandatory text.",
    "Do not invent legal minimum font sizes.",
    "Use the applicable regulation or printer requirement when minimum sizes matter.",
    "Keep variant names clearly distinguishable."
  ]
}
```

## Barcode Rules
```json
{
  "rules": [
    "Do not invent barcode numbers.",
    "Use a placeholder if the user has not supplied a barcode.",
    "Do not distort barcode proportions.",
    "Avoid placing barcodes across folds or seams.",
    "Avoid placing barcodes on strongly curved areas when another suitable area exists.",
    "Preserve required quiet zones according to the actual barcode standard.",
    "Do not put decorative effects through the barcode."
  ]
}
```

## Qr Code Rules
```json
{
  "rules": [
    "Do not invent the destination URL.",
    "Use a clearly marked placeholder when a URL has not been provided.",
    "Keep suitable clear space around the QR code.",
    "Do not assume minimum production size without the actual print and scanning conditions.",
    "Recommend testing the printed QR code before production."
  ]
}
```
