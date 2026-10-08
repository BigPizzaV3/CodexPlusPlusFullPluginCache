# -*- coding: utf-8 -*-
"""生成完整本地市场；不运行包内代码，不上传文件。"""
from pathlib import Path, PurePosixPath
import collections
import hashlib
import io
import json
import os
import re
import tarfile

ROOT=Path(__file__).resolve().parents[1]
directory=json.loads((ROOT/'directory.json').read_text())
entries=directory['entries']
groups=[]
results=[]

def choose_group(name):
    for group in groups:
        if len(group['plugins'])<1000 and name not in group['names']:
            return group
    number=len(groups)+1
    group={'number':number,'name':f'codex-plus-full-local-{number:02d}','names':set(),'plugins':[]}
    groups.append(group)
    return group

for item in entries:
    output=dict(item)
    if item['state']!='cached':
        results.append(output)
        continue
    try:
        archive_path=ROOT/'archives'/item['archiveFile']
        data=archive_path.read_bytes()
        output['archiveSha256']=hashlib.sha256(data).hexdigest()
        with tarfile.open(fileobj=io.BytesIO(data),mode='r:gz') as archive:
            members=archive.getmembers()
            if sum(m.size for m in members if m.isfile())>512*1024**2:
                output['marketState']='expanded_over_512MiB';results.append(output);continue
            if any(not(m.isfile() or m.isdir()) or PurePosixPath(m.name).is_absolute() or '..' in PurePosixPath(m.name).parts or '\\' in m.name for m in members):
                output['marketState']='archive_member_needs_review';results.append(output);continue
            candidates=[m for m in members if m.isfile() and (str(PurePosixPath(m.name))=='plugin.json' or m.name.endswith('/plugin.json') and len(PurePosixPath(m.name).parts)<=2 or m.name.endswith('.codex-plugin/plugin.json'))]
            if not candidates:
                output['marketState']='manifest_not_found';results.append(output);continue
            manifest=min(candidates,key=lambda m:(len(PurePosixPath(m.name).parts),0 if str(PurePosixPath(m.name))=='plugin.json' else 1))
            metadata=json.load(archive.extractfile(manifest))
            name=metadata.get('name')
            if not isinstance(name,str) or not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9._-]{0,127}',name):
                output['marketState']='name_needs_review';results.append(output);continue
            package_root=PurePosixPath(manifest.name).parent.parent if PurePosixPath(manifest.name).parent.name=='.codex-plugin' else PurePosixPath(manifest.name).parent
            package_key=hashlib.sha256(item['id'].encode()).hexdigest()[:16]
            group=choose_group(name)
            group_root=ROOT/'markets'/f"{group['number']:02d}"
            destination=group_root/'plugins'/package_key
            destination.mkdir(parents=True,exist_ok=True,mode=0o700)
            file_count=byte_count=0
            for member in members:
                if not member.isfile():continue
                try:path=PurePosixPath(member.name).relative_to(package_root)
                except ValueError:continue
                target=destination/str(path)
                target.parent.mkdir(parents=True,exist_ok=True,mode=0o700)
                body=archive.extractfile(member).read();target.write_bytes(body);target.chmod(0o700 if member.mode&0o111 else 0o600)
                file_count+=1;byte_count+=len(body)
            group['names'].add(name)
            group['plugins'].append({'name':name,'source':{'source':'local','path':'./plugins/'+package_key},'policy':{'installation':'AVAILABLE','authentication':'ON_USE'},'category':'Productivity'})
            output.update({'marketState':'ready','marketplaceName':group['name'],'marketplaceRoot':str(group_root),'manifestName':name,'manifestVersion':metadata.get('version'),'licenseDeclaration':metadata.get('license'),'files':file_count,'expandedBytes':byte_count})
            results.append(output)
    except Exception as error:
        output['marketState']='read_error';output['errorType']=type(error).__name__;results.append(output)

for group in groups:
    root=ROOT/'markets'/f"{group['number']:02d}"
    path=root/'.agents/plugins/marketplace.json';path.parent.mkdir(parents=True,exist_ok=True)
    manifest={'name':group['name'],'interface':{'displayName':f"Codex++ Full Local Cache {group['number']:02d}"},'plugins':group['plugins']}
    path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
directory['entries']=results
(ROOT/'directory.json').write_text(json.dumps(directory,ensure_ascii=False,indent=2)+'\n')
summary={'directoryEntries':len(results),'archiveStates':dict(collections.Counter(x['state'] for x in results)),'marketStates':dict(collections.Counter(x.get('marketState','not_cached') for x in results)),'marketplaces':[{'name':g['name'],'packages':len(g['plugins']),'root':str(ROOT/'markets'/f"{g['number']:02d}")} for g in groups],'compressedBytes':sum(x.get('archiveBytes',0) for x in results if x['state']=='cached'),'expandedBytes':sum(x.get('expandedBytes',0) for x in results),'publicUpload':False,'installerInvoked':False}
(ROOT/'summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(summary,ensure_ascii=False,indent=2))
