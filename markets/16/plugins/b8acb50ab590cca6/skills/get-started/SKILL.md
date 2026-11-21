---
name: get-started
description: Use MamaTool's tools inside ChatGPT — count words, make QR codes, generate passwords, format JSON, calculate loan EMI.
---

# Getting started with MamaTool

MamaTool is 50+ tools that run in the browser at https://mamatool.com — no
sign-up, no uploads, no API keys. This plugin exposes five of them as tools.
Everything is computed by the plugin server and nothing the user types is stored.

## When to use which tool

- The user pastes text and asks how long it is, how many words or characters it
  has, or how long it takes to read: use `count_words`.
- The user wants a QR code for a website, link or short text: use
  `generate_qr_code`. Ask what size they want only if they care; the default
  256 px is fine for screens.
- The user wants a password: use `generate_password`. Default 16 characters
  with all character sets. Never invent a password by writing one out yourself
  — always call the tool so it is cryptographically random.
- The user pastes JSON and wants it formatted, validated or checked: use
  `format_json`. If the JSON is invalid, report the exact error the tool
  returns instead of guessing a fix.
- The user asks for a loan EMI, monthly payment, total interest or total
  payment: use `calculate_emi` with the principal, annual interest rate and
  tenure in months.

## Rules

- All five tools are read-only. There is no tool that stores, sends, deletes or
  changes anything — if the user asks for that, say so plainly and offer the
  matching tool on https://mamatool.com instead.
- Never ask the user to sign in or share an API key. MamaTool has no accounts.
- If a tool returns an error, show the error message as-is and ask the user for
  corrected input.
