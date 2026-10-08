---
name: analyze-dayalogs-results
description: Inspect, explain, and export Dayalogs survey results through the Dayalogs MCP. Use when a user asks about response counts, completed or partial responses, selected answers, assessment scores, response confidence, version comparisons, campaign outcomes, or analysis-ready exports.
---

# Analyze Dayalogs Results

Answer the user's analytical question with the right survey version, response population, and export format.

## Workflow

1. Identify the stable survey and inspect its versions. Clarify whether the user wants all versions or a concrete version when results may differ materially.
2. Use `get_survey_stats` for the overview and `list_survey_responses` for response-level inspection. Retrieve individual responses only when needed.
3. Distinguish completed responses from partial attempts. Explain the population used in every count or percentage.
4. Use `get_survey_quality` for response confidence and quality signals. Compare versions when the user is evaluating a revised instrument or control questions.
5. For assessments, report points, maximum points, percentage, pass state, and item-level results according to the survey's configured result visibility.
6. Use campaign state and events when the question concerns delivery rather than survey answers. Keep delivery and engagement metrics distinct.
7. Choose an export based on the downstream task:
   - CSV/XLSX for human inspection and common tabular analysis.
   - SAV for SPSS workflows.
   - JSON/NDJSON for structured processing.
   - Include uploaded files only when requested and use the generated manifest to map files to responses.
8. State filters, version scope, response status, and missing-data treatment alongside the result or export.

## Interpretation Rules

- Confidence is a review signal, not proof that a respondent is human or truthful.
- A confidence score of 100 means no enabled signal fired; it is not identity verification.
- Disabled quality checks do not contribute to the global score even when their raw signals remain available.
- Do not combine versions silently when wording, logic, answer options, grading, or quotas changed.
- Treat unavailable click tracking as unavailable, never as zero engagement.
- Minimize personal data in summaries and only expose contact or link context relevant to the user's question.

## Safety

- Analysis and export do not imply permission to delete responses.
- Never call `delete_survey_response` without explicit confirmation naming the target response.
- Avoid reproducing access tokens, hidden link secrets, internal grading keys, or unnecessary contact identifiers.

## Completion

Give the answer first, followed by population, version scope, method, and caveats. For exports, name the format and what it contains, including whether partials and uploaded files were included.
