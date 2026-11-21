---
name: estimate-payment
description: Calculate estimated monthly lease or finance payments for BMW vehicles
---

# Estimate BMW Payments

Help users understand monthly payment estimates for BMW vehicles.

## Available Tools

- `estimate-lease-payment` — Calculate monthly lease payment estimates
- `estimate-finance-payment` — Calculate monthly finance/loan payment estimates

## Information Needed

- **Vehicle price / MSRP** (required)
- **Down payment** (optional)
- **Trade-in value** (optional)
- **Term length** (optional, defaults vary)
- **Payment type**: Lease or finance (ask if not specified)

## Workflow

1. If the user has been looking at a vehicle or configuration, use that price automatically
2. Ask for down payment and preferred term if not provided
3. Calculate and present the payment estimate clearly
4. Offer to compare lease vs. finance if the user hasn't decided

## Tips

- Always clarify these are estimates, not binding offers
- Show both lease and finance options side by side when helpful
- Explain the key differences (lease: lower monthly, return at end; finance: higher monthly, you own it)
- Suggest visiting a dealer for exact pricing and credit-based rates
