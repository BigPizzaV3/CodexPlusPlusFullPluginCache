---
name: setup
description: Use right after Gyroscope is installed, or when someone asks to set up Gyroscope, to check the connection, confirm what is shared and show what they can ask. Runs as the plugin's onboarding.
---

# Setting up Gyroscope

This runs once, right after the member adds Gyroscope. Keep it short and
friendly, and log nothing during setup.

## 1. Check the connection

- Call `gyroscope_status`.
- If no Gyroscope tools are available, or the connection is missing, follow the
  connect-gyroscope skill to get them connected, then continue here.

## 2. Confirm what is shared

- In two or three lines, confirm the connection works, the timezone Gyroscope
  will use for their dates, and the categories this connection can access.
- Name the optional categories that are off (places and travel, their mood
  and their journal), and say they can switch each one on at
  any time at
  gyrosco.pe/account/connections/.
- If logging is off, say that this connection can look things up but not add
  entries, and how to switch it on there.

## 3. Show it working

- Make one call to `load_day` for yesterday and give a one-line snapshot from
  whatever is there, such as what they ate, how they slept and their steps.
- If yesterday is empty, say so in one line and move on.

## 4. What to try next

- Offer three short ideas in their own context, one of each kind: logging what
  they eat or drink by just telling you, lining up two things from their
  wearables such as sleep against workouts, and a recap of the places they
  went or a trip they took.
- Then hand the conversation back to them.
