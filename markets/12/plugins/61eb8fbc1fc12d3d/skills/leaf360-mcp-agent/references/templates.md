# Templates And Merge Variables

Templates are durable CRM assets. Be strict, discover variables first, and leave drafts for human review.

## Required Flow

1. Call `leaf360_template_variables_get` before creating or updating templates.
2. Choose `audience` based on the target context: `lead`, `loan`, `contact`, `loanOfficer`, `company`, `system`, or `all`.
3. Choose `channel`: `email`, `sms`, `automationWorkflow`, `directEmailSend`, or `all`.
4. Use only returned variables.
5. Create or update draft templates only.
6. If the user wants organization, list folders first, then create a folder only when needed.

## Namespace Rules

- `contact.*` is for referral partners/business contacts. Do not mix `contact.*` with `lead.*` or `loan.*`.
- `lead.*` and `loan.*` may be combined only when the template is intentionally sent in a lead/loan context.
- Loan-only templates are valid for loan-scoped milestone or status updates.
- Use `loanOfficer.role` as the canonical loan officer role variable. Treat `loanOfficer.title` as deprecated.
- Use `{{loanOfficer.losApplicationLink}}` as the href for apply-now buttons and links. It resolves from the assigned loan officer's LOS application link and works in email, SMS, and automation sends.

## Reliable Loan Variables

For loan-scoped templates, prefer `loan.loanAndProperty.*` for deal terms:

- `{{loan.loanNumber}}`
- `{{loan.loanType}}`
- `{{loan.loanStage}}`
- `{{loan.loanStatus}}`
- `{{loan.allBorrowersFirstName}}`
- `{{loan.allBorrowersFullName}}`
- `{{loan.loanAndProperty.loanAmount}}`
- `{{loan.loanAndProperty.purchasePrice}}`
- `{{loan.loanAndProperty.downPayment}}`
- `{{loan.loanAndProperty.noteRate}}`
- `{{loan.loanAndProperty.amortizationTerm}}`
- `{{loan.loanAndProperty.propertyAddress.address1}}`
- `{{loan.loanAndProperty.propertyAddress.city}}`
- `{{loan.loanAndProperty.propertyAddress.state}}`
- `{{loan.loanAndProperty.propertyAddress.zip}}`
- `{{loan.loanAndProperty.propertyAddress.county}}`
- `{{loan.estimatedClosingDate}}`

Do not say the loan namespace lacks amount, rate, payment, or address fields until `leaf360_template_variables_get` has been called and checked.

## Low-Reliability Lead Deal Fields

Some lead deal fields may default to values like `0` or `None`. If a loan-scoped variable exists, use it instead.

Prefer:

- `{{loan.loanAndProperty.loanAmount}}` instead of `{{lead.loanAmount}}`
- `{{loan.loanAndProperty.noteRate}}` instead of `{{lead.noteRate}}`
- `{{loan.loanAndProperty.propertyAddress.address1}}` instead of a lead address fallback

## Email Templates

- Use `leaf360_email_template_create` for new email drafts.
- Use `leaf360_email_template_update` only for draft templates.
- Active templates are protected. If blocked, tell the user to duplicate or edit in Leaf360.
- Use safe HTML, hosted images, and merge variables for personalization.

## SMS Templates

- Use `leaf360_sms_template_create` for SMS drafts.
- Keep SMS short and clear.
- Watch for multipart and non-GSM warnings.
- Never use HTML in SMS bodies.
