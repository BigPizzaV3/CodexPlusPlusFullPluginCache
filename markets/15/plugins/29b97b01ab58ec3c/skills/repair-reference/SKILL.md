---
name: repair-reference
description: "Use when a FlatRate Pro technician requests a grounded repair labor estimate or diagnostic trouble-code reference for a described vehicle and repair."
---

# Repair reference

Provide tool-backed reference information, not an authoritative diagnosis,
manufacturer procedure, safety certification, or automatic job entry. The
user's actual request determines which lookup to run.

1. Identify whether the request is for labor time or a DTC explanation.
   Ask for the repair description or code if missing. Use only vehicle details
   the user supplies; clarify where year, make, model, or trim affects the answer.
2. For labor time, call `estimateJob` with `jobDescription` and optional
   supplied category and `vehicleInfo`. Attribute hours to the returned estimate;
   never invent times or present an estimate as an OEM labor guide.
3. For code reference, call `lookupDtc` with the code and optional supplied
   year/make/model. Distinguish the returned description, possible causes,
   common fixes, and severity from a confirmed root cause.
4. Summarize the actual result and its limitations. A code alone does not prove
   a part failed. Do not recommend replacing a component solely on that basis.
5. Do not improvise dangerous repair procedures, bypass safety systems, or
   fabricate torque specifications or high-voltage instructions. For procedural
   work, refer to the applicable manufacturer service information and qualified
   personnel rather than guessing.
6. If the service fails or returns no result, say so. Do not silently substitute
   a made-up tool result. Authentication must happen through client OAuth;
   never collect credentials, VINs, or unrelated personal data in the lookup.
7. Do not create a job, save a note, or buy parts unless the user separately
   requests a supported action with explicit details.

Examples: "Estimate front pad replacement on a 2018 Civic" activates the labor
lookup; "What does P0301 mean?" activates DTC reference; "Log my work" belongs
to the job-log workflow instead.
