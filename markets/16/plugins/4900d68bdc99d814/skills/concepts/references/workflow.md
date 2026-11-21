# Detailed design guidance

## Workflow

```json
{
  "step_1": {
    "name": "Understand Video",
    "actions": [
      "Identify title or topic.",
      "Understand the central promise.",
      "Identify the target viewer when known.",
      "Identify available images."
    ]
  },
  "step_2": {
    "name": "Find Visual Hook",
    "actions": [
      "Identify the most visually interesting element.",
      "Identify result, contrast, object, person, transformation, or question."
    ]
  },
  "step_3": {
    "name": "Generate Concepts",
    "actions": [
      "Create three different concepts by default.",
      "Use different compositions and visual hooks.",
      "Keep each concept easy to understand."
    ]
  },
  "step_4": {
    "name": "Create Text Options",
    "actions": [
      "Generate short text options when useful.",
      "Avoid repeating the entire title."
    ]
  },
  "step_5": {
    "name": "Build Composition",
    "actions": [
      "Define subject placement.",
      "Define text placement.",
      "Define background.",
      "Define visual order."
    ]
  },
  "step_6": {
    "name": "Generate Image",
    "actions": [
      "If the user asks for the actual thumbnail and image generation is available, create it.",
      "If a user likeness is required and no photo is supplied, request a photo."
    ]
  },
  "step_7": {
    "name": "Review",
    "actions": [
      "Check clarity.",
      "Check mobile readability.",
      "Check factual accuracy.",
      "Check clutter.",
      "Check title-thumbnail relationship."
    ]
  },
  "step_8": {
    "name": "Create Variants",
    "actions": [
      "Create additional concept variants when requested.",
      "Change the central idea rather than only changing typography."
    ]
  }
}
```

## Output Modes

```json
{
  "quick_ideas": {
    "output": [
      "3 thumbnail concepts",
      "text options",
      "visual layout"
    ]
  },
  "full_concepts": {
    "output": [
      "concept name",
      "visual hook",
      "composition",
      "text",
      "background",
      "subject",
      "why it fits",
      "image prompt"
    ]
  },
  "actual_thumbnail": {
    "output": "Generate thumbnail image when supported"
  },
  "prompt_only": {
    "output": "Production-grade thumbnail image prompt"
  },
  "critique": {
    "output": [
      "what works",
      "problems",
      "specific changes",
      "revised concept"
    ]
  },
  "variants": {
    "output": "Multiple meaningfully different thumbnail directions"
  }
}
```

## Input Schema

```json
{
  "video_title": "string|NOT_PROVIDED",
  "video_topic": "string|NOT_PROVIDED",
  "video_summary": "string|NOT_PROVIDED",
  "target_audience": "string|NOT_PROVIDED",
  "channel_niche": "string|NOT_PROVIDED",
  "channel_style": "string|NOT_PROVIDED",
  "creator_image_available": "boolean|UNKNOWN",
  "product_image_available": "boolean|UNKNOWN",
  "preferred_text": "string|NOT_PROVIDED",
  "preferred_mood": "string|NOT_PROVIDED",
  "brand_colors": "array|NOT_PROVIDED",
  "reference_images": "array|NOT_PROVIDED",
  "number_of_variants": "integer|DEFAULT_3"
}
```

## Concept Schema

```json
{
  "concept_id": "T1",
  "concept_name": "string",
  "core_idea": "string",
  "visual_hook": "string",
  "main_subject": "string",
  "subject_position": "LEFT|CENTER|RIGHT",
  "background": "string",
  "supporting_objects": "array",
  "text_overlay": "string|NONE",
  "text_position": "LEFT|CENTER|RIGHT|TOP|BOTTOM|NONE",
  "facial_expression": "string|NOT_APPLICABLE",
  "camera_framing": "string",
  "lighting": "string",
  "visual_hierarchy": [
    "first focal element",
    "second focal element",
    "third focal element"
  ],
  "title_relationship": "string",
  "why_it_works": "string",
  "image_generation_prompt": "string"
}
```