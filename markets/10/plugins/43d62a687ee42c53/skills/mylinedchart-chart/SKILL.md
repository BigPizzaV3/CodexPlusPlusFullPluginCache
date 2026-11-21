---
name: mylinedchart-chart
description: Read and mark up the chart open in the MyLinedChart app (symbol, candles, levels, indicators, positions, drawings). Use when the user asks about their chart or wants lines, zones or notes drawn on it.
---

MyLinedChart runs on the user's computer. The mylinedchart tools talk only to that app.

1. Call get_chart_context first to learn the symbol, timeframe and data source.
2. Use get_candles, get_indicators, get_drawings and get_trades for the facts. Quote prices from the tools, never from memory.
3. To draw, call propose_chart_changes. The user sees each change in the app and accepts or rejects it there.
4. If a tool says the app is not running, ask the user to open MyLinedChart and try again.

These tools are read only for orders. They never place, change or cancel a trade.
