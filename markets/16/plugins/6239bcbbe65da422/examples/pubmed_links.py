"""Developer example: construct PubMed Clinical Queries links; never fabricates articles.

Usage: python pubmed_links.py --query 'PPI GERD pediatric' --years 3
"""
from __future__ import annotations
import argparse
from datetime import date
from calendar import monthrange
from urllib.parse import urlencode

CATEGORIES = ('Therapy','Diagnosis','Prognosis','Etiology','Clinical Prediction Guides')
SCOPES = ('Broad','Narrow')
BASE = 'https://pubmed.ncbi.nlm.nih.gov/'


def subtract_years(d: date, years: int) -> date:
    year = d.year - years
    return d.replace(year=year, day=min(d.day, monthrange(year,d.month)[1]))


def clinical_queries(query: str, start: date | None = None, end: date | None = None):
    if not query.strip():
        raise ValueError('Search query must not be empty')
    if start and end and start > end:
        raise ValueError('Start date must not exceed end date')
    result = []
    for category in CATEGORIES:
        for scope in SCOPES:
            term = f'({query.strip()}) AND ({category}/{scope}[Filter])'
            if start:
                stop = end or date.today()
                term += f' AND ({start:%Y/%m/%d}[Date - Publication] : {stop:%Y/%m/%d}[Date - Publication])'
            elif end:
                raise ValueError('Use start along with end')
            result.append((category, scope, BASE + '?' + urlencode({'term':term, 'sort':'date'})))
    return result


def similar_articles(pmid: str):
    if not pmid.isdecimal() or not pmid.strip('0'):
        raise ValueError('Provide a verified numeric PMID')
    return (
        f'https://pubmed.ncbi.nlm.nih.gov/{pmid}/?filter=simsearch1.fha',
        f'https://pubmed.ncbi.nlm.nih.gov/?linkname=pubmed_pubmed&from_uid={pmid}'
    )


if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--query', required=True)
    p.add_argument('--years', type=int, default=0)
    a=p.parse_args()
    if a.years < 0: p.error('--years cannot be negative')
    start=subtract_years(date.today(),a.years) if a.years else None
    for cat,scope,url in clinical_queries(a.query,start):
        print(f'{cat}/{scope}: {url}')
