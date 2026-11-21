# Lukka On-chain Data MCP — hosted workflows

Adapted from the publisher-provided `lukka-mcp-hosted` product reference. Old deployment observations must be checked against current discovery and returned data.

## Bind the request to its chain and endpoint

Use lowercase `blockchain` values such as `eth` and `btc` where the live tool supports them. Coverage is per endpoint: support for a block query does not prove support for an address, asset or transaction query on that chain. Treat an explicit unsupported-chain response as a coverage result, not a reason to try unrelated addresses.

- Height and blocks: `UDA___Get_newest_block_blockheight` and `UDA___get_block`.
- Wallets: `UDA___get_address_balance` and `UDA___get_address_assets`.
- Transactions: `UDA___get_address_transactions` and `UDA___Get_transaction_for_txhash`.

For transaction lists, use either the supported newest flag or a paired range, according to the live schema. Do not combine mutually exclusive selectors. Start with a small limit and moderate verbosity; large decoded block/transaction responses need the host's available file or processing capabilities. Balance envelopes differ by chain, so inspect the returned shape and units.

## Ethereum validators

The recorded direct catalog includes validator tools. Use `UDA___get_latest_epoch` to obtain a current slot before `UDA___get_validator_balance` when the invocation requires one. Use validator event tools only for the coverage and identifiers they actually expose. The old source's blanket statement that all validator data was unavailable conflicts with its own validator section and is not carried forward.

Historical notes report that some balance values were ETH despite a Gwei description, slashing could return an empty object, and consolidation arguments once mismatched the upstream API. Check returned units, empty-result semantics and current schema; do not invent extra parameters to repair a failing backend. An unexplained 403 is not automatically a chain-coverage finding.

Report actual address/chain, block height or observation time. Wallet balances do not supply AML risk scores and this plugin does not transfer funds.
