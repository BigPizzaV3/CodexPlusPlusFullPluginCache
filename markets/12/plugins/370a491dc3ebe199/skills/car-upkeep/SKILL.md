---
name: car-upkeep
description: Log a car's mileage or fuel and report upcoming services, documents and repairs in FamilyWell Vehicles.
---

Call `vehicles_list` to find the car the user means (by name, make or plate). To record the odometer, call `vehicles_log_mileage` in km; for a fill-up, call `vehicles_log_fuel`. A photo of the dashboard is enough: read the odometer from it and confirm the number with the user if it is unclear.

After logging, call `vehicles_get` and report anything overdue first, then the next service by distance or date. To mark a service done, call `vehicles_complete_maintenance`.

Distances are in kilometres. Confirm in one or two sentences; do not show ids.
