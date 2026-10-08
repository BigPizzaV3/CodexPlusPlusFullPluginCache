#!/usr/bin/env python3
"""Private resumable workflow ledger. Records observations; never operates a browser."""
from __future__ import annotations
import argparse
from datetime import datetime,timezone
import json
import os
from pathlib import Path
import tempfile
from urllib.parse import urlsplit
import convert as core

STAGES=('source','behavior','branding','package','preflight','draft','upload','scan','compliance','submission','publication')
STATUSES=('pending','running','passed','failed','blocked')


def persist(path,data):
    path=Path(path)
    core.require(not path.is_symlink(),'État symbolique interdit.')
    path.parent.mkdir(parents=True,exist_ok=True)
    fd,tmp=tempfile.mkstemp(prefix='.checkpoint-',dir=path.parent)
    try:
        with os.fdopen(fd,'w',encoding='utf-8') as handle:
            json.dump(data,handle,ensure_ascii=False,indent=2);handle.write('\n')
        os.replace(tmp,path)
    finally:
        if os.path.exists(tmp):os.unlink(tmp)


def init(path,package,version):
    core.safe_name(package)
    core.require(not Path(path).exists(),'État déjà existant ; reprendre le fichier existant.')
    core.require(isinstance(version,str) and len(version)<=64,'Version invalide.')
    data={'schema':1,'package':package,'version':version,'plugin_id':None,'dashboard_url':None,'archive_sha256':None,
          'stages':{s:{'status':'pending','attempts':0,'evidence':[]} for s in STAGES}}
    persist(path,data);return data


def update(path,stage,status,evidence,plugin_id=None,url=None,sha=None,retry=False):
    core.require(stage in STAGES and status in STATUSES,'Étape ou statut inconnu.')
    core.text_value(evidence,'evidence',2000);core.scan_text(evidence)
    data=json.loads(Path(path).read_text(encoding='utf-8'))
    if plugin_id:
        core.require(bool(__import__('re').fullmatch(r'[A-Za-z0-9_-]{1,128}',plugin_id)),'Identité invalide.')
        core.require(data['plugin_id'] in (None,plugin_id),'Le plugin cible a changé : reprise refusée.')
        data['plugin_id']=plugin_id
    if url:
        u=urlsplit(url)
        core.require(u.scheme=='https' and u.hostname in ('platform.openai.com','chatgpt.com') and not u.username and not u.password and not u.query and not u.fragment,'URL publique sans paramètres requise.')
        data['dashboard_url']=url
    if sha:
        core.require(bool(__import__('re').fullmatch(r'[0-9a-f]{64}',sha)),'SHA-256 invalide.')
        data['archive_sha256']=sha
    record=data['stages'][stage]
    if retry:
        core.require(record['attempts']<3,'Budget de trois reprises épuisé pour cette étape.')
        record['attempts']+=1
    if status=='passed':
        if stage in ('upload','scan','submission','publication'):
            core.require(bool(data['plugin_id']) and bool(data['dashboard_url']),'Identité et URL observées requises.')
        if stage in ('upload','scan'):
            core.require(bool(data['archive_sha256']),'Empreinte du paquet requise.')
        if stage=='publication':
            core.require(data['stages']['submission']['status']=='passed','Soumission vérifiée requise avant publication.')
    record['status']=status
    record['evidence'].append({'at':datetime.now(timezone.utc).isoformat(),'observation':evidence})
    persist(path,data);return data


def main():
    p=argparse.ArgumentParser(description=__doc__);sub=p.add_subparsers(dest='cmd',required=True)
    a=sub.add_parser('init');a.add_argument('path');a.add_argument('package');a.add_argument('version')
    a=sub.add_parser('show');a.add_argument('path')
    a=sub.add_parser('set');a.add_argument('path');a.add_argument('stage',choices=STAGES);a.add_argument('status',choices=STATUSES);a.add_argument('--evidence',required=True);a.add_argument('--plugin-id');a.add_argument('--url');a.add_argument('--sha');a.add_argument('--retry',action='store_true')
    a=p.parse_args()
    try:
        if a.cmd=='init':result=init(a.path,a.package,a.version)
        elif a.cmd=='show':result=json.loads(Path(a.path).read_text())
        else:result=update(a.path,a.stage,a.status,a.evidence,a.plugin_id,a.url,a.sha,a.retry)
        print(json.dumps(result,ensure_ascii=False,indent=2))
    except (ValueError,OSError,KeyError,TypeError):
        print('État non modifié : entrée invalide, identité incohérente ou budget de reprise épuisé.')
        raise SystemExit(1)

if __name__=='__main__':main()
