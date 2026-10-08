#!/usr/bin/env python3
"""Check the package's observable retrieval, identity, and export behavior."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
from library import Library, ROOT, export_asset

lib=Library();data=lib.data
assert len(lib.entries)==1052 and len(lib.instruments)==15 and len(lib.concepts)==258
assert sum(1 for e in lib.entries.values() if e['discipline']=='core')==261
assert len(lib.disciplines)==14 and len(lib.pointers)==50
assert sum(d['sourceModels'] for d in lib.disciplines.values())==811
assert sum(d['sourceApparatus'] for d in lib.disciplines.values())==241
source=(ROOT/'data/complete-library.md').read_text()
assert source==data['source']['text']
assert hashlib.sha256(source.encode()).hexdigest()==data['source']['sha256']
for key,item in lib.items.items():
    record=lib.get(key);assert record['entry']==item and record['requested_id']==key
for key,pointer in lib.pointers.items():
    record=lib.get(key)
    assert record['canonical_id']==pointer['canonicalId']
    assert record['reference_context']['previousContext']==pointer['previousContext']
assert lib.get('core:137')['entry']['name']=='Node-by-Node Correction'
assert lib.get('core:137')['canonical_id']!=lib.get('concept:137')['canonical_id']
assert lib.get('core:137')['entry']['name']!=lib.get('concept:137')['entry']['name']
assert lib.get('instrument:J')['canonical_id']=='BE-P-J'
try: lib.get('137')
except ValueError: pass
else: raise AssertionError('Bare numeric ID should remain ambiguous')
for collection,count in [('catalog',1052),('core',261),('disciplines',791),('instruments',15),('concepts',258),('all',1325)]:
    ids=[];offset=0
    while True:
        result=lib.search('',collection=collection,limit=50,offset=offset)
        ids.extend(e['id'] for e in result['results'])
        if result['next_offset'] is None: break
        offset=result['next_offset']
    assert len(ids)==count and len(set(ids))==count,(collection,len(ids))
for d in lib.disciplines.values(): assert lib.search('',discipline=d['id'])['total']==len(d['entries'])
assert lib.search('',collection='core',part='I')['total']==110
assert lib.search('',collection='core',part='II')['total']==151
assert not lib.search('xyz_nonexistent_987654')['results']
assert lib.search('Node-by-Node Correction')['results'][0]['id']=='BE-00-137'
for p in lib.pointers.values(): assert lib.search(p['id'])['results'][0]['id']==p['canonicalId']
for key in lib.items:
    linked=lib.links(key)
    for link in linked['links']: assert link['id'] in lib.items
for route in data['routes']:
    detail=lib.routes(route['id'])
    for step in detail['steps']: assert step['entry_name']==lib.get(step['entry'])['entry']['name']
    assert detail['counter']['entry_name']==lib.get(detail['counter']['entry'])['entry']['name']
assert len(lib.routes())==12
with tempfile.TemporaryDirectory(prefix='be-plugin-verify-') as directory:
    target=Path(directory)/'atlas.html';receipt=export_asset('atlas',target)
    assert target.read_bytes()==(ROOT/'assets/Business-Engineer-Atlas.html').read_bytes()
    assert b'window.Atlas3D={plan,connections,mount}' in target.read_bytes()
    try: export_asset('atlas',target)
    except ValueError: pass
    else: raise AssertionError('Unintended overwrite should be rejected')
    assert export_asset('atlas',target,force=True)['sha256']==receipt['sha256']
for args in [['stats'],['search','bottleneck','--collection','core','--limit','3'],['get','core:137','concept:137'],['links','BE-00-137'],['routes','geopolitics'],['practice','engine']]:
    command=subprocess.run([sys.executable,str(ROOT/'scripts/library.py'),*args],capture_output=True,text=True,check=True)
    json.loads(command.stdout)
failure=subprocess.run([sys.executable,str(ROOT/'scripts/library.py'),'get','137'],capture_output=True,text=True)
assert failure.returncode==2 and 'ambiguous' in json.loads(failure.stderr)['error']
print('PASS Source fidelity, all 1,375 current/earlier/reference IDs, collection pagination, typed links, all 12 paths, CLI behavior, and exact Atlas export.')
