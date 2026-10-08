---
name: pdf-reports
description: |
  **Required for generate_pdf_report tool.**

  Read this skill BEFORE calling generate_pdf_report to understand
  how to write professional analytical reports with narrative depth.
---

# PDF Report Generation

## Report Architecture

Every report MUST follow this structure. No exceptions.

### 1. Executive Summary (text section)

- 2-3 paragraph narrative. Lead with a thesis statement about the key finding.
- Bold key statistics inline: **$266.3 billion**, **+317% YoY**.
- Provide context for every number (vs prior period, vs benchmark, vs market total).
- NOT a bullet list. Write flowing prose that tells the story.

### 2. Key Insights (text section)

- 3-5 numbered insights. The "if you read nothing else" page.
- Each insight: **Bold headline (10 words max)** followed by supporting data and one-sentence implication.
- Example: "**1. Stablecoin payments surpassed credit card volume.** Monthly payment volume hit **$48.3B** in February, exceeding Visa's average merchant settlement volume for the first time. This signals stablecoins are crossing from speculation into real commerce."

### 3. Themed Analytical Sections (3-6 sections)

Each theme follows a repeating pattern of three sections:

1. **Context text** (titled) - Why this data matters. Frame the question being answered. 1-2 sentences.
2. **Chart or table** (titled) - The visualization itself.
3. **Interpretation text** (empty title `""`) - What the data reveals. Bold the key takeaway. Call out anomalies, benchmarks, or surprising patterns. 2-4 sentences.

This interleaved pattern is critical. Charts must never appear without surrounding context and interpretation.

### 4. Methodology (text section, for reports with 3+ data sections)

- Data sources and APIs used.
- Time periods and filters applied.
- Known limitations or caveats.
- Keep it brief but honest about what the data does and doesn't cover.

## Content Writing Rules

### Before every chart/table

Write 1-2 sentences framing what the reader is about to see and why it matters.

### After every chart/table

Use an empty-title text section (`"title": ""`) for interpretation:

- 2-4 sentences interpreting findings.
- **Bold the key takeaway** so a skimmer catches it.
- Call out anomalies, inflection points, or surprising patterns.
- Provide context: vs prior period, vs benchmark, vs total.

### Statistics and numbers

- Bold key statistics inline: **$266.3 billion**, **+317%**.
- Always contextualize: "representing **42%** of total DEX volume, up from 28% last quarter."
- Don't just report WHAT. Explain WHY it matters.

### Section titles

- Use insight-driven titles, not metric-driven titles.
- Good: "Payment Adoption Outpaces Speculation"
- Bad: "Daily Trading Volume"

### Cross-references

- When data in one section relates to another, say so: "Consistent with the supply shift noted above..."

## Anti-Patterns (avoid these)

- **Bullet-list executive summaries** - Write prose paragraphs instead.
- **Naked charts** - Every chart needs context before AND interpretation after.
- **Data-descriptive section titles** - "Daily Trading Volume" tells the reader nothing. Use insight-driven titles.
- **Reports without methodology** - Include data sources and limitations for any report with 3+ data sections.
- **Restating numbers without interpretation** - Don't say "Volume was $10B." Say "Volume hit **$10B**, a **+34%** increase that coincided with the ETH ETF approval."
- **Flat structure** - Don't dump a sequence of charts. Group related data into themed sections with narrative flow.

## Empty-Title Sections

Set `"title": ""` on a section to render it without a header or TOC entry. The content flows directly below the previous section. Use this for chart/table interpretations:

```json
{"title": "Payment Adoption Outpaces Speculation", "type": "text", "data": {"content": "The shift from speculative trading to real payment usage is the defining trend of 2026..."}},
{"title": "Monthly Payment Volume", "type": "chart", "data": {"chart_type": "line", "labels": ["Jan", "Feb", "Mar"], "values": [32.1, 48.3, 51.7], "y_label": "Volume ($B)"}, "source": "Allium API"},
{"title": "", "type": "text", "data": {"content": "Payment volume grew **60%** in Q1, reaching **$51.7B** in March. The acceleration began in February when two major e-commerce platforms integrated USDC checkout. **This is the first quarter where payment volume exceeded speculative trading volume.**"}}
```

## Full Example

```json
{
  "title": "Stablecoins Infrastructure Report",
  "sections": [
    {
      "title": "Executive Summary",
      "type": "text",
      "data": {
        "content": "The stablecoin market reached a combined market capitalization of **$266.3 billion** in Q1 2026, representing a **+41% increase** year-over-year and surpassing the previous all-time high set in late 2024. This growth was driven primarily by payment adoption rather than speculative trading, marking a structural shift in how stablecoins are used.\n\nUSDT maintained its dominant position with **$142B** in circulation, but USDC grew at nearly **3x the rate**, narrowing the gap from 3.2:1 to 2.4:1. The most significant development was the emergence of institutional payment rails, with **$48.3B** in monthly payment volume processed through stablecoin networks in February alone.\n\nThis report examines supply dynamics, payment adoption, chain-level infrastructure shifts, and the competitive landscape across the top stablecoin issuers. Data is sourced from Allium's cross-chain analytics covering 15 networks."
      }
    },
    {
      "title": "Key Insights",
      "type": "text",
      "data": {
        "content": "**1. Payment volume surpassed speculative trading for the first time.** Monthly payment volume hit **$48.3B** in February, exceeding trading-related transfer volume. This signals stablecoins are crossing from speculation into real commerce.\n\n**2. USDC is closing the gap with USDT at an accelerating rate.** USDC supply grew **+89%** YoY vs USDT's **+31%**, driven by regulatory clarity in the US and EU. The ratio narrowed from 3.2:1 to 2.4:1.\n\n**3. Arbitrum and Base captured 62% of new stablecoin deployment.** L2 networks absorbed the majority of new supply, with average transaction costs under **$0.003** making micropayments viable.\n\n**4. Institutional on-ramps grew 4x in Q1.** The number of verified institutional wallets holding >$1M in stablecoins increased from 1,200 to 4,800, driven by new custody integrations.\n\n**5. Average transfer size dropped 73%, signaling retail adoption.** Median transfer fell from **$4,200** to **$1,150**, consistent with payment use cases rather than treasury management."
      }
    },
    {
      "title": "Supply Growth Signals Structural Demand",
      "type": "text",
      "data": {
        "content": "Total stablecoin supply is the most fundamental indicator of ecosystem health. Unlike trading volume, which can be inflated by wash trading or arbitrage, supply growth reflects genuine demand for dollar-denominated digital assets."
      }
    },
    {
      "title": "Total Stablecoin Supply (Q1 2025 - Q1 2026)",
      "type": "chart",
      "data": {
        "chart_type": "line",
        "labels": ["Q1 2025", "Q2 2025", "Q3 2025", "Q4 2025", "Q1 2026"],
        "values": [188.7, 205.3, 224.1, 248.9, 266.3],
        "y_label": "Market Cap ($B)"
      },
      "source": "Allium Cross-Chain Analytics"
    },
    {
      "title": "",
      "type": "text",
      "data": {
        "content": "Supply grew consistently across all four quarters, with **no quarter showing negative growth** for the first time since 2021. **The Q1 2026 figure of $266.3B represents a new all-time high**, surpassing the previous peak of $188B in late 2024. The steady growth pattern, rather than spike-and-crash, suggests structural demand rather than speculative cycles."
      }
    },
    {
      "title": "Payment Adoption Outpaces Speculation",
      "type": "text",
      "data": {
        "content": "The ratio of payment volume to speculative trading volume has been trending upward since mid-2025. This section examines whether the crossover observed in February represents a permanent shift or a temporary anomaly."
      }
    },
    {
      "title": "Monthly Volume by Use Case",
      "type": "chart",
      "data": {
        "chart_type": "bar",
        "labels": ["Oct 2025", "Nov 2025", "Dec 2025", "Jan 2026", "Feb 2026"],
        "values": [38.2, 41.5, 43.8, 45.1, 48.3],
        "y_label": "Payment Volume ($B)"
      },
      "source": "Allium Payment Classification Model"
    },
    {
      "title": "",
      "type": "text",
      "data": {
        "content": "Payment volume increased every month in the observation period, reaching **$48.3B in February**. The acceleration in January and February coincided with two major e-commerce platform integrations (Shopify USDC and Stripe stablecoin settlement). **This is the first sustained period where payment volume exceeded speculative transfer volume**, though the classification model carries a ~5% margin of error on the payment/speculation boundary."
      }
    },
    {
      "title": "Chain-Level Infrastructure Shifts",
      "type": "text",
      "data": {
        "content": "Where stablecoins live matters as much as how much exists. Chain selection reflects cost sensitivity, speed requirements, and ecosystem maturity."
      }
    },
    {
      "title": "Stablecoin Supply by Chain",
      "type": "chart",
      "data": {
        "chart_type": "pie",
        "labels": ["Ethereum", "Tron", "Arbitrum", "Base", "Solana", "Other"],
        "values": [112.5, 58.2, 38.4, 27.1, 18.9, 11.2]
      },
      "source": "Allium Cross-Chain Analytics"
    },
    {
      "title": "",
      "type": "text",
      "data": {
        "content": "Ethereum remains the largest host at **$112.5B (42%)**, but its share declined from 51% a year ago. **Arbitrum and Base together captured 62% of new supply deployment in Q1**, reflecting the migration to lower-cost L2 infrastructure. Tron's **$58.2B** remains concentrated in emerging market remittance corridors, a use case largely separate from the DeFi ecosystem."
      }
    },
    {
      "title": "Methodology",
      "type": "text",
      "data": {
        "content": "**Data sources:** Allium cross-chain analytics covering 15 EVM and non-EVM networks. Supply figures include USDT, USDC, DAI, FRAX, and PYUSD with market cap >$100M.\n\n**Time period:** Q1 2025 through Q1 2026 (April 1, 2025 - March 31, 2026). Monthly figures use end-of-month snapshots.\n\n**Payment classification:** Allium's proprietary model classifies transfers as payment vs speculative based on wallet clustering, counterparty analysis, and transaction patterns. Margin of error: ~5%.\n\n**Limitations:** Cross-chain bridge transfers may be double-counted in supply totals. Tron data excludes unverified contract deployments. L2 supply figures include bridged assets from Ethereum."
      }
    }
  ],
  "options": {
    "subtitle": "Q1 2026 Analysis",
    "author": "Allium Research",
    "date": "March 2026",
    "include_toc": true
  }
}
```

## Workflow

1. Gather data using `run_sql_query`
2. Plan your report architecture: identify 3-5 themes from the data
3. Write the executive summary and key insights FIRST (forces you to identify the story)
4. Build themed sections with the text > chart > interpretation pattern
5. Add methodology section
6. Call `generate_pdf_report` with the structured sections

## Section Types Reference

All section types support an optional `source` field for data attribution (rendered as small gray text below the content).

### Table

```json
{
  "title": "Token Holdings",
  "type": "table",
  "data": {
    "columns": ["Token", "Balance", "USD Value"],
    "rows": [["ETH", "1.5", "$5,000"], ["USDC", "1,000", "$1,000"]]
  },
  "source": "Allium API"
}
```

### Chart

```json
{
  "title": "Portfolio Allocation",
  "type": "chart",
  "data": {
    "chart_type": "pie",
    "labels": ["ETH", "USDC"],
    "values": [5000, 1000]
  },
  "source": "CoinGecko"
}
```

Chart types: `pie` (allocation), `line` (time series), `bar` (comparison)

Optional: `x_label`, `y_label` for line/bar charts.

### Text

```json
{
  "title": "Summary",
  "type": "text",
  "data": {
    "content": "Total portfolio value: $6,000 across 2 tokens. Supports **bold** and *italic* markdown."
  }
}
```

## Options

- `orientation`: "portrait" (default) or "landscape" for wide tables
- `include_timestamp`: true (default) or false
- `subtitle`: subtitle displayed on the cover page
- `author`: author name on cover page
- `date`: date string on cover page
- `include_toc`: false (default) or true - adds a table of contents page. Use for reports with 4+ sections.
