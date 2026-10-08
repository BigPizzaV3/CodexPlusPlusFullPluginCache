from __future__ import annotations

import copy
import sys
import unittest
from pathlib import Path


SCRIPTS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS_DIR))

import search_catalog
import validate_bundle


class CatalogToolsTest(unittest.TestCase):
    def test_validates_complete_bundle(self) -> None:
        self.assertEqual(validate_bundle.validate(), 29)

    def test_routes_amazon_listing_request(self) -> None:
        matches = search_catalog.search(
            "Optimize this Amazon listing title and bullets",
            limit=1,
        )
        self.assertEqual(matches[0]["code"], "amazon-listing-optimization")

    def test_routes_chinese_tiktok_selection_request(self) -> None:
        matches = search_catalog.search(
            "帮我做 TikTok Shop 美区选品",
            limit=1,
        )
        self.assertEqual(matches[0]["code"], "tiktok-product-selection")

    def test_routes_shopee_keyword_request(self) -> None:
        matches = search_catalog.search(
            "分析虾皮泰国站关键词趋势",
            limit=1,
        )
        self.assertEqual(matches[0]["code"], "shopee-keyword-analysis")

    def test_routes_creator_search_before_outreach(self) -> None:
        matches = search_catalog.search(
            "Find YouTube creators for a skincare campaign",
            limit=1,
        )
        self.assertEqual(matches[0]["code"], "youtube-creator-discovery")

    def test_rejects_duplicate_skill_code(self) -> None:
        payload = copy.deepcopy(validate_bundle.load_catalog())
        payload["skills"][1]["code"] = payload["skills"][0]["code"]
        with self.assertRaisesRegex(ValueError, "Duplicate skill code"):
            validate_bundle.validate_catalog(payload)

    def test_repository_snapshot_cannot_claim_live_publication(self) -> None:
        payload = copy.deepcopy(validate_bundle.load_catalog())
        payload["snapshot"]["publicationVerified"] = True
        with self.assertRaisesRegex(ValueError, "must not claim live publication"):
            validate_bundle.validate_catalog(payload)


if __name__ == "__main__":
    unittest.main()
