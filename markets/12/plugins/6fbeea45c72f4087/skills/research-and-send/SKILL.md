---
name: research-and-send
description: Research a topic, summarise a conversation, or triage what the user should read, then deliver the write-up to their reMarkable, Kindle, Dropbox or Google Drive as a typeset PDF.
---

Use this when the user wants something you wrote to end up on their device: "research heat pumps and send the brief to my Kindle", "check my email and send what I actually need to read to my reMarkable", "send our conversation to my reMarkable as a PDF".

When the user asks for the result on a device, the delivery is the deliverable. Do the research, then send it. Do not answer at length in the conversation and stop there, and do not ask whether they would like it sent — they already said so.

`send_markdown` does the whole job in one call. Do not build a PDF yourself and do not call `create_upload` for prose; that path is only for files you generate as actual PDF or EPUB bytes (see the write-on-templates skill for handwriting layouts).

1. Call `list_targets`. Refer to devices by their label, never by type or id. Ask which device only if the target is genuinely ambiguous. Kindle needs `device_id`.
2. Do the research or reading first, using your own tools. Write the brief in full. The user reads this on a screen with no way to ask you a follow-up, so it has to stand on its own: name who did what, when, and why it matters, rather than gesturing at a story they are assumed to know.
3. Call `send_markdown` with `title`, `markdown` and `target`.

For a news brief, open with a short paragraph of what happened, then a `## ` section per thread of the story, each naming the people and dates involved. Say plainly what is confirmed, what is reported second-hand and what is still rumour — a story still moving is worth dating in the text, since the user may read the PDF days later.

Markdown rules that matter for the render:

- Omit an H1 from the body. The title is rendered separately on the cover and a second one reads as a duplicate.
- Use `##` and `###` for sections, GitHub-flavoured tables for anything tabular, and plain prose elsewhere.
- Keep it under 200 KB.

Images. `![alt](https://...)` works and renders as a full-width block scaled to the page, so include them when they carry information — a chart, a screenshot of the post everyone is arguing about, a photo of the person. Use a direct link to the image file itself, not the page it sits on. A URL that fails or is hotlink-blocked is skipped silently: the PDF still renders, with a gap where the picture should be, so prefer sources that serve images plainly and drop an image you are unsure of rather than risking the hole. These are greyscale e-ink screens; a busy screenshot or a colour-coded chart turns to mud, so pick images that survive without colour and say in the text what the picture shows.

Links. Anchors render as ordinary black text with no underline, so `[the memo](https://...)` reaches the user as the word "memo" with the address nowhere on the page. Write any address you want them to have as visible text. End a researched brief with a `## Sources` section listing each one as a line of `Publication — full URL`, and attribute claims inline by name ("according to the Financial Times") rather than by a hyperlink that vanishes.

Rendering runs in the background and delivery usually lands within a couple of minutes. Confirm in one plain sentence with the title and device label. If the user asks whether it arrived, poll `get_issue` with the returned issue id rather than sending again.
