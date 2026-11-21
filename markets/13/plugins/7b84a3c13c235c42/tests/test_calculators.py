import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
def load(slug, name):
    spec = importlib.util.spec_from_file_location(name, ROOT/'skills'/slug/'scripts'/(name+'.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
budget = load('plan-budget', 'budget')
overlap = load('coordinate-hours', 'overlap')

class BudgetTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((ROOT/'skills/plan-budget/assets/example-input.json').read_text())
    def test_known_cash_flow(self):
        result = budget.calculate(self.data)
        self.assertEqual(result['trip_spending'], '2000.00')
        self.assertEqual(result['contingency'], '200.00')
        self.assertEqual(result['total_cash_needed'], '3700.00')
        self.assertEqual(result['cash_headroom'], '300.00')
    def test_shortfall(self):
        self.data['target'] = 3500
        self.assertEqual(budget.calculate(self.data)['cash_headroom'], '-200.00')
    def test_prorating_disclosed(self):
        self.data['nights'] = 15
        result = budget.calculate(self.data)
        self.assertEqual(result['trip_spending'], '1150.00')
        self.assertTrue(any('nights / 30' in x for x in result['notes']))
    def test_no_rate_inference(self):
        self.data['rates'] = {}
        with self.assertRaisesRegex(ValueError, 'missing explicit'): budget.calculate(self.data)
    def test_no_negative_or_nonfinite_money(self):
        for value in ['NaN', 'Infinity', '-1', True, None, {}]:
            with self.subTest(value=value):
                self.data['reserve'] = value
                with self.assertRaises(ValueError): budget.calculate(self.data)
    def test_bad_rates(self):
        for rates in [{'USD':2}, {'EUR':0}, {'EUR':'NaN'}]:
            self.data['rates'] = rates
            with self.assertRaises(ValueError): budget.calculate(self.data)
    def test_nights_strict(self):
        for value in [0, -1, 1.5, True, 3661]:
            self.data['nights'] = value
            with self.assertRaises(ValueError): budget.calculate(self.data)
    def test_deposit_cannot_recur(self):
        self.data['items'][-1]['basis'] = 'night'
        with self.assertRaises(ValueError): budget.calculate(self.data)
    def test_unknown_fields_rejected(self):
        self.data['contigency_percent'] = 99
        with self.assertRaises(ValueError): budget.calculate(self.data)
    def test_malformed_item_categories(self):
        for key in ['basis', 'kind']:
            data = copy.deepcopy(self.data)
            data['items'][0][key] = []
            with self.assertRaisesRegex(ValueError, 'basis or kind'): budget.calculate(data)
    def test_rounding_half_up(self):
        self.data['items'] = [{'label':'Tiny','amount':'1.005','currency':'USD','basis':'stay','kind':'one_time'}]
        self.assertEqual(budget.calculate(self.data)['trip_spending'],'1.01')
    def test_cli_success(self):
        result=subprocess.run([sys.executable,str(ROOT/'skills/plan-budget/scripts/budget.py'),str(ROOT/'skills/plan-budget/assets/example-input.json')],capture_output=True,text=True)
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertEqual(json.loads(result.stdout)['total_cash_needed'],'3700.00')

class OverlapTests(unittest.TestCase):
    def data(self, day='2026-10-23', end=None):
        return {'start_date':day,'end_date':end or day,'anchor':'Traveler','minimum_minutes':60,'participants':[{'name':'Traveler','zone':'Europe/Rome','start':'09:00','end':'18:00'},{'name':'Team','zone':'America/Chicago','start':'09:00','end':'17:00'}]}
    def test_europe_us_dst_mismatch(self):
        for day,minutes,hour in [('2026-10-23',120,'16:00'),('2026-10-26',180,'15:00'),('2026-11-02',120,'16:00')]:
            with self.subTest(day=day):
                result=overlap.calculate(self.data(day))['days'][0]['windows'][0]
                self.assertEqual(result['minutes'],minutes)
                self.assertIn(hour,result['start']['local']['Traveler'])
    def test_weekend_empty(self):
        result=overlap.calculate(self.data('2026-10-24'))['days'][0]
        self.assertEqual(result['windows'],[])
        self.assertFalse(result['has_sufficient_overlap'])
    def test_no_overlap(self):
        data=self.data();data['participants'][0]['end']='10:00'
        self.assertEqual(overlap.calculate(data)['days'][0]['windows'],[])
    def test_minimum_is_enforced(self):
        data=self.data();data['minimum_minutes']=121
        result=overlap.calculate(data)['days'][0]
        self.assertEqual(result['windows'][0]['minutes'],120)
        self.assertFalse(result['has_sufficient_overlap'])
    def test_overnight_date_change(self):
        data=self.data('2026-10-23')
        data['participants']=[{'name':'Traveler','zone':'UTC','start':'22:00','end':'02:00','weekdays':[4]}, {'name':'Team','zone':'Asia/Tokyo','start':'08:00','end':'12:00','weekdays':[5]}]
        result=overlap.calculate(data)['days'][0]['windows'][0]
        self.assertEqual(result['minutes'],180)
        self.assertEqual(result['start']['local']['Team'],'2026-10-24T08:00:00+09:00')
    def test_half_hour_offset(self):
        data=self.data();data['participants']=[{'name':'Traveler','zone':'Asia/Kolkata','start':'09:00','end':'18:00'},{'name':'Team','zone':'UTC','start':'09:00','end':'17:00'}]
        self.assertEqual(overlap.calculate(data)['days'][0]['windows'][0]['minutes'],210)
    def test_spring_nonexistent_boundary(self):
        data=self.data('2026-03-08');data['participants']=[{'name':'Traveler','zone':'America/New_York','start':'02:30','end':'04:00','weekdays':[6]}, {'name':'Team','zone':'UTC','start':'00:00','end':'23:59','weekdays':[6]}]
        with self.assertRaisesRegex(ValueError,'ambiguous or nonexistent'):overlap.calculate(data)
    def test_fall_ambiguous_boundary(self):
        data=self.data('2026-11-01');data['participants']=[{'name':'Traveler','zone':'America/New_York','start':'01:30','end':'04:00','weekdays':[6]}, {'name':'Team','zone':'UTC','start':'00:00','end':'23:59','weekdays':[6]}]
        with self.assertRaisesRegex(ValueError,'ambiguous or nonexistent'):overlap.calculate(data)
    def test_elapsed_time_across_clock_change(self):
        for day,minutes in [('2026-03-08',180),('2026-11-01',300)]:
            data=self.data(day);data['participants']=[{'name':'Traveler','zone':'America/New_York','start':'00:00','end':'04:00','weekdays':[6]}, {'name':'Team','zone':'UTC','start':'00:00','end':'23:59','weekdays':[6]}]
            self.assertEqual(overlap.calculate(data)['days'][0]['windows'][0]['minutes'],minutes)
    def test_equal_times_rejected(self):
        data=self.data();data['participants'][0]['end']='09:00'
        with self.assertRaises(ValueError):overlap.calculate(data)
    def test_duplicate_names_rejected(self):
        data=self.data();data['participants'][1]['name']='Traveler'
        with self.assertRaises(ValueError):overlap.calculate(data)
    def test_range_limit(self):
        with self.assertRaises(ValueError):overlap.calculate(self.data('2026-01-01','2026-12-31'))
    def test_inverted_range(self):
        with self.assertRaises(ValueError):overlap.calculate(self.data('2026-10-25','2026-10-23'))
    def test_invalid_zone(self):
        data=self.data();data['participants'][0]['zone']='Mars/Olympus'
        with self.assertRaises(overlap.ZoneInfoNotFoundError):overlap.calculate(data)
    def test_cli_success(self):
        result=subprocess.run([sys.executable,str(ROOT/'skills/coordinate-hours/scripts/overlap.py'),str(ROOT/'skills/coordinate-hours/assets/example-input.json')],capture_output=True,text=True)
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertEqual(len(json.loads(result.stdout)['days']),11)

if __name__=='__main__': unittest.main()
