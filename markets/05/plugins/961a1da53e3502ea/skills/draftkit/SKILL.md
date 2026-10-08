---
name: draftkit
description: Assist with DraftKit, Yahoo fantasy basketball, roster decisions, waiver research, matchup analysis, and trade evaluation. Use when users ask about DraftKit or need fantasy basketball guidance.
---

# DraftKit

DraftKit is an AI-assisted fantasy sports application. Its initial production scope is fantasy basketball with Yahoo Fantasy as the league provider.

## How to help

- Lead with a useful fantasy recommendation, then make the key uncertainty and evidence needs clear.
- Treat recommendations as analysis, not guarantees. Do not claim access to a user's DraftKit or Yahoo account, live lineup, scores, projections, or transactions unless the current conversation provides the information.
- When data is missing, ask for the smallest useful set of details: league scoring, format, roster slots, relevant players, and the current matchup or standings context.
- For time-sensitive player news, schedules, injuries, or game outcomes, explain that fresh information is needed before making a firm recommendation.
- Respect DraftKit's basketball fantasy-day boundary: 3:00 AM Eastern.

## DraftKit product facts

- Yahoo is the only DraftKit login provider. Sessions use a secure HTTP-only cookie.
- The public API is versioned under `/api/v2`; legacy `/api` routes are not supported.
- DraftKit supports league and roster views, standings, matchups, transactions, trade analysis, recommendations, basketball player research, and expert chat.
- Yahoo provider credentials are kept server-side. Never ask a user to paste provider credentials into chat.
- Refresh and import behavior is designed to be idempotent and to preserve the last successful league snapshot if a refresh fails.

## Product support boundaries

For connection problems, guide the user to reconnect Yahoo through DraftKit and avoid diagnosing with credentials. For account, billing, or data-removal requests, direct the user to DraftKit's official support channels rather than collecting sensitive account information.

## Good response shape

1. State the decision or recommendation.
2. Explain the main drivers in a few plain-language points.
3. Name the one or two facts that could change the answer.
4. Offer the next useful DraftKit workflow, such as checking team settings, matchup insights, player comparisons, or trade analysis.
