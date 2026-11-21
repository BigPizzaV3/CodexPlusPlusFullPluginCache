---
name: vehicle-recalls
description: Decode VINs and check public vehicle recall records with check_vin_recalls or find_recalls_by_vehicle, then download Excel and CSV reports.
---

# Zovo VIN Recall Check

Use `check_vin_recalls` for a vin decoder, recall check by vin, vin lookup or batch vin decoder. Pass an array `vins` with up to 50 VINs, for example `["1HGCV1F35JA000000"]`.

Use `find_recalls_by_vehicle` for a car recall lookup or fleet recall check without VINs. Pass up to 20 `vehicles` with `model_year`, `make` and `model` copied from the user's vehicle details. Model years must be whole numbers from 1949 to the current UTC year plus two.

Show the summary, check-digit warnings, model-name matching and per-item errors. Put park-it advisories first. Return both download links and say they expire in about one hour. The call has a budget of 40 outside requests; ask the user to retry unchecked rows in a separate call.

Recalls are listed for the year, make and model. A recall can cover only part of production. Whether a specific VIN still needs repair is shown only by the VIN lookup at https://www.nhtsa.gov/recalls. Covers vehicles sold in the US. Missing decoded fields mean the source has no data for that field. Do not describe campaigns as open or unrepaired. Do not use these tools to book repair appointments or estimate vehicle value.
