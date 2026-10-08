#!/usr/bin/env python3
"""
extract_changes.py -- Walk a redlined .docx's tracked changes in document
order and produce structured JSON for building a legal issues list.

Outputs four lists:

  content_changes     substantive edits: text inserted/deleted/substituted,
                      counter-edits (text one party inserted that another
                      then deleted), content moved, paragraphs split or
                      merged, table rows/cells structurally added or removed.

  formatting_changes  formatting-only revisions (rPrChange, pPrChange,
                      tblPrChange, tcPrChange, sectPrChange). Excluded from
                      the issues table, but reported so you can confirm
                      nothing substantive is hiding among them -- notably
                      numbering-level changes, which can mean a clause was
                      promoted or demoted rather than merely restyled.

  comments            Word comments and replies, with the text they anchor
                      to. In a counterparty markup these usually carry the
                      negotiating rationale, so they belong in the review
                      even though they aren't revisions.

  unanchored_comments comments whose anchor markers weren't found in the
                      parts scanned (e.g. anchored in a part not read).

Why a script rather than reading the XML directly: Word records
formatting-only edits with dedicated *Change elements that read like
content edits when scanning by eye; revisions nest (an <w:ins> containing
a <w:del> is a counter-edit, not a plain deletion); a substitution is
routinely split by a stray space into what looks like two unrelated
edits; clause numbers usually live in numbering.xml rather than in the
paragraph text; and changes hide in table cells, footnotes, and deleted
paragraph marks. One deterministic pass applies the same rules to all of
it and doesn't tire out on page 40.

Usage:
    python extract_changes.py redline.docx > changes.json
    python extract_changes.py redline.docx --all-parts > changes.json
    python extract_changes.py unpacked_dir/ --markdown > table.md

Inputs: a .docx, an already-unzipped folder, or a bare document.xml
(clause numbering and comments are unavailable for a bare XML file).

By default the body, footnotes, and endnotes are scanned -- legal drafting
puts substantive terms in footnotes often enough that skipping them is a
real risk. --all-parts adds headers and footers. --markdown prints a
starter issues table instead of JSON.

Known limitations, so they aren't discovered the hard way:
  - Clause numbers are computed by replaying Word's numbering counters over
    the marked-up document. Inserted or deleted paragraphs shift the
    numbering Word displays, and lvlRestart/lvlOverride edge cases aren't
    modelled, so treat a number as a locator to verify rather than a
    citation to quote. Paragraphs numbered by a style rather than direct
    formatting are resolved via styles.xml; anything Word renumbers
    dynamically in ways not captured here falls back to the nearest
    heading.
  - Table cell insert/delete/merge revisions are located and flagged but
    not diffed cell-by-cell -- inspect the flagged row directly.
  - Field codes (cross-reference fields, TOC) are read as their cached
    display text; the field's target is not resolved.
"""
import sys
import re
import json
import zipfile
import argparse
from pathlib import Path
import xml.etree.ElementTree as ET

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"

# Wrappers we recurse straight through: they neither carry revision state
# nor contribute text of their own.
TRANSPARENT = {
    "hyperlink", "smartTag", "smartTagPr", "fldSimple", "sdt", "sdtContent",
    "bookmarkStart", "bookmarkEnd", "customXml", "customXmlPr", "dir", "bdo",
}

HEADING_STYLE_RE = re.compile(r"^(heading|title|berschrift)", re.IGNORECASE)
# Fallback for documents that hard-type their clause numbers into the text.
LITERAL_CLAUSE_RE = re.compile(
    r"^\s*("
    r"\(?\d+(\.\d+)+\)?[.)]?"      # 2.1, 8.2.1, (2.1) -- trailing delimiter optional
    r"|\(?\d+\)?[.)]"              # 3. / 3) / (3) -- a lone number needs a delimiter,
                                   # otherwise "12 months from..." reads as clause 12
    r"|\([a-zA-Z]\)|\([ivxlcdm]+\)"
    r"|(Section|Clause|Article|Schedule|Exhibit|Annex|Appendix)\s+[\w.]+"
    r")(?!%)(?=\s+\S)",            # reject "1.5% per month"; require following text
    re.IGNORECASE,
)
ROMAN = [
    (1000, "m"), (900, "cm"), (500, "d"), (400, "cd"), (100, "c"), (90, "xc"),
    (50, "l"), (40, "xl"), (10, "x"), (9, "ix"), (5, "v"), (4, "iv"), (1, "i"),
]


def tag(el):
    return el.tag.split("}", 1)[-1] if "}" in el.tag else el.tag


def attr(el, name):
    return el.get(W + name) if el is not None else None


# --------------------------------------------------------------------------
# Package access: .docx zip, unzipped folder, or bare document.xml
# --------------------------------------------------------------------------

class Package:
    def __init__(self, path):
        self.path = Path(path)
        self._zip = None
        self.bare_xml = None
        if self.path.is_dir():
            self.mode = "dir"
        elif self.path.suffix.lower() == ".xml":
            self.mode = "bare"
            self.bare_xml = self.path.read_bytes()
        else:
            self.mode = "zip"
            self._zip = zipfile.ZipFile(self.path)

    def read(self, name):
        """Return bytes for a package part, or None if absent."""
        if self.mode == "bare":
            return self.bare_xml if name == "word/document.xml" else None
        if self.mode == "dir":
            p = self.path / name
            return p.read_bytes() if p.exists() else None
        try:
            return self._zip.read(name)
        except KeyError:
            return None

    def names(self):
        if self.mode == "bare":
            return ["word/document.xml"]
        if self.mode == "dir":
            return [
                str(p.relative_to(self.path)).replace("\\", "/")
                for p in self.path.rglob("*.xml")
            ]
        return self._zip.namelist()

    def part_list(self, all_parts=False):
        """Parts to scan, in a sensible reading order."""
        parts = [("body", "word/document.xml")]
        for label, pattern in (("footnotes", r"word/footnotes\.xml$"),
                               ("endnotes", r"word/endnotes\.xml$")):
            for n in sorted(self.names()):
                if re.match(pattern, n):
                    parts.append((label, n))
        if all_parts:
            for n in sorted(self.names()):
                if re.match(r"word/(header|footer)\d*\.xml$", n):
                    parts.append((Path(n).stem, n))
        return [(label, n) for label, n in parts if self.read(n) is not None]


# --------------------------------------------------------------------------
# Numbering: replay Word's counters to recover real clause numbers
# --------------------------------------------------------------------------

def format_counter(value, numfmt):
    if numfmt in (None, "decimal"):
        return str(value)
    if numfmt == "decimalZero":
        return f"{value:02d}"
    if numfmt in ("lowerLetter", "upperLetter"):
        # 1->a, 26->z, 27->aa (Word's alphabetic overflow)
        s, n = "", value
        while n > 0:
            n, rem = divmod(n - 1, 26)
            s = chr(ord("a") + rem) + s
        return s.upper() if numfmt == "upperLetter" else s
    if numfmt in ("lowerRoman", "upperRoman"):
        s, n = "", value
        for v, sym in ROMAN:
            while n >= v:
                s += sym
                n -= v
        return s.upper() if numfmt == "upperRoman" else s
    return str(value)


class Numbering:
    """Resolves a paragraph's displayed clause number (e.g. '3.2(a)')."""

    def __init__(self, pkg):
        self.abstract = {}       # abstractNumId -> {ilvl: {fmt, text, start}}
        self.num_to_abstract = {}  # numId -> abstractNumId
        self.overrides = {}     # (numId, ilvl) -> start override
        self.style_numpr = {}   # styleId -> (numId, ilvl)
        self.style_outline = {}  # styleId -> outline level int
        self.style_names = {}   # styleId -> name
        self.counters = {}      # (abstractNumId, ilvl) -> current value
        self._load_numbering(pkg)
        self._load_styles(pkg)

    def _load_numbering(self, pkg):
        raw = pkg.read("word/numbering.xml")
        if not raw:
            return
        root = ET.fromstring(raw)
        for an in root.findall(W + "abstractNum"):
            aid = attr(an, "abstractNumId")
            levels = {}
            for lvl in an.findall(W + "lvl"):
                ilvl = int(attr(lvl, "ilvl") or 0)
                levels[ilvl] = {
                    "fmt": attr(lvl.find(W + "numFmt"), "val"),
                    "text": attr(lvl.find(W + "lvlText"), "val") or "",
                    "start": int(attr(lvl.find(W + "start"), "val") or 1),
                    "pStyle": attr(lvl.find(W + "pStyle"), "val"),
                }
            self.abstract[aid] = levels
        for num in root.findall(W + "num"):
            nid = attr(num, "numId")
            ref = num.find(W + "abstractNumId")
            if ref is not None:
                self.num_to_abstract[nid] = attr(ref, "val")
            for ov in num.findall(W + "lvlOverride"):
                ilvl = int(attr(ov, "ilvl") or 0)
                sw = ov.find(W + "startOverride")
                if sw is not None:
                    self.overrides[(nid, ilvl)] = int(attr(sw, "val") or 1)

    def _load_styles(self, pkg):
        raw = pkg.read("word/styles.xml")
        if not raw:
            return
        root = ET.fromstring(raw)
        for st in root.findall(W + "style"):
            sid = attr(st, "styleId")
            name = attr(st.find(W + "name"), "val")
            if name:
                self.style_names[sid] = name
            ppr = st.find(W + "pPr")
            if ppr is None:
                continue
            numpr = ppr.find(W + "numPr")
            if numpr is not None:
                nid = attr(numpr.find(W + "numId"), "val")
                ilvl = attr(numpr.find(W + "ilvl"), "val")
                if nid:
                    self.style_numpr[sid] = (nid, int(ilvl or 0))
            outline = ppr.find(W + "outlineLvl")
            if outline is not None:
                self.style_outline[sid] = int(attr(outline, "val") or 0)

    def style_label(self, style_id):
        if not style_id:
            return None
        return self.style_names.get(style_id, style_id)

    def is_heading(self, style_id):
        if not style_id:
            return False
        if HEADING_STYLE_RE.search(style_id):
            return True
        name = self.style_names.get(style_id, "")
        return bool(HEADING_STYLE_RE.search(name)) or style_id in self.style_outline

    def resolve(self, ppr, style_id):
        """Return (numId, ilvl) from direct formatting or the paragraph style."""
        if ppr is not None:
            numpr = ppr.find(W + "numPr")
            if numpr is not None:
                nid = attr(numpr.find(W + "numId"), "val")
                ilvl = attr(numpr.find(W + "ilvl"), "val")
                if nid and nid != "0":
                    if ilvl is None and style_id in self.style_numpr:
                        ilvl = str(self.style_numpr[style_id][1])
                    return nid, int(ilvl or 0)
                if nid == "0":
                    return None  # numbering explicitly removed
        if style_id in self.style_numpr:
            return self.style_numpr[style_id]
        return None

    def advance(self, numid, ilvl):
        """Increment counters for this paragraph and render its number."""
        aid = self.num_to_abstract.get(numid)
        if aid is None or aid not in self.abstract:
            return None
        levels = self.abstract[aid]
        lvl = levels.get(ilvl)
        if lvl is None:
            return None
        fmt = lvl["fmt"]
        if fmt in ("bullet", "none"):
            return None

        key = (aid, ilvl)
        if key not in self.counters:
            start = self.overrides.get((numid, ilvl), lvl["start"])
            self.counters[key] = start
        else:
            self.counters[key] += 1
        # A new item at this level restarts everything below it.
        for (a, l) in list(self.counters):
            if a == aid and l > ilvl:
                del self.counters[(a, l)]

        text = lvl["text"]

        def sub(m):
            target = int(m.group(1)) - 1
            tlvl = levels.get(target)
            if tlvl is None:
                return ""
            val = self.counters.get((aid, target))
            if val is None:
                val = self.overrides.get((numid, target), tlvl["start"])
            return format_counter(val, tlvl["fmt"])

        rendered = re.sub(r"%(\d+)", sub, text).strip()
        return rendered or None


# --------------------------------------------------------------------------
# Segment collection: revision-aware walk of a paragraph
# --------------------------------------------------------------------------

REV_TAGS = {"ins", "del", "moveFrom", "moveTo"}

SEG_LABEL = {
    frozenset(): "unchanged",
    frozenset({"ins"}): "ins",
    frozenset({"del"}): "del",
    frozenset({"ins", "del"}): "ins_del",
    frozenset({"moveFrom"}): "move_out",
    frozenset({"moveTo"}): "move_in",
    frozenset({"moveTo", "del"}): "move_in_del",
    frozenset({"moveFrom", "ins"}): "move_out_ins",
}

RENDER = {
    "ins": "INSERTED",
    "del": "DELETED",
    "ins_del": "INSERTED THEN DELETED",
    "move_out": "MOVED OUT",
    "move_in": "MOVED IN",
    "move_in_del": "MOVED IN THEN DELETED",
    "move_out_ins": "MOVED OUT THEN RESTORED",
}


class Seg:
    __slots__ = ("kind", "text", "revs")

    def __init__(self, kind, text, revs):
        self.kind = kind
        self.text = text
        self.revs = revs  # list of (rev_tag, author, date)

    @property
    def authors(self):
        return [a for _, a, _ in self.revs if a]

    @property
    def dates(self):
        return [d for _, _, d in self.revs if d]


def collect_segments(el, revs=()):
    """Collect Seg objects from a paragraph in document order, tracking
    nested revision context so an <w:ins> wrapping a <w:del> is recognised
    as a counter-edit rather than a plain deletion."""
    out = []
    t = tag(el)

    if t in REV_TAGS:
        nested = tuple(revs) + ((t, attr(el, "author"), attr(el, "date")),)
        for child in el:
            out.extend(collect_segments(child, nested))
        return out

    if t == "r":
        rpr = el.find(W + "rPr")
        rprchange = rpr.find(W + "rPrChange") if rpr is not None else None
        if rprchange is not None and not revs:
            out.append(Seg("formatting_run", None,
                           [("rPrChange", attr(rprchange, "author"), attr(rprchange, "date"))]))
        parts = []
        for child in el:
            ct = tag(child)
            if ct in ("t", "delText", "instrText", "delInstrText"):
                parts.append(child.text or "")
            elif ct == "tab":
                parts.append("\t")
            elif ct in ("br", "cr"):
                parts.append("\n")
            elif ct in ("footnoteReference", "endnoteReference"):
                parts.append(f"[{ct.replace('Reference','')} {attr(child, 'id')}]")
        text = "".join(parts)
        if text:
            kinds = frozenset(r for r, _, _ in revs)
            out.append(Seg(SEG_LABEL.get(kinds, "complex"), text, list(revs)))
        return out

    if t == "tbl":
        return out  # table content is walked separately, cell by cell

    for child in el:
        out.extend(collect_segments(child, revs))
    return out


def merge_adjacent(segs):
    """Coalesce consecutive segments with identical kind and revision authorship."""
    merged = []
    for s in segs:
        if s.kind == "formatting_run":
            merged.append(s)
            continue
        prev = merged[-1] if merged else None
        if (prev is not None and prev.kind == s.kind
                and prev.kind != "formatting_run"
                and prev.revs == s.revs):
            prev.text += s.text
        else:
            merged.append(Seg(s.kind, s.text, list(s.revs)))
    return merged


def render_paragraph(segs, limit=None):
    out = []
    for s in segs:
        if s.kind == "formatting_run" or s.text is None:
            continue
        if s.kind == "unchanged":
            out.append(s.text)
        else:
            out.append(f"\u27e6{RENDER.get(s.kind, s.kind.upper())}: {s.text}\u27e7")
    text = "".join(out)
    if limit and len(text) > limit:
        text = text[: limit - 3].rstrip() + "..."
    return text


def visible_text(segs):
    """Text as it reads with changes accepted (deletions dropped)."""
    return "".join(
        s.text for s in segs
        if s.text and s.kind in ("unchanged", "ins", "move_in")
    )


# Unchanged text that shouldn't break a single logical edit in two: a stray
# space or a short run of punctuation between a deletion and its replacement.
CONNECTIVE_RE = re.compile(r"^(\s*|[^\w\s]{1,3}\s*)$")


def group_edits(segs):
    """Group contiguous revision segments into single edit events, bridging
    trivial unchanged text so a del+space+ins reads as one substitution.

    Returns dicts carrying the group plus the partial words either side of it.
    Comparison tools split runs mid-token (a change to "three (3)" arrives as
    "three (3" with the ")" left in an unchanged run), so the reported text is
    snapped out to the nearest whitespace to stay readable."""
    results, current, pending = [], [], []
    prev_unchanged = ""

    def close():
        if current:
            results.append({"segs": list(current), "prefix": _tail_word(prev_unchanged)})

    for s in segs:
        if s.kind == "formatting_run":
            continue
        if s.kind == "unchanged":
            if current and s.text and CONNECTIVE_RE.match(s.text):
                pending.append(s)
                continue
            if current:
                close()
                results[-1]["suffix"] = _head_word(s.text or "")
                current, pending = [], []
            prev_unchanged = s.text or ""
            continue
        if pending:
            current.extend(pending)
            pending = []
        current.append(s)
    if current:
        close()
        results[-1]["suffix"] = ""
    for r in results:
        r.setdefault("suffix", "")
    return results


def _tail_word(text, cap=30):
    """Trailing characters of `text` since the last whitespace."""
    if not text or text[-1].isspace():
        return ""
    return text[-cap:].split()[-1] if text.split() else ""


def _head_word(text, cap=30):
    """Leading characters of `text` up to the first whitespace."""
    if not text or text[0].isspace():
        return ""
    head = text[:cap]
    return head.split()[0] if head.split() else ""


def classify_group(group):
    kinds = {s.kind for s in group if s.kind != "unchanged"}
    if "ins_del" in kinds or "move_in_del" in kinds or "move_out_ins" in kinds:
        return "counter-edit"
    if kinds == {"del"}:
        return "deletion"
    if kinds == {"ins"}:
        return "insertion"
    # Comparison tools (LibreOffice's Compare Documents, Word's Combine) often
    # tag a word as "moved" when it merely also occurs elsewhere, so a
    # deletion sitting against a moved-in run is a plain substitution in
    # substance. Reading these as moves would scatter one edit across two rows.
    if kinds in ({"del", "ins"}, {"del", "move_in"}, {"move_out", "ins"},
                 {"del", "ins", "move_in"}, {"del", "ins", "move_out"}):
        return "substitution"
    if kinds == {"move_out"}:
        return "move-out"
    if kinds == {"move_in"}:
        return "move-in"
    if kinds == {"move_out", "move_in"}:
        return "move"
    return "mixed"


def group_text(group, kinds):
    return "".join(s.text for s in group if s.kind in kinds and s.text) or None


def one_or_list(values):
    uniq = sorted(set(values))
    if not uniq:
        return None
    return uniq[0] if len(uniq) == 1 else uniq


# --------------------------------------------------------------------------
# Document walk
# --------------------------------------------------------------------------

class State:
    def __init__(self, numbering, context_chars):
        self.numbering = numbering
        self.context_chars = context_chars
        self.seq = 0
        self.para_index = 0
        self.heading_stack = []   # [(outline_level, text)]
        self.last_clause = None
        self.content = []
        self.formatting = []
        self.text_lines = []
        # Set while walking inside a wholly inserted or deleted table row: the
        # row is already reported as one change, so the per-cell insertions and
        # paragraph marks underneath it are noise. A rebuilt 4-row table
        # otherwise produces 35 rows for what a reader sees as two edits.
        self.suppress = 0
        self.table_states = []
        self.comment_hits = {}    # comment id -> anchor info
        self.open_comments = {}   # comment id -> list of text fragments
        self.part = "body"

    def next_seq(self):
        if self.suppress:
            return None
        self.seq += 1
        return self.seq

    def add_content(self, rec):
        if self.suppress:
            return
        self.content.append(rec)

    def add_formatting(self, rec):
        if self.suppress:
            return
        self.formatting.append(rec)

    def section_path(self):
        return " > ".join(t for _, t in self.heading_stack) or None

    def locate(self, extra=None):
        """Human-readable locator: heading path, then the clause number if it
        adds information the heading path doesn't already carry."""
        bits = []
        if self.part != "body":
            bits.append(self.part)
        path = self.section_path()
        if path:
            bits.append(path)
        clause = self.last_clause
        if clause and (not path or clause.rstrip(".)") not in path):
            bits.append(f"clause {clause}" if path else clause)
        if extra:
            bits.append(extra)
        if not bits:
            return f"paragraph {self.para_index}"
        return " — ".join(bits) if len(bits) > 1 else bits[0]

    def base_record(self, extra_location=None):
        return {
            "part": self.part,
            "paragraph_index": self.para_index,
            "clause": self.last_clause,
            "section_path": self.section_path(),
            "location": self.locate(extra_location),
        }


def para_style(p):
    ppr = p.find(W + "pPr")
    if ppr is None:
        return None
    return attr(ppr.find(W + "pStyle"), "val")


def update_location(state, p, ppr, style_id, segs):
    """Advance numbering counters and heading/clause context for this paragraph."""
    num = state.numbering.resolve(ppr, style_id) if state.numbering else None
    number = state.numbering.advance(*num) if num else None
    text = visible_text(segs).strip()

    if number:
        state.last_clause = number
    elif text and LITERAL_CLAUSE_RE.match(text):
        state.last_clause = LITERAL_CLAUSE_RE.match(text).group(0).strip()

    if state.numbering and state.numbering.is_heading(style_id) and text:
        label = f"{number} {text}".strip() if number else text
        label = label[:120]
        level = state.numbering.style_outline.get(style_id)
        if level is None:
            m = re.search(r"(\d+)", style_id or "")
            level = int(m.group(1)) - 1 if m else 0
        state.heading_stack = [(l, t) for l, t in state.heading_stack if l < level]
        state.heading_stack.append((level, label))


def process_paragraph(p, state, extra_location=None):
    state.para_index += 1
    ppr = p.find(W + "pPr")
    style_id = para_style(p)
    segs = merge_adjacent(collect_segments(p))
    context = render_paragraph(segs, state.context_chars)

    # Resolve this paragraph's own clause number and heading position *before*
    # recording its changes. Doing it afterwards labels every change with the
    # preceding paragraph's location, which sends the reader to the wrong clause.
    update_location(state, p, ppr, style_id, segs)

    # Removing deleted runs can leave doubled spaces behind; collapse them so
    # the text reads normally and phrase searches still match.
    accepted = re.sub(r"[ \t]{2,}", " ", visible_text(segs)).strip()
    if accepted:
        prefix = state.last_clause or (
            state.heading_stack[-1][1] if state.heading_stack else f"p{state.para_index}")
        note = "" if state.part == "body" else f"{state.part}: "
        state.text_lines.append(f"[{note}{prefix}] {accepted}")

    # Paragraph-mark revisions and paragraph-level formatting revisions.
    if ppr is not None:
        rpr = ppr.find(W + "rPr")
        if rpr is not None:
            for rev_tag, ctype, note in (
                ("del", "paragraph-mark-deleted",
                 "The paragraph mark was deleted, so this paragraph merges into the one that follows. "
                 "Check whether that silently combines two separate obligations, or removes a "
                 "list item's identity for cross-referencing purposes."),
                ("ins", "paragraph-mark-inserted",
                 "A paragraph mark was inserted, splitting this text into two paragraphs. "
                 "In a numbered clause this creates a new sub-clause and shifts the numbering "
                 "of everything after it, which can break cross-references elsewhere."),
            ):
                rev = rpr.find(W + rev_tag)
                if rev is not None:
                    rec = state.base_record(extra_location)
                    rec.update({
                        "sequence": state.next_seq(),
                        "type": ctype,
                        "old_text": None,
                        "new_text": None,
                        "note": note,
                        "author": attr(rev, "author"),
                        "date": attr(rev, "date"),
                        "paragraph_context": context,
                    })
                    state.add_content(rec)

        pprchange = ppr.find(W + "pPrChange")
        if pprchange is not None:
            old_ppr = pprchange.find(W + "pPr")
            old_num = old_ppr.find(W + "numPr") if old_ppr is not None else None
            new_num = ppr.find(W + "numPr")
            old_ilvl = attr(old_num.find(W + "ilvl"), "val") if old_num is not None else None
            new_ilvl = attr(new_num.find(W + "ilvl"), "val") if new_num is not None else None
            numbering_shift = (old_num is None) != (new_num is None) or old_ilvl != new_ilvl
            rec = state.base_record(extra_location)
            rec.update({
                "type": "paragraph-formatting",
                "author": attr(pprchange, "author"),
                "date": attr(pprchange, "date"),
                "numbering_changed": numbering_shift,
                "note": (
                    "Numbering or list level changed with this formatting revision. "
                    "Review before dismissing: promoting or demoting a clause changes what "
                    "it is subordinate to, and renumbering can break cross-references."
                    if numbering_shift else
                    "Paragraph formatting only (alignment, spacing, indent, style)."
                ),
                "paragraph_preview": visible_text(segs)[:120] or None,
            })
            state.add_formatting(rec)

    for s in segs:
        if s.kind == "formatting_run":
            rec = state.base_record(extra_location)
            rec.update({
                "type": "run-formatting",
                "author": s.authors[0] if s.authors else None,
                "date": s.dates[0] if s.dates else None,
                "numbering_changed": False,
                "note": "Character formatting only (font, bold, italic, colour) with no wording change.",
                "paragraph_preview": visible_text(segs)[:120] or None,
            })
            state.add_formatting(rec)

    for g in group_edits(segs):
        group, prefix, suffix = g["segs"], g["prefix"], g["suffix"]
        gtype = classify_group(group)

        def snap(text):
            if text is None:
                return None
            return f"{prefix}{text}{suffix}"

        rec = state.base_record(extra_location)
        old_text = snap(group_text(group, {"del", "move_out"}))
        new_text = snap(group_text(group, {"ins", "move_in", "move_out_ins"}))
        # A genuine move relocates identical text. When the two sides differ,
        # the comparison tool has tagged replaced wording as moved because it
        # happens to occur elsewhere -- in substance it's a substitution.
        if gtype == "move" and (old_text or "").strip() != (new_text or "").strip():
            gtype = "substitution"
        rec.update({
            "sequence": state.next_seq(),
            "type": gtype,
            "old_text": old_text,
            "new_text": new_text,
            # Text that was inserted in an earlier round and then deleted in a
            # later one: never in the original, won't survive either.
            "inserted_then_deleted": group_text(group, {"ins_del", "move_in_del"}),
            "author": one_or_list([a for s in group for a in s.authors]),
            "date": one_or_list([d for s in group for d in s.dates]),
            "paragraph_context": context,
        })
        if gtype == "counter-edit":
            rec["note"] = (
                "Nested revision: text one author inserted has been deleted by another "
                "(or vice versa). This is negotiating history across markup rounds -- "
                "check who did what and whether the net position is the original wording."
            )
        state.add_content(rec)


def cell_text(tc, include_deleted=False):
    """Plain text of a cell. include_deleted keeps struck-through content, which
    is the only way to recover what a wholly deleted row used to say."""
    segs = merge_adjacent(collect_segments(tc))
    kinds = {"unchanged", "ins", "move_in"}
    if include_deleted:
        kinds |= {"del", "move_out", "ins_del", "move_in_del"}
    return "".join(s.text for s in segs if s.text and s.kind in kinds).strip()


def process_table(tbl, state, extra_location=None):
    # A table edited structurally is often recorded as every old row deleted
    # and every new row inserted, even when one figure changed. Detect that so
    # the rows can be reported as one rebuild to compare, not N separate edits.
    rows = tbl.findall(W + "tr")
    ins_rows = sum(1 for tr in rows
                   if (tr.find(W + "trPr") is not None
                       and tr.find(W + "trPr").find(W + "ins") is not None))
    del_rows = sum(1 for tr in rows
                   if (tr.find(W + "trPr") is not None
                       and tr.find(W + "trPr").find(W + "del") is not None))
    # A replaced table shows up two ways: one table with both inserted and
    # deleted rows, or -- as LibreOffice's compare does it -- a wholly inserted
    # table sitting next to a wholly deleted one. Either way the reviewer needs
    # to diff the two row sets rather than read each row as its own change.
    if rows and ins_rows == len(rows):
        table_status = "wholly-inserted"
    elif rows and del_rows == len(rows):
        table_status = "wholly-deleted"
    elif ins_rows and del_rows:
        table_status = "partly-replaced"
    else:
        table_status = None
    if table_status:
        state.table_states.append(table_status)

    tblpr = tbl.find(W + "tblPr")
    if tblpr is not None and tblpr.find(W + "tblPrChange") is not None:
        change = tblpr.find(W + "tblPrChange")
        rec = state.base_record(extra_location)
        rec.update({
            "type": "table-formatting",
            "author": attr(change, "author"),
            "date": attr(change, "date"),
            "numbering_changed": False,
            "note": "Table formatting only (borders, width, shading, layout).",
            "paragraph_preview": None,
        })
        state.add_formatting(rec)

    for row_i, tr in enumerate(rows, start=1):
        trpr = tr.find(W + "trPr")
        row_loc = f"table row {row_i}"
        row_wholly_revised = False
        if trpr is not None:
            for rev_tag, ctype, note in (
                ("ins", "table-row-inserted", "An entire table row was inserted."),
                ("del", "table-row-deleted", "An entire table row was deleted."),
            ):
                rev = trpr.find(W + rev_tag)
                if rev is not None:
                    row_wholly_revised = True
                    # A deleted row's content only survives in delText, so the
                    # struck-through text has to be included to report what the
                    # row used to say.
                    text = " | ".join(
                        cell_text(tc, include_deleted=(rev_tag == "del"))
                        for tc in tr.findall(W + "tc"))
                    rec = state.base_record(row_loc)
                    rec.update({
                        "sequence": state.next_seq(),
                        "type": ctype,
                        "old_text": text if rev_tag == "del" else None,
                        "new_text": text if rev_tag == "ins" else None,
                        "note": note,
                        "table_status": table_status,
                        "author": attr(rev, "author"),
                        "date": attr(rev, "date"),
                        "paragraph_context": text[: state.context_chars] if state.context_chars else text,
                    })
                    state.add_content(rec)
            if trpr.find(W + "trPrChange") is not None:
                change = trpr.find(W + "trPrChange")
                rec = state.base_record(row_loc)
                rec.update({
                    "type": "table-row-formatting",
                    "author": attr(change, "author"),
                    "date": attr(change, "date"),
                    "numbering_changed": False,
                    "note": "Row height or row formatting only.",
                    "paragraph_preview": cell_text(tr)[:120] or None,
                })
                state.add_formatting(rec)

        if row_wholly_revised:
            state.suppress += 1
        row_text = " | ".join(cell_text(tc, include_deleted=True)
                              for tc in tr.findall(W + "tc"))

        for col_i, tc in enumerate(tr.findall(W + "tc"), start=1):
            cell_loc = f"table row {row_i}, cell {col_i}"
            tcpr = tc.find(W + "tcPr")
            if tcpr is not None:
                for stag, label in (("cellIns", "inserted"), ("cellDel", "deleted"),
                                    ("cellMerge", "merged or split")):
                    node = tcpr.find(W + stag)
                    if node is not None:
                        rec = state.base_record(cell_loc)
                        rec.update({
                            "sequence": state.next_seq(),
                            "type": "table-cell-structure",
                            "old_text": None,
                            "new_text": None,
                            "note": f"A table cell or column was {label}. The affected text is not "
                                    f"auto-diffed -- inspect this cell and its row directly.",
                            "author": attr(node, "author"),
                            "date": attr(node, "date"),
                            "paragraph_context": row_text[: state.context_chars] if state.context_chars else row_text,
                        })
                        state.add_content(rec)
                if tcpr.find(W + "tcPrChange") is not None:
                    change = tcpr.find(W + "tcPrChange")
                    rec = state.base_record(cell_loc)
                    rec.update({
                        "type": "table-cell-formatting",
                        "author": attr(change, "author"),
                        "date": attr(change, "date"),
                        "numbering_changed": False,
                        "note": "Cell width, shading, or borders only.",
                        "paragraph_preview": None,
                    })
                    state.add_formatting(rec)
            walk_container(tc, state, extra_location=cell_loc)

        if row_wholly_revised:
            state.suppress -= 1


def walk_container(container, state, extra_location=None):
    for child in list(container):
        t = tag(child)
        if t == "p":
            process_paragraph(child, state, extra_location)
        elif t == "tbl":
            process_table(child, state, extra_location)
        elif t == "sectPr":
            change = child.find(W + "sectPrChange")
            if change is not None:
                rec = state.base_record(extra_location)
                rec.update({
                    "type": "section-formatting",
                    "author": attr(change, "author"),
                    "date": attr(change, "date"),
                    "numbering_changed": False,
                    "note": "Section properties only (margins, page size, columns).",
                    "paragraph_preview": None,
                })
                state.add_formatting(rec)
        elif t in ("footnote", "endnote"):
            # footnotes.xml / endnotes.xml wrap their paragraphs one level deeper.
            note_id = attr(child, "id")
            walk_container(child, state,
                           extra_location=f"note {note_id}" if note_id else None)
        elif t in ("commentRangeStart", "commentRangeEnd", "commentReference"):
            pass  # handled by the comment pass


# --------------------------------------------------------------------------
# Comments
# --------------------------------------------------------------------------

def collect_comment_anchors(root, state_part, anchors):
    """Record, per comment id, the visible text between its range markers."""
    open_ids = set()
    for order, el in enumerate(root.iter()):
        t = tag(el)
        if t == "commentRangeStart":
            cid = attr(el, "id")
            open_ids.add(cid)
            anchors.setdefault(cid, {"part": state_part, "text": "", "order": order})
        elif t == "commentRangeEnd":
            open_ids.discard(attr(el, "id"))
        elif t == "commentReference":
            cid = attr(el, "id")
            anchors.setdefault(cid, {"part": state_part, "text": "", "order": order})
        elif t in ("t", "delText") and open_ids:
            for cid in open_ids:
                anchors[cid]["text"] += el.text or ""


def load_comments(pkg, anchors, context_chars):
    raw = pkg.read("word/comments.xml")
    if not raw:
        return [], []
    root = ET.fromstring(raw)

    parents = {}
    ext = pkg.read("word/commentsExtended.xml")
    para_to_comment = {}
    if ext:
        # commentsExtended links replies by paragraph id rather than comment id,
        # so map each comment's last paragraph id first.
        for c in root.findall(W + "comment"):
            paras = c.findall(W + "p")
            if paras:
                pid = paras[-1].get(
                    "{http://schemas.microsoft.com/office/word/2010/wordml}paraId"
                )
                if pid:
                    para_to_comment[pid] = attr(c, "id")
        eroot = ET.fromstring(ext)
        for ce in eroot.iter():
            if tag(ce) != "commentEx":
                continue
            own = ce.get("{http://schemas.microsoft.com/office/word/2010/wordml}paraId")
            parent = ce.get("{http://schemas.microsoft.com/office/word/2010/wordml}paraIdParent")
            if own and parent:
                child_id = para_to_comment.get(own)
                parent_id = para_to_comment.get(parent)
                if child_id and parent_id:
                    parents[child_id] = parent_id

    records = []
    for c in root.findall(W + "comment"):
        cid = attr(c, "id")
        text = "\n".join(
            "".join(t.text or "" for t in p.iter() if tag(t) in ("t", "delText"))
            for p in c.findall(W + "p")
        ).strip()
        records.append({
            "comment_id": cid,
            "author": attr(c, "author"),
            "initials": attr(c, "initials"),
            "date": attr(c, "date"),
            "text": text,
            "reply_to": parents.get(cid),
        })

    # A reply carries no range markers of its own -- it hangs off its parent's
    # anchor, so inherit it rather than reporting the reply as unanchored.
    by_id = {r["comment_id"]: r for r in records}
    for r in records:
        anchor = anchors.get(r["comment_id"])
        if anchor is None:
            parent = r.get("reply_to")
            seen = set()
            while parent and parent not in seen:
                seen.add(parent)
                anchor = anchors.get(parent)
                if anchor:
                    break
                parent = by_id.get(parent, {}).get("reply_to")
        anchor_text = (anchor or {}).get("text", "").strip()
        if context_chars and len(anchor_text) > context_chars:
            anchor_text = anchor_text[: context_chars - 3].rstrip() + "..."
        r["anchored_to"] = anchor_text or None
        r["part"] = (anchor or {}).get("part")
        r["_order"] = (anchor or {}).get("order", 10**9)

    resolved = sorted((r for r in records if r["part"] is not None),
                      key=lambda r: (r["_order"], r["comment_id"]))
    unanchored = [r for r in records if r["part"] is None]
    for r in records:
        r.pop("_order", None)
    return resolved, unanchored


# --------------------------------------------------------------------------
# Markdown starter table
# --------------------------------------------------------------------------

def escape_cell(text):
    if text is None:
        return ""
    return text.replace("|", "\\|").replace("\n", " ").strip()


def raw_change_text(rec):
    if rec["type"] == "substitution":
        return f'"{escape_cell(rec["old_text"])}" → "{escape_cell(rec["new_text"])}"'
    if rec["type"] == "insertion":
        return f'inserted: "{escape_cell(rec["new_text"])}"'
    if rec["type"] == "deletion":
        return f'deleted: "{escape_cell(rec["old_text"])}"'
    if rec["type"] == "counter-edit":
        bits = []
        if rec.get("inserted_then_deleted"):
            bits.append(f'inserted then struck out: "{escape_cell(rec["inserted_then_deleted"])}"')
        if rec.get("new_text"):
            bits.append(f'net insertion: "{escape_cell(rec["new_text"])}"')
        if rec.get("old_text"):
            bits.append(f'original text deleted: "{escape_cell(rec["old_text"])}"')
        return "counter-edit — " + "; ".join(bits)
    parts = [rec["type"]]
    if rec.get("new_text"):
        parts.append(f'"{escape_cell(rec["new_text"])}"')
    elif rec.get("old_text"):
        parts.append(f'"{escape_cell(rec["old_text"])}"')
    elif rec.get("note"):
        parts.append(escape_cell(rec["note"]).split(".")[0])
    return " — ".join(parts)


def write_markdown(result, out):
    s = result["summary"]
    print(f"<!-- {s['content_change_count']} substantive changes, "
          f"{s['formatting_change_count']} formatting-only (excluded), "
          f"{s['comment_count']} comments. Raw extraction — the change column is "
          f"unedited machine text; rewrite it concisely, then fill comments and "
          f"impact per the skill workflow. -->", file=out)
    print(file=out)
    print("| # | location | change | comments | impact |", file=out)
    print("|---|---|---|---|---|", file=out)
    for rec in result["content_changes"]:
        print(f'| {rec["sequence"]} | {escape_cell(rec["location"])} | '
              f'{raw_change_text(rec)} |  |  |', file=out)
    if result["comments"]:
        print(file=out)
        print("### Word comments in the markup", file=out)
        print(file=out)
        print("| author | anchored to | comment |", file=out)
        print("|---|---|---|", file=out)
        for c in result["comments"]:
            print(f'| {escape_cell(c["author"])} | {escape_cell(c["anchored_to"])} | '
                  f'{escape_cell(c["text"])} |', file=out)


# --------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("path", help=".docx, unzipped folder, or a document.xml")
    ap.add_argument("--all-parts", action="store_true",
                    help="also scan headers and footers")
    ap.add_argument("--markdown", action="store_true",
                    help="print a starter issues table instead of JSON")
    ap.add_argument("--text", action="store_true",
                    help="print the document as plain text with changes accepted, "
                         "one paragraph per line prefixed by its clause number -- "
                         "greppable for defined terms and cross-references. Use this "
                         "if pandoc can't parse the file.")
    ap.add_argument("--context-chars", type=int, default=700,
                    help="truncate paragraph context (0 = no limit; lower it for "
                         "very large redlines to control output size)")
    ap.add_argument("--brief", action="store_true",
                    help="omit paragraph context and formatting detail -- a compact "
                         "index of a large redline")
    ap.add_argument("--seq",
                    help="only output these change sequence numbers, e.g. "
                         "'12,15-20'. Use with the full context to work through a "
                         "long redline in batches without reloading all of it.")
    args = ap.parse_args()

    wanted = None
    if args.seq:
        wanted = set()
        for chunk in args.seq.split(","):
            chunk = chunk.strip()
            if not chunk:
                continue
            if "-" in chunk:
                lo, hi = chunk.split("-", 1)
                wanted.update(range(int(lo), int(hi) + 1))
            else:
                wanted.add(int(chunk))

    pkg = Package(args.path)
    numbering = Numbering(pkg)
    limit = args.context_chars or None

    state = State(numbering, limit)
    anchors = {}
    parts = pkg.part_list(args.all_parts)

    for label, name in parts:
        raw = pkg.read(name)
        if raw is None:
            continue
        root = ET.fromstring(raw)
        state.part = label
        state.last_clause = None
        if label != "body":
            state.heading_stack = []
        body = root.find(W + "body")
        walk_container(body if body is not None else root, state)
        collect_comment_anchors(root, label, anchors)

    comments, unanchored = load_comments(pkg, anchors, limit)

    authors = sorted({
        a for rec in state.content + state.formatting
        for a in ([rec["author"]] if isinstance(rec.get("author"), str)
                  else (rec.get("author") or []))
        if a
    })
    type_counts = {}
    for rec in state.content:
        type_counts[rec["type"]] = type_counts.get(rec["type"], 0) + 1

    result = {
        "summary": {
            "source": str(Path(args.path).name),
            "parts_scanned": [n for _, n in parts],
            "content_change_count": len(state.content),
            "formatting_change_count": len(state.formatting),
            "comment_count": len(comments) + len(unanchored),
            "change_types": type_counts,
            "authors": authors,
            "formatting_changes_needing_review": sum(
                1 for r in state.formatting if r.get("numbering_changed")),
            "clause_numbers_resolved": bool(numbering.abstract),
            "replaced_tables": (
                min(state.table_states.count("wholly-inserted"),
                    state.table_states.count("wholly-deleted"))
                + state.table_states.count("partly-replaced")),
        },
        "content_changes": state.content,
        "formatting_changes": state.formatting,
        "comments": comments,
        "unanchored_comments": unanchored,
    }

    # Filters are applied after the summary is computed, so the counts always
    # describe the whole document even when only a slice is printed -- that way
    # a batch never looks like the full picture.
    if wanted is not None:
        result["content_changes"] = [
            r for r in result["content_changes"] if r["sequence"] in wanted]
        result["summary"]["filtered_to_sequences"] = sorted(wanted)
    if args.brief:
        for r in result["content_changes"]:
            r.pop("paragraph_context", None)
            r.pop("section_path", None)
        result["formatting_changes"] = [
            {k: v for k, v in r.items() if k in ("type", "location", "numbering_changed")}
            for r in result["formatting_changes"]
        ]

    if args.text:
        for line in state.text_lines:
            print(line)
    elif args.markdown:
        write_markdown(result, sys.stdout)
    else:
        json.dump(result, sys.stdout, indent=2, ensure_ascii=False)
        print()


if __name__ == "__main__":
    main()
