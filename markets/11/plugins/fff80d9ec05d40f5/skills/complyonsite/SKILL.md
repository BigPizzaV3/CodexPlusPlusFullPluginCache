---
name: complyonsite
description: Construction and waste questions that the ComplyOnSite tools answer directly. Use for EWC or List of Waste codes for a skip, load or material; waste codes for the US, California, Texas, Australia and Canada; filling in a waste transfer note; hazardous or special waste consignment notes and which paperwork a waste movement needs; RAMS for a job; daily hand-arm vibration (HAVS) or noise exposure from tools and times; first-aid cover for a site; how much a type of power tool vibrates or how loud it is; and HSE construction injury and death figures.
---

# ComplyOnSite tools

The `complyonsite` MCP server gives calculations and reference data for UK construction and waste work. It is anonymous and read-only.

## Which tool

| The person asks about | Tool |
|---|---|
| A UK code for a waste, skip, load or material; what a code means | `ewc_search` |
| A waste code in the US, California, Texas, Australia or Canada | `waste_code_search` |
| Filling in a waste transfer note from what the person has said | `fill_transfer_note` |
| Starting a consignment note or RAMS; a template or example | `start_document` |
| Which paperwork a waste movement needs, by nation or document | `waste_paperwork` |
| Vibration exposure for one person from tools and times | `havs_daily_exposure` |
| Noise exposure from task levels and times, or a dosemeter | `noise_daily_exposure` |
| How many first-aiders or what course for a site or workplace | `first_aid_requirements` |
| How much a type of tool vibrates or how loud it is | `power_tool_types` |
| Construction deaths, injuries or ill health in Great Britain | `construction_injury_statistics` |
| A job on a file or kept record: SDS to Excel, checking a Receipt of Waste workbook, a Defra report, reviewing a RAMS, paper form to phone form, site diary, register or issues | `site_tools` |

## How to use them

- Waste codes: search one to three material words at a time (“plasterboard”, “treated wood”), not the person's sentence. Search each material in a mixed load separately. If `match.quality` is `weak` or `none`, try the main material or a synonym rather than guessing.
- Transfer notes: find the codes with `ewc_search`, then call `fill_transfer_note` with the codes and every detail the person has given. Never invent a name, address, date or registration number; leave it out and the card asks for it. A mirror entry needs an assessment before choosing between the hazardous and non-hazardous code; say so. The person makes the waste hierarchy and mirror statements on the note themselves.
- Hazardous loads: pass the codes to `start_document` for a consignment note.
- HAVS: give each tool an HSE `category` (and `variant` where the category has several) when the person has no vibration figure. Use the tool's own m/s² figure when they have one. Time is trigger time.
- Noise: task levels are LAeq in dB(A). For noise at the ear, add the protector's SNR or H/M/L and each protected task's C-weighted level.
- Noise thresholds are two separate checks. The 80 and 85 dB(A) action values compare noise before hearing protection (`levels`); the 87 dB(A) limit compares noise at the ear, after protection (`limitCheck`). Never list 87 as a third step after 80 and 85.
- Not covered: live register checks (waste carrier, broker or dealer registration, permits, exemptions) and submitting anything to a regulator. Say so first, without asking for details, and point to the regulator's public register or service. The server does not read files; for file work, `site_tools` gives the website tool.
- If an answer depends on something the person has not said (the nation, how many people per shift, trigger time), make a sensible assumption, state it, and ask.

## Presenting answers

- Each result starts with a `summary`. Give the figure or code first, in plain words, then what it means for the person.
- Where the host shows the result card, the person already sees its figures, thresholds and buttons, and can change times, headcounts, ticked codes and note details in it. Don't repeat them as prose or a table; add only what the card doesn't show, such as the next step for their situation.
- Results include `calculatorUrl`, `url` or `downloads`. Show them as links: the calculator opens the same calculation to adjust; `start_document` links open the form with the codes or job filled in; `downloads` are a blank template and a worked example as PDFs.
- Keep each result's `limit` in the answer when it matters, for example that a code search is not a waste classification.
