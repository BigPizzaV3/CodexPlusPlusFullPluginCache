#!/usr/bin/env python3
"""Build editable detail and execution DOCX files from explicit, revision-bound copy."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import tempfile


ROLES = {"strategy_docx": "strategy-details.docx", "execution_brief_docx": "execution-brief.docx"}


def text(value, label):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label} must contain nonempty text")
    return value


def validate(package):
    if not isinstance(package, dict) or package.get("schemaVersion") != 1:
        raise ValueError("unsupported document package")
    if not re.fullmatch(r"[0-9a-f]{64}", str(package.get("strategyContentHash", ""))):
        raise ValueError("strategyContentHash must be the server-returned SHA-256")
    text(package.get("strategyTitle"), "strategyTitle")
    docs = package.get("documents")
    if not isinstance(docs, dict) or set(docs) != set(ROLES):
        raise ValueError("both strategy_docx and execution_brief_docx are required")
    for role, doc in docs.items():
        if not isinstance(doc, dict):
            raise ValueError(f"{role} must be a document")
        text(doc.get("title"), "document title")
        if not isinstance(doc.get("sections"), list) or not doc["sections"]:
            raise ValueError("each document needs sections")
        for section in doc["sections"]:
            if not isinstance(section, dict):
                raise ValueError("section must be an object")
            text(section.get("heading"), "section heading")
            if not any(section.get(k) for k in ("paragraphs", "bullets", "tables")):
                raise ValueError("section must contain authored content")
            for field in ("paragraphs", "bullets", "sources"):
                if not isinstance(section.get(field, []), list):
                    raise ValueError(f"{field} must be a list")
                for item in section.get(field, []):
                    text(item, field)
            if not isinstance(section.get("tables", []), list):
                raise ValueError("tables must be a list")
            for table in section.get("tables", []):
                if not isinstance(table, dict) or not isinstance(table.get("headers"), list) or not table["headers"]:
                    raise ValueError("table headers required")
                for header in table["headers"]:
                    text(header, "table header")
                if not isinstance(table.get("rows"), list) or not table["rows"]:
                    raise ValueError("table rows required")
                for row in table["rows"]:
                    if not isinstance(row, list) or len(row) != len(table["headers"]):
                        raise ValueError("table column counts differ")
                    for cell in row:
                        text(cell, "table cell")
    return package


def build(package, output: Path):
    from docx import Document
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    from docx.shared import Inches, Pt, RGBColor

    validate(package)
    output.mkdir(parents=True, exist_ok=True)
    targets = [output / filename for filename in ROLES.values()]
    if any(target.exists() for target in targets):
        raise ValueError("output exists; use a new directory to preserve the previous version")
    marker = f"MyMarketer strategy: {package['strategyContentHash']}"
    with tempfile.TemporaryDirectory(prefix=".strategy-documents-", dir=output) as tmp:
        tmp = Path(tmp)
        for role, filename in ROLES.items():
            document = Document()
            layout = document.sections[0]
            layout.page_width, layout.page_height = Inches(8.27), Inches(11.69)
            layout.top_margin = layout.bottom_margin = Inches(0.7)
            layout.left_margin = layout.right_margin = Inches(0.75)
            for name in ("Normal", "Title", "Heading 1", "Heading 2", "List Bullet"):
                style = document.styles[name]
                style.font.name = "Yu Gothic"
                style.element.get_or_add_rPr().rFonts.set(qn("w:eastAsia"), "Yu Gothic")
                style.font.size = Pt(10.5 if name in ("Normal", "List Bullet") else 18 if name == "Title" else 13)
                style.font.color.rgb = RGBColor.from_string("243047" if name != "Normal" else "404040")
                style.paragraph_format.space_after = Pt(6)
            document.styles["Normal"].paragraph_format.line_spacing = 1.25
            spec = package["documents"][role]
            document.add_heading(spec["title"], 0)
            document.add_paragraph(package["strategyTitle"])
            for section in spec["sections"]:
                document.add_heading(section["heading"], 1)
                for paragraph in section.get("paragraphs", []):
                    document.add_paragraph(paragraph)
                for bullet in section.get("bullets", []):
                    document.add_paragraph(bullet, style="List Bullet")
                for spec_table in section.get("tables", []):
                    table = document.add_table(rows=1, cols=len(spec_table["headers"]))
                    table.style = "Light Shading Accent 1"
                    header = table.rows[0]
                    repeat = OxmlElement("w:tblHeader")
                    header._tr.get_or_add_trPr().append(repeat)
                    for cell, value in zip(header.cells, spec_table["headers"]):
                        cell.text = value
                    for row in spec_table["rows"]:
                        for cell, value in zip(table.add_row().cells, row):
                            cell.text = value
                    document.add_paragraph()
                for source in section.get("sources", []):
                    run = document.add_paragraph().add_run("出典：" + source)
                    run.font.size = Pt(8)
            run = document.add_paragraph().add_run(marker)
            run.font.size = Pt(7)
            document.core_properties.subject = package["strategyTitle"]
            document.core_properties.author = "MyMarketer"
            document.save(tmp / filename)
        # Exclusive create avoids replacing an artifact created during rendering.
        created = []
        try:
            for target in targets:
                with target.open("xb") as stream:
                    created.append(target)
                    stream.write((tmp / target.name).read_bytes())
        except BaseException:
            for target in created:
                target.unlink(missing_ok=True)
            raise
    return targets


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("output_directory", type=Path)
    args = parser.parse_args()
    try:
        package = json.loads(args.input.read_text(encoding="utf-8"))
        for path in build(package, args.output_directory.resolve()):
            print(path)
    except (ValueError, OSError) as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
