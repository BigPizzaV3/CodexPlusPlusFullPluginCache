# Example Workflows for EduOpus Principal MCP

This document illustrates multi-step tool coordination workflows for common School Principal scenarios.

---

## Example 1: Resolving Class Name & Fetching Class Attendance

**User Prompt**: *"How is attendance today for 5th grade?"*

1. **Step 1 — Class Resolution**:
   - Model analyzes `"5th grade"`.
   - Model calls `get_attendance_summary(date: "2026-09-04")` to check active class keys and overall rates.
   - Matches `"5th grade"` -> Class name `"5"`.

2. **Step 2 — Targeted Attendance Query**:
   - Model calls `get_attendance_summary(date: "2026-09-04", class_id: "60f917e2-fc6d-40fa-b962-4511efd8bd6b")`.

3. **Step 3 — Presentation**:
   - Model presents total students, present count, absent list, and overall percentage cleanly.

---

## Example 2: Student Disambiguation Flow

**User Prompt**: *"Show me the fee breakdown for Aarav."*

1. **Step 1 — Search Query**:
   - Model calls `get_student_details(query: "Aarav")`.

2. **Step 2 — Handling Multiple Matches**:
   - Tool returns 2 candidate matches:
     - `Aarav Sharma` (`STU-101`, Class 5)
     - `Aarav Verma` (`STU-204`, Class 8A)
   - Model prompts user:
     > *"Found 2 students named Aarav in your school:*
     > *1. **Aarav Sharma** (Class 5, ID: STU-101)*
     > *2. **Aarav Verma** (Class 8A, ID: STU-204)*
     > *Which student would you like the fee breakdown for?"*

3. **Step 3 — User selects #1**:
   - Model calls `get_student_details(query: "STU-101", include_payment_history: true)`.

---

## Example 3: Two-Phase Bulk Student Import with Dry Run

**User Prompt**: *"Import these 3 students into Class 10A..."*

1. **Step 1 — Phase 1 (Dry Run)**:
   - Model calls `bulk_import_students(students: [...], dry_run: true)`.
   - Tool responds with:
     - `valid_count: 3`
     - `invalid_count: 0`
     - `duplicate_warnings: []`
     - `confirmation_token: "a9f4c3..."`

2. **Step 2 — Confirmation Gate**:
   - Model shows preview table:
     - Student 1: Amit Kumar | Guardian: Raj Kumar | Fee: ₹2,500/mo
     - Student 2: Priya Singh | Guardian: Anil Singh | Fee: ₹2,500/mo
     - Student 3: Rohit Verma | Guardian: S. Verma | Fee: ₹2,500/mo
   - Model asks: *"All 3 records passed validation. Should I proceed with committing these to Class 10A?"*

3. **Step 3 — Phase 2 (Execution)**:
   - Upon user confirmation (*"Yes"*), model calls:
     `bulk_import_students(students: [...], dry_run: false, confirmation_token: "a9f4c3...")`.
   - Model confirms successful creation with new student IDs.
