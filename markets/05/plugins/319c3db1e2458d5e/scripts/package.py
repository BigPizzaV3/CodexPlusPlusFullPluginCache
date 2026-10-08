#!/usr/bin/env python3
"""Build deterministic core and optional remote-MCP distributions; no network."""
from pathlib import Path
import hashlib
import json
import zipfile
from check import check, ROOT

def build(root=ROOT):
    check(root)
    out = root / 'dist'
    out.mkdir(exist_ok=True)
    files = {}
    for folder in ('.codex-plugin', 'skills', 'integrations', 'docs', 'assets'):
        for path in sorted((root / folder).rglob('*')):
            if path.is_file():
                files[path.relative_to(root).as_posix()] = path.read_bytes()
    files['README.md'] = (root / 'README.md').read_bytes()
    for path in sorted((root / 'scripts').glob('*.py')):
        files[path.relative_to(root).as_posix()] = path.read_bytes()
    checksums = []
    for profile in ('core', 'remote-mcp'):
        entries = dict(files)
        manifest = json.loads(entries['.codex-plugin/plugin.json'])
        manifest.pop('mcpServers', None)
        if profile == 'remote-mcp':
            entries['.mcp.json'] = files['integrations/remote-mcp.json']
            manifest['mcpServers'] = './.mcp.json'
        entries['.codex-plugin/plugin.json'] = (json.dumps(manifest, indent=2)+'\n').encode()
        archive = out / f'research-plugin-{profile}.zip'
        with zipfile.ZipFile(archive, 'w', compression=zipfile.ZIP_DEFLATED) as z:
            for name, data in sorted(entries.items()):
                info = zipfile.ZipInfo(name, date_time=(2026, 9, 7, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o100644 << 16
                z.writestr(info, data)
        with zipfile.ZipFile(archive) as z:
            assert z.testzip() is None, 'Archive integrity failure'
            assert '.codex-plugin/plugin.json' in z.namelist()
        checksums.append(hashlib.sha256(archive.read_bytes()).hexdigest()+'  '+archive.name)
        print(f'Built {archive.name} ({archive.stat().st_size} bytes)')
    (out/'SHA256SUMS').write_text('\n'.join(checksums)+'\n')

if __name__ == '__main__':
    build()
