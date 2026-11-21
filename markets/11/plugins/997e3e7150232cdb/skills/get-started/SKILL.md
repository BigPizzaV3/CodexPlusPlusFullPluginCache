---
name: get-started
description: Help someone see how RoboPilots' remote human operators would run their robot fleet, and send a quote request when they ask for one.
---

# Getting started with RoboPilots

RoboPilots provides trained human operators who run robots remotely (wheeled robots, drones, humanoids, robot arms
and quadrupeds) and returns every session as labeled training data.

1. Find out what the user's fleet is: the robot types, how many robots, and the work they do. Coverage (on demand,
   business hours, 24/7) and the start date are useful but optional.
2. Call `scope_remote_operations` with those choices. If the user mentioned their round-trip latency, their software
   stack (for example LeRobot, ROS 2, PX4) or the model or policy they run, pass `latency`, `stack` and `model` too.
   The card shows what control that latency leaves a pilot on their robot type (general research with sources, not a
   RoboPilots guarantee), the stacks and models people run on it, the plan that fits the fleet size and the operator
   expertise for the work; the user can change the setup in the card. Summarize it in the user's language.
3. If the user wants a quote, ask for their full name, work email, company and company size, and coverage and
   start date if they are still missing. Confirm the details with them, then call `request_quote` (with the setup they
   chose, if any). The user can also send the request from the card.

Never state prices: every plan is quoted on the fleet. Do not invent operator counts, response times or other
commitments. People who want to work as operators should apply at https://www.robopilots.ai/apply?utm_source=chatgpt&utm_medium=plugin&utm_campaign=robopilots-plugin&utm_content=skill-apply
