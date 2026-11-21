#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Valida registros de AUDITORIA de VRA JÁ PREENCHIDA e produz relatório textual para Google Docs.

Este script NÃO cria documento Google Docs, não aciona interface Gemini/Drive e não verifica
veracidade das fontes: exige conferência humana/IA prévia, com evidência auditável.
Uso: python scripts/validar_e_formatar_vra.py --dados tests/analise_sintetica.json --saida saida.md
"""
from __future__ import annotations
import argparse
from collections import Counter
import datetime as dt
import json
from pathlib import Path
import re
import sys
STATUSES=('CONFORME','NAO_CONFORME','EVIDENCIA_INSUFICIENTE','NAO_APLICAVEL','ANALISE_IMPOSSIBILITADA')
FILL=('ADEQUADO','RESPOSTA_INCORRETA','REFERENCIA_INCORRETA','OMISSAO_DE_PREENCHIMENTO','NAO_DETERMINADO')
DECISIONS=('APROVACAO_DOCUMENTAL','NECESSIDADE_DE_CORRECOES','IMPEDIMENTO_TECNICO')
LABELS={'APROVACAO_DOCUMENTAL':'VRA APROVADA',
 'NECESSIDADE_DE_CORRECOES':'VRA NECESSITA DE CORREÇÕES',
 'IMPEDIMENTO_TECNICO':'IMPEDIMENTO TÉCNICO À AUDITORIA'}
NOTA='Conferência documental assistida por IA - sem homologação administrativa.'
class ValidationError(ValueError): pass

def check(condition,msg):
 if not condition: raise ValidationError(msg)

def text(d,key,where='análise',allow_empty=False):
 value=d.get(key)
 check(isinstance(value,str) and (allow_empty or value.strip()),f'{where}.{key}: string obrigatória ausente')
 return value.strip()

def temporal(val,where):
 try:date=dt.datetime.fromisoformat(str(val).replace('Z','+00:00'))
 except Exception as exc:raise ValidationError(f'{where}: timestamp ISO 8601 inválido') from exc
 check(date.tzinfo is not None,f'{where}: exigido fuso horário')
 return date

def page_numbers_from_ranges(ranges,total_pages,where):
 """Expande intervalos declarados 1-3 ou páginas inteiras; não comprova inspeção real."""
 check(isinstance(ranges,list),f'{where}: lista de intervalos obrigatória')
 result=set()
 for segment in ranges:
  check(isinstance(segment,(int,str)),f'{where}: intervalo inválido')
  match=re.fullmatch(r'\s*(\d+)(?:\s*[-–]\s*(\d+))?\s*',str(segment))
  check(bool(match),f'{where}: intervalo malformado {segment!r}')
  a=int(match.group(1));b=int(match.group(2) or a)
  check(1<=a<=b<=total_pages,f'{where}: intervalo fora das páginas {segment!r}')
  result.update(range(a,b+1))
 return result

def validate_source_inventory(d,cutoff,is_date):
 """Validação estrutural de cobertura; não atesta que páginas foram realmente lidas."""
 inv=d.get('source_inventory')
 check(isinstance(inv,dict),'source_inventory: índice de páginas e movimentos obrigatório')
 for field in ('total_pages','max_movement_number'):
  check(type(inv.get(field)) is int and inv[field]>=1,f'source_inventory.{field} inválido')
 movements=inv.get('movements')
 check(isinstance(movements,list) and movements,'source_inventory.movements vazio ou inválido')
 check(type(inv.get('pdf_pages_observed')) is int,'source_inventory.pdf_pages_observed obrigatório')
 check(inv['pdf_pages_observed']==inv['total_pages'],'P0: número de páginas observado diverge do inventário')
 text(inv,'page_count_provenance','source_inventory')
 text(inv,'access_proof','source_inventory')
 samples=inv.get('first_middle_last_samples')
 check(isinstance(samples,list) and len(samples)>=3 and all(type(p) is int and 1<=p<=inv['total_pages'] for p in samples),
       'P0: amostras início/meio/fim não registradas')
 check(samples[0]==1 and samples[-1]==inv['total_pages'], 'P0: amostras devem incluir a primeira e última páginas físicas')
 check(isinstance(inv.get('reviewed_page_ranges'),list),'source_inventory.reviewed_page_ranges obrigatório')
 inspected=page_numbers_from_ranges(inv['reviewed_page_ranges'],inv['total_pages'],'reviewed_page_ranges')
 for k in ('image_only_pages','visually_inspected_pages'):
  check(isinstance(inv.get(k),list),f'source_inventory.{k}: lista obrigatória, ainda que vazia')
 imgs=page_numbers_from_ranges(inv['image_only_pages'],inv['total_pages'],'image_only_pages')
 visual=page_numbers_from_ranges(inv['visually_inspected_pages'],inv['total_pages'],'visually_inspected_pages')
 if d['decision']!='IMPEDIMENTO_TECNICO':
  check(imgs<=visual,f'Páginas de documentos digitalizados sem inspeção visual: {sorted(imgs-visual)}')
 text(inv,'visual_detection_method','source_inventory')
 nums=[];previous_end=0
 for n,m in enumerate(movements,1):
  check(isinstance(m,dict),f'movimento manifesto[{n}] inválido')
  number=m.get('number');start=m.get('page_start');end=m.get('page_end')
  check(type(number) is int and number>0,f'movimento manifesto[{n}] sem id')
  check(type(start) is int and type(end) is int and 1<=start<=end<=inv['total_pages'],f'movimento {number} com páginas inválidas')
  check(start>previous_end,f'movimento {number} sobrepõe ou retrocede páginas');previous_end=end
  nums.append(number)
  joined=temporal(m.get('joined_at'),f'movimento {number}.joined_at')
  eligible=(joined.date()<cutoff if is_date else joined<=cutoff)
  if is_date and joined.date()==cutoff:
   check(m.get('before_cutoff_by_institutional_order') is True or m.get('temporal_status')=='UNRESOLVED',
         f'movimento {number}: mesma data do corte sem evidência de ordem institucional')
   eligible=m.get('before_cutoff_by_institutional_order') is True
  status=m.get('temporal_status')
  check(status in ('ELIGIBLE','EXCLUDED_AFTER_CUTOFF','UNRESOLVED'),f'movimento {number} temporal_status inválido')
  check(status==('ELIGIBLE' if eligible else 'EXCLUDED_AFTER_CUTOFF') or (is_date and status=='UNRESOLVED'),
        f'movimento {number}: classificação temporal incoerente')
  review=m.get('review_status')
  check(review in ('REVIEWED','PARTIAL','NOT_REVIEWED','EXCLUDED'),f'movimento {number}: review_status inválido')
  text(m,'review_note',f'movimento {number}')
  if status=='EXCLUDED_AFTER_CUTOFF':check(review=='EXCLUDED',f'movimento {number}: ato posterior deve ser excluído')
  if d['decision']!='IMPEDIMENTO_TECNICO' and status=='UNRESOLVED':
   raise ValidationError(f'movimento {number}: classificação temporal não resolvida impede decisão substantiva')
  if d['decision']!='IMPEDIMENTO_TECNICO' and status=='ELIGIBLE':
   check(review=='REVIEWED',f'movimento {number}: corte com segmento elegível não revisado — impedimento técnico')
   check(set(range(start,end+1))<=inspected,f'movimento {number}: páginas historicamente elegíveis não cobertas pelo reviewed_page_ranges')
 check(nums==list(range(1,inv['max_movement_number']+1)),
       f'Inventário de movimentos incompleto: observado {nums}, esperado 1..{inv["max_movement_number"]}')
 # P0: toda página física deve ser atribuída a movimento ou intervalo não vinculado,
 # explicitamente justificado. Sem esse fechamento, lacunas podem ocultar documentos.
 assigned=set()
 for mv in movements:
  assigned.update(range(mv['page_start'],mv['page_end']+1))
 unassigned=page_numbers_from_ranges(inv.get('unassigned_page_ranges',[]),inv['total_pages'],'unassigned_page_ranges')
 check(not (assigned & unassigned),'P0: páginas duplicadas entre movimentos e intervalos não vinculados')
 missing=set(range(1,inv['total_pages']+1))-assigned-unassigned
 if d['decision']!='IMPEDIMENTO_TECNICO':
  check(not missing,f'P0: páginas físicas sem vínculo no inventário: {sorted(missing)}')
  if unassigned:
   text(inv,'unassigned_pages_note','source_inventory')
   check(unassigned<=inspected,'P0: páginas não vinculadas a movimentos não foram revisadas')
 if d['decision']!='IMPEDIMENTO_TECNICO':
  check(not inv.get('corpus_incomplete'), 'Corpus declarado incompleto não permite conclusão substantiva')
 return inv

def validate_evidence_locator(e,movements,where):
 """Confere apenas localizadores explícitos PDF-ordinal e movimento numerado.

 Páginas de documentos anexos podem ter paginação interna diferente; nesses
 casos fornecer o localizador PDF original para poder validar o vínculo.
 """
 movement=str(e.get('movement','')).strip()
 m=re.fullmatch(r'(?i)(?:mov(?:imento)?\.?\s*)?0*(\d+)',movement)
 pg=str(e.get('page','')).strip()
 p=re.fullmatch(r'(?i)(?:p(?:ág(?:ina)?)?\.?\s*)?(\d+)',pg)
 if not (m and p):return
 num=int(m.group(1)); page=int(p.group(1))
 by_num={v['number']:v for v in movements}
 check(num in by_num,f'{where}: movimento {num} ausente do inventário')
 v=by_num[num]
 check(v['page_start']<=page<=v['page_end'],
       f'{where}: página PDF {page} fora do movimento {num} ({v["page_start"]}-{v["page_end"]})')
 check(v['temporal_status']=='ELIGIBLE',f'{where}: referência a movimento posterior ou temporalmente não resolvido')


def validate_absence_claims(d,seen):
 claims=d.get('absence_claims')
 check(isinstance(claims,list),'absence_claims: lista obrigatória, ainda que vazia')
 ids=set()
 for n,c in enumerate(claims,1):
  check(isinstance(c,dict),f'absence_claims[{n}] inválido')
  for key in ('item_id','document_type','counterevidence_review','conclusion'):text(c,key,f'absence_claims[{n}]')
  check(c['item_id'] in seen,f'absence_claims[{n}]: item não inventariado')
  check(isinstance(c.get('searched_movement_ids'),list) and c['searched_movement_ids'],
        f'absence_claims[{n}]: movimentos examinados não comprovados')
  check(isinstance(c.get('searched_page_ranges'),list) and c['searched_page_ranges'],
        f'absence_claims[{n}]: intervalos de páginas não registrados')
  check(isinstance(c.get('search_methods'),list) and len(c['search_methods'])>=2,
        f'absence_claims[{n}]: exigir busca e inspeção contextual')
  check(any('context' in m.lower() or 'manual' in m.lower() or 'leitura' in m.lower() for m in c['search_methods']),
        f'absence_claims[{n}]: busca textual isolada não prova ausência')
  check(not c.get('positive_matches'),f'absence_claims[{n}]: existe contraprova de presença do documento')
  ids.add(c['item_id'])
 for f in d.get('findings',[]):
  if f.get('claim_type')=='DOCUMENT_ABSENCE':
   check(f['item_id'] in ids,f'{f["item_id"]}: achado de ausência sem manifesto de buscas')
  if re.search(r'\b(não consta(?:m)? dos autos|inexist[eê]ncia de documento|documento não juntado)\b',
               f.get('issue',''),re.IGNORECASE):
   check(f.get('claim_type')=='DOCUMENT_ABSENCE',f'{f["item_id"]}: afirmação de ausência sem claim_type explícito')
 return claims

def validate(d):
 check(isinstance(d,dict),'O JSON deve conter objeto raiz')
 for field in ('process_id','vra_title','cutoff_at','cutoff_source','decision','executive_summary','scope','coverage_statement','conclusion'):text(d,field)
 check(d['decision'] in DECISIONS,'Decisão fora do domínio')
 is_date=bool(re.fullmatch(r'\d{4}-\d{2}-\d{2}',d['cutoff_at']))
 if is_date:
  check(d.get('cutoff_precision')=='DATE_ONLY','Corte apenas por data exige cutoff_precision=DATE_ONLY')
  text(d,'date_only_resolution')
  cutoff=dt.date.fromisoformat(d['cutoff_at'])
 else:cutoff=temporal(d['cutoff_at'],'cutoff_at')
 validate_source_inventory(d,cutoff,is_date)
 for field in ('items','findings','sources'):
  check(isinstance(d.get(field,[]),list),f'{field} deve ser lista')
 items=d.get('items',[]);findings=d.get('findings',[]);sources=d.get('sources',[])
 check(isinstance(d.get('expected_items_count'),int) and d['expected_items_count']>=0,'expected_items_count ausente ou inválido')
 check(len(items)==d['expected_items_count'],f'Cobertura inválida: {len(items)} registros para {d["expected_items_count"]} itens inventariados')
 if d['decision']!='IMPEDIMENTO_TECNICO':
  check(items,'Resultado substantivo exige itens avaliados')
  check(sources,'Resultado substantivo exige fontes examinadas')
  check(not d.get('coverage_blocked'),'Cobertura bloqueada exige impedimento técnico')
 seen=set(); issues=[]
 for n,item in enumerate(items,1):
  check(isinstance(item,dict),f'items[{n}] deve ser objeto')
  for field in ('item_id','vra_item_locator','item_text','material_status','filling_status','rationale'):text(item,field,f'items[{n}]')
  check(isinstance(item.get('declared_references'),(str,list)),f'items[{n}].declared_references deve refletir campo original ou ausência explícita')
  check(isinstance(item.get('original_justification',''),str),f'items[{n}].original_justification inválida')
  check(isinstance(item.get('answer_raw'),str),f'items[{n}].answer_raw deve ser string')
  ident=item['item_id']
  check(ident not in seen,f'item_id duplicado: {ident}');seen.add(ident)
  st=item['material_status'];fill=item['filling_status']
  check(st in STATUSES and fill in FILL,f'items[{n}]: classificação inválida')
  ev=item.get('evidence',[]);check(isinstance(ev,list),f'items[{n}].evidence não é lista')
  if st in ('CONFORME','NAO_CONFORME','NAO_APLICAVEL'):
   check(bool(ev),f'{ident}: {st} sem evidência documental')
  if st=='EVIDENCIA_INSUFICIENTE':text(item,'evidence_gap',ident)
  if st=='NAO_APLICAVEL':text(item,'na_basis',ident)
  if st=='ANALISE_IMPOSSIBILITADA':text(item,'block_reason',ident)
  for j,e in enumerate(ev,1):
   check(isinstance(e,dict),f'{ident}: evidência {j} inválida')
   check(bool(e.get('movement') or e.get('document')),f'{ident}: evidência {j} não localizável')
   check(bool(e.get('page') or e.get('locator')),f'{ident}: evidência {j} sem página/localizador')
   check(e.get('eligible_by_cutoff') is True,f'{ident}: evidência {j} sem anterioridade confirmada')
   text(e,'temporal_basis',f'{ident}/evidencia[{j}]')
   validate_evidence_locator(e,d['source_inventory']['movements'],f'{ident}/evidencia[{j}]')
   if e.get('joined_at'):
    joined=temporal(e['joined_at'],f'{ident}.joined_at')
    if is_date:
     check(joined.date()<=cutoff,f'{ident}: documento posterior ao corte')
     if joined.date()==cutoff:
      check(e.get('before_cutoff_by_institutional_order') is True,f'{ident}: sequência no dia do corte não comprovada')
    else: check(joined<=cutoff,f'{ident}: documento posterior ao corte')
  if st not in ('CONFORME','NAO_APLICAVEL') or fill!='ADEQUADO':issues.append(ident)
 validate_absence_claims(d,seen)
 for j,source in enumerate(sources,1):
  check(isinstance(source,dict),f'sources[{j}]: fonte inválida')
  validate_evidence_locator(source,d['source_inventory']['movements'],f'sources[{j}]')
 check(not (d['decision']!='IMPEDIMENTO_TECNICO' and any(i['material_status']=='ANALISE_IMPOSSIBILITADA' for i in items)),
       'Impossibilidade em item impede decisão substantiva')
 finding_items=set()
 for n,f in enumerate(findings,1):
  for field in ('id','item_id','issue','criterion','evidence_text','remediation','priority','review_criterion'):text(f,field,f'findings[{n}]')
  check(f['item_id'] in seen,f'findings[{n}] referencia item inexistente')
  check(f['priority'] in ('ALTA','MEDIA','BAIXA'),'Prioridade fora do domínio')
  finding_items.add(f['item_id'])
 if d['decision']=='APROVACAO_DOCUMENTAL':
  check(not issues,'Aprovação com item pendente ou preenchimento incorreto')
  check(not findings,'Aprovação com achados')
  check(not d.get('material_gaps'),'Aprovação com lacunas materiais')
 elif d['decision']=='NECESSIDADE_DE_CORRECOES':
  check(issues,'Correções sem item afetado')
  check(set(issues).issubset(finding_items),f'Itens afetados sem achado individualizado: {set(issues)-finding_items}')
 else: text(d,'technical_block')
 return d


def inline(value):
 """Escape de metacaracteres Markdown para dados oriundos dos autos."""
 if isinstance(value,list):value=', '.join(str(x) for x in value)
 if value is None:value='Não informado nos registros'
 s=str(value).replace('\r',' ').replace('\n',' / ')
 return re.sub(r'([\\`*_\[\]<>|])',r'\\\1',s)

def evlabel(e):
 return ' · '.join(f'{k}: {inline(e[v])}' for k,v in [('Mov.','movement'),('Documento','document'),('Página','page'),('Localizador','locator')] if e.get(v))


def validate_against_pdf_file(d,pdf_path):
 """Checa número de páginas informado no JSON contra PDF real, não a leitura das provas."""
 from pathlib import Path
 import importlib.util
 module_path=Path(__file__).with_name("verificar_pdf_entrada.py")
 spec=importlib.util.spec_from_file_location("vra_pdf_preflight",module_path)
 module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
 info=module.inspect_pdf(Path(pdf_path))
 claimed=d['source_inventory']['total_pages']
 claimed_sha=d['source_inventory'].get('source_pdf_sha256')
 if claimed_sha is not None:
  check(isinstance(claimed_sha,str) and bool(re.fullmatch(r'[a-fA-F0-9]{64}',claimed_sha)),
        'source_inventory.source_pdf_sha256: SHA-256 inválido')
  check(claimed_sha.lower()==info['source_sha256'],
        'ERR_CORPUS_DIFERENTE: SHA-256 do PDF não corresponde ao inventário')
 check(claimed==info['pdf_pages_observed'],
       f'ERR_CORPUS_TRUNCADO: inventário informa {claimed} páginas, PDF físico tem {info["pdf_pages_observed"]}')
 return info

def validate_original_vra_file(d,vra_path):
 """Vincula o PDF fornecido à impressão digital declarada, quando presente.

 Não prova que as marcações no documento foram transcritas corretamente.
 """
 import importlib.util
 module_path=Path(__file__).with_name('verificar_pdf_entrada.py')
 spec=importlib.util.spec_from_file_location('vra_pdf_preflight_original',module_path)
 module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
 info=module.inspect_pdf(Path(vra_path))
 claimed_sha=d.get('vra_pdf_sha256')
 if claimed_sha is not None:
  check(isinstance(claimed_sha,str) and bool(re.fullmatch(r'[a-fA-F0-9]{64}',claimed_sha)),
        'vra_pdf_sha256: SHA-256 inválido')
  check(claimed_sha.lower()==info['source_sha256'],
        'ERR_VRA_ORIGINAL_DIFERENTE: SHA-256 da VRA não corresponde ao registro')
 return info


def validate_formatted_report(markdown,expected_items,decision):
 """FMT-01 textual: complementa, mas não substitui, validação probatória."""
 import importlib.util
 spec=importlib.util.spec_from_file_location('vra_formal_gate',Path(__file__).with_name('auditar_formato_google_docs.py'))
 module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
 outcome=module.audit_format(markdown,expected_items,decision)
 check(outcome['format_gate']=='PASS', 'FMT-01: '+str(outcome['errors']))
 return outcome


def render_markdown(d):
 validate(d)
 out=[]
 def line(v=''):out.append(str(v))
 line('# MINISTÉRIO PÚBLICO DO ESTADO DE GOIÁS')
 line('# RELATÓRIO DE AUDITORIA DO PREENCHIMENTO DA VRA')
 line('**Processo administrativo:** '+inline(d['process_id']))
 line('**VRA ORIGINAL auditada:** '+inline(d['vra_title']))
 line('**Resultado:** '+LABELS[d['decision']])
 line('**Natureza:** '+NOTA)
 line('')
 line('## 1. IDENTIFICAÇÃO E CORTE TEMPORAL')
 for label,key in [('Processo','process_id'),('VRA','vra_title'),('Localização da VRA','vra_location'),('Objeto','object'),('Unidade','unit'),('Assinaturas','signatures'),('Marco temporal histórico','cutoff_at'),('Prova da conclusão','cutoff_source')]:
  line(f'**{label}:** {inline(d.get(key))}')
 line('**Regra aplicada:** apenas autos/documentos juntados até a assinatura/conclusão da VRA.')
 line('')
 line('## 2. AUDITORIA DO PREENCHIMENTO ORIGINAL: OBJETO, ESCOPO E LIMITAÇÕES')
 line(inline(d['scope']))
 line('**Cobertura:** '+inline(d['coverage_statement']))
 inv=d['source_inventory']
 line('**Integridade do corpus:** '+str(inv['total_pages'])+' páginas; movimentos 1 a '+str(inv['max_movement_number'])+'.')
 line('**Contagem verificada por:** '+inline(inv['page_count_provenance']))
 line('**Amostras início/meio/fim:** '+inline(inv['first_middle_last_samples']))
 line('**Evidência de acesso:** '+inline(inv['access_proof']))
 if inv.get('source_pdf_sha256'):line('**SHA-256 do PDF dos autos:** '+inline(inv['source_pdf_sha256']))
 if inv.get('unassigned_page_ranges'):
  line('**Páginas fora da numeração dos movimentos:** '+inline(inv['unassigned_page_ranges']))
  line('**Tratamento dessas páginas:** '+inline(inv.get('unassigned_pages_note')))
 line('**Páginas image-backed relevantes detectadas:** '+inline(inv['image_only_pages'] or 'Nenhuma declarada'))
 line('**Páginas inspecionadas visualmente:** '+inline(inv['visually_inspected_pages'] or 'Nenhuma declarada'))
 line('**Método de detecção de páginas sem texto:** '+inline(inv['visual_detection_method']))
 line('**Manifesto dos movimentos e cortes:**')
 for mv in inv['movements']:
  line('- Mov. '+str(mv['number'])+' · páginas '+str(mv['page_start'])+'-'+str(mv['page_end'])+' · '+inline(mv['temporal_status'])+' · '+inline(mv['review_status']))
 if d.get('absence_claims'):
  line('**Controle de alegações de ausência documental:**')
  for c in d['absence_claims']:
   line('- Item '+inline(c['item_id'])+' · '+inline(c['document_type'])+' · mov. '+inline(c['searched_movement_ids'])+' · páginas '+inline(c['searched_page_ranges'])+' · revisão de contraprovas: '+inline(c['counterevidence_review']))
 for limitation in d.get('limitations',[]):line('- '+inline(limitation))
 line('')
 line('## 3. RESULTADO DA AUDITORIA DA VRA PREENCHIDA')
 line('**DECISÃO: '+LABELS[d['decision']]+'**')
 line(inline(d['executive_summary']))
 if d.get('technical_block'):line('**Impedimento técnico:** '+inline(d['technical_block']))
 line('')
 line('## 4. QUADRO-SÍNTESE')
 counts=Counter(i['material_status'] for i in d['items'])
 line(f'- **Itens inventariados:** {d["expected_items_count"]}')
 line(f'- **Itens registrados:** {len(d["items"])}')
 for status in STATUSES:line(f'- **{status}:** {counts[status]}')
 err=sum(i['filling_status']!='ADEQUADO' for i in d['items'])
 line(f'- **Itens com preenchimento não adequado:** {err}')
 line(f'- **Achados:** {len(d.get("findings",[]))}')
 line('As cinco classificações materiais somam o total de itens; erros de preenchimento são uma dimensão independente.')
 line('')
 line('## 5. MATRIZ INTEGRAL DA AUDITORIA DE 100% DOS ITENS DA VRA ORIGINAL')
 for item in d['items']:
  line('### Item '+inline(item['item_id']))
  for label,key in [('Localizador do item na VRA original','vra_item_locator'),('Pergunta literal ORIGINAL','item_text'),('Resposta ORIGINAL da VRA','answer_raw'),('Justificativa/observação ORIGINAL','original_justification'),('Referências ORIGINALMENTE declaradas','declared_references'),('Avaliação material','material_status'),('Avaliação do preenchimento','filling_status'),('Fundamentação','rationale')]:
   line(f'**{label}:** {inline(item.get(key) if key!='original_justification' or item.get(key) else 'Não registrada na VRA original')}')
  if item['evidence']:
   for e in item['evidence']:
    line('- **Evidência:** '+evlabel(e)+' — '+inline(e.get('excerpt','Fonte examinada')))
  else:line('**Evidência:** nenhuma fonte afirmativa localizada nos registros examinados.')
  for label,key in [('Lacuna probatória','evidence_gap'),('Justificativa de N.A.','na_basis'),('Impedimento do item','block_reason')]:
   if item.get(key):line(f'**{label}:** {inline(item[key])}')
  line('')
 if d['decision']=='NECESSIDADE_DE_CORRECOES':
  line('## 6. ACHADOS NA VRA ORIGINAL E AJUSTES PROPOSTOS PARA REVISÃO HUMANA')
  for f in d.get('findings',[]):
   line('### Achado '+inline(f['id'])+' — Item '+inline(f['item_id']))
   for label,key in [('Resposta ORIGINAL da VRA','_answer_original'),('Referência ORIGINAL da VRA','_refs_original'),('Apontamento','issue'),('Prioridade','priority'),('Fundamento','criterion'),('Fonte/evidência','evidence_text'),('Proposta de ajuste (não altera a VRA)','remediation'),('Critério de revalidação','review_criterion')]:
    item_orig=next((i for i in d['items'] if i['item_id']==f['item_id']),{})
    original={'_answer_original':item_orig.get('answer_raw'),'_refs_original':item_orig.get('declared_references')}
    line(f'**{label}:** {inline(original[key] if key in original else f.get(key))}')
   line('')
 line('## 7. ITENS NÃO APLICÁVEIS')
 na=[i for i in d['items'] if i['material_status']=='NAO_APLICAVEL']
 if not na:line('Nenhum item classificado como não aplicável.')
 for i in na:line('- **Item '+inline(i['item_id'])+':** '+inline(i.get('na_basis')))
 line('')
 line('## 8. CONCLUSÃO SOBRE O PREENCHIMENTO ORIGINAL E ENCAMINHAMENTO')
 line(inline(d['conclusion']))
 line('**Revisão humana:** '+inline(d.get('human_review','Revisão humana requerida antes do uso administrativo.')))
 line(NOTA)
 line('')
 line('## 9. FONTES, EXCLUSÕES E REGISTRO DE COBERTURA')
 line('**Fontes examinadas:**')
 if not d['sources']:line('- Nenhuma fonte validada devido a impedimento técnico.')
 for s in d['sources']:
  line('- '+evlabel(s)+' — '+inline(s.get('function','Fonte examinada')))
 line('**Fontes posteriores ao corte, excluídas:**')
 if not d.get('excluded_after_cutoff'):line('- Nenhuma identificada nos registros examinados.')
 else:
  for x in d['excluded_after_cutoff']:line('- '+inline(x))
 if d.get('uninspected_references'):
  line('**Referências não inspecionadas:**')
  for x in d['uninspected_references']:line('- '+inline(x))
 if d.get('material_gaps'):
  line('**Lacunas materiais:**')
  for x in d['material_gaps']:line('- '+inline(x))
 line(f'**Cobertura da VRA:** {len(d["items"])} de {d["expected_items_count"]} itens inventariados.')
 result='\n'.join(out)+'\n'
 for i in d['items']:
  check('### Item '+inline(i['item_id']) in result,'Item ausente da saída textual')
 check(result.count(NOTA)>=2,'Falta ressalva institucional')
 check('## 9. FONTES' in result,'Sem fontes')
 return result

def main():
 ap=argparse.ArgumentParser()
 ap.add_argument('--dados',required=True)
 ap.add_argument('--saida')
 ap.add_argument('--autos',help='PDF real dos autos; confere contagem e SHA-256, se declarado')
 ap.add_argument('--vra',help='VRA ORIGINAL em PDF; confere SHA-256 quando declarado')
 args=ap.parse_args()
 try:
  d=json.loads(Path(args.dados).read_text(encoding='utf-8'))
  if args.autos:
   validate_against_pdf_file(d,args.autos)
  if args.vra:
   validate_original_vra_file(d,args.vra)
  rendered=render_markdown(d)
  validate_formatted_report(rendered,d['expected_items_count'],d['decision'])
  if args.saida:
   Path(args.saida).write_text(rendered,encoding='utf-8')
   print(json.dumps({'status':'VALIDO_PARA_FORMATACAO_LOCAL','saida':str(Path(args.saida).resolve()),'itens':len(d['items']),'google_docs_created':False},ensure_ascii=False))
  else:print(rendered)
  return 0
 except (ValidationError,ValueError,KeyError,OSError) as e:
  print('ERR_REGISTROS_INVALIDOS: '+str(e),file=sys.stderr)
  return 2
if __name__=='__main__':sys.exit(main())
