---
name: energy-advice
description: Explain the existing clever-PV optimisation and estimate when charging or shifting consumption is cheap, based on the user's stated constraints and clever-PV prices and forecasts, without changing anything. Use when the user asks when to charge a car or battery cheaply, or whether shifting consumption saves money.
---

Use the connected clever-PV MCP tools and their current schemas. Respond in the user's language. Advice is read-only: never call a `set_*` tool as part of advice.

- Explain the existing optimisation first with `get_automation_settings`, and for a vehicle or wallbox with `get_device` (for example its `target-charging` capability). If target or smart charging is active, say that clever-PV plans charging itself and your estimate is only a comparison. If the device data does not show it, say that it cannot be determined; do not treat a missing value as "not active".
- For a charging window, get the energy to charge (kWh), the time charging must be finished and the charging power (kW) from the user. Do not derive them from device data, typical values or earlier conversations unless the user confirms them. Ask for exactly the values that are missing.
- Use `get_energy_prices` (ct/kWh, UTC timestamps) for the period until the deadline and, for PV surplus, `get_energy_forecast` or `get_solar_forecast`. Only use prices that are returned; if prices do not reach the deadline, say so and suggest asking again after the next day's prices are published. Do not extrapolate prices.
- Work out the window transparently: number of quarter hours needed = ceil(4 × energy (kWh) / power (kW)) (energy / power is hours; one hour has four quarter hours); pick the cheapest returned quarter hours before the deadline, earlier ones first on equal prices. Show the chosen times in the user's time zone, the prices used and your arithmetic, so the user can check it.
- Label every cost figure as an estimate from the returned prices, and state which price components they contain (the background documentation linked in the energy-assistant skill explains prices and tariffs if the tool descriptions do not). Never present them as guaranteed savings or as the user's bill. Negative exchange prices do not mean the user is paid for charging. Forecasts are estimates, not measurements.
- A suggested window is not a setting. Changing target charging, automation or device settings needs a separate, explicit request from the user and the change flow of the energy-assistant skill.
- Use only data returned by the tools. Missing prices, forecasts or device data are limitations to report, not gaps to fill with assumptions.
