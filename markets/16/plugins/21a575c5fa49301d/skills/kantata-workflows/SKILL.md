---
name: kantata-workflows
description: Use when working with Kantata OX projects, tasks, resource planning, time entries, timesheets, expenses, or project reporting through the connected Kantata OX App.
---

# Kantata workflows

Use the connected Kantata OX App and its actual tool schemas. Discover available tools before choosing an action; do not assume a tool exists merely because a workflow is described here. Respect the authenticated user's permissions and the server's operating notes.

## Dates and terminology

A Kantata work week runs Sunday through Saturday. Interpret "this week" as the Sunday on or before today through the following Saturday, and "last week" as the preceding seven days. Use the user's timezone and state the date range in time-based reports.

Kantata API workspaces are projects; stories are tasks. Workspace allocations describe resource planning. Resolve named projects, tasks, and people to verified IDs through read tools before mutations. Ask when multiple plausible matches remain.

## Retrieve and report

Choose narrow filters and only the associations needed. Follow pagination until the requested scope is complete; if incomplete, state that limitation rather than presenting partial totals as complete. Kantata responses can index objects by ID in top-level collections and order references in a results array; resolve those references before summarizing. Distinguish actual time from planned hours and approved or submitted time from unsubmitted time. Preserve currency and billable status when aggregating financial values.

For project reviews, retrieve the relevant projects and tasks, then the time, allocations, status reports, or financial records needed for the user's question. Report the scope and source records, distinguish observed facts from inferred risks, and avoid treating missing or inaccessible values as zero.

## Requested changes

Read the target's current state and validate required fields before updating it. Carry out only the user's requested changes. Follow tool-specific confirmation requirements and report verified results, including per-item failures in bulk operations. Do not blindly retry a mutation after an uncertain response; check whether it succeeded first.

For timesheet approvals or rejections, retrieve submissions first and verify pending status and the intended submitters and projects. Do not attempt self-approval. Include a rejection reason when provided or required. Confirm cancellation with the user before calling a cancellation tool, as required by the Kantata tools. A cancelled submission returns entries to unsubmitted state and requires a new submission to resubmit. Creating a timesheet submission is scoped to one project; inspect the tool schema and eligible entries first.

## Connection

Use the Kantata App connection created by the submission portal for https://app.mavenlink.com/mcp. Use the host's App connection flow when sign-in is needed. Never request credentials in chat, embed tokens in files, or treat existing tools from another Kantata connection as proof that this plugin's connection is authenticated. If a connection or permission blocks a task, describe the missing step precisely and preserve any useful completed analysis.


