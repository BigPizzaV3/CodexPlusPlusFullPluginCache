---
name: crisphive-book-job
description: Book a field-service job end-to-end with Crisphive — find or create the customer, check real availability windows, create the booking, quote the work, and confirm an exact appointment slot with automatic technician assignment. Use whenever the user wants to schedule, book, or arrange a service visit, repair, installation, or maintenance job for a customer.
---

# Book a field-service job with Crisphive

You are driving a deterministic scheduling engine. Follow the steps in order —
each step feeds the next. A job cannot be confirmed before it is quoted.

Every tool returns the envelope `{"error_code": 0 | "CODE", "message": "…",
"data": {…}}`. `error_code` 0 = success; otherwise it is a stable string
explaining the failure — read it before retrying.

## Environments: sandbox vs production

This skill works identically in BOTH environments — same tools, same fields,
same responses. The credential decides which one you are in:

- **Sandbox** — API key starting `chsk_test_`, or an OAuth connection the
  business owner authorized while their dashboard was in sandbox mode. All
  data is an isolated test copy: bookings here never reach a real customer
  and send no real notifications. Use it to experiment freely and to rehearse
  a flow before running it live.
- **Production** — API key starting `chsk_live_`, or an OAuth connection
  authorized from a live dashboard session. Every step below creates or
  changes REAL business data, and a confirmed booking schedules a REAL
  technician visit and notifies a REAL customer.

You cannot switch environments with a parameter; reconnect with the other
credential. **In production, recap the details and get the user's explicit
go-ahead before step 5 (`confirmJobRequest`).**

## 1. Resolve the customer

- Search first: `listCustomers` with the `q` filter (matches name, phone,
  email). Reuse the existing customer's `id` if found.
- Otherwise `createCustomer`. **Include the street address AND
  `address.latitude`/`address.longitude`** — the engine needs coordinates to
  compute travel times and match service areas; an address string alone is
  stored but NOT geocoded server-side. Use coordinates you know with
  confidence for the stated address, or confirm the location with the user.
  Pass an `idempotency_key` so a retried create never duplicates.

## 2. Check real availability windows

- `listJobRequestBookingWindows` with `x_timezone` = the CUSTOMER's IANA
  timezone (e.g. `America/Toronto`). Never invent windows.
- The response is a grid of days × periods (`morning` / `afternoon` /
  `evening`). These are *preference windows*, not exact appointment times.
- Offer the user only windows present in the response.

## 3. Create the booking

- `createJobRequest` with `customer_id` and `job_dates` — an array of
  `{date: "YYYY-MM-DD", periods: [{period: "morning"}]}` picked in step 2.
- Optional: `job_type_id` (discover via `listJobTypes`), `skill_ids`
  (discover via `listSkills`) when the user described the kind of work, and
  `description` (free text). Pass an `idempotency_key`.
- Do not set `priority` unless the job is genuinely urgent (see the
  crisphive-emergency-dispatch skill); omitted bookings get the business's
  default priority.

## 4. Quote the work

- `quoteJobRequest` with `job_duration_minutes` (on-site work time) plus
  `mobilization_minutes` / `demobilization_minutes` (travel/setup before and
  after). If the user gave no durations, propose sensible ones and confirm
  with the user before quoting.
- Quotes are time bundles only — Crisphive job requests carry NO prices,
  amounts, or currency. Never invent monetary fields.

## 5. Confirm an exact slot

- The confirm API needs an exact start time, not a window. Fetch the exact
  bookable start times with `listMatchingSlots` (optional `step_minutes`,
  default 30), then call `confirmJobRequest` with:
  - `scheduled_at` — the chosen slot's business-local naive datetime
    (`2026-08-04T09:00:00`, NO timezone offset — take the
    `business_time.datetime` value from the slot response verbatim).
  - `status_version` — echo the value from your last `getJobRequest` read to
    fence against concurrent edits (optional but recommended).
  - `technician_id` — ONLY when the user explicitly demands a specific
    person; otherwise omit it and the matching engine auto-assigns the best
    technician by skills, travel time, and availability.
- Pass an `idempotency_key`.

## 6. Verify and report

- Read back with `getJobRequest` / `getJobRequestTimeline`: assigned
  technician, arrival window, scheduled start/end, and the next workflow
  action. Summarize these for the user.

## Recovering from errors

- `JOB_REQUEST_NO_TECHNICIAN_AVAILABLE` on confirm: that exact time has no
  feasible technician. Re-run `listMatchingSlots` and offer the nearest
  alternatives — do not retry the same time.
- Empty booking windows / empty slots: the business may have no technicians
  with availability in that service area. Say so instead of inventing times.
- `JOB_REQUEST_STAGE_CONFLICT` (409): someone changed the job concurrently —
  re-read with `getJobRequest` and redo the step with the fresh
  `status_version`.
- `IDEMPOTENCY_KEY_REUSE` (422): you reused a key with a different body —
  generate a fresh key.

