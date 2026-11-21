---
name: get-started
description: Getting started with IMEILookup — connect the account, see what device checks are available, and route to the right workflow skill. Use when the user is new, asks what you can do, or hasn't specified a task yet.
---

# Getting started with IMEILookup

IMEILookup runs paid device checks by IMEI or serial number against the connected account's credit. Every tool is authenticated with the user's OAuth-connected IMEILookup account — never ask for or handle passwords, tokens, or secrets.

## Available tools

| Tool | Purpose |
|------|---------|
| `list_services` | Browse available checks (GSMA Blocklist, FMI, MDM, and more) with IDs, prices, and sample output |
| `place_bulk_order` | Submit one or more IMEI/serial numbers for a chosen service |
| `list_orders` | List past orders with filters and pagination |
| `get_order` | Fetch one order's full result by ID |
| `list_batches` | List batches of orders |
| `export_batch` | Export a batch's results to CSV |
| `get_user_credit` | Check the current credit balance |
| `get_user_details` | Check account profile and balance |

## Sign in

The first time a tool is called, ChatGPT prompts the user to connect their IMEILookup account via OAuth. The session token is forwarded automatically on every tool call.

## Workflow routing

For a specific task, load the matching skill instead of re-reading everything here:

- Choosing or comparing a service → `browse-services`
- Placing a check / order → `run-device-checks`
- Tracking orders or batches → `track-orders`
- Exporting to CSV → `export-results`
- Credit / account details → `manage-account`
- Reading files or making labels → `files-and-labels`

## Guardrails

- Resolve the requested check and a compatible service before placing an order. When the user delegates selection, choose from the live catalogue and explain the coverage and estimated cost; an exact service name is not required. Ask only if the requested outcome or compatibility remains unclear, and respect client permission controls.
- Duplicate identifiers in a bulk submission are removed automatically.
- Failed orders are not charged; accepted orders are charged only on success.
