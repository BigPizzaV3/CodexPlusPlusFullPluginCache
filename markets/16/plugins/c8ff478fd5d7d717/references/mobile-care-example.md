# Synthetic mobile-care worked example

This example illustrates a practice adding mobile wound-care capacity. Every numerical input is invented for demonstration. It is not a client forecast, reimbursement schedule, clinical protocol, or evidence of patient demand. Use clinician-established care patterns and locally validated costs for a real study.

Read the [synthetic input](../skills/model-healthcare-finances/assets/synthetic-mobile-care.json) with the [financial skill](../skills/model-healthcare-finances/SKILL.md). Execute it in a new user workspace directory when supported. It models two mutually exclusive encounter profiles, 40–60 available provider hours monthly, travel/documentation embedded in encounter minutes, per-visit contractor costs, and a small increase in fixed costs after month 6. Collection timing splits equally between one and two months after the service.

It deliberately makes later demand exceed capacity. Report both unserved demand and delivered activity rather than billing every desired visit. Compare narrower geography or clustered facility days by changing travel minutes and costs together. More reach can increase potential demand while reducing delivered visits.

For a standalone alternative, explicitly add the organization, administrative staffing, systems, insurance, and other costs actually needed. Changing the `mode` label alone does not change costs. For a salaried-clinician alternative, remove the same compensation from per-visit costs before adding it to fixed payroll.

Potential downstream clinic work belongs in a separate supported scenario with its own costs, payer assumptions, capacity, and clinical appropriateness. Do not assume it rescues a weak direct service. Product purchasing, waste, and delayed claim recovery can dominate cash needs; this example does not model a graft-product business or recommend skin-substitute use.

The useful decision is which operational or payment assumption needs validation before expansion, not whether this synthetic example appears profitable.
