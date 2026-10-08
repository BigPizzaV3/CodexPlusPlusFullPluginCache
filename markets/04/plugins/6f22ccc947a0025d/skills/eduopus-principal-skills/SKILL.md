---
name: eduopus-principal-skills
description: Operational guidelines, tool coordination patterns, fuzzy entity resolution, disambiguation rules, and safety protocols for the EduOpus School Principal MCP tool suite.
---

# EduOpus Principal MCP Skill Guide

This skill guides OpenAI models on how to safely, accurately, and effectively orchestrate the **EduOpus School Principal MCP Tool Suite**. All tools operate with strict Row Level Security (RLS) under the authenticated Principal's school context.

---

## 1. Class Name Resolution Protocol

### The Challenge
School class names in databases often differ in formatting from natural user phrasing (e.g., a class named `"5"` or `"Class 10A"` vs. user input `"5th"`, `"grade 5"`, `"Grade 10-A"`).

### Protocol
1. **Never Guess or Require Exact Case/Punctuation**:
   - Before calling tools like `get_class_roster`, `get_fee_status`, `mark_attendance`, `create_homework_assignment`, or `add_student`, check the school's active classes using `get_school_overview` or `get_attendance_summary`.
2. **Apply Fuzzy Token Matching**:
   - Normalize numerical suffixes (`"1st" -> "1"`, `"5th" -> "5"`, `"12th" -> "12"`).
   - Strip redundant prefixes (`"Class 10A"` matches `"10A"`, `"Grade 10 A"`, or `"10-A"`).
3. **Handle Ambiguity / No Confident Match**:
   - If user input does not cleanly resolve to a single class in the school's roster, **do not fail silently or guess**.
   - List the active classes currently registered in the school and politely ask the principal:
     > *"I couldn't find a class matching '7th B'. Here are the active classes in your school: [Class 7A, Class 7, Class 8A]. Which one did you mean?"*

---

## 2. Student Disambiguation Protocol

### The Challenge
Multiple students across different classes (or within the same class) may share similar or identical names (e.g., *"Rahul Sharma"*). However, asking for confirmation when the user was already specific creates unnecessary friction.

### Protocol
1. **Pre-Query Context Narrowing (One-Shot Resolution)**:
   - Before calling `get_student_details` with just a raw name, check if the user's prompt or conversation history already contains narrowing context (e.g., a class name, a grade like *"in 5th"*, or a section mentioned earlier).
   - If narrowing context exists, pass it immediately as the `class_name` parameter on the very first tool call. Genuinely specific requests (e.g., *"Show fee details for Aarav in Class 5"*) will resolve in one shot without ever triggering `multiple_matches_found`.
2. **Conversational Entity Continuity (Follow-Up Actions)**:
   - If a student was already confirmed/selected earlier in the same conversation and the user's next message clearly continues referring to the same student (e.g., *"also mark her present today"*, *"what about his pending fee receipts?"*), **reuse that same `student_identifier` directly** without re-asking.
3. **Ambiguity Resolution (When True Ambiguity Exists)**:
   - If `get_student_details` or student search tools return `multiple_matches_found: true` (or a candidate list without enough context to distinguish):
     - **Never auto-select or guess the first match.**
     - Present the disambiguation list clearly with:
       - **Full Name**
       - **Class / Section**
       - **Student Identifier** (e.g., `STU-1767344857114`)
       - **Guardian Name**
     - Ask the principal to clarify which student they mean before executing further actions.
4. **Core Rule**:
   - Disambiguation should only ever interrupt the conversational flow when the AI genuinely cannot tell which student is meant — never as a redundant blanket confirmation step.

---

## 3. Dynamic Fee Status Interpretation

### The Challenge
EduOpus calculates fee balances dynamically using time-based elapsed billing cycles from the student's `joining_date`, rather than static ledger balances.

### Protocol
1. **Live Data Over Previous Chat Memory**:
   - Always query `get_fee_status` fresh. Never rely on numbers from earlier conversational turns.
2. **Interpret Accruals Accurately**:
   - A student showing `remaining_fee: 0` in an earlier month may now have an active pending balance if a new monthly billing cycle has started.
3. **Explain Clearly**:
   - When presenting fee reports to the principal, distinguish between:
     - **Total Expected Fees** (annual/monthly accrued)
     - **Collected Fees** (paid to date)
     - **Remaining / Overdue Fees** (currently outstanding)
     - **Net Profit / Settlement Metrics** (if school-wide totals are requested)

---

## 4. Write Action Confirmation & Dry-Run Protocols

### The Challenge
Modifying school records (attendance, student profiles, homework assignments) directly impacts students, teachers, and parents.

### Protocol
Before invoking any of the 6 write tools:
- `mark_attendance`
- `add_student`
- `update_student`
- `bulk_import_students`
- `create_homework_assignment`
- `review_homework_submission`

### Required Workflow:
1. **Plain-Language Summary & Confirmation**:
   - State exactly what changes will be recorded (target class, dates, names, updated values).
   - Require explicit user affirmation (*"Yes, proceed"*) before sending the execution tool call.
2. **Special Rule for `bulk_import_students`**:
   - **Phase 1 (Mandatory Dry-Run)**: Always invoke `bulk_import_students` with `dry_run: true` first.
   - Present the preview table: total valid records, detected duplicates/conflicts, and the `confirmation_token`.
   - **Phase 2 (Commit)**: Only after the principal reviews and confirms the preview, call `bulk_import_students` with `dry_run: false` and the returned `confirmation_token`.
3. **Attendance Overwrites**:
   - If `mark_attendance` indicates an existing record was overwritten (e.g., modifying a status previously marked by a teacher), highlight the diff clearly to the principal.

---

## 5. Privacy by Default (PII Protection)

### The Challenge
Student records contain sensitive personal identifiable information (PII) including guardian mobile numbers, parent emails, and home addresses.

### Protocol
1. **Opt-In Visibility**:
   - By default, keep `include_contact_info: false` when calling `get_student_details` or `get_class_roster`.
2. **Strict Need-to-Know Exposure**:
   - Never surface `guardian_phone`, `parent_email`, or home addresses in chat responses unless the principal's explicit prompt requested contact details (e.g., *"Show me Aarav's father's phone number"* or *"Send me parent contact sheet for Class 10"*).
3. **Settlements & Financial Privacy**:
   - Bank accounts are automatically masked (e.g., `••••••••1234`). Never attempt to unmask or query raw account numbers.

---

## Quick Tool Reference Matrix

| Tool Name | Type | Key Purpose | Safety / Confirmation Required |
| :--- | :--- | :--- | :--- |
| `get_school_overview` | Read | School-level KPI metrics & totals | None (Instant Read) |
| `get_fee_status` | Read | Live fee collections & overdue balances | None (Instant Read) |
| `get_attendance_summary`| Read | Attendance percentages & stats | None (Instant Read) |
| `get_class_roster` | Read | Class student roster & enrollment dates| None (PII hidden by default) |
| `get_student_details` | Read | Detailed single-student profile | Disambiguate if duplicate names |
| `get_staff_roster` | Read | Teacher & employee listings | None (Instant Read) |
| `get_homework_overview` | Read | Class homework review metrics | None (Instant Read) |
| `get_settlement_status` | Read | Payout batches & masked bank UTRs | None (Read-only) |
| `get_school_gallery` | Read | School activity media & moments | None (Instant Read) |
| `create_homework_assignment` | Write | Post new homework assignment | Summarize & Confirm |
| `update_homework_assignment` | Write | Edit homework instructions/deadline | Summarize & Confirm |
| `review_homework_submission` | Write | Record submission status & remarks | Summarize & Confirm |
| `mark_attendance` | Write | Record/overwrite daily attendance | Summarize & Confirm (Highlight diffs)|
| `add_student` | Write | Register new student & fee plan | Summarize & Confirm |
| `update_student` | Write | Edit academic profile details | Summarize & Confirm |
| `bulk_import_students` | Write | Import student batches | **Mandatory Dry-Run Preview First** |
