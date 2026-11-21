---
name: soxoa-process-discovery
description: "Interview the user about recurring manual work and turn confirmed workload facts into an automation intake before estimating value."
---

# Discover the actual process

Work from what the user supplies; this interview does not inspect staff, mailboxes or business systems. Ask a few relevant questions at a time about the trigger, input, current steps, decisions, exceptions, tools, human owner and desired output. Use a normal example and a difficult one. Keep customer names and credentials out of an intake that needs only generic workflow facts.

For each workflow, collect its name, weekly team hours, predictability, judgment required, error cost, data sensitivity and actual number of systems. Ratings use low, medium or high. Suggest a rating only as a suggestion the user can correct. If valuing it, also collect people, hours per person per week and loaded hourly cost with currency. Distinguish team hours from per-person hours, show conversions, and label rough user estimates.

Do not invent missing workload, wages, ratings, reliability or process measurements. If the user does not know timing, propose measuring an ordinary week or record a rough value they actually choose. Optional automatable share, working weeks and implementation cost remain omitted when unknown; the current Soxoa defaults are 60% and 48 weeks, while missing cost means no calculated payback.

Return a usable intake table with supplied, estimated, defaulted and missing facts distinguished. If the request already includes ranking or valuation and the required facts are available, use `prioritize_automation_workflows` or `estimate_automation_roi` at https://soxoa.com/mcp without requesting the same permission again. Ask only for a genuinely missing decision. Triage accepts one to twelve workflows. A tool failure or missing connection leaves calculations pending; never present invented tool results.

For a pilot, the collected trigger, steps, systems, review owner and success checks support `build_workflow_pilot`. Return practical next data to gather. This does not connect systems, start automation, save a server-side process inventory or schedule a follow-up. Connection help: https://soxoa.com/mcp-guide.
