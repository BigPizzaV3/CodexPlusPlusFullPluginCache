---
name: get-started
description: How to use livedot to find running and cycling clubs and coaches near you, follow someone in a live race, a charity team's live map and where to give, adventure routes and trips, race-day weather, help, and (signed in) Garmin LiveTrack, charity teams and events.
---
# Using livedot

livedot: live race tracking and route weather for runners and cyclists (Windline for cycling, RunFast for running). Each answer has a card; don't restate the whole card.


- **Follow someone live:** "Where's Megan in the Comrades?" uses find_person, then where_is. How a race or a club is doing: event_status or club_in_race. If several people share the name, show the likeliest few and ask one short question; never guess.
- **Race-day weather:** "What will the weather be like for the NYC Marathon?" uses event_weather. It gives the live forecast within 10 days and 10 years of history beyond; always say which.
- **Fly a course:** "Fly the Comrades" uses fly_route.
- **Cycling tours:** "What's the ProLend 2027 Durban Tour route?" uses tour_route. Route files appear only when the organiser shares them. tour_notes gives the organiser's own words.
- **A route the user shares:** when they attach a GPX file (pass it as gpx_file), give a route link or a route's points, and ask about the weather, wind, heat, a flyover or a video, call plan_route with their start time. If you can read the file yourself, you may pass its text as gpx or its points as points. Never treat a file name as an event name: event_weather is only for named events and races. No sign-in.
- **Find a club:** find_clubs ("best running club to join in Fourways") and find_events ("cycle tours around Johannesburg") list clubs and public events near a place, with Join or I'm in to their page. No sign-in.
- **Find a coach:** find_coaches ("personal cycling trainer in Joburg", "running coach near Sandton") lists coaches and training groups near a place, with Book / contact and their page. Qualifications are the coach's own words; never call a coach verified or certified. No sign-in.
- **Race day (signed in, for the person themselves):** garmin_livetrack gives their own livedot LiveTrack address, the set-up steps from the help article and when the last LiveTrack link came in (a data field link code only when they ask for the data field, with field: true); add_my_race joins the race they're doing (the race already on livedot, never a copy; several matches: ask which; only if none, their own private race from the GPX, date and start); add_my_tour makes their multi-day tour, a day per stage; my_live_plan says what's armed. Races and tours are events: never call them Ride live or Run live.
- **Charities (livedot for Good):** find_charity_events lists verified charities' rides, runs and walks; charity_team_map shows a team live (a tap on the back for a fundraiser goes through tap_on_the_back with charity and fundraiser); support_links gives the charity's and each fundraiser's own donation pages: links only, livedot never handles money. The demo charity, Brightpath Children's Trust (its Coast Ride always live), is labelled a demo and nobody joins it. Signed in: add_charity_event (a preview, then confirm: true), my_charity_team (reminders only on a yes), join_charity_team, set_my_cause.
- **Adventures and help:** find_adventure_routes (known trekking routes: weather by month, day splits, sourced permit and guide rules), trip_status (a trip's live status; a tap on the back is counted only, never sent to an inReach or SPOT), help_guides (answers from the apps' own help articles, with the link).
- **Organisers (signed in):** list_my_events, create_event (always a draft), update_event (never a finished event), add_tour_notes, post_club_ride and publish_event (only after the user confirms).
- Use the user's units: miles and °F for US users, km and °C otherwise.
