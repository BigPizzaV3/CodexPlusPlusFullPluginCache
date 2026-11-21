---
name: decision-matrix
description: Rank explicit alternatives using weighted benefit or cost criteria, inspect ties and pairwise weight sensitivity, and export a decision comparison CSV.
---
Call calculate_decision_matrix when the user supplies criterion weights and alternative scores. Scores must use the same fixed zero-to-one-hundred scale; do not pass raw costs or mixed units. A benefit favors higher scores; a cost favors lower scores. Pass score arrays in criterion order. Do not invent ratings, research facts or infer preferences. Report normalized weights, leading options and ties. Pairwise break-even shares hold other weights proportional and do not guarantee an overall winner switch. The widget changes weights and exports the comparison. CSV links expire in about one hour.
