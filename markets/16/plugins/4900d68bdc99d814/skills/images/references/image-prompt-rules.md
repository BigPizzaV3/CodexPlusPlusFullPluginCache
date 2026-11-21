# Detailed design guidance

## Image Generation

```json
{
  "enabled_when_available": true,
  "default_behavior": "When the user explicitly asks to create, generate, make, or design the actual thumbnail, create the image rather than returning only instructions.",
  "image_requirements": [
    "16:9 composition",
    "Clear main subject",
    "Space for text if text is requested",
    "Strong readability at small size",
    "No unnecessary micro-details",
    "No watermarks",
    "No fake platform UI unless requested and factually appropriate"
  ],
  "user_photo_rule": "If the thumbnail includes the user and no image of the user has been provided in the current conversation, ask the user to upload a photo before generating their likeness."
}
```

## Image Prompt Builder

```json
{
  "prompt_components": [
    "canvas and composition",
    "main subject",
    "subject position",
    "facial expression if relevant",
    "camera framing",
    "background",
    "lighting",
    "supporting objects",
    "text area",
    "visual hierarchy",
    "thumbnail-specific readability requirements"
  ],
  "prompt_rule": "Describe visual relationships clearly instead of filling the prompt with vague quality adjectives."
}
```

## Image Prompt Schema

```json
{
  "format": "YouTube thumbnail, 16:9",
  "main_subject": "string",
  "composition": "string",
  "background": "string",
  "expression": "string|NOT_APPLICABLE",
  "lighting": "string",
  "props": "array",
  "text_overlay": "string|NONE",
  "text_area": "string|NONE",
  "avoid": "array"
}
```