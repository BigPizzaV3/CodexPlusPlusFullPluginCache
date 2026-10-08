---
name: goc-creation-skill
description: Create GOC maintenance-notification CSV files from a maintenance Excel extract and matching Jira Stories. Use when preparing weekly or monthly GOC CX notification imports, filtering maintenance windows, matching environment names to Jira Story summaries, or producing the standard GOC CSV format.
---

# GOC Creation Skill

Create a CSV for GOC maintenance-notification tickets from the Pineapple GOC creation report and matching Jira Stories.

## Source report

1. Use **Edge** and open the Pineapple Maintenance Summary Report: `https://apex.oraclecorp.com/pls/apex/f?p=23830:115:108786578130065:::::`.
2. Select the saved **GOC creation report** view. This is the required first step and the base extract for every run.
3. Ask the person running the skill for the scheduled start and end dates. Set `Vertical` to `HOTEL` and set that date range, then download the report as Excel. Leave `Region` on `- All Regions -`; never apply a region filter. Use that extract for the remaining workflow.

## Inputs

- A maintenance Excel extract with columns including `Environment Name`, `Scheduled Start`, `Scheduled End`, `Status`, `Datacenter`, `Work Summary`, `Create GOC CX`, and `Maintenanceactivity`.
- Jira Stories for the relevant reporting period.
- A previous GOC CX CSV when its exact column order or fixed values must be matched.

## Workflow

1. Inspect the GOC creation report extract and the reference CSV before creating an output. Preserve the reference CSV's exact 12-column order, UTF-8 BOM encoding, and fixed values.
2. Keep only rows where `Create GOC CX` is `Y`.
3. Keep only windows whose status is `TPM Coordination`, `To Be Scheduled`, or `Scheduled`.
4. Exclude rows whose activity or work summary indicates:
   - CNE upgrades
   - DOM0 or DOMU patching
   - OKV or OKV endpoint patching
   - work marked `reserved for upgrades` or `reserve for upgrades`
   - migration activities
   - capacity expansions
   - `Capacity Expansion E4 to E5 (OL7>OL8)`
   - `HCMS_MIGRATION`
   - `VMDB OS Patching`
5. Match each remaining `Environment Name` exactly to a Jira Story `Summary`, as a VLOOKUP-style join. Use the Jira Story key as `Master Ticket`. Do not guess a ticket key when no exact Story match exists. Keep that eligible APEX row out of the import CSV, but add it to a clearly labelled **Missing Jira Stories** exceptions file or list, with its environment name, scheduled time, and status, so the report owner can create the Story and rerun the match.
6. Generate one CSV row per included environment using these columns in this order:

   `Product ID`, `Category ID`, `CI Cost Center`, `CI Name`, `CI Type`, `CI Environment Type`, `CI Location`, `CI Line of Business`, `Subject`, `Description`, `Contact ID`, `Intended Assign Group`.

7. Follow the approved sample's conventions:
   - Set `Product ID` to `1232`, `Category ID` to `738`, `CI Cost Center` to `HGBU`, `CI Type` to `Business service`, and `CI Line of Business` to `Opera Cloud`.
   - Set `Contact ID` according to the report owner: Andrea `8962`, Raluca `8961`, or Mumtaz `9338`. Ask which owner is preparing the report if it is not clear. Leave `Intended Assign Group` blank.
   - `CI Name`: environment name.
   - `CI Environment Type`: use the tier token from `Environment Name`. For the approved GOC template, write `PROD` for names containing `PROD` and `UAT` for names containing `UAT`; do not convert these to `Production` or `Test`.
   - `CI Location`: copy the source APEX `Datacenter` value.
   - `Subject`: `Send Maintenance Notification: Please send notification for <environment> - Maintenance START TIME: <dd/mm/yyyy HH:MM>`.
   - `Description`: subject text, then `Maintenance END TIME: <dd/mm/weekday HH:MM>`, `Master Ticket: <Jira Story key>`, and `GDCP Customer Name: <environment>`, each on its own line.
   - Use these fixed values unless the user gives updated values.
8. **Before providing the final report**, independently compare the completed CSV against the supplied GOC template. Confirm the UTF-8 BOM, exact 12-column order, fixed values, permitted `PROD`/`UAT` labels, APEX datacenter locations, Contact ID, and four-line Subject/Description pattern. Also confirm one row per included source record, parsable CSV quoting, exact Jira joins, and no excluded or unmatched rows. Correct any mismatch and repeat this comparison before delivery.

## Handling gaps

- Never silently drop an eligible APEX row because its Jira Story is missing. Keep it out of the import CSV until there is an exact Story-summary match, but flag it in a **Missing Jira Stories** exceptions file or list for the report owner; never invent a master ticket.
- If the input CSV sample conflicts with the stated filtering rules, follow the user's latest stated rules and explicitly flag the difference.
- Ask for clarification when a work summary is ambiguous or when a new status should be included.
