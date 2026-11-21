#!/usr/bin/env python3
"""Magnos finance helpers: one file, Python 3.9+, standard library only.

This is the single source of the shared library. tools/sync.py copies it into
every skill's scripts/ folder so each skill travels on its own (Claude apps,
ChatGPT and Codex load a skill folder by itself); a test fails when a copy
drifts from this file.

What is here:
- numbers: parse amounts as people write them ("$1,234", "(1,234)", "4.95M",
  "12%") and format them back the Magnos way ("$4.95M", "−$370K", "1.6%",
  "−0.2 pts");
- tables: read CSV, TSV and XLSX (values and formulas), write a small XLSX;
- calculations: an exact decimal calculator for expressions, variance,
  percentage change and bridges, each logged to the session's ledger;
- figures: find the figures in an answer and trace each one to the evidence
  (tool output, the user's message, the ledger) at the precision shown;
- the finance profile in .magnos/finance.md.

Run `python3 magnos_fin.py --help` for the command line.
"""
from __future__ import annotations

import argparse
import bisect
import csv
import datetime as _dt
import io
import json
import os
import re
import sys
import zipfile
from dataclasses import dataclass, field, asdict
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP, getcontext
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple
from xml.etree import ElementTree as ET
from xml.sax.saxutils import escape as _xml_escape

getcontext().prec = 34

MINUS = "−"  # the minus sign Magnos prints for negatives
D0 = Decimal(0)

# ---------------------------------------------------------------- numbers

_SCALE_WORDS = {
    "k": Decimal(1000), "thousand": Decimal(1000),
    "m": Decimal(1_000_000), "mm": Decimal(1_000_000), "million": Decimal(1_000_000),
    "b": Decimal(1_000_000_000), "bn": Decimal(1_000_000_000), "billion": Decimal(1_000_000_000),
}
_AMOUNT_RE = re.compile(
    r"""^\s*(?P<open>\()?\s*(?P<sign>[-+−–])?\s*(?P<cur>[$€£]|usd|eur|gbp)?\s*
        (?P<sign2>[-+−–])?\s*(?P<num>\d[\d,\s]*(?:\.\d+)?|\.\d+)\s*
        (?P<scale>k|m|mm|b|bn|thousand|million|billion)?\s*(?P<pct>%)?\s*(?P<cur2>[$€£]|usd|eur|gbp)?\s*
        (?P<close>\))?\s*(?P<trail>[-−])?\s*$""",
    re.X | re.I,
)


def to_decimal(value: Any, percent_as_ratio: bool = False) -> Optional[Decimal]:
    """Parse an amount the way finance files write it; None when it is not one.

    "$1,234.56" -> 1234.56; "(1,234)" -> -1234; "1,234-" -> -1234;
    "4.95M" -> 4950000; "12%" -> 12 (or 0.12 with percent_as_ratio).
    """
    if value is None:
        return None
    if isinstance(value, Decimal):
        return value
    if isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        return Decimal(str(value))
    text = str(value).strip().replace(" ", " ")
    if not text or text in {"-", "−", "–", "n/a", "N/A", "NA", "null", "None"}:
        return None
    m = _AMOUNT_RE.match(text)
    if not m:
        return None
    num = m.group("num").replace(",", "").replace(" ", "")
    try:
        out = Decimal(num)
    except InvalidOperation:
        return None
    scale = (m.group("scale") or "").lower()
    if scale:
        out *= _SCALE_WORDS[scale]
    negative = bool(m.group("open") and m.group("close")) or bool(m.group("trail"))
    for s in (m.group("sign"), m.group("sign2")):
        if s and s in "-−–":
            negative = not negative
    if negative:
        out = -out
    if m.group("pct") and percent_as_ratio:
        out = out / 100
    return out


def dec(value: Any) -> Decimal:
    """Like to_decimal, but raises ValueError when the value is not a number."""
    out = to_decimal(value)
    if out is None:
        raise ValueError(f"not a number: {value!r}")
    return out


def _q(x: Decimal, decimals: int) -> Decimal:
    return x.quantize(Decimal(1).scaleb(-decimals), rounding=ROUND_HALF_UP)


def num(x: Any, decimals: int = 0) -> str:
    """1234.5 -> "1,235"; negatives with the minus sign."""
    v = dec(x)
    s = f"{abs(_q(v, decimals)):,.{decimals}f}"
    return (MINUS + s) if v < 0 and _q(v, decimals) != 0 else s


def money(x: Any, unit: str = "auto", decimals: Optional[int] = None, currency: str = "$", signed: bool = False) -> str:
    """Format an amount the Magnos way.

    unit "auto": $4.95M (from 1M), $370K (from 10K), $1,245 below; "K": $4,950K;
    "M": $4.95M; "1": $4,950,000. Negatives print "−$370K"; signed adds "+".
    """
    v = dec(x)
    a = abs(v)
    u = unit.upper() if unit else "AUTO"
    if u == "AUTO":
        if a >= Decimal("1e9"):
            u = "B"
        elif a >= Decimal("1e6"):
            u = "M"
        elif a >= Decimal("1e4"):
            u = "K"
        else:
            u = "1"
    if u == "B":
        body = f"{_q(a / Decimal('1e9'), 2 if decimals is None else decimals):,}B"
    elif u == "M":
        body = f"{_q(a / Decimal('1e6'), 2 if decimals is None else decimals):,}M"
    elif u == "K":
        d = 0 if decimals is None else decimals
        body = f"{_q(a / Decimal('1e3'), d):,.{d}f}K"
    else:
        d = 0 if decimals is None else decimals
        body = f"{_q(a, d):,.{d}f}"
    zero = re.fullmatch(r"[0.,]+[KMB]?", body) is not None
    sign = MINUS if v < 0 and not zero else ("+" if signed and v > 0 else "")
    return f"{sign}{currency}{body}"


def pct(x: Any, decimals: int = 1, signed: bool = False, is_ratio: bool = True) -> str:
    """0.016 -> "1.6%" (is_ratio); 1.6 -> "1.6%" with is_ratio=False."""
    v = dec(x) * (100 if is_ratio else 1)
    q = _q(v, decimals)
    body = f"{abs(q):,.{decimals}f}%"
    if q < 0:
        return MINUS + body
    return ("+" + body) if signed and q > 0 else body


def pts(x: Any, decimals: int = 1, signed: bool = True) -> str:
    """A change in a percentage, in points: -0.2 -> "−0.2 pts"."""
    q = _q(dec(x), decimals)
    body = f"{abs(q):,.{decimals}f} pts"
    if q < 0:
        return MINUS + body
    return ("+" + body) if signed and q > 0 else body


def multiple(x: Any, decimals: int = 1) -> str:
    """3.2 -> "3.2×"."""
    return f"{_q(dec(x), decimals):,.{decimals}f}×"


def fmt(x: Any, kind: str = "number", unit: str = "auto", decimals: Optional[int] = None) -> str:
    """Format by kind: money, pct (a ratio), pts, multiple, number."""
    if kind == "money":
        return money(x, unit=unit, decimals=decimals)
    if kind == "pct":
        return pct(x, decimals=1 if decimals is None else decimals)
    if kind == "pts":
        return pts(x, decimals=1 if decimals is None else decimals)
    if kind == "multiple":
        return multiple(x, decimals=1 if decimals is None else decimals)
    return num(x, decimals=0 if decimals is None else decimals)


def safe_div(a: Any, b: Any) -> Optional[Decimal]:
    b = dec(b)
    return None if b == 0 else dec(a) / b


# ---------------------------------------------------------------- dates

_MONTHS = {m.lower(): i for i, m in enumerate(
    ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], start=1)}
_MONTHS.update({m.lower(): i for i, m in enumerate(
    ["January", "February", "March", "April", "May", "June", "July", "August", "September",
     "October", "November", "December"], start=1)})
_MONTHS["sept"] = 9


def parse_date(value: Any) -> Optional[_dt.date]:
    """ISO dates, US m/d/Y, d.m.Y, Excel serials, "Sep 2026" and "2026-09" (first of the month)."""
    if value is None:
        return None
    if isinstance(value, _dt.datetime):
        return value.date()
    if isinstance(value, _dt.date):
        return value
    s = str(value).strip()
    if not s:
        return None
    m = re.fullmatch(r"(\d{4})-(\d{1,2})-(\d{1,2})(?:[T ].*)?", s)
    if m:
        return _safe_date(int(m[1]), int(m[2]), int(m[3]))
    m = re.fullmatch(r"(\d{1,2})/(\d{1,2})/(\d{2,4})", s)
    if m:
        y = int(m[3]) + (2000 if len(m[3]) == 2 else 0)
        return _safe_date(y, int(m[1]), int(m[2]))
    m = re.fullmatch(r"(\d{1,2})\.(\d{1,2})\.(\d{4})", s)
    if m:
        return _safe_date(int(m[3]), int(m[2]), int(m[1]))
    m = re.fullmatch(r"(\d{4})-(\d{1,2})", s)
    if m:
        return _safe_date(int(m[1]), int(m[2]), 1)
    m = re.fullmatch(r"([A-Za-z]{3,9})\.?\s+(\d{4})", s)
    if m and m[1].lower() in _MONTHS:
        return _safe_date(int(m[2]), _MONTHS[m[1].lower()], 1)
    m = re.fullmatch(r"([A-Za-z]{3,9})\.?\s+(\d{1,2}),?\s+(\d{4})", s)
    if m and m[1].lower() in _MONTHS:
        return _safe_date(int(m[3]), _MONTHS[m[1].lower()], int(m[2]))
    if re.fullmatch(r"\d{5}(\.\d+)?", s):  # an Excel serial date
        n = int(float(s))
        if 20000 < n < 80000:
            return _dt.date(1899, 12, 30) + _dt.timedelta(days=n)
    return None


def _safe_date(y: int, m: int, d: int) -> Optional[_dt.date]:
    try:
        return _dt.date(y, m, d)
    except ValueError:
        return None


def month_end(d: _dt.date) -> _dt.date:
    nxt = _dt.date(d.year + (d.month == 12), d.month % 12 + 1, 1)
    return nxt - _dt.timedelta(days=1)


def month_label(d: _dt.date) -> str:
    return d.strftime("%b %Y")


# ---------------------------------------------------------------- tables


@dataclass
class Table:
    """Rows of a sheet as dicts of strings, with the header order kept."""
    columns: List[str]
    rows: List[Dict[str, str]]
    path: str = ""
    sheet: str = ""

    def __len__(self) -> int:
        return len(self.rows)

    def col(self, name: str) -> List[str]:
        return [r.get(name, "") for r in self.rows]

    def numbers(self, name: str) -> List[Optional[Decimal]]:
        return [to_decimal(v) for v in self.col(name)]

    def total(self, name: str) -> Decimal:
        return sum((v for v in self.numbers(name) if v is not None), D0)

    def kind(self, name: str) -> str:
        """number, date, text or empty, by what most non-empty values are."""
        vals = [v for v in self.col(name) if str(v).strip()]
        if not vals:
            return "empty"
        sample = vals[:500]
        n_num = sum(1 for v in sample if to_decimal(v) is not None)
        n_date = sum(1 for v in sample if parse_date(v) is not None and to_decimal(v) is None)
        if n_date >= 0.8 * len(sample):
            return "date"
        if n_num >= 0.8 * len(sample):
            return "number"
        return "text"


def _norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", str(s).lower())


def find_column(table: Table, *candidates: str, required: bool = False, exclude: Sequence[str] = ()) -> Optional[str]:
    """The column whose normalized name equals a candidate; else the closest one containing it.

    "account" picks "Account No" over "Account Name" (the shorter name wins);
    `exclude` names columns already taken by another role.
    """
    taken = {_norm(x) for x in exclude}
    cols = {_norm(c): c for c in table.columns if _norm(c) not in taken}
    for cand in candidates:
        if _norm(cand) in cols:
            return cols[_norm(cand)]
    for cand in candidates:
        nc = _norm(cand)
        hits = sorted((k for k in cols if nc and nc in k), key=lambda k: (len(k) - len(nc), k))
        if hits:
            return cols[hits[0]]
    if required:
        raise KeyError(f"{table.path or 'table'}: none of the columns {candidates} found; columns are {table.columns}")
    return None


def read_table(path: str, sheet: Optional[str] = None) -> Table:
    """Read a CSV, TSV or XLSX sheet into a Table (values, not formulas)."""
    low = path.lower()
    if low.endswith((".xlsx", ".xlsm")):
        wb = read_xlsx(path)
        name = sheet or wb.sheet_names[0]
        grid = wb.grid(name)
        while grid and not any(str(c).strip() for c in grid[0]):
            grid.pop(0)
        if not grid:
            return Table([], [], path, name)
        header = [str(h).strip() or f"col{i+1}" for i, h in enumerate(grid[0])]
        rows = []
        for g in grid[1:]:
            if not any(str(c).strip() for c in g):
                continue
            rows.append({header[i]: (str(g[i]) if i < len(g) else "") for i in range(len(header))})
        return Table(header, rows, path, name)
    with open(path, "r", encoding="utf-8-sig", newline="") as fh:
        text = fh.read()
    dialect_delim = "\t" if low.endswith(".tsv") else None
    if dialect_delim is None:
        try:
            dialect_delim = csv.Sniffer().sniff(text[:4096], delimiters=",;\t|").delimiter
        except csv.Error:
            dialect_delim = ","
    reader = csv.reader(io.StringIO(text), delimiter=dialect_delim)
    data = [r for r in reader]
    while data and not any(c.strip() for c in data[0]):
        data.pop(0)
    if not data:
        return Table([], [], path)
    header = [h.strip() or f"col{i+1}" for i, h in enumerate(data[0])]
    rows = []
    for r in data[1:]:
        if not any(c.strip() for c in r):
            continue
        rows.append({header[i]: (r[i].strip() if i < len(r) else "") for i in range(len(header))})
    return Table(header, rows, path)


def write_csv(path: str, headers: Sequence[str], rows: Iterable[Sequence[Any]]) -> None:
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(headers)
        for r in rows:
            w.writerow(["" if v is None else v for v in r])


# ---------------------------------------------------------------- xlsx

_NS = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
       "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
       "pr": "http://schemas.openxmlformats.org/package/2006/relationships"}


def col_letter(n: int) -> str:
    """1 -> A, 27 -> AA."""
    s = ""
    while n:
        n, r = divmod(n - 1, 26)
        s = chr(65 + r) + s
    return s


def col_number(letters: str) -> int:
    n = 0
    for ch in letters.upper():
        n = n * 26 + ord(ch) - 64
    return n


def split_ref(ref: str) -> Tuple[str, int]:
    m = re.fullmatch(r"\$?([A-Za-z]{1,3})\$?(\d+)", ref)
    if not m:
        raise ValueError(f"not a cell reference: {ref}")
    return m[1].upper(), int(m[2])


@dataclass
class Cell:
    ref: str
    value: Any = ""
    formula: Optional[str] = None
    kind: str = "n"  # n number, s string, b boolean, e error, str formula string

    @property
    def row(self) -> int:
        return split_ref(self.ref)[1]

    @property
    def col(self) -> int:
        return col_number(split_ref(self.ref)[0])


@dataclass
class Workbook:
    path: str
    sheet_names: List[str]
    sheets: Dict[str, Dict[str, Cell]]
    external_links: List[str] = field(default_factory=list)
    defined_names: Dict[str, str] = field(default_factory=dict)

    def cells(self, sheet: str) -> Dict[str, Cell]:
        return self.sheets.get(sheet, {})

    def grid(self, sheet: str) -> List[List[Any]]:
        cells = self.cells(sheet)
        if not cells:
            return []
        max_r = max(c.row for c in cells.values())
        max_c = max(c.col for c in cells.values())
        grid = [["" for _ in range(max_c)] for _ in range(max_r)]
        for c in cells.values():
            grid[c.row - 1][c.col - 1] = c.value
        return grid


_REF_IN_FORMULA = re.compile(r"(?<![A-Za-z_$\d.])(\$?)([A-Z]{1,3})(\$?)(\d+)(?![\d(A-Za-z_!])")


def shift_formula(formula: str, d_row: int, d_col: int) -> str:
    """Move the relative references of a shared formula by rows and columns."""
    def repl(m: re.Match) -> str:
        c_abs, letters, r_abs, digits = m.groups()
        c = col_number(letters) if c_abs else col_number(letters) + d_col
        r = int(digits) if r_abs else int(digits) + d_row
        if c < 1 or r < 1:
            return m.group(0)
        return f"{c_abs}{col_letter(c)}{r_abs}{r}"
    # leave quoted strings alone
    parts = re.split(r'("[^"]*")', formula)
    return "".join(p if p.startswith('"') else _REF_IN_FORMULA.sub(repl, p) for p in parts)


def read_xlsx(path: str) -> Workbook:
    """Values and formulas of every sheet; shared formulas expanded; external links listed."""
    with zipfile.ZipFile(path) as z:
        names = set(z.namelist())
        shared: List[str] = []
        if "xl/sharedStrings.xml" in names:
            root = ET.fromstring(z.read("xl/sharedStrings.xml"))
            for si in root.findall("m:si", _NS):
                shared.append("".join(t.text or "" for t in si.iter(f"{{{_NS['m']}}}t")))
        wb = ET.fromstring(z.read("xl/workbook.xml"))
        rels = {}
        if "xl/_rels/workbook.xml.rels" in names:
            for r in ET.fromstring(z.read("xl/_rels/workbook.xml.rels")).findall("pr:Relationship", _NS):
                rels[r.get("Id")] = r.get("Target")
        sheet_names, sheet_files = [], {}
        for s in wb.find("m:sheets", _NS).findall("m:sheet", _NS):
            nm = s.get("name")
            rid = s.get(f"{{{_NS['r']}}}id")
            target = rels.get(rid, "")
            target = target.lstrip("/")
            if not target.startswith("xl/"):
                target = "xl/" + target
            sheet_names.append(nm)
            sheet_files[nm] = target
        defined = {}
        dn = wb.find("m:definedNames", _NS)
        if dn is not None:
            for d in dn.findall("m:definedName", _NS):
                defined[d.get("name")] = d.text or ""
        sheets: Dict[str, Dict[str, Cell]] = {}
        for nm in sheet_names:
            target = sheet_files[nm]
            if target not in names:
                sheets[nm] = {}
                continue
            root = ET.fromstring(z.read(target))
            cells: Dict[str, Cell] = {}
            masters: Dict[str, Tuple[str, str]] = {}
            for c in root.iter(f"{{{_NS['m']}}}c"):
                ref = c.get("r")
                t = c.get("t", "n")
                f = c.find("m:f", _NS)
                v = c.find("m:v", _NS)
                is_ = c.find("m:is", _NS)
                formula = None
                if f is not None:
                    if f.get("t") == "shared":
                        si = f.get("si")
                        if f.text:
                            masters[si] = (ref, f.text)
                            formula = f.text
                        elif si in masters:
                            mref, mtext = masters[si]
                            mc, mr = split_ref(mref)
                            cc, cr = split_ref(ref)
                            formula = shift_formula(mtext, cr - mr, col_number(cc) - col_number(mc))
                    else:
                        formula = f.text or ""
                raw = v.text if v is not None else None
                if t == "s" and raw is not None:
                    value: Any = shared[int(raw)] if int(raw) < len(shared) else ""
                elif t == "inlineStr" and is_ is not None:
                    value = "".join(x.text or "" for x in is_.iter(f"{{{_NS['m']}}}t"))
                    t = "s"
                elif t == "b":
                    value = raw == "1"
                elif t in ("str", "e"):
                    value = raw or ""
                else:
                    value = raw if raw is not None else ""
                    if isinstance(value, str) and value:
                        dv = to_decimal(value)
                        value = dv if dv is not None else value
                cells[ref] = Cell(ref, value, formula, t)
            sheets[nm] = cells
        ext = []
        link_rels = [n for n in names if re.fullmatch(r"xl/externalLinks/_rels/externalLink\d+\.xml\.rels", n)]
        # in [1], [2], ... order: the number a formula's [n] refers to
        for n in sorted(link_rels, key=lambda x: int(re.search(r"externalLink(\d+)", x).group(1))):
            for r in ET.fromstring(z.read(n)).findall("pr:Relationship", _NS):
                if r.get("Target"):
                    ext.append(r.get("Target"))
    return Workbook(path, sheet_names, sheets, ext, defined)


def write_xlsx(path: str, sheets: Dict[str, Sequence[Sequence[Any]]], bold_first_row: bool = True) -> None:
    """Write a small workbook: sheet name -> rows. A str starting with "=" is a formula."""
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    names = list(sheets)
    ct = ['<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
          '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">',
          '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>',
          '<Default Extension="xml" ContentType="application/xml"/>',
          '<Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>',
          '<Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/>']
    ct += [f'<Override PartName="/xl/worksheets/sheet{i+1}.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>' for i in range(len(names))]
    ct.append("</Types>")
    rels_root = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                 '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
                 '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/>'
                 '</Relationships>')
    wb = ['<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
          '<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><sheets>']
    wb += [f'<sheet name="{_xml_escape(n[:31])}" sheetId="{i+1}" r:id="rId{i+1}"/>' for i, n in enumerate(names)]
    wb.append("</sheets></workbook>")
    wrels = ['<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
             '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">']
    wrels += [f'<Relationship Id="rId{i+1}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet{i+1}.xml"/>' for i in range(len(names))]
    wrels.append(f'<Relationship Id="rId{len(names)+1}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>')
    wrels.append("</Relationships>")
    styles = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
              '<styleSheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">'
              '<fonts count="2"><font><sz val="11"/><name val="Calibri"/></font><font><b/><sz val="11"/><name val="Calibri"/></font></fonts>'
              '<fills count="2"><fill><patternFill patternType="none"/></fill><fill><patternFill patternType="gray125"/></fill></fills>'
              '<borders count="1"><border><left/><right/><top/><bottom/><diagonal/></border></borders>'
              '<cellStyleXfs count="1"><xf numFmtId="0" fontId="0" fillId="0" borderId="0"/></cellStyleXfs>'
              '<cellXfs count="2"><xf numFmtId="0" fontId="0" fillId="0" borderId="0" xfId="0"/>'
              '<xf numFmtId="0" fontId="1" fillId="0" borderId="0" xfId="0" applyFont="1"/></cellXfs>'
              '</styleSheet>')
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", "".join(ct))
        z.writestr("_rels/.rels", rels_root)
        z.writestr("xl/workbook.xml", "".join(wb))
        z.writestr("xl/_rels/workbook.xml.rels", "".join(wrels))
        z.writestr("xl/styles.xml", styles)
        for i, n in enumerate(names):
            out = ['<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
                   '<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"><sheetData>']
            for ri, row in enumerate(sheets[n], start=1):
                out.append(f'<row r="{ri}">')
                for ci, v in enumerate(row, start=1):
                    ref = f"{col_letter(ci)}{ri}"
                    style = ' s="1"' if (bold_first_row and ri == 1) else ""
                    if v is None or v == "":
                        continue
                    if isinstance(v, str) and v.startswith("="):
                        out.append(f'<c r="{ref}"{style}><f>{_xml_escape(v[1:])}</f></c>')
                    elif isinstance(v, bool):
                        out.append(f'<c r="{ref}" t="b"{style}><v>{int(v)}</v></c>')
                    elif isinstance(v, (int, float, Decimal)):
                        out.append(f'<c r="{ref}"{style}><v>{v}</v></c>')
                    else:
                        out.append(f'<c r="{ref}" t="inlineStr"{style}><is><t xml:space="preserve">{_xml_escape(str(v))}</t></is></c>')
                out.append("</row>")
            out.append("</sheetData></worksheet>")
            z.writestr(f"xl/worksheets/sheet{i+1}.xml", "".join(out))


# ---------------------------------------------------------------- the finance profile

PROFILE_PATH = os.path.join(".magnos", "finance.md")
PROFILE_DEFAULTS: Dict[str, Any] = {
    "fiscal_year_start": "January",
    "currency": "USD",
    "materiality_amount": Decimal(25000),
    "materiality_pct": Decimal(10),
    "variance_sign": "favourable-positive",
    "entities": "",
    "figure_check": "warn",
}


def magnos_dir(cwd: Optional[str] = None) -> str:
    return os.path.join(cwd or os.getcwd(), ".magnos")


def load_profile(cwd: Optional[str] = None) -> Dict[str, Any]:
    """Read .magnos/finance.md (`key: value` lines); defaults for what is missing.

    The result has `_source`: the file's path, or "defaults".
    """
    out = dict(PROFILE_DEFAULTS)
    path = os.path.join(magnos_dir(cwd), "finance.md")
    out["_source"] = "defaults"
    if not os.path.exists(path):
        return out
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            m = re.match(r"^\s*[-*]?\s*([a-z_]+)\s*:\s*(.+?)\s*$", line)
            if not m:
                continue
            k, v = m[1], m[2]
            if k in ("materiality_amount", "materiality_pct"):
                dv = to_decimal(v)
                if dv is not None:
                    out[k] = dv
            else:
                out[k] = v
    out["_source"] = path
    return out


def fiscal_start_month(profile: Dict[str, Any]) -> int:
    s = str(profile.get("fiscal_year_start", "January")).strip().lower()
    if s.isdigit():
        return max(1, min(12, int(s)))
    return _MONTHS.get(s, _MONTHS.get(s[:3], 1))


_SYMBOLS = {"USD": "$", "EUR": "€", "GBP": "£", "JPY": "¥", "CAD": "C$", "AUD": "A$",
            "CHF": "CHF ", "SEK": "SEK ", "TRY": "₺"}


def currency_symbol(code: Any) -> str:
    """"USD" -> "$"; an unknown code prints as itself and a space: "NOK 25K"."""
    c = str(code or "USD").strip().upper()
    return _SYMBOLS.get(c, f"{c} ")


def profile_line(profile: Dict[str, Any]) -> str:
    """"FY Jan–Dec · USD · materiality $25K / 10%" for status lines and answers."""
    start = fiscal_start_month(profile)
    end = (start + 10) % 12 + 1
    names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    amt = money(profile["materiality_amount"], currency=currency_symbol(profile.get("currency", "USD")))
    return f"FY {names[start-1]}–{names[end-1]} · {profile['currency']} · materiality {amt} / {num(profile['materiality_pct'])}%"


# ---------------------------------------------------------------- the ledger

def ledger_path(cwd: Optional[str] = None) -> str:
    return os.path.join(magnos_dir(cwd), "ledger.jsonl")


def ledger_append(entry: Dict[str, Any], cwd: Optional[str] = None) -> Dict[str, Any]:
    """Append one calculation to .magnos/ledger.jsonl; returns the stored entry."""
    os.makedirs(magnos_dir(cwd), exist_ok=True)
    stored = {"ts": _dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds")}
    stored.update({k: (str(v) if isinstance(v, Decimal) else v) for k, v in entry.items()})
    with open(ledger_path(cwd), "a", encoding="utf-8") as fh:
        fh.write(json.dumps(stored, ensure_ascii=False) + "\n")
    return stored


def ledger_read(cwd: Optional[str] = None, since: Optional[str] = None, limit: int = 2000) -> List[Dict[str, Any]]:
    path = ledger_path(cwd)
    if not os.path.exists(path):
        return []
    out = []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            try:
                e = json.loads(line)
            except json.JSONDecodeError:
                continue
            if since and str(e.get("ts", "")) < since:
                continue
            out.append(e)
    return out[-limit:]


# ---------------------------------------------------------------- calculations

class CalcError(ValueError):
    pass


_TOKEN = re.compile(r"\s*(?:(?P<num>(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?)(?P<suffix>%|[kKmMbB](?![a-zA-Z]))?|(?P<name>[A-Za-z_]+)|(?P<op>[-+*/(),−×÷]))")
_FUNCS = {"sum", "avg", "mean", "min", "max", "abs", "round"}


def calc_eval(expression: str) -> Decimal:
    """Exact decimal arithmetic: + − × ÷ ( ), %, K/M/B suffixes, sum avg min max abs round.

    Thousands commas are not allowed (a comma separates arguments); "$" is ignored.
    """
    src = expression.replace("$", "").replace("_", "")
    pos, toks = 0, []
    while pos < len(src):
        if src[pos].isspace():
            pos += 1
            continue
        m = _TOKEN.match(src, pos)
        if not m or m.end() == pos:
            raise CalcError(f"cannot read {src[pos:pos+12]!r}")
        pos = m.end()
        if m.group("num") is not None:
            v = Decimal(m.group("num"))
            suf = m.group("suffix")
            if suf == "%":
                v /= 100
            elif suf:
                v *= _SCALE_WORDS[suf.lower()]
            toks.append(("num", v))
        elif m.group("name"):
            nm = m.group("name").lower()
            if nm not in _FUNCS:
                raise CalcError(f"unknown name {m.group('name')!r}; use numbers and {sorted(_FUNCS)}")
            toks.append(("fn", nm))
        else:
            op = {"−": "-", "×": "*", "÷": "/"}.get(m.group("op"), m.group("op"))
            toks.append(("op", op))
    toks.append(("end", None))
    i = 0

    def peek():
        return toks[i]

    def take(kind=None, val=None):
        nonlocal i
        t = toks[i]
        if kind and (t[0] != kind or (val is not None and t[1] != val)):
            raise CalcError(f"expected {val or kind}, found {t[1]!r}")
        i += 1
        return t

    def expr():
        v = term()
        while peek() in (("op", "+"), ("op", "-")):
            op = take()[1]
            r = term()
            v = v + r if op == "+" else v - r
        return v

    def term():
        v = factor()
        while peek() in (("op", "*"), ("op", "/")):
            op = take()[1]
            r = factor()
            if op == "/" and r == 0:
                raise CalcError("division by zero")
            v = v * r if op == "*" else v / r
        return v

    def factor():
        if peek() == ("op", "-"):
            take()
            return -factor()
        if peek() == ("op", "+"):
            take()
            return factor()
        return primary()

    def primary():
        t = peek()
        if t[0] == "num":
            return take()[1]
        if t == ("op", "("):
            take()
            v = expr()
            take("op", ")")
            return v
        if t[0] == "fn":
            fn = take()[1]
            take("op", "(")
            args = [expr()]
            while peek() == ("op", ","):
                take()
                args.append(expr())
            take("op", ")")
            if fn == "sum":
                return sum(args, D0)
            if fn in ("avg", "mean"):
                return sum(args, D0) / len(args)
            if fn == "min":
                return min(args)
            if fn == "max":
                return max(args)
            if fn == "abs":
                return abs(args[0])
            if fn == "round":
                n = int(args[1]) if len(args) > 1 else 0
                return _q(args[0], n)
        raise CalcError(f"unexpected {t[1]!r}")

    v = expr()
    if peek()[0] != "end":
        raise CalcError(f"unexpected {peek()[1]!r}")
    return v


def pretty_formula(expression: str) -> str:
    """"(4950-4870)/4870" -> "(4,950 − 4,870) ÷ 4,870" for the ledger and the Figures pane."""
    def group(m: re.Match) -> str:
        whole, frac = m.group(1), m.group(2) or ""
        return f"{int(whole):,}{frac}" if len(whole) > 3 else m.group(0)
    s = re.sub(r"(?<![\d.])(\d+)(\.\d+)?", group, expression.replace("$", ""))
    s = re.sub(r"\s*\*\s*", " × ", s)
    s = re.sub(r"\s*/\s*", " ÷ ", s)
    s = re.sub(r"(?<=[\w)%])\s*-\s*", " − ", s)
    s = re.sub(r"\s*\+\s*", " + ", s)
    return re.sub(r"\s+", " ", s).strip()


def calc(expression: str, label: str = "", kind: str = "number", unit: str = "auto",
         decimals: Optional[int] = None, cwd: Optional[str] = None, log: bool = True) -> Dict[str, Any]:
    """Evaluate, format and log one calculation. kind: money, pct (ratio), pts, multiple, number."""
    value = calc_eval(expression)
    display = fmt(value, kind=kind, unit=unit, decimals=decimals)
    entry = {"label": label or expression, "value": str(value), "display": display,
             "formula": pretty_formula(expression), "kind": kind, "tool": "calc"}
    if log:
        ledger_append(entry, cwd)
    return entry


def variance(actual: Any, budget: Any, is_cost: bool = False, label: str = "",
             cwd: Optional[str] = None, log: bool = True) -> Dict[str, Any]:
    """Actual against budget. favourable: revenue above budget, cost below it.

    diff is actual − budget; better is the favourable amount (positive when better).
    """
    a, b = dec(actual), dec(budget)
    diff = a - b
    better = -diff if is_cost else diff
    p = None if b == 0 else diff / abs(b)
    out = {
        "label": label, "actual": str(a), "budget": str(b), "diff": str(diff), "better": str(better),
        "pct": None if p is None else str(p), "favourable": better >= 0,
        "display": {
            "actual": money(a), "budget": money(b), "diff": money(diff, signed=True),
            "better": money(better, signed=True),
            "pct": None if p is None else pct(p, signed=True),
            "better_pct": None if p is None else pct(-p if is_cost else p, signed=True),
        },
    }
    if log:
        for key, val, disp, formula in (
            ("variance", diff, out["display"]["diff"], f"{num(a)} − {num(b)}"),
            ("variance %", p, out["display"]["pct"], f"({num(a)} − {num(b)}) ÷ {num(abs(b))}"),
        ):
            if val is not None:
                ledger_append({"label": f"{label} {key}".strip(), "value": str(val), "display": disp,
                               "formula": formula, "tool": "variance"}, cwd)
    return out


def pct_change(new: Any, old: Any, label: str = "", cwd: Optional[str] = None, log: bool = True) -> Optional[Dict[str, Any]]:
    n, o = dec(new), dec(old)
    if o == 0:
        return None
    ch = (n - o) / abs(o)
    out = {"label": label, "value": str(ch), "display": pct(ch, signed=True),
           "formula": f"({num(n)} − {num(o)}) ÷ {num(abs(o))}", "tool": "pct_change"}
    if log:
        ledger_append(dict(out), cwd)
    return out


def bridge(start: Tuple[str, Any], steps: Sequence[Tuple[str, Any]], end_label: str = "End",
           expected_end: Any = None, cwd: Optional[str] = None, log: bool = True) -> Dict[str, Any]:
    """A walk from a start value through signed steps to an end value."""
    run = dec(start[1])
    rows = [{"label": start[0], "value": str(run), "running": str(run), "kind": "total"}]
    for lab, v in steps:
        dv = dec(v)
        run += dv
        rows.append({"label": lab, "value": str(dv), "running": str(run), "kind": "step"})
    rows.append({"label": end_label, "value": str(run), "running": str(run), "kind": "total"})
    ties = None if expected_end is None else (_q(run, 2) == _q(dec(expected_end), 2))
    out = {"rows": rows, "end": str(run), "ties": ties}
    if log:
        ledger_append({"label": f"bridge {start[0]} → {end_label}", "value": str(run), "display": money(run),
                       "formula": " ".join([num(dec(start[1]))] + [("+ " if dec(v) >= 0 else "− ") + num(abs(dec(v))) for _, v in steps]),
                       "tool": "bridge"}, cwd)
    return out


# ---------------------------------------------------------------- markdown

def md_table(headers: Sequence[str], rows: Iterable[Sequence[Any]], align: Optional[Sequence[str]] = None) -> str:
    """A GitHub markdown table; align: 'l' or 'r' per column (numbers right by default)."""
    rows = [["" if v is None else str(v) for v in r] for r in rows]
    if align is None:
        align = ["l"] + ["r"] * (len(headers) - 1)
    sep = ["---:" if a == "r" else ":---" for a in align]
    lines = ["| " + " | ".join(headers) + " |", "| " + " | ".join(sep) + " |"]
    lines += ["| " + " | ".join(r) + " |" for r in rows]
    return "\n".join(lines)


def emit(markdown: str, data: Optional[Dict[str, Any]] = None, json_path: Optional[str] = None) -> None:
    """Print the human result; optionally save the machine result as JSON."""
    print(markdown)
    if data is not None and json_path:
        os.makedirs(os.path.dirname(os.path.abspath(json_path)), exist_ok=True)
        with open(json_path, "w", encoding="utf-8") as fh:
            json.dump(data, fh, indent=2, default=str, ensure_ascii=False)


# ---------------------------------------------------------------- figures


@dataclass
class Figure:
    raw: str
    value: str      # the number as shown, without scale (e.g. "4.95")
    kind: str       # money, pct, pts, multiple, count
    decimals: int
    scale: str      # "", K, M, B
    start: int = 0


@dataclass
class Trace:
    figure: Figure
    traced: bool
    source: str = ""


_FIG_RE = re.compile(
    r"""(?P<cur>[$€£])?
        (?P<num>\d{1,3}(?:,\d{3})+(?:\.\d+)?|\d+(?:\.\d+)?)
        (?:\s?(?P<scale>[KMB]|bn|k|thousand|million|billion)(?![A-Za-z]))?
        (?:(?P<pct>\s?%)|\s(?P<pts>pts?|pp|percentage\spoints?)(?![A-Za-z])|(?P<mult>×|x(?![A-Za-z0-9])))?
    """,
    re.X,
)
_SCALE_LETTER = {"k": "K", "thousand": "K", "m": "M", "million": "M", "b": "B", "bn": "B", "billion": "B"}
_UNIT = {"": Decimal(1), "K": Decimal(1000), "M": Decimal(1_000_000), "B": Decimal(1_000_000_000)}


def extract_figures(text: str) -> List[Figure]:
    """The figures in an answer: amounts, percentages, points, multiples and grouped counts.

    Not figures: years, dates, period names (Q3, FY26, v3), account numbers and
    other bare numbers without a currency, a scale, a % or thousands grouping.
    Code blocks and inline code are skipped.
    """
    clean = re.sub(r"```.*?```", lambda m: " " * len(m.group(0)), text, flags=re.S)
    clean = re.sub(r"`[^`\n]*`", lambda m: " " * len(m.group(0)), clean)
    out: List[Figure] = []
    for m in _FIG_RE.finditer(clean):
        s, e = m.span()
        before = clean[max(0, s - 2):s]
        after = clean[e:e + 1]
        if re.search(r"[A-Za-z_]\Z", before) or (before.endswith(("#", "/")) and not m.group("cur")):
            continue  # Q3, FY26, v3, #12
        if after and (after.isalnum() or after in "-–/:") and not (m.group("pct") or m.group("pts") or m.group("mult")):
            if not (m.group("scale") and after in "-–"):
                continue  # 2026-09-30, 6100-6199, 10:30, 3rd
        if clean[max(0, s - 1):s] in ("-", "–") and re.search(r"\d\Z", clean[max(0, s - 3):s - 1]) and not (m.group("cur") or m.group("pct")):
            continue  # the second half of a range of plain numbers
        number = m.group("num")
        scale = _SCALE_LETTER.get((m.group("scale") or "").lower(), "")
        if m.group("pct"):
            kind = "pct"
        elif m.group("pts"):
            kind = "pts"
        elif m.group("mult"):
            kind = "multiple"
        elif m.group("cur") or scale:
            kind = "money"
        elif "," in number:
            kind = "count"
        else:
            continue
        digits = number.replace(",", "")
        if kind == "count" and re.fullmatch(r"(19|20)\d\d", digits):
            continue
        if Decimal(digits) == 0:
            continue
        decs = len(digits.split(".")[1]) if "." in digits else 0
        out.append(Figure(m.group(0).strip(), digits, kind, decs, scale, s))
    return out


_EVID_RE = re.compile(
    r"(?P<num>\d[\d,]*(?:\.\d+)?|\.\d+)(?:\s?(?P<scale>[KMB]|bn|k|thousand|million|billion)(?![A-Za-z]))?(?P<pct>\s?%)?"
)
_DATE_RE = re.compile(r"\b\d{4}-\d{1,2}-\d{1,2}(?:[T ]\d{1,2}:\d{2}(?::\d{2})?(?:\.\d+)?Z?)?\b|\b\d{1,2}/\d{1,2}/\d{2,4}\b|\b\d{1,2}:\d{2}(?::\d{2})?\b")


_COUNT_NOUNS = (r"lines?|rows?|accounts?|deals?|items?|customers?|clients?|logos?|reps?|people|persons?|users?|seats?|"
                r"employees?|files?|figures?|records?|entries|entry|transactions?|invoices?|orders?|products?|days?|weeks?|"
                r"months?|quarters?|years?|steps?|scenes?|chapters?|words?|characters?|values?|matches|columns?|sheets?|"
                r"cells?|formulas?|clips?|seconds?|minutes?|hours?|journals?|vendors?|suppliers?|entities|times")
_COUNT_AFTER = re.compile(rf"^\s*(?:of\s+[\d,]+\s+)?(?:[A-Za-z&'-]+\s+){{0,2}}(?:{_COUNT_NOUNS})\b", re.I)


class Evidence:
    """Every number in the evidence, searchable by value at any scale.

    Two tiers. Strong evidence is computed or stated: the calculator's ledger,
    script output, the user's own messages. Raw evidence is file contents as
    read. A figure with fewer than three significant digits ("$1.2M", "12%")
    can match strong evidence only: in a raw export of thousands of numbers,
    something always rounds to it.

    Numbers that count things ("1,221 bank lines", "14 reps") are kept apart:
    they can trace a count, never an amount or a percentage.
    """

    def __init__(self) -> None:
        # (strong, is_count) -> sorted values and their sources
        self._vals: Dict[Tuple[bool, bool], List[float]] = {(a, b): [] for a in (True, False) for b in (True, False)}
        self._src: Dict[Tuple[bool, bool], List[str]] = {(a, b): [] for a in (True, False) for b in (True, False)}
        self._sorted = True

    def add_text(self, text: str, source: str, strong: bool = True) -> None:
        text = _DATE_RE.sub(" ", text or "")
        for m in _EVID_RE.finditer(text):
            raw = m.group("num").replace(",", "")
            try:
                v = abs(float(raw))
            except ValueError:
                continue
            scale = _SCALE_LETTER.get((m.group("scale") or "").lower(), "")
            if not scale and not m.group("pct") and "." not in raw and 1900 <= v <= 2100:
                continue  # a year
            is_count = (not scale and not m.group("pct") and "." not in raw
                        and _COUNT_AFTER.match(text[m.end():m.end() + 60]) is not None)
            self._add(v, source, strong, is_count)
            if scale:
                self._add(v * float(_UNIT[scale]), source, strong, False)
            if m.group("pct"):
                self._add(v / 100, source, strong, False)

    def add_value(self, value: Any, source: str, strong: bool = True) -> None:
        dv = to_decimal(value)
        if dv is not None:
            self._add(abs(float(dv)), source, strong, False)

    def _add(self, v: float, source: str, strong: bool, is_count: bool) -> None:
        self._vals[(strong, is_count)].append(v)
        self._src[(strong, is_count)].append(source)
        self._sorted = False

    def _ensure(self) -> None:
        if not self._sorted:
            for key in self._vals:
                pairs = sorted(zip(self._vals[key], self._src[key]), key=lambda p: p[0])
                self._vals[key] = [p[0] for p in pairs]
                self._src[key] = [p[1] for p in pairs]
            self._sorted = True

    def find(self, lo: float, hi: float, strong: bool = True, counts: bool = False) -> Optional[str]:
        """A source in the tier holding a value in [lo, hi), or None. counts: search counting numbers too."""
        self._ensure()
        for key in ((strong, False), (strong, True)) if counts else ((strong, False),):
            vals = self._vals[key]
            i = bisect.bisect_left(vals, lo)
            if i < len(vals) and vals[i] < hi:
                return self._src[key][i]
        return None

    def __len__(self) -> int:
        return sum(len(v) for v in self._vals.values())


def significant_digits(value: str) -> int:
    digits = value.replace(".", "").lstrip("0")
    return len(digits)


def trace_figure(fig: Figure, ev: Evidence) -> Trace:
    """Trace one figure: at the precision shown, at any scale (K, M), counts only for counts.

    A precise figure (three significant digits or more) names the file it came
    from when the file holds it; a rough one must come from a computed or
    stated value.
    """
    v = float(fig.value)
    h = 0.5 * 10 ** (-fig.decimals)
    tol = 1e-9 * max(1.0, v)
    counts = fig.kind == "count"
    if fig.kind in ("pct", "pts"):
        windows = [(v - h - tol, v + h), ((v - h) / 100 - tol, (v + h) / 100)]
        raw_windows = windows[:1]
    elif counts:
        # A grouped number is a count ("1,221 lines") or an amount in a $K or $M table ("35,590"):
        # it matches counting numbers at face value, other numbers at any scale.
        face = (v - h - tol, v + h)
        windows = [(face[0] / s, face[1] / s) for s in (1.0, 1e3, 1e6, 1e-3)]
        raw_windows = windows
    else:
        u = float(_UNIT[fig.scale])
        lo, hi = (v - h) * u - tol, (v + h) * u
        windows = [(lo / s, hi / s) for s in (1.0, 1e3, 1e6, 1e-3)]
        raw_windows = windows
    precise = significant_digits(fig.value) >= 3
    tiers = ((False, raw_windows), (True, windows)) if precise else ((True, windows),)
    for strong, wins in tiers:
        for i, (lo, hi) in enumerate(wins):
            src = ev.find(max(lo, 0.0), hi, strong=strong, counts=counts and i == 0)
            if src:
                return Trace(fig, True, src)
    return Trace(fig, False, "")


def trace_figures(text: str, ev: Evidence) -> List[Trace]:
    return [trace_figure(f, ev) for f in extract_figures(text)]


def evidence_from_files(paths: Sequence[str], ledger: bool = False, cwd: Optional[str] = None,
                        ev: Optional[Evidence] = None) -> Evidence:
    """Evidence from files: data files cell by cell (raw evidence, sourced "file · column, row" or
    "file · Sheet!B2"), other text files whole (strong: script output, notes), plus the ledger."""
    ev = ev or Evidence()
    for path in paths:
        name = os.path.basename(path)
        low = path.lower()
        try:
            if low.endswith((".xlsx", ".xlsm")):
                wb = read_xlsx(path)
                for sheet in wb.sheet_names:
                    for ref, cell in wb.cells(sheet).items():
                        src = f"{name} · {sheet}!{ref}"
                        if isinstance(cell.value, Decimal):
                            ev.add_value(cell.value, src, strong=False)
                        elif cell.value not in ("", None):
                            ev.add_text(str(cell.value), src, strong=False)
            elif low.endswith((".csv", ".tsv")):
                t = read_table(path)
                for i, row in enumerate(t.rows, start=2):
                    for col in t.columns:
                        v = row.get(col, "")
                        if not v:
                            continue
                        dv = to_decimal(v)
                        src = f"{name} · {col}, row {i}"
                        if dv is not None:
                            ev.add_value(dv, src, strong=False)
                        else:
                            ev.add_text(v, src, strong=False)
            else:
                with open(path, encoding="utf-8", errors="replace") as fh:
                    ev.add_text(fh.read(), name, strong=True)
        except (OSError, zipfile.BadZipFile, ET.ParseError, KeyError, ValueError):
            continue
    if ledger:
        for e in ledger_read(cwd):
            src = f"calc · {e.get('formula') or e.get('label', '')}"
            ev.add_value(e.get("value"), src)
            ev.add_text(str(e.get("display", "")), src)
    return ev


def figures_report(traces: Sequence[Trace]) -> Dict[str, Any]:
    total = len(traces)
    traced = sum(1 for t in traces if t.traced)
    return {
        "total": total, "traced": traced, "untraced": total - traced,
        "figures": [{"raw": t.figure.raw, "kind": t.figure.kind, "traced": t.traced, "source": t.source} for t in traces],
    }


# ---------------------------------------------------------------- command line

def _cli(argv: Optional[Sequence[str]] = None) -> int:
    p = argparse.ArgumentParser(prog="magnos_fin.py", description="Magnos finance helpers")
    sub = p.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("calc", help="exact arithmetic, logged to .magnos/ledger.jsonl")
    c.add_argument("expression")
    c.add_argument("--label", default="")
    c.add_argument("--kind", default="number", choices=["money", "pct", "pts", "multiple", "number"])
    c.add_argument("--unit", default="auto")
    c.add_argument("--decimals", type=int)
    v = sub.add_parser("variance", help="actual against budget")
    v.add_argument("--actual", required=True)
    v.add_argument("--budget", required=True)
    v.add_argument("--cost", action="store_true", help="the line is a cost: below budget is favourable")
    v.add_argument("--label", default="")
    f = sub.add_parser("figures", help="trace the figures of a text against evidence files")
    f.add_argument("text_file")
    f.add_argument("evidence", nargs="*")
    f.add_argument("--ledger", action="store_true", help="also use .magnos/ledger.jsonl")
    sub.add_parser("profile", help="show the finance profile")
    a = p.parse_args(argv)
    if a.cmd == "calc":
        r = calc(a.expression, a.label, a.kind, a.unit, a.decimals)
        print(f"{r['label']}: {r['display']}  ({r['formula']} = {r['value']})")
    elif a.cmd == "variance":
        r = variance(a.actual, a.budget, a.cost, a.label)
        d = r["display"]
        print(f"{a.label or 'variance'}: actual {d['actual']}, budget {d['budget']}, "
              f"{'better' if r['favourable'] else 'worse'} by {money(abs(dec(r['better'])))} ({d['better_pct']})")
    elif a.cmd == "figures":
        ev = evidence_from_files(a.evidence, ledger=a.ledger)
        with open(a.text_file, encoding="utf-8") as fh:
            rep = figures_report(trace_figures(fh.read(), ev))
        for fig in rep["figures"]:
            mark = "✓" if fig["traced"] else "✕"
            print(f"{mark} {fig['raw']}  {fig['source'] or 'not found in any file or calculation'}")
        print(f"{rep['total']} figures · {rep['traced']} traced")
        return 0 if rep["untraced"] == 0 else 1
    elif a.cmd == "profile":
        prof = load_profile()
        print(profile_line(prof) + f"  ({prof['_source']})")
    return 0


if __name__ == "__main__":
    sys.exit(_cli())
