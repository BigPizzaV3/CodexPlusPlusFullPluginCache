# Accounting

This plugin helps with day-to-day accounting, financial reporting, and audit work. Use it to reconcile records, investigate discrepancies, or carry out tasks in your accounting software and workbooks.

The [Accounting skill](skills/accounting/SKILL.md) guides the assistant to investigate issues before drawing conclusions and make its work easy to review. The assistant explains its accounting judgments, flags unresolved questions, and saves a changelog through the Library tool when available.

## Target users

The skill should scale from basic to power users. The working mental model of the median accounting user is someone who:

- Mostly uses the web.
- Prefers collaborating with ChatGPT/Codex.
- Does not yet trust the model to complete long-horizon tasks independently.

## Themes

- Investigate available evidence before asking the user for missing information.
- Make it easy for the user to verify the work, including through an audit trail.
- Add guidelines that address select failure modes.
- Offer additional help when it aligns with the user's task or when the model can confidently add value with little or no user effort.
- Keep the skill concise to limit token usage and risk of unintended interpretation of skills instructions.

## Optional connections

Google Drive and SharePoint can provide access to workbooks, company procedures, and audit evidence. Gmail and Outlook Email can provide access to accounting correspondence and attachments. NetSuite, QuickBooks, Xero, Rillet, and Campfire can provide access to accounting records and workflows. The **Works with** section uses the optional dependencies and categories declared in [plugin.json](.codex-plugin/plugin.json) under `extensions.com.openai.dependencies`.

| App | Catalog name |
| --- | --- |
| NetSuite | `app-69d954576c8081919b329f17e38e67a6` |
| Xero | `app-6a7ee05cee1881918dbfaba26fb555e1` |
| Rillet | `app-6a95f1295f7c819193d4e0f73131ae7b` |
| Campfire | `app-6ab432f315848191a14eea7caf742d8d` |
| Oracle NetSuite QuickStart | `app-6abbbd251da881918ada4c5ce02f3903` |
| FreshBooks | `freshbooks-mcp` |
| BILL | `bill` |

These declarations do not install the connectors or grant account access. The app running the plugin must support the dependency declaration to offer activation.

## Distribution

Accounting ships through the [OpenAI-maintained marketplace](../../marketplace.json). After the version bump merges to `master`, use Platform to import or sync Accounting, then publish the approved version. [Shipping OpenAI-maintained plugins V2](https://chatgpt.com/space/page_840237cadae48191825ca898e9ee37f6)

## Validation

From the repository root:

```sh
python3 plugins/codex-plugin-skill-authoring/scripts/validate_plugin.py chatgpt/oai-maintained-plugins/plugins/accounting
```

To check the release import contract, run `cloud-plugin-admin validate-plugin-for-release chatgpt/oai-maintained-plugins/plugins/accounting`.
