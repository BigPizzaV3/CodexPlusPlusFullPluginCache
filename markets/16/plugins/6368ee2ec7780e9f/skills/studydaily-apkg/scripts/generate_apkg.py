"""Offline APKG exporter for ChatGPT's Python runtime (standard library only).

The empty SQLite template is produced by Study Daily's shared Dart exporter.
Only text notes and new cards are inserted here; no network or MCP is used.
"""
import hashlib
from contextlib import closing
import html
import io
import json
from pathlib import Path
import re
import sqlite3
import sys
import tempfile
import zipfile

EPOCH = 1700000000
TYPE_ID = 1700000000001
MAX_INPUT = 1024 * 1024
TEMPLATE = Path(__file__).resolve().parent.parent / "assets/schema11-template.anki2"


def compact(value):
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"))


def digest(value):
    return hashlib.sha256(compact(value).encode("utf-8")).hexdigest()


def checked_text(value, maximum, label):
    if not isinstance(value, str):
        raise ValueError(f"{label} must be text")
    # Dart String.trim includes FEFF; preserve the same stable identity inputs.
    trim_chars = " \t\n\r\v\f\u00a0\u1680\u2028\u2029\u202f\u205f\u3000\ufeff" + "".join(chr(code) for code in range(0x2000, 0x200b))
    value = value.replace("\r\n", "\n").replace("\r", "\n").strip(trim_chars)
    if not value or len(value.encode("utf-16-le")) // 2 > maximum or re.search(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]", value):
        raise ValueError(f"{label} is empty, too long, or contains control characters")
    return value


def escape_text(value):
    value = html.escape(value, quote=False).replace("\n", "<br>")
    for char, entity in [("[", "&#91;"), ("]", "&#93;"), ("{", "&#123;"), ("}", "&#125;")]:
        value = value.replace(char, entity)
    return value


def normalized(raw):
    if not isinstance(raw, dict) or set(raw) - {"title", "deck_key", "cards"}:
        raise ValueError("Expected title, optional deck_key, and cards")
    if len(compact(raw).encode("utf-8")) > MAX_INPUT:
        raise ValueError("Input exceeds 1 MiB")
    title = checked_text(raw.get("title"), 120, "title")
    if "::" in title or "\n" in title or "\t" in title:
        raise ValueError("title must be a single deck name")
    key = raw.get("deck_key", digest(["studydaily-title-v1", title]))
    if not isinstance(key, str) or not re.fullmatch(r"[a-z0-9-]{1,64}", key):
        raise ValueError("deck_key must contain 1–64 lowercase letters, digits or hyphens")
    rows = raw.get("cards")
    if not isinstance(rows, list) or not rows:
        raise ValueError("cards must contain at least one question/answer pair")
    pairs, seen = [], set()
    for row in rows:
        if not isinstance(row, dict) or set(row) != {"question", "answer"}:
            raise ValueError("Each card requires exactly question and answer")
        pair = tuple(checked_text(row[name], 4000, name) for name in ("question", "answer"))
        if pair in seen:
            raise ValueError("Duplicate question/answer pair")
        seen.add(pair)
        pairs.append(pair)
    return title, key, pairs


def package_bytes(raw):
    title, key, pairs = normalized(raw)
    deck_id = 1700000000000 + int(digest(["deck", key])[:10], 16)
    with tempfile.TemporaryDirectory(prefix="studydaily-offline-") as directory:
        db_path = Path(directory) / "collection.anki2"
        with closing(sqlite3.connect(TEMPLATE.as_uri() + "?mode=ro", uri=True)) as source, closing(sqlite3.connect(db_path)) as db:
            source.backup(db)
            if db.execute("SELECT ver FROM col").fetchone() != (11,):
                raise ValueError("Unsupported SQLite template")
            if any(db.execute(f"SELECT count(*) FROM {table}").fetchone()[0] for table in ("notes", "cards", "revlog", "graves")):
                raise ValueError("SQLite template must contain no user records")
            decks = json.loads(db.execute("SELECT decks FROM col").fetchone()[0])
            deck = next(iter(decks.values()))
            deck.update(id=deck_id, name=title)
            db.execute("UPDATE col SET decks=?", (compact({str(deck_id): deck}),))
            ids = set()
            for position, (question, answer) in enumerate(pairs, 1):
                guid = "sd1-" + digest([key, question, answer])
                note_id = 1700000000000 + int(digest(["note", guid])[:10], 16)
                card_id = 1700000000000 + int(digest(["card", guid])[:10], 16)
                if note_id in ids or card_id in ids or note_id == card_id:
                    raise ValueError("ID collision")
                ids.update((note_id, card_id))
                front, back = escape_text(question), escape_text(answer)
                checksum = int(hashlib.sha1(re.sub(r"<[^>]*>", "", front).encode("utf-8")).hexdigest()[:8], 16)
                db.execute("INSERT INTO notes VALUES (?,?,?,?,?,?,?,?,?,?,?)", (note_id, guid, TYPE_ID, EPOCH, -1, " chatgpt ", front + "\x1f" + back, front, checksum, 0, ""))
                db.execute("INSERT INTO cards VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (card_id, note_id, deck_id, 0, EPOCH, -1, 0, 0, position, 0, 0, 0, 0, 0, 0, 0, 0, ""))
            db.commit()
            if db.execute("PRAGMA integrity_check").fetchone() != ("ok",):
                raise ValueError("SQLite verification failed")
            if db.execute("SELECT count(*) FROM notes").fetchone()[0] != len(pairs) or db.execute("SELECT count(*) FROM cards").fetchone()[0] != len(pairs):
                raise ValueError("Card count verification failed")
        data = io.BytesIO()
        with zipfile.ZipFile(data, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            for name, payload in [("collection.anki2", db_path.read_bytes()), ("media", b"{}")]:
                entry = zipfile.ZipInfo(name, (2023, 11, 14, 22, 13, 20))
                entry.compress_type = zipfile.ZIP_DEFLATED
                entry.external_attr = 0o600 << 16
                archive.writestr(entry, payload)
        result = data.getvalue()
        if len(result) > 2 * 1024 * 1024:
            raise ValueError("Package exceeds 2 MiB")
        with zipfile.ZipFile(io.BytesIO(result)) as archive:
            if archive.testzip() is not None or set(archive.namelist()) != {"collection.anki2", "media"}:
                raise ValueError("Archive verification failed")
        return result, len(pairs)


def generate_package(raw, output):
    """Use from Code Interpreter: generate_package(dict, '/mnt/data/name.apkg')."""
    data, count = package_bytes(raw)
    output = Path(output)
    if output.suffix.lower() != ".apkg":
        raise ValueError("Output must end in .apkg")
    with output.open("xb") as file:
        file.write(data)
    return {"file": str(output), "card_count": count, "byte_size": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def main():
    if len(sys.argv) != 3:
        raise ValueError("Usage: python3 generate_apkg.py input.json output.apkg")
    with Path(sys.argv[1]).open("rb") as file:
        data = file.read(MAX_INPUT + 1)
    if len(data) > MAX_INPUT:
        raise ValueError("Input exceeds 1 MiB")
    print(compact(generate_package(json.loads(data), sys.argv[2])))


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, sqlite3.Error, zipfile.BadZipFile):
        print("APKG generation failed; check the input and output path.", file=sys.stderr)
        sys.exit(1)
