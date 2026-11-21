---
name: get-started
description: Introduce the IRM365 connection. Use when the user has just connected IRM365, asks what IRM365 can do here, or asks which company or data the connection can see.
---

# Get started with IRM365

1. Call `get_workspace_context` first. It returns the company, the signed-in person, their timezone and the data areas this connection may read.
2. Tell the user, in two or three sentences:
   - which company and person the connection acts for;
   - which areas are shared (leads and follow-ups, opportunities, activity notes);
   - that the connection is read-only and does not share the phone and email fields (free-text notes may still contain whatever people typed).
3. Offer three things they can ask next, picked from the shared areas. For example:
   - "What follow-ups do I have today?"
   - "Show my hot leads that haven't been contacted this week."
   - "Which opportunities should close this month?"

Use the timezone from `get_workspace_context` for every date you mention. If an area the user asks about isn't shared, say so and tell them their company admin or the IRM365 consent screen controls it. Don't guess at data you couldn't read.
