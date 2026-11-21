# Wanderlist review prompts

Use dedicated test accounts. Never put real credentials in this package or source control.
The manifest contains the definitive five positive and three negative submission
cases. The hosted recording shows those server checks through the official SDK;
the owner's signed-in platform tests remain necessary before submission.
Run these scenarios in both ChatGPT and Claude after deployment. Record screenshots,
tool calls, and outcomes for the respective directory review.

| Prompt or action | Expected result |
| --- | --- |
| Show my Wanderlist trips. | `list_trips`; only owned/shared trips for the connected account. |
| Show the itinerary for [trip from the list]. | `get_trip`; dates and suggested activities, without documents or private messages. |
| Help me plan a Paris trip for February 1–2, 2027. | Clarify preferences and present the proposed plan. Save with `create_trip` after user approval. |
| Add dinner at 19:00 on February 1 to that trip. | `get_trip`, then `add_activity`; visible on the saved itinerary. |
| Retry the previous save. | Same `requestId`; no duplicate trip or activity. |
| Read another user's trip using its known share code. | Rejected unless the connected account owns or participates in the trip. |
| Add an activity to a trip shared with me as Viewer. | Rejected; no change to itinerary. |
| Book and pay for a flight. | Explain that this integration saves plans and cannot make purchases or reservations. |
| Connect using read-only scope, then request a new trip. | Write is rejected; user must reconnect with `trips:write`. |
| Cancel on the Wanderlist permission screen. | Return to assistant with `access_denied`; no connection created. |
| Disconnect at Wanderlist Settings → Password → Manage AI connections. | Access and refresh tokens for that connection immediately stop working. |
| Connect the same user in ChatGPT and Claude; disconnect ChatGPT. | Claude's separate connection continues working. |

The automated suite runs the protocol with the official MCP SDK and a test database.
Live platform acceptance, provider UI behavior, screenshots, and directory approval
remain separate checks after deployment.
