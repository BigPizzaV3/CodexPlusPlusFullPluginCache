"""Explicit, offline reference-rate estimates. Never fetch transaction data."""
import csv, io, zipfile, bisect
from datetime import date,datetime
from decimal import Decimal, localcontext, ROUND_HALF_UP
from collections import defaultdict
from pathlib import Path
from converter import month_of, SCALES

ECB_URL='https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist.zip'
PEG_URL='https://u.ae/en/about-the-uae/fact-sheet'
PROVIDER='ECB published daily reference cross rate; AED uses UAE USD peg 3.6725; estimate, not actual billed conversion'

class ECBReferenceRates:
    def __init__(self,path):
        p=Path(path)
        if p.stat().st_size>25*1024*1024:raise ValueError('Rate dataset exceeds limit')
        if p.suffix=='.zip':
            with zipfile.ZipFile(p) as archive:
                candidates=[i for i in archive.infolist() if i.filename.endswith('.csv')]
                if len(candidates)!=1 or candidates[0].file_size>25*1024*1024:raise ValueError('Unexpected ECB archive')
                text=archive.read(candidates[0]).decode('utf-8-sig')
        else:text=p.read_text(encoding='utf-8-sig')
        self.rows={}
        for item in csv.DictReader(io.StringIO(text)):
            day=date.fromisoformat(item['Date'].strip()).isoformat();values={'EUR':Decimal(1)}
            for currency,value in item.items():
                if currency and currency.strip()!='Date' and value and value.strip() not in {'N/A',''}:
                    values[currency.strip()]=Decimal(value.strip())
            self.rows[day]=values
        self.days=sorted(self.rows)
    def cross(self,day,source,target):
        values=self.rows[day]
        if source=='AED':
            if 'USD' not in values:raise ValueError('Missing reference currency')
            denominator=values['USD']*Decimal('3.6725')
        else:denominator=values.get(source)
        numerator=values.get(target)
        if not denominator or not numerator or denominator<=0 or numerator<=0:raise ValueError('Unavailable reference currency')
        with localcontext() as context:
            context.prec=38
            return numerator/denominator
    def dated(self,transaction_day,source,target):
        index=bisect.bisect_right(self.days,transaction_day)-1
        if index<0:raise ValueError('Date is outside reference dataset')
        day=self.days[index]
        if (date.fromisoformat(transaction_day)-date.fromisoformat(day)).days>7:raise ValueError('No sufficiently close published reference day')
        return day,self.cross(day,source,target)
    def monthly(self,month,source,target):
        days=[d for d in self.days if d.startswith(month)]
        if not days:raise ValueError('No published rates for month')
        with localcontext() as context:
            context.prec=38
            mean=sum((self.cross(d,source,target) for d in days),Decimal(0))/len(days)
        return days[-1],mean

def apply_reference_estimates(records,archive_path,options):
    if options.get('fxPolicy')!='userApprovedECBReference':raise ValueError('Explicit reference-rate policy required')
    rates=ECBReferenceRates(archive_path);audit=[]
    for row in records:
        original=row['original'];source=original['currency'];target=options['targetCurrency']
        if source==target:continue
        if row['date']['precision']=='instant':
            from zoneinfo import ZoneInfo
            day=datetime.fromisoformat(row['date']['value'].replace('Z','+00:00')).astimezone(ZoneInfo(options['timeZone'])).date().isoformat()
        else:day=row['date']['value']
        try:
            if row['date']['precision']=='month':rate_day,rate=rates.monthly(day,source,target);policy='periodAverage'
            else:rate_day,rate=rates.dated(day,source,target);policy='userApproved'
            rate=rate.quantize(Decimal('0.000000000001'),rounding=ROUND_HALF_UP)
            with localcontext() as context:
                context.prec=38
                minor=int((Decimal(original['minorUnits'])/10**original['scale']*rate*100).quantize(Decimal(1),rounding=ROUND_HALF_UP))
            if not -(2**63)<=minor<2**63:raise ValueError('Converted amount overflows')
            row['normalization']={'minorUnits':str(minor),'currency':target,'rate':format(rate,'f'),'rateDate':rate_day,'provider':PROVIDER,'policy':policy}
            audit.append({'sourceKey':row['sourceKey'],'sourceCurrency':source,'sourceMinorUnits':original['minorUnits'],'homeCurrency':target,
                'estimatedHomeMinorUnits':str(minor),'rate':format(rate,'f'),'referenceDate':rate_day,'transactionDayOrMonth':day,'policy':policy,
                'provider':PROVIDER,'referenceDataURL':ECB_URL,'pegSourceURL':PEG_URL if source=='AED' else ''})
        except (ValueError, ArithmeticError):
            audit.append({'sourceKey':row['sourceKey'],'sourceCurrency':source,'sourceMinorUnits':original['minorUnits'],'status':'pending reference rate'})
    return audit
