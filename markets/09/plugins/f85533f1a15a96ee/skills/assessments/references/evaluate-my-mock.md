# Evaluate My Mock

Use this workflow when a student wants MockMentor to analyze a completed mock, scorecard, OMR sheet, or other supported assessment result.

Do not use `grade_take_my_mock` for an externally completed assessment. That tool is only for an attempt created by the Take My Mock workflow.

## Collect and prepare

1. Perform the account-and-access preflight. Continue only when onboarding is complete and `evaluate_my_mock` appears in `accessibleFeatureKeys`.
2. If the student has not provided a completed mock, report, scorecard, OMR sheet, answer sheet, or typed summary, ask them to attach or paste it. Ask for the answer key or marking scheme when the supplied format cannot be evaluated without one.
3. Infer the report type, subject or paper, and any attempt or year explicitly shown or stated. Call `prepare_evaluate_my_mock` with only that classification. Do not put raw file contents, extracted scores, answers, roll numbers, registration details, centres, addresses, or other personal data in tool arguments.
4. Use the returned primary exam, language, published rules, syllabus hierarchy, verified sources, and evaluation contract as current context. A published exam pattern is not an answer key or a detailed marking rubric unless the result explicitly contains one.

## Extract and confirm

Extract only fields visible in the student's material. Prefer this structure when available:

- exam, attempt or year, mock title, subject or paper;
- score, maximum score, percentage, percentile or rank when explicitly shown;
- correct, incorrect, unanswered, attempted, and negative marks;
- section, topic, question, difficulty, and timing breakdowns; and
- applicable answer key, marking rule, or rubric.

Ignore and never repeat unnecessary personal identifiers. If an important value is unreadable, cropped, internally inconsistent, or inferred rather than printed, label it. Read back the material facts understood and ask the student to correct them before evaluating whenever ambiguity could change the score or conclusion. Do not guess.

## Evaluate at the supported evidence level

- A total score supports overall analysis only.
- Section data supports section comparisons, not topic weaknesses.
- Topic data supports topic-level strengths and gaps.
- Question-level answers plus a usable key and marking rule support question-level error analysis.
- An OMR sheet without the applicable answer key cannot establish correctness.
- A written answer without a named rubric supports qualitative feedback, not precise marks.
- Unanswered questions do not by themselves prove time pressure. Attribute time loss only when timing evidence supports it.

Apply negative marking only when the returned or student-supplied rule establishes it. Show calculations. Separate extracted facts, calculated results, and model inference. When the supplied report conflicts with current published guidance, explain the conflict rather than silently changing the student's data.

## Present the evaluation

Use the student's preferred language when practical and present:

1. **Score snapshot** — neutral facts and calculations.
2. **Evidence quality** — what level of analysis the material supports and what is missing.
3. **Strengths** — no more than three, each tied to visible evidence.
4. **Highest-impact opportunities** — no more than three, with the evidence and an actionable correction.
5. **Marks lost** — separate knowledge, method, negative-marking, unanswered, and timing losses only when supported.
6. **Next step** — one focused practice recommendation for the next seven days.

State the score without judgment. Label every recoverable-marks figure as an estimate and show its basis. End with:

> AI-generated evaluation—verify high-stakes conclusions against the official scorecard, answer key, marking scheme, or your instructor.

## Scoped syllabus context

Use returned IDs and `whyRelevant` labels to interpret the selected syllabus. `syllabusPage` describes that list only. If more context is needed, pass its `nextCursor` as `cursor` with unchanged inputs. Omit the cursor when changing topic or subject. No matches means clarify the label; it does not prove the topic is absent from the exam. Reuse the initial preflight for pagination within this workflow; each call still enforces access server-side.
