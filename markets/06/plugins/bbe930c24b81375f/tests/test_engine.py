import sys
from pathlib import Path
import unittest
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'scripts'))
from run import run

class IncidentBundleTests(unittest.TestCase):
    def test_sanitizes_and_groups(self):
        result=run({'incidents':[{'id':'e1','message':'Request 123 failed for demo@example.invalid','request':{'method':'GET','path':'/x?token=a'},'expected_response':{'status':500}}]})
        self.assertEqual(result['summary']['fixtures'],1);self.assertIn('[REDACTED_EMAIL]',result['groups'][0]['signature']);self.assertEqual(result['status'],'analyzed')
    def test_migration_review_is_finding(self):
        result=run({'incidents':[{'id':'e1','message':'failure'}],'migration_checks':[{'id':'m','title':'FK mapping','status':'needs_review','evidence_ids':['e1']}]})
        self.assertTrue(result['approval_required']);self.assertEqual(result['status'],'needs_review')
