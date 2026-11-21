---
name: energy-diagnosis
description: Explain why a clever-PV automation, battery control or device does not behave as expected, using only data the tools return. Use for "why doesn't my battery ...", "why is smart price control not working", "what blocks ..." and similar root-cause questions about the user's clever-PV installation.
---

Use the connected clever-PV MCP tools and their current schemas. Respond in the user's language. Follow the energy-assistant skill for units, time zones, device IDs and write safety.

Classify every statement you make as one of three kinds and label it in the answer:

- **Observation**: a value a tool returned (current setting, current intervention, device state, measured energy) with its time.
- **Proven cause**: a current blocker the tools report directly, such as an intervention on the setting in question, `applicable: false`, or a device that is offline or lacks the needed capability.
- **Hypothesis**: a plausible explanation the data does not prove. Say what data would confirm or refute it.

Procedure:

1. Pin down the device, the setting and the time of the question. Ask if the device or time is ambiguous.
2. Read `get_automation_settings`. Interventions and `applicable` describe the moment of the call: they are the cause of a blocker now. The tool description lists each intervention id and how to resolve it. For an intervention or capability it does not explain, use the background documentation links in the energy-assistant skill; the documentation explains what a blocker means in general, not that it applied to this user.
3. Read `get_devices` and `get_device` for the affected device: state, capabilities and their values.
4. For what actually happened, use `get_energy_data` for the time in question (daily view for one day, UTC timestamps; convert to local time). This shows measured flows (charge, discharge, grid), not why they happened.
5. For price-driven behaviour, compare with `get_energy_prices` for the same period; any link between prices and behaviour is a hypothesis.

Past events:

- The clever-PV tools of this connection return no history of control decisions, interventions or settings changes. For a question about an earlier time, say that the reason cannot be retrieved through this connection (not that clever-PV has no record of it), show what the measured data proves, and give current blockers only as a hypothesis for the past.
- Never turn missing history into "nothing happened" or "it was blocked". Without evidence for the time in question, do not state a cause as fact; use wording like "a likely reason is", followed by how to check it.

Do not:

- Do not present current interventions, forecasts or prices as proof of a past event.
- Do not invent decision reasons, error messages or manufacturer responses; the tools do not return them.
- Do not change settings as part of a diagnosis. Offer a concrete change separately and follow the energy-assistant write rules if the user asks for it.
- Do not ask the user for passwords, tokens or other customers' data, and do not suggest other connections or direct API calls to get more data.
