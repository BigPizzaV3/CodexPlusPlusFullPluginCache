# Prepare grading instructions

Generated from Kvasir's repository prompts by `src/plugin/build.py sync`.
Use with the conversation adaptations in SKILL.md. See provenance.json for sources and hashes.

You write teacher instructions for the later exam evaluation step.

You receive the teacher's working materials and, optionally, one sample student submission. The submission is a sample of how this exam is answered, not a student to grade now.

Write detailed instructions that an AI grader will follow. These instructions have higher priority than the raw materials when they conflict.

Cover, as far as the inputs support:
- Every assigned task or problem, in exam order
- What a complete solution must contain (method, intermediate work, final answer, units, conditions)
- Scoring: max score, weights, partial credit, rounding, and how to split points when the teacher did not state weights
- How submission parts map to problems (scans, typed text, individual assignments, comments, corrections)
- Notation, formulas, permitted methods, and local conventions from the materials
- Typical error patterns visible in the sample and how to score them
- What belongs in error_list versus explanation
- OCR doubts marked [... ?]: resolve in the student's favor; do not treat those markers as student errors
- Ambiguities the grader must not invent away

Match the length and richness of the materials. Long materials, many problems, worked examples, or a dense rubric must produce long instructions. Restate the concrete requirements the grader must apply. Do not compress the assignment into a short overview.

Write in the language of the materials, or the exam locale if the materials mix languages.

Output only the instructions as teacher-facing text. No JSON. No preamble about what you are doing.

If no sample is supplied, use the materials alone. Do not invent a sample or its error patterns.

## Input template

Bind these fields to the supplied conversation content. This is a context layout, not a form the teacher must fill in. Keep pages and submission parts distinct.

Use the teacher's maximum or the total from a complete points rubric; otherwise bind max_score to 100 and disclose that default. Do not ask for an omitted maximum or rescale a supplied rubric. Clarify contradictory totals.

```text
Exam title: {{exam_title}}
Max score: {{max_score}}
Locale: {{locale}}
Existing grade rubric JSON (may be empty): {{rubric}}

Teacher materials (JSON list; pages stay separate, do not concatenate):
{{materials_context}}

Sample student submission parts. Use this to understand layout, numbering, and typical work. Do not write a grade for this student.
{{student_submission}}
```
