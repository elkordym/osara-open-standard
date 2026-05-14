"""Convert a .docx to clean markdown for OSARA specs.

Handles:
- Paragraphs (with style-aware heading detection)
- Tables (as GitHub-flavored markdown tables)
- Lists (bulleted / numbered)

Usage:
    python scripts/docx_to_md.py <input.docx> <output.md>
"""

from __future__ import annotations

import sys
from pathlib import Path

from docx import Document
from docx.oxml.ns import qn
from docx.table import Table
from docx.text.paragraph import Paragraph


def iter_block_items(parent):
    """Yield paragraphs and tables in document order."""
    if hasattr(parent, "element"):
        parent_elm = parent.element.body
    else:
        parent_elm = parent._element

    for child in parent_elm.iterchildren():
        if child.tag == qn("w:p"):
            yield Paragraph(child, parent)
        elif child.tag == qn("w:tbl"):
            yield Table(child, parent)


def heading_level(style_name: str) -> int | None:
    if not style_name:
        return None
    name = style_name.strip().lower()
    if name.startswith("heading "):
        try:
            return int(name.split()[1])
        except (IndexError, ValueError):
            return None
    if name == "title":
        return 1
    return None


def list_prefix(paragraph: Paragraph) -> str | None:
    style = (paragraph.style.name if paragraph.style else "").lower()
    pPr = paragraph._p.find(qn("w:pPr"))
    has_numpr = pPr is not None and pPr.find(qn("w:numPr")) is not None
    if has_numpr or "list" in style or "bullet" in style:
        return "- "
    return None


def cell_text(cell) -> str:
    parts = []
    for para in cell.paragraphs:
        text = para.text.strip()
        if text:
            parts.append(text)
    joined = " \\| ".join(parts) if len(parts) > 1 else (parts[0] if parts else "")
    return joined.replace("\n", " ").replace("|", "\\|")


def table_to_md(table: Table) -> str:
    rows = []
    for row in table.rows:
        rows.append([cell_text(c) for c in row.cells])
    if not rows:
        return ""
    width = max(len(r) for r in rows)
    rows = [r + [""] * (width - len(r)) for r in rows]
    header = rows[0]
    sep = ["---"] * width
    body = rows[1:]
    out = ["| " + " | ".join(header) + " |"]
    out.append("| " + " | ".join(sep) + " |")
    for r in body:
        out.append("| " + " | ".join(r) + " |")
    return "\n".join(out)


def convert(docx_path: Path) -> str:
    doc = Document(str(docx_path))
    lines: list[str] = []
    for block in iter_block_items(doc):
        if isinstance(block, Paragraph):
            text = block.text.strip()
            if not text:
                if lines and lines[-1] != "":
                    lines.append("")
                continue
            level = heading_level(block.style.name if block.style else "")
            if level:
                lines.append("")
                lines.append("#" * min(level, 6) + " " + text)
                lines.append("")
            else:
                prefix = list_prefix(block)
                if prefix:
                    lines.append(prefix + text)
                else:
                    lines.append(text)
        elif isinstance(block, Table):
            lines.append("")
            lines.append(table_to_md(block))
            lines.append("")
    cleaned: list[str] = []
    blank = False
    for line in lines:
        if line == "":
            if not blank:
                cleaned.append("")
            blank = True
        else:
            cleaned.append(line)
            blank = False
    return "\n".join(cleaned).strip() + "\n"


def main() -> None:
    if len(sys.argv) != 3:
        print("usage: docx_to_md.py <input.docx> <output.md>", file=sys.stderr)
        sys.exit(2)
    src = Path(sys.argv[1])
    dst = Path(sys.argv[2])
    md = convert(src)
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(md, encoding="utf-8")
    print(f"wrote {dst} ({len(md):,} bytes)")


if __name__ == "__main__":
    main()
