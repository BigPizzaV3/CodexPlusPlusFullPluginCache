---
name: salary-benchmarks
description: Use SalaryAPI when the user wants a salary benchmark, compensation range, market median, percentile, gross-to-net salary estimate, take-home pay estimate, or remaining SalaryAPI search allowance.
---

# SalaryAPI salary tools

Use `search_salary_benchmark` for salary benchmark questions. Use `get_salary_quota` when the user asks about their allowance, plan, reset time, or whether several searches will fit.

Use `calculate_net_salary` when the user wants estimated take-home pay, gross-to-net salary, tax and payroll deductions, or annual, monthly, and hourly net pay for a supported country. Send the gross amount as `salary`, identify it as `annual` or `monthly` with `salaryPeriod`, and translate the country to an exact uppercase code from the tool schema. The amount must be in the selected country's calculator currency. If the gross amount or country is missing, or the supplied currency does not match the calculator currency, ask for the needed local-currency amount before calling the tool.

The chat calculator uses current default country assumptions. Do not silently ignore a requested tax year, filing status, dependents, region, pension setting, or other personal modifier. Explain that this tool cannot apply that override and ask whether the user wants the default estimate before calling it.

Users must sign in through the hosted flow opened by the SalaryAPI MCP connection. Use the sign-in method offered by that flow. If a tool returns an authentication challenge, ask the user to complete that flow and retry the same request. If the connection returns `account_link_required` before the tool runs, direct the user to the returned `accountUrl` and follow the returned account-linking instructions before retrying.

Salary benchmark requests share the account's website and chat allowance. The default allowance is 10 requests in the existing rolling 24-hour window. Connected accounts can have different allowances. Net salary calculations do not consume that search allowance or create search history. Do not imply that chat has a separate search pool.

Available percentiles depend on the connected account. When a tool returns `feature_not_available`, explain which option is unavailable without suggesting a purchase or account upgrade. When it returns `quota_exceeded` or `search_temporarily_paused`, show the supplied reset time and do not retry before that time. Do not add pricing or checkout links.

Treat salary results as annual gross base salary unless the tool result says otherwise. Do not describe bonuses, equity, or benefits as included when they are not.

For benchmark answers, include the returned percentile amount, currency, confidence label, and remaining search allowance. If no benchmark was found, say so without supplying a salary amount. For allowance questions, include the returned plan, remaining allowance, and reset time.

Treat net salary results as estimates. Explain the returned assumptions and country-specific deductions when useful, and do not present them as guaranteed payroll, tax, legal, or financial advice.

For benchmark searches, use only the advertised fields: `jobTitle`, `country`, `currency`, `seniority`, and `percentile`. Preserve the requested role, currency, seniority, and percentile using supported schema values. Use defaults only for options the user did not specify. When the user requests a country market, send its exact supported uppercase country code. The country is the public job market selected by the user, not the user's current location. Never put a person's name, resume content, private address, contact details, credentials, or other personal data into tool arguments.

Role-title inputs use Latin letters. When the user writes a role title in another script, translate it to the accurate Latin-script equivalent before calling the tool. Translate a requested country market to its exact supported uppercase code. Preserve the intended role, seniority, and job market.

Never describe or speculate about how SalaryAPI obtains, prepares, validates, stores, refreshes, or generates salary data. You may explain the inputs, returned fields, confidence label, coverage, no-result behavior, compensation scope, and user-facing limitations.

Prefer one precise search over broad batches. For comparisons, make only the country-level searches needed for the requested markets and stop if the tool reports that the allowance is exhausted.
