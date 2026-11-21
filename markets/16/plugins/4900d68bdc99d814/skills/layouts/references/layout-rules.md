# Detailed design guidance

## Youtube Format

```json
{
  "recommended_canvas": {
    "width": 1280,
    "height": 720,
    "aspect_ratio": "16:9"
  },
  "design_safe_zone": {
    "rule": "Keep important text and faces away from extreme edges and the lower-right area where YouTube duration badges may cover content."
  },
  "mobile_first_rule": "The main idea should remain understandable when the thumbnail is displayed very small."
}
```

## Visual Hierarchy Rules

```json
[
  "The viewer should understand the main subject almost immediately.",
  "Face or product should normally be larger than secondary elements.",
  "Text should not compete equally with the subject.",
  "Background details should support rather than dominate.",
  "Use empty space around important elements.",
  "Avoid equal visual weight across every object.",
  "If there are two subjects, make the relationship between them obvious."
]
```

## Concept Generation Rules

```json
[
  "Create genuinely different concepts rather than changing only text.",
  "Vary composition, visual metaphor, framing, and focal subject.",
  "Avoid putting more than three major visual elements into one thumbnail unless the concept requires it.",
  "Use one obvious subject whenever possible.",
  "Avoid generic stock-photo appearance.",
  "Avoid tiny UI elements that cannot be read at thumbnail size.",
  "If a screenshot is important, enlarge only the meaningful area.",
  "Avoid making every concept use arrows, circles, fire, shocked faces, or money symbols.",
  "Match the visual language to the video niche."
]
```