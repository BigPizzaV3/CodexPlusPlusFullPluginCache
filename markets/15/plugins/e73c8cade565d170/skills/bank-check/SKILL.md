---
name: bank-check
description: Look up US banks in FDIC records with find_bank and bank_history, and estimate insured and uninsured deposits with estimate_deposit_coverage.
---

# Zovo Bank Insurance Check

Use `find_bank` when the user asks whether a bank is FDIC insured or needs its FDIC certificate number, regulator, assets or website. Pass `name` (for example "Wells Fargo"), optionally `state` (two letters) and `city`, or `cert` when known. Set `include_inactive: true` for closed, failed or merged banks.

Use `bank_history` with one `cert` for a bank's failures, mergers and successor bank.

Use `estimate_deposit_coverage` when the user wants to know how much of their deposits are insured. Pass `accounts`, each with `cert`, `category` (single, joint, retirement, trust, business, employee_benefit_plan, government) and `balance` in US dollars. For joint accounts pass `owners` with 2 to 10 labels such as ["you", "spouse"]; use the same label for the same person across accounts. For trust accounts pass `beneficiaries`. If the user gives only a bank name, call `find_bank` first to get the certificate number.

Show the insured and uninsured totals first, then each bank and category. Say that the result is an estimate and give the FDIC EDIE link. Give the download links and say they expire in about one hour. Quote the FDIC source and retrieval time. FDIC limits apply per chartered bank (certificate number), not per brand. Do not use these tools for credit unions, interest rates or opening accounts.
