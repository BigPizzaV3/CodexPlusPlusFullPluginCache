---
name: primesync-studio
description: Build, convert, repair, audit, and validate trader-owned TradingView Pine Script or Python strategies with PrimeSync Studio. Use when a trader wants to turn their own rules into code, preserve existing logic or visuals, compare strategy candidates, or run Monte Carlo on chronological backtest returns. Do not use for trade execution, broker access, or profit guarantees.
---

# PrimeSync Studio

Use PrimeSync Studio as a structured engineering layer for trader-owned strategy ideas. Never insert PrimeSync indicator settings, hidden presets, or trading rules that the user did not provide.

## Choose the right tool

- Use `primesync_research_builder` for new strategies or indicators, experiments, conversions, isolated repairs, cross-asset research, optimization, fresh-result validation, or standalone Monte Carlo.
- Use `primesync_strategy_builder` for a focused TradingView/Python strategy blueprint from complete user-supplied rules.
- Use `primesync_audit_strategy` to compare generated code against approved rules and correct implementation failures without inventing logic.
- Use `primesync_monte_carlo` when chronological trade returns are already available and the user wants a deterministic robustness assessment.

## Workflow

1. Capture the trader's idea exactly as supplied.
2. If essential rules are missing, ask one bundled clarification covering only the missing items. Do not silently assign indicator periods, thresholds, sessions, timeframe, execution timing, costs, exits, sizing, or risk.
3. Create a concise approved blueprint before generating code.
4. Generate complete Pine Script v6 or Python as requested.
5. Audit the finished code against every approved rule. Fix code defects without changing intended logic.
6. Treat generated code as a candidate until the user supplies fresh chronological TradingView results.
7. Run Monte Carlo on chronological returns when supplied. Report downside outcome, drawdown, losing streak, and probability of a negative result.
8. Compare multiple candidates by the user's stated objective. If none is stated, prefer robustness and lower downside drawdown rather than claiming a profitable winner.

## Preservation rules

When converting or repairing existing code, preserve logic, order behavior, arrows, plotted levels, and visual timing only when the user requests those invariants. Clearly disclose any unavoidable platform limitation before changing behavior.

## Boundaries

- Do not execute trades, connect to brokers, publish scripts, or access live accounts.
- Do not describe backtests or Monte Carlo as proof of future profitability.
- Do not provide personalized financial advice.
- Do not create reusable market profiles unless the user explicitly asks for profiles.
- Keep assumptions visible and separate supplied rules from inferred implementation details.

When a tool returns a clarification request, ask the user for the missing information instead of generating incomplete code. When a tool returns code or analysis, explain the result concisely and give the next practical TradingView validation step.
