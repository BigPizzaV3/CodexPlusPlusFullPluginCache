#!/usr/bin/env python3
"""Offline package integrity checks; does not assert live MCP compatibility."""
import ast
import json
import re
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
errors = []

def require(ok, message):
    if not ok:
        errors.append(message)

skills = sorted((root / 'skills').glob('*/workflow.md'))
require(len(skills) == 66, 'Expected 66 bundled workflows')
require((root / 'SKILL.md').is_file(), 'Missing root SKILL.md')
for directory in (root / 'skills').iterdir():
    if directory.is_dir():
        require((directory / 'workflow.md').is_file(), f'Missing workflow: {directory.name}')
references = 0
for path in root.rglob('*.md'):
    text = path.read_text()
    if path.name in ('SKILL.md', 'workflow.md'):
        require(text.startswith('---\n'), f'No frontmatter: {path}')
        meta = text.split('---', 2)[1]
        match = re.search(r'^name:\s*([^\n]+)', meta, re.M)
        require(match and match[1] == path.parent.name, f'Skill name mismatch: {path}')
        require(bool(re.search(r'^description:\s*\S', meta, re.M)), f'No description: {path}')
        require(not re.search(r'^model:|^tools:', meta, re.M), f'Provider-specific metadata: {path}')
    if path.is_relative_to(root / 'skills') or path.is_relative_to(root / 'shared'):
        require(not any(x in text for x in ('CLAUDE_PLUGIN_ROOT', '/gather:', '/plugin install', 'claude.ai')), f'Old runtime dependency: {path}')
    for ref in re.findall(r'`((?:\.\./)+[^`\s]+\.(?:md|py|html))`', text):
        if '*' in ref:
            continue
        references += 1
        target = (path.parent / ref).resolve()
        require(target.is_relative_to(root) and target.is_file(), f'Missing resource: {path.relative_to(root)} -> {ref}')
catalogue = (root / 'SKILL.md').read_text()
for ref in re.findall(r'\]\((skills/[^)]+/workflow\.md)\)', catalogue):
    require((root / ref).is_file(), f'Missing catalogue workflow: {ref}')
require(len(re.findall(r'\]\((skills/[^)]+/workflow\.md)\)', catalogue)) == 66, 'Catalogue must list 66 workflows')
for path in (root / 'scripts').rglob('*.py'):
    try:
        ast.parse(path.read_text())
    except SyntaxError as exc:
        errors.append(f'{path}: {exc}')
if errors:
    print('\n'.join(errors))
    sys.exit(1)
print(f'PASS: root skill, {len(skills)} workflows, {references} relative file references and valid Python syntax.')
print('Live integration smoke results are in docs/VALIDATION.md; full workflow acceptance remains pending.')
