# Hebrew RTL Module

Use when the requested final artifact is Hebrew or Hebrew/English and document layout matters.

## Direction rules
- Document base direction: RTL.
- Hebrew paragraphs, headings, bullets and table text: RTL and right aligned unless the design requires otherwise.
- Technical identifiers remain LTR and isolated: hostnames, FQDNs, IPs, IPv6, WWPNs, WWNs, MACs, commands, paths, versions, model numbers, job IDs, URLs, code and CLI output.
- Do not allow punctuation or parentheses around LTR tokens to reorder visually.
- Preserve English product names exactly.
- Tables must remain readable when Hebrew labels and LTR technical values appear in the same row.
- Numbering and bullets must appear on the correct RTL side.

## Output-specific behavior
DOCX: use proper paragraph and run bidi/RTL properties; validate tables and mixed-direction cells.
PDF: render from a bidi-capable source and visually verify representative pages.
PPTX: use RTL text boxes for Hebrew and LTR isolation for technical tokens.

## Quality gate
Check title page, headings, numbered lists, bullets, mixed Hebrew/English paragraphs, tables, IP/WWPN rows, commands, parentheses and punctuation before delivery.
