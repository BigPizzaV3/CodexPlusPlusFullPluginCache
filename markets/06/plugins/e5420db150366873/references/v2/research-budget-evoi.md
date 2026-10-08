
# Research Budget and Expected Value of Information

Before deep research, rank unresolved questions. Use expected decision impact, probability the research changes the present conclusion, uncertainty reduction, source accessibility, time cost, and dependency centrality.

The deterministic priority score is:

    decision_impact * change_probability * uncertainty_reduction * dependency_multiplier / max(cost_hours, 0.25)

Inputs are normalized to 0-1 except hours and the dependency multiplier, normally 1.0-2.0. Scores are priorities, not truth. Research the highest-value question first, then recompute after material discoveries. Stop or defer low-value work when it cannot change the decision, unblock a mandatory gate, or materially narrow the range. Never use this rule to omit a legally, ethically, or methodologically mandatory check.
