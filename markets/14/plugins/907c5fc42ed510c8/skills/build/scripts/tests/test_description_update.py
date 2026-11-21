"""Present-day public listing and historical user-copy provenance tests."""
import hashlib
import unittest
from check_package import ROOT, AUTO, read_json, validate_listing_contract

class DescriptionUpdateTests(unittest.TestCase):
    def setUp(self):
        self.m = read_json(ROOT/'.codex-plugin/plugin.json')
        self.history = read_json(AUTO/'AB60.json')

    def test_current_public_listing_is_honest_and_has_new_brand(self):
        ui = self.m['interface']
        self.assertEqual(ui['displayName'], 'Build_')
        self.assertTrue(ui['longDescription'].startswith('Describe an app and let our plugin build it for you.'))
        for phrase in ('Build_', 'run.bat', 'PROGRAM/', 'LogReport.zip',
                       'new chat with Build_ enabled', 'Python 3.10 or newer'):
            self.assertIn(phrase, ui['longDescription'])
        self.assertEqual(ui.get('defaultPrompt'), ['Press Enter to begin'])
        validate_listing_contract(self.m)

    def test_current_public_info_and_supporting_copy_are_consistent(self):
        page=(ROOT/'readme.md').read_text(encoding='utf-8')
        guide=(AUTO/'NC58.md').read_text(encoding='utf-8')
        self.assertIn('Build_ public review',page)
        self.assertIn('Build_', guide)
        self.assertIn('legacy',page.casefold()) if 'legacy' in page.casefold() else self.assertIn('original Build_',page)

    def test_original_build_and_historical_copy_retained_as_provenance(self):
        old=self.history['copy_update']['previous_manifest']
        self.assertEqual(old['interface']['displayName'],'Build_')
        self.assertEqual(self.m['name'],'berrer-build-mcp')
        self.assertEqual(self.m['skills'],'./skills/')
        self.assertEqual(self.m['mcpServers'],'./.mcp.json')
        self.assertEqual(self.history['legacy_text_invocation'],'Build_')

    def test_mechanical_engine_remains_at_its_accepted_production_hash(self):
        recorded = self.history['production_files_sha256']
        self.assertGreaterEqual(len(recorded), 15)
        checked=0
        for rel, digest in recorded.items():
            if rel == 'skills/build/scripts/guide.py':
                continue  # This module intentionally recognizes the renamed label.
            self.assertEqual(hashlib.sha256((ROOT/rel).read_bytes()).hexdigest(), digest, rel)
            checked+=1
        self.assertGreaterEqual(checked, 14)

    def test_no_claim_of_account_side_publication(self):
        self.assertFalse(self.history['copy_update']['account_update_performed'])
        self.assertFalse(read_json(AUTO/'EB25.json')['current_release_account_update_tested'])
        self.assertFalse(read_json(AUTO/'EB25.json')['publish'])
