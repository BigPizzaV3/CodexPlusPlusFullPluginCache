#!/usr/bin/env python3
import argparse,json
from pathlib import Path
from validate_report import validate
def merge(r,x,entity_id,source_url):
 e=next((e for e in r['entities'] if e['id']==entity_id),None)
 if e is None or e['domain'].removeprefix('www.')!=x['domain'].removeprefix('www.'):raise ValueError('Entity/domain mismatch')
 prior=r.get('seo_exports',[])
 # Comparison must have a common date/country/scope. Do not silently mix slices.
 if any((p['country'],p['as_of'],p['scope'])!=(x['country'],x['as_of'],x['scope']) for p in prior):raise ValueError('SEO exports differ in country, date or scope; build a separate comparison snapshot.')
 sid='ahrefs-'+entity_id+'-'+x['kind']+'-'+x['sha256'][:8]
 if any(s['id']==sid for s in r['sources']):return r
 r['sources'].append(dict(id=sid,title=f"Ahrefs {x['kind']}: {e['name']}",url=source_url,observed_date=x['as_of'],note=f"User-supplied export; {x['country']}; {x['scope']}; {x['coverage']} File digest {x['sha256']}. Private export retained locally."))
 if x['kind']=='overview':
  value=x['rows'][0]['estimated_organic_traffic'];e['organic_traffic']=dict(status='unknown' if value is None else 'estimated',value=value,unit='estimated monthly organic visits',reason='Provider estimate; not measured sessions.' if value is not None else 'Provider did not report a value.',source_ids=[sid],country=x['country'],as_of=x['as_of'],scope=x['scope'])
 elif x['kind']=='top-pages':
  ranked=sorted([p for p in x['rows'] if p['estimated_organic_traffic'] is not None],key=lambda p:p['estimated_organic_traffic'],reverse=True)
  e['top_pages']=dict(status='estimated' if ranked else 'unknown',rows=[dict(**p,source_ids=[sid]) for p in ranked],reason=x['coverage'],source_ids=[sid])
 else:e['organic_keywords']=dict(rows=x['rows'],source_ids=[sid],coverage=x['coverage'])
 r.setdefault('seo_exports',[]).append(dict(entity_id=entity_id,source_ids=[sid],**{k:x[k] for k in ['kind','country','as_of','scope','sha256','row_count','coverage']}))
 errors=validate(r)
 if errors:raise ValueError('\n'.join(errors))
 return r
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('report');ap.add_argument('normalized');ap.add_argument('--entity',required=True);ap.add_argument('--source-url',required=True);ap.add_argument('--out',required=True);a=ap.parse_args();r=merge(json.loads(Path(a.report).read_text()),json.loads(Path(a.normalized).read_text()),a.entity,a.source_url);Path(a.out).write_text(json.dumps(r,indent=2)+'\n');print('Merged. Review stale unknown findings and refresh the brief/web view before publication.')
