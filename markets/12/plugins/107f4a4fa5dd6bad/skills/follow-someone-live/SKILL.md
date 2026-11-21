---
name: follow-someone-live
description: "Use when someone wants to follow a friend, family member or athlete live during a race, ride or run: 'where's Megan in the Comrades?', 'how can I follow my friend running a marathon live?', 'how is our club doing in the race?'. Shows where they are now on a live map and lets the user send a tap on the back."
---
# Following someone live

- **A person:** find_person with the name, handle (@megan, livedot.me/megan) or follow link, then where_is for their live position: km, time against their goal, finish estimate and the weather where they are, on a map that updates itself.
- Only people who chose to be Findable on public races are found by name. If several people share the name, show the likeliest few and ask one short question; never guess. The tools never give a position near the start or finish, or once someone has stopped.
- **A race or a club in a race:** event_status for how a race is going; club_in_race for a club's or coach's athletes in it.
- **Cheering:** tap_on_the_back sends a tap that buzzes on their phone while they're out there. Send it only when the user asks.
- If the person isn't live on livedot, say so, and say they can share their livedot link next time (Windline for cycling, RunFast for running, or Garmin LiveTrack).
- Use the user's units: miles and °F for US users, km and °C otherwise.
