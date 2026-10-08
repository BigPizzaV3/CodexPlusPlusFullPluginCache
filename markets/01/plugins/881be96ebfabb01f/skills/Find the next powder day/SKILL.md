---
name: "Find the next powder day"
description: "Find the best upcoming powder day within driving distance and show the route."
---

When the user asks where and when to catch fresh snow ("powder"), call
`find_powder_days` with their starting city and preferred maximum driving time.
Pick the best date/resort combination (most fresh snow, reasonable drive) and call
`get_route` for it so the user sees the route. Summarize: date, resort, expected
snowfall in cm, drive time.
