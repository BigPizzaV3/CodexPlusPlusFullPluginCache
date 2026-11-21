# Two-column alignment protocol

## Use cases
User commands such as `trình bày 2 cột`, `dịch song song`, `đối chiếu`, `parallel English-Vietnamese`, `compare draft` and `before vs after` MUST create a two-column Markdown table. Default to English on the left and Vietnamese on the right for EN→VI; reverse for VI→EN. For editing use original on left and edited text on right. Label language direction accurately.

### Medical sentence alignment (illustrative, not a patient diagnosis)
| Original (English) | Bản dịch (Tiếng Việt) |
|---|---|
| The child regurgitates food shortly after meals. | Trẻ trào thức ăn trở lại miệng ngay sau bữa ăn. |
| There is no associated heartburn or chest pain. | Không kèm ợ nóng hoặc đau ngực. |
| The diagnosis is based primarily on the clinical history. | Chẩn đoán chủ yếu dựa vào bệnh sử. |

### Original versus revised English
| Câu gốc | Câu chỉnh sửa |
|---|---|
| He don't have chest pain. | He does not have chest pain. |
| The patient only spit the food. | The patient only regurgitates food. |

## Fidelity checklist
- Exactly two comparison columns unless expressly asked otherwise.
- Row N in column 2 corresponds to row N in column 1; no swapped order, additions, omitted sentences or unexplained summarization.
- Keep technical signs (>, <, ≤, p, CI), units, dosages, numbered evidence and negations faithful. Escape vertical bar (`\|`) within content.
- For multi-paragraph documents, split at paragraph or sentence boundaries and maintain original section subheadings. Start a new two-column table with a header if necessary; no invented content to fill empty cells.
- When `song song` is NOT requested, prefer unadorned translation over a table; for long context the user may choose bilingual output.
- Medical context does not mean the plugin should diagnose: the table illustrates wording, not clinical advice.
