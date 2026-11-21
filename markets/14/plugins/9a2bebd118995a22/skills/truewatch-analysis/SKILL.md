---
name: truewatch-analysis
description: Use when the user wants evidence-based analysis of TrueWatch telemetry, trends, anomalies, latency, errors, or potential incident causes.
---

# Analyze TrueWatch data

Collect evidence using the [query workflow](../truewatch-query/SKILL.md) before analyzing it.

1. Translate the question into targets, metrics, time windows, and comparison baselines. State any default to the last 30 minutes. Use consistent filters, units, and granularity across comparison windows.
2. Query overall trends and distributions first, then isolate anomalies using discovered dimensions. Correlate logs, traces, events, or topology as needed. Each additional query should address a specific uncertainty.
3. Check sample counts, missing values, sampling, data delay, pagination, and truncation. Do not average group percentiles to derive an overall percentile. State the numerator and denominator for error rates; report a zero denominator as not computable.
4. Distinguish observations, correlations, and potential causes. Do not present unverified correlations as root causes. Never invent values, trends, or conclusions when evidence is missing.
5. Respond in the user's language with a concise conclusion, key evidence, scope and limitations, and suggested verification steps. Cite only identifiers and links actually returned. Label charts with timezone, units, granularity, and baseline.

Default to read-only operations. Query and analysis requests do not authorize changes to TrueWatch. Verify the actual tool and authorization scope only when the user separately requests a write.
