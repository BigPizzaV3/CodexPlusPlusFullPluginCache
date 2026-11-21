# Opening a plan in MayRetire

Use `plan_handoff_url` only when the user asks to see, open, review, or
visualize an available plan in the MayRetire web UI. The tool creates a URL
with the plan in its fragment; it does not open a browser, save the plan to
an account, or run a calculation. Do not call it in comparison, search, or
simulation loops. If opening would merely be helpful, offer it first.

Treat the generated URL as sensitive because it contains plan data. Avoid
copying it into logs, notes, or broad summaries. Tell the user what the link
does and that opening it can replace the current plan in that browser; use
the tool's confirmation option when the user wants a browser-side prompt.
