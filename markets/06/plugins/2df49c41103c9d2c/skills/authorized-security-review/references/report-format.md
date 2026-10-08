# HackerOne report draft

Use the program's supplied template when available. Otherwise use this structure. Include only sections supported by evidence and explicitly label uncertainties.

## Title
Name the failed security control and concrete effect.

## Summary
State the affected asset, actor privileges, unexpected behavior, and demonstrated impact in a few sentences.

## Asset and prerequisites
Record the exact in-scope endpoint/application/version, test date, accounts/roles, required configuration, and relevant scope rule.

## Reproduction
Provide numbered minimal steps with expected versus actual results. Include relevant sanitized requests, commands, or source references. Replace secrets with clear placeholders and explain which test account supplies them. Do not imply that proposed steps were executed.

## Evidence
Reference saved artifacts and explain what each proves. Preserve relevant timestamps and request IDs where useful; redact private data. Source evidence needs path and verified line numbers. Runtime evidence needs the actual observed effect and the control comparison.

## Impact and severity
Explain the demonstrated boundary crossing and prerequisites. Separate proven effects from hypothetical extensions. Apply the program's rating convention and justify the rating without promising acceptance or payment.

## Remediation
Describe the root control to repair and how the program can verify the fix, when the evidence supports a recommendation.

## Limitations
State remaining proof gaps, untested configurations, or lack of deployment/runtime verification.

Drafting is not submission. Do not click Submit, send messages, publish findings, or contact the program unless the user requests that external action. Preserve the exact report and destination for that action; avoid duplicate submissions when the outcome is uncertain.
