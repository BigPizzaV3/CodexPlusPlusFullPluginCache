"""Lukka compact notation parser.

Hosted Lukka MCP servers return responses in a compact object notation -
unquoted keys, bare-string values (addresses, ISO timestamps, enum
values), ``_`` for null. This is NOT RFC 8259 JSON, so ``json.loads``
rejects it.

Usage:
    from lukka_notation import load

    data = load('/tmp/response.raw')   # handles both JSON and Lukka form

Table-shaped containers (``{cols: [...], rows: [[...], ...]}``) are
frequent in Lukka responses. Use ``rows_to_dicts`` to flatten them into
list-of-dicts shapes.
"""

import json
from pathlib import Path


class LukkaParser:
    """Recursive-descent parser for Lukka compact notation."""

    def __init__(self, s):
        self.s = s
        self.i = 0
        self.n = len(s)

    def _skip_ws(self):
        while self.i < self.n and self.s[self.i].isspace():
            self.i += 1

    def _peek(self):
        self._skip_ws()
        return self.s[self.i] if self.i < self.n else ''

    def _consume(self, c):
        self._skip_ws()
        if self.i < self.n and self.s[self.i] == c:
            self.i += 1
            return True
        return False

    def parse(self):
        val = self._parse_value()
        self._skip_ws()
        if self.i != self.n:
            raise ValueError(f"Trailing data at pos {self.i}")
        return val

    def _parse_value(self):
        self._skip_ws()
        if self.i >= self.n:
            raise ValueError("Unexpected end of input")
        c = self.s[self.i]
        if c == '{':
            return self._parse_object()
        if c == '[':
            return self._parse_array()
        if c == '"':
            return self._parse_string()
        return self._parse_bare_value()

    def _parse_object(self):
        self.i += 1
        obj = {}
        self._skip_ws()
        if self._peek() == '}':
            self.i += 1
            return obj
        while True:
            self._skip_ws()
            key = self._parse_key()
            if not self._consume(':'):
                raise ValueError(f"Expected ':' after key {key!r} at pos {self.i}")
            obj[key] = self._parse_value()
            self._skip_ws()
            if self._consume(','):
                continue
            if self._consume('}'):
                break
            raise ValueError(f"Expected ',' or '}}' at pos {self.i}")
        return obj

    def _parse_array(self):
        self.i += 1
        arr = []
        self._skip_ws()
        if self._peek() == ']':
            self.i += 1
            return arr
        while True:
            arr.append(self._parse_value())
            self._skip_ws()
            if self._consume(','):
                continue
            if self._consume(']'):
                break
            raise ValueError(f"Expected ',' or ']' at pos {self.i}")
        return arr

    def _parse_string(self):
        self.i += 1
        out = []
        while self.i < self.n:
            c = self.s[self.i]
            if c == '\\' and self.i + 1 < self.n:
                esc = self.s[self.i + 1]
                if esc == 'n':
                    out.append('\n')
                elif esc == 't':
                    out.append('\t')
                elif esc == 'r':
                    out.append('\r')
                elif esc == '"':
                    out.append('"')
                elif esc == '\\':
                    out.append('\\')
                else:
                    out.append(esc)
                self.i += 2
                continue
            if c == '"':
                self.i += 1
                return ''.join(out)
            out.append(c)
            self.i += 1
        raise ValueError("Unterminated string")

    def _parse_key(self):
        self._skip_ws()
        if self.i < self.n and self.s[self.i] == '"':
            return self._parse_string()
        j = self.i
        while j < self.n and self.s[j] not in ':,}{[]" \t\n\r':
            j += 1
        key = self.s[self.i:j]
        self.i = j
        return key

    def _parse_bare_value(self):
        j = self.i
        while j < self.n and self.s[j] not in ',}]':
            j += 1
        tok = self.s[self.i:j].rstrip()
        self.i = j
        if tok == '_' or tok == 'null':
            return None
        if tok == 'true':
            return True
        if tok == 'false':
            return False
        try:
            if '.' in tok or 'e' in tok or 'E' in tok:
                return float(tok)
            return int(tok)
        except ValueError:
            return tok


def loads(text):
    """Parse a string. Accepts standard JSON or Lukka compact notation."""
    text = text.strip()
    if not text:
        raise ValueError("Empty input")
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    return LukkaParser(text).parse()


def load(path):
    """Load a file. Accepts standard JSON or Lukka compact notation."""
    return loads(Path(path).read_text())


def rows_to_dicts(container):
    """Convert ``{cols: [...], rows: [[...], ...]}`` into list-of-dicts.

    Returns ``None`` if the container is not in the expected column-oriented
    shape. Useful because many Lukka responses embed tables (transactions,
    candles, market caps, risk factors) as cols/rows pairs.
    """
    if not isinstance(container, dict):
        return None
    cols = container.get("cols")
    rows = container.get("rows")
    if not isinstance(cols, list) or not isinstance(rows, list):
        return None
    return [dict(zip(cols, row)) for row in rows if isinstance(row, list)]
