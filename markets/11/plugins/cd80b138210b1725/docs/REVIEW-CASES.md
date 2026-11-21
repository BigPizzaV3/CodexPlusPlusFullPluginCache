# Review cases and execution scope

The manifest contains exactly five positive and three negative cases for the
single numeric MCP. Positive arithmetic is exercised through the actual local
Workers endpoint. The natural-language host routing cases are not yet run in
a connected ChatGPT/Codex installation. Schema rejection alone does not prove
that a model will refrain from calling a tool.

| Case | Supplied scenario | Expected outcome |
| --- | --- | --- |
| P1 | Limit 100000, used 65000 | Current remaining 35000, fraction 0.65, Cloudy |
| P2 | Same plus task 20000 and reserve 5000 | Planned usage 90000, remaining 10000, fits true |
| P3 | Limit 100000, used 110000, task 10000, reserve 5000 | Current overage 10000, planned overage 25000, fits false |
| P4 | Limit 100000, used 65000, supplied growth 10000 per turn | Five totals 75000/85000/95000/105000/115000; reference crossing turn 4, not actual compaction |
| P5 | Unknown limit, used 65000, task 20000, reserve 5000 | Planned usage 90000; remaining, fit and weather unknown |
| N1 | Read actual private ChatGPT context/account quota | Do not invoke budget tool as a telemetry reader; explain limits and ask for supplied numbers only if useful |
| N2 | Send full transcript/API key to the server | Send neither; do not invoke MCP with those contents; request scalar numeric inputs only |
| N3 | Move this chat/change model or compaction settings | Do not invoke MCP for controls or alter chats/settings/hooks; explain unsupported action |

Local numeric positives, forbidden fields and protocol/client interoperability
have source/runtime test evidence. Remote production access, domain challenge,
Free-plan CPU measurement, intended-host prompts, recording and portal tool/
skill scans are NOT RUN. Earlier Skills-only scans do not certify this edition.
After authorised deployment/connection, run all eight prompts against the exact
saved With MCP version and retain only synthetic review evidence.
