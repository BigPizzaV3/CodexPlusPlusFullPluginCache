---
name: connect-gyroscope
description: Use when someone asks about their Gyroscope data or asks to log something, but no Gyroscope tools are available in this chat, or when they ask how to connect Gyroscope, what it can access, or why a category is missing.
---

# Connecting Gyroscope

Gyroscope works only with a connected Gyroscope account. Every answer about
their food, sleep, workouts, weight or places comes from the Gyroscope tools,
and every log goes through them. Without those tools there is no data to
answer from and nothing to log into.

## When the Gyroscope tools are not available

- Say plainly that Gyroscope is not connected in this chat yet, and help them
  connect it. Never answer from guesses, never invent numbers, and never say
  something was logged.
- Connecting starts from the Gyroscope plugin in ChatGPT. It opens a sign-in on
  gyrosco.pe, so ChatGPT never sees their password. They then choose what to
  share and approve it.
- Anyone without a Gyroscope account can create one at gyrosco.pe or in the
  Gyroscope app, then connect.
- Once connected, offer to pick up the request they started with.

## What a connection includes

- Included: food and nutrition, sleep, steps, workouts and lifts, fitness
  test and brain game results, weight, heart rate and HRV, screen time
  (computer and phone, the apps they use, pickups and notifications),
  weather, and account basics such as their timezone.
- Optional, each off unless they switch it on: places and travel history,
  their mood and their journal. These are more personal, so never load them
  without their explicit permission or request.
- Logging is on by default and can be switched off for a look-only connection.
  In ChatGPT it covers what they ate and what they did: meals, drinks,
  workouts, runs, rides and lifts, and journal notes. Nothing else goes in
  through this connection, it adds nothing they did not ask to log, and it
  cannot edit or delete anything.

## When a category is missing

- A tool that answers `insufficient_scope` includes a link to their connection
  page on gyrosco.pe. Give them that link. The change applies to their next
  question, with no need to reconnect. Do not retry until they say they have
  allowed it.
- `connection_revoked` means they disconnected. They can connect again from
  the Gyroscope plugin.
- If Gyroscope says something is not included in their account, pass that on
  plainly with the link it gives.

They can review, change or end what each assistant can access at any time at
gyrosco.pe/account/connections/.
