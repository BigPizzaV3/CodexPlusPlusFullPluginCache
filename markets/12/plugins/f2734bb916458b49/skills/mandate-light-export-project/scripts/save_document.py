"""Verify and save an exported document with native agent file tools only."""
import argparse
import base64
import hashlib
import io
import json
import os
from pathlib import Path
import re
import tempfile
import zipfile

LIMIT = 16 * 1024 * 1024

def save(packet_path, directory):
    raw = Path(packet_path).read_bytes()
    if len(raw) > 2 * LIMIT + 4096:
        raise ValueError("Export request is too large.")
    packet = json.loads(raw)
    if packet.get("format") != "mandate-document-request" or packet.get("version") != 1:
        raise ValueError("Invalid document request.")
    name = packet.get("filename")
    if (not isinstance(name, str) or len(name) > 200 or
            re.search(r'[/\\\x00-\x1f]', name) or not re.search(r'\.(pdf|docx|md|html)$', name)):
        raise ValueError("Invalid document filename.")
    data = base64.b64decode(packet["base64"], validate=True)
    if not data or len(data) > LIMIT:
        raise ValueError("Export exceeds 16 MB.")
    digest = hashlib.sha256(data).hexdigest()
    if digest != packet.get("sha256"):
        raise ValueError("Export hash does not match. No file was saved.")
    suffix = Path(name).suffix
    if suffix == ".pdf" and not data.startswith(b"%PDF-"):
        raise ValueError("Invalid PDF.")
    if suffix == ".docx":
        with zipfile.ZipFile(io.BytesIO(data)) as document:
            if not {"[Content_Types].xml", "word/document.xml"}.issubset(document.namelist()):
                raise ValueError("Invalid Word document.")
    if suffix in (".md", ".html"):
        data.decode("utf-8")
    root = Path(directory).resolve()
    root.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(dir=root, delete=False) as stream:
            temporary = Path(stream.name)
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        for number in range(1, 10001):
            target = root / (name if number == 1 else f"{Path(name).stem} ({number}){suffix}")
            if target.is_symlink():
                raise ValueError("Destination is a symbolic link. Choose another folder.")
            try:
                os.link(temporary, target)
            except FileExistsError:
                if not target.is_file() or target.read_bytes() != data:
                    continue
            if hashlib.sha256(target.read_bytes()).hexdigest() != digest:
                raise ValueError("Saved export verification failed.")
            return {"path": str(target), "sha256": digest, "bytes": len(data), "verified": True}
        raise ValueError("Choose another destination folder.")
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("packet")
    parser.add_argument("--directory", required=True)
    args = parser.parse_args()
    print(json.dumps(save(args.packet, args.directory)))
