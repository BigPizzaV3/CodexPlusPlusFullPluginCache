---
name: get-started
description: Help a user take their first steps with RouteSurvey after connecting it. Confirms which RouteSurvey account is connected, shows their most recent surveyed routes and explains what they can ask. Use right after installation, or when the user asks how to start with RouteSurvey.
---

Use this skill to set the user up with RouteSurvey. Explicit instructions from the user take priority over this skill.

1. Call `routesurvey_account` and say in one sentence which account is connected: name, email and account type. If the call fails because the user is not signed in, ask them to connect RouteSurvey again and stop.
2. Call `routesurvey_list_routes` with `page_size` 5 and list the routes it returns by name. If there are none, say that surveys recorded in the RouteSurvey app or web console appear here once they are saved, then go to step 3 and stop after it.
3. In two or three short lines, say what the user can ask, for example:
   - whether a load of a given height, width and weight can travel one of these routes, and where it is blocked;
   - the largest load a route can take;
   - the survey photos of a route, or a photo report PDF to send to a client.
4. Offer to check the newest route against a load. Ask for the load's height, width and weight; do not assume them.

Do not change anything in the user's RouteSurvey account during setup.
