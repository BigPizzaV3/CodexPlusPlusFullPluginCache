---
name: explain-cricket-score
description: Explain the score, innings, overs notation, and reported result of a specific Cricket Explorer match when the user asks what the displayed score means or wants help following it. Use model-visible match data; do not trigger for general cricket rules without a match context or for ball-by-ball analysis.
---

# Explain Cricket Score

Turn one reported match snapshot into an explanation suited to the user's familiarity with cricket.

## Inputs and retrieval

1. Resolve the requested match from returned `structuredContent.selectedMatch`, a returned match row, or the latest `widgetState.modelContent.selectedMatch`. Use only context actually visible to the model.
2. If details are needed and an ID is supplied or observed, call `open-cricket-explorer` with `reason`, `initialPanel: "matches"`, and `matchId`. Read the returned `selectedMatch`; treat a null selection as a failed detail lookup.
3. If the identity is ambiguous, open the Matches panel with `reason` and `initialPanel: "matches"`, then ask the user to select the match. Use its next model-visible selection. Never invent IDs or pass names as IDs.
4. Keep `get-cricket-data` for the widget runtime. The model-facing tool has no search, pagination, or refresh-bypass arguments.

## Explain the snapshot

1. Identify the reported match type and status. Treat `matchType: "unknown"` as unavailable. Use `matchEnded`, `matchWinner`, and the status together; flag contradictions instead of inventing an outcome.
2. Explain each relevant `scoreLines` entry using its `inning`, `runs`, `wickets`, and `overs`. Prefer these fields to the derived `summary`: missing wickets can appear as zero in that summary, so preserve a null wicket count as unknown.
3. Decode runs and wickets, then explain overs as completed overs plus legal balls. For example, `18.4` means 18 overs and four balls, not 18.4 decimal overs. Treat missing or malformed overs as unavailable.
4. Explain the reported result or current position in plain language. Use the status for targets, leads, trails, and victory margins; totals alone may omit innings, revised targets, or other match conditions.
5. If the user requests a run rate, calculate it only from a valid runs value and unambiguous six-ball overs notation: convert whole overs and zero through five extra balls into legal balls, then divide runs by balls divided by six. Label the result as a calculation from this snapshot. Leave the rate unresolved for zero balls or unsupported notation.
6. Keep tactical explanations, player performances, partnerships, remaining-ball calculations, and causes of a result outside the evidence unless the user supplies supporting information.

## Deliverable

Lead with the reported result or position, explain the score notation, and connect it to what the user can understand from this snapshot. Scale detail to their question; use an innings table when several innings need comparison. Mark missing or conflicting values explicitly.

Describe data as reported by CricketData and potentially cached for up to 24 hours. A response timestamp records the tool response, not the upstream score's observation time. Reopening a match does not establish a fresh live score. If no usable score is returned, explain the available status and identify the missing score data.
