---
name: get-started
description: Help an EasyBracket organiser get started with the connector.
---

# Getting started with EasyBracket

1. Call `list_organisations` to find the organisations the user runs. If it is empty, explain that the connector is for organisation admins and that players see nothing.
2. Call `list_tournaments` and offer three useful next steps based on what is running: today's matches (`list_matches`), the table (`get_standings`) or the bracket (`get_bracket`).
3. Before changing anything (`update_tournament`, `schedule_match`, `record_result`), say what will change and wait for the user to confirm.
4. Kick-off times are local times in the organisation's time zone (`get_tournament` returns `time_zone`).
5. Refunds, fees, deleting and publishing are done in the EasyBracket app, not here. Point the user to https://easybracket.app.
