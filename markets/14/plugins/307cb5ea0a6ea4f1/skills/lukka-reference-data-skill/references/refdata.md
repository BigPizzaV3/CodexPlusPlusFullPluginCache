# Lukka Reference Data MCP — hosted workflows

Adapted from the publisher-provided `lukka-mcp-hosted` product reference. Old deployment observations must be checked against current discovery and returned data.

## Resolve identity before enriching it

Use `refdata___get_asset_mappings` with the user's exchange context and ticker or canonical code; inspect collisions before choosing an asset. Use the returned Lukka ID with `refdata___get_asset_by_id`. Do not assume ticker uniqueness or pass an asset code to an ID-only parameter.

For venue-specific pair resolution, use `refdata___get_pair_mappings` with both pair and `entityCode`. Complete relevant pagination before concluding a venue is unmapped. `CPRO`, `KRAK` and `BINA` are documented example entity codes; resolve the intended entity rather than substituting a familiar exchange name.

## Select reference data

Use `refdata___get_sectors` for taxonomy, the available score tools for dated scores, and entity/VASP tools for returned reference observations. `refdata___list_vasps` does not justify filtering by an entity parameter absent from its live schema; filter returned entity fields locally when appropriate.

For `refdata___list_assets`, inspect the live types of `lukkaAssetIds` and `expandDetails`. The supplied hosted notes describe bracket-encoded values for string passthrough parameters; do not add brackets to a true array or use that historical convention without checking the actual schema. Do not add `detailed` when it is absent from the input schema.

The source notes describe filters that once ignored their input. Validate returned identities against the requested asset instead of accepting HTTP 200 as a successful match. Bound coverage-statistics requests; never issue an unfiltered expensive request to diagnose a known coverage problem. Report an entitlement or backend error without fabricating a replacement score.

Market/custodian tools described as removed in the source must not be invoked unless current discovery actually exposes them. This connection supplies reference observations; pricing and wallet-owner identification are outside its scope.
