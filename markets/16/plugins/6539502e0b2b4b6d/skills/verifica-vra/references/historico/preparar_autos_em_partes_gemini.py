#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Prepara PDF integral em partes menores, com rastreio das páginas originais.

Dependência local: PyMuPDF (`pip install pymupdf`, se autorizado).
Não pressupõe capacidade de executar scripts no Gemini e NÃO audita mérito.
Não exclui movimentos posteriores; corte temporal é aplicado após ler a VRA.
Não comunica arquivos a serviços externos.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import pathlib
import sys
from datetime import datetime, timezone


def sha256(path):
    h=hashlib.sha256()
    with open(path,'rb') as f:
        for chunk in iter(lambda:f.read(1024*1024),b''):
            h.update(chunk)
    return h.hexdigest()


def split_corpus(autos_path,output_dir,vra_path=None,pages_per_part=30,batch_size=5):
    try:
        import fitz
    except ImportError as err:
        raise RuntimeError('PyMuPDF não instalado; NÃO declarar corpus preparado.') from err
    original=pathlib.Path(autos_path).resolve()
    if not original.is_file(): raise ValueError('Autos PDF não localizado')
    if not 5<=pages_per_part<=100: raise ValueError('pages_per_part deve estar entre 5 e 100')
    if not 1<=batch_size<=10: raise ValueError('batch_size deve estar entre 1 e 10')
    out=pathlib.Path(output_dir).resolve()
    if out==original.parent: raise ValueError('Saída em pasta separada dos autos originais')
    out.mkdir(parents=True,exist_ok=True)
    with fitz.open(original) as doc:
        if doc.needs_pass: raise RuntimeError('Autos protegidos por senha; não contornar proteção')
        total=len(doc)
        if total<=0:raise RuntimeError('Documento sem páginas')
        parts=[]
        for start in range(0,total,pages_per_part):
            end=min(start+pages_per_part,total)
            name=f'AUTOS_PARTE_{len(parts)+1:03d}_P{start+1:04d}-{end:04d}.pdf'
            path=out/name
            if path.exists():raise FileExistsError(f'Arquivo já existe: {path}; usar nova pasta, sem sobrescrever')
            with fitz.open() as part:
                part.insert_pdf(doc,from_page=start,to_page=end-1,annots=True,links=True)
                part.save(str(path),garbage=4,deflate=True)
            with fitz.open(path) as verify:
                if len(verify)!=end-start:raise RuntimeError('Segmento ficou com contagem inesperada de páginas')
                # O conteúdo textualmente extraível da primeira/última página deve ser idêntico ao original.
                for local,source in [(0,start),(len(verify)-1,end-1)]:
                    src=hashlib.sha256(doc[source].get_text().encode('utf-8')).hexdigest()
                    got=hashlib.sha256(verify[local].get_text().encode('utf-8')).hexdigest()
                    if src!=got:raise RuntimeError(f'Conteúdo textual alterado: {name} p.{local+1}')
            parts.append({'filename':name,'first_original_pdf_page':start+1,'last_original_pdf_page':end,
                          'page_count':end-start,'sha256':sha256(path)})
    if sum(x['page_count'] for x in parts)!=total:raise RuntimeError('Inconsistência na cobertura de páginas')
    if any(a['last_original_pdf_page']+1!=b['first_original_pdf_page'] for a,b in zip(parts,parts[1:])):
        raise RuntimeError('Lacunas ou duplicações de páginas detectadas')
    vra=None
    if vra_path:
        p=pathlib.Path(vra_path).resolve()
        if not p.is_file():raise ValueError('VRA não localizada')
        with fitz.open(p) as d:
            if d.needs_pass:raise RuntimeError('VRA protegida por senha')
            vra={'filename':p.name,'sha256':sha256(p),'pdf_pages':len(d)}
    batches=[parts[i:i+batch_size] for i in range(0,len(parts),batch_size)]
    manifest={'schema':'vra_corpus_parts_v1','created_utc':datetime.now(timezone.utc).isoformat(),
              'origin':{'filename':original.name,'sha256':sha256(original),'pdf_pages':total},
              'vra':vra,'parts':parts,'batches':[[part['filename'] for part in b] for b in batches],
              'verification':{'structural_coverage':True,'reading_by_gemini':'NOT_VERIFIED',
              'visual_inspection':'NOT_PERFORMED','substantive_audit':'NOT_PERFORMED'},
              'constraints':['O manifesto não prova leitura semântica do Gemini.',
              'Usar páginas originais indicadas no nome de cada parte; número da página da parte != página dos autos.',
              'NÃO realizar auditoria conclusiva até receber e examinar TODOS os lotes pertinentes ao marco temporal.',
              'NÃO utilizar movimentos posteriores à conclusão da VRA como prova da resposta histórica.',
              'Não criar alegações de ausência com base em buscas de apenas um subconjunto.']}
    mpath=out/'manifesto_corpus_vra.json'
    if mpath.exists():raise FileExistsError('Manifesto já existe; usar nova pasta')
    mpath.write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
    lines=['# Roteiro de apresentação dos autos ao Gemini',
           f'Autos: {original.name} — {total} páginas físicas — SHA-256 {manifest["origin"]["sha256"]}',
           f'Partes criadas: {len(parts)} | Lotes: {len(batches)}',
           'Esta etapa é EXTERNA ao Gemini Apps: não presumir que o Gemini executou Python.',
           'Anexe a VRA original junto ao primeiro lote.',
           'Solicite apenas o registro das partes recebidas e páginas originais cobertas em cada lote.',
           'Após o último lote, peça a auditoria. Se faltar segmento ou leitura visual, emitir IMPEDIMENTO TÉCNICO.',
           'Não anexar peças posteriores ao corte como fundamento da auditoria.',
           'O manifesto prova a divisão física, NÃO a leitura, conteúdo, validade documental ou exame humano.','']
    for i,batch in enumerate(batches,1):
        lines.append(f'## Lote {i}/{len(batches)}')
        for item in batch:
            lines.append(f'- {item["filename"]} (páginas originais {item["first_original_pdf_page"]}-{item["last_original_pdf_page"]})')
    (out/'INSTRUCOES_LOTES_GEMINI.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    return manifest


def main(argv=None):
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--autos',required=True,help='PDF integral dos autos')
    ap.add_argument('--vra',help='VRA preenchida (somente registra hash e quantidade de páginas)')
    ap.add_argument('--saida',required=True,help='Pasta NOVA para partes e manifesto')
    ap.add_argument('--paginas-por-parte',type=int,default=30)
    ap.add_argument('--partes-por-lote',type=int,default=5)
    a=ap.parse_args(argv)
    result=split_corpus(a.autos,a.saida,a.vra,a.paginas_por_parte,a.partes_por_lote)
    print(json.dumps({'status':'SEGMENTACAO_LOCAL_CONCLUIDA','pdf_pages':result['origin']['pdf_pages'],
                      'parts':len(result['parts']),'batches':len(result['batches']),
                      'gemini_reading_verified':False},ensure_ascii=False,indent=2))
if __name__=='__main__':
    try:main()
    except (OSError,ValueError,RuntimeError) as exc:
        print(f'ERRO: {exc}',file=sys.stderr);sys.exit(2)
