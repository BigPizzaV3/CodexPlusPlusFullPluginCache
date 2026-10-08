---
name: dispatch-handover
description: Produce a concise dispatcher-to-driver or dispatcher-to-dispatcher road-freight handover and use HaulNavi EU calculations when cost or confirmed driving-time capacity matters.
---

Create a structured operational handover from information explicitly provided in the conversation. Do not request the full chat history.

Use this order when the data exists: mission reference; pickup; delivery; cargo/handling notes; booking references; timing; vehicle/trailer; documents; route/parking notes; customer instructions; open issues; next action.

When the user provides an estimated driving duration and a driving-time balance already confirmed by the driver, tachograph, TMS, or another authoritative system, call `plan_from_confirmed_available_driving_time`. Never calculate statutory driving/rest entitlement yourself.

For current legal or regulatory questions, use authoritative official sources (for example European Commission, national transport authority, UNECE) and clearly separate those facts from the operational handover.
