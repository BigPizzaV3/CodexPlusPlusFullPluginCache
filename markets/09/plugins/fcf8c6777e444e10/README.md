# Rankfor Answer Trail plugin package

This directory is the portable package for Rankfor Answer Trail.

## Contents

- `plugin.json`: package identity, listing metadata, review cases and publication notes.
- `mcp.json`: one production Streamable HTTP MCP endpoint with OAuth Dynamic Client Registration (DCR); OAuth endpoints are discovered from the service.
- `skills/answer-trail/SKILL.md`: bounded instructions for running and reporting snapshots.
- `assets/rankfor-mark.png`: existing Rankfor mark used for the directory logo and composer icon.

The package contains the public listing metadata, one remote MCP connection, bounded operating instructions and the existing Rankfor mark. Secrets, reviewer credentials and private test evidence stay outside the archive.

If sign-in is interrupted, retry the plugin connection so the OAuth flow can resume; do not add credentials to the package.

## Service scope

The plugin exposes two focused tools from the deployed MCP endpoint:

- `create_visibility_snapshot` creates one dated provider-API snapshot from a neutral buyer question.
- `get_visibility_snapshot` reads or polls a snapshot owned by the connected Rankfor account.

Its purpose is to inspect returned brand evidence, candidate brands, cited sources and collection status for one buyer question at a time.

## Validation and submission

Follow `../DIRECTORY-SUBMISSION.md` for package validation, reviewer materials, live-server gates and portal steps. A valid ZIP is an upload artifact. It is not evidence that the MCP server passed domain verification, authentication, tool scanning, reviewer testing or publication review.
