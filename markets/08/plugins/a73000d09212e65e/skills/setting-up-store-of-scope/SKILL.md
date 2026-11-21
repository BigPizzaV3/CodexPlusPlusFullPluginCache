---
name: setting-up-store-of-scope
description: Use when a user asks to set up, connect, configure, reconnect, schedule, or recover Store of Scope, including missing Gmail, Calendar, Drive, or automation capabilities.
---

# Setting up Store of Scope

## Overview

Complete one reviewable setup from dependency checks through a verified preview. Gmail is required. Calendar is optional and recommended. Drive is optional. Never ask the user to install Noodle Seed.

Read [the setup contract](references/setup-contract.md) before changing configuration or creating an automation.

## Setup order

1. Call `get_store_of_scope_status`. If the hosted MCP connection fails, stop and report the connection error; do not request Noodle credentials or attempt to bypass the configured endpoint.
2. Verify Gmail capabilities are installed, enabled, signed in, and able to perform a safe read. If absent, guide the user to install the Gmail app through the host and stop until authorization completes.
3. Request Gmail read access first. Verify send access only when delivery is enabled. Do not request delete, archive, label, trash, or read-status mutation.
4. Offer Calendar only for a managed reading event. Offer Drive only for user-owned cloud exports. A declined optional connection must not block newsletter setup.
5. Collect sender addresses, timezone, cadence, archive window, edition limit, delivery recipient, delivery mode, and optional reading-event settings.
6. Reject duplicate or invalid sender addresses before any mailbox search. Show a redacted configuration summary.
7. Run a read-only Gmail count preview by source. Do not pass credentials, raw message bodies, MIME content, or attachment bytes to Store of Scope.
8. Obtain explicit approval for initial ingestion, then save configuration using the current revision.
9. Generate and validate a workbook and e-book preview through separately authorized host capabilities. Do not claim success without validation receipts.
10. Obtain separate approval for the first send and future unattended sends. A first-send approval is not unattended-send approval.
11. If enabled, upsert one Calendar reading event and reconcile duplicates before creating another.
12. Propose one daily scheduled task in the configured timezone. Create it only after the user approves the exact schedule and prompt.
13. Re-read status and report connections, source counts, delivery mode, next run, pause control, and manual-mode fallback.

## Recovery

- On a revision conflict, reread status and reconcile; never overwrite.
- On Gmail disconnection, pause dependent work and guide reconnection.
- On a pending run, recover or reconcile it before starting another.
- If scheduled tasks are unavailable, configure manual mode and provide: `Run today's Store of Scope newsletter workflow.` Do not claim automation is active.
- Require confirmation before retirement, workspace deletion, Calendar cleanup, or replacement of user-owned artifacts.
