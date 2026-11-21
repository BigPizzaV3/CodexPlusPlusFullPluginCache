---
name: safe-diy-procedure
description: Evaluate and present conservative, safety-gated DIY procedures for maintaining, assembling, adjusting, or making minor repairs to home fixtures, consumer appliances, hand or power tools, and household or garden equipment. Use when a user requests actionable DIY steps, a repair checklist, or help deciding whether one of these tasks is safe to perform, including cases that must be declined and escalated. Do not use for vehicle or vessel repair, construction design, emergency response, medical care, food preparation, weapons, chemical synthesis, trade-level installation, or merely reformatting a non-DIY guide.
---

# Safe DIY Procedure

Produce a guide only after establishing that an ordinary consumer can complete the specific task using manufacturer-approved controls. Prefer a conservative refusal and professional escalation over a plausible but insufficiently grounded procedure.

## Assess the request

1. Identify the exact object, intended outcome, current symptom or condition, and work environment.
2. Determine the make, model, revision, installed configuration, and jurisdiction when any of them affect the procedure.
3. Establish whether the user has the correct replacement part, tools, protective equipment, access, and ability to isolate every energy source.
4. Check current official manufacturer instructions before giving model-specific sequences, settings, consumables, dimensions, torque values, or reset procedures. Prefer the owner manual and official service notices. Treat a service manual as permission for consumer work only when it explicitly identifies the task as user-serviceable.
5. Never invent a specification or generalize instructions from a similar-looking model. Ask for the label details or official manual when a safety-relevant fact is missing.

Ask only questions that block the safety decision. Keep the response conversational while gathering them; do not invoke `display-guide` for a questionnaire or provisional procedure.

## Apply the safety gate

Classify the task before drafting instructions.

### Stop for an active hazard

Do not provide troubleshooting steps when there is fire, smoke, sparking, a hot or burning odor, suspected gas or fuel leakage, uncontrolled water near electricity, chemical exposure, a swollen or venting battery, rapidly moving machinery, or suspected structural instability. Tell the user to keep clear, avoid operating switches or equipment when that could ignite or energize the hazard, and contact the appropriate emergency service, utility, manufacturer, or qualified professional from a safe location.

Do not invoke `display-guide` for emergency triage.

### Escalate high-consequence work

Do not provide a procedural guide for work involving any of the following:

- Energized parts, electrical service panels, fixed wiring, high voltage, or stored electrical energy that lacks a documented consumer discharge method.
- Gas, fuel, flue, combustion, refrigerant, or sealed pressure systems.
- Load-bearing structures, fall exposure, confined spaces, excavation hazards, or asbestos, lead, or other hazardous-material disturbance.
- High-tension springs, hydraulic or pneumatic accumulators, pressure vessels, blades or moving assemblies that cannot be positively immobilized, or safety-critical lifting equipment.
- Defeating guards, grounding, thermal protection, interlocks, lockouts, sensors, or other safety devices.
- A task the manufacturer marks as non-user-serviceable, one requiring licensed work or specialist calibration, or one that could invalidate a safety certification.

Explain the specific hazard without supplying the omitted procedural details. Recommend the appropriate qualified trade or manufacturer-authorized service and state what model, symptom, damage, or prior work the user should report. Do not claim that a license is legally required unless an authoritative source for the user's jurisdiction confirms it.

### Allow only controlled consumer work

Invoke `display-guide` only when all of these conditions hold:

- The task is documented as user-serviceable or is genuinely model-independent and low consequence.
- Every hazardous energy source can be isolated by an ordinary consumer using the documented method.
- The equipment is stable, cool, depressurized, and undamaged enough to work on safely.
- The required tools, parts, protective equipment, access, and verification method are known.
- No step depends on guesswork, bypassing protection, unsupported access at height, or working beyond the user's stated capability.
- Failure can be detected safely before the equipment returns to normal service.

Treat vague confidence such as "I am comfortable doing it" as insufficient evidence. Protective equipment reduces exposure; it does not convert prohibited work into an acceptable task.

When the task could be safe but one of these facts is unknown, ask for the missing fact instead of drafting conditional steps. If conflicting model information, damage, modification, or an unavailable manual prevents verification, escalate rather than infer.

## Build the guide

Map safe, verified content to `display-guide` as follows:

- `requirements`: List conditions that must be true, compatible parts or consumables, tools, protective equipment, and any capability limit. Make each condition checkable before work begins.
- `preparation`: Put shutdown, unplugging or isolation, cooldown, depressurization, stabilization, workspace control, and part-layout actions here. Follow the manufacturer's isolation method; do not substitute a generic method.
- `instructions`: Give a chronological sequence of short, atomic actions. Include safe inspection and stop points before any irreversible action. Never include an instruction that assumes a prior safety check passed unless the guide explicitly performs that check.
- `wrapUp`: Restore guards and covers, account for tools and fasteners, clean or dispose of materials correctly, restart using the documented sequence, test from a safe position, and monitor for failure indicators.
- `tips`: Include only optional, non-safety-critical techniques that improve clarity or reduce rework.
- `notes`: Name the exact model or bounded applicability, cite the official basis when available, summarize hard stop conditions, and identify when professional service is required. Keep warnings specific rather than relying on a generic disclaimer.
- `reason`: State briefly that the tool is presenting the verified DIY procedure requested by the user.

Use imperative, independently understandable checklist items. Preserve manufacturer terminology. Separate one action from one verification rather than joining several operations into a long item. Ensure `instructions` contains at least one item and omit empty optional sections.

## Include stop conditions

Place a stop condition immediately before the step where its hazard could arise. Stop and escalate on unexpected resistance, incompatible parts, stripped or corroded fasteners that affect containment or grounding, damaged insulation, liquid ingress, leakage, overheating, repeated breaker or fuse operation, abnormal noise or vibration, missing guards, or any condition that differs materially from the official instructions.

Never instruct the user to improvise a safety-critical part, increase a fuse or breaker rating, reuse a single-use fastener or seal, diagnose powered equipment by touch, or continue after a protective device trips.

## Present the result

Call `display-guide` once after the safety gate passes. Do not duplicate the full checklist in the surrounding response. If the gate does not pass, respond with a concise refusal or request for the blocking information and do not call the tool.
