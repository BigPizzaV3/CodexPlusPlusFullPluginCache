---
name: trip-profitability
description: Evaluate road-freight trip cost, revenue, margin, empty kilometres, waiting costs, or compare two route options using HaulNavi EU calculators.
---

Use HaulNavi EU whenever the user wants a deterministic profitability or trip-cost calculation for road freight.

Workflow:
1. Use only figures the user supplied or figures clearly obtained from a trusted source in the current task. Never invent tolls, fuel prices, route distance, ferry costs, or revenue.
2. Call `estimate_trip_cost` for one trip. Call `compare_route_costs` when the user is comparing two alternatives.
3. If empty kilometres materially affect the decision, call `calculate_empty_km_impact`.
4. If loading or delivery waiting is part of the problem, call `calculate_waiting_time_cost`.
5. Present total cost, cost/km, revenue/km and margin when available. Distinguish estimates from actual booked costs.
6. Do not imply that the cheapest route is legally or operationally feasible unless the user separately establishes that.
