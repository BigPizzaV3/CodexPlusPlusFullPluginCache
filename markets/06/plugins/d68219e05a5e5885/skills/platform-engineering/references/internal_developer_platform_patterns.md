# Internal Developer Platform Patterns

## Platform as a product

Internal developers are users of the platform.

Start with their highest-friction journeys:
- create service;
- get environment;
- deploy;
- get credentials;
- expose endpoint;
- observe service;
- request data/infrastructure;
- debug incident.

Measure whether the platform makes these faster, safer, and more consistent.

## Golden paths

A golden path is an opinionated supported route for a common task.

Good golden paths provide:
- safe defaults;
- templates;
- documentation;
- built-in security/observability;
- lifecycle ownership;
- escape hatch.

They should not prohibit every valid exception.

## Self-service

Self-service should be:
- discoverable;
- permission-aware;
- bounded;
- auditable;
- fast;
- reversible when possible.

Automating a ticket form without reducing cognitive load is not meaningful self-service.

## Platform interfaces

Possible interfaces:
- CLI;
- API;
- portal;
- templates;
- Git workflows;
- service catalog.

Choose based on user workflow, not trend.

## Scorecards

Use scorecards only when:
- criteria are meaningful;
- teams can act on them;
- ownership is clear;
- incentives do not encourage gaming.

Examples:
- owner set;
- SLO defined;
- production runbook;
- dependency metadata;
- supported runtime;
- security baseline.

## Adoption

Measure:
- time-to-first-deploy;
- developer wait time;
- change failure rate;
- platform task success;
- support volume;
- paved-road adoption;
- satisfaction.

Do not optimize raw portal page views.

## Platform boundaries

Document:
- what platform team owns;
- what product teams own;
- what is shared;
- escalation path;
- unsupported use cases.

A platform with unclear ownership becomes a new bottleneck.
