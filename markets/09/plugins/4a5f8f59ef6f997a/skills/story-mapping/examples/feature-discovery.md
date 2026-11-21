# Example: Feature Discovery — Bulk Import

A discovery board for exploring a "Bulk Import" feature, focusing on surfacing unknowns and mapping different user scenarios before committing to build.

## Board Structure

**Board name:** "Bulk Import Discovery"
**Board description:** "Exploring how users import data from external tools — scenarios, risks, and open questions"

### Journeys (left to right)

1. **Import from CSV** — File-based import for structured data
2. **Import from Competitor** — Direct integration with competitor APIs
3. **Import via API** — Programmatic import for technical users

### No milestones

This is a discovery board — milestones will be added once the team decides what to build and in what order.

---

## Detailed Structure

### Journey: Import from CSV

#### Step: Prepare File

- (question) "What CSV formats and encodings do we support?"
- (knowledge_gap) "What do users' actual export files look like? Need samples."
- (risk) "Users may have malformed CSV files — need robust error handling"
- (none) "Document supported CSV schema"

#### Step: Upload and Map Fields

- (objective) "User can map their columns to our fields in under 1 minute"
- (none) "Drag-and-drop file upload"
- (none) "Auto-detect column mapping with manual override"
- (question) "Do we support partial imports (some rows fail, others succeed)?"
- (risk) "Large files (>100MB) may time out on upload"

#### Step: Review and Confirm

- (objective) "User has confidence import will work before committing"
- (none) "Preview first 10 rows with mapped data"
- (none) "Validation summary showing errors and warnings"
- (none) "Dry-run option that validates without importing"
- (learn) "Competitor X shows a diff view — users reported this as their favorite feature (G2 reviews)"

### Journey: Import from Competitor

#### Step: Authenticate

- (knowledge_gap) "Which competitors expose export APIs? Need to audit top 5."
- (risk) "Competitor APIs may change without notice"
- (none) "OAuth connection flow for supported competitors"
- (question) "Do we store competitor credentials or use one-time tokens?"

#### Step: Select and Import

- (objective) "User imports their existing workspace structure, not just flat data"
- (none) "Show preview of data structure from competitor"
- (none) "Let user select which projects/items to import"
- (risk) "Data model mismatch — competitor concepts may not map 1:1"
- (question) "How do we handle data types that don't exist in our product?"

#### Step: Post-Import Cleanup

- (none) "Import summary with success/skip/error counts"
- (none) "Suggested cleanup actions for unmapped data"
- (learn) "Users expect import to preserve their organizational structure, not just individual items (from 8 user interviews)"

### Journey: Import via API

#### Step: API Design

- (objective) "Developer can build an import integration in under 1 hour"
- (knowledge_gap) "What import API patterns do developers expect? REST? GraphQL? Webhook?"
- (none) "Design bulk import API endpoint"
- (none) "Rate limiting and batch size documentation"
- (question) "Do we need a webhook for async import completion?"

#### Step: Developer Experience

- (none) "API reference documentation with examples"
- (none) "Import SDK or code samples in 3 languages"
- (risk) "Without good error messages, developers will flood support"
- (learn) "Top 3 requested integration from our community survey: Zapier, API, CSV (in that order)"

---

## Card Count Summary

| Journey                | Steps | Story Cards | Objectives | Risks | Questions | Knowledge Gaps | Learnings |
| ---------------------- | ----- | ----------- | ---------- | ----- | --------- | -------------- | --------- |
| Import from CSV        | 3     | 13          | 2          | 2     | 2         | 1              | 1         |
| Import from Competitor | 3     | 11          | 1          | 2     | 2         | 1              | 1         |
| Import via API         | 2     | 8           | 1          | 1     | 1         | 1              | 1         |
| **Total**              | **8** | **32**      | **4**      | **5** | **5**     | **3**          | **3**     |

## Notes

- This is a discovery board — heavy on questions, risks, and knowledge gaps relative to regular story cards
- No milestones yet: the purpose is to explore before planning
- No colors used — could add colors later to mark "validated" vs "needs research" cards
- Learnings are grounded in specific evidence (user interviews, competitor analysis, surveys)
- The board will evolve: questions become learnings, risks become mitigated tasks, and milestones get added when the team is ready to plan
