---
name: ando-migrate-buzz
description: Move a Buzz relay community into Ando with the maintained Buzz importer, local validation, identity mapping, resumable uploads, and import readback. Use for Buzz history migration requests.
---

# Migrate from Buzz

Read the [shared migration workflow](../../references/migration-workflow.md)
and current [Buzz import guide](https://docs.ando.so/docs/buzz-import).
Use the maintained `@andocorp/buzz-import` CLI; inspect its current `--help`
and version before execution. Verify the relay URL and source identity rather
than treating a community name as a destination or credential.

## Export and preview

Have the user provide `BUZZ_PRIVATE_KEY` through their local secret/environment
mechanism. Do not request the key in chat. With the relay URL resolved, the
documented command shape is:

```sh
npx @andocorp/buzz-import export --relay <relay-url> --out buzz.jsonl
npx @andocorp/buzz-import import --from buzz.jsonl --dry-run
```

Replace angle-bracket values with verified values before running. Export reads
the source; dry run transforms and validates locally without calling Ando.
Record actual snapshot coverage, dropped records, and planned counts. Normal
export follows the source identity's access. Do not imply it includes every
private channel or DM, or reach for an operator database dump to bypass access.

The current CLI does not expose channel/date selection flags. Do not call a
full-community import a one-channel pilot. Use the supported scope or an
authorized test community/workspace, and review the real write scope first.

## Map and import

Use an Ando owner/admin API key with Import history (`imports:write`), and
`files:write` when copying attachments. Check its target workspace. Imported
placeholder members preserve attribution; they are not invited accounts.
Resolve existing Ando member IDs before proposing `--map` entries.

For an explicitly approved self mapping, keep `ANDO_API_KEY` locally configured
and use the verified Buzz public identity:

```sh
npx @andocorp/buzz-import import --from buzz.jsonl --map-self --self <npub-or-hex>
```

`--map-self` maps to the Ando member owning the API key; use it only when that
is the correct person. Repeat `--map <npub-or-hex>=<ando-member-id>` for other
verified matches. Omitting these options retains attribution-only placeholders.

Keep `BUZZ_PRIVATE_KEY` available during write import when copying relay-hosted
files. Review `--skip-files` and `--max-file-mb` when applicable: skipped or
oversized files remain links. Do not describe links as durable uploaded copies.

Retain the snapshot and stable source-workspace ID for resume. Inspect the
CLI's JSON summary, including every dropped/skipped record and file result,
then read back representative content and membership in Ando. Reusing the same
source IDs permits resume; it can also update source renames, visibility, or
archiving, so review those changes before a later delta import.

## Set expectations

The maintained importer preserves source authors and times without sending
notifications or adding unread state. Imported channels do not simply merge
with same-named existing channels, and imported DMs may be separate from
existing Ando DMs. Check actual resulting names and conversation mappings.
An export/import run is a history migration, not continuous Buzz sync or
automatic migration of app integrations.
