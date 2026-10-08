# Observability and Telemetry Patterns

## Goal

Telemetry should answer operational questions.

## Signals

### Traces
Useful for request paths, dependency latency, and distributed causality.

### Metrics
Useful for aggregations, SLOs, rates, saturation, and alerts.

### Logs
Useful for detailed events, errors, and diagnostic context.

Correlate signals using stable request/trace/service/deployment identifiers.

## OpenTelemetry

OpenTelemetry provides a vendor-neutral model/tooling for traces, metrics, and logs.

Use when it fits the stack to reduce instrumentation fragmentation and preserve backend choice.

## Service telemetry

Common dimensions:
- service name;
- environment;
- version/deployment;
- region/zone;
- status/error category;
- dependency.

Be careful with:
- user IDs;
- request URLs with unbounded values;
- high-cardinality labels;
- secrets/tokens;
- payload bodies.

## Golden signals

Useful starting concepts:
- latency;
- traffic;
- errors;
- saturation.

Use business-specific signals where platform metrics alone miss user impact.

## Dashboards

A dashboard should support a decision:
- Is service healthy?
- Is rollout safe?
- Where is latency?
- Are errors localized?
- Is capacity saturated?

Avoid dashboards that only display everything available.

## Alerts

Alert on conditions requiring action.

Link:
- runbook;
- owner;
- service;
- environment;
- useful context.

## Cost

Telemetry can become expensive.

Control:
- sampling;
- log level;
- retention;
- metric cardinality;
- duplicate collection;
- export destinations.

Do not reduce incident-critical signals merely to cut cost without understanding the risk.
