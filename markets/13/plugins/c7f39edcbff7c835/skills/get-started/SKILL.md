---
name: get-started
description: Set up Dubai Car Index after installation, check its connection when requested, and help the user try a first Dubai car-price question. Use for get started, onboarding, setup, connection checks, or questions about what the plugin covers.
---

# Get started with Dubai Car Index

Explain the plugin in a few sentences, then offer one concrete question to try.
Explicit user instructions take priority over this guidance.

## Choose the requested path

- For "set up", "get started" or "is it connected", call `whoami` once if
  available and report only the returned scopes. `mcp:read` confirms access.
- If tools are unavailable or authentication fails, say the connection is not
  verified and direct the user to connect or reconnect in the host. Do not
  claim the plugin is ready merely because this skill is present.
- If the user already asked a car-price question, answer it with the tools
  instead of suggesting that same question.

## What to say

- Dubai Car Index publishes what a car in Dubai should cost: UAE new-car list
  prices by trim, used values by model year and mileage, a fair-price check
  for an asking price, rental rates by day, week and month, and dealer versus
  independent garage repair costs.
- Every list price links to its source and the date it was checked. Used
  values, rental rates and repair bands are modelled from those prices and
  published quotes, and are labelled as such.
- Every tool reads published data. Nothing is bought, booked or sent anywhere.

## What it cannot do

It covers the UAE only. It does not value a specific car's condition or
accident history, quote insurance or finance, or buy, sell or book anything.

## Suggested first questions

- "Is AED 165,000 a fair price for a 2021 Toyota Land Cruiser with 80,000 km?"
- "Which SUVs can I buy new in Dubai for under AED 150,000?"
- "What does a Mercedes-Benz major service cost at the dealer versus an independent garage?"

Do not quote a figure from memory; figures come only from tool results.
