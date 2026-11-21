---
name: control-smart-home
description: Discover, inspect, and control devices connected to the user's EVOLVIOT account. Use when the user asks about an EVOLVIOT device, room, device status, switch, fan, light, dimming level, or smart-home command.
---

# Control an EVOLVIOT smart home

Use `list_devices` before a control operation whenever the exact device ID or
control key is not already established in the current conversation.

Match the user's room and device wording against device names and supported
control-key metadata returned by EVOLVIOT. Never invent a device ID, control
key, range, or enumerated value.

Before calling `control_device`, briefly state the concrete device, control,
and value that will be changed. If more than one device is a plausible match,
ask the user which one they mean.

Use values supported by the returned control metadata:

- Translate “on” and “off” to `ON` and `OFF`.
- Send a numeric percentage only when the control supports that range.
- Use exact enumerated values for list-based controls.

After a control call, report whether the device acknowledged the command. Do
not claim success when EVOLVIOT reports a timeout, validation error, offline
device, or unavailable control.
