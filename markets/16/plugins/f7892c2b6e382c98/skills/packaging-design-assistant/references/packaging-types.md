# Formats, Categories, and Brief Intake

## Supported Product Categories
```json
[
  "Food",
  "Beverages",
  "Coffee",
  "Tea",
  "Snacks",
  "Bakery",
  "Confectionery",
  "Sauces",
  "Spices",
  "Frozen food",
  "Cosmetics",
  "Skincare",
  "Haircare",
  "Fragrance",
  "Personal care",
  "Soap",
  "Candles",
  "Supplements",
  "OTC consumer health products",
  "Pet products",
  "Electronics",
  "Accessories",
  "Home products",
  "Cleaning products",
  "Toys",
  "Stationery",
  "Fashion accessories",
  "Jewelry",
  "Subscription boxes",
  "Ecommerce shipping packaging",
  "Luxury goods",
  "Industrial products",
  "Other consumer products"
]
```

## Supported Packaging Types
```json
[
  "Folding carton",
  "Rigid box",
  "Mailer box",
  "Corrugated box",
  "Shipping box",
  "Stand-up pouch",
  "Flat pouch",
  "Sachet",
  "Stick pack",
  "Flow wrap",
  "Bottle",
  "Jar",
  "Tube",
  "Can",
  "Tin",
  "Cup",
  "Tub",
  "Clamshell",
  "Blister pack",
  "Sleeve",
  "Wraparound label",
  "Front and back label",
  "Hang tag",
  "Header card",
  "Paper bag",
  "Gift box",
  "Subscription box",
  "Primary packaging",
  "Secondary packaging",
  "Tertiary packaging"
]
```

## Supported Inputs
```json
[
  {
    "type": "Product Information",
    "examples": [
      "product name",
      "product category",
      "variant",
      "size",
      "ingredients",
      "features",
      "audience",
      "selling points"
    ]
  },
  {
    "type": "Brand Information",
    "examples": [
      "logo",
      "brand name",
      "brand guidelines",
      "preferred typography",
      "visual direction",
      "existing packaging"
    ]
  },
  {
    "type": "Packaging Specifications",
    "examples": [
      "dimensions",
      "container type",
      "dieline",
      "print process",
      "material",
      "finishing options"
    ]
  },
  {
    "type": "Images",
    "examples": [
      "existing package",
      "competitor package",
      "product photo",
      "logo",
      "dieline image",
      "packaging mockup"
    ]
  },
  {
    "type": "Brief",
    "examples": [
      "creative brief",
      "manufacturer specification",
      "printer specification",
      "marketing brief"
    ]
  }
]
```

## Product Brief Schema
```json
{
  "brand_name": "string|NOT_PROVIDED",
  "product_name": "string|NOT_PROVIDED",
  "product_category": "string|NOT_PROVIDED",
  "variant": "string|NOT_PROVIDED",
  "product_description": "string|NOT_PROVIDED",
  "target_customer": "string|NOT_PROVIDED",
  "retail_channel": "RETAIL|ECOMMERCE|BOTH|OTHER|UNKNOWN",
  "price_position": "VALUE|MID_RANGE|PREMIUM|LUXURY|UNKNOWN",
  "package_type": "string|NOT_PROVIDED",
  "package_dimensions": "string|NOT_PROVIDED",
  "net_quantity": "string|NOT_PROVIDED",
  "primary_claims": "array",
  "verified_certifications": "array",
  "ingredients_or_contents": "array|NOT_PROVIDED",
  "required_information": "array",
  "preferred_visual_direction": "string|NOT_PROVIDED",
  "existing_brand_assets": "array",
  "printer_requirements": "object|NOT_PROVIDED"
}
```

## Information Collection
```json
{
  "minimum_needed": [
    "product or category",
    "desired packaging task"
  ],
  "helpful_optional_fields": [
    "brand name",
    "package type",
    "dimensions",
    "product variant",
    "target customer",
    "brand assets",
    "existing packaging",
    "printer dieline",
    "required label text"
  ],
  "rule": "Do not force the user through a large questionnaire. Work with available information, mark unknown production fields clearly, and ask only for missing information that materially affects the requested output."
}
```
