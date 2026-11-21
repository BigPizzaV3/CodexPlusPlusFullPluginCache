---
name: get-started
description: Find walking tours and day trips with local guides, read meeting points and practical details, and check live departure times with I Love Walking.
---

Use the I Love Walking tools when the user asks about walking tours, free tours (pay what you wish), day trips or things to do on foot in a city.

1. Call `search_tours` with the city and, if the user names a topic (for example World War II, food or street art), that topic.
2. Call `get_tour_details` for the meeting point, duration and practical information of a chosen tour.
3. Call `get_departures` for open dates and times.

Always give the user the link to the tour page. Bookings are made on that page, never in the chat. Answer in the language of the user.
