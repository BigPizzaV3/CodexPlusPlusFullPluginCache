---
name: check-mataro-live
description: Check recent Mataró transport, traffic, municipal notices, weather, or air quality from the public Mataró.fm live feed. Use for current conditions and service disruptions.
---

# Check Mataró live information

Call `get_live_data` with the relevant `state_type` when the question names a topic. For a broad "what is happening now" request, call it without a type and summarize the returned categories. Include `observed_at` for time-sensitive claims. Avoid repeating source names and links in routine summaries; identify or link a source when the user asks or when needed to qualify a claim.

An empty result means no recent data is available through this tool; it does not prove normal service. Train positions are recent observations, not a punctuality guarantee. Weather values from Open-Meteo are supporting data, not official Meteocat XEMA observations. Air-quality values from CAMS through Open-Meteo are not official XVPCA station measurements. Do not infer an emergency or write a news article from a routine live state.
