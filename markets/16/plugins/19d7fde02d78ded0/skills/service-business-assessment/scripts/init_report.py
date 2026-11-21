#!/usr/bin/env python3
"""Initialize reviewed entities from crawls. Judgment and rendered/account checks stay explicit."""
import argparse,datetime,json,re
from pathlib import Path
from validate_report import validate
def initialize(config):
 date=datetime.date.today().isoformat();entities=[];pages=[];sources=[]
 for e in config['entities']:
  c=json.loads(Path(e['crawl']).read_text());s=c['scope'];sid='crawl-'+e['id'];sources.append(dict(id=sid,title=e['name']+' bounded public crawl',url='https://'+e['domain'],observed_date=c['observed_at'][:10],note=s['method']+'; max pages '+str(s['max_pages'])))
  entities.append(dict(**{k:e[k] for k in ['id','name','domain','region','selection_reason']},source_ids=[sid],sitemap_urls=s['sitemap_urls'],html_candidates=sum(not re.search(r'\.(pdf|jpg|png|xml)$',u,re.I) for u in s['sitemap_url_list']),crawled_pages=s['pages_crawled'],crawl_limited=s['truncated'],organic_traffic=dict(status='unknown',value=None,unit='estimated monthly organic visits',reason='No account/export measurement supplied.',source_ids=[]),top_pages=dict(status='unknown',rows=[],reason='No page-performance export supplied.')))
  seen=set()
  for p in c['pages']:
   canonical=(p['canonical'] or p['final_url']).rstrip('/')
   if canonical in seen:continue
   seen.add(canonical);pages.append(dict(entity_id=e['id'],url=p['url'],canonical=canonical,title=p['title'],description=p['description'],http_status=p['status'],type='unreviewed',tel_links=len(p['tel_links']),platform=p['platform'],source_ids=[sid],observed_at=c['observed_at']))
 subject=entities[0];r=dict(schema_version='1.0',id=config['id'],title=subject['name'],assessment_date=date,version=1,business=dict(name=subject['name'],domain=subject['domain'],region=subject['region'],services=config['services'],source_ids=subject['source_ids']),summary='Draft: review the evidence and write a business-specific recommendation before delivery.',status='draft',entities=entities,findings=[],pages=pages,ads=[],seo_opportunities=[],opportunities=[],sources=sources,email_test=dict(status='not_tested',reason='No controlled inquiry performed.',submission_at=None,customer_received_at=None,owner_received_at=None,conversion_event_count=None),model=dict(label='Illustrative assumptions; replace before interpreting',additional_visits=100,inquiry_rate=.03,qualified_rate=.6,close_rate=.25,job_value=1000,currency='USD',formula='additional_visits × inquiry_rate × qualified_rate × close_rate × job_value',limitations='Not a forecast; booked revenue before acquisition and delivery costs.'),methodology=dict(crawl='Bounded public HTML crawl; no form submission. Sitemap is not indexed pages.',score_policy='No composite grade; unknown is not a failed check.'),data_needed=['Comparable SEO exports','Rendered conversion-path review','Authorized inbox test','Owner traffic, advertising and job-economics data'])
 errors=validate(r)
 if errors:raise ValueError('\n'.join(errors))
 return r
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('config',help='JSON with id, services and entities. First entity is subject; 3–5 peers follow. Each has id,name,domain,region,selection_reason,crawl.');ap.add_argument('--out',required=True);a=ap.parse_args();Path(a.out).write_text(json.dumps(initialize(json.loads(Path(a.config).read_text())),indent=2)+'\n');print('Draft initialized. Review and add evidence before delivery.')
