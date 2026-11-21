---
name: saleslumen-campaigns
description: >-
  Manage Saleslumen campaigns via MCP: campaigns, people, variables, sequences,
  rules, schedules, deliveries, and suppressions. Use when the user wants
  outreach campaigns, enrollments, or sequence steps. Do not use for inbox
  email, workflows, or running a people script.
---

# Saleslumen Campaigns

Use the Saleslumen MCP connector for campaign setup and enrollment. Keep the conversation natural; change structure and people with tools.

## Concepts

A campaign holds settings, variables, people, one immutable entry sequence, additional sequences, and rules. Variables define the schema; people hold values for those variables. Create already includes `given_name` and `family_name`.

Sequences are trigger-free `SEND_EMAIL` trees. `campaigns_create` returns `campaign` and `entry_sequence`. The entry sequence is named Main. Its first email stays `START_NEW`. Later steps are `CONTINUE`. A non-entry sequence may start `START_NEW` or `CONTINUE`. Enabled `START_NEW` variants require `subject`. `CONTINUE` variants omit `subject`. `body_document` is `schema_version` 1 and `doc`. Omit step and variant names on create.

Rules are a separate resource. A rule matches one event type: `MESSAGE_OPENED`, `MESSAGE_CLICKED`, `MESSAGE_REPLIED`, `MESSAGE_REPLY_SENT`, `THREAD_LABEL_ADDED`, `THREAD_LABEL_REMOVED`, or `SEQUENCE_COMPLETED`. `srl_expression` is Saleslumen Rule Language. Priority is unique within the event type; lower runs first. Actions are `ENTER_SEQUENCE` (with `target_sequence`), `RESUME_SEQUENCE`, `STOP`, and `CANCEL_PENDING_TRANSITION` (`delay_seconds` 0). Rule changes apply to future events.

`campaigns_get_task` and `campaigns_get_operation` report async work. Parent statuses are `PENDING`, `PROCESSING`, `RETRYING`, `COMPLETED`, and `FAILED`. Poll until `COMPLETED` or `FAILED`. Treat `RETRYING` as still in progress.

This plugin does not run a campaign people script.

## Workflow

1. Clarify the goal (settings, people, variables, sequences, rules, metrics, deliveries, or task status).
2. Read with `campaigns_list` / `campaigns_get` before you change an existing campaign. A create does not need a prior read.
3. `campaigns_create` returns a draft and its entry sequence. Add other sequences with `campaigns_create_sequence`. `campaigns_update_sequence` replaces that sequence's display name and step tree. There is no step tool and no sequence trigger.
4. Write a rule's `srl_expression` in SRL; do not substitute prose.
5. Confirm with the user before delete, `campaigns_set_variables`, archive, unsubscribe, and stop.
6. Summarize the new resource names and the next useful step.

## Tools

| Task | Tools |
| --- | --- |
| Campaigns | `campaigns_list`, `campaigns_create`, `campaigns_get`, `campaigns_update`, `campaigns_delete`, `campaigns_archive`, `campaigns_unarchive`, `campaigns_activate`, `campaigns_pause`, `campaigns_resume`, `campaigns_complete` |
| Variables and senders | `campaigns_set_variables`, `campaigns_set_sender_accounts` |
| Metrics | `campaigns_get_metrics` |
| People | `campaigns_list_people`, `campaigns_create_person`, `campaigns_get_person`, `campaigns_update_person`, `campaigns_delete_person`, `campaigns_batch_delete_people`, `campaigns_import_people`, `campaigns_pause_person`, `campaigns_resume_person`, `campaigns_unsubscribe_person`, `campaigns_stop_person`, `campaigns_list_person_activity` |
| Sequences | `campaigns_list_sequences`, `campaigns_create_sequence`, `campaigns_get_sequence`, `campaigns_update_sequence`, `campaigns_delete_sequence`, `campaigns_preview_sequence` |
| Rules | `campaigns_list_rules`, `campaigns_create_rule`, `campaigns_get_rule`, `campaigns_update_rule`, `campaigns_delete_rule` |
| Schedules | `campaigns_list_schedules`, `campaigns_create_schedule`, `campaigns_get_schedule`, `campaigns_update_schedule`, `campaigns_delete_schedule` |
| Deliveries and suppressions | `campaigns_list_deliveries`, `campaigns_get_delivery`, `campaigns_resolve_unknown_delivery`, `campaigns_list_suppressions`, `campaigns_create_suppression`, `campaigns_delete_suppression` |
| Tasks | `campaigns_get_task`, `campaigns_get_operation` |

## Guidance

- `campaigns_set_variables` replaces the whole ordered variable list.
- Enroll people with `campaigns_create_person`. `email_address` is optional. Read existing values before you overwrite them.
- `campaigns_create` takes `display_name` and a `request_id` UUID. The response is `campaign` and `entry_sequence`. `campaign.state` is `DRAFT`. The identifier is `campaign.name` (`campaigns/{uuid}`). There is no `id` field. `campaign.entry_sequence` is `campaigns/{campaign}/sequences/{sequence}`. `campaigns_list` returns `campaigns` and `next_page_token`.
- `campaigns_resolve_unknown_delivery` requires the exact `expected_attempt_id` and `expected_attempt_number` 1..3 from `campaigns_get_delivery`.
- Stay in the Campaigns tools for this skill. Use the Apps Script or Workflows skill when the user wants script projects or workflow graphs.
