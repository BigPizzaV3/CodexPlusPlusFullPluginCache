"""Public ZIP metadata and immutable runtime regression tests (local, not portal tests)."""
import copy
import hashlib
import unittest
from check_package import ROOT, AUTO, read_json, validate_listing_contract, validate_guidance_contract

class PublicSubmissionTests(unittest.TestCase):
    def setUp(self):
        self.m=read_json(ROOT/'.codex-plugin/plugin.json')

    def test_submission_metadata_is_consistent(self):
        self.assertEqual(self.m['name'],'berrer-build-mcp')
        self.assertEqual(self.m['version'],'0.8.6')
        self.assertEqual(self.m['author']['name'],'Richard Dawson')
        self.assertEqual(self.m['author']['email'],'berrergates@gmail.com')
        self.assertEqual(self.m['homepage'],'https://build.berrergate.com/')
        self.assertEqual(self.m['interface']['developerName'],'Richard Dawson')
        self.assertLessEqual(len(self.m['interface']['shortDescription']),30)
        self.assertTrue(validate_listing_contract(self.m)['public_directory_subtitle_ready'])
        self.assertEqual(validate_guidance_contract(ROOT,self.m)['onboarding_skill'],
                         './skills/build-start/SKILL.md')
        self.assertEqual(self.m['mcpServers'],'./.mcp.json')
        self.assertEqual(self.m['interface'].get('defaultPrompt'), ['Press Enter to begin'])

    def test_missing_public_url_is_rejected(self):
        for name in ('websiteURL','supportURL','privacyPolicyURL','termsOfServiceURL'):
            m=copy.deepcopy(self.m)
            m['interface'].pop(name)
            with self.subTest(name=name), self.assertRaises(ValueError):
                validate_listing_contract(m)

    def test_current_engine_matches_recorded_release_inventory(self):
        inventory=read_json(AUTO/'AB60.json')['production_files_sha256']
        for rel,sha in inventory.items():
            with self.subTest(path=rel):
                self.assertEqual(hashlib.sha256((ROOT/rel).read_bytes()).hexdigest(),sha)
