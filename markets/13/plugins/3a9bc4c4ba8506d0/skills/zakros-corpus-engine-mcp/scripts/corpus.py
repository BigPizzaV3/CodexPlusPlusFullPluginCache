#!/usr/bin/env python3
"""Read-only exact queries over the supplied Zakros v1.5 evidence graph."""
import argparse
import csv
import hashlib
import json
import re
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / 'references' / 'corpus-v1.5'
TABLES = {
    'nodes': ('nodes_v1_5.csv', 'node_id'),
    'edges': ('edges_v1_5.csv', 'edge_id'),
    'parser_rules': ('parser_rules_v1_5.csv', 'rule_id'),
    'claim_guardrails': ('claim_guardrails_v1_5.csv', 'guardrail_id'),
}


def load_graph():
    return json.loads((DATA / 'graph_v1_5.json').read_text(encoding='utf-8-sig'))


def normalize(value):
    return re.sub(r'\s+', '', value).upper()


def select_node(graph, query, inscription=False):
    key = normalize(query)
    for node in graph['nodes']:
        if (node['node_type'] == 'inscription') != inscription:
            continue
        aliases = {normalize(node['node_id']), normalize(node['label'])}
        if not inscription:
            aliases.add(normalize(node['label'].split(' {', 1)[0]))
        if key in aliases:
            return node
    return None


def records(graph, query, inscription=False):
    node = select_node(graph, query, inscription)
    result = {
        'source': 'graph_v1_5.json', 'query': query,
        'status': 'FOUND' if node else 'ABSENT_FROM_GRAPH',
        'node': node, 'edges': [], 'connected_nodes': [],
        'interpretation': 'These are graph records, not a translation or independently verified readings.',
    }
    if node is None:
        result['limitation'] = 'Absent from this export; no conclusion about corpus-wide attestation.'
        return result
    nid = node['node_id']
    result['edges'] = [
        e for e in graph['edges']
        if nid in (e['source_node_id'], e['target_node_id'])
        or (inscription and normalize(e.get('inscription') or '') == normalize(node['label']))
    ]
    ids = {e[k] for e in result['edges'] for k in ('source_node_id', 'target_node_id')} - {nid}
    result['connected_nodes'] = [n for n in graph['nodes'] if n['node_id'] in ids]
    return result


def search_table(graph, table, query=None):
    values = graph[table]
    if query:
        term = query.casefold()
        values = [v for v in values if any(term in str(x).casefold() for x in v.values() if x is not None)]
    return {'source': 'graph_v1_5.json', 'table': table, 'query': query, 'records': values,
            'limitation': 'Text matching only; applicability requires checking each rule condition.'}


def verify(graph):
    checks = {}
    node_ids = [n['node_id'] for n in graph['nodes']]
    checks['unique_nodes'] = len(set(node_ids)) == len(node_ids)
    checks['edge_endpoints_exist'] = all(e[k] in set(node_ids) for e in graph['edges'] for k in ('source_node_id', 'target_node_id'))
    for table, (filename, idkey) in TABLES.items():
        with (DATA / filename).open(encoding='utf-8-sig', newline='') as stream:
            csv_rows = list(csv.DictReader(stream))
        json_rows = [{k: '' if v is None else str(v) for k, v in row.items()} for row in graph[table]]
        checks[table + '_csv_parity'] = csv_rows == json_rows
        ids = [r[idkey] for r in graph[table]]
        checks[table + '_unique_ids'] = len(ids) == len(set(ids))
    for table, metakey in [('nodes', 'node_count'), ('edges', 'edge_count'), ('parser_rules', 'parser_rule_count'), ('claim_guardrails', 'guardrail_count')]:
        checks[table + '_count'] = len(graph[table]) == graph['metadata'][metakey]
    return {'status': 'PASS' if all(checks.values()) else 'FAIL', 'checks': checks,
            'sha256': {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(DATA.iterdir()) if p.is_file()},
            'limitation': 'Internal consistency only; not independent verification of the scholarship.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    for name in ('status', 'verify'):
        sub.add_parser(name)
    for name in ('inscription', 'form'):
        sub.add_parser(name).add_argument('query')
    for name in ('rules', 'guardrails'):
        sub.add_parser(name).add_argument('query', nargs='?')
    args = parser.parse_args()
    graph = load_graph()
    if args.command == 'status':
        result = {'metadata': graph['metadata'], 'inscriptions': [n['label'] for n in graph['nodes'] if n['node_type'] == 'inscription'],
                  'counts': {k: len(graph[k]) for k in TABLES}}
    elif args.command == 'verify':
        result = verify(graph)
    elif args.command in ('inscription', 'form'):
        result = records(graph, args.query, args.command == 'inscription')
    else:
        result = search_table(graph, 'parser_rules' if args.command == 'rules' else 'claim_guardrails', args.query)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if result.get('status') == 'FAIL' else 0


if __name__ == '__main__':
    raise SystemExit(main())
