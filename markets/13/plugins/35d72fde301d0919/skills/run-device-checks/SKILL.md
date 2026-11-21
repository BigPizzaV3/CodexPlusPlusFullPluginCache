---
name: run-device-checks
description: Use when the user wants to run a device check (single or bulk) — submit IMEI/serial numbers to a service with place_bulk_order.
---

# Running device checks

Submit identifiers for one selected service with `place_bulk_order`. Successful checks spend existing account credit; failed orders are not charged. Resolve the service using `browse-services`; when selection is delegated, choose a compatible service and explain its coverage and estimated cost without demanding an exact service name. Respect the user's budget and client permission controls.

## Prepare identifiers

1. Treat all identifiers as text; preserve leading zeros and the original spelling/order.
2. Trim surrounding whitespace and discard blank entries.
3. Dedupe within the current request/service: match IMEIs exactly, serial numbers case-insensitively. Previous orders do not block an intentional new check; different services may each check the same device.
4. Flag unreadable or clearly incompatible entries before ordering. Do not repair, guess, or substitute identifiers.

## Submit

- `serviceId`: from `list_services`.
- `batchName`: descriptive; preserve a user-provided name. Group by service (and brand when requested).
- `imeis`: the extracted identifier strings (never file paths).
- `notify`: `false` unless the user requests notifications.

Explain the chosen service, its coverage, the unique input count, and estimated cost using current prices. Do not invent a currency or final charge. Respect budgets and consent controls.

## Interpret the response

The response reports `submittedCount`, `duplicatesRemoved`, `uniqueCount`, `acceptedCount`, `rejectedCount`, and `rejectedInputs` (each with a reason). For small batches it may also include the created `orders`.

- Report acceptance separately from completion. Use `acceptedCount` for created orders — never describe `uniqueCount`/`submittedCount` as the number of devices checked.
- Failed orders are not charged; accepted orders are charged only on success.
- Read errors inside the payload even when the outer envelope looks successful.

## Reconciliation and retries

- If inputs are missing, report the discrepancy and evidence; do not invent rejection reasons or retry blindly.
- On a timeout or uncertain paid submission, reconcile by batch ID, name, time, and identifiers. There is no verified retry guarantee — never repeat the paid call blindly or assume no charge from a missing response.

## After submitting

Give a brief acknowledgment and available progress totals for large batches. Check progress with `list_orders`/`list_batches`. Do not promise future monitoring or notification unless actually enabled.

## Follow-up workflows

- Run multiple stages only when the user requests them. Advance only devices whose successful results explicitly satisfy the requested condition, such as FMI OFF. Pending, failed, rejected, missing, or unclear results do not qualify. Keep stage results separate and stop when no devices qualify.
- Choose compatible services for the requested stages; a combined service may be used when it covers the requested checks and meets the user's price criteria. Do not add other stages or checks.
- An optional service suggestion must be relevant and include its current price and added value. Suggest at most two; never treat a suggestion as permission to order. For labels, use only actual returned fields from the requested final group.
