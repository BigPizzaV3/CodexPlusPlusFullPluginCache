# Packaging Copy and Claims

## Packaging Copy
```json
{
  "supported_copy": [
    "product name",
    "variant name",
    "short product descriptor",
    "front-of-pack benefit line",
    "product story",
    "usage instructions",
    "feature descriptions",
    "brand story",
    "call to action"
  ],
  "rules": [
    "Base claims on user-supplied facts.",
    "Do not invent health benefits.",
    "Do not invent environmental benefits.",
    "Do not invent certification language.",
    "Do not rewrite legally required warnings in a way that changes their meaning.",
    "Use placeholders for unknown legal or technical content."
  ]
}
```

## Claim Types
```json
{
  "creative_claim": {
    "example": "A short emotional or lifestyle statement.",
    "rule": "Must not contradict product facts."
  },
  "functional_claim": {
    "example": "Describes a product function.",
    "rule": "Require support from product facts."
  },
  "health_claim": {
    "rule": "Do not create as factual without applicable evidence and regulatory support."
  },
  "environmental_claim": {
    "rule": "Do not create as factual without evidence."
  },
  "certification_claim": {
    "rule": "Only use certifications confirmed by the user or verified sources."
  }
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
