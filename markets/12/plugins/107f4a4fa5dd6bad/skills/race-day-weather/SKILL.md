---
name: race-day-weather
description: "Use when someone asks what the weather, wind or heat will be on race day or along a route, or wants to see a course before they ride or run it: 'weather for the NYC Marathon', 'will there be a headwind on my ride on Saturday?' with a GPX file, 'fly the Comrades course'."
---
# Race-day weather and routes

- **A named race or event:** event_weather. Within 10 days it gives the live forecast along the course at the right time of day; further out it gives 10 years of history for that date. Always say which one it is.
- **A route the user shares:** when they attach a GPX file (pass it as gpx_file), give a route link or a route's points, call plan_route with their start time for the weather, wind and heat along it and a flyover. Never treat a file name as an event name.
- **See a course:** fly_route flies a race's course on a 3D map.
- **Cycling tours:** tour_route for a tour's stages and route files (only when the organiser shares them), tour_notes for the organiser's own notes.
- No sign-in. Use the user's units: miles and °F for US users, km and °C otherwise.
