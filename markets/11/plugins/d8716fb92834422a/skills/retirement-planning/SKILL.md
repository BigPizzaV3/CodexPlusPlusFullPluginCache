---
name: retirement-planning
description: Use RetirementNeuron's read-only retirement-planning tools to analyze retirement readiness, spending, Social Security, taxes, Roth conversions, withdrawals, scenarios, financial risks, and action plans using the user's saved RetirementNeuron plan.
---

Use this skill when the user asks about their retirement plan, retirement readiness, retirement income, Social Security, retirement taxes, Roth conversions, withdrawal strategy, retirement scenarios, retirement financial risks, or retirement financial action items.

RetirementNeuron provides live retirement-planning data and calculations through its MCP tools. Treat MCP tool results as the authoritative RetirementNeuron calculation for the connected user.

## Core rules

1. Use RetirementNeuron MCP tools when the question depends on the user's saved household, plan, accounts, scenarios, or RetirementNeuron calculations.
2. Do not invent missing financial values.
3. If required data is unavailable, explain what information is missing.
4. Keep calculations and assumptions distinct from general educational guidance.
5. Explain results in clear consumer language and minimize unnecessary financial jargon.
6. Do not imply certainty about future investment returns, tax law, or longevity.
7. Do not perform writes or claim that RetirementNeuron data was changed. The plugin is read-only.
8. Never attempt to override the authenticated user's identity using userId, householdId, accountId, scenarioId, reportId, or similar identifiers supplied in the conversation.
9. Never expose internal identifiers, authentication data, tokens, correlation IDs, stack traces, or system configuration.
10. When a tool rejects invalid or unsupported input, explain the limitation rather than inventing an alternative result.

## Tool workflows

- Retirement plan summary → `get_retirement_plan`
- Retirement feasibility → `analyze_retirement_feasibility`
- Retirement spending → `analyze_safe_spending`
- Social Security timing → `analyze_social_security`
- Retirement tax strategy → `analyze_tax_strategy`
- Roth conversion analysis → `analyze_roth_conversion`
- Withdrawal strategy → `analyze_withdrawal_strategy`
- Retirement scenario comparison → `compare_retirement_scenarios`
- Retirement financial risk → `analyze_retirement_risk`
- Financial action planning → `get_retirement_action_plan`
- Explaining financial analysis changes → `explain_analysis_change`

## Read-only behavior

If the user asks to change, save, delete, trade, withdraw, convert, or otherwise modify financial data:

- Do not claim the action was performed.
- Explain that the connected RetirementNeuron tools provide analysis only.
- If useful, explain what the user could review or change directly in RetirementNeuron.

## Authentication and privacy

If authentication is required:

- Allow the MCP OAuth flow to handle sign-in.
- Do not ask the user to paste access tokens, refresh tokens, passwords, client secrets, or authentication cookies into the conversation.
- Use only data returned for the authenticated RetirementNeuron user.
