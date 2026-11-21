---
name: gpa-calculator
description: Calculate exact unweighted, weighted, and cumulative GPA from letter or percentage grades and credits, plan the GPA needed to reach a target, and find the final exam score needed for a course grade.
---

# Zovo GPA Calc

Pick the tool from the question:

- **calculate_gpa**: the user lists courses with grades ("A in Bio 4 credits, B+ in Calc 3"). Pass every course with `grade` (letter A+ to F, a percentage as "91%", grade points such as 3.7, or P/NP/W), `credits`, and `level` (regular, honors, ap, ib, dual) when the user mentions it. Add `previous_gpa` and `previous_credits` for a cumulative GPA.
- **plan_target_gpa**: "what GPA do I need next semester to reach 3.5?" Needs current GPA, credits completed, target GPA, and upcoming credits.
- **final_grade_needed**: "what do I need on the final?" Needs current grade %, final weight %, and desired grade %.

Scale settings: the default is the standard 4.0 scale with A+ = 4.0, honors +0.5, and AP/IB/dual +1.0. Schools differ, so pass `a_plus_points: 4.3`, `weights`, `percent_cutoffs`, or `grade_points` whenever the user mentions their school's rules. When the user gives the grades, call the tool right away instead of asking first. If credits are not given, use 1 credit per class (equal weighting) and say so; if the term's credit total for a target is missing, ask for it.

After the tool returns, give the headline number first (2 decimals), then the most useful detail: the biggest what-if lever, whether a target is impossible, or the score needed for each letter. Do not round impossible results down to look reachable.

Do not use these tools for admissions predictions, essay writing, study tips, explaining what a GPA is in general, or choosing a major.
