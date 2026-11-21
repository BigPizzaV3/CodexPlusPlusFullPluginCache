# Lukka-AML - 4 Production Tools

AML report generation across 107+ blockchains. All tools are exposed as `AML___<tool>`.

Only the 4 report tools below are available on the hosted surface.

## Report Tools (4)

| Tool | Use when | Size | Notes |
|------|----------|------|-------|
| `AML___generateAmlScoringReport` | Light AML check (default) | small | Available on all supported chains. Returns risk score, letter grade, top factors. A clean/no-history address scores **~33 (MEDIUM)**, not 0/LOW - that is the baseline, not a risk signal. |
| `AML___generateAmlStandardReport` | Full AML report | 300-500 KB | MUST be piped through `process_aml_report.py` (see `large-data-processing` skill). See supported chains below |
| `AML___generateAmlEnhancedReport` | Deepest AML analysis | 500 KB+ | Always pipe through `process_aml_report.py`. See supported chains below |
| `AML___generateAmlSimplifiedReport` | Light report for additional chains | small | See supported chains below |

### Report parameters

- `address` (string, required) - the raw wallet address ONLY. Pass the bare hex/base58 string (e.g. `0x13203aB9...3477`), never a phrase. The hosted API does NOT parse natural language: appending anything like `on Eth` / `on Ethereum` to the address returns HTTP 422. If the user typed a sentence, extract just the address before calling.
- `address_type` (string, required, UPPERCASE) - `BTC`, `ETH`, `SOL`, `TRX`, etc. **Not `blockchain`** - the hosted MCP wrapper enforces this exact field name. The chain goes here, never inside `address`.

### Report tier availability by chain

Each report tier is available on specific chains:

- **SCORING** - available on all supported chains (light default).
- **STANDARD / ENHANCED** - available on: `ADA, AVAX, BCH, BSV, BTC, CC, DASH, DOGE, DOT, DOT_AH, ETC, ETH, FIL, ICP, IOTA_MAINNET, IOTAEVM, LTC, MATIC, NEAR, NEO, RSK, SOL, TRX, VET, XDAI, XLM, XRP, XTZ, ZEC, ZKS`
- **SIMPLIFIED** - available on: `ALGO, APT, ARBITRUM, ATOM, AZERO, BASE, BNB, BSC, CANTO, CELO, CHZ, CKB, COTI, CRO, CRONOS, DCR, DGB, DOGECHAIN, ECS, EGLD, EOS, ETHW, EVMOS, FET, FLOW, FTM, FUSE, GLMR, GRAM, HASH, HBAR, HT, IMX, IOTA, IOTX, KAVA, KCS, KDA, KLAY, KSM, LINEA, LSK, LUNA, LUNC, MINA, MNT, MOVR, NEO3, ONE, ONT, OP, PALM, PLS, QTUM, REEF, RON, ROOT, RUNE, SDN, SEI, SMR, STX, SUI, TAO, THETA, TLOS, TON, VIC, WAN, WAVES, WAX, XDC, XEC, XEM, XNO, XVG, XYM, ZEN, ZIL, ZKEVM`

### Choosing the right report depth

```
Any chain, default light check        -> generateAmlScoringReport (no processor needed)
STANDARD/ENHANCED chain + "full"      -> generateAmlStandardReport + processor
STANDARD/ENHANCED chain + "deep dive" -> generateAmlEnhancedReport + processor
SIMPLIFIED chain + light report       -> generateAmlSimplifiedReport
SIMPLIFIED chain + "full/deep"        -> use generateAmlScoringReport (deep tiers cover the STANDARD/ENHANCED chain list above)
```

## Counterparty Exposure and Address Assets

For counterparty exposure use `generateAmlStandardReport`/`generateAmlEnhancedReport` (pipe through the processor); for address assets use `UDA___get_address_assets`.

## Quick Examples

```
# Light AML check
AML___generateAmlScoringReport({
  address: "0x13203aB9C9f054fe8B4671bC0EEC3ab26D2f3477",
  address_type: "ETH"
})

# Full report (always pipe through processor to avoid context overflow)
AML___generateAmlStandardReport({
  address: "0x13203aB9C9f054fe8B4671bC0EEC3ab26D2f3477",
  address_type: "ETH"
})
# Save JSON to /tmp/aml_report.json, then:
# python3 /tmp/process_aml_report.py /tmp/aml_report.json
```

For counterparty exposure use `generateAmlStandardReport`/`generateAmlEnhancedReport` (pipe through processor); for address assets use `UDA___get_address_assets`.
