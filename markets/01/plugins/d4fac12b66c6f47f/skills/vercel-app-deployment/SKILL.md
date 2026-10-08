---
name: vercel-app-deployment
description: |
  **Required for Vercel app tools.**

  Read this skill BEFORE using create_vercel_app to understand
  app types, configuration options, and the iteration workflow.
---

# Vercel App Deployment

Generate and deploy Next.js apps powered by Allium data APIs.

## App Types

### wallet_tracker

Track wallet holdings, PnL, and transaction history.

**Features:**

- Token holdings with USD values
- PnL chart showing portfolio value over time
- Transaction history with send/receive indicators
- Multi-chain support

**Options:**

```json
{
  "show_pnl": true,           // Show PnL chart (default: true)
  "show_transactions": true   // Show transaction history (default: true)
}
```

**Example:**

```json
{
  "app_type": "wallet_tracker",
  "title": "My Wallet Tracker",
  "chains": ["ethereum", "polygon", "arbitrum"],
  "theme": "dark",
  "options": {"show_pnl": true, "show_transactions": true}
}
```

### token_analytics

Analyze token prices and market stats.

**Features:**

- Price chart with time range selection (24H, 7D, 30D, 90D)
- Token stats cards (price, price change 24h)

**Options:**

```json
{
  "show_stats": true    // Show stats cards (default: true)
}
```

**Example:**

```json
{
  "app_type": "token_analytics",
  "title": "Token Analyzer",
  "chains": ["ethereum", "base"],
  "theme": "light"
}
```

### price_chart

Dedicated OHLCV price chart with dynamic coloring and detailed stats.

**Features:**

- OHLCV (Open, High, Low, Close, Volume) price chart
- Dynamic green/red coloring based on price direction
- Detailed OHLC tooltip showing all price data points
- Stats card with current price, 24h change, 24h high/low
- Time range selection (24H, 7D, 30D, 90D)
- Optional pre-configured token address

**Options:**

```json
{
  "default_token_address": null,  // Pre-configured token (default: null)
  "default_chain": null,          // Pre-configured chain (default: first chain)
  "show_ohlc_details": true,      // Show OHLC in tooltip (default: true)
  "show_stats_card": true,        // Show price stats card (default: true)
  "show_token_selector": true     // Allow changing token (default: true)
}
```

**Example:**

```json
{
  "app_type": "price_chart",
  "title": "WETH Price Tracker",
  "chains": ["ethereum", "base", "arbitrum"],
  "theme": "dark",
  "options": {
    "default_token_address": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
    "show_ohlc_details": true
  }
}
```

**When to use price_chart vs token_analytics:**

- Use `price_chart` when the focus is on detailed price visualization with OHLCV data and dynamic coloring
- Use `token_analytics` for general token analysis with market cap, volume, and liquidity stats

### wallet_flows

Visualize wallet inflows and outflows as a Sankey diagram.

**Features:**

- Sankey flow chart showing token transfers
- Table view with detailed inflow/outflow data
- Aggregates transfers by counterparty

**Example:**

```json
{
  "app_type": "wallet_flows",
  "title": "Wallet Flow Analyzer",
  "chains": ["ethereum", "polygon"],
  "theme": "dark"
}
```

### custom_dashboard

Custom SQL dashboard with configurable widgets.

**Features:**

- Data tables from Allium Explorer queries
- Charts (line, bar, pie) from query results
- Metric cards for single values

**Options:**

```json
{
  "widgets": [
    {
      "type": "metric",
      "title": "Total Users",
      "query_id": "abc123"
    },
    {
      "type": "chart",
      "title": "Daily Active Users",
      "query_id": "def456",
      "chart_type": "line"
    },
    {
      "type": "table",
      "title": "Top Wallets",
      "query_id": "ghi789"
    }
  ]
}
```

Widget types:

- `metric`: Single value (first cell of query result)
- `chart`: Line, bar, or pie chart
- `table`: Data table with all results

## Supported Chains

- `ethereum` - Ethereum Mainnet
- `polygon` - Polygon PoS
- `arbitrum` - Arbitrum One
- `optimism` - Optimism
- `base` - Base
- `avalanche` - Avalanche C-Chain
- `bsc` - BNB Smart Chain
- `solana` - Solana

## Workflow

### Initial Creation

1. Call `create_vercel_app` with app type and options
2. Tool generates Next.js app and deploys to Vercel
3. Returns `app_id`, `deployment_url`, and `claim_url`
4. User clicks `claim_url` to take ownership on Vercel
5. User adds `ALLIUM_API_KEY` in Vercel project settings

### Iteration

1. `list_vercel_app_files` - See file structure
2. `read_vercel_app_file` - Read files to modify
3. `write_vercel_app_file` - Update files (can batch multiple writes)
4. `deploy_vercel_app` - Deploy changes

**Example iteration:**

```text
User: "Add a dark mode toggle"

1. list_vercel_app_files(app_id="abc123")
   -> See: app/layout.tsx, components/...

2. read_vercel_app_file(app_id="abc123", file_path="app/layout.tsx")
   -> Get current layout code

3. write_vercel_app_file(app_id="abc123", file_path="components/ThemeToggle.tsx", content="...")
   -> Create new component

4. write_vercel_app_file(app_id="abc123", file_path="app/layout.tsx", content="...")
   -> Update layout to include toggle

5. deploy_vercel_app(app_id="abc123")
   -> Deploy updated app
```

## Post-Deployment Setup

After claiming the app, the user must:

1. Go to Vercel project settings
2. Navigate to Environment Variables
3. Add: `ALLIUM_API_KEY` = their API key from <https://app.allium.so/settings/api-keys>
4. Redeploy the app (or wait for next deployment)

## File Structure

Generated apps follow this structure:

```text
app/
  layout.tsx      # Root layout with metadata
  page.tsx        # Main page component
  globals.css     # Global styles
  api/            # API routes (proxy to Allium)
    wallet/
      balances/route.ts
      pnl/route.ts
      transactions/route.ts
components/
  Holdings.tsx    # Feature components
  WalletInput.tsx
  ChainSelector.tsx
  ...
package.json      # Dependencies
tsconfig.json     # TypeScript config
tailwind.config.js
next.config.js
```

## Tips

- **Theme**: `dark` works best for blockchain apps
- **Chains**: Include chains your users are most likely to use
- **Custom Dashboard**: Create queries in Allium Explorer first, then reference their IDs
- **Iteration**: Make multiple file changes before deploying to batch updates
