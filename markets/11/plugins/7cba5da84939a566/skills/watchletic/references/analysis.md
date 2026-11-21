# Training analysis

Begin with `get_training_context` for the requested range and timezone. Check completeness and access status before interpreting the result.

Summarize actual frequency, duration, distance, load, readiness, and scheduled work. Prefer Watchletic's deterministic analytics and selected training-load sources before making qualitative inferences. For one workout, use its compact activity summary first, followed by interval summaries when lap-level detail is needed. Do not fetch every raw sample to calculate averages that the summary tools already provide. Request selected raw channels only for a named time-series question the summaries cannot answer. A FIT export is available when a complete portable workout file is specifically useful. State uncertainty where activities are excluded, raw samples are absent, dates are sparse, or analytics are processing.

Use returned IDs to fetch one focused activity or structured workout when required. Request only the raw channels that can answer a named question, such as pace or heart-rate drift, DFA-alpha1 response, route and elevation effects, or sensor quality. Location data is precise and should be requested only when relevant.

Training analysis is informational and is not medical advice. Do not diagnose, override professional guidance, or infer unsupported health conditions.
