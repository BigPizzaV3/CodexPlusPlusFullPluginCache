# HỌC NHI — v0.7.0 Release Notes

Source bundle: `Hocnhi.zip` / 0.6.1. This package is an educational Skills-only plugin, not a medical service.

## Kept unchanged

- Portable package `name` ID, original logo `assets/gpt-icon.png` (binary identical).
- All five original pedagogical, reasoning, evidence, Update by Bing and response-pattern reference `.txt` files (binary identical).
- Existing Skills-only package layout and `Education & Research` category.

## Enhanced

- Rewrote core `SKILL.md` to formalize topic-based teaching, learner adaptation, sequential synthetic case reasoning, lecture/file study, pediatric lab context and urgent-symptom boundaries.
- Added 4 reference playbooks for age-specific curriculum, Bloom/MCQ and answer-release policy, simulated cases/classroom-sharing, reference audit/evidence appraisal.
- Added explicit no-answer-before-attempt behavior for user-requested practice quizzes. Added Bloom 6 caution where MCQ format cannot assess creation directly.
- Added source provenance labels S0–S3 (pedagogical labels, **not** GRADE certainty).
- Retained Update by Bing as a real-web-verification workflow, never a claim that Bing is necessarily the actual underlying search engine.
- Improved metadata, three starter prompts, four HLP Plugin Hub listing URLs, and author/homepage URLs.
- Updated internal skills reference index and display metadata.

## Explicit limitations

No dynamic browser/clinical performance validation performed by packaging QA. The four HLP URLs were **not reachable from the available web fetch tool** and should be tested manually in a browser before submission. A successful static check does not imply OpenAI review approval. Publication and pricing are controlled separately; no unnecessary `publication`/`commerce` declarations were added.
