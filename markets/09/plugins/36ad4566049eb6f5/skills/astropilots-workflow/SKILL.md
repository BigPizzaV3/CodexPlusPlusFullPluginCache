---
name: astropilots-workflow
description: Use AstroPilots for astrology readings and chart-based follow-up questions. Invoke the appropriate AstroPilots MCP tool when the user asks for a reading, chart, what is going on in their life, or a follow-up about timing, relationships, work, money, or another chart topic.
---

# AstroPilots workflow

Use the connected AstroPilots MCP server for astrology-specific requests rather than attempting to calculate or invent chart data locally.

## Tool routing

- Use `get_reading` when the user asks for an astrology reading, birth chart/chart reading, or asks broadly what is going on in their life according to astrology.
- `get_reading` should use the user's saved birth details when available through AstroPilots. If the user supplies a date, time, and birthplace in the request, use those details.
- Use `ask_astropilots` for follow-up questions about an existing chart or reading, including timing, relationships, work, money, and other chart-specific questions.
- If the user asks a follow-up that clearly depends on their prior chart, use `ask_astropilots` rather than generating a generic astrology answer.

## Birth details

Do not invent missing birth date, birth time, or birthplace. If AstroPilots cannot access saved birth details and the request requires them, ask the user for the missing information.

## Response behavior

Present AstroPilots' results clearly and distinguish chart-derived interpretations from ordinary factual statements. Do not claim a prediction is certain. If AstroPilots reports uncertainty or limitations, preserve that uncertainty.
