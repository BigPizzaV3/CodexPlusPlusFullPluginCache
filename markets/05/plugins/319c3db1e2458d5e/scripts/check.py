#!/usr/bin/env python3
"""Check portable package invariants with Python's standard library."""
from pathlib import Path
from urllib.parse import urlsplit
import json
import re
import struct

ROOT = Path(__file__).resolve().parents[1]

def check(root=ROOT):
    manifest = json.loads((root / '.codex-plugin/plugin.json').read_text())
    assert manifest['name'] == root.name, 'Plugin name and directory differ'
    assert manifest['skills'] == './skills/', 'Unexpected skills path'
    for field in ('composerIcon', 'logo'):
        target = manifest['interface'].get(field)
        assert isinstance(target, str) and target.startswith('./assets/'), f'Missing or invalid {field}'
        path = (root / target).resolve()
        assert path.is_relative_to(root.resolve()), f'Escaping {field} path'
        header = path.read_bytes()[:24]
        assert header[:8] == bytes([137, 80, 78, 71, 13, 10, 26, 10]), f'{field} must be PNG'
        assert header[12:16] == b'IHDR', f'Invalid PNG header: {field}'
        width, height = struct.unpack('>II', header[16:24])
        assert width == height and width > 0, f'{field} must be square'
    skills = sorted((root / 'skills').glob('*/SKILL.md'))
    assert len(skills) == 4, 'Missing or unexpected skill'
    for path in skills:
        text = path.read_text()
        assert text.startswith('---\n'), f'Missing frontmatter: {path}'
        assert f'name: {path.parent.name}\n' in text, f'Name mismatch: {path}'
    for path in sorted(root.rglob('*')):
        if 'dist' in path.relative_to(root).parts or '__pycache__' in path.parts:
            continue
        assert not path.is_symlink(), f'Nonportable symlink: {path}'
        if path.suffix not in {'.md', '.json', '.py'}:
            continue
        text = path.read_text()
        assert not re.search(r'[\u0400-\u04ff]', text), f'Non-English authored text: {path}'
        if path.suffix == '.md':
            for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', text):
                if urlsplit(target).scheme or target.startswith('#'):
                    continue
                resolved = (path.parent / target.split('#')[0]).resolve()
                assert resolved.is_relative_to(root.resolve()), f'Escaping link: {path}: {target}'
                assert resolved.exists(), f'Broken link: {path}: {target}'
    cfg = json.loads((root / 'integrations/remote-mcp.json').read_text())
    for server in cfg['mcpServers'].values():
        assert set(server) == {'type', 'url'}, 'Credentials or local execution in MCP config'
        url = urlsplit(server['url'])
        assert server['type'] == 'http' and url.scheme == 'https' and url.hostname
        assert url.hostname not in {'localhost', '127.0.0.1', '::1'}
        assert not url.username and not url.password and not url.query
    print(f'Portable package checks passed: {len(skills)} skills, 2 remote endpoints')

if __name__ == '__main__':
    check()
