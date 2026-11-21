#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Preflight local de PDF: metadados objetivos, texto-âncora e páginas com provável imagem.
Não comprova auditoria jurídica, não lê imagens semanticamente e não roda no ChatGPT por presunção.
Requer PyMuPDF/fitz instalado no ambiente executor. Não publica conteúdo privado no resultado.
"""
import argparse, hashlib, json, pathlib, sys

def inspect_pdf(pdf_path,fixture_path=None):
 try: import fitz
 except ImportError as e:raise RuntimeError('PyMuPDF indisponível no ambiente; não simular execução') from e
 p=pathlib.Path(pdf_path)
 if not p.is_file():raise RuntimeError('PDF não encontrado')
 digest_hash=hashlib.sha256()
 with p.open('rb') as source:
  for block in iter(lambda:source.read(1024*1024),b''):
   digest_hash.update(block)
 digest=digest_hash.hexdigest()
 try:doc=fitz.open(p)
 except Exception as e:raise RuntimeError('PDF inacessível/corrompido') from e
 n=len(doc)
 if n<1:raise RuntimeError('PDF sem páginas')
 mid=max(1,n//2)
 samples=[]
 for pn in sorted(set((1,mid,n))):
  page=doc[pn-1]; s=page.get_text()
  samples.append({'page':pn,'text_chars':len(s),'embedded_images_count':len(page.get_images()),
                  'sample_accessed_by':'PyMuPDF.get_text metadata only'})
 result={'source_sha256':digest,'pdf_pages_observed':n,'page_count_provenance':'PyMuPDF document metadata from supplied exact file',
   'sample_first_middle_last_pages':samples,'source_file_name':p.name,
   'semantic_document_review':False,'visual_review':False,'fixture_applied':False,'anchor_checks':[]}
 if fixture_path:
  fixture=json.loads(pathlib.Path(fixture_path).read_text(encoding='utf-8'))
  if digest!=fixture.get('pdf_sha256_exact'):
   result['fixture_status']='NOT_APPLICABLE_SOURCE_HASH_MISMATCH'
  else:
   result['fixture_applied']=True
   if n!=fixture['pdf_pages']:raise RuntimeError('Contagem física diverge do fixture da mesma fonte')
   for a in fixture['anchors']:
    pn=a['page']; t=doc[pn-1].get_text(); needle=a.get('needle')
    if a['kind']=='text':
     is_found=needle.casefold() in t.casefold()
     result['anchor_checks'].append({'page':pn,'kind':'text','text_anchor_found':is_found,'result':'PASS' if is_found else 'FAIL'})
    else:
     result['anchor_checks'].append({'page':pn,'kind':'image_requires_visual','result':'PENDING_VISUAL_INSPECTION'})
   result['fixture_status']='ANCHOR_TEXT_MISMATCH' if any(c['result']=='FAIL' for c in result['anchor_checks']) else 'TEXT_ANCHORS_PRESENT_VISUAL_PENDING'
 return result

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--autos',required=True);ap.add_argument('--fixture');ap.add_argument('--saida')
 a=ap.parse_args();report=inspect_pdf(a.autos,a.fixture)
 rendered=json.dumps(report,ensure_ascii=False,indent=2)
 if a.saida:pathlib.Path(a.saida).write_text(rendered,encoding='utf-8')
 print(rendered)
 return 2 if report.get('fixture_status')=='ANCHOR_TEXT_MISMATCH' else 0
if __name__=='__main__':sys.exit(main())
