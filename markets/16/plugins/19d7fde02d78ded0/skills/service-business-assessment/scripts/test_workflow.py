#!/usr/bin/env python3
import copy,json,tempfile,unittest
from pathlib import Path
from unittest.mock import patch
from collect import extract,public_url
from import_ahrefs import number,normalize
from validate_report import validate
from merge_ahrefs import merge
from export_markdown import render as markdown
def fixture():
 source=dict(id='s1',title='Fixture evidence',url='https://example.com',note='Test fixture only',observed_date='2026-09-09')
 es=[dict(id=str(i),name='Example '+str(i),domain=('example.com' if i==0 else f'peer{i}.example.com'),region='Example city',selection_reason='Fixture overlap',source_ids=['s1'],sitemap_urls=1,html_candidates=1,crawled_pages=1,crawl_limited=False,organic_traffic=dict(status='unknown',value=None,unit='estimated monthly organic visits',reason='No export',source_ids=[]),top_pages=dict(status='unknown',rows=[],reason='No export')) for i in range(4)]
 return dict(schema_version='1.0',id='example',title='Example',assessment_date='2026-09-09',version=1,business=dict(name='Example',domain='example.com',region='Example city',services=['Example service'],source_ids=['s1']),summary='Test fixture',status='draft',entities=es,findings=[],pages=[],ads=[],opportunities=[],sources=[source],email_test=dict(status='not_tested',reason='No test',submission_at=None),model=dict(label='Assumptions',additional_visits=100,inquiry_rate=.03,qualified_rate=.6,close_rate=.25,job_value=10000,currency='USD',formula='v*i*q*c*j',limitations='Not a forecast'),methodology=dict(score='No composite'),data_needed=['Export'])
class Tests(unittest.TestCase):
 def test_markdown_retains_partial_keyword_data(self):
  r=fixture();r['entities'][0]['organic_keywords']=dict(rows=[dict(keyword='example service',volume=10,position=2,url='https://example.com',estimated_organic_traffic=0)],source_ids=['s1'],coverage='Partial fixture')
  result=markdown(r);self.assertIn('example service',result);self.assertIn('Unknown',result);self.assertIn('Partial fixture',result);self.assertNotIn('## Workplan',result)
 def test_markdown_distinguishes_observed_empty(self):
  r=fixture();e=r['entities'][0];e['organic_keywords']=dict(status='observed',rows=[],source_ids=['s1']);e['top_pages']=dict(status='observed',rows=[],source_ids=['s1'])
  result=markdown(r);self.assertIn('No keywords detected.',result);self.assertIn('No pages detected.',result)
 def test_unknown_is_not_zero(self):
  r=fixture();self.assertEqual(validate(r),[]);r['entities'][0]['organic_traffic']['value']=0;self.assertTrue(any('unknown traffic' in e for e in validate(r)))
 def test_numeric_zero_and_missing(self):
  self.assertEqual(number('0'),0);self.assertEqual(number(0),0);self.assertIsNone(number('—'));self.assertEqual(number('1.2K'),1200)
  with self.assertRaises(ValueError):number('<10')
 def test_private_network_rejected(self):
  with self.assertRaises(ValueError):public_url('http://127.0.0.1/')
  with self.assertRaises(ValueError):public_url('file:///etc/passwd')
 def test_rendered_form_cannot_be_inferred_absent(self):
  p=extract('https://example.com',b'<html><title>Test</title><script src="forms.js"></script><div id="form"></div></html>',200,'https://example.com')
  self.assertEqual(p['static_forms'],[]);self.assertIn('render before inferring absence',p['form_presence_scope'])
 def test_ambiguous_ad_count_rejected(self):
  r=fixture();r['ads']=[dict(entity_id='0',platform='Meta',status='ambiguous',returned_count=49,scope='keyword',summary='Mixed publishers',source_ids=['s1'],observed_date='2026-09-09')];self.assertTrue(any('Unverified ad' in e for e in validate(r)))
 def test_missing_source_rejected(self):
  r=fixture();r['entities'][0]['source_ids']=['missing'];self.assertTrue(any('missing source' in e for e in validate(r)))
 def test_untested_email_rejects_fake_receipt(self):
  r=fixture();r['email_test']['customer_received_at']='2026-09-09T12:00:00Z';self.assertTrue(any('Untested email' in e for e in validate(r)))
 def test_utf16_export_and_domain_boundary(self):
  with tempfile.TemporaryDirectory() as tmp:
   p=Path(tmp)/'pages.csv';p.write_text('URL\tOrganic traffic\nhttps://example.com/service\t0\n',encoding='utf-16');x=normalize(p,'top-pages','example.com','US','2026-09-09','domain');self.assertEqual(x['rows'][0]['estimated_organic_traffic'],0)
   p.write_text('URL,Organic traffic\nhttps://badexample.com/service,100\n');
   with self.assertRaises(ValueError):normalize(p,'top-pages','example.com','US','2026-09-09','domain')
 def test_top_pages_are_not_domain_total(self):
  r=fixture();x=dict(kind='top-pages',domain='example.com',country='US',as_of='2026-09-09',scope='domain',sha256='abcdef1234567890',row_count=1,coverage='Exported rows only',rows=[dict(url='https://example.com/service',estimated_organic_traffic=10)])
  r=merge(r,x,'0','https://app.ahrefs.com/');self.assertIsNone(r['entities'][0]['organic_traffic']['value']);self.assertEqual(r['entities'][0]['top_pages']['rows'][0]['estimated_organic_traffic'],10)
  x=copy.deepcopy(x);x['as_of']='2026-09-08';x['sha256']='other'
  with self.assertRaises(ValueError):merge(r,x,'0','https://app.ahrefs.com/')
 def test_empty_export_is_not_zero(self):
  with tempfile.TemporaryDirectory() as tmp:
   p=Path(tmp)/'empty.csv';p.write_text('Domain,Organic traffic\n')
   with self.assertRaises(ValueError):normalize(p,'overview','example.com','US','2026-09-09','domain')
if __name__=='__main__':unittest.main()
