"""Verifica invariantes selecionadas; não comprova equivalência semântica."""
import json
import re
import sys
from pathlib import Path

root = Path(__file__).resolve().parent
cases = json.loads((root / 'casos.json').read_text(encoding='utf-8'))
path = Path(sys.argv[1]) if len(sys.argv) > 1 else root / 'resultados.json'
rows = json.loads(path.read_text(encoding='utf-8'))
results = {row['id']: row['resposta'] for row in rows}
errors = []
if len(results) != len(rows):
    errors.append('IDs duplicados nos resultados')
expected = {c['id'] for c in cases if c['ativar']}
if set(results) != expected:
    errors.append('Conjunto de resultados difere dos casos positivos')
for case in cases:
    if not case['ativar']:
        continue
    output = results.get(case['id'], '')
    for token in case.get('preservar', []):
        if token not in output:
            errors.append(f"{case['id']}: trecho protegido ausente: {token!r}")
    for token in case.get('proibir', []):
        if token.casefold() in output.casefold():
            errors.append(f"{case['id']}: adição indevida: {token!r}")
    if case['id'] == 'lista-formula':
        if re.findall(r'^([0-9]+)\. ', output, re.M) != ['1', '2', '3']:
            errors.append('lista-formula: quantidade ou ordem dos itens mudou')
    if case['id'] == 'json':
        try:
            value = json.loads(output)
            assert set(value) == {'id', 'texto', 'aprovado'}
            assert type(value['id']) is int and value['id'] == 17
            assert value['aprovado'] is False
            assert isinstance(value['texto'], str)
        except (ValueError, TypeError, AssertionError):
            errors.append('json: formato, chaves ou tipos alterados')
if errors:
    print('\n'.join(errors))
    sys.exit(1)
print(f'{len(expected)} casos: invariantes selecionadas preservadas. Revisão semântica ainda necessária.')
