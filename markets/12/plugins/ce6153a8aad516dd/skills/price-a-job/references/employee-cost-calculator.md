# True Cost of an Employee Calculator

Answers: What does an employee really cost me, beyond their salary?
Learn more: https://omnyra.ai/wiki/business/labor-cost

## Inputs

| Input | Unit | Default | What it means |
|---|---|---|---|
| Annual base salary | $ a year | none, ask for it | The employee's yearly pay before anything else is added. For an hourly employee, the hourly wage x 2,080. |
| Employer payroll tax rate | % | 7.65% | The employer's payroll taxes as a percentage of salary. |
| Health insurance | $ a year | $7,000 | What the employer pays toward this employee's health cover in a year. |
| Retirement match | % | 3% | The employer's retirement contribution as a percentage of salary. |
| Workers' compensation rate | % | 1.5% | Workers' compensation insurance as a percentage of salary. It varies a great deal by trade. |
| Overhead per employee | $ a year | $5,000 | Desk, equipment, software, phone, vehicle, training: what one more person adds in a year. |
| Paid days off | days a year | 15 | Vacation, holidays and sick days that are paid. |

## Before you calculate

- Annual base salary must be above 0.

## Formula

1. Payroll taxes = base salary x payroll tax rate / 100
2. Retirement match = base salary x retirement match / 100
3. Workers' compensation = base salary x workers' compensation rate / 100
4. Cost of paid days off = base salary / 260 x paid days off. 260 is the working days in a year.
5. True annual cost = base salary + payroll taxes + health insurance + retirement match + workers' compensation + overhead per employee + cost of paid days off
6. True hourly cost = true annual cost / 2,080. 2,080 is 40 hours x 52 weeks.
7. Multiplier = true annual cost / base salary

## Rounding

Give the multiplier and the hourly cost to two decimal places and other dollars to the nearest whole dollar. The Playbook's own calculator shows the hourly cost rounded to the whole dollar.

## Worked example

Inputs: Annual base salary $60,000; Employer payroll tax rate 7.65%; Health insurance $7,000; Retirement match 3%; Workers' compensation rate 1.5%; Overhead per employee $5,000; Paid days off 15.

1. Payroll taxes = $60,000 x 7.65 / 100 = $4,590
2. Retirement match = $60,000 x 3 / 100 = $1,800
3. Workers' compensation = $60,000 x 1.5 / 100 = $900
4. Cost of paid days off = $60,000 / 260 x 15 = $3,462
5. True annual cost = $60,000 + $4,590 + $7,000 + $1,800 + $900 + $5,000 + $3,462 = $82,752
6. True hourly cost = $82,752 / 2,080 = $39.78
7. Multiplier = $82,752 / $60,000 = 1.38x

Result for these inputs:

- True annual cost: $82,752
- Multiplier on salary: 1.38x
- True hourly cost: $39.78
- True monthly cost: $6,896
- Payroll taxes: $4,590
- Retirement match: $1,800
- Workers' compensation: $900
- Cost of paid days off: $3,462

Rule of thumb for this result: Moderate, review the benefits.

## The Playbook's rule of thumb

- The multiplier is under 1.3: **Normal employer costs.** The costs on top of salary are well controlled. As a rule of thumb the employee should bring in two to three times this true annual cost in revenue.
- The multiplier is 1.3 to 1.5: **Moderate, review the benefits.** Benefits and overhead are above average, which is common where insurance or equipment is expensive. Check that each cost earns its keep in retention and output. The employee needs to bring in at least twice this true annual cost in revenue.
- The multiplier is over 1.5: **High, audit the costs.** The employer pays half the salary again or more on top of it. Check the workers' compensation rate, the health plan and the overhead per person, and whether equipment or software can be shared. At this level the employee needs to bring in about three times the true annual cost in revenue.

## Notes

- The cost of paid days off is counted on top of salary, as the Playbook's own calculator counts it: it is the pay for days when no work is produced.
- The defaults are starting points. Ask for the owner's own figures where they have them, the workers' compensation rate above all.
- To charge for this employee's time, the true hourly cost is the floor before overhead and profit, and it assumes every one of the 2,080 hours is billed.
