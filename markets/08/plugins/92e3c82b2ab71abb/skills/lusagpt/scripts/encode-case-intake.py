"""Emit preview_case arguments from a local TXT; no network or application writes."""
import argparse
import json
from pathlib import Path


def encode_file(path: Path) -> dict:
    if path.suffix.lower() != '.txt':
        raise ValueError('Expected a .txt file')
    with path.open('rb') as source:
        data = source.read(64 * 1024 + 1)
    if len(data) > 64 * 1024:
        raise ValueError('TXT exceeds 64 KiB')
    text = data.decode('utf-8-sig', errors='strict')
    if '\x00' in text or '\ufffd' in text:
        raise ValueError('Invalid TXT characters')
    if not isinstance(json.loads(text), dict):
        raise ValueError('Expected one JSON object')
    return {'fileName': path.name, 'content': 'hex-json-v1:' + data.hex()}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('file', type=Path)
    args = parser.parse_args()
    try:
        print(json.dumps(encode_file(args.file), ensure_ascii=False))
    except (OSError, ValueError) as error:
        parser.exit(1, f'Cannot encode TXT: {type(error).__name__}\n')
