#!/usr/bin/env python3
"""Local preflight, deterministic archives, and submission dossier. No network calls."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import re
import struct
import unicodedata
import xml.etree.ElementTree as ET
import convert as core

CATEGORIES={'Productivity','Creativity','Developer Tools','Business & Operations','Data & Analytics','Communication','Education & Research','Security','Finance','Healthcare','Travel','Entertainment','Other'}


def frontmatter(path):
    content=path.read_text(encoding='utf-8')
    head=content[4:].split('\n---\n',1)[0]
    fields={}
    for line in head.splitlines():
        if ': ' in line:
            k,v=line.split(': ',1)
            fields[k]=json.loads(v) if v.startswith('"') else v
    return fields


def one_line(value,maximum):
    return isinstance(value,str) and bool(value.strip()) and len(value)<=maximum and not any(unicodedata.category(c) in ('Cc','Cf','Zl','Zp') for c in value)


def image_dimensions(path):
    data=path.read_bytes()
    core.require(len(data)<=5*1024*1024,'Asset supérieur à 5 Mo.')
    if path.suffix.lower()=='.svg':
        text=data.decode('utf-8')
        core.require(not re.search(r'<!DOCTYPE|<!ENTITY|<script|\bon\w+\s*=|href\s*=',text,re.I),'SVG actif ou externe interdit.')
        node=ET.fromstring(text)
        core.require(node.tag.split('}')[-1]=='svg','Racine SVG invalide.')
        if 'viewBox' in node.attrib:
            box=[float(x) for x in re.split(r'[ ,]+',node.attrib['viewBox'].strip())]
            core.require(len(box)==4,'viewBox invalide.')
            return box[2],box[3]
        return float(node.attrib['width']),float(node.attrib['height'])
    if path.suffix.lower()=='.png':
        core.require(data[:8]==b'\x89PNG\r\n\x1a\n' and data[12:16]==b'IHDR','En-tête PNG invalide.')
        return struct.unpack('>II',data[16:24])
    raise ValueError('Utiliser SVG inerte ou PNG ; autre format à contrôler avec le décodeur de l’hôte.')


def preflight(root):
    root=Path(root)
    checks=[]
    def check(field,ok,issue):
        checks.append({'field':field,'status':'pass' if ok else 'fail','issue':None if ok else issue})
    try:
        structural=core.audit(root)
        check('structure',True,'')
    except (ValueError,OSError,KeyError,TypeError,ET.ParseError):
        return {'status':'fail','checks':[{'field':'structure','status':'fail','issue':'Audit structurel échoué ; exécuter convert.py audit pour localiser le contrôle.'}]}
    m=json.loads((root/'.codex-plugin/plugin.json').read_text())
    i=m['interface']
    check('interface.category',i.get('category') in CATEGORIES,'Catégorie non reconnue par le portail.')
    for f,maxlen in [('displayName',30),('shortDescription',30),('developerName',80)]:
        check('interface.'+f,one_line(i.get(f),maxlen),f'Texte non vide, une ligne, {maxlen} caractères maximum.')
    check('version',len(m['version'])<=64,'Version limitée à 64 caractères.')
    check('interface.longDescription',isinstance(i.get('longDescription'),str) and 0<len(i['longDescription'].strip())<=4000,'Description de 1 à 4000 caractères.')
    check('author.name',m['author']['name']==i['developerName'],'L’auteur et le développeur doivent correspondre.')
    normalized=set()
    for n,p in enumerate(i['defaultPrompt']):
        norm=' '.join(unicodedata.normalize('NFKC',p).split()).casefold()
        check(f'prompts[{n}]',one_line(p,128) and norm not in normalized and not re.search(r'@\w',p),'Amorce unique, une ligne, 128 caractères, sans mention technique.')
        normalized.add(norm)
    for f in ('logo','composerIcon'):
        ok=False;problem='Asset absent ou invalide.'
        try:
            value=i[f];asset=root/value
            core.require(value.startswith('./assets/') and '..' not in Path(value).parts,'Chemin non local.')
            w,h=image_dimensions(asset)
            ok=w==h and 48<=w<=4096
            problem='Image carrée de 48 à 4096 pixels, au plus 5 Mo.'
        except (ValueError,OSError,KeyError,TypeError,ET.ParseError,struct.error): pass
        check('interface.'+f,ok,problem)
    for s in sorted((root/'skills').glob('*/SKILL.md')):
        fm=frontmatter(s)
        check(s.parent.name+':identity',len(m['name']+':'+fm['name'])<=64,'Identité plugin:skill limitée à 64 caractères.')
    for file in sorted(root.rglob('*.md')):
        for raw in re.findall(r'\]\(([^)]+)\)',file.read_text()):
            link=raw.split('#',1)[0]
            if not link or re.match(r'[a-zA-Z][a-zA-Z0-9+.-]*:',link):continue
            dest=(file.parent/link).resolve()
            ok=dest.is_relative_to(root.resolve()) and dest.exists()
            check(str(file.relative_to(root))+':link',ok,'Référence locale absente ou sortant du paquet.')
    return {'status':'pass' if all(c['status']=='pass' for c in checks) else 'fail','checked_against':'OpenAI submission-errors, 2026-09-21, skills-only subset','structural':structural,'checks':checks,'limitations':['Précontrôle local ; le scan du portail et les essais métier restent distincts.','Le contrôle PNG vérifie en-tête et dimensions ; le décodage visuel doit être effectué par l’hôte.']}


def package(root,archive):
    report=preflight(root)
    core.require(report['status']=='pass','Précontrôle de dépôt échoué. Exécuter preflight avant de créer le ZIP.')
    p=core.package(root,archive)
    return {'archive':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'preflight':report}


def submission(root,cases_path,output):
    root=Path(root);m=json.loads((root/'.codex-plugin/plugin.json').read_text())
    cases=json.loads(Path(cases_path).read_text())
    core.require(isinstance(cases,dict) and set(cases)=={'positive','negative'},'Listes positive et negative requises.')
    for key,count in [('positive',5),('negative',3)]:
        core.require(isinstance(cases[key],list) and len(cases[key])==count,f'{count} cas {key} requis.')
        for item in cases[key]:
            core.require(isinstance(item,dict),'Cas invalide.')
            for f in ('prompt','expected_behavior','expected_result','fixture','execution'):
                core.text_value(item.get(f),f)
    core.scan_text(json.dumps(cases,ensure_ascii=False))
    out=Path(output)
    core.require(not out.exists(),'Dossier de soumission déjà présent.')
    info={k:m['interface'].get(k) for k in ('displayName','shortDescription','longDescription','developerName','category','defaultPrompt')}
    result={'format':'qg-review-dossier-v1','note':'Dossier de travail ; aucun format d’import officiel n’est présumé.',
        'package':{'name':m['name'],'version':m['version']},'submission_type':'Skills only',
        'listing':info,'tests':cases,'tools':[],'release_notes':f"Version {m['version']} de {m['interface']['displayName']}. {m['description']}",
        'publication_status':'not-submitted','prerequisites_to_verify':['Identité vérifiée','Permissions de dépôt','Scan de chaque skill','Territoires','Attestations affichées'],
        'preflight':preflight(root)}
    core.write_json(out,result)
    return out


def main():
    p=argparse.ArgumentParser(description=__doc__);sub=p.add_subparsers(dest='command',required=True)
    a=sub.add_parser('preflight');a.add_argument('root');a.add_argument('--report')
    a=sub.add_parser('package');a.add_argument('root');a.add_argument('archive');a.add_argument('--report')
    a=sub.add_parser('submission');a.add_argument('root');a.add_argument('cases');a.add_argument('output')
    a=p.parse_args()
    try:
        if a.command=='submission':print(submission(a.root,a.cases,a.output));return
        result=preflight(a.root) if a.command=='preflight' else package(a.root,a.archive)
        if a.report:core.write_json(Path(a.report),result)
        print(json.dumps(result,ensure_ascii=False,indent=2))
        if result.get('status')=='fail':raise SystemExit(1)
    except (ValueError,OSError,KeyError,TypeError,ET.ParseError):
        print('Échec : vérifier les entrées, le précontrôle et les chemins. Aucun dépôt distant effectué.')
        raise SystemExit(1)

if __name__=='__main__':main()
