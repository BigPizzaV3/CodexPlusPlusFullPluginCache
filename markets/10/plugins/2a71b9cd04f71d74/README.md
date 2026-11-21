# Solana Intelligence by Nova

Version 0.3.2 adds interactive token charts and public-wallet views in ChatGPT while preserving Nova’s 47 model-visible, read-only research operations. The public endpoint remains https://ai.nov.ag/mcp/solana-intelligence and requires no authentication. The [tool guide](skills/solana-intelligence/references/tools.md) retains each public operation’s accepted inputs.

## Interactive research

Chart results render automatically from `nova_token_chart`; no separate UI opener is needed. Expand a chart to inspect supplied observations and use the available Price/Market Cap and history-range controls. Prices, missing volume and observation gaps retain their actual data limits.

Public-wallet cards expand into a profile with Positions, Closed and Activity tabs. The widget resolves the public profile and reads Nova’s canonical wallet views through app-only operations. The initial public summary retains its requested currency and strict/adjusted accounting; expanded tabs preserve their own canonical accounting and coverage. Closed rows use token-lifetime aggregates, and Activity may lack transfer-only history.

Normal responses and cards identify Nova. Original provenance remains in raw tool results; the user interface does not add a visible provider breakdown or Details/Data notes panel. Material warnings, unknown observation freshness, stale/partial/indexing/unavailable states and nullable values remain meaningful.

## Research coverage

Token information and mint facts; bounded holder, bundler, first-buyer and trader cohorts; indexed trades, liquidity and sampled flows; token OHLCV and batch prices; public-wallet holdings, positions, PnL and historical analytics; KOL directory and monitored activity; sampled smart-money and whale observations; indexed DCA intentions; discovery and deployer history; and short signal/KOL snapshots.

These are research observations with bounded coverage. The package does not execute trades, construct or sign transactions, broadcast, provide complete wallet cash ledgers, read private messages or create continuing watches. A chart or tab response does not establish continuous live delivery, complete history or finality.

## Package and current review status

The package identity, supplied PNG/SVG icon, developer identity, legal/support links, endpoint and 47 model-tool parameter contracts are unchanged. The duplicated manifests describe 0.3.2 and six positive/three negative review cases. App-only profile/view calls support explicit widget interactions.

The owner-account 0.3.2 draft metadata and SKILL scan passed with No Findings. The C1 MCP rescan published updated UI definitions for 44 tools, including three app-only helpers. Six existing KOL tools remain EarlierVersionPublished with the finding that their new definitions need further review. Their model-visible schemas and read-only annotations are unchanged; the updated associations use Nova’s UI resource/templates. Technical scans do not establish legal rights or review approval.

A C3 UI correction is being prepared with resource v3.1 and v3 read compatibility. Actual ChatGPT-host testing under enforced CSP has exercised the chart, Market Cap, manual transaction-history read and Open interaction. Final C3 host/compatibility verification is pending. Current review context and the separate manual-review appeal draft are retained outside this package in `work/release-verification/`.

## Demo and current UI evidence

The retained demo URL is https://nov.ag/plugin-review/solana-intelligence-0.2.4-demo.mp4 and remains available with HTTP 200. It demonstrates the existing core CLI research flow in the unchanged 47-operation catalog; it does not show the new 0.3.2 interactive UI or prove all 47 tools were exercised. Current UI evidence consists of local actual-host screenshots, not a newly recorded public video.

The current submission form has six declarations and an optional note, without a new public-video field. No additional public-video requirement is inferred here. The owner must finish final host verification and complete the applicable declarations/submission. This README status update does not alter the already uploaded manifests or ZIP.

## Icon update

Version 0.3.2 replaces the listing and composer artwork with the exact owner-selected Aurora glass Solana icon from Figma node 44:11. Research tool schemas and read-only scope are unchanged.

Website and support/legal links use app.nov.ag. The separate MCP identifies itself as Nova Super Intelligence with its owner-supplied Nova brand mark.
