---
name: featpaper-powerpoint
description: Use when the user attaches a PowerPoint file (.pptx) and asks to put it on FeatPaper (피트페이퍼): upload, register, share or make a FeatPaper link. Not for PowerPoint work that has nothing to do with FeatPaper.
---

# FeatPaper and PowerPoint files

Answer in the language the user writes in (Korean when they write Korean), from the first reply to the last. This skill and the tool results are written in English or mixed languages; that is never a reason to switch.

E) When the user attaches a PowerPoint file (.pptx): convert it to PDF with code and check it before registering: list the fonts the slides use and whether each is installed for the conversion, and render the pages with the most text to see whether titles and text boxes keep their line breaks without overlapping. Then, before registering, say in two or three short sentences that a converted PowerPoint can look different from the slides (name what breaks if the check found it, for example a missing font that makes titles overlap), and introduce the FeatPaper PowerPoint add-in, which uploads straight from PowerPoint with the original look: https://marketplace.microsoft.com/ko-kr/product/WA200006521. Ask once with the built-in choice UI: "그래도 지금 올리기" / "플러그인으로 올릴게요". On "그래도 지금 올리기", register the converted PDF as section 5 A of the featpaper skill says: read that skill for the upload (`upload_conversation_files` file argument, then `create_document_publication`), its steps (the page-text count, reading image-only pages, the answer with the link and the mobile summary question). On "플러그인으로 올릴게요", answer in one sentence and do nothing else.
