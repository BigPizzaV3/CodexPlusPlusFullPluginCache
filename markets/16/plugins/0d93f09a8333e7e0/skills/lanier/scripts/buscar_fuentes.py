#!/usr/bin/env python3
"""Consulta de solo lectura del corpus de Lanier, sin red ni dependencias externas."""
import argparse,json,re,unicodedata
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]/'references'
def norm(s):
 return ''.join(c for c in unicodedata.normalize('NFD',s.lower()) if unicodedata.category(c)!='Mn')
def main():
 p=argparse.ArgumentParser(description=__doc__)
 p.add_argument('--query');p.add_argument('--doc');p.add_argument('--page',type=int);p.add_argument('--limit',type=int,default=5)
 a=p.parse_args();catalog=json.loads((ROOT/'catalog.json').read_text())
 if a.doc and a.doc not in {x['id'] for x in catalog}:p.error('ID desconocido; consultar references/catalog.json')
 if a.page is not None and (not a.doc or a.page<1):p.error('--page requiere --doc y un número positivo')
 if not a.query and a.page is None:p.error('Indicar --query o --doc y --page')
 if not 1<=a.limit<=20:p.error('--limit debe estar entre 1 y 20')
 terms=re.findall(r'\w+',norm(a.query or ''));hits=[]
 for d in catalog:
  if a.doc and a.doc!=d['id']:continue
  pages=(ROOT/d['text']).read_text().split('\f')
  if a.page is not None:
   if a.page>len(pages):p.error('Página fuera del documento')
   print(json.dumps({'doc':d['id'],'title':d['title'],'pdf_page':a.page,'pdf':str(ROOT/d['pdf']),'text':pages[a.page-1]},ensure_ascii=False,indent=2));return
  for n,page in enumerate(pages,1):
   s=norm(page);counts=[s.count(t) for t in terms]
   if not terms or not all(counts):continue
   start=max(0,min(s.find(t) for t in terms)-180)
   hits.append({'doc':d['id'],'title':d['title'],'pdf_page':n,'score':sum(counts),'excerpt':page[start:start+1800]})
 hits.sort(key=lambda x:(-x['score'],x['doc'],x['pdf_page']))
 print(json.dumps({'matches':len(hits),'results':hits[:a.limit],'note':'Leer la página completa antes de citar; numeración física del PDF.'},ensure_ascii=False,indent=2))
if __name__=='__main__':main()
