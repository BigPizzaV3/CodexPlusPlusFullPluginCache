#!/usr/bin/env python3
"""A typographic grid for the panel, a layout that records what it draws, and a lint.

After Müller-Brockmann: the line height is the module. Margins, gutters and
fields are whole lines, every baseline sits on a line (descenders hang below),
and blocks snap to fields.

    from layout import Grid, Layout
    grid = Grid(columns=6)                  # 800x480, near (24 px text on 30 px lines)
    page = Layout(grid)
    red = page.meaning("alarm", "red")      # one colour, one meaning
    page.figure(grid.field(0, 0, cols=3), "7:30", cap_lines=3, ink=red)    # hangs from the top
    page.text(grid.lines_box(0, 3, 3, 1), "Réveil de demain", role="label")  # its caption
    page.save("screen.png")                 # also writes screen.json, the layout description

    python3 layout.py lint screen.json      # rules, sizes, contrast, grid, overflow
    python3 layout.py overlay screen.png -o screen.grid.png   # preview only

Grids (landscape 800x480; portrait swaps the axes):
    columns=6: 40 px sides, 6 columns of 95 px   halves, thirds: several elements
    columns=5: 30 px sides, 5 columns of 124 px  a 2 + 3 split: few, larger elements
Both: 30 px lines, 30 px top and bottom, 3 rows of 4 lines, 1-line gutters.
Portrait 480x800: 30 px sides, 3 columns of 120 (or 2 of 195); 40 px top and
bottom, 5 rows of 4 lines.

`far` (read at 2-3 m) keeps the geometry and doubles the type: 48 px text on
two lines instead of 24 px on one.
"""
import argparse
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from inks import INK, _pixels, contrast, pick_font  # noqa: E402

LINE = 30
ROW_LINES = 4
# Type roles per reading distance: (size in px, lines each line of text takes).
ROLES = {
    "near": {"label": (20, 1), "text": (24, 1), "heading": (48, 2)},
    "far": {"label": (24, 1), "text": (48, 2), "heading": (72, 3)},
}
# Text colour pairings, from references/typography.md.
ANY_SIZE = {("black", "white"), ("black", "yellow"), ("white", "red"), ("white", "black")}
HEADLINE_ONLY = {("red", "white"), ("black", "green"), ("black", "blue"), ("blue", "white")}
HEADLINE_PX = 40
MIN_TEXT_PX = 16
_BY_VALUE = {rgb: name for name, rgb in INK.items()}


class Grid:
    """Fields, lines and baselines for one panel, in whole pixels."""

    def __init__(self, width=800, height=480, columns=None, preset="near"):
        self.width, self.height, self.preset, self.line = width, height, preset, LINE
        landscape = width >= height
        if landscape:
            columns = columns or 6
            sides = {6: 40, 5: 30}
            if columns not in sides:
                raise ValueError("landscape grids have 6 or 5 columns")
            self.side, self.top = sides[columns], 30
        else:
            columns = columns or 3
            if columns not in (3, 2):
                raise ValueError("portrait grids have 3 or 2 columns")
            self.side, self.top = 30, 40
        self.columns = columns
        inner = width - 2 * self.side - (columns - 1) * LINE
        self.column_width = inner // columns
        self.lines = (height - 2 * self.top) // LINE
        self.rows = (self.lines + 1) // (ROW_LINES + 1)
        if inner % columns or (height - 2 * self.top) % LINE or \
                self.rows * (ROW_LINES + 1) - 1 != self.lines:
            raise ValueError(f"{width}x{height} does not divide into this grid")

    def x(self, column):
        return self.side + column * (self.column_width + LINE)

    def line_y(self, line):
        """Top of content line `line` (0 = first line under the top margin)."""
        return self.top + line * LINE

    def row_line(self, row):
        """First content line of field row `row`."""
        return row * (ROW_LINES + 1)

    def field(self, col, row, cols=1, rows=1):
        """(x0, y0, x1, y1), end exclusive, of a block of fields with its gutters."""
        x0 = self.x(col)
        x1 = self.x(col + cols - 1) + self.column_width
        y0 = self.line_y(self.row_line(row))
        y1 = self.line_y(self.row_line(row + rows - 1) + ROW_LINES)
        return (x0, y0, x1, y1)

    def lines_box(self, col, cols, first_line, count):
        """A box spanning columns and whole content lines (for text or a chart)."""
        return (self.x(col), self.line_y(first_line),
                self.x(col + cols - 1) + self.column_width, self.line_y(first_line + count))

    def role(self, name):
        return ROLES[self.preset][name]

    def describe(self):
        return {"width": self.width, "height": self.height, "columns": self.columns,
                "preset": self.preset, "line": LINE, "side": self.side, "top": self.top,
                "column_width": self.column_width, "rows": self.rows, "row_lines": ROW_LINES}


def _wrap(draw, text, face, width):
    lines, current = [], ""
    for word in text.split():
        trial = f"{current} {word}".strip()
        if current and draw.textlength(trial, font=face) > width:
            lines.append(current)
            current = word
        else:
            current = trial
    if current:
        lines.append(current)
    return lines


class Layout:
    """Draws on a Grid and records every element: the layout description lint reads."""

    def __init__(self, grid, background="white"):
        from PIL import Image, ImageDraw
        self.grid = grid
        self.image = Image.new("RGB", (grid.width, grid.height), INK[background])
        self.draw = ImageDraw.Draw(self.image)
        self.draw.fontmode = "1"
        self.background = background
        self.meanings = {}
        self.elements = []

    def meaning(self, name, ink):
        """Declare what a colour means; returns its name, to pass as `ink`."""
        self.meanings[name] = ink
        return ink

    def _bg(self, box):
        """The ink under a box: the last recorded block containing it, else the page."""
        for element in reversed(self.elements):
            if element["kind"] == "block":
                x0, y0, x1, y1 = element["box"]
                if x0 <= box[0] and y0 <= box[1] and box[2] <= x1 and box[3] <= y1:
                    return element["ink"]
        return self.background

    def block(self, box, ink, note=""):
        """A solid ink area (it should carry a meaning)."""
        self.draw.rectangle((box[0], box[1], box[2] - 1, box[3] - 1), fill=INK[ink])
        self.elements.append({"kind": "block", "box": list(box), "ink": ink, "note": note})

    def graphic(self, box, draw_fn, inks, note=""):
        """Free drawing inside a box (a chart): draw_fn(draw, box). List the inks used."""
        draw_fn(self.draw, box)
        self.elements.append({"kind": "graphic", "box": list(box), "inks": list(inks), "note": note})

    def text(self, box, text, role="text", ink="black", bold=False, sizes=None, first_line=0):
        """Flush-left text on the grid's lines, fitted into box.

        Tries the role's size, then each smaller size in `sizes`; records the
        result, including any overflow, for lint. Returns the element.
        """
        size, span = self.grid.role(role)
        candidates = [(size, span)] + [(s, max(1, math.ceil(s * 1.2 / LINE))) for s in (sizes or [])]
        width, height_lines = box[2] - box[0], (box[3] - box[1]) // LINE - first_line
        chosen = None
        for size, span in candidates:
            face, font_name = pick_font("text", size, bold=bold)
            lines = _wrap(self.draw, text, face, width)
            chosen = (size, span, face, font_name, lines)
            if len(lines) * span <= height_lines:
                break
        size, span, face, font_name, lines = chosen
        room = height_lines // span
        top = box[1] + first_line * LINE
        # Baselines sit on the lines (descenders hang below), as in Müller-Brockmann:
        # text centred between lines looks like it floats.
        baselines = [top + (i + 1) * span * LINE for i in range(min(room, len(lines)))]
        for baseline, line in zip(baselines, lines):
            self.draw.text((box[0], baseline), line, font=face, fill=INK[ink], anchor="ls")
        # The pixels the text inks (ascenders to descenders), for the collision check.
        inked = [self.draw.textbbox((box[0], b), l, font=face, anchor="ls") for b, l in zip(baselines, lines) if l]
        used = [min(b[0] for b in inked), min(b[1] for b in inked), max(b[2] for b in inked),
                max(b[3] for b in inked)] if inked else [box[0], top, box[0], top]
        element = {"kind": "text", "box": list(box), "used": used, "text": text, "size": size, "font": font_name,
                   "ink": ink, "bg": self._bg(box), "lines": len(lines), "overflow": max(0, len(lines) - room),
                   "role": role, "baselines": baselines}
        self.elements.append(element)
        return element

    def figure(self, box, text, cap_lines=3, ink="black", role="headline", first_line=0):
        """One big figure whose capital height spans `cap_lines` whole lines."""
        probe, _ = pick_font(role, 100)
        cap = probe.getbbox("H")[3] - probe.getbbox("H")[1]
        size = round(100 * cap_lines * LINE / cap)
        face, font_name = pick_font(role, size)
        baseline = box[1] + (first_line + cap_lines) * LINE
        self.draw.text((box[0], baseline), text, font=face, fill=INK[ink], anchor="ls")
        ink_box = self.draw.textbbox((box[0], baseline), text, font=face, anchor="ls")
        element = {"kind": "text", "box": list(box), "used": list(ink_box), "text": text, "size": size,
                   "font": font_name, "ink": ink, "bg": self._bg(box), "lines": 1,
                   "overflow": int(ink_box[2] > box[2]), "role": "figure", "baselines": [baseline]}
        self.elements.append(element)
        return element

    def save(self, path):
        self.image.save(path)
        spec = {"grid": self.grid.describe(), "background": self.background,
                "meanings": self.meanings, "elements": self.elements}
        with open(os.path.splitext(path)[0] + ".json", "w", encoding="utf-8") as handle:
            json.dump(spec, handle, ensure_ascii=False, indent=1)
        return path


def lint(spec, image=None):
    """Every rule the layout description (and the PNG, if given) breaks: [(level, message)]."""
    issues = []
    grid = spec["grid"]
    meanings = spec.get("meanings", {})
    inks_meaning = {}
    for name, ink in meanings.items():
        inks_meaning.setdefault(ink, []).append(name)
    for ink, names in inks_meaning.items():
        if len(names) > 1:
            issues.append(("error", f"{ink} carries {len(names)} meanings ({', '.join(names)}): one colour, one meaning"))
    if len(meanings) > 3:
        issues.append(("warning", f"{len(meanings)} colour meanings: 2-3 read best"))
    meaning_inks = set(meanings.values()) | {"black", "white"}
    sizes = set()
    for element in spec["elements"]:
        label = element.get("text") or element.get("note") or element["kind"]
        x0, y0, x1, y1 = element["box"]
        if x0 < min(grid["side"], 30) or y0 < min(grid["top"], 30) or \
                x1 > grid["width"] - min(grid["side"], 30) or y1 > grid["height"] - min(grid["top"], 30):
            issues.append(("error", f"'{label}' reaches into the margin"))
        if (y0 - grid["top"]) % grid["line"] or (y1 - grid["top"]) % grid["line"]:
            issues.append(("warning", f"'{label}' is off the {grid['line']} px lines"))
        for ink in ([element["ink"]] if "ink" in element else element.get("inks", [])):
            if ink not in meaning_inks:
                issues.append(("warning", f"'{label}' uses {ink}, which has no declared meaning"))
        if element["kind"] != "text":
            continue
        size, fg, bg = element["size"], element["ink"], element["bg"]
        sizes.add(size)
        if size < MIN_TEXT_PX:
            issues.append(("warning", f"'{label}' at {size} px: under the recommended {MIN_TEXT_PX} px"))
        pair = (fg, bg)
        if pair not in ANY_SIZE:
            if pair in HEADLINE_ONLY and size < HEADLINE_PX:
                issues.append(("error", f"'{label}': {fg} on {bg} is for {HEADLINE_PX} px headlines, "
                                        f"not {size} px (contrast {contrast(fg, bg):.1f})"))
            elif pair not in HEADLINE_ONLY:
                issues.append(("error", f"'{label}': {fg} on {bg} is not a recommended pairing "
                                        f"(contrast {contrast(fg, bg):.1f})"))
        if any((b - grid["top"]) % grid["line"] for b in element.get("baselines", [])):
            issues.append(("warning", f"'{label}' has a baseline off the lines: text between lines floats"))
        if element.get("overflow"):
            issues.append(("error", f"'{label}' overflows its box by {element['overflow']} line(s): "
                                    "shorten the text first, then a smaller step, then another layout"))
    if len(sizes) > 3:
        issues.append(("warning", f"{len(sizes)} text sizes ({', '.join(map(str, sorted(sizes)))}): at most 3"))
    # Collisions: the space text actually takes (a figure's ink box), against
    # other text and against graphics.
    placed = [e for e in spec["elements"] if e["kind"] in ("text", "graphic")]
    area = lambda e: e.get("used") or e["box"]
    for i, a in enumerate(placed):
        for b in placed[i + 1:]:
            if (a["kind"] == "text" or b["kind"] == "text") and _overlap(area(a), area(b)):
                name = lambda e: e.get("text") or e.get("note") or e["kind"]
                issues.append(("error", f"'{name(a)}' and '{name(b)}' overlap"))
    if image is not None:
        pixels = _pixels(image.convert("RGB"))
        off = sum(1 for p in pixels if p not in _BY_VALUE)
        if off:
            issues.append(("error", f"{100 * off / len(pixels):.1f} % of pixels are not exact inks"))
    return issues


def _overlap(a, b):
    return a[0] < b[2] and b[0] < a[2] and a[1] < b[3] and b[1] < a[3]


def overlay(image, grid):
    """The grid drawn over a copy of the image, for a preview only (never the panel)."""
    from PIL import ImageDraw
    out = image.convert("RGB").copy()
    d = ImageDraw.Draw(out)
    guide, field = (0, 200, 255), (255, 0, 200)
    for line in range(grid.lines + 1):
        y = grid.line_y(line)
        d.line((0, y, grid.width, y), fill=guide)
    for col in range(grid.columns):
        for row in range(grid.rows):
            d.rectangle(tuple(v - (1 if i > 1 else 0) for i, v in enumerate(grid.field(col, row))), outline=field)
    return out


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    l = sub.add_parser("lint", help="check a layout description (and its PNG) against the rules")
    l.add_argument("spec")
    o = sub.add_parser("overlay", help="draw the grid over a design, for a preview")
    o.add_argument("image")
    o.add_argument("-o", "--output", required=True)
    o.add_argument("--columns", type=int)
    args = parser.parse_args(argv)
    from PIL import Image
    if args.command == "lint":
        with open(args.spec, encoding="utf-8") as handle:
            spec = json.load(handle)
        png = os.path.splitext(args.spec)[0] + ".png"
        issues = lint(spec, Image.open(png) if os.path.exists(png) else None)
        for level, message in issues:
            print(f"{level:7} {message}")
        if not issues:
            print("clean: no rule broken")
        return 1 if any(level == "error" for level, _ in issues) else 0
    image = Image.open(args.image)
    spec_path = os.path.splitext(args.image)[0] + ".json"
    columns = args.columns
    if columns is None and os.path.exists(spec_path):
        with open(spec_path, encoding="utf-8") as handle:
            columns = json.load(handle)["grid"]["columns"]
    overlay(image, Grid(image.width, image.height, columns=columns)).save(args.output)
    print(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
