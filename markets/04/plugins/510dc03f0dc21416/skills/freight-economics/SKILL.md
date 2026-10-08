---
name: freight-economics
description: Evaluate whether a specific freight load offer makes economic sense for an owner-operator or carrier using the carrier's own weekly operating costs, loaded miles, deadhead, break-even, and target economics.
---

Use this skill when a user asks whether a specific freight offer is economically attractive, whether they should accept/counter/pass based on operating economics, or what gross rate would be needed to meet their target.

## Required workflow

1. Gather the values required by `evaluate_load_offer`:
   - offered pay
   - loaded miles
   - deadhead miles
   - weekly fixed operating costs
   - variable operating cost per mile
   - projected total weekly miles
   - expected loaded weekly miles
   - desired weekly driver pay
   - desired weekly reserve/profit

2. Never invent carrier-specific costs. If required values are missing, ask only for the missing values. If the user explicitly requests an example or rough scenario, clearly label assumptions before calling the tool.

3. Call `evaluate_load_offer` when the required inputs are available.

4. Treat the tool response as the canonical economic calculation. Do not recompute the verdict using a different RPM definition.

5. Explain results in this order:
   - ACCEPT / COUNTER / PASS
   - offered loaded RPM
   - offered all-mile RPM
   - all-mile break-even RPM
   - all-mile target RPM
   - target gross for the evaluated miles when useful
   - margin/contribution over break-even
   - deadhead share
   - short reason for the verdict

## Canonical semantic distinction

- `target_loaded_rpm` is a weekly revenue-mile planning metric.
- It does NOT control the verdict for a specific offered load.
- A specific offered load is evaluated using offered all-mile RPM against all-mile break-even RPM and target all-mile RPM.

## Hard boundaries

RigReceipts V0 is economic decision support only.

Do not claim or imply that it:
- searches load boards or finds freight;
- contacts brokers, shippers, carriers, or facilities;
- negotiates, bids, books, accepts, rejects, tenders, or dispatches freight;
- verifies hours-of-service, route legality, equipment suitability, insurance, safety, regulatory compliance, contract terms, or counterparty/payment reliability;
- guarantees profit or actual trip outcome;
- reads private RigReceipts account records in anonymous V0;
- persists the user's offer or operating-cost inputs.

For unsupported operational/transactional requests, state the boundary briefly and offer to evaluate the economics of a user-supplied load when useful.

## Output discipline

Use the dollar/RPM values returned by the tool. State that the result depends on user-supplied operating assumptions. Do not describe margin over break-even as guaranteed net profit.

If the tool returns input validation failure, request correction of the invalid input instead of fabricating an answer.
