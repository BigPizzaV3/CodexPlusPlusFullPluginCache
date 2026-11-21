# Mockup and Channel Visual Planning

## Mockup Creation
```json
{
  "enabled_when_image_generation_available": true,
  "mockup_types": [
    "front-facing retail package",
    "three-quarter package view",
    "shelf scene",
    "ecommerce product image",
    "box mockup",
    "pouch mockup",
    "bottle label mockup",
    "jar label mockup",
    "tube mockup",
    "shipping box mockup",
    "unboxing scene"
  ],
  "rules": [
    "Treat generated images as concepts unless based on exact production artwork.",
    "Do not present an AI-generated mockup as a manufactured sample.",
    "Keep product claims consistent with supplied information.",
    "Do not invent mandatory label text.",
    "If exact logo placement is required, use the supplied logo."
  ]
}
```

## Mockup Prompt Schema
```json
{
  "package_type": "string",
  "view": "FRONT|THREE_QUARTER|SIDE|TOP|SHELF|ECOMMERCE",
  "material": "string",
  "package_shape": "string",
  "main_graphics": "string",
  "label_content": "string",
  "environment": "string",
  "lighting": "string",
  "camera": "string",
  "surface": "string",
  "production_finish": "array",
  "avoid": "array"
}
```

## Shelf Design
```json
{
  "evaluation": [
    "brand recognition",
    "product-category recognition",
    "variant recognition",
    "contrast against likely competitors",
    "readability at distance",
    "distinct silhouette when applicable",
    "front-panel information density"
  ],
  "rule": "Do not claim actual retail performance without testing."
}
```

## Ecommerce Design
```json
{
  "evaluation": [
    "readability in small product cards",
    "clear product type",
    "clear variant",
    "strong front-facing package recognition",
    "minimal dependence on small text",
    "consistent package silhouette"
  ]
}
```
