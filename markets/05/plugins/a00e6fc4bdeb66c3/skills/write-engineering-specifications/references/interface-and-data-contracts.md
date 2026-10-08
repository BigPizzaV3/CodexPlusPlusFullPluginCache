# Interface and Data Contracts

## API or service contract

Define for each operation:

- stable operation ID and purpose;
- protocol, method/topic, path, version, and ownership;
- authentication, authorization, scopes, and tenant boundary;
- request headers, parameters, body schema, units, limits, and examples;
- response schema, status codes, pagination, ordering, and examples;
- validation and error model;
- idempotency, concurrency, timeout, retry, and rate-limit behavior;
- compatibility and deprecation policy;
- logging, metrics, traces, privacy redaction, and audit requirements;
- consumer/provider contract tests.

Examples must conform to the schema and must not contain real secrets or personal data.

## Event or asynchronous contract

Define event name, producer, consumers, schema version, ordering, delivery semantics, deduplication key, correlation ID, retry/dead-letter behavior, retention, replay, privacy, and compatibility.

## Data model

For each entity or collection define:

- owner and source of truth;
- fields, types, nullability, defaults, units, constraints, and sensitive classification;
- identifiers, uniqueness, relationships, indexes, and integrity rules;
- lifecycle, retention, deletion, archival, and audit behavior;
- read/write paths and permission model;
- expected scale and access pattern.

## Migration plan

Document baseline, target, schema/data transformation, backfill, validation, dual-read/write if needed, cutover, compatibility window, rollback, failure recovery, observability, and removal of temporary paths. Never describe a destructive migration as reversible without a tested recovery mechanism.
