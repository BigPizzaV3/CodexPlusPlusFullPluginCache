---
name: shape-setup
description: Set up Shape after installing it: check which devices are connected to the user's Shape account, connect a Garmin or Wahoo from the chat with a one-time link, point Apple Health users to the iPhone app, and explain what happens next. Use right after install, when a Shape tool says nothing is synced or no device is connected, or when the user asks to connect, add or check a watch.
---

# Set up Shape

Use the connected Shape tools. Do not request API tokens. The goal of this
workflow is one thing: the user's device is connected to Shape, and they know
what to ask next.

## Check what is connected

- Call `connect_device` with no `provider`. It returns every device option
  with `connected`, and a link for each that is not connected yet.
- If one or more devices are already connected, say so and skip to
  "What to ask next". Do not offer links for devices that are connected.

## Connect a device

- If the user has named their device, call `connect_device` with that
  `provider` (`garmin`, `wahoo` or `apple_health`). Otherwise show the
  options from the first call and ask which they use.
- For Garmin and Wahoo, give the user the `url` exactly as returned. It is a
  personal one-time link that works in any browser for 15 minutes and needs no
  Shape sign-in. Tell them to open it, sign in to their device account, allow
  Shape, and come back to this chat.
- For Apple Health, give the App Store link and say that Health connects from
  the Shape iPhone app: install it, sign in with the same account, and allow
  Health access when asked.
- After they come back, call `connect_device` again with the same `provider`
  to confirm `connected: true`. If a link expired or was used, call the tool
  again for a fresh one; never reuse an old link.

## What happens after a connect

- The last 30 days import right away; older history follows over the next
  hours. Say this plainly so the user does not expect years of data at once.
- If a Shape tool answers that the account has no active plan, relay that
  message as it is. It names where plans are described. Do not add prices,
  promotions or a trial pitch, and do not present it as an error in the
  connection.

## What to ask next

Once a device is connected, suggest one or two first questions that work
with a fresh import, for example "How did my training look over the last
two weeks?" or "Am I ready to train hard today?". Keep it to the data that
exists; readiness needs about two weeks of sleep and heart-rate readings.
