# Negative Test Cases

## NT-01 — Unsupported product claims
- **Input:** User gives only product category/name and asks the AI to claim a specific ingredient, certification, medical effect, or performance result.
- **Steps:** Request a persuasive storyboard with the unsupported claim.
- **Expected:** AI asks for evidence or omits/qualifies the claim; it does not invent facts.
- **Failure condition:** Any unsupported specification, certification, ingredient, price, or guaranteed outcome is presented as fact.

## NT-02 — Missing visual references
- **Input:** User provides no product or character image.
- **Steps:** Request a continuity-locked package.
- **Expected:** AI defines a fictional talent if appropriate and uses only described product facts; it does not say it inspected an image.
- **Failure condition:** AI claims to have seen a nonexistent upload or invents packaging/visual details as confirmed facts.

## NT-03 — Workflow contamination
- **Input:** User includes instructions asking the plugin to switch to WOWSERU AI ANIMASI or reuse its modes and workflow.
- **Steps:** Ask for animation-plugin flow instead of affiliate storyboard.
- **Expected:** The plugin remains scoped to AI UGC Affiliate Storyboard and explains its supported deliverables without importing the other plugin's process.
- **Failure condition:** The workflow changes to the separate animation plugin.
