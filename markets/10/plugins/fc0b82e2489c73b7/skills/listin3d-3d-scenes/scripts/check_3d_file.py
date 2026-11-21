#!/usr/bin/env python3
"""Check a GLB model or HTML scene against Listin3D's 3D proposal rules.

Usage: python3 check_3d_file.py FILE
Prints a JSON report and exits 0 when the file can be sent, 1 otherwise.
Uses only the Python standard library.
"""
import json
import os
import struct
import sys

MIB = 1024 * 1024
GLB_MAX = 50 * MIB
HTML_MAX = 5 * MIB
INLINE_CHARACTERS = 1_000_000
UPLOAD_LINK_MAX = 30 * MIB


def check_glb(data, problems, warnings):
    if len(data) < 20 or data[:4] != b"glTF":
        problems.append("Not a binary glTF file (missing glTF header).")
        return
    version, length, chunk_length, chunk_type = struct.unpack_from("<IIII", data, 4)
    if version != 2:
        problems.append(f"glTF version {version}; Listin3D needs version 2.")
    if length != len(data):
        problems.append("The header length does not match the file size.")
    if chunk_type != 0x4E4F534A or chunk_length < 2 or chunk_length > len(data) - 20:
        problems.append("The first chunk is not a valid JSON chunk.")
        return
    try:
        gltf = json.loads(data[20 : 20 + chunk_length].decode("utf-8"))
    except ValueError:
        problems.append("The JSON chunk cannot be parsed.")
        return
    if (gltf.get("asset") or {}).get("version") != "2.0":
        problems.append('asset.version must be "2.0".')
    if not gltf.get("scenes"):
        problems.append("The file has no scenes.")
    external = [
        entry.get("uri")
        for entry in (gltf.get("buffers") or []) + (gltf.get("images") or [])
        if entry.get("uri") and not entry["uri"].startswith("data:")
    ]
    if external:
        problems.append(
            "External files are referenced (" + ", ".join(external[:3])
            + "). Embed all buffers and textures in the GLB."
        )
    if len(data) > GLB_MAX:
        problems.append("Larger than 50 MB.")
    elif len(data) > 15 * MIB:
        warnings.append("Over 15 MB; consider compressing for phones.")


def check_html(data, problems, warnings):
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        problems.append("Not valid UTF-8 text.")
        return None
    lower = text.lower()
    if "\x00" in text or "<script" not in lower:
        problems.append("A single-file HTML scene must contain a script.")
    if "LISTIN3D_READY" not in text:
        problems.append(
            'Missing the readiness snippet: parent.postMessage({ type: "LISTIN3D_READY" }, "*").'
        )
    if "LISTIN3D_VISIBILITY" not in text:
        warnings.append("Does not handle LISTIN3D_VISIBILITY; pause rendering when hidden.")
    if len(data) > HTML_MAX:
        problems.append("Larger than 5 MB.")
    for marker in ('src="./', "src='./", 'href="./', "from './", 'from "./'):
        if marker in text:
            warnings.append("Relative paths found; local side files are not uploaded.")
            break
    return text


def main():
    if len(sys.argv) != 2:
        print(__doc__.strip())
        return 2
    path = sys.argv[1]
    with open(path, "rb") as handle:
        data = handle.read()
    problems, warnings = [], []
    name = os.path.basename(path)
    if data[:4] == b"glTF" or name.lower().endswith(".glb"):
        kind = "model"
        check_glb(data, problems, warnings)
        text = None
    elif name.lower().endswith((".html", ".htm")):
        kind = "html"
        text = check_html(data, problems, warnings)
    else:
        kind = None
        text = None
        problems.append("Use a .glb model or a .html scene.")
    if kind == "html" and text is not None and len(text) <= INLINE_CHARACTERS:
        transfer = "submit_3d_scene_html (send the file text as html)"
    elif len(data) <= UPLOAD_LINK_MAX:
        transfer = "create_3d_upload_link (exact size_bytes), or import_3d_file for an attached/public file"
    else:
        transfer = "import_3d_file from a public HTTPS link, or upload on the Listin3D website"
    print(
        json.dumps(
            {
                "file": name,
                "kind": kind,
                "size_bytes": len(data),
                "ok": not problems,
                "problems": problems,
                "warnings": warnings,
                "transfer": transfer if not problems else None,
            },
            indent=2,
        )
    )
    return 0 if not problems else 1


if __name__ == "__main__":
    sys.exit(main())
