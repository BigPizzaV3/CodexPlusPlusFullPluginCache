#!/usr/bin/env python3
import argparse,json
from pathlib import Path
from urllib.parse import urlparse
from jsonschema import Draft202012Validator,FormatChecker
SCHEMA=Path(__file__).resolve().parents[1]/'references/report.schema.json'
def validate(r):
 errors=[f'{list(e.path)}: {e.message}' for e in Draft202012Validator(json.loads(SCHEMA.read_text()),format_checker=FormatChecker()).iter_errors(r)]
 sources={x['id'] for x in r.get('sources',[])};entities={x['id'] for x in r.get('entities',[])}
 for key in ['sources','entities','findings','opportunities']:
  ids=[x['id'] for x in r.get(key,[])];
  if len(ids)!=len(set(ids)):errors.append('Duplicate IDs in '+key)
 def walk(v,path='report'):
  if isinstance(v,dict):
   for k,x in v.items():
    if k=='source_ids' and isinstance(x,list):
     for i in x:
      if i not in sources:errors.append(path+': missing source '+str(i))
    if k=='source_id' and x not in sources:errors.append(path+': missing source '+str(x))
    if k=='entity_id' and x not in entities:errors.append(path+': unknown entity '+str(x))
    walk(x,path+'.'+k)
  elif isinstance(v,list):
   for i,x in enumerate(v):walk(x,path+f'[{i}]')
 walk(r)
 for e in r.get('entities',[]):
  metric=e.get('organic_traffic',{})
  if metric.get('status')=='unknown' and metric.get('value') is not None:errors.append(e['id']+': unknown traffic must be null')
  if metric.get('status')!='unknown' and (metric.get('value') is None or not metric.get('source_ids')):errors.append(e['id']+': measured/estimated traffic needs a value and sources')
  if e.get('top_pages',{}).get('status')=='unknown' and e['top_pages'].get('rows'):errors.append(e['id']+': unknown top pages must have no ranked rows')
 for a in r.get('ads',[]):
  if a.get('status') in ['ambiguous','unknown','blocked'] and a.get('returned_count') is not None:errors.append('Unverified ad identity/availability cannot carry a business count')
  if a.get('status')=='no_matches' and a.get('returned_count')!=0:errors.append('No matches must record scoped zero')
  if a.get('status')!='unknown' and not a.get('source_ids'):errors.append('Ad observation requires a source')
 for f in r.get('findings',[]):
  if f.get('status') in ['pass','gap','partial'] and not f.get('source_ids'):errors.append(f['id']+': substantive check requires evidence')
 for s in r.get('sources',[]):
  if urlparse(s['url']).scheme not in ['https','http']:errors.append(s['id']+': published source must use http(s)')
 if r.get('email_test',{}).get('status')=='not_tested':
  for k in ['submission_at','customer_received_at','owner_received_at','conversion_event_count']:
   if r['email_test'].get(k) is not None:errors.append('Untested email cannot have '+k)
 for p in r.get('brief',{}).get('pages',[]):
  for b in p.get('blocks',[]):
   if b.get('type')=='finding' and b.get('finding_id') not in {f['id'] for f in r.get('findings',[])}:errors.append('Unknown brief finding '+str(b.get('finding_id')))
 return errors
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('report');a=ap.parse_args();r=json.loads(Path(a.report).read_text());errors=validate(r)
 if errors:print('\n'.join(errors));raise SystemExit(1)
 print(f"Valid {r['id']}: {len(r['entities'])} entities, {len(r['findings'])} findings, {len(r['sources'])} sources")
