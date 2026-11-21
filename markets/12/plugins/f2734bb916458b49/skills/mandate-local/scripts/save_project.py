"""Save a user-requested portable file with native agent file tools.

No network, approval changes, browser launch, or overwrite of an earlier copy.
The agent supplies a packet file and a destination within its writable workspace.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import tempfile


def save(packet_path, directory):
    packet_bytes = Path(packet_path).read_bytes()
    if len(packet_bytes) > 128 * 1024 * 1024:
        raise ValueError("Save request is too large.")
    packet = json.loads(packet_bytes)
    if packet.get("format") != "mandate-save-request" or packet.get("version") != 1:
        raise ValueError("Invalid save request.")
    name, text = packet.get("filename"), packet.get("text")
    if (not isinstance(name, str) or not name.endswith(".mandate")
            or len(name) > 200 or re.search(r'[/\\\x00-\x1f]', name)):
        raise ValueError("Invalid project filename.")
    if not isinstance(text, str):
        raise ValueError("Missing project file contents.")
    data = text.encode("utf-8")
    if len(data) > 16 * 1024 * 1024:
        raise ValueError("Project exceeds 16 MB.")
    digest = hashlib.sha256(data).hexdigest()
    if digest != packet.get("sha256"):
        raise ValueError("Project hash does not match. No file was saved.")
    document = json.loads(text)
    if (document.get("format") != "mandate-project" or document.get("version") not in (1, 2)
            or not isinstance(document.get("projectId"), str)
            or not isinstance(document.get("tables"), dict)):
        raise ValueError("Invalid project document.")
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
            target = root / (name if number == 1 else f"{name[:-8]} ({number}).mandate")
            if target.is_symlink():
                raise ValueError("Destination is a symbolic link. Choose another folder.")
            try:
                os.link(temporary, target)
            except FileExistsError:
                if not target.is_file() or target.read_bytes() != data:
                    continue
            if target.read_bytes() != data:
                raise ValueError("Saved file verification failed.")
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
