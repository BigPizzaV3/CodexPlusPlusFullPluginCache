# Detailed design guidance

## Thumbnail Text Rules

```json
{
  "default_word_count": "0-5 words",
  "preferred": "1-4 words",
  "rules": [
    "Use large readable words.",
    "Do not repeat the exact video title unless repetition is necessary.",
    "Prefer one short phrase.",
    "Avoid paragraph-length text.",
    "Avoid unnecessary punctuation.",
    "Use numbers only when they materially support the concept.",
    "Do not invent numerical claims.",
    "Do not use fake quotes.",
    "Do not use misleading labels such as FREE, SECRET, EXPOSED, or GUARANTEED unless the video genuinely supports them."
  ],
  "examples": [
    {
      "video_title": "I Used AI to Build a SaaS in 7 Days",
      "weak_thumbnail_text": "I Used AI to Build a SaaS in 7 Days",
      "stronger_options": [
        "7 DAYS",
        "AI BUILT THIS?",
        "$0 → SaaS"
      ]
    }
  ]
}
```

## Title Thumbnail Pairing

```json
{
  "goal": "Make the title and thumbnail provide complementary information.",
  "rules": [
    "Do not make the thumbnail simply restate the full title.",
    "Let the title explain context while the thumbnail creates a visual question, result, contrast, or proof point.",
    "If the title already contains a number, the thumbnail does not always need the same number.",
    "Avoid conflicting claims between title and thumbnail."
  ],
  "example": {
    "title": "I Built 10 AI Tools in 30 Days",
    "possible_thumbnail_text": "10 TOOLS",
    "visual": "Creator surrounded by several clearly differentiated app cards with one large finished product in focus"
  }
}
```