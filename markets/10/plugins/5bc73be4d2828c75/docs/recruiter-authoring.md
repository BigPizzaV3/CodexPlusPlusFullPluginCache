# Authoring recruiter skills

Each directory under `skills/` contains a portable `SKILL.md` with YAML frontmatter: `name`, a discriminating `description`, `license`, and string-valued `metadata.version`. The directory and name must match. Keep additional resources inside that directory so individual installation remains self-contained.

Write a real procedure that changes the assistant's decisions. Specify required inputs, evidence handling, missing information, output, a fictional example, quality checks, and completion. Use optional references only where needed. Avoid generic filler, empty placeholders, and duplicated manuals.

Skills are individually installable. References to another skill are optional handoffs, not relative file dependencies. The coordinator must handle an absent specialist skill.

Methods should work with user-supplied context when possible. Connected actions must use tools actually present in the current connection. Never infer that an email was sent, a calendar event booked, a record saved, or an approval executed from a draft or pending response.

Keep criteria tied to the work, distinguish facts from inference, and preserve human hiring decisions. Honor user authorization already given while enforcing real service approval boundaries. Do not add indiscriminate permission prompts to reads or drafting.

Update `catalog.json`, README, and CHANGELOG with the skill. Add a behavioral evaluation case when a new failure mode needs coverage. Run the documented checks and submit a scoped PR.
