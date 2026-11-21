---
name: train-status
description: Check the reported running status of an Indian train for a given origin departure date, such as delay and last known location. Use when the user asks where a train is, whether it is late, or how it is running.
---

# Train running status

1. Make sure you have a train number. If the user gave a name, resolve it first with `search_trains` and confirm the match.
2. Ask for, or infer from context, the date the train departed from its origin (YYYY-MM-DD, Asia/Kolkata). Today's date is fine only if the user means a train that left its origin today.
3. Call `get_train_running_status` with the train number and `origin_departure_date`.
4. Summarise the current position, delay and next stops. Starred times are estimates; say so.

Important:
- The tool reads RailJournal's existing website cache and does not start a live refresh. A cache miss returns an error. Tell the user the status is not available right now and suggest trying again shortly. Do not retry in a loop and do not invent a status.
- Retrieval time is not observation time. Mention when the data was retrieved.
- Include the source link from the result.
