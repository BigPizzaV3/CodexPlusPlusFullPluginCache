# HR policy option values

The values `preview_hr_policy` accepts. They are exactly what the HR Policy Studio offers. Anything else is rejected.

| Field | Allowed values |
|---|---|
| `workingDays` | `26 Days (Monday to Saturday)`, `26 Days (Business is Operational all 30 Days)`, `22 Days (Weekend Off)`, `Custom` (then also `customWorkingDays`, 1 to 30) |
| `workOnWeekOffOption` | `comp-off`, `paid-month-end` |
| `clEligibility` | `paid-leave`, `Based on CLC` |
| `paidLeaveUnusedHandling` | `carry-forward`, `paid-month-end` (only with `paid-leave`) |
| `carryForwardDays` | whole number 1 to 60 (only with `carry-forward`) |
| `paidLeaveYearEndBasis` | `india-fy`, `australia-fy`, `us-fy`, `uk-fy`, `gulf-calendar`, `singapore-calendar`, `malaysia-calendar`, `hong-kong-fy`, `japan-fy`, `china-calendar`, `calendar`, `custom` (then `paidLeaveYearEndCustom`, like `31 December`) |
| `customLeaveTypes[]` | `name`, `days`, `period` (`yearly`, `monthly`, `per-instance`), `paid` (true or false); up to 10 |
| `holidayReward` | `1 Day Salary`, `1.5 Days Salary`, `2 Days Salary` (`foodAllowance` only with this) |
| `reportingTime` | `single-time` (then `customTime`, like `9:30 AM`), `multi-shifts` (then `shifts`, up to 6 times) |
| `shiftDurationType` | `single` (then `shiftDurationHours`), `multiple` (then `shiftDurations`, the first is the default) |
| shift hours | `4`, `5`, `6`, `7`, `7.5`, `8`, `8.5`, `9`, `10`, `11`, `12` |
| `lunchBreakMinutes` | `30`, `40`, `50`, `60` |
| `autoHalfDayThresholdHours` | 1 to 6 in steps of 0.5 (needs `enableAutoHalfDay`) |
| `otCalculation` | `Not Applicable`, `As per Salary (Pockets of 30 Mins)`, `Perks or Benefits` |
| `probationPeriod` | `1 to 3 Months`, `3 to 6 Months` |
| `noticePeriodType` | `single` (then `singleNoticePeriod`), `multiple` (then `labourNoticePeriod`, `staffNoticePeriod`, `coreNoticePeriod`) |
| `noticePeriodUnit` | `days`, `weeks`, `months` (default `months`) |
| `benefits[]` | `PA Cover (Personal Accident Cover)`, `Health Insurance as per CLC`, `CLC (Career Ladder Chart)`, `Training & Development`, `Refreshments`, `Annual Bonus`, `Performance Incentives` |
| `safetyMeasures[]` | `CCTV Surveillance`, `Good Work Environment`, `Safety Equipment` |
| `memos` | `Will be Given` |
| `month` | `January` to `December` |
| `year` | four-digit year as text, 2000 to 2099, like `2026` |

Free text (up to 500 characters each): `customNotes_workingDays`, `customNotes_leavePolicy`, `customNotes_timingPermissions`, `customNotes_salaryCalculations`, `customNotes_incentives`, `customNotes_guidelinesBenefits`. `deductions` is free text up to 300 characters, like `ESI and PF as per Indian law`.

Yes/no switches: `clawbackOnExit`, `unapprovedLeavesClause`, `enableLateToPermission`, `enableAutoHalfDay`, `enableLeaveViaCheckin`, `enableSlashCommands`, `performanceIncentives`, `enableBusinessCommunication`, `enableWorkplaceCelebration`, `enableCompanyPolicies`.

Not accepted (they come from the company's live settings): logo, weekly offs, holidays, leave allowance days, permission hours, per-day salary method.
