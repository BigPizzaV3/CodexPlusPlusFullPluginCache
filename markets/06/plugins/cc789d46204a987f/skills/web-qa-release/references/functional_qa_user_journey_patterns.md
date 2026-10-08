# Functional QA and User Journey Patterns

## Purpose

Use this file to design focused functional tests around user-visible behavior.

# 1. Journey model

For each important flow define:
- user goal;
- preconditions;
- starting state;
- steps;
- expected outcome;
- error/recovery behavior;
- permissions;
- data changes;
- external dependencies.

Do not create browser tests around internal implementation details when user-visible behavior is available.

# 2. Critical journey template

## Journey
What the user is trying to accomplish.

## Preconditions
Account, permissions, data, environment.

## Steps
Smallest realistic sequence.

## Expected
Observable behavior.

## Failure states
Important errors, invalid inputs, dependency failures, or permissions.

## Evidence
Trace, screenshot, console, network, test output.

## Status
Pass / Fail / Needs verification.

# 3. Forms

Check:
- required vs optional;
- labels;
- validation timing;
- preserved input after errors;
- invalid formats;
- min/max values;
- duplicate submit;
- keyboard behavior;
- server-side validation.

Do not assume client validation is authoritative.

# 4. Authentication/session

When relevant test:
- signup;
- login;
- logout;
- expired session;
- protected route;
- password reset;
- verification;
- session persistence;
- role/permission changes;
- cross-tab behavior.

# 5. CRUD/state changes

For create/edit/delete verify:
- success;
- refresh/persistence;
- unauthorized user;
- duplicate action;
- optimistic UI rollback;
- destructive confirmation;
- undo/restore when applicable.

# 6. Upload/download/export

Check:
- supported type/size;
- invalid file;
- interrupted upload;
- duplicate filename;
- progress/error state;
- authorization;
- output correctness;
- renderer differences when relevant.

# 7. Search/filter/sort

Check:
- empty query;
- no results;
- special characters;
- combined filters;
- reset;
- pagination;
- stable sorting;
- stale state after navigation.

# 8. External dependencies

For payments, auth providers, maps, email, storage, etc., test:
- success;
- timeout;
- cancellation;
- dependency error;
- callback/retry;
- duplicate webhook/action when relevant.

# 9. Playwright guidance

Prefer resilient, user-facing locators such as roles/labels/test IDs over deep CSS/XPath selectors.

Keep tests isolated and deterministic.

Avoid arbitrary sleeps when an observable condition can be awaited.

# 10. Failure evidence

For failed journeys collect when useful:
- screenshot;
- trace;
- console;
- network response;
- server correlation/request ID;
- browser/device;
- build/version.

A useful failure report should help reproduce the defect, not merely state that a test failed.
