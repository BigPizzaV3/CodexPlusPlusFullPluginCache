# Evidence labels

Use these four labels whenever you explain, investigate or prioritize. Short status answers can skip the labels but must still never present an inference as a fact.

| Label | Comes from | Example |
|---|---|---|
| **Fact** | Measured values, series and arithmetic Eskopia returned (`findings` with `kind: "fact"`, `metrics`, `hourly`, `revenue_decomposition`) | "Orders were 31 vs an average of 56 for this window on the last 4 Mondays (-44%)." |
| **Detected condition** | Eskopia's rule-based detections (`findings` with `kind: "detected_condition"`, `active_anomalies`, `related_anomalies`, insights) | "Eskopia's No orders check fired at 5 PM (critical): no orders in 3 hours when about 17 are normal." |
| **Inference** | Your reasoning over the facts and detections | "Because traffic held steady and the drop is at the final checkout step, a checkout or payment problem is the most likely explanation." |
| **Unknown** | What Eskopia can't observe (`unknowns`, `data_quality.unavailable_measurements`) or didn't have enough data for (`data_quality.insufficient_data`) | "Eskopia can't see payment gateway errors, so it can't confirm this." |

## Rules

- An inference must name the facts it rests on.
- When two explanations fit, say so and say what would tell them apart.
- If the evidence is thin (`insufficient_data`, nulls, few hours), say "Eskopia doesn't have enough data to determine that reliably."
- Never upgrade a detected condition into a cause: "Eskopia flagged an abandoned checkout spike" is a detection; "customers abandoned because shipping costs rose" is an inference Eskopia cannot support.
- Ranking ("what to look at first"): critical detected conditions, then tracking/webhook gaps, then warnings, then notable facts. Say it's your prioritization.
