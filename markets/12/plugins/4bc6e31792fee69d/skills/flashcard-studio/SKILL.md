---
name: flashcard-studio
description: Review user-supplied flashcard pairs and export paired cut-out PDF cards or a Front/Back import CSV.
---

Call `generate_flashcard_deck` when the user supplies explicit question-answer pairs and requests interactive review, printable cut-out cards, or CSV import. Preserve the provided learning content; do not invent or verify answers. Pass optional title and A4 or Letter paper size. Explain duplicate removal and any PDF character substitutions. CSV has no header; import as Front/Back plain text with HTML disabled. Progress stays in the current widget session; ratings are self-assessments. Do not use for factual answers, exams, or spaced-repetition scheduling. Large decks should be split to stay within the 2,800-byte payload limit.
