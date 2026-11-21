"""Optional offline checks for the public Build_ package; never an installer or submission."""
from __future__ import annotations
import argparse
import ast
import hashlib
import io
import json
import os
from pathlib import Path
import re
import sys
import tempfile
import unittest
from urllib.parse import urlsplit
import zipfile

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[3]
SCRIPT = Path(__file__).resolve().parent
SCHEMA = 'https://agent-plugins.org/schemas/1.0.0/plugin.schema.json'


def payload(root):
    for path in sorted(Path(root).rglob('*')):
        if '__pycache__' in path.parts or path.suffix in ('.pyc', '.pyo'):
            continue
        if path.is_symlink():
            raise ValueError('Linked package file: '+str(path))
        if not path.is_file():
            continue
        rel = path.relative_to(root).as_posix()
        if rel == 'skills/build/scripts/LogReport.zip' or rel.startswith('skills/build/scripts/.LogReport-'):
            continue
        yield rel, path


def read_json(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def interface(manifest):
    return manifest.get('extensions', {}).get('com.openai', {}).get('interface', manifest.get('interface', {}))


def validate_listing_contract(manifest):
    ui = interface(manifest)
    if ui.get('displayName') != 'Build_':
        raise ValueError('Unexpected display name.')
    for field in ('displayName', 'shortDescription', 'longDescription', 'developerName', 'category'):
        if not isinstance(ui.get(field), str) or not ui[field].strip():
            raise ValueError('Missing listing field: '+field)
    for field, limit in (('displayName', 30), ('shortDescription', 30),
                         ('longDescription', 4000), ('developerName', 80)):
        if len(ui[field]) > limit:
            raise ValueError('Listing field exceeds limit: '+field)
    if ui['category'] != 'Developer Tools':
        raise ValueError('Unexpected public category.')
    expected_urls = {
        'websiteURL': 'https://build.berrergate.com/',
        'supportURL': 'https://build.berrergate.com/support/',
        'privacyPolicyURL': 'https://build.berrergate.com/privacy/',
        'termsOfServiceURL': 'https://build.berrergate.com/terms/',
    }
    for field, expected in expected_urls.items():
        if ui.get(field) != expected:
            raise ValueError('Public listing URL changed: '+field)
    return {'display_name': ui['displayName'], 'host_rendering': 'not_tested'}


def validate_guidance_contract(root, manifest):
    ext = manifest.get('extensions', {}).get('com.openai', {})
    if ext.get('onboardingSkill') != './skills/build-start/SKILL.md':
        raise ValueError('Onboarding reference changed.')
    for name in ('build', 'build-start'):
        path = Path(root)/'skills'/name/'SKILL.md'
        source = path.read_text(encoding='utf-8')
        parts = source.split('---', 2)
        if len(parts) != 3 or parts[0] or not parts[2].strip():
            raise ValueError('Missing skill frontmatter: '+name)
        values = {}
        for line in parts[1].splitlines():
            if ': ' in line:
                key, value = line.split(': ', 1)
                values[key] = value.strip()
        if values.get('name') != name or not values.get('description'):
            raise ValueError('Invalid skill metadata: '+name)
        if len(source.encode()) > 1024*1024:
            raise ValueError('Skill too large.')
    return {'skills': ['build', 'build-start'], 'native_activation': 'not_tested'}


def validate_web_contract(root, manifest):
    if manifest.get('name') != 'berrer-build-mcp' or manifest.get('$schema') != SCHEMA:
        raise ValueError('Unexpected package identity/format.')
    paths = {p for p, _ in payload(root)}
    if '.app.json' in paths or 'hooks.json' in paths:
        raise ValueError('Public upload must not contain private App bindings or hooks.')
    ext = manifest.get('extensions', {}).get('com.openai', {})
    legacy = read_json(Path(root)/'.codex-plugin/plugin.json')
    for candidate in (manifest, legacy):
        ce = candidate.get('extensions', {}).get('com.openai', {})
        if candidate.get('apps') is not None or ce.get('apps') is not None:
            raise ValueError('Public manifests must not declare apps.')
    if ext.get('hooks'):
        raise ValueError('Unexpected hook configuration.')
    expected = {'$schema': 'https://agent-plugins.org/schemas/1.0.0/mcp.schema.json',
                'mcpServers': {'build-dependency-checker': {
                    'type': 'streamable-http', 'url': 'https://build-api.berrergate.com/mcp'}}}
    if read_json(Path(root)/'mcp.json') != expected:
        raise ValueError('Unexpected portable MCP endpoint or transport.')
    compat = {'mcpServers': {'build-dependency-checker': {
        'type': 'http', 'url': 'https://build-api.berrergate.com/mcp'}}}
    if read_json(Path(root)/'.mcp.json') != compat or legacy.get('mcpServers') != './.mcp.json':
        raise ValueError('MCP compatibility configuration differs.')
    discovered = sorted(p for p in paths if p.startswith('skills/') and p.endswith('/SKILL.md'))
    if discovered != ['skills/build-start/SKILL.md', 'skills/build/SKILL.md']:
        raise ValueError('Unexpected skill set.')
    if interface(manifest).get('defaultPrompt') != 'Press Enter to begin':
        raise ValueError('Existing starter prompt changed.')
    return {'configuration': 'portable_public_mcp', 'private_app_binding': 'absent',
            'guide_is_build_prerequisite': False, 'live_connection': 'not_tested_by_offline_check'}


def validate_review_contract(manifest):
    ext = manifest.get('extensions', {}).get('com.openai', {})
    review, publication = ext.get('review', {}), ext.get('publication', {})
    cases = review.get('test_cases', {})
    if set(cases) != {'positive', 'negative'} or len(cases['positive']) != 5 or len(cases['negative']) != 3:
        raise ValueError('Initial public MCP review needs five positive and three negative cases.')
    for kind, items in cases.items():
        if not isinstance(items, list):
            raise ValueError('Review cases must be arrays.')
        for case in items:
            fields = ('description', 'prompt', 'tools_triggered', 'expected_behavior') if kind == 'positive' else ('description', 'prompt')
            if not isinstance(case, dict) or any(not isinstance(case.get(f), str) or not case[f].strip() for f in fields):
                raise ValueError('Incomplete review case: '+kind)
            if kind == 'positive':
                tools = {name.strip() for name in case['tools_triggered'].split(',')}
                if not tools <= {'get_build_workflow', 'check_windows_dependencies'}:
                    raise ValueError('A public case expects an undeclared tool.')
    if review.get('commerce') is not False:
        raise ValueError('Recorded no-commerce declaration changed.')
    prompts = review.get('prompts')
    if not isinstance(prompts, list) or not 1 <= len(prompts) <= 20 or any(not isinstance(p, str) or not p.strip() or len(p) > 4000 for p in prompts):
        raise ValueError('Invalid review prompts.')
    if not isinstance(publication.get('release_notes'), str) or not publication['release_notes'].strip():
        raise ValueError('Missing current release notes.')
    if 'test_credentials' in review or 'reviewer_instructions' in review:
        raise ValueError('Reviewer credentials/instructions belong in secure Portal fields.')
    demo = review.get('demo_recording_url')
    if demo is not None:
        u = urlsplit(demo) if isinstance(demo, str) else None
        if not u or u.scheme != 'https' or not u.netloc or u.username or u.password:
            raise ValueError('Invalid demo recording URL.')
    return {'positive_cases': 5, 'negative_cases': 3,
            'demo_recording': 'declared_not_playback_verified' if demo else 'missing',
            'countries': 'preserve_saved_portal_targeting' if 'countries' not in publication else 'declared',
            'portal_checks': 'not_tested_by_offline_check',
            'submission_ready': False}


def validate(root=ROOT):
    root = Path(root)
    manifest = read_json(root/'plugin.json')
    legacy = read_json(root/'.codex-plugin/plugin.json')
    if manifest.get('version') != legacy.get('version') or manifest.get('name') != legacy.get('name'):
        raise ValueError('Manifest identity mismatch.')
    if not re.fullmatch(r'\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?', manifest['version']):
        raise ValueError('Invalid version.')
    current_ui=dict(interface(manifest)); legacy_ui=dict(legacy.get('interface', {}))
    for ui in (current_ui, legacy_ui):
        if ui.get('defaultPrompt') is None: ui.pop('defaultPrompt', None)
    if current_ui != legacy_ui:
        raise ValueError('Manifest presentation mismatch.')
    if legacy.get('skills', '').rstrip('/') != './skills':
        raise ValueError('Compatibility skill path mismatch.')
    for field in ('description', 'author', 'homepage'):
        if manifest.get(field) != legacy.get(field):
            raise ValueError('Compatibility metadata mismatch: '+field)
    ext=manifest.get('extensions', {}).get('com.openai', {})
    if legacy.get('apps') != ext.get('apps'):
        raise ValueError('Compatibility App binding mismatch.')
    if legacy.get('requires_local_executor') != ext.get('requires_local_executor'):
        raise ValueError('Compatibility executor setting mismatch.')
    for field in ('onboardingSkill', 'review', 'publication'):
        if legacy.get('extensions', {}).get('com.openai', {}).get(field) != ext.get(field):
            raise ValueError('Compatibility OpenAI metadata mismatch: '+field)
    listing = validate_listing_contract(manifest)
    guidance = validate_guidance_contract(root, manifest)
    web = validate_web_contract(root, manifest)
    review = validate_review_contract(manifest)
    entries = dict(payload(root)); seen = set()
    for rel, path in entries.items():
        key = rel.casefold()
        if key in seen or '\\' in rel or '..' in Path(rel).parts:
            raise ValueError('Unsafe/colliding path: '+rel)
        seen.add(key)
        if path.suffix == '.py':
            ast.parse(path.read_text(encoding='utf-8'), filename=rel, feature_version=(3, 10))
    from branding_check import png_info
    for field in ('composerIcon', 'composerIconDark', 'logo', 'logoDark'):
        rel = interface(manifest)[field]
        if not rel.startswith('./assets/') or '..' in Path(rel).parts:
            raise ValueError('Unsafe asset reference.')
        png_info((root/rel).read_bytes())
    actual = {rel: hashlib.sha256(path.read_bytes()).hexdigest() for rel, path in entries.items()
              if rel != 'skills/build/Automation/AB60.json'}
    expected = read_json(root/'skills/build/Automation/AB60.json')['file_sha256']
    if actual != expected:
        bad = sorted(set(actual)^set(expected) | {p for p in actual.keys() & expected.keys() if actual[p] != expected[p]})
        raise ValueError('Package inventory mismatch: '+', '.join(bad[:10]))
    return {'status': 'passed', 'name': manifest['name'], 'version': manifest['version'],
            'files': len(entries), 'integrity': 'matched', 'listing': listing,
            'guidance': guidance, 'web': web, 'review': review}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--self-test', action='store_true')
    p.add_argument('--no-report', action='store_true')
    args = p.parse_args(); result = {'scope': 'offline plugin package', 'native_chatgpt': 'not_tested'}
    stream = io.StringIO(); code = 0
    try:
        result['package'] = validate()
        if args.self_test:
            sys.path.insert(0, str(SCRIPT/'tests'))
            suite = unittest.defaultTestLoader.loadTestsFromNames(['test_testable_delivery', 'test_qualified_delivery'])
            run = unittest.TextTestRunner(stream=stream, verbosity=1).run(suite)
            result['tests'] = {'run': run.testsRun, 'failures': len(run.failures), 'errors': len(run.errors), 'skipped': len(run.skipped)}
            code = 0 if run.wasSuccessful() else 1
    except Exception as exc:
        result['error'] = str(exc); code = 1
    result['exit_code'] = code
    print(json.dumps(result, indent=2))
    if stream.getvalue(): print(stream.getvalue())
    if not args.no_report:
        fd, temporary = tempfile.mkstemp(prefix='.LogReport-', suffix='.zip', dir=SCRIPT); os.close(fd)
        try:
            with zipfile.ZipFile(temporary, 'w', zipfile.ZIP_DEFLATED) as z:
                z.writestr('report.json', json.dumps(result, indent=2)); z.writestr('console.txt', stream.getvalue())
            os.replace(temporary, SCRIPT/'LogReport.zip')
        finally:
            Path(temporary).unlink(missing_ok=True)
    return code


if __name__ == '__main__':
    raise SystemExit(main())
