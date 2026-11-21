---
name: life-insurance-quick-quote
description: Use for a new Amore Insurance term life insurance quote, premium estimate, or eligibility range. Do not use for other insurance products, policy servicing, or general insurance education.
---

# Life insurance quick quote

Help the user obtain a new term life insurance quote through the Amore MCP server. Use the connected tools for all eligibility limits, province codes, and quote results.

1. Collect the applicant's first name, date of birth (`yyyy-MM-dd`), sex (`Male` or `Female`, as accepted by the tool), province, and smoking status. Ask for missing details conversationally. Ask for smoking status explicitly; an omitted value defaults to `false` in the tool, which may produce an inaccurate quote.
2. Call `get_state_provinces` to match the province to an available `code`. If there is no clear match, ask the user to clarify. Do not invent a code.
3. Call `get_quick_quote_limits` with the date of birth before offering policy term or benefit choices. If `isEligible` is false, relay the returned `message` and stop.
4. Ask for the desired `policyTermYears` and `benefitAmount`, using the returned minimum and maximum values. If either is outside the range, ask for a valid value. Do not assume a term or amount.
5. Once the user has supplied all inputs, call `create_quick_quote` once. If the tool returns an error, relay its message accurately and stop. Do not retry a creation call blindly, because it may have created a quote before the error appeared.
6. On success, report `totalPremium` exactly as returned and provide `quoteUrl` as the link to continue the application. Do not guess the currency, payment frequency, policy approval status, or any missing result field.

This workflow only handles new term life insurance quotes. For other products, policy servicing, or general educational questions, answer within your normal capabilities without using these quote tools.
