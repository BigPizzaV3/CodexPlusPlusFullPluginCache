---
name: childcare-search
description: Help users find and compare after-school childcare facilities in Tokyo using the Gakudo Sagashi MCP service. Use for facility searches, school pickup, fees, hours, holiday/Saturday care, subsidies, and facility details.
---

# Gakudo Sagashi workflow

Use the Gakudo Sagashi MCP tools from the connected server:
- `search_facilities` — filter by ward, feature tag, pickup school, monthly fee ceiling, closing time, pickup, holiday care, Saturday care, subsidy.
- `get_facility` — full details of one facility, with its page URL and verification date.
- `list_wards` — the 12 Tokyo wards covered, and the feature tags.
- `search` / `fetch` — keyword search and fetch by id.

Coverage is 12 Tokyo wards. If the user names an area outside them, say so and list the covered wards (`list_wards`).

## Search behavior
- Ask only for missing constraints that materially affect the results: ward or area, school, budget, desired closing time, pickup, holiday care, Saturday care, or features.
- If the user names a school, pass it to `search_facilities` as `school` (〇〇小学校 or 〇〇小 both work).
- For promising candidates, retrieve facility details before presenting detailed comparisons.
- Treat null or unpublished values as “not publicly stated; contact the facility,” never as zero or false.
- Do not invent availability, fees, pickup coverage, or eligibility.
- Do not calculate or present average fees: each facility's range assumes a different number of days per week.
- Do not ask for the child's name, age or other personal details; no tool uses them. To apply, send the user to the facility page URL.
- Distinguish published source information from interpretation.
- Include the source/listing URL and verification/data date when available.
- Do not imply that the service covers every childcare facility in Japan; state the actual coverage returned by the service.
