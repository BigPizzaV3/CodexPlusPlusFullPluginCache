#!/usr/bin/env python3
"""Offline reviewed-spec packager. Never fetches URLs or executes source instructions."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import tempfile
import textwrap
from urllib.parse import urlsplit, urlunsplit
import zipfile

NAME = re.compile(r'[a-z0-9]+(?:-[a-z0-9]+)*\Z')
SEMVER = re.compile(r'(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)\Z')
# Heuristic tripwires, not a complete data-loss-prevention engine.
SECRETS = [r'sk-(?:proj-)?[A-Za-z0-9_-]{20,}', r'gh[pousr]_[A-Za-z0-9]{20,}',
           r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',
           r'(?i)bearer\s+[A-Za-z0-9._-]{16,}',
           r'(?i)(?:api[_-]?key|password|access[_-]?token|client[_-]?secret)[\"\']?\s*[=:]\s*["\']?[^\s"\']{8,}']


def require(ok, message):
    if not ok:
        raise ValueError(message)


def text_value(value, field, limit=50000):
    require(isinstance(value, str) and 0 < len(value.strip()) <= limit, f'Champ invalide : {field}')
    require('\x00' not in value, f'Caractère nul : {field}')
    return value


def safe_name(value):
    require(isinstance(value, str) and len(value) <= 64 and NAME.fullmatch(value), 'Nom invalide : minuscules, chiffres, tirets, 64 caractères maximum.')
    return value


def canonical_url(raw):
    require(isinstance(raw, str) and len(raw) < 2048 and not any(ord(c) < 33 for c in raw), 'URL invalide.')
    u = urlsplit(raw)
    require(u.scheme == 'https' and u.hostname in ('chatgpt.com', 'chat.openai.com'), 'Lien HTTPS officiel de GPT requis.')
    require(u.username is None and u.password is None and u.port in (None, 443), 'Identifiants ou port non autorisés.')
    require(re.fullmatch(r'/g/g-[A-Za-z0-9][A-Za-z0-9-]*/?', u.path), 'Chemin de GPT invalide.')
    return urlunsplit(('https', u.hostname, u.path.rstrip('/'), '', ''))


def scan_text(content):
    for pattern in SECRETS:
        require(re.search(pattern, content) is None, 'Secret potentiel détecté. Retirer la valeur avant de créer le paquet.')


def scan_strings(value):
    if isinstance(value,str): scan_text(value)
    elif isinstance(value,list):
        for item in value: scan_strings(item)
    elif isinstance(value,dict):
        for item in value.values(): scan_strings(item)


def strings(items, field, minimum=0, maximum=50):
    require(isinstance(items, list) and minimum <= len(items) <= maximum, f'Liste invalide : {field}')
    for item in items:
        text_value(item, field, 500)
    return items


def validate_spec(s):
    require(isinstance(s, dict), 'La spécification doit être un objet JSON.')
    allowed = {'name','display_name','description','author','version','prompts','source_url','fidelity','missing','skills','category'}
    require(not set(s) - allowed, 'Champs inconnus dans la spécification.')
    safe_name(s.get('name'))
    allowed_categories = {'Productivity','Creativity','Developer Tools','Business & Operations','Data & Analytics','Communication','Education & Research','Security','Finance','Healthcare','Travel','Entertainment','Other'}
    require(s.get('category','Productivity') in allowed_categories, 'Catégorie non reconnue.')
    for key, limit in [('display_name',30),('description',4000),('author',80)]:
        text_value(s.get(key), key, limit)
    require(SEMVER.fullmatch(s.get('version','1.0.0')) is not None, 'Version numérique X.Y.Z requise.')
    require(s.get('fidelity') in ('configuration-consultee','adaptation-partielle'), 'Fidélité explicite requise.')
    strings(s.get('prompts'), 'prompts', 1, 3)
    require(all(len(x) <= 128 for x in s['prompts']), 'Amorce limitée à 128 caractères.')
    strings(s.get('missing'), 'missing')
    if s['fidelity'] == 'adaptation-partielle':
        require(bool(s['missing']), 'Indiquer les éléments manquants pour une adaptation partielle.')
    if s.get('source_url'):
        s['source_url'] = canonical_url(s['source_url'])
    require(isinstance(s.get('skills'), list) and 1 <= len(s['skills']) <= 12, 'Prévoir entre 1 et 12 skills.')
    seen = set()
    for skill in s['skills']:
        require(isinstance(skill, dict) and set(skill) == {'name','description','instructions'}, 'Skill : name, description, instructions requis.')
        name = safe_name(skill['name'])
        require(name not in seen, 'Nom de skill dupliqué.')
        seen.add(name)
        require(len(s['name'] + ':' + name) <= 64, 'Identité plugin:skill limitée à 64 caractères.')
        text_value(skill['description'], 'skill.description', 1024)
        text_value(skill['instructions'], 'skill.instructions')
    scan_strings(s)
    return s


def write_json(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def make_icon(path, identity):
    # Each package receives its own geometric vector mark, not an AI-generated logo.
    digest = hashlib.sha256(identity.encode('utf-8')).digest()
    hue = int.from_bytes(digest[:2], 'big') % 360
    shapes = []
    for row in range(5):
        for col in range(3):
            if digest[2 + row * 3 + col] & 1:
                for mirror in sorted({col, 4-col}):
                    shapes.append(f'<rect x="{48+mirror*32}" y="{48+row*32}" width="28" height="28" rx="8" fill="hsl({hue},65%,65%)"/>')
    shapes.append('<path d="M86 225h84m-16-14 16 14-16 14" fill="none" stroke="white" stroke-width="6" stroke-linecap="round"/>')
    svg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256"><rect width="256" height="256" rx="46" fill="#15162B"/>' + ''.join(shapes) + '</svg>'
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(svg,encoding='utf-8')


def build(spec, output):
    s = validate_spec(spec)
    output = Path(output).expanduser()
    require(not output.exists() and not output.is_symlink(), 'Le dossier de sortie existe déjà. Choisir un nouveau dossier ; aucun écrasement.')
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = Path(tempfile.mkdtemp(prefix='.conversion-', dir=output.parent))
    try:
        root = temporary / s['name']
        root.mkdir()
        desc = s['description']
        if s['fidelity'] == 'adaptation-partielle':
            desc = 'Adaptation partielle. ' + desc
        manifest = {
            'name':s['name'], 'version':s.get('version','1.0.0'), 'description':desc,
            'author':{'name':s['author']}, 'skills':'./skills/',
            'interface':{'displayName':s['display_name'], 'shortDescription':textwrap.shorten(desc,width=30,placeholder='…'),
                'longDescription':desc, 'developerName':s['author'], 'category':s.get('category','Productivity'),
                'capabilities':[], 'defaultPrompt':s['prompts'], 'logo':'./assets/icon.svg', 'composerIcon':'./assets/icon.svg'}
        }
        write_json(root / '.codex-plugin/plugin.json', manifest)
        make_icon(root / 'assets/icon.svg', s['name'])
        for skill in s['skills']:
            folder = root / 'skills' / skill['name']
            folder.mkdir(parents=True)
            header = '\n'.join(['---', 'name: ' + json.dumps(skill['name']),
                       'description: ' + json.dumps(skill['description'],ensure_ascii=False), '---', ''])
            (folder / 'SKILL.md').write_text(header + '\n' + skill['instructions'].strip() + '\n', encoding='utf-8')
        audit(root)
        archive = temporary / (s['name'] + '.zip')
        package(root, archive)
        report = {
            'plugin':s['name'], 'source_url':s.get('source_url'), 'fidelity':s['fidelity'],
            'missing':s['missing'], 'structure':'validated-local',
            'behavioral_tests':'not-executed-by-packager', 'installed':False, 'published':False,
            'archive_sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),
            'note':'Bilan privé séparé du ZIP. Vérifier le comportement et les droits avant partage.'}
        write_json(temporary / 'bilan-conversion.json', report)
        # Reserve destination atomically. A simultaneous conversion cannot replace it.
        output.mkdir()
        for child in temporary.iterdir():
            shutil.move(str(child), str(output / child.name))
        return output / archive.name
    finally:
        shutil.rmtree(temporary, ignore_errors=True)


def audit(root):
    root = Path(root).expanduser()
    require(root.is_dir() and not root.is_symlink(), 'Dossier de plugin réel requis.')
    files = sorted(root.rglob('*'))
    require(len(files) <= 300, 'Paquet trop volumineux pour cet audit.')
    total = 0
    for file in files:
        require(not file.is_symlink(), 'Lien symbolique interdit dans le paquet.')
        if not file.is_file():
            require(file.is_dir(), 'Type de fichier non pris en charge.')
            continue
        rel = file.relative_to(root)
        require(not any(x in ('.git','__pycache__','node_modules') or x.startswith('.env') for x in rel.parts), 'Fichier privé ou temporaire dans le paquet.')
        require(file.suffix.lower() in ('.md','.json','.py','.svg','.png','.jpg','.jpeg','.yaml','.yml','.txt'), 'Type de fichier non admis dans le paquet.')
        total += file.stat().st_size
        require(total <= 20_000_000, 'Paquet supérieur à 20 Mo.')
        if file.suffix.lower() not in ('.png','.jpg','.jpeg'):
            content = file.read_text(encoding='utf-8')
            scan_text(content)
            require(('[' + 'TODO:') not in content, 'Placeholder non résolu dans le paquet.')
            if file.suffix.lower() == '.svg':
                require(not re.search(r'<script|<!ENTITY|<!DOCTYPE|\bon\w+\s*=|(?:href)\s*=',content,re.I), 'SVG actif ou ressource externe interdite.')
    m = json.loads((root / '.codex-plugin/plugin.json').read_text(encoding='utf-8'))
    require(isinstance(m, dict), 'Manifeste objet requis.')
    require(m.get('name') == root.name, 'Identité du dossier et du manifeste différente.')
    safe_name(m['name'])
    require(re.fullmatch(r'\d+\.\d+\.\d+(?:\+[a-zA-Z0-9.-]+)?', m.get('version','')), 'Version invalide.')
    text_value(m.get('description'), 'manifest.description')
    require(m.get('skills') == './skills/', 'Chemin de skills invalide.')
    require('apps' not in m and 'mcpServers' not in m and 'hooks' not in m, 'Cet audit est réservé aux paquets skills-only.')
    text_value(m.get('author',{}).get('name'), 'author.name')
    interface = m.get('interface',{})
    for key in ('displayName','shortDescription','longDescription','developerName','category'):
        text_value(interface.get(key), key)
    prompts = strings(interface.get('defaultPrompt'), 'defaultPrompt', 1, 3)
    require(all(len(p) <= 128 for p in prompts), 'Amorce trop longue.')
    for key in ('composerIcon','logo','logoDark'):
        if key in interface:
            value = interface[key]
            require(isinstance(value,str) and value.startswith('./assets/') and '..' not in Path(value).parts, 'Chemin d’asset invalide.')
            require((root / value).is_file(), 'Asset manquant.')
    skills = list((root / 'skills').glob('*/SKILL.md'))
    require(bool(skills), 'Aucun skill.')
    for path in skills:
        content = path.read_text(encoding='utf-8')
        require(content.startswith('---\n') and '\n---\n' in content[4:], 'Frontmatter absent.')
        header, body = content[4:].split('\n---\n',1)
        require(bool(body.strip()), 'Skill vide.')
        fields = {}
        for line in header.splitlines():
            if ': ' in line:
                k,v = line.split(': ',1)
                fields[k] = json.loads(v) if v.startswith('"') else v
        require(fields.get('name') == path.parent.name, 'Nom du skill différent du dossier.')
        safe_name(fields['name'])
        text_value(fields.get('description'), 'skill.description', 1024)
    return {'status':'validated-local', 'files':sum(p.is_file() for p in files), 'skills':len(skills), 'bytes':total}


def package(root, archive):
    root, archive = Path(root), Path(archive)
    audit(root)
    require(not archive.exists() and not archive.is_symlink(), 'Archive déjà existante ; aucun écrasement.')
    require(root.resolve() not in archive.resolve().parents, 'Créer le ZIP en dehors du plugin.')
    archive.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(archive, 'x', zipfile.ZIP_DEFLATED) as z:
        for file in sorted(root.rglob('*')):
            if file.is_file():
                # Archive paths start at .codex-plugin/, skills/, assets/; no enclosing folder.
                data = file.read_bytes()
                entry = zipfile.ZipInfo(file.relative_to(root).as_posix(), (2026,1,1,0,0,0))
                entry.compress_type = zipfile.ZIP_DEFLATED
                entry.external_attr = 0o100644 << 16
                z.writestr(entry, data)
    with zipfile.ZipFile(archive) as z:
        require(z.testzip() is None, 'Archive corrompue.')
    return archive


def main():
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest='command',required=True)
    sub.add_parser('url').add_argument('url')
    a = sub.add_parser('build'); a.add_argument('spec'); a.add_argument('output')
    a = sub.add_parser('audit'); a.add_argument('root')
    a = sub.add_parser('package'); a.add_argument('root'); a.add_argument('archive')
    args = p.parse_args()
    try:
        if args.command == 'url': print(canonical_url(args.url))
        elif args.command == 'build':
            require(Path(args.spec).stat().st_size <= 1_000_000, 'Spécification trop volumineuse.')
            print(build(json.loads(Path(args.spec).read_text(encoding='utf-8')), args.output))
        elif args.command == 'audit': print(json.dumps(audit(args.root),ensure_ascii=False))
        else: print(package(args.root,args.archive))
    except (ValueError, OSError, KeyError, TypeError, AttributeError) as e:
        # No raw payload or source content in error output.
        print('Échec du contrôle : ' + str(e) if isinstance(e,ValueError) and not isinstance(e,json.JSONDecodeError) else 'Échec : entrée invalide ou fichier inaccessible.')
        raise SystemExit(1)

if __name__ == '__main__': main()
