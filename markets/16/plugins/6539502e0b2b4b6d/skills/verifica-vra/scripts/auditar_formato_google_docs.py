#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Checagem puramente FORMAL de texto destinado à relatório editável para Google Docs.

Não audita autos, não conhece a veracidade das fontes, não acessa Drive/Google Docs.
Ex.: python scripts/auditar_formato_google_docs.py --relatorio saida.md --itens 42 --decisao NECESSIDADE_DE_CORRECOES
"""
import argparse, json, pathlib, re, sys

SECTION_CODES=('1','2','3','4','5','7','8','9')
LABEL={'APROVACAO_DOCUMENTAL':'VRA APROVADA','NECESSIDADE_DE_CORRECOES':'VRA NECESSITA DE CORREÇÕES','IMPEDIMENTO_TECNICO':'IMPEDIMENTO TÉCNICO À AUDITORIA'}
DISCLAIMER='Conferência documental assistida por IA - sem homologação administrativa.'
class FormatViolation(ValueError):pass

def audit_format(source,expected_items,decision):
    errs=[]
    text=source.strip()
    lines=text.splitlines()
    if len(lines)<2 or lines[0].strip()!='# MINISTÉRIO PÚBLICO DO ESTADO DE GOIÁS' or lines[1].strip()!='# RELATÓRIO DE AUDITORIA DO PREENCHIMENTO DA VRA':
        errs.append('Título institucional não abre integralmente a resposta')
    heads=[(m.group(1),m.start()) for m in re.finditer(r'^## ([1-9])\.\s+(.+)$',text,re.M)]
    nums=[h[0] for h in heads]
    desired=['1','2','3','4','5']+(['6'] if decision=='NECESSIDADE_DE_CORRECOES' else [])+['7','8','9']
    if nums!=desired:errs.append(f'Seções numeradas incorretas: {nums}; esperado: {desired}')
    blocks=re.findall(r'^### Item\s+([^\n]+)$',text,re.M)
    if len(blocks)!=expected_items or len(set(blocks))!=expected_items:
        errs.append(f'Matriz incompleta/duplicada: {len(blocks)} blocos, {len(set(blocks))} IDs; esperado {expected_items}')
    match=re.search(r'^## 5\..+?(?=^## [67]\.|\Z)',text,re.M|re.S)
    if match:
        matrix=match.group(0)
        chunks=re.split(r'^### Item\s+[^\n]+$',matrix,flags=re.M)[1:]
        for i,c in enumerate(chunks,1):
            for field in ('Localizador do item na VRA original','Pergunta literal ORIGINAL','Resposta ORIGINAL da VRA',
                          'Avaliação material','Avaliação do preenchimento','Fundamentação','Evidência'):
                if field not in c:errs.append(f'Item {blocks[i-1] if i-1<len(blocks) else i}: campo obrigatório ausente: {field}')
    else:errs.append('Seção 5 de matriz integral ausente')
    if text.count(DISCLAIMER)<1:errs.append('Ressalva institucional obrigatória ausente')
    if '**DECISÃO: '+LABEL[decision]+'**' not in text:errs.append('Decisão conclusiva ausente ou diferente do contrato')
    if re.search(r'\[(?:extraíd[oa]|inserir|número|repetir|movimento/|resposta|página|\s*N\s*\])',text,re.I):errs.append('Placeholder do modelo permanece no relatório')
    if re.search(r'(?i)^(?:segue|a seguir|preparei|agora vou|você pode exportar)',text):errs.append('Prefácio externo ao relatório')
    return {'format_gate':'PASS' if not errs else 'FAIL','expected_items':expected_items,'item_blocks':len(blocks),'section_codes':nums,'errors':errs,'google_docs_created':False,'scope':'apenas formatação textual; não valida atos ou prova documental'}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--relatorio',required=True);ap.add_argument('--itens',type=int,required=True);ap.add_argument('--decisao',choices=tuple(LABEL),required=True)
    a=ap.parse_args()
    out=audit_format(pathlib.Path(a.relatorio).read_text(encoding='utf-8'),a.itens,a.decisao)
    print(json.dumps(out,ensure_ascii=False,indent=2));return 0 if out['format_gate']=='PASS' else 2
if __name__=='__main__':sys.exit(main())
