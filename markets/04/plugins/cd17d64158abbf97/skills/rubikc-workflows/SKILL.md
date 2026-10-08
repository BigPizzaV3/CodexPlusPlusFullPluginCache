---
name: rubikc-workflows
description: Inspect and manage Rubikc storefronts, cubes, content, navigation, structures, files, brand, onboarding, and analytics through Rubikc MCP tools. Use when the user mentions Rubikc, a storefront, cubes, feed content, navigation menus, collections, or storefront analytics.
---

# Rubikc workflows

Use this skill for Rubikc storefront, cube, content, asset, navigation, structure, brand, onboarding, and analytics work.

Do not copy Rubikc playbooks into this skill. Load domain rules from the MCP `instructions` tool when a workflow needs them.

## Start

1. Call `getMcpStatus` if authentication or the connection is unclear.
2. Call `listStorefronts` before storefront-specific work and select an explicit `storefrontId`.
3. Inspect existing state before proposing or making changes.

## Load domain rules

Call `instructions` with the matching topic instead of restating cube, content, image, or analytics rules here:

- `content` for cubes and feed content
- `images` for JPG 9:16 import and upload
- `navigation` for menu documents
- `structures` for collection membership
- `analytics` for metrics and reporting
- `onboarding` for launch-ready storefront setup

## Inspect before mutate

Prefer `getStorefrontMap`, the relevant playbook, or an `inspect*` / `analyze*` tool before writes.

## Safe changes

- Prefer preview, dry-run, and read operations before mutations when available.
- Before a broad mutation, state which storefront and resources will change.
- Do not publish content, delete records, revoke access, or perform other destructive actions unless the user explicitly requests that outcome.
- Use Rubikc-hosted asset URLs in content. Import or upload external assets before attaching them.

## Workflow map

- content / cubes → `instructions` `content`, then `manageCubes` / `manageCubeContent*`
- images / 9:16 assets → `instructions` `images`, then `manageFiles`
- navigation → `instructions` `navigation`, then `manageNavigation`
- structures / collections → `instructions` `structures`, then `manageStructures`
- analytics → `instructions` `analytics`, then `analyzeStorefront` / `analyzeCubes` / `inspectSessions`
- new storefront setup → `instructions` `onboarding`, then `getOnboardingContext` / `manageOnboarding`

## Example first turn

1. Call `getMcpStatus` if needed.
2. Call `listStorefronts` and pick a `storefrontId`.
3. Inspect with `getStorefrontMap` or the matching read tool.
4. Stop and report findings unless the user asked for a change.
