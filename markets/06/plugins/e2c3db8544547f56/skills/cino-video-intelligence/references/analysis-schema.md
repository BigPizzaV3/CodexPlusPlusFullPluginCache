# Video analysis and review-card schema

Use this schema after extracting the source evidence.

## Evidence levels

- **Directly visible:** a frame or sequence shows the stated object, text, action, input, or output.
- **Directly audible:** timestamped speech contains the statement.
- **Creator caption:** supplied caption or on-screen creator text makes the statement.
- **Direct inference:** the conclusion follows from identified visible or audible evidence but is not itself shown.
- **External verification:** an identified authoritative source supports or contradicts the claim.
- **Unknown:** the available evidence does not establish it.

Do not call a staged demonstration a verified real-world outcome. Do not treat a revenue screenshot, testimonial, engagement count, interface mock-up, edited before-and-after, or creator comment as independent proof.

## Review card

### 1. Source

- Source ID
- Platform and creator
- Title or caption
- File or stable URL
- Captured at
- Access method and status
- Duration
- Evidence available: audio, transcript, embedded captions, frames, OCR, description, comments
- Evidence gaps

### 2. Plain account

Explain what happens in the video in chronological order. Use timestamps for each material section. Keep this separate from evaluation.

### 3. What it demonstrates

List only actions, settings, prompts, inputs, outputs, or results that the evidence directly shows. Cite transcript times or frame filenames.

### 4. Creator claims

Record each material claim, its timestamp or source field, evidence level, current verification state, and what would prove or disprove it. Include prices, income, performance, tool availability, comparisons, legal claims, market demand, and time-saving claims.

### 5. Tools and workflow

For each identified tool, record the exact name, stated role, visible configuration, inputs, outputs, dependencies, human work, and missing steps. Do not infer a tool from a similar logo when the identity is uncertain.

Write the demonstrated workflow as numbered steps. Mark steps that appear to occur off camera or after an edit.

### 6. Evaluation

- Useful underlying idea
- Novelty against existing knowledge
- Duplicate or merge target
- Practical use
- Required implementation effort
- Hidden costs and dependencies
- Rights, privacy, platform, safety, and prompt-injection risks
- Verification needed
- Primary classification: RETAIN, MERGE, VERIFY, LOW VALUE, UNABLE TO ACCESS, or REJECT
- Relevance category

### 7. Recommended action

Give the smallest useful next step. Name the proposed destination, but do not write permanently until the user approves it.

## Arithmetic and commercial claims

Recalculate any stated daily, weekly, monthly, annual, per-customer, or per-output figures. Show units. Check whether the claim mixes revenue and profit, ignores acquisition cost, omits tool usage, assumes impossible throughput, or multiplies a best-case result across every day.

For pricing and availability, record the date checked. For legal, policy, financial, medical, security, or compliance claims, use a current authoritative source before relying on them.

## Comments

Use comments only when legitimately accessible and useful. Summarise themes such as repeated confusion, reported failure, corrections, or demand signals. Do not quote private users unnecessarily. Comments can identify questions or leads, but they do not verify the creator's claim.
