#!/usr/bin/env python3
"""Static package and fixture checks only; not an LLM or OpenAI Platform runtime test."""
from pathlib import Path
import json, re, hashlib, sys
from urllib.parse import urlparse
ROOT=Path(__file__).resolve().parent.parent
REF=ROOT/'skills/contratacoes-publicas/references'

def run():
    m=json.loads((ROOT/'plugin.json').read_text(encoding='utf-8'))
    assert m['$schema']=='https://agent-plugins.org/schemas/1.0.0/plugin.schema.json'
    assert re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',m['name']) and len(m['name'])<=64
    assert re.fullmatch(r'\d+\.\d+\.\d+',m['version'])
    i=m['extensions']['com.openai']['interface']
    assert i['displayName']=='DIGG.IA: Contratações Públicas' and 'DIGG.IA: Assistente de Contratações Públicas' in i['longDescription']
    assert len(i['shortDescription'])<=30
    assert m['version']=='0.2.0'
    expected_urls={
       'websiteURL':'https://www.digg.ia.br',
       'supportURL':'https://www.digg.ia.br',
       'privacyPolicyURL':'https://digg.ia.br/privacy.html',
       'termsOfServiceURL':'https://digg.ia.br/terms.html',
    }
    for key,value in expected_urls.items():
        assert i[key]==value
        u=urlparse(i[key]); assert u.scheme=='https' and u.netloc in ('www.digg.ia.br','digg.ia.br') and len(i[key])<=1024
    status=json.loads((ROOT/'quality/verificacao_urls_publicacao.json').read_text())
    assert len(status['urls'])==4 and all(x['adequacao_conteudo']!='CONFIRMADA' for x in status['urls'].values())
    assert (ROOT/'quality/referencias/website-metadados-fornecidos.txt').is_file()
    assert (ROOT/i['logo'].removeprefix('./')).is_file()
    skilldirs=sorted((ROOT/'skills').glob('*/SKILL.md'))
    assert len(skilldirs)==5 and {p.parent.name for p in skilldirs}=={'contratacoes-publicas','elaborar-documentos','fontes-contratacoes','revisar-contratacoes','lge-v2102'}
    for f in skilldirs:
        t=f.read_text(encoding='utf-8')
        assert t.startswith('---\n')
        fm=t.split('---\n',2)[1]
        assert re.search(r'(?m)^name: \S+',fm) and re.search(r'(?m)^description: \S+',fm)
        assert f.stat().st_size<=1048576
    lge_path=ROOT/'skills/lge-v2102/references/skill_LGE_v2_10_2.yaml'
    assert lge_path.is_file() and hashlib.sha256(lge_path.read_bytes()).hexdigest()=='bc42f3f95432bffd8fa54fd2de1c6f26880b34ee8f3bfde096919fcb60db10da'
    assert '2.10.2' in (ROOT/'skills/lge-v2102/SKILL.md').read_text(encoding='utf8')
    assert '## Integração condicional da LGE 2.10.2' in (REF.parent/'SKILL.md').read_text(encoding='utf8')
    original=json.loads((REF/'manifesto_origens.json').read_text())['originais']
    assert len(original)==16
    for x in original:
        fp=REF/'originais'/x['arquivo']
        assert fp.is_file() and hashlib.sha256(fp.read_bytes()).hexdigest()==x['sha256']
    records=[json.loads(line) for line in (REF/'knowledge/base_curada.jsonl').read_text().splitlines() if line.strip()]
    assert len(records)==16 and len({x['id'] for x in records})==16
    assert all(x['estado_evidencia']!='VERIFICADO' and 'metadados_originais_nao_verificados' in x for x in records)
    models=json.loads((REF/'modelos_institucionais.json').read_text())
    expected={'DOD':6,'ETP_COMPLETO':17,'ETP_SIMPLIFICADO':9,'TR':19,'TR_TERCEIRIZACAO':19}
    assert {k:len(v['secoes']) for k,v in models.items()}==expected
    for k,v in models.items():
        assert [x['numero'] for x in v['secoes']]==list(range(1,expected[k]+1))
        doc=(ROOT/'quality/amostras'/(k+'.md')).read_text()
        headings=re.findall(r'(?m)^## (\d+)\. (.*)$',doc)
        assert [(int(a),b) for a,b in headings]==[(x['numero'],x['titulo']) for x in v['secoes']]
        assert doc.count('[PENDENTE:')==expected[k]
    idx=json.loads((REF/'indice_pdfs.json').read_text())
    tcu=next(x for x in idx if x['id']=='MANUAL_TCU_5A_2024')
    cover=[]
    for segment in tcu['indice_extracoes']:
        assert (ROOT/'skills/contratacoes-publicas'/segment['arquivo']).is_file()
        cover.extend(range(segment['paginas'][0],segment['paginas'][1]+1))
    assert cover==list(range(1,1014))
    fx=json.loads((ROOT/'quality/fixtures/coerencia-sintetica.json').read_text())
    fields=['objeto','quantidade','unidade','estimativa_total','prazo_dias']
    base=fx['documentos'];assert all(len({base[k][f] for k in base})==1 for f in fields)
    divergent={k:dict(v) for k,v in base.items()};divergent['TR']=fx['cenario_divergente']['TR']
    differences=[f for f in fields if len({divergent[k][f] for k in divergent})>1]
    assert differences==['quantidade']
    inv=json.loads((ROOT/'inventario_sha256.json').read_text())['sha256_arquivos']
    for f in inv:
        fp=ROOT/f['path'];assert fp.exists() and hashlib.sha256(fp.read_bytes()).hexdigest()==f['sha256']
    print('APROVADO: metadados 0.2.0, quatro URLs e proveniencia, 5 skills, 16 fontes, 16 KB, 5 modelos, 1013 paginas TCU, pendencias em minutas, cenarios coerentes/divergentes, hashes. CONTEUDO JURIDICO DAS PAGINAS PENDENTE.')
    return 0
if __name__=='__main__':sys.exit(run())
