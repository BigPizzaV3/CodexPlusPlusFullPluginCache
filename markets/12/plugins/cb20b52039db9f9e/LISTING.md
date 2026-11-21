# Tradermaths: directory listing copy

**Name:** Tradermaths
**Short description:** Your graduate role tracker
**Long description:** see plugin.json interface.longDescription

## Starter prompts
- Give me a weekly review of my Tradermaths applications.
- Which of my applications are at the online test stage, and what should I prep?
- Show me open graduate trading programmes I haven't tracked yet.
- How many roles do I have at each stage?
- What prep resources do you have for Optiver?

## Tools (all readOnlyHint: true)
list_board, get_board_role, board_summary, list_programmes, get_prep_resources

## Review test cases

The root `plugin.json` contains the review metadata: five positive and three negative MCP cases. The positive cases cover board summary, board filtering and role-specific preparation, role detail and history, open programme discovery, and public firm preparation resources. The negative cases verify that the read-only plugin does not change applications, submit applications, or access another user's tracker.

Reviewer credentials and sign-in instructions must be entered in the submission portal's secure Review details fields, not in this package. The positive cases require a dedicated reviewer account with tracked roles, including at least one Online test role at a firm with a public guide.
