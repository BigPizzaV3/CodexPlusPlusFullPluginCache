#!/usr/bin/env python3
"""Export a locally generated policy.json to editable Word. No network access."""
import json
import sys
from pathlib import Path

try:
    from docx import Document
    from docx.enum.section import WD_SECTION_START, WD_ORIENT
    from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    from docx.shared import Inches, Pt, RGBColor
except ImportError:
    sys.exit("Word export needs python-docx. Use the generated Markdown draft if it is unavailable.")


def field(paragraph, name):
    element = OxmlElement('w:fldSimple')
    element.set(qn('w:instr'), name)
    paragraph._p.append(element)


def page_setup(section, landscape=False):
    section.orientation = WD_ORIENT.LANDSCAPE if landscape else WD_ORIENT.PORTRAIT
    section.page_width = Inches(11 if landscape else 8.5)
    section.page_height = Inches(8.5 if landscape else 11)
    section.top_margin = section.bottom_margin = Inches(0.65)
    section.left_margin = section.right_margin = Inches(0.7)
    section.header_distance = section.footer_distance = Inches(0.3)
    section.different_first_page_header_footer = False


def export(source, destination):
    if destination.exists():
        raise ValueError('Output already exists. Choose a new filename to preserve the previous draft.')
    content = json.loads(source.read_text(encoding='utf-8'))
    required = ['title', 'subtitle', 'preparedLine', 'postureLabel', 'postureSummary',
                'disclaimer', 'sections', 'boardQuestions']
    if not isinstance(content, dict) or any(k not in content for k in required):
        raise ValueError('Use policy.json from the bundled policy generator.')
    if len(content['sections']) != 13 or len(content['boardQuestions']) != 10:
        raise ValueError('Expected eleven sections, two appendices, and ten board questions.')
    doc = Document()
    doc.settings.odd_and_even_pages_header_footer = False
    page_setup(doc.sections[0])
    for style in doc.styles:
        for element in style.element.xpath('./w:pPr/w:pBdr | ./w:pPr/w:contextualSpacing'):
            element.getparent().remove(element)
    normal = doc.styles['Normal']
    normal.font.name = 'Calibri'
    normal.font.size = Pt(11)
    normal.paragraph_format.space_after = Pt(6)
    normal.paragraph_format.line_spacing = 1.06
    for name, size in [('Title', 23), ('Subtitle', 12), ('Heading 1', 15), ('Heading 2', 12)]:
        style = doc.styles[name]
        style.font.name = 'Calibri'
        style.font.size = Pt(size)
        style.font.color.rgb = RGBColor(0, 0, 0)
        style.paragraph_format.space_before = Pt(12 if name.startswith('Heading') else 0)
        style.paragraph_format.space_after = Pt(6)
        style.paragraph_format.keep_with_next = True
    for name in ['List Bullet', 'List Number']:
        doc.styles[name].font.name = 'Calibri'
        doc.styles[name].font.size = Pt(11)
        doc.styles[name].paragraph_format.space_after = Pt(4)
    doc.core_properties.author = 'StratusLIVE'
    doc.core_properties.title = content['title']
    doc.core_properties.subject = 'Draft nonprofit AI policy for board review'
    doc.core_properties.keywords = 'draft, nonprofit, AI policy, board review'
    doc.core_properties.comments = 'Generated from fixed policy clauses and explicit choices. Not legal advice.'
    header = doc.sections[0].header.paragraphs[0]
    header.text = 'AI USE POLICY | DRAFT FOR BOARD REVIEW'
    header.runs[0].font.size = Pt(8)
    footer = doc.sections[0].footer.paragraphs[0]
    footer.text = 'Draft for review • '
    footer.runs[0].font.size = Pt(8)
    field(footer, 'PAGE')
    doc.add_paragraph(content['title'], 'Title')
    doc.add_paragraph(content['subtitle'], 'Subtitle')
    doc.add_paragraph(content['preparedLine'])
    p = doc.add_paragraph()
    p.add_run(content['postureLabel'] + '. ').bold = True
    p.add_run(content['postureSummary'])
    p = doc.add_paragraph(content['disclaimer'])
    for run in p.runs:
        run.italic = True
        run.font.size = Pt(10)
    for section in content['sections']:
        appendix = section['number'].startswith('Appendix')
        if appendix:
            page_setup(doc.add_section(WD_SECTION_START.NEW_PAGE), section['number'] == 'Appendix A')
        title = f"{section['number']} {section['heading']}"
        doc.add_heading(title, level=1)
        for block in section['blocks']:
            kind = block['type']
            if kind == 'p':
                doc.add_paragraph(block['text'])
            elif kind == 'note':
                p = doc.add_paragraph(block['text'])
                for run in p.runs:
                    run.italic = True
                    run.font.size = Pt(10)
            elif kind in ['bullets', 'numbered']:
                for item in block['items']:
                    doc.add_paragraph(item, 'List Bullet' if kind == 'bullets' else 'List Number')
            elif kind == 'table':
                table = doc.add_table(rows=1, cols=len(block['header']))
                table.style = 'Table Grid'
                table.alignment = WD_TABLE_ALIGNMENT.CENTER
                table.autofit = False
                available = 9.6 if section['number'] == 'Appendix A' else 7.1
                count = len(block['header'])
                for column in table.columns:
                    column.width = Inches(available / count)
                repeat = OxmlElement('w:tblHeader')
                table.rows[0]._tr.get_or_add_trPr().append(repeat)
                for cell, label in zip(table.rows[0].cells, block['header']):
                    cell.text = label
                    shading = OxmlElement('w:shd')
                    shading.set(qn('w:fill'), 'E9ECEF')
                    cell._tc.get_or_add_tcPr().append(shading)
                    for run in cell.paragraphs[0].runs:
                        run.bold = True
                        run.font.color.rgb = RGBColor(0, 0, 0)
                for row in block['rows']:
                    for cell, value in zip(table.add_row().cells, row):
                        cell.text = value
                for row in table.rows:
                    for cell in row.cells:
                        cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.TOP
                        for p in cell.paragraphs:
                            p.paragraph_format.space_after = Pt(5)
                            for run in p.runs:
                                run.font.size = Pt(10)
                doc.add_paragraph()
            else:
                raise ValueError('Unrecognized policy block type.')
    doc.add_page_break()
    doc.add_heading('Questions your board will ask about AI in fundraising', 1)
    for i, question in enumerate(content['boardQuestions'], 1):
        doc.add_heading(f"{i} {question['q']}", 2)
        p = doc.add_paragraph()
        p.add_run('Why they ask ').italic = True
        p.add_run(question['why']).italic = True
        doc.add_paragraph(question['answer'])
    doc.add_paragraph(content['disclaimer'])
    destination.parent.mkdir(parents=True, exist_ok=True)
    doc.save(destination)
    print(json.dumps({'ok': True, 'file': str(destination.resolve()), 'policySections': 11,
                      'appendices': 2, 'boardQuestions': 10}))


if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit('Usage: python3 export-docx.py policy.json policy.docx')
    try:
        export(Path(sys.argv[1]), Path(sys.argv[2]))
    except (OSError, ValueError, KeyError, TypeError) as error:
        sys.exit(str(error))
