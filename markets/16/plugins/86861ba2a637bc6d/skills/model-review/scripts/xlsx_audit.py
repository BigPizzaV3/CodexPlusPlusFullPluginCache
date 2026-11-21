#!/usr/bin/env python3
"""Model review: map every formula of a workbook and list what to fix before it goes to the board.

Reads the workbook (never writes it) and reports, each with sheet, cell and formula:

  1. typed numbers inside formulas: constants in arithmetic other than 0, 1, 12 and 100
     as written ("1.00" counts: it is a rate typed in), and formulas that are only a number (=1412);
  2. formulas that break their row's pattern, compared in relative (R1C1) form;
  3. links to other files: external link parts and [file.xlsx] references;
  4. totals (SUM) whose range leaves out filled cells next to it in the same row or column;
  5. error values (#REF!, #DIV/0!, #N/A, #VALUE! and the rest).

  python3 scripts/xlsx_audit.py Budget_FY27.xlsx
  python3 scripts/xlsx_audit.py model.xlsx --allow 1000 --allow 365

Prints Markdown; saves the full result to .magnos/runs/model-review.json. Writes nothing else.
"""
from __future__ import annotations

import argparse
import os
import posixpath
import re
import sys
import zipfile
from dataclasses import dataclass
from decimal import Decimal
from typing import Dict, List, Optional, Sequence, Set, Tuple
from urllib.parse import unquote
from xml.etree import ElementTree as ET

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import magnos_fin as mf  # noqa: E402

JSON_PATH = os.path.join(".magnos", "runs", "model-review.json")
ALLOWED = {"0", "1", "12", "100"}
ARITH = set("+-*/^")
SHORT_MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
LONG_MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September",
               "October", "November", "December"]
WORDS = ["Nothing", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]
ERRORS = ("#NULL!", "#DIV/0!", "#VALUE!", "#REF!", "#NAME?", "#NUM!", "#N/A", "#SPILL!", "#CALC!", "#GETTING_DATA")


class InputError(Exception):
    """A problem with the person's file or flags: exit 2 with one plain sentence."""


# ---------------------------------------------------------------- formula tokens

_TOKEN = re.compile(r"""
  (?P<str>"(?:[^"]|"")*")
| (?P<err>\#(?:NULL!|DIV/0!|VALUE!|REF!|NAME\?|NUM!|N/A|SPILL!|CALC!|GETTING_DATA))
| (?P<ref>(?:'(?:[^']|'')+'!|\[\d+\][^!\s'"(),;:]*!|\[[^\]]+\][^!\s'"(),;:]*!|[A-Za-z_\\][A-Za-z0-9_.]*!)?
     \$?[A-Za-z]{1,3}\$?\d+(?::\$?[A-Za-z]{1,3}\$?\d+)?)(?![A-Za-z0-9_(.!])
| (?P<func>[A-Za-z_][A-Za-z0-9_.]*(?=\s*\())
| (?P<num>(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?%?)
| (?P<name>(?:'(?:[^']|'')+'!|\[\d+\][^!\s]*!|[A-Za-z_\\][A-Za-z0-9_.]*!)?[A-Za-z_\\][A-Za-z0-9_.?\\]*)
| (?P<ws>\s+)
| (?P<op><>|<=|>=|.)
""", re.X | re.S)
_CELL = re.compile(r"(\$?)([A-Za-z]{1,3})(\$?)(\d+)")


@dataclass
class Tok:
    kind: str
    text: str


def tokens(formula: str) -> List[Tok]:
    out, pos = [], 0
    while pos < len(formula):
        m = _TOKEN.match(formula, pos)
        if not m or m.end() == pos:  # pragma: no cover - the op branch matches any character
            out.append(Tok("op", formula[pos]))
            pos += 1
            continue
        out.append(Tok(m.lastgroup, m.group(0)))
        pos = m.end()
    return out


def split_prefix(ref: str) -> Tuple[str, str]:
    """"Opex!B14:G14" -> ("Opex!", "B14:G14")."""
    i = ref.rfind("!")
    return (ref[:i + 1], ref[i + 1:]) if i >= 0 else ("", ref)


def sheet_of(prefix: str) -> str:
    s = prefix[:-1] if prefix.endswith("!") else prefix
    if s.startswith("'") and s.endswith("'"):
        s = s[1:-1].replace("''", "'")
    return s


def is_external(prefix: str) -> bool:
    return "[" in prefix and "]" in prefix


def _move(part: str, d_row: int, d_col: int) -> str:
    m = _CELL.fullmatch(part)
    if not m:
        return part
    ca, letters, ra, digits = m.groups()
    c = mf.col_number(letters) + (0 if ca else d_col)
    r = int(digits) + (0 if ra else d_row)
    if c < 1 or r < 1:
        return "#REF!"
    return f"{ca}{mf.col_letter(c)}{ra}{r}"


def shift_formula(formula: str, d_row: int, d_col: int) -> str:
    """Move the relative references of a shared formula; absolute parts stay, on any sheet.

    Replaces magnos_fin.shift_formula, which moves the column of "Assumptions!$B$3"
    (the "$" after "!" hides the absolute marker from its pattern).
    """
    out = []
    for t in tokens(formula):
        if t.kind == "ref":
            prefix, body = split_prefix(t.text)
            out.append(prefix + ":".join(_move(p, d_row, d_col) for p in body.split(":")))
        else:
            out.append(t.text)
    return "".join(out)


mf.shift_formula = shift_formula  # read_xlsx expands shared formulas with it


def r1c1(formula: str, row: int, col: int) -> str:
    """The formula in relative form, so that a row's filled-right formulas read the same."""
    out = []
    for t in tokens(formula):
        if t.kind == "ws":
            continue
        if t.kind == "ref":
            prefix, body = split_prefix(t.text)
            parts = []
            for p in body.split(":"):
                m = _CELL.fullmatch(p)
                ca, letters, ra, digits = m.groups()
                c, r = mf.col_number(letters), int(digits)
                rs = f"R{r}" if ra else ("R" if r == row else f"R[{r - row}]")
                cs = f"C{c}" if ca else ("C" if c == col else f"C[{c - col}]")
                parts.append(rs + cs)
            out.append(prefix.upper() + ":".join(parts))
        elif t.kind in ("func", "name"):
            out.append(t.text.upper())
        else:
            out.append(t.text)
    return "".join(out)


def _unary(sig: Sequence[Tok], j: int) -> bool:
    """Whether the + or - at sig[j] is a sign rather than an operation."""
    if j == 0:
        return True
    p = sig[j - 1]
    return p.kind == "op" and p.text not in (")", "%")


def typed_numbers(formula: str, allowed: Set[str]) -> Tuple[List[str], bool]:
    """(typed constants in arithmetic, whether the formula is only a number)."""
    sig = [t for t in tokens(formula) if t.kind != "ws"]
    core = [t for i, t in enumerate(sig) if not (t.kind == "op" and (t.text in "()" or (t.text in "+-" and _unary(sig, i))))]
    if len(core) == 1 and core[0].kind == "num":
        return [core[0].text], True
    found = []
    for i, t in enumerate(sig):
        if t.kind != "num" or t.text in allowed:
            continue
        j = i - 1
        while j >= 0 and sig[j].kind == "op" and sig[j].text in "+-" and _unary(sig, j):
            j -= 1
        before = j >= 0 and sig[j].kind == "op" and sig[j].text in ARITH and not _unary(sig, j)
        nxt = sig[i + 1] if i + 1 < len(sig) else None
        after = nxt is not None and nxt.kind == "op" and nxt.text in ARITH
        if before or after:
            found.append(t.text)
    return found, False


def sum_ranges(formula: str) -> List[str]:
    """The range arguments (A1:B2 form) given directly to SUM."""
    stack: List[Optional[str]] = []
    pending: Optional[str] = None
    out = []
    for t in tokens(formula):
        if t.kind == "ws":
            continue
        if t.kind == "func":
            pending = t.text.upper()
            continue
        if t.kind == "op" and t.text == "(":
            stack.append(pending)
            pending = None
            continue
        pending = None
        if t.kind == "op" and t.text == ")":
            if stack:
                stack.pop()
            continue
        if t.kind == "ref" and ":" in t.text and stack and stack[-1] == "SUM":
            out.append(t.text)
    return out


# ---------------------------------------------------------------- the workbook

def external_books(path: str) -> Dict[int, str]:
    """[n] in formulas -> the linked file, in the order of workbook.xml's externalReferences."""
    ns_m = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
    ns_r = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
    ns_p = "http://schemas.openxmlformats.org/package/2006/relationships"
    out: Dict[int, str] = {}
    with zipfile.ZipFile(path) as z:
        names = set(z.namelist())
        wb = ET.fromstring(z.read("xl/workbook.xml"))
        rels = {}
        if "xl/_rels/workbook.xml.rels" in names:
            for r in ET.fromstring(z.read("xl/_rels/workbook.xml.rels")).findall(f"{{{ns_p}}}Relationship"):
                rels[r.get("Id")] = r.get("Target", "")
        refs = wb.find(f"{{{ns_m}}}externalReferences")
        if refs is None:
            return out
        for i, er in enumerate(refs.findall(f"{{{ns_m}}}externalReference"), start=1):
            target = rels.get(er.get(f"{{{ns_r}}}id"), "")
            part = posixpath.normpath(posixpath.join("xl", target)) if not target.startswith("/") else target.lstrip("/")
            rel = posixpath.join(posixpath.dirname(part), "_rels", posixpath.basename(part) + ".rels")
            if rel in names:
                for r in ET.fromstring(z.read(rel)).findall(f"{{{ns_p}}}Relationship"):
                    if r.get("Target"):
                        out[i] = r.get("Target")
                        break
            out.setdefault(i, f"external link {i}")
    return out


def file_label(target: str) -> str:
    t = unquote(target.replace("\\", "/"))
    if t.startswith("file:///"):
        t = t[8:]
    return t.rsplit("/", 1)[-1] or target


@dataclass
class Book:
    path: str
    wb: mf.Workbook
    links: Dict[int, str]

    def cell(self, sheet: str, row: int, col: int) -> Optional[mf.Cell]:
        return self.wb.cells(sheet).get(f"{mf.col_letter(col)}{row}")

    def is_num(self, sheet: str, row: int, col: int) -> bool:
        c = self.cell(sheet, row, col)
        return c is not None and isinstance(c.value, Decimal)

    def text(self, sheet: str, row: int, col: int) -> str:
        c = self.cell(sheet, row, col)
        if c is None or isinstance(c.value, (Decimal, bool)) or c.kind == "e":
            return ""
        return str(c.value).strip()

    def row_label(self, sheet: str, row: int, col: int) -> str:
        for c in range(1, col):
            t = self.text(sheet, row, c)
            if t:
                return t
        return ""

    def col_label(self, sheet: str, row: int, col: int) -> str:
        for r in range(row - 1, 0, -1):
            t = self.text(sheet, r, col)
            if t:
                return t
        return ""


def load(path: str) -> Book:
    if not os.path.exists(path):
        raise InputError(f"Cannot find {path}. Check the path, or run the command from the folder that holds it.")
    if os.path.isdir(path):
        raise InputError(f"{path} is a folder. Name the workbook inside it.")
    low = path.lower()
    if low.endswith(".xls"):
        raise InputError(f"{os.path.basename(path)} is an old .xls workbook. Save it as .xlsx in Excel and run the review again.")
    if not low.endswith((".xlsx", ".xlsm")):
        raise InputError(f"{os.path.basename(path)} is not an Excel workbook. Give an .xlsx or .xlsm file.")
    try:
        wb = mf.read_xlsx(path)
        links = external_books(path)
    except (zipfile.BadZipFile, KeyError, ET.ParseError) as exc:
        raise InputError(f"Cannot read {os.path.basename(path)} as an Excel workbook ({exc.__class__.__name__}). "
                         "Open it in Excel, save it as .xlsx and try again.")
    for i, t in enumerate(wb.external_links, start=1):
        links.setdefault(i, t)
    return Book(path, wb, links)


# ---------------------------------------------------------------- checks

def month_word(label: str) -> str:
    return LONG_MONTHS[SHORT_MONTHS.index(label)] if label in SHORT_MONTHS else label


def is_month(label: str) -> bool:
    return label in SHORT_MONTHS or label in LONG_MONTHS


def display(formula: str, book: Book) -> str:
    """The formula as Excel shows it: "=" and [1] replaced by the linked file's name."""
    out = []
    for t in tokens(formula):
        if t.kind in ("ref", "name"):
            def repl(m: re.Match) -> str:
                return "[" + file_label(book.links.get(int(m.group(1)), f"link {m.group(1)}")) + "]"
            out.append(re.sub(r"\[(\d+)\]", repl, t.text))
        else:
            out.append(t.text)
    return "=" + "".join(out)


def formulas(book: Book) -> List[Tuple[str, mf.Cell]]:
    out = []
    for sheet in book.wb.sheet_names:
        cells = sorted(book.wb.cells(sheet).values(), key=lambda c: (c.row, c.col))
        out += [(sheet, c) for c in cells if c.formula]
    return out


def check_typed(book: Book, allowed: Set[str]) -> List[dict]:
    out = []
    for sheet, c in formulas(book):
        found, only = typed_numbers(c.formula, allowed)
        if found:
            out.append({"sheet": sheet, "cell": c.ref, "formula": display(c.formula, book),
                        "numbers": found, "only_a_number": only})
    return out


def _is_row_total(book: Book, sheet: str, c: mf.Cell) -> bool:
    for rng in sum_ranges(c.formula or ""):
        prefix, body = split_prefix(rng)
        if prefix and sheet_of(prefix) != sheet:
            continue
        a, b = body.replace("$", "").split(":")
        (ac, ar), (bc, br) = mf.split_ref(a), mf.split_ref(b)
        if ar == br == c.row and mf.col_number(bc) < c.col:
            return True
    return False


def check_patterns(book: Book) -> List[dict]:
    out = []
    for sheet in book.wb.sheet_names:
        rows: Dict[int, List[mf.Cell]] = {}
        for c in book.wb.cells(sheet).values():
            if c.formula and not typed_numbers(c.formula, ALLOWED)[1]:
                rows.setdefault(c.row, []).append(c)
        for row, cells in sorted(rows.items()):
            cells.sort(key=lambda c: c.col)
            if len(cells) < 3:
                continue
            forms = [r1c1(c.formula, c.row, c.col) for c in cells]
            counts: Dict[str, int] = {}
            for f in forms:
                counts[f] = counts.get(f, 0) + 1
            ranked = sorted(counts.items(), key=lambda kv: -kv[1])
            top, n_top = ranked[0]
            if n_top < 3 or n_top < 0.6 * len(cells) or (len(ranked) > 1 and ranked[1][1] == n_top):
                continue
            chain = re.search(r"(?<![A-Z\]])RC\[-\d+\]", top) is not None
            rep = next(c for c, f in zip(cells, forms) if f == top)
            for i, (c, f) in enumerate(zip(cells, forms)):
                if f == top or counts[f] > 2:
                    continue
                if i == 0 and chain:
                    continue  # the first month of a chain starts it
                if i == len(cells) - 1 and _is_row_total(book, sheet, c):
                    continue  # a total column at the end of the row
                labels = [book.col_label(sheet, x.row, x.col) for x in cells if x is not c]
                out.append({"sheet": sheet, "cell": c.ref, "formula": display(c.formula, book),
                            "pattern": display(rep.formula, book), "pattern_cell": rep.ref,
                            "row_label": book.row_label(sheet, c.row, c.col),
                            "col_label": book.col_label(sheet, c.row, c.col),
                            "months": bool(labels) and all(is_month(x) for x in labels if x)})
    return out


def check_links(book: Book) -> List[dict]:
    out = []
    used: Set[int] = set()
    here = os.path.dirname(os.path.abspath(book.path))

    def files_in(formula: str) -> List[str]:
        found = []
        for t in tokens(formula):
            if t.kind not in ("ref", "name"):
                continue
            for m in re.finditer(r"\[(\d+)\]", t.text):
                used.add(int(m.group(1)))
                found.append(file_label(book.links.get(int(m.group(1)), f"external link {m.group(1)}")))
            for m in re.finditer(r"\[([^\]]+\.(?:xlsx|xlsm|xlsb|xls|xltx|csv|ods))\]", t.text, re.I):
                found.append(file_label(m.group(1)))
        return sorted(set(found))

    for sheet, c in formulas(book):
        files = files_in(c.formula)
        if files:
            out.append({"sheet": sheet, "cell": c.ref, "formula": display(c.formula, book), "files": files,
                        "in_folder": [os.path.exists(os.path.join(here, f)) for f in files],
                        "row_label": book.row_label(sheet, c.row, c.col)})
    for name, ref in sorted(book.wb.defined_names.items()):
        files = files_in(ref)
        if files:
            out.append({"sheet": "", "cell": f"name {name}", "formula": display(ref, book), "files": files,
                        "in_folder": [os.path.exists(os.path.join(here, f)) for f in files], "row_label": name})
    for i, target in sorted(book.links.items()):
        if i not in used:
            f = file_label(target)
            out.append({"sheet": "", "cell": "", "formula": "", "files": [f],
                        "in_folder": [os.path.exists(os.path.join(here, f))], "row_label": "",
                        "unused": True})
    return out


def _covers(book: Book, sheet: str, c: mf.Cell, vertical: bool, line: int, lo: int, hi: int) -> bool:
    """Whether cell c is itself a total of this line (a SUM over it), so a block stops there."""
    for rng in sum_ranges(c.formula or ""):
        prefix, body = split_prefix(rng)
        if prefix and sheet_of(prefix) != sheet:
            continue
        a, b = body.replace("$", "").split(":")
        (ac, ar), (bc, br) = mf.split_ref(a), mf.split_ref(b)
        ac, bc = mf.col_number(ac), mf.col_number(bc)
        if vertical and ac <= line <= bc and ar <= lo and br >= hi:
            return True
        if not vertical and ar <= line <= br and ac <= lo and bc >= hi:
            return True
    return False


def check_totals(book: Book) -> List[dict]:
    out = []
    for sheet, c in formulas(book):
        for rng in sum_ranges(c.formula):
            prefix, body = split_prefix(rng)
            if is_external(prefix):
                continue
            target = sheet_of(prefix) if prefix else sheet
            if target not in book.wb.sheet_names:
                continue
            a, b = body.replace("$", "").split(":")
            (ac, ar), (bc, br) = mf.split_ref(a), mf.split_ref(b)
            ac, bc = mf.col_number(ac), mf.col_number(bc)
            if ar == br and bc > ac:
                vertical, line, lo, hi = False, ar, ac, bc
            elif ac == bc and br > ar:
                vertical, line, lo, hi = True, ac, ar, br
            else:
                continue  # one cell, or a block of rows and columns

            def at(k: int) -> Tuple[int, int]:
                return (k, line) if vertical else (line, k)

            def stop(k: int) -> bool:
                r, col = at(k)
                if k < 1 or not book.is_num(target, r, col):
                    return True
                if target == sheet and (r, col) == (c.row, c.col):
                    return True
                return _covers(book, target, book.cell(target, r, col), vertical, line, lo, hi)

            first, last = lo, hi
            while not stop(first - 1):
                first -= 1
            while not stop(last + 1):
                last += 1
            if (first, last) == (lo, hi):
                continue

            def ref(k1: int, k2: int) -> str:
                r1, c1 = at(k1)
                r2, c2 = at(k2)
                return f"{mf.col_letter(c1)}{r1}:{mf.col_letter(c2)}{r2}"

            def label(k1: int, k2: int) -> str:
                if vertical:
                    x, y = book.row_label(target, k1, line), book.row_label(target, k2, line)
                else:
                    x, y = book.col_label(target, line, k1), book.col_label(target, line, k2)
                return f"{x}–{y}" if x and y and x != y else (x or "")

            def gap(k1: int, k2: int) -> str:
                text = ref(k1, k2) if k2 > k1 else ref(k1, k1).split(":")[0]
                lab = label(k1, k2)
                return (prefix if target != sheet else "") + text + (f" ({lab})" if lab else "")

            left_out = []
            if first < lo:
                left_out.append(gap(first, lo - 1))
            if last > hi:
                left_out.append(gap(hi + 1, last))
            heads = [] if vertical else [book.col_label(target, line, k) for k in range(first, last + 1)]
            unit = "rows" if vertical else ("months" if heads and all(is_month(h) for h in heads) else "columns")
            out.append({"sheet": sheet, "cell": c.ref, "formula": display(c.formula, book),
                        "range": (prefix + body) if prefix else body, "range_label": label(lo, hi),
                        "should_be": ref(first, last), "should_be_label": label(first, last),
                        "left_out": left_out, "covered": hi - lo + 1, "filled": last - first + 1, "unit": unit,
                        "row_label": book.row_label(sheet, c.row, c.col)})
    return out


def check_errors(book: Book) -> List[dict]:
    out = []
    for sheet in book.wb.sheet_names:
        for c in sorted(book.wb.cells(sheet).values(), key=lambda c: (c.row, c.col)):
            shown = str(c.value) if c.kind == "e" else ""
            in_formula = sorted({t.text for t in tokens(c.formula) if t.kind == "err"}) if c.formula else []
            if not shown and isinstance(c.value, str) and c.value.strip() in ERRORS:
                shown = c.value.strip()
            if shown or in_formula:
                out.append({"sheet": sheet, "cell": c.ref, "formula": display(c.formula, book) if c.formula else "",
                            "error": shown or in_formula[0], "in_formula": in_formula})
    return out


# ---------------------------------------------------------------- the answer

def at(f: dict) -> str:
    return f"{f['sheet']}!{f['cell']}" if f.get("sheet") else f.get("cell", "")


def code(s: str) -> str:
    return "`" + s.replace("`", "'") + "`" if s else ""


def cell_text(s: str) -> str:
    return s.replace("|", "\\|")


def plural(n: int, one: str, many: str) -> str:
    return f"{n} {one if n == 1 else many}"


def count_word(n: int) -> str:
    return WORDS[n] if n < len(WORDS) else str(n)


def headline_items(book: Book, res: Dict[str, List[dict]]) -> List[Tuple[str, str]]:
    items: List[Tuple[str, str]] = []
    cited = {at(f) for k in ("patterns", "links", "totals", "errors") for f in res[k]}
    typed = res["typed"]
    if typed:
        only = [f for f in typed if f["only_a_number"] and at(f) not in cited]
        arith = [f for f in typed if not f["only_a_number"] and at(f) not in cited]
        rest = [f for f in typed if f not in only and f not in arith]
        ex = (only[:1] + arith[:1] + only[1:2] + arith[1:2] + rest)[:2]
        title = "1 formula has a typed number" if len(typed) == 1 else f"{len(typed)} formulas have typed numbers"
        detail = "For example " + " and ".join(f"{at(f)} is {code(f['formula'])}" for f in ex) + "."
        sheets = [s for s in book.wb.sheet_names if re.search(r"assum|input|driver", s, re.I)]
        detail += f" Move the rates to {sheets[0]}." if sheets else " Put them in an assumptions sheet and point to them."
        items.append((title, detail))
    pats = res["patterns"]
    if pats:
        f = pats[0]
        where = ", ".join(x for x in (f["row_label"], month_word(f["col_label"])) if x) or at(f)
        title = f"{where} breaks the pattern" if len(pats) == 1 else f"{len(pats)} formulas break their row's pattern"
        others = "the other months use" if f["months"] else "the rest of the row uses"
        detail = f"{at(f)} is {code(f['formula'])}; {others} {code(f['pattern'])}."
        if len(pats) > 1:
            detail = "For example " + detail
        items.append((title, detail))
    links = res["links"]
    if links:
        f = links[0]
        files = sorted({x for l in links for x in l["files"]})
        missing = [x for l in links for x, ok in zip(l["files"], l["in_folder"]) if not ok]
        if len(links) == 1 and not f.get("unused"):
            title = f"{f['row_label'] or at(f)} links to another file"
        else:
            title = f"{plural(len(files), 'file is', 'files are')} linked in"
        where = "which is not in this folder" if missing else "which is in this folder"
        if f.get("unused"):
            detail = f"The workbook keeps a link to [{f['files'][0]}] that no formula uses, {where}."
        else:
            detail = f"{at(f)} reads [{f['files'][0]}], {where}."
        if len(links) > 1:
            detail = f"{plural(len([l for l in links if not l.get('unused')]), 'cell reads', 'cells read')} " \
                     f"{', '.join('[' + x + ']' for x in files)}. For example {detail[0].lower() + detail[1:]}"
        items.append((title, detail))
    tots = res["totals"]
    if tots:
        f = tots[0]
        if len(tots) == 1:
            title = f"{f['row_label'] or at(f)} covers {f['covered']} of {f['filled']} {f['unit']}"
        else:
            title = f"{len(tots)} totals leave out rows or columns"
        rl = f" ({f['range_label']})" if f["range_label"] else ""
        sl = f" ({f['should_be_label']})" if f["should_be_label"] else ""
        detail = f"{at(f)} adds {f['range']}{rl}, not {f['should_be']}{sl}."
        if len(tots) > 1:
            detail = "For example " + detail
        items.append((title, detail))
    errs = res["errors"]
    if errs:
        f = errs[0]
        title = f"{plural(len(errs), 'cell shows', 'cells show')} an error value"
        detail = f"For example {at(f)} shows {f['error']}" + (f" ({code(f['formula'])})." if f["formula"] else ".")
        items.append((title, detail))
    return items


def table(headers: Sequence[str], rows: List[List[str]], limit: int) -> str:
    shown = rows[:limit]
    text = mf.md_table(headers, [[cell_text(x) for x in r] for r in shown], align=["l"] * len(headers))
    if len(rows) > limit:
        text += f"\n\n{len(rows) - limit} more in {JSON_PATH}."
    return text


def render(book: Book, res: Dict[str, List[dict]], stats: dict, limit: int) -> Tuple[str, List[Tuple[str, str]]]:
    items = headline_items(book, res)
    name = os.path.basename(book.path)
    out = []
    if items:
        word = count_word(len(items))
        thing = "thing" if len(items) == 1 else "things"
        out.append(f"**{word} {thing} to fix before this goes to the board:**")
        out.append("")
        for i, (title, detail) in enumerate(items, 1):
            out.append(f"{i}. **{title}.** {detail}")
    else:
        out.append(f"**Nothing to fix in {name}:** no typed numbers in formulas, no broken row patterns, "
                   "no links to other files, no short totals and no error values.")
    out.append("")
    out.append(f"Mapped {plural(stats['formulas'], 'formula', 'formulas')} in "
               f"{plural(stats['cells'], 'cell', 'cells')} on {plural(len(book.wb.sheet_names), 'sheet', 'sheets')} "
               f"({', '.join(book.wb.sheet_names)}) of {name}. The workbook was not changed.")
    sections = [
        ("Typed numbers in formulas", res["typed"], ["Sheet", "Cell", "Formula", "Typed number"],
         lambda f: [f["sheet"], f["cell"], code(f["formula"]),
                    "the whole formula" if f["only_a_number"] else ", ".join(f["numbers"])]),
        ("Formulas that break their row's pattern", res["patterns"], ["Sheet", "Cell", "Formula", "The rest of the row"],
         lambda f: [f["sheet"], f["cell"], code(f["formula"]), f"{code(f['pattern'])} (as in {f['pattern_cell']})"]),
        ("Links to other files", res["links"], ["Sheet", "Cell", "Formula", "File", "In this folder"],
         lambda f: [f["sheet"] or "workbook", f["cell"] or "link part, used by no formula", code(f["formula"]),
                    ", ".join(f["files"]), ", ".join("yes" if x else "no" for x in f["in_folder"])]),
        ("Totals that leave out rows or columns", res["totals"], ["Sheet", "Cell", "Formula", "Adds", "Leaves out"],
         lambda f: [f["sheet"], f["cell"], code(f["formula"]),
                    f["range"] + (f" ({f['range_label']})" if f["range_label"] else ""), ", ".join(f["left_out"])]),
        ("Error values", res["errors"], ["Sheet", "Cell", "Formula", "Shows"],
         lambda f: [f["sheet"], f["cell"], code(f["formula"]), f["error"]]),
    ]
    for title, found, headers, row in sections:
        out.append("")
        out.append(f"## {title} ({len(found)})")
        out.append("")
        out.append(table(headers, [row(f) for f in found], limit) if found else "None.")
    return "\n".join(out), items


def main(argv: Optional[Sequence[str]] = None) -> int:
    p = argparse.ArgumentParser(description="Review an Excel model's formulas before it goes to the board. "
                                            "Reads the workbook, never changes it.")
    p.add_argument("workbook", help="the .xlsx or .xlsm file")
    p.add_argument("--allow", action="append", default=[], metavar="NUMBER",
                   help="a constant that is fine in formulas, as written (for example 1000); repeat for more")
    p.add_argument("--limit", type=int, default=60, help="most rows per table (default 60; all are in the JSON)")
    a = p.parse_args(argv)
    try:
        book = load(a.workbook)
        extra = {x.strip() for x in a.allow if x.strip()}
        bad = [x for x in extra if not re.fullmatch(r"(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?%?", x)]
        if bad:
            raise InputError(f"--allow {bad[0]} is not a number as a formula writes it; use, for example, --allow 1000.")
        allowed = ALLOWED | extra
        res = {"typed": check_typed(book, allowed), "patterns": check_patterns(book), "links": check_links(book),
               "totals": check_totals(book), "errors": check_errors(book)}
    except InputError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    stats = {"formulas": len(formulas(book)), "cells": sum(len(book.wb.cells(s)) for s in book.wb.sheet_names)}
    md, items = render(book, res, stats, max(1, a.limit))
    data = {"workbook": os.path.abspath(book.path), "sheets": book.wb.sheet_names, "formulas": stats["formulas"],
            "cells": stats["cells"], "external_links": {str(k): v for k, v in sorted(book.links.items())},
            "allowed_constants": sorted(allowed, key=lambda x: float(x.rstrip("%"))),
            "headline": [{"title": t, "detail": d} for t, d in items],
            "findings": {"typed_numbers": res["typed"], "pattern_breaks": res["patterns"], "links": res["links"],
                         "short_totals": res["totals"], "errors": res["errors"]},
            "changed_workbook": False}
    mf.emit(md, data, JSON_PATH)
    return 0


if __name__ == "__main__":
    sys.exit(main())
