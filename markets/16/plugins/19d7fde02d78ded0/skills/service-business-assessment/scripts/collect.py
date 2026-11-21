#!/usr/bin/env python3
"""Bounded public website collector. No submissions, credentials, or ad/SEO estimates."""
import argparse, csv, datetime, hashlib, ipaddress, json, re, socket, time
from pathlib import Path
from urllib.parse import urljoin, urlparse, urldefrag
from urllib.robotparser import RobotFileParser
import xml.etree.ElementTree as ET
import requests
from bs4 import BeautifulSoup
UA='OvertimePresenceAudit/1.0'

def public_url(url):
 p=urlparse(url)
 if p.scheme not in ('http','https') or not p.hostname or p.username or p.password or p.port not in (None,80,443):raise ValueError('Use a public http(s) website without credentials or custom ports.')
 for addr in socket.getaddrinfo(p.hostname,p.port or 443,type=socket.SOCK_STREAM):
  if not ipaddress.ip_address(addr[4][0]).is_global:raise ValueError('Non-public network destination is not allowed.')
 return url

def get(url):
 for _ in range(6):
  public_url(url)
  with requests.get(url,headers={'User-Agent':UA},timeout=(6,15),allow_redirects=False,stream=True) as r:
   if r.status_code in (301,302,303,307,308):url=urljoin(url,r.headers['location']);continue
   parts=[];size=0
   for chunk in r.iter_content(32768):
    size+=len(chunk)
    if size>2500000:raise ValueError('Response exceeded 2.5 MB collection limit.')
    parts.append(chunk)
   body=b''.join(parts)
   return r.status_code,url,dict(r.headers),body
 raise ValueError('Too many redirects.')

def extract(url,body,status,final_url):
 s=BeautifulSoup(body,'html.parser');title=s.title.get_text(' ',strip=True) if s.title else ''
 def meta(name):
  el=s.find('meta',attrs={'name':re.compile('^'+name+'$',re.I)});return el.get('content','') if el else None
 canonical=s.find('link',rel=lambda x:x and 'canonical' in x)
 links=sorted({urldefrag(urljoin(final_url,a.get('href','')))[0] for a in s.find_all('a',href=True)})
 scripts=' '.join(str(x) for x in s.find_all('script'));html=str(s)
 forms=[{'action':f.get('action'),'method':f.get('method','get'),'fields':[{'name':i.get('name'),'type':i.get('type',i.name),'required':i.has_attr('required')} for i in f.find_all(['input','select','textarea']) if i.get('type') not in ('hidden','submit')]} for f in s.find_all('form')]
 headings=[{'level':h.name,'text':h.get_text(' ',strip=True)} for h in s.find_all(re.compile('^h[1-3]$'))]
 ld=[]
 for v in s.find_all('script',type='application/ld+json'):
  try:ld.append(json.loads(v.string or v.get_text()))
  except (ValueError,TypeError):pass
 for e in s(['script','style','noscript']):e.decompose()
 text=s.get_text(' ',strip=True)
 return {'url':url,'final_url':final_url,'status':status,'title':title,'description':meta('description'),'robots':meta('robots'),'canonical':urljoin(final_url,canonical.get('href','')) if canonical else None,'headings':headings,'word_count':len(text.split()),'links':links,'tel_links':[x for x in links if x.startswith('tel:')],'email_links':[x for x in links if x.startswith('mailto:')],'static_forms':forms,'form_presence_scope':'HTML only; render before inferring absence','gtm_ids':sorted(set(re.findall(r'GTM-[A-Z0-9]+',scripts))),'ga4_ids':sorted(set(re.findall(r'\bG-[A-Z0-9]{6,}\b',scripts))),'google_ads_ids':sorted(set(re.findall(r'AW-\d+',scripts))),'platform':'Squarespace' if 'squarespace' in html.lower() else ('WordPress' if 'wp-content' in html else 'Unclassified'),'json_ld':ld,'text_excerpt':text[:12000],'image_count':len(s.find_all('img')),'empty_alt_count':sum(not x.get('alt','').strip() for x in s.find_all('img'))}

def collect(domain,out,max_pages=25):
 start='https://'+domain if '://' not in domain else domain
 public_url(start);out=Path(out);out.mkdir(parents=True,exist_ok=True);raw=out/'raw';raw.mkdir(exist_ok=True)
 observed=datetime.datetime.now(datetime.timezone.utc).isoformat();status,home,headers,body=get(start)
 base=urlparse(home).scheme+'://'+urlparse(home).netloc;host=urlparse(home).hostname.removeprefix('www.')
 same=lambda u: urlparse(u).hostname and urlparse(u).hostname.removeprefix('www.')==host
 robots=RobotFileParser();robot_status=None;robot_body='';errors=[]
 try:
  robot_status,ru,rh,rb=get(base+'/robots.txt');robot_body=rb.decode('utf-8','replace')
  if robot_status==200:robots.parse(robot_body.splitlines())
  elif robot_status==404:robots.parse([])
  else:robots.parse(['User-agent: *','Disallow: /'])
 except Exception as e:robots.parse(['User-agent: *','Disallow: /']);errors.append({'url':base+'/robots.txt','error':str(e)})
 (raw/'robots.txt').write_text(robot_body)
 sitemap_locs=[];maps=re.findall(r'(?im)^sitemap:\s*(\S+)',robot_body) or [base+'/sitemap.xml'];seen_maps=set()
 while maps and len(seen_maps)<10:
  u=maps.pop(0)
  if u in seen_maps or not same(u):continue
  seen_maps.add(u)
  try:
   st,fu,he,bb=get(u)
   if st!=200:continue
   root=ET.fromstring(bb);locs=[x.text.strip() for x in root.iter() if x.tag.endswith('}loc') or x.tag=='loc' if x.text]
   (raw/('sitemap-'+str(len(seen_maps))+'.xml')).write_bytes(bb)
   if root.tag.endswith('sitemapindex'):maps.extend(locs)
   else:sitemap_locs.extend(x for x in locs if same(x))
  except Exception as e:errors.append({'url':u,'error':str(e)})
 sitemap_locs=sorted(set(sitemap_locs))[:1000]
 pages=[];seen=set();queue=[home]+sitemap_locs;skipped=[]
 while queue and len(pages)<max_pages:
  u=queue.pop(0).split('#')[0]
  if u in seen or not same(u):continue
  if urlparse(u).query or re.search(r'\.(pdf|png|jpg|jpeg|gif|zip|xml|webp|svg|mp4)$',urlparse(u).path,re.I):continue
  seen.add(u)
  if not robots.can_fetch(UA,u):skipped.append({'url':u,'reason':'robots restriction or unavailable robots policy'});continue
  try:
   if u==home:st,fu,he,bb=status,home,headers,body
   else:st,fu,he,bb=get(u);time.sleep(.15)
   if 'html' not in he.get('Content-Type',he.get('content-type','')):continue
   if not same(fu):skipped.append({'url':u,'reason':'Redirected outside selected business domain'});continue
   page=extract(u,bb,st,fu);key=hashlib.sha256(u.encode()).hexdigest()[:16];page['raw_file']='raw/'+key+'.html';(raw/(key+'.html')).write_bytes(bb);pages.append(page)
   for link in page['links']:
    if same(link) and link not in seen:queue.append(link)
  except Exception as e:errors.append({'url':u,'error':str(e)})
 canonical={p['canonical'] or p['final_url'] for p in pages if p['status']==200}
 result={'schema_version':'1.0','domain':host,'observed_at':observed,'scope':{'max_pages':max_pages,'method':'HTTP HTML + robots + sitemap; no rendered browser or form submission','sitemap_urls':len(sitemap_locs),'sitemap_url_list':sitemap_locs,'pages_crawled':len(pages),'unique_canonical_pages_observed':len(canonical),'truncated':bool(queue),'robots_status':robot_status},'business_discovery':{'home_title':pages[0]['title'] if pages else None,'candidate_services':[h['text'] for p in pages[:1] for h in p['headings'] if h['level'] in ('h2','h3')],'region_requires_review':True,'competitor_search_templates':['{core service} {city} installation','{secondary service} {city} company']},'pages':pages,'errors':errors,'skipped':skipped}
 (out/'crawl.json').write_text(json.dumps(result,indent=2))
 with (out/'pages.csv').open('w') as f:
  w=csv.DictWriter(f,fieldnames=['url','status','title','description','canonical','word_count','platform']);w.writeheader();w.writerows({k:p.get(k) for k in w.fieldnames} for p in pages)
 print(json.dumps({'domain':host,'output':str(out/'crawl.json'),'pages':len(pages),'sitemap_urls':len(sitemap_locs),'errors':len(errors),'skipped':len(skipped)}))
 return result

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('domain');ap.add_argument('--out',required=True);ap.add_argument('--max-pages',type=int,default=25);a=ap.parse_args()
 if not 1<=a.max_pages<=100:ap.error('--max-pages must be between 1 and 100')
 collect(a.domain,a.out,a.max_pages)
