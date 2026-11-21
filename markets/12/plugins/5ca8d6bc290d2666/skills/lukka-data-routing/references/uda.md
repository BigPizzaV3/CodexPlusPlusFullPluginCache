# Lukka-UDA - 6 Production Tools

Universal Data API for raw blockchain data. All tools exposed as `UDA___<tool>`. Blockchain symbols are **lowercase** (`btc`, `eth`, `xrp`, ...).

## Supported blockchains

**Support is PER-ENDPOINT, not global per chain.** A chain served by one tool can be unsupported on another - always confirm against the actual endpoint you need. An unsupported chain returns `{"content":"Unsupported crypto symbol: <chain>"}` (or a 404 with that text) - a hard signal, not a transient error; do NOT retry with another address.

Address / transaction data endpoints (`get_address_balance`, `get_address_assets`, `get_address_transactions`, `Get_transaction_for_txhash`):

| Chain | balance | assets | transactions |
|-------|:---:|:---:|:---:|
| btc, bch, ltc, doge, dash | yes | yes | yes |
| eth, avax | yes | yes | yes |
| xrp, xlm, near, dot | yes | yes | yes |
| **vet** | yes | **NO** | **NO** |
| trx, matic, sol, ada | **NO** | **NO** | **NO** |

- `vet` is balance-only: `get_address_assets` / `get_address_transactions` return "Unsupported crypto symbol: vet".
- `trx`, `matic`, `sol`, `ada` are NOT served by ANY address/transaction endpoint - do not route wallet scans, AML-adjacent balance lookups, or tx pulls for these chains to UDA.


## Chain Data (2 tools)

| Tool | Use when | Key params |
|------|----------|-----------|
| `UDA___Get_newest_block_blockheight` | Latest block height (legacy v1) | `blockchain` |
| `UDA___get_block` | Block detail + tx list | `blockchain`, `block`, `verbose` ("1"=tx hashes, default / "2"=full decoded tx objects) |

## Address / Transaction Data (4 tools)

| Tool | Use when | Key params |
|------|----------|-----------|
| `UDA___get_address_balance` | Current balance | `blockchain`, `address`; optional `asset` |
| `UDA___get_address_assets` | All tokens an address holds / interacted with | `blockchain`, `address` |
| `UDA___get_address_transactions` | Transaction list | `blockchain`, `address`, `verbose` ("0"=hashes / "1"=details / "2"=full decoded tx object), `limit` (max 1000), `get_newest`, `from_time`, `to_time`, `from_block`, `to_block`. **`verbose:"2"` only with a small `limit`** - high latency / response size |
| `UDA___Get_transaction_for_txhash` | Single transaction detail | `blockchain`, `txhash` |

### Wallet scan guidance (context safety)

- Preview: `verbose:"1"`, `limit: 100` or less, `get_newest:"1"`.
- Full scan: call with `limit: 1000`, save raw JSON to `/tmp/txs.json`, pipe through `process_transactions.py` (see `large-data-processing` skill), then selectively decode flagged hashes via `Get_transaction_for_txhash`.
- Never call `verbose:"1"` at high limits without a processor ready - responses run 150 KB+ per call.

## ETH Staking / Validator Data

For ETH staking and validator data, use the Lukka-Pricing derivative trades / historical derivative trades as adjacent data for ETH staking derivatives.

## Quick Examples

```
# ETH wallet balance
UDA___get_address_balance({
  blockchain: "eth",
  address: "0x13203aB9C9f054fe8B4671bC0EEC3ab26D2f3477"
})

# Latest BTC block
UDA___Get_newest_block_blockheight({ blockchain: "btc" })

# Preview 50 newest ETH txs
UDA___get_address_transactions({
  blockchain: "eth",
  address: "0x13203aB9C9f054fe8B4671bC0EEC3ab26D2f3477",
  verbose: "1",
  limit: 50,
  get_newest: "1"
})

# Specific transaction
UDA___Get_transaction_for_txhash({
  blockchain: "eth",
  txhash: "0xabc..."
})
```
