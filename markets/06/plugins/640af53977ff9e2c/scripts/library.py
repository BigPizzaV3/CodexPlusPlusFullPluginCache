#!/usr/bin/env python3
"""Read-only ontology retrieval and explicit local exports; Python standard library only."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import sys
import unicodedata

ROOT = Path(__file__).resolve().parents[1]

def normalized(value):
    text = unicodedata.normalize('NFKD', str(value or '')).lower()
    return re.sub(r'[^a-z0-9]+', ' ', ''.join(c for c in text if not unicodedata.combining(c))).strip()

class Library:
    def __init__(self, path=None):
        self.data = json.loads(Path(path or ROOT / 'data/library.json').read_text())
        self.entries = {e['id']: e for e in self.data['entries']}
        self.instruments = {e['id']: e for e in self.data['instruments']}
        self.concepts = {e['id']: e for e in self.data['concepts']}
        self.items = {**self.entries, **self.instruments, **self.concepts}
        self.pointers = {p['id']: p for p in self.data['pointers']}
        self.disciplines = {d['id']: d for d in self.data['disciplines']}
        self.incoming = {}
        for e in list(self.entries.values()) + list(self.instruments.values()):
            for target in e.get('coreRefs', []) + e.get('instrumentRefs', []):
                self.incoming.setdefault(target, []).append(e['id'])
        self.pointer_terms = {}
        for p in self.pointers.values():
            self.pointer_terms.setdefault(p['canonicalId'], []).extend([p['id'], p['name'], p.get('discipline', '')])
        self.index = {e['id']: normalized(' '.join(str(e.get(k, '')) for k in ['id','name','sourceNumber','essence','body','definition','keyQuestion','apply','use_when','aliases','sectionName','discipline']) + ' ' + ' '.join(self.pointer_terms.get(e['id'], []))) for e in self.items.values()}

    def resolve(self, token):
        if token.isdigit():
            raise ValueError('A number alone is ambiguous. Use core:'+token+' or concept:'+token+', or a full entry ID.')
        if token.lower().startswith('core:'):
            number = token.split(':', 1)[1]
            if not number.isdigit(): raise ValueError('Core IDs require a numeric model number.')
            token = 'BE-00-' + str(int(number)).zfill(3)
        elif token.lower().startswith('concept:'):
            number = token.split(':', 1)[1]
            if not number.isdigit(): raise ValueError('Concept IDs require a numeric concept number.')
            token = 'BE-M' + str(int(number)).zfill(4)
        elif token.lower().startswith('instrument:'):
            token = 'BE-P-' + token.split(':', 1)[1].upper()
        if token not in self.items and token not in self.pointers:
            raise ValueError('Unknown entry: '+token+'. Search by name or use stats to inspect the collections.')
        return token

    def collection(self, entry_id):
        if entry_id in self.concepts: return 'concepts'
        if entry_id in self.instruments: return 'instruments'
        return 'core' if self.entries[entry_id]['discipline'] == 'core' else 'disciplines'

    def summary(self, e):
        return {'id':e['id'], 'name':e['name'], 'collection':self.collection(e['id']),
                'discipline':e.get('discipline'), 'type':e.get('kind', e.get('form')),
                'essence':e.get('essence', e.get('definition','')),
                'key_question':e.get('keyQuestion',''), 'source_line':e.get('sourceLine'),
                'status':e.get('status'), 'atlas_fragment':'#atlas?entry='+e['id']}

    def get(self, token):
        requested = self.resolve(token)
        pointer = self.pointers.get(requested)
        canonical = pointer['canonicalId'] if pointer else requested
        entry = self.items[canonical]
        return {'requested_id':requested, 'canonical_id':canonical, 'collection':self.collection(canonical),
                'entry':entry, 'reference_context':pointer,
                'provenance':{'source':self.data['source']['filename'] if canonical not in self.concepts else 'Earlier reconciled ontology',
                              'source_line':entry.get('sourceLine'), 'source_sha256':self.data['source']['sha256'] if canonical not in self.concepts else None,
                              'attribution':self.data['source']['attribution']},
                'atlas_fragment':'#atlas?entry='+requested}

    def pool(self, collection='catalog'):
        if collection == 'all': return list(self.items.values())
        if collection == 'instruments': return list(self.instruments.values())
        if collection == 'concepts': return list(self.concepts.values())
        if collection in ['core','disciplines']: return [e for e in self.entries.values() if self.collection(e['id']) == collection]
        return list(self.entries.values())

    def search(self, query='', collection='catalog', discipline=None, part=None, kind=None, limit=8, offset=0):
        if discipline and discipline not in self.disciplines: raise ValueError('Unknown discipline: '+discipline)
        if not 1 <= limit <= 50 or offset < 0: raise ValueError('Use limit 1–50 and a nonnegative offset.')
        q = normalized(query); words = q.split()
        found = []
        for e in self.pool(collection):
            if discipline and e.get('discipline') != discipline: continue
            if part and e.get('part') != part: continue
            if kind and e.get('kind',e.get('form')) != kind: continue
            if not all(w in self.index[e['id']] for w in words): continue
            title = normalized(e['name'])
            score = (120 if q and normalized(e['id']) == q else 0) + (100 if q and title == q else 0) + (80 if q and str(e.get('sourceNumber')) == query else 0) + (30 if q and q in title else 0) + sum(4 for w in words if w in title)
            if e['id'] in self.pointer_terms and q in [normalized(x) for x in self.pointer_terms[e['id']]]: score += 120
            found.append((score,e))
        found.sort(key=lambda pair:-pair[0])
        chosen = found[offset:offset+limit]
        return {'query':query, 'collection':collection, 'total':len(found), 'offset':offset,
                'next_offset':offset+limit if offset+limit < len(found) else None,
                'results':[self.summary(e) for _,e in chosen],
                'note':'Retrieval matches, not a recommendation score. Read get results before applying an entry.'}

    def links(self, token):
        record = self.get(token); key = record['canonical_id']; e = record['entry']; links = []
        def add(other, kind, direction, evidence):
            if other in self.items and other != key:
                links.append({'id':other,'name':self.items[other]['name'],'collection':self.collection(other),'type':kind,'direction':direction,'evidence':evidence})
        if key in self.concepts:
            for r in self.data['relations']:
                if r['subject'] == key: add(r['object'],r['type'],'outgoing',r['description'])
                elif r['object'] == key: add(r['subject'],r['type'],'incoming',r['description'])
            for other in self.entries.values():
                if key in other.get('concepts',[]): add(other['id'],'Title match','comparison','Comparable title in the consolidated catalog; identity is not asserted.')
        else:
            for ref in e.get('coreRefs',[]): add(ref,'Core reference','outgoing','Numbered reference in the consolidated source.')
            for ref in e.get('instrumentRefs',[]): add(ref,'Practice reference','outgoing','Instrument reference in the consolidated source.')
            for ref in self.incoming.get(key,[]): add(ref,'Cited by','incoming','This entry cites the selected model or instrument.')
            for theme in self.data['themes']:
                if theme['id'] in e.get('themes',[]):
                    for ref in theme['entries']: add(ref,'Shared thread','undirected',theme['name']+'; editorial navigation, not a causal assertion.')
            for ref in e.get('concepts',[]): add(ref,'Title match','comparison','Comparable title in the earlier ontology; identity is not asserted.')
        seen = set(); unique = []
        for link in links:
            signature = (link['id'],link['type'],link['direction'],link['evidence'])
            if signature not in seen: unique.append(link); seen.add(signature)
        return {'requested_id':record['requested_id'], 'canonical_id':key, 'links':unique,
                'canonical_references':[p for p in self.pointers.values() if p['canonicalId'] == key],
                'note':'Models connected by the same assumption do not provide independent confirmation.'}

    def routes(self, route_id=None):
        if not route_id:
            return [{'id':r['id'],'name':r['name'],'question':r['question'],'steps':len(r['steps'])} for r in self.data['routes']]
        route = next((r for r in self.data['routes'] if r['id'] == route_id), None)
        if not route: raise ValueError('Unknown decision path: '+route_id)
        return {**route, 'steps':[{**s,'entry_name':self.get(s['entry'])['entry']['name']} for s in route['steps']],
                'counter':{**route['counter'],'entry_name':self.get(route['counter']['entry'])['entry']['name']},
                'note':'Authored reading path, not a validated decision score.'}

    def stats(self):
        return {'counts':self.data['counts'], 'source':{k:v for k,v in self.data['source'].items() if k!='text'},
                'disciplines':[{'id':d['id'],'name':d['name'],'entries':len(d['entries']),'question':d['question']} for d in self.data['disciplines']],
                'meaning':'The 1,052-entry catalog includes 261 core models. Instruments (15) and the overlapping earlier ontology (258) are separate collections.'}

def export_asset(kind, output, force=False):
    source = ROOT / 'assets' / ('Business-Engineer-Atlas.html' if kind=='atlas' else 'business-analysis-template.html')
    target = Path(output).expanduser().resolve()
    if target.exists() and not force: raise ValueError('Output exists. Choose another path, or use --force for an intended replacement.')
    target.parent.mkdir(parents=True,exist_ok=True)
    shutil.copyfile(source,target)
    return {'file':str(target),'bytes':target.stat().st_size,'sha256':hashlib.sha256(target.read_bytes()).hexdigest()}

def parser():
    p=argparse.ArgumentParser(description=__doc__);sub=p.add_subparsers(dest='command',required=True)
    sub.add_parser('stats')
    search=sub.add_parser('search');search.add_argument('query',nargs='?',default='')
    search.add_argument('--collection',choices=['catalog','core','disciplines','instruments','concepts','all'],default='catalog')
    search.add_argument('--discipline');search.add_argument('--part',choices=['I','II','III','IV','V','VI','VII','VIII']);search.add_argument('--kind');search.add_argument('--limit',type=int,default=8);search.add_argument('--offset',type=int,default=0)
    get=sub.add_parser('get');get.add_argument('ids',nargs='+')
    links=sub.add_parser('links');links.add_argument('id')
    routes=sub.add_parser('routes');routes.add_argument('id',nargs='?')
    practice=sub.add_parser('practice');practice.add_argument('section',choices=['engine','modes','routing','quality','spine'])
    export=sub.add_parser('export');export.add_argument('kind',choices=['atlas','report-template']);export.add_argument('output');export.add_argument('--force',action='store_true')
    return p

def main():
    args=parser().parse_args()
    try:
        if args.command=='export': result=export_asset(args.kind,args.output,args.force)
        else:
            lib=Library()
            if args.command=='stats': result=lib.stats()
            elif args.command=='search': result=lib.search(args.query,args.collection,args.discipline,args.part,args.kind,args.limit,args.offset)
            elif args.command=='get': result=[lib.get(token) for token in args.ids]
            elif args.command=='links': result=lib.links(args.id)
            elif args.command=='routes': result=lib.routes(args.id)
            else: result=lib.data['spine'] if args.section=='spine' else lib.data['practice'][args.section]
        print(json.dumps(result,ensure_ascii=False,indent=2))
    except (ValueError,OSError) as error:
        print(json.dumps({'error':str(error)},ensure_ascii=False),file=sys.stderr)
        return 2
    return 0

if __name__=='__main__': sys.exit(main())
