from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

required_files = [
    ROOT / 'SKILL.md',
    ROOT / 'README.md',
    ROOT / 'TESTS.md',
    ROOT / 'adapters' / 'generic-system-prompt.md',
    ROOT / 'adapters' / 'chatgpt-codex.md',
    ROOT / 'adapters' / 'claude.md',
    ROOT / 'adapters' / 'gemini.md',
]

missing = [str(p.relative_to(ROOT)) for p in required_files if not p.exists()]
assert not missing, f"Missing required files: {missing}"

skill = (ROOT / 'SKILL.md').read_text(encoding='utf-8')
assert skill.startswith('---\n'), 'SKILL.md must start with YAML frontmatter'
frontmatter = skill.split('---', 2)[1]
assert re.search(r'^name:\s+socratic-tutor\s*$', frontmatter, re.M), 'Invalid or missing skill name'
assert re.search(r'^description:\s+.+$', frontmatter, re.M), 'Missing description'

name = re.search(r'^name:\s+(.+)$', frontmatter, re.M).group(1).strip()
assert len(name) <= 64 and re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name), 'Name violates Agent Skills naming rules'

description = re.search(r'^description:\s+(.+)$', frontmatter, re.M).group(1).strip()
assert 1 <= len(description) <= 1024, 'Description violates length rules'

required_phrases = [
    'one focused question',
    'three genuine attempts',
    'purely factual',
    'misconception',
    'clarifying',
    'probing',
    'hypothetical',
    'devil',
    'host system',
]
low = skill.lower()
for phrase in required_phrases:
    assert phrase in low, f"SKILL.md missing expected concept: {phrase}"

assert len(skill.splitlines()) < 500, 'SKILL.md should remain under 500 lines for progressive disclosure'

for adapter in required_files[3:]:
    text = adapter.read_text(encoding='utf-8').lower()
    assert 'skill.md' in text, f"{adapter.name} must point back to SKILL.md rather than duplicate the skill"

print('PASS: package structure and core invariants validated')
