# Revise existing manuscript text

Read the passage and its context first. Diagnose the concrete issue before proposing a rewrite. Depth: language preserves argument and claims; argument also improves logical order and evidence connections; scientific additionally audits the available scientific support. Do not imply that unavailable data were checked.

In proposal mode, call `writing.propose` for each coherent passage: project-relative path (empty for pasted text), exact manuscript `before`, replacement `after`, concise `analysis`, and `reason`. Use the actual LaTeX source where applicable. The tool creates an editable chat card and DOES NOT modify the manuscript. Do not substitute a Markdown diff or repeat the full replacement in the closing answer. Never use write/shell/subagent tools to bypass proposals.

The user's current edited proposal supersedes the original tool output. For a follow-up, revise that current text while keeping `before` anchored to the unchanged manuscript. Discarding a proposal never writes a file. Application is an explicit UI action.

In direct mode, use normal guarded editing tools within scope and report the actual change. Approval gates still apply. Check affected cross-references and claims. Compilation and PDF inspection follow applied LaTeX changes, not unapplied proposals. Report unresolved verification without claiming completion.
