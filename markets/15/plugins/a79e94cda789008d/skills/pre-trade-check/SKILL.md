---
name: pre-trade-check
description: Run a full pre-trade check on one coin before the user acts on an idea elsewhere. Scans token safety, reads trend and derivatives positioning, sizes the position to their risk and checks liquidation against the stop. Use when the user says they are about to buy, long or short a coin, or asks whether a trade idea holds up.
---

# Pre-trade check

Work through the steps in order and stop early if a step returns a danger verdict. Ask once, in one message, for anything missing: coin, side, entry, stop, account size and risk percentage. Use defaults the user already gave in this conversation.

## 1. Token safety (small caps and contracts only)

If the coin is not a top-50 asset or the user gave a contract address, call `scan_token`. On a `danger` verdict, report the flags and stop here. On `caution`, list the flags and continue.

## 2. Trend and levels

Call `analyze_coin` for the coin. Report the verdict, the two or three strongest reasons, nearby support and resistance and the ATR stop. Say plainly if the user's stop sits inside normal daily noise.

## 3. Positioning

Call `get_derivatives_positioning`. Report the bias and squeeze risk in one or two sentences. Note when crowding runs against the user's side.

## 4. Size it

Call `build_trade_plan` with the user's numbers and any leverage they named. Report units, notional, risk in USD, R-multiples at each target and the breakeven win rate. Relay every warning, especially liquidation before the stop.

## 5. Summary

Close with a three-line summary: what supports the idea, what argues against it, and the size that keeps risk at their chosen percentage. These tools do not place orders; the user acts on their own venue.

End with: "These are analysis tools, not financial advice."
