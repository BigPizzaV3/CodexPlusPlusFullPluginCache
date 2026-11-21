#!/usr/bin/env python3
import argparse,json
from pathlib import Path
def render(r):
 src={s['id']:s for s in r['sources']}
 def refs(ids):return ' · '.join('['+src[i]['title']+']('+src[i]['url']+')' for i in ids)
 out=[f"# {r['title']}: digital presence assessment",f"As of {r['assessment_date']} · {r['status']}",r['summary'],'## Businesses compared']
 for e in r['entities']:
  m=e['organic_traffic'];v='Unknown: '+m.get('reason','') if m['value'] is None else str(m['value'])+' estimated organic visits / month'
  out.extend([f"### {e['name']}",e['selection_reason'],f"Region: {e['region']}. Sitemap URLs: {e['sitemap_urls']}; HTML-like candidates: {e['html_candidates']}; pages fetched: {e['crawled_pages']}. {v}",refs(e['source_ids'])])
  if m.get('source_ids'):out.append(refs(m['source_ids']))
 if any(e.get('organic_keywords') for e in r['entities']):
  out.extend(['## Search visibility data',r['methodology'].get('seo','')])
  def table(headers,rows):
   def cell(x):return ('Unknown' if x is None else str(x)).replace('|','\\|').replace('\n',' ')
   return '\n'.join(['| '+' | '.join(headers)+' |','| '+' | '.join(['---']*len(headers))+' |']+['| '+' | '.join(cell(x) for x in row)+' |' for row in rows])
  for e in r['entities']:
   out.append('### '+e['name'])
   if e.get('seo_profile'):out.extend(['Backlink measures are global; search estimates use the stated country.','```json',json.dumps(e['seo_profile'],indent=2),'```'])
   top=e.get('top_pages',{});keys=e.get('organic_keywords',{})
   out.extend(['#### Top pages',top.get('reason','')])
   if top.get('rows'):out.append(table(['Page','Estimated monthly visits','Keywords','Top keyword','Monthly volume (country scope)','Position'],[[p['url'],p['estimated_organic_traffic'],p.get('keywords'),p.get('top_keyword'),p.get('volume'),p.get('position')] for p in top['rows']]))
   else:out.append('No pages detected.' if top.get('status')=='observed' else 'Not yet verified.')
   if top.get('source_ids'):out.append(refs(top['source_ids']))
   out.extend(['#### Organic keywords',keys.get('coverage','')])
   if keys.get('rows'):out.append(table(['Keyword','Monthly volume (country scope)','Difficulty','CPC USD','Estimated visits','Position','Page','Last SERP update'],[[k['keyword'],k['volume'],k.get('difficulty'),k.get('cpc_usd'),k.get('estimated_organic_traffic'),k.get('position'),k.get('url'),k.get('last_serp_update')] for k in keys['rows']]))
   else:out.append('No keywords detected.' if keys.get('status')=='observed' else 'Not yet verified.')
   if keys.get('source_ids'):out.append(refs(keys['source_ids']))
  if r.get('keyword_opportunities'):
   out.append('### Search opportunities')
   for k in r['keyword_opportunities']:out.extend([f"- {k['keyword']}: {k['volume']} estimated US searches / month. {k['opportunity']}",refs(k['source_ids'])])
 for section in ['website','seo','ads','email']:
  out.append('## '+section.upper() if section=='seo' else '## '+section.capitalize())
  for f in r['findings']:
   if f['section']==section:out.extend([f"### {f['title']} [{f['status']}]",f['observation'],f['recommendation'],refs(f['source_ids'])])
  if section=='ads':
   for a in r['ads']:out.extend([f"### {a['entity_id']} / {a['platform']} [{a['status']}]",a['summary'],a['scope'],refs(a['source_ids'])])
 out.append('## Observed page inventory')
 for p in r['pages']:out.append(f"- {p['entity_id']}: [{p['title'] or p['url']}]({p['url']}) — {p['type']}; HTTP {p['http_status']}; canonical {p['canonical']}; observed {p['observed_at']}. {refs(p['source_ids'])}")
 out.append('## Content opportunities')
 for g in r.get('seo_opportunities',[]):out.extend(['### '+g['theme'],g['current'],g['competitor'],g['proposed'],refs(g['source_ids'])])
 if r.get('performance'):out.extend(['## Performance measurements','```json',json.dumps(r['performance'],indent=2),'```'])
 if r.get('social'):out.extend(['## Social sample',r['social']['scope'],'```json',json.dumps(r['social']['rows'],indent=2),'```'])
 out.append('## Focus areas and opportunities')
 for o in r['opportunities']:out.extend(['### '+o['title'],o['work'],'Signal to watch: '+o['done'],refs(o['source_ids'])])
 out.extend(['## Opportunity model',r['model']['label'],r['model']['formula'],r['model']['limitations'],'```json',json.dumps(r['model'],indent=2),'```','## Data still needed',*['- '+x for x in r['data_needed']],'## Method',*r['methodology'].values(),'## Source register'])
 for s in r['sources']:out.append(f"- [{s['title']}]({s['url']}) ({s['id']}; {s['observed_date']}): {s['note']}")
 return '\n\n'.join(out)+'\n'
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('report');ap.add_argument('--out',required=True);a=ap.parse_args();Path(a.out).write_text(render(json.loads(Path(a.report).read_text())))
