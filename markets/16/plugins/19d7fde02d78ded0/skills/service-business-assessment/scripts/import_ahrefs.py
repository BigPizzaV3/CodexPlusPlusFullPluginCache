#!/usr/bin/env python3
"""Normalize Ahrefs CSV/TSV exports without inventing missing metrics."""
import argparse,csv,datetime,hashlib,io,json,re
from pathlib import Path
from urllib.parse import urlparse
def number(value):
 s=str('' if value is None else value).strip().replace(',','').replace('\u00a0','')
 if s.lower() in ('','-','—','n/a','na','null','not available'):return None
 m=re.fullmatch(r'(\d+(?:\.\d+)?)\s*([kKmMbB]?)',s)
 if not m:raise ValueError('Unsupported numeric value: '+s)
 return float(m[1])*{'':1,'k':1000,'m':1000000,'b':1000000000}[m[2].lower()]
def read_csv(path):
 raw=Path(path).read_bytes();enc='utf-16' if raw.startswith((b'\xff\xfe',b'\xfe\xff')) else 'utf-8-sig';s=raw.decode(enc)
 try:dialect=csv.Sniffer().sniff(s[:10000],delimiters=',\t;')
 except csv.Error:dialect=csv.excel
 rows=list(csv.DictReader(io.StringIO(s),dialect=dialect))
 return [{re.sub(r'\s+',' ',str(k).strip().lower()):v for k,v in row.items() if k is not None} for row in rows],hashlib.sha256(raw).hexdigest()
def normalize(path,kind,domain,country,as_of,scope):
 datetime.date.fromisoformat(as_of);rows,digest=read_csv(path)
 if not rows:raise ValueError('Empty export: keep the measurement unknown; do not infer zero.')
 def pick(r,names,required=False):
  for name in names:
   if name in r:return r[name]
  if required:raise ValueError('Missing expected column; accepted headers: '+', '.join(names))
  return None
 out=[]
 for row in rows:
  traffic=number(pick(row,['organic traffic','current organic traffic','traffic'],kind!='keywords'))
  u=pick(row,['url','page url','top page','current url'],kind=='top-pages')
  host=(urlparse(u).hostname or '').removeprefix('www.') if u else ''
  expected=domain.removeprefix('www.')
  if u and (urlparse(u).scheme not in ['https','http'] or not (host==expected or (scope=='subdomains' and host.endswith('.'+expected)))):raise ValueError('Page URL does not match the selected domain: '+u)
  if kind=='overview':
   rd=pick(row,['domain','target']);
   if rd and rd.replace('https://','').replace('http://','').removeprefix('www.').strip('/')!=domain.removeprefix('www.').strip('/'):raise ValueError('Overview domain mismatch')
  normalized=dict(url=u,estimated_organic_traffic=traffic)
  if kind=='keywords':normalized.update(keyword=pick(row,['keyword'],True),position=number(pick(row,['current position','position'])),volume=number(pick(row,['volume','search volume'])))
  out.append(normalized)
 if kind=='overview' and len(out)!=1:raise ValueError('Overview must contain one current domain observation; filter time-series exports first.')
 return dict(provider='Ahrefs',measurement_kind='provider_estimate',kind=kind,domain=domain,country=country.upper(),as_of=as_of,scope=scope,sha256=digest,row_count=len(out),coverage='Exported rows only; export limits or filters may truncate coverage.',rows=out)
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('csv');ap.add_argument('--kind',choices=['overview','top-pages','keywords'],required=True);ap.add_argument('--domain',required=True);ap.add_argument('--country',required=True);ap.add_argument('--as-of',required=True);ap.add_argument('--scope',choices=['domain','subdomains','exact','prefix'],required=True);ap.add_argument('--out',required=True);a=ap.parse_args()
 out=normalize(a.csv,a.kind,a.domain,a.country,a.as_of,a.scope);Path(a.out).write_text(json.dumps(out,indent=2)+'\n');print('Normalized',len(out['rows']),'rows; review before merging.')
