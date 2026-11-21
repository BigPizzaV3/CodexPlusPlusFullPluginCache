#!/usr/bin/env python3
"""Build a deterministic Device It review ZIP from the explicit file allowlist."""
import argparse
import hashlib
import json
from pathlib import Path
import zipfile

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('output', type=Path, help='New ZIP path outside the package source')
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
output = args.output.expanduser().resolve()
if output == root or root in output.parents:
    parser.error('Output must be outside the package source')
if output.exists() or output.with_suffix(output.suffix + '.sha256').exists():
    parser.error('Output already exists; choose a new ZIP path')
files = json.loads((root / 'package-files.json').read_text())
if len(set(files)) != len(files):
    raise ValueError('Duplicate package file')
entries = []
for relative in sorted(files):
    name = Path(relative)
    if name.is_absolute() or '..' in name.parts or any(p in {'local-state', 'node_modules', 'work', 'deploy', 'mdm', 'push', 'templates', 'references'} for p in name.parts):
        raise ValueError(f'Excluded package path: {relative}')
    source = root
    for part in name.parts:
        source /= part
        if source.is_symlink():
            raise ValueError(f'Symlink is forbidden: {relative}')
    if not source.is_file():
        raise ValueError(f'Missing package file: {relative}')
    entries.append((relative, source.read_bytes()))
output.parent.mkdir(parents=True, exist_ok=True)
with zipfile.ZipFile(output, 'x', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
    for relative, data in entries:
        info = zipfile.ZipInfo(relative, date_time=(2026, 1, 1, 0, 0, 0))
        info.create_system = 3
        info.external_attr = (0o100755 if relative.endswith('.sh') else 0o100644) << 16
        info.compress_type = zipfile.ZIP_DEFLATED
        archive.writestr(info, data, compresslevel=9)
with zipfile.ZipFile(output) as archive:
    assert archive.testzip() is None
    assert set(archive.namelist()) == set(files)
digest = hashlib.sha256(output.read_bytes()).hexdigest()
output.with_suffix(output.suffix + '.sha256').write_text(f'{digest}  {output.name}\n')
print(f'{output}\nSHA-256 {digest}')
