import sys
from pathlib import Path
import unittest
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'scripts'))
from run import run

class OutcomeBundleTests(unittest.TestCase):
    def test_combines_signals_and_requires_review(self):
        result=run({'goal':'Improve close','evidence':[{'id':'e1','source':'report','claim':'14 open'}],'kpis':[{'id':'k','name':'open','value':14,'evidence_ids':['e1']}],'actions':[{'id':'a','title':'Review','evidence_ids':['e1'],'requires_approval':True}]})
        self.assertEqual(result['plugin'],'aivana-outcome-operations');self.assertTrue(result['summary']['approval_required']);self.assertEqual(result['summary']['steps'],1)
    def test_unknown_evidence_rejected(self):
        with self.assertRaises(ValueError): run({'goal':'x','evidence':[{'id':'e','source':'s','claim':'c'}],'actions':[{'id':'a','title':'x','evidence_ids':['missing']}]})
